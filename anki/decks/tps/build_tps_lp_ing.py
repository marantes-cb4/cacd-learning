#!/usr/bin/env python3
"""
Build TPS Anki cards for Língua Portuguesa and Língua Inglesa.
Run from any directory; output goes to the same folder as this script.
"""

import json, os, sqlite3, struct, hashlib, tempfile, time, zipfile
from pathlib import Path

# ── APKG builder ────────────────────────────────────────────────────────────

def _csum(fld):
    h = hashlib.sha1(fld.encode()).digest()
    return struct.unpack(">I", h[:4])[0]

SCHEMA = """
CREATE TABLE col (id integer primary key, crt integer not null, mod integer not null, scm integer not null, ver integer not null, dty integer not null, usn integer not null, ls integer not null, conf text not null, models text not null, decks text not null, dconf text not null, tags text not null);
CREATE TABLE notes (id integer primary key, guid text not null, mid integer not null, mod integer not null, usn integer not null, tags text not null, flds text not null, sfld integer not null, csum integer not null, flags integer not null, data text not null);
CREATE TABLE cards (id integer primary key, nid integer not null, did integer not null, ord integer not null, mod integer not null, usn integer not null, type integer not null, queue integer not null, due integer not null, ivl integer not null, factor integer not null, reps integer not null, lapses integer not null, left integer not null, odue integer not null, odid integer not null, flags integer not null, data text not null);
CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null, ease integer not null, ivl integer not null, lastIvl integer not null, factor integer not null, time integer not null, type integer not null);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn ON notes (usn); CREATE INDEX ix_cards_usn ON cards (usn); CREATE INDEX ix_revlog_usn ON revlog (usn); CREATE INDEX ix_cards_nid ON cards (nid); CREATE INDEX ix_cards_sched ON cards (did, queue, due); CREATE INDEX ix_revlog_cid ON revlog (cid); CREATE INDEX ix_notes_csum ON notes (csum);
"""

def build_apkg(out_path, deck_name, cards_list):
    now = int(time.time())
    mid = now; did = now + 1; counter = now * 1000 + 2
    model = {str(mid): {"id": mid, "name": "CACD TPS", "type": 0, "mod": now, "usn": -1, "sortf": 0, "did": did,
        "tmpls": [{"name": "Card 1", "ord": 0, "qfmt": "{{Frente}}", "afmt": "{{FrontSide}}<hr>{{Verso}}",
                   "bqfmt": "", "bafmt": "", "did": None, "bfont": "", "bsize": 0}],
        "flds": [{"name": "Frente", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
                 {"name": "Verso", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []}],
        "css": ".card{font-family:Arial;font-size:18px}",
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}", "req": [[0, "any", [0]]], "tags": [], "vers": []}}
    deck = {str(did): {"id": did, "name": deck_name, "conf": 1, "extendNew": 10, "extendRev": 50,
        "collapsed": False, "browserCollapsed": False, "desc": "", "dyn": 0, "usn": -1,
        "lrnToday": [0,0], "newToday": [0,0], "revToday": [0,0], "timeToday": [0,0], "mod": now},
        "1": {"id": 1, "name": "Default", "conf": 1, "extendNew": 10, "extendRev": 50,
        "collapsed": False, "browserCollapsed": False, "desc": "", "dyn": 0, "usn": -1,
        "lrnToday": [0,0], "newToday": [0,0], "revToday": [0,0], "timeToday": [0,0], "mod": now}}
    dconf = {"1": {"id": 1, "mod": 0, "name": "Default", "usn": 0, "autoplay": True, "timer": 0,
        "replayq": True, "maxTaken": 60,
        "new": {"bury": True, "delays": [1,10], "initialFactor": 2500, "ints": [1,4,7], "order": 1, "perDay": 20, "separate": True},
        "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8, "minInt": 1, "mult": 0},
        "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "minSpace": 1, "perDay": 100},
        "dyn": False}}
    conf = json.dumps({"nextPos":1,"estTimes":True,"activeDecks":[1],"sortType":"noteFld","timeLim":0,
        "sortBackwards":False,"addToCur":True,"dayLearnFirst":False,"newBury":True,"newSpread":0,
        "dueCounts":True,"rememberLastDeck":True,"collapseTime":1200})
    with tempfile.TemporaryDirectory() as tmp:
        db_path = os.path.join(tmp, "collection.anki2")
        conn = sqlite3.connect(db_path)
        conn.executescript(SCHEMA)
        conn.execute("INSERT INTO col VALUES (1,?,?,?,11,0,-1,0,?,?,?,?,'{}')",
                     (now, now, now*1000, conf, json.dumps(model), json.dumps(deck), json.dumps(dconf)))
        for i, (front, back) in enumerate(cards_list):
            nid = counter + i*2; cid = counter + i*2+1
            guid = f"tps{hash(front) % 100000000:08d}"
            flds = f"{front}\x1f{back}"
            conn.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                         (nid, guid, mid, now, -1, "TPS", flds, front, _csum(front), 0, ""))
            conn.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (cid, nid, did, 0, now, -1, 0, 0, i+1, 0, 0, 0, 0, 0, 0, 0, 0, ""))
        conn.commit(); conn.close()
        with zipfile.ZipFile(str(out_path), "w", zipfile.ZIP_DEFLATED) as z:
            z.write(db_path, "collection.anki2")
            z.writestr("media", "{}")
    print(f"  Saved {out_path} ({len(cards_list)} cards)")


