#!/usr/bin/env python3
"""Gera todos os decks de Política Internacional como .apkg individuais."""

import hashlib
import json
import os
import random
import shutil
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path

OUT_DIR = Path(__file__).parent / "decks" / "politica-internacional"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Anki schema helpers ──────────────────────────────────────────────────────

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


def _csum(s: str) -> int:
    return int(hashlib.sha1(s.encode()).hexdigest()[:8], 16)


def _make_model(mid: int, name: str) -> dict:
    now = int(time.time())
    return {
        "id": mid, "name": name, "type": 0, "mod": now, "usn": -1,
        "sortf": 0, "did": None, "tmpls": [{
            "name": "Card 1", "ord": 0,
            "qfmt": "{{Frente}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Verso}}",
            "bqfmt": "", "bafmt": "", "did": None, "bfont": "", "bsize": 0,
        }],
        "flds": [
            {"name": "Frente", "ord": 0, "sticky": False, "rtl": False,
             "font": "Arial", "size": 20, "media": []},
            {"name": "Verso",  "ord": 1, "sticky": False, "rtl": False,
             "font": "Arial", "size": 20, "media": []},
        ],
        "css": ".card { font-family: Arial; font-size: 20px; text-align: center; }",
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "tags": [], "vers": [],
    }


def _make_deck(did: int, name: str) -> dict:
    now = int(time.time())
    return {
        "id": did, "name": name, "conf": 1, "extendNew": 10,
        "extendRev": 50, "collapsed": False, "browserCollapsed": False,
        "desc": "", "dyn": 0, "usn": -1, "lrnToday": [0, 0],
        "newToday": [0, 0], "revToday": [0, 0], "timeToday": [0, 0], "mod": now,
    }


def build_apkg(stem: str, deck_name: str, model_name: str,
               cards: list[tuple[str, str]], source_tag: str) -> Path:
    """Build a .apkg and return its path."""
    tmp = Path(tempfile.mkdtemp())
    db_path = tmp / "collection.anki2"

    now = int(time.time())
    mid = abs(hash(model_name)) % (10**13)
    did_default = 1
    did = abs(hash(deck_name)) % (10**13) + 1

    model = _make_model(mid, model_name)
    decks = {
        "1": _make_deck(did_default, "Default"),
        str(did): _make_deck(did, deck_name),
    }

    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    conn.execute(
        "INSERT INTO col VALUES (1,?,?,?,11,0,-1,0,?,?,?,?,'{}')",
        (now, now, now * 1000, COL_CONF,
         json.dumps({str(mid): model}),
         json.dumps(decks),
         DCONF),
    )

    counter = now * 1000
    for i, (front, back) in enumerate(cards):
        counter += 1
        nid = counter
        counter += 1
        cid = counter

        flds = f"{front}\x1f{back}"
        sfld = front
        guid = hashlib.md5(f"{deck_name}:{front}".encode()).hexdigest()[:10]

        conn.execute(
            "INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (nid, guid, mid, now, -1, source_tag, flds, sfld,
             _csum(front), 0, ""),
        )
        conn.execute(
            "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (cid, nid, did, 0, now, -1, 0, 0, i + 1,
             0, 0, 0, 0, 0, 0, 0, 0, ""),
        )

    conn.commit()
    conn.close()

    out = OUT_DIR / f"{stem}.apkg"
    with zipfile.ZipFile(str(out), "w", zipfile.ZIP_DEFLATED) as z:
        z.write(str(db_path), "collection.anki2")
        z.writestr("media", "{}")

    shutil.rmtree(str(tmp))
    print(f"  ✓ {stem}.apkg — {len(cards)} cards")
    return out


# ── Card data ────────────────────────────────────────────────────────────────

