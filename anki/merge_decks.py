#!/usr/bin/env python3
"""Merge all .apkg files in /anki/decks/ into a single CACD.apkg.

Deck hierarchy produced:
  CACD
  CACD::direito
  CACD::direito::<topic>
  CACD::economia
  CACD::economia::<topic>
  CACD::historia_brasil
  CACD::historia_brasil::<topic>
  CACD::historia_mundial
  CACD::historia_mundial::<topic>
"""

import json
import os
import re
import shutil
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path

DECKS_DIR = Path(__file__).parent / "decks"
OUTPUT_PATH = DECKS_DIR / "CACD.apkg"

FOLDER_SUBDECKS = {
    "direito": "direito",
    "economia": "economia",
    "historia-br": "historia_brasil",
    "historia-mundial": "historia_mundial",
}

COL_CONF = json.dumps({
    "nextPos": 1, "estTimes": True, "activeDecks": [1],
    "sortType": "noteFld", "timeLim": 0, "sortBackwards": False,
    "addToCur": True, "dayLearnFirst": False, "newBury": True,
    "newSpread": 0, "dueCounts": True, "rememberLastDeck": True,
    "collapseTime": 1200,
})

DCONF = json.dumps({
    "1": {
        "id": 1, "mod": 0, "name": "Default", "usn": 0, "autoplay": True,
        "timer": 0, "replayq": True, "maxTaken": 60,
        "new": {"bury": True, "delays": [1, 10], "initialFactor": 2500,
                "ints": [1, 4, 7], "order": 1, "perDay": 20, "separate": True},
        "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8,
                  "minInt": 1, "mult": 0},
        "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1,
                "maxIvl": 36500, "minSpace": 1, "perDay": 100},
        "dyn": False,
    }
})

SCHEMA = """
CREATE TABLE col (
    id integer primary key, crt integer not null, mod integer not null,
    scm integer not null, ver integer not null, dty integer not null,
    usn integer not null, ls integer not null, conf text not null,
    models text not null, decks text not null, dconf text not null,
    tags text not null
);
CREATE TABLE notes (
    id integer primary key, guid text not null, mid integer not null,
    mod integer not null, usn integer not null, tags text not null,
    flds text not null, sfld integer not null, csum integer not null,
    flags integer not null, data text not null
);
CREATE TABLE cards (
    id integer primary key, nid integer not null, did integer not null,
    ord integer not null, mod integer not null, usn integer not null,
    type integer not null, queue integer not null, due integer not null,
    ivl integer not null, factor integer not null, reps integer not null,
    lapses integer not null, left integer not null, odue integer not null,
    odid integer not null, flags integer not null, data text not null
);
CREATE TABLE revlog (
    id integer primary key, cid integer not null, usn integer not null,
    ease integer not null, ivl integer not null, lastIvl integer not null,
    factor integer not null, time integer not null, type integer not null
);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn ON notes (usn);
CREATE INDEX ix_cards_usn ON cards (usn);
CREATE INDEX ix_revlog_usn ON revlog (usn);
CREATE INDEX ix_cards_nid ON cards (nid);
CREATE INDEX ix_cards_sched ON cards (did, queue, due);
CREATE INDEX ix_revlog_cid ON revlog (cid);
CREATE INDEX ix_notes_csum ON notes (csum);
"""


def make_deck_entry(did: int, name: str) -> dict:
    now = int(time.time())
    return {
        "id": did, "name": name, "conf": 1, "extendNew": 10,
        "extendRev": 50, "collapsed": False, "browserCollapsed": False,
        "desc": "", "dyn": 0, "usn": -1, "lrnToday": [0, 0],
        "newToday": [0, 0], "revToday": [0, 0], "timeToday": [0, 0], "mod": now,
    }


def extract_topic(raw_name: str) -> str:
    """Pull the last segment from 'CACD :: Subj :: Topic' or 'CACD · Subj · Topic'."""
    for sep in [" :: ", " · "]:
        if sep in raw_name:
            return raw_name.split(sep)[-1].strip()
    return raw_name.strip()


