#!/usr/bin/env python3
"""Gera deck Anki: Direito Interno - Organização dos Poderes - Executivo"""

import genanki
import os
import random

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "anki", "decks", "direito")

STYLE = """
.card { font-family: Arial, sans-serif; font-size: 16px; text-align: left; padding: 12px; }
.front { font-weight: bold; }
"""

def make_deck(title, filename, cards):
    model_id = random.randrange(1_000_000_000, 2_000_000_000)
    deck_id = random.randrange(1_000_000_000, 2_000_000_000)

    model = genanki.Model(
        model_id,
        "CACD Basic",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card",
            "qfmt": '<div class="front">{{Frente}}</div>',
            "afmt": '{{FrontSide}}<hr>{{Verso}}',
        }],
        css=STYLE,
    )

    deck = genanki.Deck(deck_id, title)
    for front, back in cards:
        deck.add_note(genanki.Note(model=model, fields=[front, back]))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename)
    genanki.Package(deck).write_to_file(out_path)
    print(f"✅ {filename} — {len(cards)} cards")
    print(f"🎉 Deck gerado em {OUTPUT_DIR}")


CARDS = [
    # ── SEPARAÇÃO DOS PODERES ─────────────────────────────────────────────────
    (
        "Onde está previsto o princípio da separação dos poderes na CF/88 e qual é sua natureza?",
        "Previsto no <b>Art. 2 CF/88</b>. É <b>cláusula pétrea</b> (Art. 60, §4), portanto não "
        "pode ser abolido por emenda constitucional. Baseia-se no mecanismo de <b>freios e "
        "contrapesos</b> (checks and balances) com controle recíproco entre os poderes.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),
    (
        "Qual a diferença entre funções típicas e atípicas dos poderes do Estado?",
        "<b>Funções típicas</b>: desempenhadas de modo <i>preponderante</i> pelo poder.<br>"
        "<b>Funções atípicas</b>: desempenhadas de modo <i>secundário</i>, sem preponderância.<br>"
        "Todos os três poderes exercem ambos os tipos de função.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),
    (
        "Quais são a função típica e as funções atípicas do Poder Executivo?",
        "<b>Função típica</b>: administrativa (prestação de serviços públicos e gestão dos "
        "servidores públicos).<br>"
        "<b>Funções atípicas</b> (2):<br>"
        "1. <b>Legislativa</b>: criação de medidas provisórias e leis delegadas pelo Presidente<br>"
        "2. <b>Jurisdicional</b>: órgãos do Executivo que julgam recursos administrativos "
        "(ex.: Ministro da Justiça julgando recurso contra decisão do CONARE – Art. 29, Lei 9.474/1997)<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo / Art. 76–91 CF/88</i>",
    ),

    # ── PRESIDENCIALISMO ─────────────────────────────────────────────────────
    (
        "O que define o sistema presidencialista e quais as duas atribuições do Presidente?",
        "O presidencialismo concentra no Presidente duas atribuições:<br>"
        "1. <b>Chefe de Estado</b> (plano internacional, exerce soberania): mantém relações "
        "exteriores, assina tratados, declara guerra (Art. 84 CF/88)<br>"
        "2. <b>Chefe de Governo</b> (plano nacional, exerce autonomia): nomeia ministros, "
        "dirige a adm. federal, inicia processo legislativo<br>"
        "O Executivo é <b>unipessoal</b>: ministros auxiliam mas não compartilham a chefia.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),

    # ── DECRETOS ─────────────────────────────────────────────────────────────
    (
        "O que é um decreto regulamentar (Art. 84, IV CF/88) e a que tipo de controle está sujeito?",
        "<b>Decreto regulamentar</b>: garante a fiel execução de lei; explica como o Executivo "
        "cumprirá determinações impostas pelo legislador.<br>"
        "<b>Ato normativo secundário</b>: decorre da lei (não da CF diretamente).<br>"
        "Sujeito a <b>controle de legalidade</b> (não de constitucionalidade).<br>"
        "O Congresso Nacional pode sustá-lo pelo <b>Art. 49, V</b> se exorbitar o poder "
        "regulamentar.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),
    (
        "O que é um decreto autônomo (Art. 84, VI CF/88) e quais são suas hipóteses?",
        "<b>Decreto autônomo</b>: ato normativo <b>primário</b> (mesmo nível que leis; decorre "
        "da CF).<br>"
        "Duas situações:<br>"
        "1. Organizar a adm. pública <b>sem</b> aumento de despesa ou criação/extinção de "
        "órgãos públicos<br>"
        "2. Extinguir <b>cargos e funções públicas quando vagos</b> (nunca órgãos — extinção "
        "de órgãos exige lei)<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),
    (
        "Quais são as 3 competências delegáveis do Art. 84 (parágrafo único CF/88) e para quem?",
        "<b>Competências delegáveis</b> (apenas 3):<br>"
        "1. <b>Art. 84, VI</b>: expedir decreto autônomo<br>"
        "2. <b>Art. 84, XII</b>: conceder indultos e comutar penas<br>"
        "3. <b>Art. 84, XXV, 1ª parte</b>: prover cargos públicos<br>"
        "<b>Destinatários</b>: Ministros de Estado, Procurador-Geral da República ou "
        "Advogado-Geral da União.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),

    # ── IMPEDIMENTO E VACÂNCIA ────────────────────────────────────────────────
    (
        "Qual a diferença entre impedimento e vacância no Poder Executivo (Arts. 79–81 CF/88)?",
        "<b>Impedimento</b>: obstáculo <i>temporário</i> (viagens, férias) → <b>substituição</b><br>"
        "<b>Vacância</b>: obstáculo <i>definitivo</i> (morte, renúncia, impeachment) → "
        "<b>sucessão</b><br>"
        "Art. 79: Vice-presidente substitui ou sucede o Presidente em qualquer momento do mandato.<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo</i>",
    ),
    (
        "O que ocorre em caso de duplo impedimento e de dupla vacância do Presidente e do VP?",
        "<b>Duplo impedimento (Art. 80)</b>: assumem de forma <i>interina</i>, nessa ordem:<br>"
        "1. Presidente da Câmara → 2. Presidente do Senado → 3. Presidente do STF<br><br>"
        "<b>Dupla vacância (Art. 81)</b>: realizam-se novas eleições:<br>"
        "• Nos <b>2 primeiros anos</b>: eleições <b>diretas</b> em até <b>90 dias</b><br>"
        "• Nos <b>2 últimos anos</b>: eleições <b>indiretas</b> no CN em até <b>30 dias</b><br>"
        "Em qualquer caso, o mandato é <b>tampão</b> (restante do mandato original).<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo / Art. 80–81 CF/88</i>",
    ),

    # ── IMUNIDADES DO PRESIDENTE ──────────────────────────────────────────────
    (
        "Quais são as imunidades penais do Presidente e a quem se aplicam?",
        "Somente ao <b>Presidente da República</b> (não a governadores ou prefeitos):<br>"
        "1. <b>Imunidade ao processo penal (§4)</b>: durante o mandato, responde apenas por "
        "crimes <i>ligados às funções presidenciais</i>; crimes particulares aguardam o fim "
        "do mandato<br>"
        "2. <b>Imunidade à prisão (§3)</b>: durante o mandato, só pode ser preso por "
        "<i>sentença penal condenatória</i> — não cabe prisão em flagrante, preventiva ou "
        "provisória<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo / Art. 86, §3 e §4 CF/88</i>",
    ),
    (
        "Como funciona o processo bifásico de responsabilização penal do Presidente?",
        "Ambas as vias exigem <b>autorização de ⅔ da Câmara dos Deputados</b>:<br>"
        "• <b>STF</b>: julga <i>crimes comuns ligados à função</i> (ação penal)<br>"
        "• <b>Senado Federal</b>: julga <i>crimes de responsabilidade</i> (impeachment)<br>"
        "O Presidente fica <b>afastado por até 180 dias</b> a partir do início do julgamento; "
        "se não concluído em 180 dias, retorna ao cargo (processo continua).<br>"
        "<i>Fonte: Anotações – Organização dos Poderes - Executivo / Art. 86 CF/88</i>",
    ),

    # ── EXERCÍCIOS — Q01 (Rodada 02 – Nov/2023) ──────────────────────────────
    (
        "[Exercício] I – O chefe do Poder Executivo federal não desempenha funções que possam "
        "repercutir nos interesses dos estados-membros, devido ao princípio federativo.",
        "<b>ERRADO.</b> O Presidente da República exerce diversas competências que repercutem "
        "diretamente nos estados-membros, como a condução da política econômica, a celebração "
        "de tratados internacionais e a gestão de recursos federais — tudo isso afeta os "
        "interesses estaduais, ainda que o Brasil adote o federalismo.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q01-I</i>",
    ),
    (
        "[Exercício] II – A competência do Senado Federal para sustar atos normativos do "
        "Poder Executivo que exorbitem do poder regulamentar configura hipótese de controle político.",
        "<b>ERRADO.</b> Dois erros: (1) a competência é do <b>Congresso Nacional</b> (Art. 49, V "
        "CF/88), não só do Senado; (2) o controle é de natureza <b>política repressiva</b> "
        "(pós-edição do ato), não simplesmente \"político\" — distinção relevante para provas.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q01-II</i>",
    ),
    (
        "[Exercício] III – Compete ao presidente da República, mediante decreto, extinguir "
        "órgãos, funções ou cargos públicos que estejam vagos.",
        "<b>ERRADO.</b> O Art. 84, VI, b CF/88 permite ao Presidente extinguir mediante decreto "
        "autônomo apenas <b>cargos e funções públicas quando vagos</b>. A extinção de "
        "<b>órgãos públicos</b> exige lei — não pode ser feita por decreto.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q01-III</i>",
    ),
    (
        "[Exercício] IV – A competência para conceder indulto é privativa do Presidente, "
        "portanto não pode ser delegada a ministros de Estado.",
        "<b>ERRADO.</b> O indulto (Art. 84, XII CF/88) é uma das <b>três competências "
        "delegáveis</b> previstas no Art. 84, parágrafo único. Pode ser delegada a Ministros "
        "de Estado, ao PGR ou ao AGU.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – A competência para celebrar tratados internacionais sujeitos a "
        "referendo do Congresso Nacional não é passível de delegação pelo presidente.",
        "<b>CERTO.</b> A competência para celebrar tratados (Art. 84, VIII CF/88) <b>não consta</b> "
        "entre as três competências delegáveis do Art. 84, parágrafo único — que são: "
        "decreto autônomo (VI), indulto (XII) e provimento de cargos (XXV, 1ª parte).<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q02-I</i>",
    ),
    (
        "[Exercício] II – Ausentando-se por mais de 15 dias sem autorização do CN, a sanção "
        "mais gravosa ao Presidente é a censura pelo Poder Legislativo.",
        "<b>ERRADO.</b> A ausência do País por mais de 15 dias sem autorização do Congresso "
        "Nacional configura infração político-administrativa. A sanção mais grave é a "
        "<b>perda do cargo</b> (por crime de responsabilidade), não mera censura.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q02-II</i>",
    ),
    (
        "[Exercício] III – O Presidente falece no início do 3º ano do mandato; o VP renuncia. "
        "Deve ser organizada eleição direta em até 90 dias.",
        "<b>ERRADO.</b> O 3º ano do mandato (de 4 anos) está nos <b>2 últimos anos</b>, hipótese "
        "que demanda eleições <b>indiretas</b> no Congresso Nacional em até <b>30 dias</b> "
        "(Art. 81, §1º CF/88). Eleições diretas em 90 dias ocorrem apenas quando a vacância "
        "se abre nos 2 primeiros anos do mandato.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q02-III</i>",
    ),
    (
        "[Exercício] IV – Compete aos ministros de Estado referendar os atos e decretos "
        "assinados pelo Presidente, bem como expedir instruções para a execução de leis, "
        "decretos e regulamentos.",
        "<b>CERTO.</b> Art. 87, parágrafo único, I e II CF/88: são atribuições dos Ministros "
        "de Estado referendar atos presidenciais e expedir instruções para execução de leis, "
        "decretos e regulamentos.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – O processo de crime de responsabilidade do Presidente divide-se em: "
        "juízo de admissibilidade perante o Senado + julgamento perante a Câmara dos Deputados.",
        "<b>ERRADO.</b> Está <b>invertido</b>: o juízo de <i>admissibilidade</i> ocorre na "
        "<b>Câmara dos Deputados</b> (aprovação por ⅔ de seus membros), e o <i>julgamento</i> "
        "ocorre no <b>Senado Federal</b> (processo de impeachment).<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q03-I</i>",
    ),
    (
        "[Exercício] II – O Presidente só responde a processo criminal no STF após autorização "
        "da Câmara (⅔). O juízo de admissibilidade da Câmara não vincula o STF.",
        "<b>CERTO.</b> O STF realiza juízo prévio e independente sobre o recebimento da "
        "denúncia ou queixa-crime — a autorização da Câmara (⅔) é condição necessária, mas "
        "o STF não está vinculado ao teor da decisão da Câmara para fins de admissibilidade "
        "da ação penal.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q03-II</i>",
    ),
    (
        "[Exercício] III – Os crimes comuns do Presidente são processados perante o STF, "
        "e o Presidente fica afastado desde o recebimento da denúncia ou queixa-crime.",
        "<b>CERTO.</b> Art. 86, §1º CF/88: após o recebimento da denúncia ou queixa-crime "
        "pelo STF, o Presidente fica <b>suspenso de suas funções por até 180 dias</b>. Se o "
        "julgamento não for concluído nesse prazo, o Presidente retorna ao cargo e o processo "
        "continua.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q03-III</i>",
    ),
    (
        "[Exercício] IV – Não viola a CF/88 a prisão de governador de estado ou do DF, "
        "por infração penal comum, ainda que inexista sentença penal condenatória.",
        "<b>CERTO.</b> A imunidade à prisão antes de sentença (Art. 86, §3 CF/88) é "
        "exclusiva do <b>Presidente da República</b>. Governadores e demais chefes do "
        "Executivo estadual podem ser presos em flagrante, preventiva ou provisória, "
        "pois não gozam dessa prerrogativa constitucional.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 02, Nov/2023, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Interno::Organização dos Poderes - Executivo",
        "Direito Interno - Organização dos Poderes - Executivo.apkg",
        CARDS,
    )