DECKS = [

    # ── 1 ────────────────────────────────────────────────────────────────────
    ("fundamentos_ri_paradigmas_pi",
     "CACD :: Política Internacional :: Fundamentos de RI e Paradigmas Teóricos",
     "CACD Política Internacional",
     "PI-I Cap.1 + Nogueira & Messari",
     [
        ("O que distingue o Realismo do Idealismo nas RI?",
         "Para o Realismo, a anarquia internacional e o poder são determinantes; o Idealismo acredita que leis racionais e a opinião pública podem garantir a paz."),
        ("Quais são as premissas comuns ao Realismo?",
         "Estado como ator central; anarquia internacional; ausência de autoridade supranacional; busca da sobrevivência e maximização do poder."),
        ("O que é o Neorrealismo (Realismo Estrutural)?",
         "Corrente de Kenneth Waltz: a estrutura do sistema internacional (distribuição de poder entre Estados) determina o comportamento estatal, independentemente de fatores internos."),
        ("Quais são as premissas centrais do Liberalismo nas RI?",
         "Cooperação internacional é possível; instituições e regimes mitigam a anarquia; democracias tendem à paz; interdependência reduz conflitos."),
        ("O que é interdependência complexa (Keohane & Nye)?",
         "Situação em que múltiplos canais conectam sociedades (não só Estado-Estado), a agenda não tem hierarquia clara e a força militar perde relevância relativa."),
        ("O que é a Economia Política Internacional (EPI)?",
         "Corrente que analisa a interação entre poder político e relações econômicas: como Estados moldam mercados e como mercados condicionam decisões políticas."),
        ("O que caracteriza o Construtivismo nas RI?",
         "A realidade internacional é socialmente construída: identidades, normas e ideias moldam os interesses e o comportamento dos atores — não apenas o poder material."),
        ("Quais são os principais atores das RI além dos Estados?",
         "Organizações internacionais (ONU, OMC), empresas transnacionais, ONGs, movimentos sociais transnacionais e atores subnacionais."),
        ("O que é o conceito de 'anarquia internacional'?",
         "Ausência de autoridade central (governo mundial) acima dos Estados soberanos; cada Estado deve prover sua própria segurança — premissa central do Realismo."),
        ("O que é 'soft power' segundo Joseph Nye?",
         "Capacidade de atrair e co-optar, em vez de coagir: valores, cultura, políticas e diplomacia que levam outros a querer o que você quer."),
        ("O que são 'regimes internacionais'?",
         "Conjunto de princípios, normas, regras e procedimentos de tomada de decisão em torno dos quais convergem as expectativas dos atores em uma área temática."),
        ("O que diferencia teoria e conceituação nas RI, segundo Raymond Aron?",
         "Teoria simplifica um mecanismo-chave para explicar fenômenos; conceitualizações descrevem sem explicar causas. Aron adverte contra construir teorias rígidas de causa/efeito em RI."),
     ]),

    # ── 2 ────────────────────────────────────────────────────────────────────
    ("politica_externa_brasileira_pi",
     "CACD :: Política Internacional :: Política Externa Brasileira desde 1945",
     "CACD Política Internacional",
     "PI-I Cap.2 + Cervo & Bueno",
     [
        ("Quais as duas tendências da política externa brasileira entre 1945 e 1989, segundo Amado Cervo?",
         "Desenvolvimentismo liberal associado (alinhamento ao Ocidente/EUA) vs. nacional-desenvolvimentismo (pragmatismo, universalismo, autonomia estatal nos setores estratégicos)."),
        ("O que foi a Política Externa Independente (PEI)?",
         "Doutrina dos governos Jânio Quadros e João Goulart (1961–64): universalismo, defesa da autodeterminação, apoio à descolonização, diversificação de parceiros sem alinhamento ideológico."),
        ("O que significou o 'alinhamento sem recompensa' no governo Dutra?",
         "O Brasil alinhou-se política e militarmente aos EUA no pós-guerra, mas não obteve contrapartidas econômicas significativas, frustrando expectativas desenvolvimentistas."),
        ("O que foi a Operação Pan-Americana (OPA) e quem a propôs?",
         "Iniciativa do governo JK (1958) que propunha aos EUA um programa multilateral de desenvolvimento para a América Latina, antecipando que a contenção do comunismo exigia combater a miséria."),
        ("O que caracterizou o 'pragmatismo responsável e ecumênico' do governo Geisel?",
         "Diversificação de parcerias (acordos com Alemanha, aproximação com África e Oriente Médio), reconhecimento de Angola, defesa de interesses econômicos sem ruptura ideológica."),
        ("O que foi a 'diplomacia do universalismo' do governo Figueiredo?",
         "Aprofundamento das relações com o Sul Global, ampliação de acordos com países africanos e árabes, maior presença brasileira em foros multilaterais."),
        ("Quais foram os principais eixos da política externa do governo Lula (2003–2010)?",
         "Ênfase na cooperação Sul-Sul, criação do IBAS e fortalecimento do BRICS, Rodada Doha na OMC, ativismo em operações de paz (Haiti/MINUSTAH), defesa da reforma da ONU."),
        ("Quais os princípios que regem o Brasil nas relações internacionais (art. 4º CF/1988)?",
         "Independência nacional; prevalência dos DH; autodeterminação dos povos; não intervenção; igualdade entre os Estados; defesa da paz; solução pacífica de conflitos; repúdio ao terrorismo e racismo; cooperação entre os povos; integração latino-americana."),
        ("O que foi o 'princípio da não indiferença' na PEB do governo Lula?",
         "O Brasil não seria indiferente a crises humanitárias, mas interviria por meio de cooperação, mediação e operações de paz — complemento à não intervenção que admite engajamento multilateral."),
        ("O que diferencia 'política de Estado' de 'política de governo' na PEB?",
         "A PEB é política de Estado: tem continuidade e diretrizes estruturais que transcendem governos, ainda que com ênfases distintas — desenvolvimentismo, universalismo ou autonomia permanecem como vetores."),
        ("Qual foi o papel do Brasil na criação e funcionamento da ONU?",
         "Sócio fundador (1945); primeiro país a discursar na AGNU (tradição mantida); membros no CS em várias ocasiões; presidência da AGNU por Oswaldo Aranha (aprovação do Plano de Partilha da Palestina, 1947)."),
     ]),

    # ── 3 ────────────────────────────────────────────────────────────────────
    ("brasil_america_sul_mercosul_pi",
     "CACD :: Política Internacional :: Brasil, América do Sul e MERCOSUL",
     "CACD Política Internacional",
     "PI-I Cap.3",
     [
        ("O que foi o Pacto do ABC (1915) e qual seu significado?",
         "Tratado entre Argentina, Brasil e Chile para solução pacífica de controvérsias, inspirado por Rio Branco; primeira iniciativa de concertação política sul-americana; não foi ratificado pelo Congresso brasileiro."),
        ("O que foi a ALALC e por que não prosperou?",
         "Associação Latino-Americana de Livre-Comércio (1960): propôs zona de livre comércio em 12 anos; fracassou por resistências nacionais e falta de mecanismos supranacionais. Substituída pela ALADI em 1980."),
        ("O que é a ALADI e como difere da ALALC?",
         "Associação Latino-Americana de Integração (1980): substituiu a ALALC com flexibilidade — acordos parciais são permitidos entre subgrupos de países, sem exigir integração simultânea de todos."),
        ("Como surgiu o MERCOSUL?",
         "Do processo de aproximação Argentina-Brasil iniciado com a Declaração de Iguaçu (1985) e os ACE's; formalizado pelo Tratado de Assunção (1991) com Brasil, Argentina, Uruguai e Paraguai."),
        ("Quais os objetivos originais do MERCOSUL (Tratado de Assunção, 1991)?",
         "Livre circulação de bens, serviços e fatores produtivos; Tarifa Externa Comum; política comercial comum; coordenação de políticas macroeconômicas; harmonização legislativa."),
        ("Qual o estágio atual do MERCOSUL e quais os principais desafios?",
         "União aduaneira incompleta: TEC com muitas exceções; livre circulação de pessoas limitada; assimetrias entre membros; tensões políticas; dificuldades de negociação do acordo com a UE."),
        ("O que é a IIRSA / COSIPLAN?",
         "Iniciativa para a Integração da Infraestrutura Regional Sul-Americana (2000), depois integrada à UNASUL como Conselho Sul-Americano de Infraestrutura e Planejamento; foca em integração física: transporte, energia e comunicações."),
        ("O que foi a UNASUL e quais seus objetivos?",
         "União de Nações Sul-Americanas (2008): foro político de 12 países sul-americanos; objetivos de integração política, social, econômica, ambiental e de defesa; enfraquecida por crises políticas regionais pós-2018."),
        ("O que é o Conselho de Defesa Sul-Americano (CDS)?",
         "Órgão da UNASUL criado em 2008: promove cooperação em defesa, confiança mútua e identidade sul-americana em segurança; não é aliança militar coletiva, mas fórum de diálogo."),
        ("Qual foi o papel da CEPAL na integração regional?",
         "Forneceu base teórica (deterioração dos termos de troca, ISI) e apoiou a ALALC; defendia que a integração regional ampliaria escalas produtivas e reduziria dependência dos países centrais."),
        ("O que é o 'regionalismo aberto' e como se aplica ao MERCOSUL?",
         "Integração regional compatível com a abertura ao comércio global (não proteccionismo fechado); o MERCOSUL segue esse princípio ao manter TEC com terceiros e negociar acordos externos (UE, OMC)."),
     ]),

    # ── 4 ────────────────────────────────────────────────────────────────────
    ("relacoes_bilaterais_americas_pi",
     "CACD :: Política Internacional :: Relações Bilaterais nas Américas",
     "CACD Política Internacional",
     "PI-II Caps.5.5 + 6.2",
     [
        ("Qual era a rivalidade histórica entre Brasil e Argentina e como foi superada?",
         "Competição geopolítica e corrida armamentista até os anos 1970; superada pela Declaração de Iguaçu (1985), acordos de cooperação nuclear e pelo MERCOSUL (1991), transformando rivalidade em parceria estratégica."),
        ("O que foi o 'Espírito de Uruguaiana' (1961)?",
         "Reunião entre Quadros e Frondizi que inaugurou entendimento argentino-brasileiro na PEI: coordenação de políticas externas autônomas, sem alinhamento automático ao EUA ou à URSS."),
        ("Como evoluiu a relação Brasil-Argentina sob os regimes militares?",
         "Inicial rivalidade (projetos de usinas hidrelétricas, corrida armamentista nuclear); gradual entendimento a partir de 1979 (Acordo Tripartite Itaipu-Corpus); cooperação nuclear civil nos anos 1980."),
        ("Qual foi a natureza das relações Brasil-EUA no pós-Segunda Guerra?",
         "Alinhamento automático no governo Dutra; tentativa de 'barganha' por JK e Vargas; ruptura parcial com a PEI; reaproximação no regime militar (1964–74); oscilações posteriores conforme agenda bilateral."),
        ("O que foi a 'Aliança para o Progresso' e qual o papel do Brasil?",
         "Programa norte-americano (1961) de ajuda ao desenvolvimento na AL para conter o comunismo pós-Cuba; o Brasil foi receptor importante, mas manteve tensões com os EUA sobre autonomia de política econômica."),
        ("Quais os principais contenciosos Brasil-EUA na área comercial?",
         "Subsídios agrícolas norte-americanos (açúcar, algodão, soja); barreiras a produtos brasileiros; disputa do algodão na OMC (vitória do Brasil); questões de propriedade intelectual e acesso a mercados."),
        ("O que representa a OEA para o Brasil e a América Latina?",
         "Organização dos Estados Americanos (1948): principal foro hemisférico político-diplomático; instrumentos como a Carta Democrática Interamericana (2001) e o TIAR; o Brasil usa-a com reservas à hegemonia norte-americana."),
        ("Qual foi a política do Brasil para Cuba após a Revolução de 1959?",
         "JK e a PEI: resistência à expulsão de Cuba da OEA; rompimento de relações em 1964 pelo regime militar; reatamento em 1986; relação cooperativa na era Lula e Dilma."),
        ("O que é o TIAR e qual sua relevância atual?",
         "Tratado Interamericano de Assistência Recíproca (1947): defesa coletiva hemisférica; o Brasil está entre os signatários; importância reduzida no pós-Guerra Fria; reativado simbolicamente por alguns países em 2019."),
        ("Como o Brasil posiciona-se no sistema interamericano em relação aos EUA?",
         "Busca autonomia: defende soberania, não intervenção e solução pacífica de controvérsias; usa a OEA como plataforma, mas recusa subordinação às posições de Washington, especialmente em questões latino-americanas."),
     ]),

    # ── 5 ────────────────────────────────────────────────────────────────────
    ("uniao_europeia_pi",
     "CACD :: Política Internacional :: União Europeia",
     "CACD Política Internacional",
     "PI-II Cap.6.1",
     [
        ("Como surgiu a União Europeia?",
         "Das Comunidades Europeias (CECA 1951, CEE e Euratom 1957); o Tratado de Maastricht (1992) criou a UE com três pilares: Comunidades, PESC e Cooperação Judiciária/Interior."),
        ("Quais os principais tratados fundadores da integração europeia?",
         "Tratado de Paris (CECA, 1951); Tratados de Roma (CEE e Euratom, 1957); Ato Único Europeu (1986); Maastricht (1992); Amsterdã (1997); Nice (2001); Lisboa (2007)."),
        ("Quais são os órgãos principais da UE e suas funções?",
         "Conselho Europeu (direção política); Conselho da UE (legislativo dos Estados); Parlamento Europeu (legislativo eleito); Comissão Europeia (executivo/proposta legislativa); Tribunal de Justiça (jurisdição)."),
        ("O que é a Política Externa e de Segurança Comum (PESC) da UE?",
         "Pilar de política externa da UE (desde Maastricht): coordenação das posições dos Estados-membros; representada pelo Alto Representante; limitada pela unanimidade e soberania dos membros."),
        ("Qual é o estado atual das relações Brasil-UE?",
         "Parceria Estratégica desde 2007; principal destino das exportações brasileiras; negociações do acordo Mercosul-UE concluídas em 2019 (aguardando ratificação); cooperação em meio ambiente, DH e comércio."),
        ("O que foi o Acordo-Quadro de Cooperação Brasil-CE (1992)?",
         "Acordo de terceira geração (em vigor desde 1995): contempla comércio, investimentos, finanças e tecnologia; incluiu cláusula democrática como condição para parceria."),
        ("Como o MERCOSUL condicionou as relações Brasil-UE?",
         "A partir do Tratado de Assunção (1991), a UE passou a tratar a AL via Mercosul; em 1995, firmou-se o Acordo Marco Inter-regional Mercosul-UE, base das negociações comerciais."),
        ("Quais os principais pontos de tensão nas relações Brasil-UE?",
         "Política Agrícola Comum (PAC) europeia subsidia produtores, distorcendo concorrência com o agronegócio brasileiro; impasses na negociação do acordo Mercosul-UE sobre acesso a mercados agrícolas."),
        ("Qual é o papel do euro e do Banco Central Europeu?",
         "O euro (desde 1999/2002) é a moeda única de 20 membros da zona euro; o BCE administra a política monetária de forma independente, visando estabilidade de preços."),
        ("O que é o Brexit e quais suas implicações para o Brasil?",
         "Saída do Reino Unido da UE (efetivada em 2020); o Brasil teve de negociar separadamente acordos com o RU; impactou investimentos e fluxos comerciais bilaterais."),
     ]),

    # ── 6 ────────────────────────────────────────────────────────────────────
    ("relacoes_bilaterais_sul_pi",
     "CACD :: Política Internacional :: Relações Bilaterais com o Sul Global",
     "CACD Política Internacional",
     "PI-II Caps.5.1–5.4",
     [
        ("Como evoluíram as relações Brasil-África da PEI ao governo Lula?",
         "PEI: redescoberta da África, abertura de embaixadas. Pragmatismo responsável: comércio, diversificação energética (Angola, Nigéria). Governo Lula: explosão de parcerias, abertura de embaixadas, cooperação técnica, CPLP."),
        ("Por que a Crise do Petróleo de 1973 foi divisora de águas para a PEB com o Oriente Médio?",
         "O Brasil importava ~40% de seu petróleo; o choque triplicou custos. Geisel adotou a 'Diplomacia do Petróleo': aproximou-se dos países árabes, diversificou fontes, abriu embaixadas no Golfo."),
        ("Qual foi a posição tradicional do Brasil na questão israelopalestina?",
         "Equidistância histórica; em 1947, presidiu votação do Plano de Partilha. Em 1973–1980, aproximação dos árabes por razões energéticas; retorno gradual à equidistância nos anos 1990; tentativa de mediação Lula (2010)."),
        ("O que foi a 'Diplomacia do Petróleo' do governo Geisel?",
         "Política de diversificação de parcerias com países árabes para garantir fornecimento de petróleo; apoio a resoluções da ONU favoráveis à causa palestina; voto a favor da Resolução 3.379 (1975, sionismo = racismo)."),
        ("Quais os principais eixos das relações Brasil-China?",
         "Parceria estratégica (1993); China é o principal parceiro comercial do Brasil desde 2009; cooperação em tecnologia (satélites CBERS); tensões por pauta de comércio concentrada em commodities."),
        ("O que marcou o início das relações Brasil-Japão?",
         "Imigração japonesa ao Brasil (1908); após a WWII, Tratado de Paz (1952); joint ventures estratégicas (Usiminas, CENIBRA, ALBRAS); transferência de tecnologia e investimentos japoneses no milagre econômico."),
        ("Quais são os pilares das relações Brasil-Índia?",
         "Convergência em foros multilaterais (G-20 agrícola, IBAS); cooperação em biotecnologia e software; parceria estratégica (2006); posições comuns na reforma da ONU e do Conselho de Segurança."),
        ("Como evoluíram as relações Brasil-Rússia da Guerra Fria ao século XXI?",
         "Ruptura (1947-1961) por alinhamento aos EUA; reatamento com a PEI (1961); comércio durante o regime militar; Parceria Estratégica (2002); cooperação no BRICS; oscilações após invasão da Ucrânia (2022)."),
        ("O que caracterizou a política africana do governo Lula (2003–2010)?",
         "Abertura de 19 embaixadas em África; cooperação técnica (embrapa, fiocruz); cancelamento/reestruturação de dívidas; fortalecimento da CPLP; liderança da MINUSTAH no Haiti."),
        ("Qual foi a posição do Brasil na Guerra do Iraque (2003)?",
         "O Brasil recusou apoiar a invasão norte-americana, considerando que o uso da força contrariava as decisões multilaterais da ONU; defendeu o esgotamento dos meios pacíficos e das inspeções da ONU."),
     ]),

    # ── 7 ────────────────────────────────────────────────────────────────────
    ("agenda_multilateral_pi",
     "CACD :: Política Internacional :: Agenda Multilateral e ONU",
     "CACD Política Internacional",
     "PI-II Cap.7 + fontes múltiplas",
     [
        ("O que foi a Conferência de Estocolmo (1972) e qual foi a posição do Brasil?",
         "Primeira grande conferência ambiental global; o Brasil (sob o regime militar) defendeu soberania nacional sobre recursos e o direito ao desenvolvimento, opondo-se ao 'crescimento zero' dos países ricos."),
        ("O que é desenvolvimento sustentável e qual foi sua origem no multilateralismo?",
         "Conceito consagrado pelo Relatório Brundtland (1987): satisfazer necessidades do presente sem comprometer gerações futuras. Entrou na agenda da ONU e foi central na CNUMAD (Rio 1992)."),
        ("O que foi a Rio-92 (CNUMAD) e quais seus resultados?",
         "Conferência da ONU sobre Meio Ambiente e Desenvolvimento (1992): produziu a Agenda 21, a Convenção-Quadro sobre Mudanças Climáticas (UNFCCC), a Convenção da Biodiversidade e a Declaração do Rio."),
        ("Quais são os principais instrumentos do regime internacional de DH?",
         "Carta da ONU (1945); Declaração Universal dos DH (1948); Pacto de Direitos Civis e Políticos e Pacto de Direitos Econômicos, Sociais e Culturais (1966); Convenção Americana (Pacto de São José, 1969)."),
        ("O que é o Conselho de Direitos Humanos da ONU (CDH) e como funciona?",
         "Órgão subsidiário da AGNU (criado em 2006, substituindo a Comissão); 47 membros eleitos por 3 anos; analisa situações de DH; inclui Revisão Periódica Universal (RPU) — mecanismo proposto pelo Brasil."),
        ("Quais são os princípios fundamentais dos DH consagrados nas Conferências de Teerã (1968) e Viena (1993)?",
         "Universalidade, indivisibilidade, inter-relação e interdependência dos DH; o Brasil apoiou o universalismo em detrimento do relativismo cultural."),
        ("O que é a Responsabilidade de Proteger (R2P)?",
         "Norma adotada na Cúpula da ONU (2005): os Estados têm responsabilidade de proteger suas populações do genocídio, crimes de guerra, limpeza étnica e crimes contra a humanidade; se falharem, a comunidade internacional pode intervir."),
        ("O que são as operações de paz da ONU e qual o papel do Brasil?",
         "Missões autorizadas pelo Conselho de Segurança para estabilizar conflitos; o Brasil liderou o componente militar da MINUSTAH (Haiti, 2004–2017) — maior participação histórica em operações de paz."),
        ("Quais as instâncias da ONU para questões de segurança?",
         "Conselho de Segurança (15 membros; 5 permanentes com veto: EUA, RU, França, Rússia, China); Assembleia Geral; Secretariado; a Resolução 'Unidos pela Paz' permite à AGNU agir quando o CS está paralisado."),
        ("O que é o princípio da não indiferença na PEB?",
         "Complemento à não intervenção: o Brasil não seria indiferente a graves crises humanitárias; engaja-se via cooperação, mediação e operações de paz, sem recorrer à força unilateral."),
        ("Qual é a posição do Brasil sobre a reforma do Conselho de Segurança da ONU?",
         "O Brasil defende a expansão do CS, inclusive com novos membros permanentes (candidatura própria como representante da América do Sul), tornando-o mais representativo e legítimo."),
     ]),

    # ── 8 ────────────────────────────────────────────────────────────────────
    ("omc_comercio_internacional_pi",
     "CACD :: Política Internacional :: OMC e Comércio Internacional",
     "CACD Política Internacional",
     "PI-II Cap.8",
     [
        ("Como surgiu o GATT e o que ele regula?",
         "General Agreement on Tariffs and Trade (1947): acordo multilateral para liberalização do comércio de bens; surgiu porque a OIC (Conf. de Havana) não foi criada; funcionou sem personalidade jurídica até 1994."),
        ("O que é a OMC e quando foi criada?",
         "Organização Mundial do Comércio: criada pela Ata de Marrakesh (1994), entrou em vigor em 1º jan 1995; personalidade jurídica; cobre bens (GATT-94), serviços (GATS) e propriedade intelectual (TRIPS)."),
        ("O que é o princípio do single undertaking na OMC?",
         "Ao aderir à OMC, o país vincula-se automaticamente a todos os acordos multilaterais (Anexos 1, 2 e 3); nada está acordado até tudo estar acordado — vale para rodadas de negociação."),
        ("O que é a cláusula da Nação Mais Favorecida (NMF)?",
         "Art. I GATT: qualquer vantagem concedida a um país deve ser imediata e incondicionalmente estendida a todos os demais membros da OMC — base do princípio da não discriminação."),
        ("O que é o tratamento nacional na OMC?",
         "Art. III GATT: produtos importados não podem ser tratados de forma menos favorável que os produtos nacionais em questões de tributação interna e regulação — não discriminação interna."),
        ("Quais foram as principais rodadas de negociação do GATT/OMC?",
         "Kennedy (1964–67): antidumping. Tóquio (1973–79): barreiras não tarifárias. Uruguai (1986–94): criação da OMC, agricultura, serviços, TRIPS. Doha (2001–): desenvolvimento, em impasse."),
        ("O que é o Sistema de Solução de Controvérsias (SSC) da OMC?",
         "Mecanismo vinculante: painel de árbitros analisa disputas; relatório aprovado pelo Órgão de Solução de Controvérsias (OSC); permite retaliação autorizada — diferente do GATT onde era consenso."),
        ("Como o Brasil usa o SSC da OMC?",
         "Um dos mais ativos usuários: vitórias contra os EUA (algodão — caso que obrigou compensação), UE e outros em disputas sobre açúcar, aviação (Embraer) e outros setores."),
        ("O que é o G-20 agrícola e qual o papel do Brasil?",
         "Coalizão de países em desenvolvimento criada em Cancún (2003) para negociar redução de subsídios agrícolas dos países ricos na Rodada Doha; Brasil e Índia lideraram a coalizão."),
        ("Quais os princípios do Sistema Geral de Preferências (SGP)?",
         "Permite que países desenvolvidos concedam preferências tarifárias a países em desenvolvimento sem reciprocidade — derroga a NMF; aprovado na UNCTAD (1968) e incorporado ao GATT."),
        ("O que é a Rodada Doha e por que está em impasse?",
         "Rodada de Desenvolvimento lançada em 2001: visa reduzir barreiras ao comércio de países em desenvolvimento; bloqueada por divergências entre países desenvolvidos e emergentes sobre agricultura e indústria."),
     ]),

    # ── 9 ────────────────────────────────────────────────────────────────────
    ("cooperacao_sul_sul_cplp_pi",
     "CACD :: Política Internacional :: Cooperação Sul-Sul e CPLP",
     "CACD Política Internacional",
     "PI-II Cap.9",
     [
        ("O que é a Cooperação Sul-Sul (CSS) e como difere da cooperação Norte-Sul?",
         "CSS é cooperação entre países em desenvolvimento (horizontal, baseada em experiências similares); Norte-Sul é cooperação de países desenvolvidos para subdesenvolvidos (vertical, geralmente condicional)."),
        ("O que é a CTPD e qual é a base jurídica da CSS no âmbito da ONU?",
         "Cooperação Técnica entre Países em Desenvolvimento; baseada no Cap. IX da Carta da ONU e no Plano de Ação de Buenos Aires (1978), que definiu objetivos e recomendações para a CTPD."),
        ("Qual o papel da ABC (Agência Brasileira de Cooperação) na CSS?",
         "A ABC coordena a cooperação técnica recebida e prestada pelo Brasil; trabalha com capacitação, transferência de tecnologia e projetos em saúde, agricultura, educação e segurança pública."),
        ("Quais as principais áreas de cooperação técnica do Brasil com países do Sul?",
         "Agricultura (Embrapa): tecnologias tropicais. Saúde (Fiocruz): produção de medicamentos, combate a doenças. Educação e formação profissional. Biocombustíveis e energia renovável."),
        ("O que é a CPLP e quais seus membros?",
         "Comunidade dos Países de Língua Portuguesa (1996): Angola, Brasil, Cabo Verde, Guiné-Bissau, Guiné Equatorial, Moçambique, Portugal, São Tomé e Príncipe e Timor-Leste; foca em língua, cultura e cooperação."),
        ("Qual é a importância estratégica da CPLP para o Brasil?",
         "Plataforma de aproximação com a África lusófona (PALOP) e Timor-Leste; reforça laços histórico-culturais; amplia inserção multilateral; base da cooperação técnica brasileira em saúde e agricultura."),
        ("O que é a 'Diplomacia da Solidariedade' e qual seu fundamento?",
         "Conceito do governo Lula: o Brasil se engaja em cooperação com países mais pobres não como caridade, mas como expressão de solidariedade e de interesse estratégico em reformar a ordem global."),
        ("Como o Brasil se diferencia dos doadores tradicionais (OCDE) na CSS?",
         "Não impõe condicionalidades políticas; enfatiza transferência de conhecimento e fortalecimento institucional; respeita a soberania do país recipiendário; financia principalmente via cooperação técnica, não AOD."),
        ("Qual foi a atuação do Brasil no Haiti como exemplo de CSS?",
         "Liderança militar da MINUSTAH (2004–2017); cooperação em saúde, infraestrutura e segurança pública; modelo de integração entre componente militar e desenvolvimento — 'princípio da não indiferença'."),
        ("O que é a Cooperação Triangular praticada pelo Brasil?",
         "Modalidade em que o Brasil, com apoio financeiro de um país desenvolvido (Japão, UE) ou organismo internacional, presta cooperação técnica a um terceiro país em desenvolvimento."),
     ]),

    # ── 10 ───────────────────────────────────────────────────────────────────
    ("coalizoes_brics_ibas_g20_pi",
     "CACD :: Política Internacional :: Coalizões — BRICS, IBAS e G-20",
     "CACD Política Internacional",
     "PI-I Cap.4",
     [
        ("O que é o IBAS e quais seus objetivos?",
         "Fórum de Diálogo Índia-Brasil-África do Sul (2003): coalizão de democracias em desenvolvimento nos três continentes; promove cooperação técnica, posições comuns em foros multilaterais e combate à pobreza (Fundo IBAS)."),
        ("O que é o BRICS e como evoluiu institucionalmente?",
         "Brasil, Rússia, Índia, China e África do Sul (desde 2011); do acrônimo analítico (Goldman Sachs, 2001) à coalizão política; cúpulas anuais desde 2009; criou o Novo Banco de Desenvolvimento (NDB) e o Arranjo Contingente de Reservas (ACR) em 2014."),
        ("O que é o Novo Banco de Desenvolvimento (NDB) do BRICS?",
         "Banco multilateral criado em 2015 com sede em Xangai; financia infraestrutura e desenvolvimento sustentável nos países-membros e emergentes; capital inicial de USD 100 bi; alternativa ao FMI e Banco Mundial."),
        ("O que é o G-20 financeiro e qual o papel do Brasil?",
         "Fórum de 20 maiores economias (criado em 1999, cúpulas desde 2008 pós-crise); coordena políticas macroeconômicas, reforma financeira e desenvolvimento global; o Brasil ocupa posição de destaque como economia emergente."),
        ("Como surgiu o G-20 agrícola (comercial) na OMC?",
         "Formado em Cancún (2003) na 5ª Conferência Ministerial da OMC: países em desenvolvimento (Brasil, Índia, China, África do Sul) criaram bloco para pressionar pela redução de subsídios agrícolas dos países ricos na Rodada Doha."),
        ("O que diferencia o IBAS do BRICS como instrumento de política externa?",
         "IBAS: democracias de três continentes, ênfase em cooperação técnica e agenda política; BRICS: maior diversidade política (inclui China e Rússia não-democráticas), peso econômico maior, ênfase em reforma da governança global."),
        ("Quais são as premissas da cooperação Sul-Sul multilateral do Brasil?",
         "Solidariedade terceiro-mundista; reforma das estruturas do sistema internacional; defesa de regras mais justas no comércio e nas finanças; não imposição de condicionalidades; princípio da igualdade soberana."),
        ("O que foi a Conferência de Bandung (1955) e sua relevância para a CSS?",
         "I Conferência Afro-Asiática (Indonésia): 29 países; primeiros princípios de cooperação Sul-Sul; origem da identidade do Terceiro Mundo; antecedeu o Movimento dos Países Não Alinhados (1961)."),
        ("O que é o Movimento dos Países Não Alinhados (MPNA) e qual a relação do Brasil?",
         "Fundado em Belgrado (1961): países que recusavam alinhamento aos blocos da Guerra Fria; o Brasil nunca foi membro formal, mas dialogou com o movimento, especialmente durante a PEI e o pragmatismo responsável."),
        ("Como o BRICS posiciona-se em relação à reforma da governança global?",
         "Defende maior representação dos emergentes no FMI, Banco Mundial e Conselho de Segurança; propõe alternativas ao sistema de Bretton Woods; critica o unilateralismo e defende o multilateralismo."),
        ("O que é a Nova Ordem Econômica Internacional (NOEI) e como o Brasil se posicionou?",
         "Proposta dos anos 1970 (G-77/UNCTAD) para reformar o sistema econômico mundial: termos de troca mais justos, controle sobre recursos naturais, regulação de multinacionais; o Brasil apoiou ativamente a NOEI."),
     ]),
]

# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    total = 0
    results = []

    for stem, deck_name, model_name, source_tag, cards in DECKS:
        path = build_apkg(stem, deck_name, model_name, cards, source_tag)
        total += len(cards)
        results.append((stem, len(cards)))

    print(f"\nTotal: {total} cards em {len(DECKS)} decks")
    print("Decks gerados:")
    for stem, n in results:
        print(f"  {stem}: {n} cards")
