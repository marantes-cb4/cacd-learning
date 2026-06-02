#!/usr/bin/env python3
"""Gera deck Anki: Direito Interno - Estado: Conceito e Formas"""

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


ESTADO_CONCEITO_FORMAS = [
    # ── 4 CONCEITOS ESTRUTURAIS ────────────────────────────────────────────────
    (
        "Quais são os 4 conceitos estruturais do direito constitucional brasileiro?",
        "1. <b>Forma de Estado</b>: Federação<br>"
        "2. <b>Forma de governo</b>: República<br>"
        "3. <b>Sistema de governo</b>: Presidencialismo<br>"
        "4. <b>Regime de governo</b>: Democracia<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas / Art. 18 CF/88</i>",
    ),
    (
        "O que é federação? Quais são os 4 entes federados brasileiros?",
        "Forma de <b>Estado composto</b> com múltiplas instâncias do poder estatal, que promove a "
        "<b>descentralização política</b> em prol dos entes federados autônomos.<br>"
        "Entes: <b>União, Estados, Distrito Federal e Municípios</b> (art. 18 CF/88).<br>"
        "A forma federativa é <b>cláusula pétrea</b> (art. 60, §4, I CF/88).<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),

    # ── AUTONOMIA ──────────────────────────────────────────────────────────────
    (
        "O que é autonomia e quais são suas 4 capacidades políticas?",
        "Atributo de todos os entes federados = <b>personalidade jurídica de direito público interno</b>.<br>"
        "1. <b>Auto-organização</b>: criar órgãos e definir competências (CF/estadual/lei orgânica)<br>"
        "2. <b>Autogoverno</b>: realizar as próprias eleições<br>"
        "3. <b>Autolegislação</b>: criar leis conforme suas competências<br>"
        "4. <b>Autoadministração</b>: prestar seus próprios serviços e ter servidores públicos<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),
    (
        "Existe hierarquia entre os entes federados brasileiros? O que é o princípio da "
        "preponderância de interesses?",
        "<b>Não existe hierarquia</b> — todos têm o mesmo atributo (autonomia). Posição sedimentada "
        "do STF (art. 18 CF/88).<br>"
        "<b>Preponderância de interesses</b>: interesse nacional prevalece sobre o regional e local; "
        "regional prevalece sobre local. Não é hierarquia entre entes, mas entre <i>interesses</i>.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),
    (
        "Qual a diferença entre soberania e autonomia?",
        "<b>Soberania</b> (art. 1 CF/88): atributo da <b>República Federativa do Brasil</b> → "
        "personalidade jurídica de <b>direito público externo</b>. A União apenas a representa.<br>"
        "<b>Autonomia</b>: atributo de <b>todos os entes federados</b> (União, estados, DF, "
        "municípios) → personalidade jurídica de <b>direito público interno</b>.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),

    # ── TERRITÓRIOS E DF ───────────────────────────────────────────────────────
    (
        "Qual a condição jurídica dos territórios federais? (art. 18 §2 CF/88)",
        "<b>Não são entes federados</b>, não têm autonomia e não integram a organização "
        "político-administrativa da República. São <b>autarquias federais</b> (partes integrantes "
        "da União), criadas por lei complementar para assegurar serviços públicos onde não é viável "
        "um estado autônomo. Ex.: Fernando de Noronha até 1988.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas / Art. 18 §2 CF/88</i>",
    ),
    (
        "Por que o Distrito Federal é considerado 'sui generis'? (art. 32 CF/88)",
        "É ente federado autônomo com duas singularidades:<br>"
        "1. Tem competências legislativas <b>de estado e de município</b> (art. 32 §1)<br>"
        "2. <b>Não pode ser dividido em municípios</b> — Brasília é divisão administrativa, "
        "não município. O DF não tem capital própria; Brasília é a capital federal.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas / Art. 32 CF/88</i>",
    ),
    (
        "Quais serviços do DF são organizados e mantidos pela União? (art. 21 CF/88)",
        "• <b>Poder Judiciário e Ministério Público</b> (art. 21, XIII) — não inclui Defensoria Pública<br>"
        "• <b>Segurança pública</b>: polícia civil, penal, militar e corpo de bombeiros "
        "(art. 21, XIV)<br>"
        "<b>Súmula Vinculante 39 STF</b>: lei federal fixa a remuneração desses servidores "
        "distritais (pois a União paga a conta).<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),

    # ── INDISSOLUBILIDADE E DIVISIBILIDADE ─────────────────────────────────────
    (
        "O que são indissolubilidade e divisibilidade da federação brasileira?",
        "<b>Indissolubilidade</b> (art. 1 caput): entes federados não podem exercer direito de "
        "secessão — se tentado, haverá intervenção federal.<br>"
        "<b>Divisibilidade</b> (art. 18 §§3-4): é possível criar novos estados e municípios, "
        "potencializando a descentralização política.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),
    (
        "Quais são as etapas para criação de novos estados? (art. 18 §3 CF/88)",
        "1. <b>Plebiscito</b> com toda a população do Estado original (área nova + remanescente, "
        "segundo o STF)<br>"
        "2. <b>Lei complementar federal</b> conferindo personalidade jurídica de direito público "
        "interno<br>"
        "As mesmas etapas valem para a criação de territórios federais.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas / Art. 18 §3 CF/88</i>",
    ),
    (
        "Quais são as 4 etapas para criação de novos municípios? (art. 18 §4 CF/88)",
        "1. <b>Lei complementar federal</b> fixando o período em que estados podem criar municípios<br>"
        "2. <b>Estudo de viabilidade municipal</b> comprovando capacidade financeira autossuficiente<br>"
        "3. <b>Plebiscito</b> com a população diretamente interessada<br>"
        "4. <b>Lei estadual ordinária</b> criando efetivamente o município<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas / Art. 18 §4 CF/88</i>",
    ),

    # ── FEDERAÇÃO vs. CONFEDERAÇÃO ─────────────────────────────────────────────
    (
        "Quais são os dois processos históricos de formação de federações?",
        "<b>Centrípeto/Agregação</b>: Estados soberanos abrem mão da soberania para formar uma "
        "federação. Ex.: EUA (13 colônias, 1787).<br>"
        "<b>Centrífugo/Segregação</b>: Estado unitário é descentralizado em partes autônomas. "
        "Ex.: Brasil (1891 — províncias imperiais → estados autônomos).<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),
    (
        "Quais são as principais diferenças entre federação e confederação?",
        "<b>Federação</b>: base = constituição escrita; corte constitucional (STF no BR); "
        "sem direito de secessão; nacionalidade única.<br>"
        "<b>Confederação</b>: base = tratado internacional; sem tribunal habilitado; "
        "direito de secessão existe; cada Estado mantém sua própria nacionalidade.<br>"
        "Confederações não existem no mundo atual.<br>"
        "<i>Fonte: Anotações – Estado: Conceito e Formas</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Todos os estados brasileiros podem adotar sua própria Constituição e "
        "editar suas leis, desde que não infrinjam as normas e os princípios estabelecidos na "
        "Constituição Federal.",
        "<b>CERTO.</b> Decorre diretamente da autonomia dos estados: a capacidade de "
        "auto-organização (constituição estadual) e autolegislação (leis estaduais), dentro dos "
        "limites da CF/88.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q01-I</i>",
    ),
    (
        "[Exercício] II – Da capacidade de auto-organização municipal decorre a constatação de "
        "que o estado-membro não pode ingerir na autonomia organizatória do município, o que "
        "confere a este a possibilidade de ordenar internamente, inclusive por meio de lei "
        "orgânica, sem a necessidade de anuência do respectivo governo estadual.",
        "<b>CERTO.</b> A autonomia municipal é garantida diretamente pela CF/88. Municípios "
        "elaboram suas leis orgânicas independentemente de aprovação do estado-membro.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q01-II</i>",
    ),
    (
        "[Exercício] III – O Brasil adotou a forma republicana de governo e o modelo federativo "
        "de Estado que se embasa na autonomia e na soberania dos estados-membros, expressa pela "
        "capacidade destes de se auto-organizarem por meio das constituições estaduais.",
        "<b>ERRADO.</b> Os estados-membros têm <b>autonomia</b>, não soberania. A soberania "
        "pertence à República Federativa do Brasil como um todo (art. 1 CF/88), não aos "
        "estados individualmente.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q01-III</i>",
    ),
    (
        "[Exercício] IV – A substituição da União, dos estados, do Distrito Federal (DF) e dos "
        "municípios por um único ente central somente seria possível por um poder constituinte "
        "originário.",
        "<b>CERTO.</b> A forma federativa é cláusula pétrea (art. 60, §4, I CF/88) — não pode "
        "ser abolida por emenda constitucional. Somente o Poder Constituinte Originário, ao criar "
        "uma nova constituição, poderia extinguir a federação.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – A organização político-administrativa da República Federativa do Brasil "
        "compreende a União, os estados, os territórios, o Distrito Federal e os municípios, "
        "todos autônomos, nos termos da CF.",
        "<b>ERRADO.</b> Os <b>territórios</b> não são entes federados nem têm autonomia — são "
        "autarquias federais integrantes da União. O art. 18 CF/88 lista como autônomos apenas "
        "União, estados, DF e municípios.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q02-I</i>",
    ),
    (
        "[Exercício] II – Os territórios federais integram a União. A criação deles, a "
        "transformação em estado ou a reintegração ao estado de origem serão reguladas em "
        "lei ordinária.",
        "<b>ERRADO.</b> A criação de territórios segue as mesmas etapas da criação de estados "
        "(art. 18 §3): plebiscito com a população diretamente interessada + "
        "<b>lei complementar federal</b> (não lei ordinária).<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q02-II</i>",
    ),
    (
        "[Exercício] III – A organização e a manutenção dos serviços locais de segurança pública "
        "do DF (Polícia Militar, Polícia Penal, Polícia Civil e Corpo de Bombeiros) são de "
        "competência privativa do próprio DF.",
        "<b>ERRADO.</b> Pelo art. 21, XIV CF/88 e Súmula Vinculante 39 do STF, é competência "
        "da <b>União</b> organizar e manter as polícias e bombeiros do DF, bem como legislar "
        "sobre sua remuneração.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q02-III</i>",
    ),
    (
        "[Exercício] IV – Na organização da República Federativa do Brasil, os municípios são "
        "entes federados que não têm subordinação hierárquica frente à União nem aos "
        "estados-membros.",
        "<b>CERTO.</b> O STF tem entendimento sedimentado de que não existe hierarquia entre "
        "entes federados — todos têm o mesmo atributo: autonomia (art. 18 CF/88).<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Os Estados têm o poder de se unir, dividir-se ou desmembrar-se para se "
        "integrarem a outros estados, formarem novos estados ou territórios federais. Esse processo "
        "requer a aprovação da população envolvida por meio de plebiscito e a posterior aprovação "
        "do Congresso Nacional, por meio de uma lei complementar.",
        "<b>CERTO.</b> Art. 18 §3 CF/88: criação/fusão/desmembramento de estados exige "
        "plebiscito com a população diretamente interessada + lei complementar federal aprovada "
        "pelo Congresso Nacional.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q03-I</i>",
    ),
    (
        "[Exercício] II – Para que sejam alterados os limites territoriais de um município, é "
        "necessária a realização de consulta prévia, mediante referendo, às populações dos "
        "municípios envolvidos, nos termos da CF.",
        "<b>ERRADO.</b> O instrumento previsto no art. 18 §4 CF/88 é o <b>plebiscito</b> "
        "(consulta <i>prévia</i> à decisão), não referendo (consulta <i>posterior</i>). "
        "São institutos distintos (art. 14 CF/88).<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q03-II</i>",
    ),
    (
        "[Exercício] III – No Brasil, os estados têm plena autonomia para criar, organizar e "
        "extinguir municípios, desde que observem os requisitos estabelecidos pela Constituição "
        "Federal.",
        "<b>CERTO.</b> A criação de municípios é competência dos estados (via lei estadual "
        "ordinária), respeitadas as 4 etapas do art. 18 §4 CF/88: lei complementar federal "
        "fixando o período + estudo de viabilidade + plebiscito + lei estadual.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q03-III</i>",
    ),
    (
        "[Exercício] IV – No Brasil, os municípios são considerados elementos indissolúveis e "
        "divisíveis da federação.",
        "<b>CERTO.</b> <b>Indissolúveis</b>: não podem se separar da federação (art. 1 caput — "
        "proibição de secessão). <b>Divisíveis</b>: podem se fundir, dividir ou desmembrar "
        "conforme as regras do art. 18 §4 CF/88.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 02 Mar/2024, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Interno::Estado - Conceito e Formas",
        "Direito Interno - Estado Conceito e Formas.apkg",
        ESTADO_CONCEITO_FORMAS,
    )