# ── Card definitions: Língua Portuguesa ──────────────────────────────────────

LP_CARDS = [
    # Formatos e bancas
    ("Quais bancas organizaram o TPS de LP e em quais anos?",
     "CEBRASPE: 2015–2018 e 2024–2026; IADES: 2019, 2020, 2022, 2023. — TPS 2015–2026"),

    ("Qual a diferença de formato entre os anos CEBRASPE (2015–2018) e IADES (2019–2023) em LP?",
     "CEBRASPE: questões agrupadas (Q1–Q10), 4 itens cada. IADES: mesma estrutura, mas com foco maior em semântica e discurso. — TPS 2015–2026"),

    ("No formato CEBRASPE a partir de 2024, como estão estruturados os itens de LP?",
     "Itens individuais (1–40), cada um vinculado a um texto-comando precedente — sem agrupamento em questões. — TPS 2024–2026"),

    # Tipos de texto
    ("Qual o perfil dos textos base de LP no TPS?",
     "Ensaios acadêmicos, textos literários clássicos, prosa narrativa do séc. XIX–XX e textos histórico-culturais. Nunca texto jornalístico cotidiano simples. — TPS 2015–2026"),

    ("Quais autores da literatura brasileira aparecem com maior frequência nos textos base de LP?",
     "Machado de Assis, Lima Barreto, Clarice Lispector, Euclides da Cunha, Padre Vieira, Graciliano Ramos, Manoel de Barros. — TPS 2015–2026"),

    ("A partir de que ano o TPS LP passou a incluir textos em grafia histórica (séc. XVII–XIX)?",
     "2019 (IADES) e, de forma mais marcante, 2026 (Padre Vieira, carta de 1654). — TPS 2019, 2026"),

    # Tópicos mais cobrados
    ("Qual o tópico gramatical mais frequente no TPS de LP?",
     "Relações semântico-sintáticas (conectivos, valor lógico de conjunções e preposições) — cobrado em todos os 11 anos. — TPS 2015–2026"),

    ("Concordância verbal com sujeito posposto ou composto aparece em quantos anos do TPS LP?",
     "10 de 11 anos analisados (2015–2026). É o segundo tópico mais recorrente. — TPS 2015–2026"),

    ("A crase diante de pronome possessivo feminino é cobrada com que frequência no TPS LP?",
     "8 anos. Armadilha: itens afirmam que é facultativa diante de possessivo — ERRADO; é obrigatória quando há artigo contraído. — TPS 2015–2026"),

    ("Qual a pegadinha mais recorrente da banca CEBRASPE em itens de reescrita (LP)?",
     "A reescrita parece correta mas altera a ênfase, o foco informacional ou um valor lógico sutil. Critério: correção gramatical E manutenção de sentido. — TPS 2015–2026"),

    ("Como a banca testa pronomes em LP no TPS?",
     "Propõe referente errado para pronome relativo/oblíquo; ou afirma que a retirada do pronome manteria a correção quando cria ambiguidade. — TPS 2015–2026"),

    ("Figuras de linguagem são cobradas com qual frequência e foco em LP?",
     "7 anos. Foco em hipérbato, metáfora, anáfora, sinestesia e pleonasmo — identificação e análise de efeito retórico, nunca definição abstrata. — TPS 2015–2026"),

    # Padrões CORRETO/ERRADO
    ("O que torna um item de LP tipicamente CORRETO (C) no TPS?",
     "Paráfrases fiéis, identificação correta de referente pronominal, substituições sintaticamente equivalentes e com mesmo sentido. — TPS 2015–2026"),

    ("O que torna um item de LP tipicamente ERRADO (E) no TPS?",
     "Distorção do sentido (ampliar/restringir), referente incorreto de pronome, substituição de conectivo que muda o valor lógico, ausência de vírgula obrigatória. — TPS 2015–2026"),

    # Diferenças IADES vs. CEBRASPE
    ("Como o foco dos itens de LP difere entre os anos IADES e CEBRASPE recentes?",
     "IADES (2019–2023): ênfase em semântica, discurso e argumentação. CEBRASPE (2024–2026): ênfase em gramática normativa, reescrita e análise sintática. — TPS 2015–2026"),

    # Recomendações
    ("Qual tipo de texto deve-se praticar para se preparar para LP no TPS?",
     "Ensaios filosóficos, literários e históricos de alta densidade; textos do séc. XIX–XX em grafia original; nunca textos jornalísticos simples. — TPS 2015–2026"),

    ("Quais verbos e construções sintáticas merecem maior atenção no estudo de concordância para o TPS LP?",
     "'Haver' (impessoal), 'fazer' (temporal), 'ser' com predicativo plural e verbos com sujeito posposto — cobrados em 10 dos 11 anos. — TPS 2015–2026"),

    ("Qual a distinção fundamental que a banca testa entre inferência e afirmação explícita em LP?",
     "'Depreende-se' / 'infere-se' = relação implícita; 'o texto afirma' = conteúdo literal. Itens que confundem os dois são tipicamente ERRADOS. — TPS 2015–2026"),

    ("Quais tópicos gramaticais NUNCA foram foco central de questão em LP no TPS?",
     "Fonética/fonologia pura, formação de palavras como tema isolado, análise morfológica sem contexto sintático-semântico. — TPS 2015–2026"),

    ("Qual o padrão do item 'sem prejuízo das informações originais' no TPS LP?",
     "A banca propõe reescrita que parece equivalente mas altera: (a) ênfase, (b) foco informacional ou (c) valor lógico de conectivo. Sempre verificar os três critérios. — TPS 2015–2026"),
]


