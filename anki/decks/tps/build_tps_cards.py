#!/usr/bin/env python3
"""
Build TPS Anki cards for all 6 subjects.
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


# ── Card definitions ─────────────────────────────────────────────────────────

PI_CARDS = [
    # Integração regional
    ("Qual o objetivo principal da UNASUL e quando foi reativada pelo Brasil?",
     "Integração política, social, econômica e cultural sul-americana; reativada em 2023 via decreto. TPS 2015, 2018, 2025"),
    ("Qual a diferença entre cooperação e integração regional no contexto da UNASUL?",
     "Cooperação = ações conjuntas sem cessão de soberania; integração = fusão de mercados/políticas. UNASUL prioriza cooperação. TPS 2015, 2018"),
    ("Quais os princípios do Conselho de Defesa da UNASUL?",
     "Rege-se pelas Cartas da ONU e OEA; respeita soberania, não intervenção e solução pacífica. TPS 2015"),
    ("O que é a IIRSA e como se relaciona com a UNASUL?",
     "Iniciativa brasileira de integração de infraestrutura (2000); incorporada ao COSIPLAN/UNASUL. TPS 2018"),
    ("Qual a distinção entre o MERCOSUL original e sua agenda ampliada?",
     "Criado como mercado comum; incorporou temas não econômicos na fase de transição, dificultando consolidação. TPS 2018"),
    # PEB
    ("Quais os princípios constitucionais que regem a PEB (art. 4, CF/88)?",
     "Não-intervenção, autodeterminação, igualdade dos Estados, solução pacífica, cooperação, repúdio ao terrorismo/racismo. TPS 2024, 2025"),
    ("O que é cooperação Sul-Sul triangular e como o Brasil a pratica?",
     "Parceria entre dois países em desenvolvimento + doador do Norte; Brasil não impõe condicionalidades. TPS 2022"),
    ("Como o estruturalismo da CEPAL explica a divisão centro-periferia?",
     "Diferenças tecnológicas entre atividades primárias e industriais geram deterioração dos termos de troca. TPS 2025"),
    ("Qual a crítica do sistema-mundo (Wallerstein) ao estruturalismo da CEPAL?",
     "Acrescenta o conceito de semiperiferia e analisa a divisão internacional do trabalho historicamente. TPS 2025"),
    # União Europeia
    ("Quando Ursula von der Leyen se tornou presidente da Comissão Europeia?",
     "2019 — primeira mulher no cargo. TPS 2022"),
    ("Quais foram os elementos do Brexit acionados pela Theresa May?",
     "Acionamento do Art. 50 do Tratado de Lisboa em março de 2017; autorização prévia do parlamento britânico. TPS 2017"),
    ("Por que a Escócia e a Irlanda do Norte votaram 'remain' no Brexit?",
     "Maioria escocesa e norte-irlandesa apoiou permanência na UE; Inglaterra e País de Gales votaram 'leave'. TPS 2017"),
    ("Quem liderou o governo britânico que defendeu a permanência na UE no referendo de 2016?",
     "David Cameron (conservador pró-UE); perdeu o referendo e renunciou; Theresa May assumiu. TPS 2017"),
    # Teorias RI
    ("Qual a diferença entre realismo defensivo e realismo ofensivo?",
     "Defensivo (Waltz): Estados buscam segurança, não maximizar poder. Ofensivo (Mearsheimer): maximização do poder. TPS 2025"),
    ("Segundo o realismo defensivo, o que a posse de arma nuclear pelo Irã geraria?",
     "Waltz argumenta que geraria estabilidade (dissuasão mútua) no Oriente Médio. TPS 2017"),
    # ONU
    ("Como é escolhido o Secretário-Geral da ONU conforme a Carta das Nações Unidas?",
     "Indicação do Conselho de Segurança + aprovação da Assembleia-Geral. TPS 2017"),
    ("Quais as funções do depositário de um tratado segundo a Convenção de Viena (1969)?",
     "Receber instrumentos de ratificação, informar partes, registrar o tratado, examinar documentos formais. TPS 2016"),
    # Cooperação Sul-Sul e multilateralismo
    ("O que caracteriza a Cooperação Sul-Sul brasileira em contraste com a cooperação Norte-Sul?",
     "Ausência de condicionalidades; baseada em demanda; solidariedade; transferência de tecnologia e capacitação. TPS 2022"),
    ("Como a participação do Brasil em procedimentos consultivos da CIJ expressa o princípio da solução pacífica?",
     "Brasil participou em opiniões sobre Kosovo, Chagos e uso de armas nucleares, reforçando o direito internacional. TPS 2024"),
    ("O que distingue o princípio da não-intervenção do princípio da solução pacífica dos conflitos?",
     "Não-intervenção: respeito à condução interna dos Estados; solução pacífica: uso de meios diplomáticos/judiciais internacionais. TPS 2024"),
]

HB_CARDS = [
    # Período colonial
    ("Quais foram as principais exceções legais que permitiam a escravidão indígena na América portuguesa?",
     "Guerras justas e resgate de índios prestes a ser mortos. Na prática, amplamente usadas pelos colonizadores. TPS 2019, 2024"),
    ("Qual foi o papel da Holanda no Nordeste colonial no século XVII?",
     "Presença holandesa (1630-1654) nas capitanias do norte; não diversificou a economia — manteve o açúcar como base. TPS 2019, 2024"),
    ("O que Padre Antônio Vieira defendeu em seus sermões em relação à escravidão?",
     "Criticou a escravidão indígena e defendeu os índios, mas aceitou a africana; combateu os hereges holandeses. TPS 2019"),
    ("Como Portugal arrendou o Brasil nos primeiros anos após 1500?",
     "Arrendou o litoral a consórcio de comerciantes lisboetas nos primeiros 5 anos para iniciar exploração. TPS 2024"),
    # Independência
    ("Quais três movimentos emancipacionistas o TPS frequentemente cita como exemplos pré-independência?",
     "Inconfidência Mineira (1789), Conjuração Baiana (1798), Revolução Pernambucana (1817). TPS 2025"),
    ("Qual a diferença de objetivos entre a Inconfidência Mineira e a Conjuração Baiana?",
     "Mineira: independência liderada por elites; Baiana: revolução social com participação popular, libertação de escravos. TPS 2025"),
    ("Como a Revolução do Porto (1820) impactou o processo de independência do Brasil?",
     "Exigiu retorno de D. João VI a Portugal e recolonização do Brasil; acelerou o movimento separatista. TPS 2025"),
    ("Qual a importância simbólica da Missão Artística Francesa (1816) para o Estado imperial brasileiro?",
     "Dotar o Brasil de arte e cultura 'civilizada' segundo padrões europeus; legitimação do Estado nacional. TPS 2022"),
    ("Quem foi o responsável por contratar os artistas franceses em 1816, e por quê?",
     "O marquês de Marialva (embaixador em Paris), por iniciativa do príncipe regente João. TPS 2022"),
    # República Velha
    ("O que foi a Proclamação da República e qual sua base social?",
     "Golpe militar de 15/11/1889; militares sem base social ampla foram logo alijados do poder. TPS 2025"),
    ("Quais foram os principais levantes no governo de Floriano Peixoto?",
     "Revolta da Armada (marinha monarquista) e Revolução Federalista no Rio Grande do Sul. TPS 2020"),
    ("O que foi o Manifesto Antropófago de Oswald de Andrade e qual sua relação com a identidade nacional?",
     "1928; 'devoração crítica' da cultura europeia; diferente da posição de Mário de Andrade (menos radical). TPS 2024"),
    # Barão do Rio Branco
    ("Como o Barão do Rio Branco chegou ao Itamaraty e qual foi seu primeiro grande desafio?",
     "Convidado por Rodrigues Alves por suas vitórias arbitrais; primeiro desafio foi a Questão do Acre. TPS 2023"),
    ("Quais foram as vitórias arbitrais do Barão do Rio Branco antes de assumir o Itamaraty?",
     "Arbitragem das Missões (1895, com EUA) e Amapá (1900, com França). TPS 2023"),
    # Guerra do Paraguai
    ("Como Solano López construiu o culto à personalidade durante a Guerra do Paraguai?",
     "Identificou-se com o Estado; imprensa (Cabichuí, 1867) o comparava a Moisés; repressão interna intensa. TPS 2020"),
    # Regime Militar
    ("Qual foi o impacto do relatório da Anistia Internacional (1972) sobre o Brasil na ONU?",
     "Brasil foi impedido de participar como membro da Comissão de Direitos Humanos da ONU até a abertura política. TPS 2024"),
    # Segundo Reinado e abolição
    ("Qual o impacto político da abolição da escravidão (1888) para o Império?",
     "Alienou a elite agrária do Sudeste; enfraqueceu a base de sustentação de d. Pedro II; acelerou a República. TPS 2025"),
]

HM_CARDS = [
    # Segunda Guerra Mundial
    ("O que foi a Conferência de Munique (1938) e qual seu resultado?",
     "França e Reino Unido cederam Sudetenland à Alemanha; fracasso do apaziguamento; Liga das Nações foi ineficaz. TPS 2022"),
    ("Qual a diferença entre o Anschluss da Áustria e a anexação da Checoslováquia?",
     "Anschluss (março 1938): anexação da Áustria; Tchecoslováquia (setembro 1938): arbitrada em Munique. TPS 2022"),
    ("O que foi o Swope Plan e como se relaciona com o New Deal?",
     "Plano da fase 1 do New Deal; visava incentivar crescimento industrial via remoção temporária de controles de preços. TPS 2022"),
    ("O que eram as company unions e por que as corporações as criavam?",
     "Sindicatos criados pelas próprias empresas para contornar o Art. 7 do NIRA que garantia organização sindical. TPS 2022"),
    # Guerra Fria
    ("O que foi o 'longo telegrama' de George Kennan e qual seu impacto?",
     "Telegrama de 1946 da embaixada em Moscou; fundamentou a estratégia de contenção da URSS pelos EUA. TPS 2020"),
    ("O Plano Marshall era doação ou empréstimo? Quem ficou de fora?",
     "Combinação de doações e empréstimos; URSS recusou participar e proibiu satélites; criou a OECE (hoje OCDE). TPS 2020"),
    ("Qual o papel da OTAN na estrutura da Guerra Fria?",
     "Aliança militar ocidental (1949); contraponto ao Pacto de Varsóvia (1955); artigo 5 de defesa coletiva. TPS 2020"),
    # Descolonização
    ("Quem foi Kwame Nkrumah e qual sua contribuição ao pan-africanismo?",
     "Líder da independência do Gana (1957); defendeu pan-africanismo antes mesmo das independências. TPS 2019"),
    ("O que é a RASD e qual sua disputa com o Marrocos?",
     "República Árabe Saaraui Democrática; reivindica soberania sobre o Saara Ocidental; Marrocos não reconhece. TPS 2023"),
    ("Por que o Marrocos não é membro da União Africana?",
     "Retirou-se em 1984 após a UA reconhecer a RASD; reintegrou-se em 2017 mas questão permanece. TPS 2023"),
    # Revoluções europeias
    ("Por que os camponeses russos não apoiaram os bolcheviques na guerra civil de 1918-1920?",
     "Políticas de requisição de grãos (comunismo de guerra); camponeses queriam terra, não coletivização. TPS 2025"),
    ("Qual o papel do liberalismo clássico e da maçonaria na Revolução Francesa?",
     "Liberalismo articulou os interesses burgueses; maçonaria foi canal de difusão de ideias iluministas. TPS 2025"),
    ("Qual a tese central de Benedict Anderson sobre o nacionalismo?",
     "Nação = 'comunidade imaginada': intrinsecamente limitada e soberana; construção histórica e discursiva. TPS 2024"),
    # Revolução Industrial
    ("Qual a tese de David Landes sobre o ritmo da Revolução Industrial?",
     "Inovações não surgem de repente; precisam de série de pequenos aperfeiçoamentos graduais. TPS 2024"),
    ("Como o colonialismo se relacionou com o liberalismo no século XIX, segundo a historiografia?",
     "Colonialismo não foi secundário ao liberalismo; teve impacto direto e imediato na política e economia do século. TPS 2024"),
    # Oriente Médio
    ("Por que os países árabes bloquearam o Catar em 2017?",
     "Alegavam que o Catar financiava terrorismo e mantinha relações com o Irã; Al-Jazeera também foi alvo. TPS 2017"),
]

GEO_CARDS = [
    # Pensamento geográfico
    ("Quais as quatro principais correntes da geografia científica e seus enfoques?",
     "Tradicional (Humboldt/Ritter); Nova Geografia (quantitativa); Crítica (Milton Santos); Humanista (espaço vivido). TPS 2016, 2025"),
    ("O que é o possibilismo geográfico e quem o criou?",
     "La Blache: o meio oferece possibilidades, a sociedade escolhe. Conceito de 'gêneros de vida'. ≠ determinismo. TPS 2025"),
    ("O que é o determinismo geográfico e quem é seu principal expoente?",
     "Ratzel: o meio físico determina as sociedades. NÃO incorporou o conceito de gêneros de vida (este é possibilista). TPS 2025"),
    ("Qual é a proposta metodológica de Richard Hartshorne para a geografia?",
     "Região como campo empírico (chorologia); abordagem idiográfica, NÃO sistemática ou universal. TPS 2025"),
    ("O que Alexander von Humboldt inaugurou no pensamento geográfico?",
     "Compreensão do equilíbrio dos ecossistemas e perigos da ação antrópica; renovação do pensamento geográfico. TPS 2025"),
    ("O que Milton Santos chama de 'meio técnico-científico-informacional'?",
     "Fase atual do espaço geográfico onde ciência, tecnologia e informação se difundem no território (ex.: agronegócio). TPS 2022"),
    # Urbanização
    ("O que é metropolização e como se manifesta no Brasil?",
     "Expansão das metrópoles, concentração de capital e população, periferização e surgência de regiões metropolitanas. TPS 2023"),
    ("O que é um sistema urbano e como o IADES o conceitualiza nas provas?",
     "Componente espacial do desenvolvimento social; resultado de evolução histórica; rede de cidades com interdependências. TPS 2023"),
    ("O que é pendularidade e por que não é considerada migração?",
     "Deslocamento diário para cidade vizinha (trabalho/estudo) sem mudança de domicílio. ≠ migração definitiva. TPS 2025"),
    # Agronegócio e território
    ("O que é a fronteira agrícola moderna e onde se localiza no Brasil?",
     "Áreas de expansão do agronegócio com uso de tecnologia (MATOPIBA: MA, TO, PI, BA); Cerrado. TPS 2022"),
    ("Por que o saldo comercial do agronegócio pode ser subestimado?",
     "Insumos importados (fertilizantes, pesticidas) NÃO são subtraídos do saldo calculado pelo MAPA. TPS 2024"),
    # Migrações
    ("Quais os critérios de convergência do Tratado de Maastricht para a zona do euro?",
     "Déficit ≤ 3% PIB; dívida pública ≤ 60% PIB; inflação e juros convergentes. (NÃO 30% como o TPS testa). TPS 2015"),
    ("O que o Acordo de Residência do MERCOSUL permite?",
     "Residência para nacionais dos Estados-partes e associados do MERCOSUL, ampliando fluxos migratórios regionais. TPS 2024"),
    # Domínios brasileiros
    ("Qual a distinção entre várzeas e igapós na Amazônia?",
     "Várzeas: inundáveis por rios de água branca (férteis); igapós: inundáveis por rios de água preta (menos férteis). TPS 2020"),
    ("O que caracteriza o domínio morfoclimático do Cerrado?",
     "Chapadões do Brasil Central; savana tropical; grande biodiversidade; avanço da fronteira agrícola moderna. TPS 2020"),
    # Geopolítica regional
    ("Por que o determinismo geográfico alemão influenciou a consolidação da geografia como ciência?",
     "O expansionismo alemão necessitava de fundamentos científicos; Ratzel desenvolveu a geopolítica para justificá-lo. TPS 2025"),
    ("Como a teoria geral dos sistemas foi incorporada pela Geografia Teorética?",
     "Permitiu modelar fenômenos (migrações, dinâmicas naturais) com cálculo de probabilidades e previsão de eventos. TPS 2016"),
]

ECON_CARDS = [
    # Modelos de crescimento
    ("No modelo de Harrod-Domar, o que determina o crescimento de longo prazo?",
     "Taxa de poupança dividida pela razão capital-produto (v). Crescimento instável — 'fio de navalha'. TPS 2019"),
    ("No modelo de Solow, o que acontece quando a economia atingi o estado estacionário (steady state)?",
     "Capital e produto crescem à mesma taxa (crescimento balanceado); relação capital-produto estável. TPS 2019"),
    ("Por que aumentos na taxa de poupança, em Solow, elevam o crescimento apenas temporariamente?",
     "Retornos decrescentes do capital; a economia converge para um novo steady state com nível mais alto, não taxa maior. TPS 2019"),
    # Dívida externa
    ("Quais os principais indicadores de solvência externa usados pelo FMI?",
     "Dívida externa/PIB (risco de inadimplência); serviço da dívida/exportações (principal + juros). TPS 2025"),
    ("O que mede a razão dívida externa de curto prazo / reservas internacionais?",
     "Liquidez de curto prazo; capacidade de liquidar rápido a dívida (regra de Guidotti). TPS 2025"),
    ("Uma baixa relação dívida/exportações indica maior ou menor vulnerabilidade?",
     "Menor vulnerabilidade (mais exportações = mais capacidade de pagar). Alta relação = maior risco. TPS 2025"),
    # Política monetária
    ("O que é Quantitative Easing (QE) e quando o FED o utilizou?",
     "Compra de ativos pelo BC para injetar liquidez; FED usou após 2008 e durante COVID (2020). TPS 2025"),
    ("Qual a diferença entre QE e a prática de juros negativos sobre reservas bancárias?",
     "QE = compra de ativos; juros negativos = taxa abaixo de zero cobrada do banco pela reserva depositada no BC. TPS 2025"),
    ("O que é política monetária não convencional? Cite dois exemplos.",
     "Instrumentos além da taxa básica: QE (compra de ativos) e juros negativos sobre reservas. TPS 2025"),
    # Inflação
    ("O que foi a estagflação dos anos 1980 no Brasil?",
     "Combinação de recessão (crise da dívida) + alta inflação; causada também pela inércia inflacionária (indexação). TPS 2023"),
    ("O Plano Cruzado foi ortodoxo ou heterodoxo? Por que falhou?",
     "Heterodoxo (congelamento de preços + URV); falhou com o descongelamento e demanda represada (1986). TPS 2023"),
    ("Quais planos econômicos dos anos 1980 usaram APENAS medidas ortodoxas no Brasil?",
     "Nenhum: Cruzado, Bresser e Verão foram heterodoxos ou mistos; o Real (1994) usou âncora cambial. TPS 2023"),
    # Comércio internacional
    ("Quais os dois princípios fundamentais da OMC para o comércio de bens?",
     "Nação mais favorecida (NMF): estender benefícios a todos; Tratamento nacional: não discriminar importados. TPS vários"),
    ("O que o TRIPS estabelece para direitos de propriedade intelectual?",
     "Padrões mínimos de proteção de patentes; países podem ir além; baseia-se em NMF e tratamento nacional. TPS 2025"),
    ("O que é a deterioração dos termos de troca (Prebisch-Singer)?",
     "Preços de primários caem relativamente a manufaturados no longo prazo; prejudica economias exportadoras de commodities. TPS 2023"),
    # Macroeconomia aberta
    ("O que é a regra de Guidotti para gestão de reservas internacionais?",
     "Reservas devem cobrir toda a dívida externa de curto prazo; indica liquidez suficiente para 1 ano. TPS 2025"),
    ("Como a paridade do poder de compra (PPC) relaciona câmbio e inflação?",
     "Taxa de câmbio deve refletir diferença de inflações entre países; lei do preço único no longo prazo. TPS vários"),
]

DIP_CARDS = [
    # Direito Administrativo - Lei 8.112/90
    ("Qual o prazo de não comparecimento que caracteriza abandono de cargo (Lei 8.112/90)?",
     "Mais de 30 dias ininterruptos sem justificativa. Apurado via PAD de rito sumário (30+15 dias). TPS 2025"),
    ("O que é inassiduidade habitual e como se diferencia do abandono de cargo?",
     "Faltas injustificadas intercaladas (60/ano); NÃO exige animus de abandono; PAD sumário também. TPS 2025"),
    ("Quando começa a contar o prazo prescricional disciplinar (Lei 8.112/90)?",
     "Da data da consumação do ilícito. Ao ser interrompido, reinicia do zero. TPS 2025"),
    ("Quais os prazos de prescrição da ação disciplinar na Lei 8.112/90?",
     "5 anos (demissão/cassação/destituição); 2 anos (suspensão); 180 dias (advertência). TPS 2025"),
    # Lei 11.440/2006 - Serviço Exterior
    ("O que é proibido ao servidor do SEB sem autorização expressa da Secretaria de Estado?",
     "Renunciar a imunidades de que goze no exterior; divulgar informações relevantes de política externa. TPS 2025"),
    ("Para aceitar comissão, emprego ou pensão de governo estrangeiro, o que o servidor do SEB precisa?",
     "Expressa autorização do Ministro de Estado das Relações Exteriores. TPS 2025"),
    # Responsabilidade do Estado
    ("Contra quem deve ser ajuizada ação por danos causados por agente público (art. 37, §6, CF)?",
     "Contra o Estado (ou PJ de direito privado prestadora de serviço público); o agente é parte ilegítima. TPS 2020, 2022"),
    ("O que garante o art. 37, §6 da CF em relação ao agente público causador do dano?",
     "Estado responde objetivamente; tem direito de regresso contra o agente em caso de dolo ou culpa. TPS 2020, 2022"),
    # Direito Internacional Público
    ("As organizações internacionais têm personalidade jurídica? Desde quando e com base em quê?",
     "Sim; construída progressivamente; Parecer da CIJ de 1949 (caso Conde Bernadotte) foi o marco. TPS 2015, 2025"),
    ("O que é o Acordo BBNJ e qual seu princípio norteador principal?",
     "Acordo ONU (2023) sobre diversidade biológica em áreas além da jurisdição nacional; princípio do patrimônio comum da humanidade. TPS 2024"),
    ("O Brasil aceitou a jurisdição compulsória da CIJ? Pode ser acionado?",
     "Sim; o Brasil apresentou declaração; pode ser acionado e pode acionar outros. TPS 2024"),
    ("As intervenções de terceiros Estados na CIJ têm aumentado? O que a Corte fez?",
     "Sim; CIJ ajustou suas regras de procedimento para acomodar o crescente número de intervenções. TPS 2024"),
    # Direitos Humanos Internacionais
    ("Quais são as características dos direitos humanos segundo a Declaração de Viena (1993)?",
     "Universais, indivisíveis, interdependentes e inter-relacionados. TPS 2023"),
    ("A Convenção contra a Tortura (ONU, 1984) admite exceções para estados de guerra?",
     "Não. A proibição da tortura é absoluta; nenhuma circunstância excepcional a justifica. TPS 2023"),
    # ONU
    ("Como é escolhido o Secretário-Geral da ONU, segundo a Carta?",
     "Indicação do Conselho de Segurança + aprovação da Assembleia-Geral. NÃO é indicado pela AG. TPS 2017"),
    ("Quais as funções do depositário de um tratado (Convenção de Viena 1969)?",
     "Receber ratificações, informar as partes, registrar o tratado, examinar instrumentos formais. TPS 2016"),
    # Princípios constitucionais PEB
    ("O que o princípio da defesa da paz implica para a PEB?",
     "Postura crítica a interpretações expansivas do direito à legítima defesa; participação em OPs de paz. TPS 2024"),
    ("O princípio da solução pacífica dos conflitos impede o Brasil de ser acionado na CIJ?",
     "Não. O Brasil tem declaração de aceitação da jurisdição compulsória; pode ser acionado. TPS 2024"),
    # Licitações
    ("O que são bens e serviços especiais segundo a Lei 14.133/2021?",
     "Aqueles cujos padrões de desempenho NÃO podem ser definidos objetivamente por especificações de mercado. TPS 2022"),
    ("Qual a diferença entre bens comuns e especiais na Lei 14.133/2021?",
     "Comuns: padrões objetivamente definíveis (pregão). Especiais: padrões NÃO definíveis objetivamente (técnica e preço). TPS 2022"),
]

# ── Build all decks ──────────────────────────────────────────────────────────

OUTPUT_DIR = Path(__file__).parent

DECKS = [
    ("tps_pi.apkg",   "politica_internacional", PI_CARDS),
    ("tps_hb.apkg",   "historia_brasil",        HB_CARDS),
    ("tps_hm.apkg",   "historia_mundial",       HM_CARDS),
    ("tps_geo.apkg",  "geografia",               GEO_CARDS),
    ("tps_econ.apkg", "economia",                ECON_CARDS),
    ("tps_dip.apkg",  "direito",                 DIP_CARDS),
]

for fname, deck_name, cards in DECKS:
    out = OUTPUT_DIR / fname
    build_apkg(out, deck_name, cards)

print(f"\nDone! {len(DECKS)} decks created in {OUTPUT_DIR}")