class Merger:
    def __init__(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.db_path = self.tmp / "collection.anki2"
        self.media_dir = self.tmp / "media_files"
        self.media_dir.mkdir()

        now = int(time.time())
        self._counter = now * 1000  # monotone ID generator (ms precision)

        conn = sqlite3.connect(str(self.db_path))
        conn.executescript(SCHEMA)
        # Seed with Default deck (Anki requires it)
        default_decks = {"1": make_deck_entry(1, "Default")}
        conn.execute(
            "INSERT INTO col VALUES (1,?,?,?,11,0,-1,0,?,?,?,?,'{}')",
            (now, now, now * 1000, COL_CONF, "{}", json.dumps(default_decks), DCONF),
        )
        conn.commit()
        conn.close()

        self._decks: dict[str, dict] = {"1": make_deck_entry(1, "Default")}
        self._deck_by_name: dict[str, int] = {"Default": 1}
        self._models: dict[str, dict] = {}
        self._model_by_name: dict[str, int] = {}
        self._media: dict[str, str] = {}  # counter_str → filename
        self._media_count = 0

    def _next_id(self) -> int:
        self._counter += 1
        return self._counter

    def _get_or_create_deck(self, name: str) -> int:
        if name in self._deck_by_name:
            return self._deck_by_name[name]
        # Ensure all ancestor decks exist first
        parts = name.split("::")
        for depth in range(1, len(parts)):
            parent = "::".join(parts[:depth])
            if parent not in self._deck_by_name:
                pid = self._next_id()
                self._decks[str(pid)] = make_deck_entry(pid, parent)
                self._deck_by_name[parent] = pid
        did = self._next_id()
        self._decks[str(did)] = make_deck_entry(did, name)
        self._deck_by_name[name] = did
        return did

    def _get_or_create_model(self, model: dict) -> int:
        name = model.get("name", "")
        if name in self._model_by_name:
            return self._model_by_name[name]
        new_mid = self._next_id()
        m = dict(model)
        m["id"] = new_mid
        self._models[str(new_mid)] = m
        self._model_by_name[name] = new_mid
        return new_mid

    def add_apkg(self, path: Path, subfolder: str) -> tuple[int, int]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            with zipfile.ZipFile(str(path)) as z:
                z.extractall(str(tmp_path))

            db = tmp_path / "collection.anki2"
            if not db.exists():
                db = tmp_path / "collection.anki21"
            if not db.exists():
                print(f"    WARNING: no DB in {path.name}")
                return 0, 0

            # Copy media files
            media_json = tmp_path / "media"
            if media_json.exists():
                with open(str(media_json)) as f:
                    old_media = json.load(f)
                for num, filename in old_media.items():
                    src = tmp_path / num
                    if src.exists():
                        key = str(self._media_count)
                        shutil.copy2(str(src), str(self.media_dir / key))
                        self._media[key] = filename
                        self._media_count += 1

            src = sqlite3.connect(str(db))
            row = src.execute("SELECT models, decks FROM col").fetchone()
            src_models = json.loads(row[0])
            src_decks = json.loads(row[1])

            # Build model remapping
            mid_map: dict[int, int] = {}
            for old_mid_str, model in src_models.items():
                mid_map[int(old_mid_str)] = self._get_or_create_model(model)

            # Build deck remapping — skip Default, rename real decks to CACD hierarchy
            did_map: dict[int, int] = {}
            for old_did_str, deck in src_decks.items():
                raw = deck.get("name", "")
                if raw == "Default":
                    did_map[int(old_did_str)] = 1
                    continue
                topic = extract_topic(raw)
                new_name = f"CACD::{subfolder}::{topic}"
                did_map[int(old_did_str)] = self._get_or_create_deck(new_name)

            notes = src.execute(
                "SELECT id,guid,mid,mod,usn,tags,flds,sfld,csum,flags,data FROM notes"
            ).fetchall()
            cards = src.execute(
                "SELECT id,nid,did,ord,mod,usn,type,queue,due,ivl,factor,reps,"
                "lapses,left,odue,odid,flags,data FROM cards"
            ).fetchall()
            src.close()

            dst = sqlite3.connect(str(self.db_path))

            # Insert notes with new IDs
            nid_map: dict[int, int] = {}
            for n in notes:
                old_nid = n[0]
                new_nid = self._next_id()
                nid_map[old_nid] = new_nid
                new_mid = mid_map.get(n[2], n[2])
                dst.execute(
                    "INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (new_nid, n[1], new_mid, n[3], -1, n[5], n[6], n[7], n[8], n[9], n[10]),
                )

            # Insert cards with new IDs
            for c in cards:
                new_cid = self._next_id()
                new_nid = nid_map.get(c[1], c[1])
                new_did = did_map.get(c[2], 1)
                dst.execute(
                    "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (new_cid, new_nid, new_did, c[3], c[4], -1,
                     0, 0, c[8], 0, 0, 0, 0, 0, 0, 0, c[16], c[17]),
                )

            dst.commit()
            dst.close()
            return len(notes), len(cards)

    def save(self, output: Path):
        # Flush accumulated decks and models into the col row
        conn = sqlite3.connect(str(self.db_path))
        conn.execute(
            "UPDATE col SET models=?, decks=? WHERE id=1",
            (json.dumps(self._models), json.dumps(self._decks)),
        )
        conn.commit()
        conn.close()

        with zipfile.ZipFile(str(output), "w", zipfile.ZIP_DEFLATED) as z:
            z.write(str(self.db_path), "collection.anki2")
            for key in self._media:
                src = self.media_dir / key
                if src.exists():
                    z.write(str(src), key)
            z.writestr("media", json.dumps(self._media))

        shutil.rmtree(str(self.tmp))
        print(f"\nSaved → {output}")


def main():
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()

    merger = Merger()
    total_notes = total_cards = 0

    for folder in sorted(DECKS_DIR.iterdir()):
        if not folder.is_dir() or folder.name not in FOLDER_SUBDECKS:
            continue
        subfolder = FOLDER_SUBDECKS[folder.name]
        print(f"\n{folder.name}  →  CACD::{subfolder}")

        for apkg in sorted(folder.glob("*.apkg")):
            n, c = merger.add_apkg(apkg, subfolder)
            print(f"  {apkg.stem}: {n} notes, {c} cards")
            total_notes += n
            total_cards += c

    merger.save(OUTPUT_PATH)
    print(f"\nTotal: {total_notes} notes · {total_cards} cards")

    # Print deck hierarchy
    print("\nDeck hierarchy:")
    for name in sorted(merger._deck_by_name):
        depth = name.count("::")
        print("  " + "  " * depth + name)


if __name__ == "__main__":
    main()