# ── Card definitions: Língua Inglesa ─────────────────────────────────────────

ING_CARDS = [
    # Formatos e bancas
    ("Quais bancas organizaram o TPS de Inglês e em quais anos?",
     "CEBRASPE: 2015–2018 e 2024–2026 (tarde, itens 32–44 ou ≈34–40). IADES: 2019, 2020, 2022, 2023 (itens 35–43 ou 36–44). — TPS 2015–2026"),

    ("Qual o formato dos itens de Inglês no TPS?",
     "Todos os itens são C/E (right/wrong) — nunca questão de múltipla escolha ou produção textual. — TPS 2015–2026"),

    # Perfil dos textos
    ("Qual é o padrão temático dos textos base em Inglês no TPS?",
     "Diplomacia, relações internacionais, política global, teoria política, história cultural e, mais recentemente, tecnologia/IA. — TPS 2015–2026"),

    ("Cite exemplos de autores/obras usados como textos base em Inglês no TPS.",
     "Edward Said (Orientalismo, 2016); Patrick Deneen (Why Liberalism Failed, 2023); C. P. Snow (Corridors of Power, 2024); Simon Schama (história holandesa, 2022). — TPS 2016–2024"),

    ("Textos sobre mudanças climáticas ou temas ambientais apareceram em Inglês no TPS?",
     "Sim: 2019 (ondas de calor, The Economist style) e 2025 (Revolução Industrial e emissões de CO2). — TPS 2019, 2025"),

    ("Qual é o perfil temático mais frequente dos textos em Inglês no TPS pós-2020?",
     "Diplomacia digital, IA e relações internacionais (2025, 2026), representação feminina em organismos internacionais (2025), cibersegurança (2026). — TPS 2020–2026"),

    # Tópicos mais cobrados
    ("Qual o tópico mais cobrado em Inglês no TPS?",
     "Inferência e interpretação textual ('right/wrong based on text') — presente em todos os 11 anos. — TPS 2015–2026"),

    ("Referência pronominal é cobrada com qual frequência em Inglês no TPS?",
     "11 de 11 anos. Identifique o antecedente de 'it', 'they', 'their', 'which', 'who' em períodos com múltiplos substantivos. — TPS 2015–2026"),

    ("O que testa a banca com itens de 'equivalência lexical' em Inglês?",
     "Se o candidato reconhece o sentido contextual de palavras de alta densidade: 'exacting', 'albeit', 'ephemeral', 'imbued', 'lest', 'transient'. — TPS 2015–2026"),

    ("Como a banca testa conectivos lógicos em Inglês?",
     "Propõe substituição de 'yet', 'albeit', 'lest', 'whereas' por conectivos aparentemente equivalentes; o candidato deve identificar se o valor lógico é preservado. — TPS 2015–2026"),

    # Pegadinhas
    ("Qual a pegadinha mais frequente em itens de inferência em Inglês no TPS?",
     "'It can be inferred' quando a informação NÃO está no texto, ou quando vai além do que o texto permite concluir — esses itens são tipicamente ERRADOS. — TPS 2015–2026"),

    ("Como a banca usa expressões idiomáticas do inglês para criar itens errados?",
     "Propõe o sentido literal de expressões idiomáticas ('die hard', 'dog' como perseguição, 'lie of the land') — o candidato deve conhecer o sentido real. — TPS 2017, 2024"),

    ("O que distingue um item CORRETO de um ERRADO em paráfrase de Inglês no TPS?",
     "CORRETO: mantém sujeito, objeto e relação lógica. ERRADO: muda foco, inverte sujeito/agente ou usa sinônimo de registro diferente. — TPS 2015–2026"),

    ("Por que itens sobre 'omissão de palavra' são armadilhas frequentes em Inglês no TPS?",
     "A omissão parece facultativa, mas elimina um aposto ou cria ambiguidade de referência — ex.: omitir o segundo 'critics' em TPS 2024 tornava o pronome ambíguo. — TPS 2024"),

    # Diferenças IADES vs. CEBRASPE
    ("Como o foco de Inglês difere entre anos IADES (2019–2023) e CEBRASPE recentes (2024–2026)?",
     "IADES: compreensão global e inferência argumentativa. CEBRASPE 2024–2026: análise sintática granular, substituição lexical e equivalência semântica em nível de frase. — TPS 2015–2026"),

    # Recomendações
    ("Quais publicações em inglês cobrem melhor o perfil dos textos do TPS?",
     "The Economist, Foreign Affairs, Survival, The Guardian (internacional), além de excertos de obras acadêmicas de RI e teoria política. — TPS 2015–2026"),

    ("Qual vocabulário acadêmico é prioritário estudar para o TPS de Inglês?",
     "Academic Word List: 'exacting', 'imbued', 'albeit', 'transient', 'ephemeral', 'immanent', 'hubris', 'meritocratic', 'hubris', 'rubric'. — TPS 2015–2026"),

    ("Quais tópicos NUNCA foram cobrados em Inglês no TPS?",
     "Fonética, produção textual, business English, gramática básica sem contexto textual, literatura anglófona como análise estética isolada. — TPS 2015–2026"),

    ("Como identificar a posição do autor em textos de Inglês do TPS?",
     "Observe marcadores: 'argues', 'claims', 'suggests' (posição do autor) vs. 'is said to', 'is reported' (posição de outros). Itens que invertam essa distinção são ERRADOS. — TPS 2015–2026"),

    ("Qual a estratégia correta ao ler textos de Inglês no TPS antes de julgar os itens?",
     "Identificar: (1) tese central; (2) progressão argumentativa; (3) referentes pronominais principais. Só depois julgar item por item. — TPS 2015–2026"),
]


# ── Build both decks ──────────────────────────────────────────────────────────

OUTPUT_DIR = Path(__file__).parent

DECKS = [
    ("tps_lp.apkg",  "CACD :: TPS :: Língua Portuguesa", LP_CARDS),
    ("tps_ing.apkg", "CACD :: TPS :: Língua Inglesa",    ING_CARDS),
]

for fname, deck_name, cards in DECKS:
    out = OUTPUT_DIR / fname
    build_apkg(out, deck_name, cards)
    print(f"  Deck: {deck_name} — {len(cards)} cards")

print(f"\nDone! {len(DECKS)} decks created in {OUTPUT_DIR}")
