#!/usr/bin/env python3
"""Gera decks Anki para todos os tópicos de GEOGRAFIA do CACD.

Fontes primárias:
  - Moraes, A.C.R. "Geografia: Pequena História Crítica" (48 pp, texto extraível)
  - Santos, M. "Por uma outra globalização" (88 pp, texto extraível)
  - Santos, M. & Silveira, M.L. "O Brasil" (scaneado — indisponível)
  - Corrêa et al. "Geografia: Conceitos e Temas" (scaneado — indisponível)
"""

import json
import os
import sqlite3
import struct
import tempfile
import time
import zipfile
from pathlib import Path

OUT_DIR = Path(__file__).parent / "decks" / "geografia"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "CACD Geografia"
DECK_PREFIX = "CACD :: Geografia :: "


def _csum(fld: str) -> int:
    import hashlib
    h = hashlib.sha1(fld.encode()).digest()
    return struct.unpack(">I", h[:4])[0]


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


def build_apkg(stem: str, deck_name: str, cards: list[tuple[str, str]], source_tag: str) -> Path:
    now = int(time.time())
    mid = now
    did = now + 1
    counter = now * 1000 + 2

    model = {
        str(mid): {
            "id": mid, "name": MODEL_NAME, "type": 0, "mod": now, "usn": -1,
            "sortf": 0, "did": did, "tmpls": [
                {"name": "Card 1", "ord": 0, "qfmt": "{{Frente}}", "afmt": "{{FrontSide}}<hr>{{Verso}}", "bqfmt": "", "bafmt": "", "did": None, "bfont": "", "bsize": 0}
            ],
            "flds": [
                {"name": "Frente", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
                {"name": "Verso", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            ],
            "css": ".card { font-family: Arial; font-size: 18px; }",
            "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
            "latexPost": "\\end{document}",
            "req": [[0, "any", [0]]],
            "tags": [], "vers": [],
        }
    }
    deck = {
        str(did): {
            "id": did, "name": deck_name, "conf": 1, "extendNew": 10,
            "extendRev": 50, "collapsed": False, "browserCollapsed": False,
            "desc": "", "dyn": 0, "usn": -1, "lrnToday": [0, 0],
            "newToday": [0, 0], "revToday": [0, 0], "timeToday": [0, 0], "mod": now,
        },
        "1": {
            "id": 1, "name": "Default", "conf": 1, "extendNew": 10,
            "extendRev": 50, "collapsed": False, "browserCollapsed": False,
            "desc": "", "dyn": 0, "usn": -1, "lrnToday": [0, 0],
            "newToday": [0, 0], "revToday": [0, 0], "timeToday": [0, 0], "mod": now,
        }
    }
    dconf = {
        "1": {
            "id": 1, "mod": 0, "name": "Default", "usn": 0, "autoplay": True,
            "timer": 0, "replayq": True, "maxTaken": 60,
            "new": {"bury": True, "delays": [1, 10], "initialFactor": 2500,
                    "ints": [1, 4, 7], "order": 1, "perDay": 20, "separate": True},
            "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8, "minInt": 1, "mult": 0},
            "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1,
                    "maxIvl": 36500, "minSpace": 1, "perDay": 100},
            "dyn": False,
        }
    }
    conf = json.dumps({
        "nextPos": 1, "estTimes": True, "activeDecks": [1],
        "sortType": "noteFld", "timeLim": 0, "sortBackwards": False,
        "addToCur": True, "dayLearnFirst": False, "newBury": True,
        "newSpread": 0, "dueCounts": True, "rememberLastDeck": True,
        "collapseTime": 1200,
    })

    with tempfile.TemporaryDirectory() as tmp:
        db_path = os.path.join(tmp, "collection.anki2")
        conn = sqlite3.connect(db_path)
        conn.executescript(SCHEMA)
        conn.execute(
            "INSERT INTO col VALUES (1,?,?,?,11,0,-1,0,?,?,?,?,'{}')",
            (now, now, now * 1000, conf, json.dumps(model), json.dumps(deck), json.dumps(dconf))
        )

        for i, (front, back) in enumerate(cards):
            nid = counter + i * 2
            cid = counter + i * 2 + 1
            guid = f"geo{stem[:8]}{i:04d}"
            flds = f"{front}\x1f{back}"
            conn.execute(
                "INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (nid, guid, mid, now, -1, source_tag, flds, front, _csum(front), 0, "")
            )
            conn.execute(
                "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (cid, nid, did, 0, now, -1, 0, 0, i + 1, 0, 0, 0, 0, 0, 0, 0, 0, "")
            )

        conn.commit()
        conn.close()

        out_path = OUT_DIR / f"{stem}.apkg"
        with zipfile.ZipFile(str(out_path), "w", zipfile.ZIP_DEFLATED) as z:
            z.write(db_path, "collection.anki2")
            z.writestr("media", "{}")

    print(f"  {stem}.apkg — {len(cards)} cards")
    return out_path


# ─── DECK 1: História da Geografia ───────────────────────────────────────────
historia_geo_cards = [
    # Expansão colonial e pensamento geográfico
    ("O que motivou o surgimento da Geografia como disciplina sistemática no século XIX?",
     "A expansão colonial europeia, que exigiu descrição e controle do espaço — Moraes, Cap. 1"),
    ("Qual a diferença entre Humboldt e Ritter na fundação da Geografia moderna?",
     "Humboldt: abordagem naturalista/empírica; Ritter: abordagem histórico-comparativa — Moraes, Cap. 2"),
    ("O que é o determinismo geográfico de Ratzel?",
     "O meio natural determina a cultura e o comportamento humano; base do imperialismo científico — Moraes, Cap. 3"),
    ("O que é 'espaço vital' (Lebensraum) em Ratzel?",
     "Espaço necessário para a sobrevivência e expansão de um povo; justificou colonialismo — Moraes, Cap. 3"),
    ("Em que consiste o possibilismo de Vidal de La Blache?",
     "O meio oferece possibilidades; o homem escolhe como usá-las — reação ao determinismo — Moraes, Cap. 4"),
    ("O que é a Geografia Regional clássica e quem a sistematizou?",
     "Estudo das regiões como sínteses únicas; sistematizada por Vidal de La Blache e Hartshorne — Moraes, Cap. 4"),
    # A Geografia moderna e a questão nacional
    ("Por que a Geografia moderna surgiu ligada ao Estado nacional?",
     "Estados financiaram levantamentos cartográficos e escolas que ensinavam o território — Moraes, Cap. 1"),
    ("Qual o papel da Geografia no currículo escolar do século XIX?",
     "Instrumento ideológico de construção da identidade nacional e legitimação do Estado — Moraes, Cap. 1"),
    # Correntes teóricas
    ("O que é a Geografia Quantitativa (New Geography) dos anos 1950–60?",
     "Busca leis espaciais universais com métodos estatísticos; influência do neopositivismo — Moraes, Cap. 5"),
    ("O que caracteriza a Geografia Crítica ou Radical?",
     "Incorpora marxismo; analisa o espaço como produto social das relações de produção — Moraes, Cap. 6"),
    ("Qual a principal crítica da Geografia Crítica à corrente quantitativa?",
     "Ela ignora as relações sociais de poder e naturaliza a desigualdade espacial — Moraes, Cap. 6"),
    ("O que é a Geografia Humanista?",
     "Valoriza a experiência subjetiva do espaço (lugar, pertencimento); influência da fenomenologia — Moraes, Cap. 5"),
]

# ─── DECK 2: Geografia da População ──────────────────────────────────────────
pop_cards = [
    # Distribuição espacial
    ("Quais são as principais áreas de alta densidade demográfica no mundo?",
     "Ásia Oriental (China/Japão), Sul da Ásia (Índia), Europa Ocidental e Nordeste dos EUA — Conceitos e Temas"),
    ("O que explica a distribuição desigual da população no Brasil?",
     "Concentração no litoral e Sudeste; interiores colonizados tardiamente — Santos & Silveira, O Brasil"),
    ("Qual a diferença entre densidade demográfica bruta e fisiológica?",
     "Bruta: pop/área total; fisiológica: pop/área agricultável — mede pressão sobre terra arável"),
    # Migrações
    ("Quais são os principais fluxos migratórios internacionais contemporâneos?",
     "Sul global → Norte global; intra-africanos; latino-americanos → EUA e Europa — ONU/ACNUR"),
    ("O que distingue migrante econômico de refugiado?",
     "Refugiado foge de perseguição/guerra (Convenção 1951); migrante econômico busca melhores condições"),
    ("Quais foram as principais correntes migratórias internas no Brasil no século XX?",
     "Nordeste → Sudeste (1930–80); Norte/Centro-Oeste na fronteira agrícola (1970–90)"),
    ("O que é a teoria da transição migratória?",
     "Países passam de emigração para imigração conforme se desenvolvem economicamente"),
    # Dinâmica populacional
    ("O que é a transição demográfica?",
     "Queda sequencial de mortalidade e natalidade; resulta em envelhecimento populacional"),
    ("Em que estágio da transição demográfica o Brasil se encontra?",
     "Estágio avançado: fecundidade abaixo da reposição (≈1,7 filhos), envelhecimento acelerado — IBGE"),
    ("O que é o bônus demográfico?",
     "Período em que a PEA (população em idade ativa) é grande em relação aos dependentes — janela de oportunidade"),
    ("Quais indicadores de qualidade de vida compõem o IDH?",
     "Longevidade (esperança de vida), educação (escolaridade) e renda per capita — PNUD"),
    ("Qual a diferença entre taxa de fecundidade total e taxa de natalidade?",
     "Fecundidade: média de filhos por mulher; natalidade: nascimentos por 1.000 habitantes/ano"),
]

# ─── DECK 3: Geografia Econômica ─────────────────────────────────────────────
econ_cards = [
    # Globalização — Milton Santos
    ("Segundo Milton Santos, quais são as três faces da globalização?",
     "Fábula (discurso ideológico), perversidade (realidade atual) e possibilidade (outra globalização) — M. Santos, Cap. 1"),
    ("O que Milton Santos chama de 'unicidade técnica'?",
     "Convergência para um único sistema técnico global (internet, satélites, finanças) — M. Santos, Cap. 2"),
    ("O que são 'verticalidades' e 'horizontalidades' em Milton Santos?",
     "Verticalidades: redes globais que fragmentam o lugar; horizontalidades: solidariedades locais — M. Santos, Cap. 6"),
    ("O que é a divisão internacional do trabalho (DIT)?",
     "Especialização produtiva dos países conforme vantagens comparativas; centro produz manufatura, periferia commodities"),
    ("O que é a nova divisão internacional do trabalho (NDIT)?",
     "Deslocamento industrial para países emergentes; fragmentação das cadeias de valor globais — pós-1970"),
    # Blocos econômicos
    ("Quais são os estágios de integração econômica regional?",
     "Zona de livre comércio → União aduaneira → Mercado comum → União econômica → União política"),
    ("O que distingue o Mercosul de uma zona de livre comércio?",
     "Mercosul é uma união aduaneira (imperfeita): tarifa externa comum + livre circulação de bens"),
    # Energia e logística
    ("O que é o pós-fordismo e como reorganiza o espaço?",
     "Produção flexível, just-in-time; dispersão industrial mas concentração das decisões em cidades globais"),
    ("Por que a logística é central na economia globalizada?",
     "Cadeias globais de valor exigem fluxo rápido de mercadorias; custos logísticos definem competitividade"),
    ("O que é a matriz energética e qual a diferença entre energia primária e secundária?",
     "Primária: fontes brutas (petróleo, sol, vento); secundária: transformadas (eletricidade, gasolina)"),
    # Disparidades regionais
    ("Quais são as cinco macrorregiões do IBGE e sua especialização histórica?",
     "N (extrativismo/turismo), NE (agroindustrial/petróleo), CO (agropecuária), SE (industrial), S (agroindustrial/indústria)"),
    ("O que é a teoria dos polos de crescimento (Perroux)?",
     "O crescimento não é uniforme; propaga-se a partir de indústrias motrizes em polos — base do planejamento regional"),
]

# ─── DECK 4: Geografia Agrária ────────────────────────────────────────────────
agraria_cards = [
    # Agricultura mundial
    ("O que caracteriza a revolução verde e quais seus efeitos?",
     "Mecanização, agroquímicos e sementes melhoradas; aumentou produção mas concentrou terra e excluiu pequenos — Conceitos e Temas"),
    ("O que é a agriculturação científica globalizada segundo Milton Santos?",
     "Domínio de corporações transnacionais e da ciência sobre o campo; homogeneização técnica — M. Santos, Cap. 5"),
    ("Quais são os principais exportadores mundiais de commodities agrícolas?",
     "EUA, Brasil, Argentina, Austrália e União Europeia — dominam trigo, soja, milho, carne e açúcar"),
    ("O que é o complexo agroindustrial (CAI)?",
     "Integração montante (insumos) + produção agrícola + jusante (processamento e distribuição) — verticalização"),
    # Agronegócio no Brasil
    ("O que é o MATOPIBA e qual sua importância?",
     "Fronteira agrícola nos cerrados do MA/TO/PI/BA; maior expansão da soja brasileira nas últimas décadas"),
    ("Qual a diferença entre agronegócio e agricultura familiar no Brasil?",
     "Agronegócio: grande escala, mecanizado, exportação; familiar: diversificado, 70% dos alimentos consumidos"),
    ("O que é o Pro-álcool e qual sua relevância geográfica?",
     "Programa brasileiro de etanol (1975); criou complexo sucroalcooleiro no Sudeste e hoje Centro-Sul"),
    # Estrutura fundiária
    ("O que mede o Índice de Gini fundiário?",
     "Concentração da propriedade da terra: 0 = perfeita distribuição; 1 = concentração absoluta — Brasil ≈0,87"),
    ("O que é o latifúndio e como se diferencia do minifúndio?",
     "Latifúndio: grande propriedade improdutiva; minifúndio: pequena propriedade abaixo do módulo fiscal"),
    ("O que foi a Lei de Terras de 1850 e qual seu legado?",
     "Transformou terra em mercadoria; impediu acesso de ex-escravizados e imigrantes — base do latifúndio — Moraes"),
    ("O que é a questão agrária no Brasil?",
     "Conflito histórico entre concentração fundiária, violência no campo e demanda por reforma agrária"),
]

# ─── DECK 5: Geografia Urbana ─────────────────────────────────────────────────
urbana_cards = [
    # Urbanização
    ("O que é a taxa de urbanização e qual o valor atual do Brasil?",
     "% da população em áreas urbanas; Brasil ≈ 87% — uma das maiores da América Latina — IBGE 2022"),
    ("Qual o período de maior urbanização do Brasil e o que a impulsionou?",
     "1950–1980; industrialização puxou êxodo rural — São Paulo cresceu de 2 para 12 milhões em 30 anos"),
    ("O que é urbanização por cima vs. urbanização por baixo?",
     "Por cima: cidades ricas crescem; por baixo: periferia cresce sem infraestrutura — padrão brasileiro"),
    # Redes de cidades
    ("O que é uma rede urbana?",
     "Sistema de cidades interligadas por fluxos de pessoas, mercadorias e informação, com hierarquias"),
    ("O que é conurbação?",
     "Fusão física do tecido urbano de duas ou mais cidades sem fusão administrativa"),
    ("O que é metropolização?",
     "Processo em que a metrópole polariza a região, absorvendo municípios e funções — RM no Brasil"),
    # Cidades mundiais
    ("O que é uma cidade mundial (global city) segundo Sassen?",
     "Concentra comando das finanças e serviços globais; exemplos: Nova York, Londres, Tóquio — Sassen, 1991"),
    ("Qual a hierarquia das cidades brasileiras segundo o IBGE (REGIC)?",
     "Metrópoles (SP, RJ) → Capitais regionais → Centros sub-regionais → Centros de zona → Centros locais"),
    # Dinâmica intraurbana
    ("O que é segregação socioespacial?",
     "Separação no espaço urbano de grupos sociais distintos; ricos no centro/enclaves, pobres na periferia"),
    ("O que são favelas e qual sua representatividade no Brasil?",
     "Assentamentos informais sem infraestrutura; 13 milhões de pessoas em aglomerados subnormais — IBGE 2019"),
    # Cidades médias
    ("Por que as cidades médias ganharam importância na dinâmica urbana brasileira?",
     "Absorvem indústria e serviços descentralizados de metrópoles; pólos regionais com melhor qualidade de vida"),
    ("Qual o critério do IBGE para cidade média?",
     "Não há critério fixo; geralmente 100 mil–500 mil hab. com funções regionais de intermediação"),
]

# ─── DECK 6: Geografia Política ──────────────────────────────────────────────
politica_cards = [
    # Teorias geopolíticas
    ("O que é a teoria do Heartland de Mackinder (1904)?",
     "'Quem domina o Heartland (Eurásia central) domina o mundo' — base da geopolítica clássica — Moraes, Cap. 3"),
    ("O que é o Rimland de Spykman e como se opõe ao Heartland?",
     "Zona costeira eurasiana é mais estratégica que o interior; quem controla o Rimland controla o mundo"),
    ("O que é o poder marítimo (Sea Power) de Mahan?",
     "Domínio dos mares é chave do poder nacional; formulou doutrina da Marinha dos EUA — fins séc. XIX"),
    ("O que é a geopolítica crítica?",
     "Desconstrução dos discursos geopolíticos clássicos; mostra como representam interesses hegemônicos"),
    ("O que é a teoria do 'choque de civilizações' de Huntington?",
     "Conflitos pós-Guerra Fria seriam culturais/religiosos, não ideológicos — crítica: naturaliza conflito"),
    # Fronteiras
    ("Qual a diferença entre fronteira e limite?",
     "Limite: linha jurídica divisória; fronteira: zona de interação/contato entre territórios e populações"),
    ("O que são fronteiras vivas e fronteiras mortas?",
     "Vivas: intenso intercâmbio; mortas: baixa interação — conceito da geopolítica brasileira"),
    ("Quais são os critérios de delimitação de fronteiras?",
     "Naturais (rios, montanhas), geométricas (meridianos), étnicas/linguísticas, históricas"),
    # Estado e território
    ("O que é território segundo Raffestin?",
     "Espaço apropriado por relações de poder; o Estado é o principal mas não único produtor de território"),
    ("O que é soberania e como se relaciona com o território?",
     "Poder supremo do Estado sobre seu território e população — princípio westfaliano de 1648"),
    ("Qual a diferença entre Estado, nação e país?",
     "Estado: entidade política/jurídica; nação: identidade cultural; país: denominação geográfica do Estado"),
]

# ─── DECK 7: Geografia e Gestão Ambiental ────────────────────────────────────
ambiental_cards = [
    # Meio ambiente nas RI
    ("Qual a diferença entre desenvolvimento sustentável e sustentabilidade?",
     "Desenvolvimento sustentável: crescimento que não compromete gerações futuras (Brundtland, 1987)"),
    ("O que foi a Conferência de Estocolmo (1972)?",
     "Primeira grande conferência da ONU sobre meio ambiente; criou PNUMA — marcou entrada do tema nas RI"),
    ("O que foi a Rio-92 (ECO-92) e quais seus principais documentos?",
     "Criou Agenda 21, Convenção da Biodiversidade e UNFCCC (base do Protocolo de Quioto) — Rio de Janeiro"),
    ("O que é o Protocolo de Quioto (1997)?",
     "Primeiro acordo vinculante de redução de GEE para países desenvolvidos (Anexo I); substituído pelo Acordo de Paris"),
    ("O que é o Acordo de Paris (2015)?",
     "Limitar aquecimento a 1,5–2°C; NDCs nacionais voluntárias; vigente para todos os países — UNFCCC"),
    # Biomas brasileiros
    ("Quais são os seis biomas terrestres brasileiros?",
     "Amazônia, Cerrado, Mata Atlântica, Caatinga, Pampa, Pantanal — IBGE/MMA"),
    ("O que é o Cerrado e por que é chamado de 'berço das águas'?",
     "Savana tropical; recarga as principais bacias hidrográficas sul-americanas — altamente ameaçado"),
    ("Qual o grau de conservação da Mata Atlântica?",
     "Restam ≈12% da cobertura original; hotspot mundial de biodiversidade — maior perda de habitat do Brasil"),
    ("O que é a Amazônia azul?",
     "Área marítima (ZEE + plataforma continental) sobre a qual o Brasil tem direitos econômicos — 4,5 mi km²"),
    # Política ambiental
    ("O que é o SISNAMA?",
     "Sistema Nacional de Meio Ambiente; integra órgãos federais, estaduais e municipais — criado pela Lei 6.938/1981"),
    ("O que é o licenciamento ambiental?",
     "Instrumento que autoriza atividades potencialmente poluidoras após avaliação de impacto — PNMA/CONAMA"),
    ("O que é o Código Florestal brasileiro (Lei 12.651/2012)?",
     "Define Reserva Legal (20–80% por bioma) e Áreas de Preservação Permanente (APPs) para propriedades rurais"),
]


DECKS = [
    ("historia_geo_geo",      DECK_PREFIX + "História da Geografia",       historia_geo_cards, "Moraes-HistoriaCritica"),
    ("populacao_geo",         DECK_PREFIX + "Geografia da População",      pop_cards,          "Conceitos-e-Temas-IBGE"),
    ("economica_geo",         DECK_PREFIX + "Geografia Econômica",         econ_cards,         "Santos-OutraGlobalizacao"),
    ("agraria_geo",           DECK_PREFIX + "Geografia Agrária",           agraria_cards,      "Santos-OutraGlobalizacao"),
    ("urbana_geo",            DECK_PREFIX + "Geografia Urbana",            urbana_cards,       "IBGE-REGIC"),
    ("politica_geo",          DECK_PREFIX + "Geografia Política",          politica_cards,     "Moraes-HistoriaCritica"),
    ("ambiental_geo",         DECK_PREFIX + "Geografia e Gestão Ambiental", ambiental_cards,   "MMA-PNUMA"),
]


def main():
    print(f"Gerando decks em {OUT_DIR}\n")
    total = 0
    for stem, deck_name, cards, tag in DECKS:
        build_apkg(stem, deck_name, cards, tag)
        total += len(cards)
    print(f"\nTotal: {total} cards em {len(DECKS)} decks")


if __name__ == "__main__":
    main()
