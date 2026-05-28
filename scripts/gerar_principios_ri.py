#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Principios das Relacoes Internacionais"""

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


PRINCIPIOS_RI = [
    # ── CONCEITOS ──────────────────────────────────────────────────────────────
    (
        "O que é o Art. 4 da CF/88 e qual seu significado histórico?",
        "Primeiro dispositivo constitucional brasileiro a reger a atuação do Brasil no cenário internacional. "
        "Os princípios listados já estavam na Carta da ONU (arts. 1 e 2) desde 1945; "
        "a inclusão do art. 4 marcou a reinserção do Brasil na ordem internacional.<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "Quais são os 10 princípios das relações internacionais do Brasil previstos no Art. 4 da CF/88?",
        "1. Independência nacional<br>2. Prevalência dos DH<br>3. Autodeterminação dos povos<br>"
        "4. Não-intervenção<br>5. Igualdade soberana dos povos<br>6. Defesa da paz<br>"
        "7. Solução pacífica dos conflitos<br>8. Repúdio ao terrorismo<br>"
        "9. Cooperação entre os povos para o progresso da humanidade<br>10. Concessão de asilo político.<br>"
        "<i>Fonte: Art. 4, I–X, CF/88</i>",
    ),
    (
        "O que prevê o parágrafo único do Art. 4 da CF/88?",
        "Promover a integração política, econômica, social e cultural com os povos da <b>América Latina</b>, "
        "visando formar uma comunidade latino-americana de nações.<br>"
        "<i>Fonte: Art. 4, parágrafo único, CF/88</i>",
    ),
    (
        "O que são princípios como 'mandamentos de otimização' segundo Robert Alexy?",
        "Comandos normativos abertos que exigem concretização e aplicação progressiva, "
        "aperfeiçoando o ordenamento jurídico. O art. 4 CF/88 orienta os 3 poderes na atuação internacional — "
        "não apenas o Executivo.<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "Quem é a autora de referência para os princípios constitucionais das relações internacionais do Brasil?",
        "<b>Flávia Piovesan</b>.<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "Como o Poder Executivo aplica os princípios do Art. 4 CF/88 em relação a tratados de DH?",
        "Celebra tratados internacionais e indica ao Congresso Nacional tratados de DH para votação "
        "<b>2-2-⅗</b> (aprovação como emenda constitucional, conforme art. 5, §3º, CF/88).<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "O que decidiu o STF na ADI 1625 (2023) sobre a denúncia de tratados internacionais?",
        "Ampliou a competência do Congresso (art. 49, I, CF/88): além de autorizar a <b>ratificação</b>, "
        "o Congresso Nacional também pode autorizar a <b>denúncia</b> de tratados por decreto legislativo.<br>"
        "<i>Fonte: STF, ADI 1625 (2023)</i>",
    ),
    (
        "Qual o status dos tratados internacionais de direitos humanos não incorporados como emenda "
        "constitucional, segundo o STF?",
        "Status <b>supralegal</b>: acima das leis ordinárias, mas abaixo da Constituição Federal. "
        "Ex.: Pacto de São José da Costa Rica (1969), convenções da OIT, tratados de meio ambiente.<br>"
        "<i>Fonte: STF – RE 466.343</i>",
    ),
    (
        "Qual é o principal tratado do Sistema Interamericano de Proteção aos DH? Qual seu status no Brasil?",
        "<b>Pacto de São José da Costa Rica (1969)</b>. Status supralegal, pois não foi votado como emenda "
        "constitucional.<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "O que é o controle de convencionalidade da legislação brasileira?",
        "Análise, por juízes e tribunais, da compatibilidade entre leis internas e tratados de DH. "
        "Se houver incompatibilidade, o juiz deixa de aplicar a lei interna (<b>efeito paralisante</b>).<br>"
        "<i>Fonte: Anotações – Princípios das Relações Internacionais</i>",
    ),
    (
        "O que diz o STJ sobre a atuação dos juízes brasileiros em relação ao Pacto de São José da Costa Rica?",
        "Os juízes brasileiros devem atuar como <b>juízes interamericanos</b>, aplicando internamente "
        "o Pacto de São José da Costa Rica.<br>"
        "<i>Fonte: STJ – jurisprudência sobre controle de convencionalidade</i>",
    ),
    (
        "Em que circunstância o STF flexibilizou a imunidade de jurisdição de Estados soberanos?",
        "Quando atos de império (ex.: atos de guerra) praticados por Estado estrangeiro no Brasil "
        "<b>importem violação aos direitos humanos</b> — o Brasil afasta a imunidade e admite o julgamento.<br>"
        "<i>Fonte: STF – Caso Changri-lá</i>",
    ),
    (
        "O que foi o caso Changri-lá e qual sua importância?",
        "Em 1943, a Alemanha naufragou um barco pesqueiro brasileiro durante a 2ª Guerra. "
        "O STF aplicou o art. 4, II, CF/88 (prevalência dos DH) para garantir indenização aos familiares, "
        "afastando a imunidade de jurisdição da Alemanha por ato de império que violou DH.<br>"
        "<i>Fonte: STF – Caso Changri-lá</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – A garantia do desenvolvimento nacional é um princípio que rege as relações "
        "internacionais da República Federativa do Brasil.",
        "<b>ERRADO.</b> O art. 4 CF/88 não prevê 'garantia do desenvolvimento nacional' entre os princípios "
        "das relações internacionais. 'Desenvolvimento nacional' é objetivo fundamental da República (art. 3, II).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q01-I</i>",
    ),
    (
        "[Exercício] II – A concessão de asilo político e de refúgio é um dos princípios previstos no texto "
        "constitucional para orientar a atuação da República Federativa do Brasil nas suas relações internacionais.",
        "<b>ERRADO.</b> O art. 4, X, CF/88 prevê apenas a concessão de <b>asilo político</b>, não de refúgio. "
        "O refúgio é instituto distinto, regulado pela Lei 9.474/1997.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q01-II</i>",
    ),
    (
        "[Exercício] III – A soberania não consta como um dos princípios que regem as relações internacionais "
        "da República Federativa do Brasil.",
        "<b>CERTO.</b> A soberania é fundamento da República (art. 1, I, CF/88). O art. 4 traz a "
        "'igualdade soberana dos povos', mas não a soberania nacional como princípio isolado das relações "
        "internacionais.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q01-III</i>",
    ),
    (
        "[Exercício] IV – O repúdio ao terrorismo autorizará, no plano internacional, intervenção armada "
        "pelo Brasil.",
        "<b>ERRADO.</b> O repúdio ao terrorismo (art. 4, VIII) coexiste com a não-intervenção (art. 4, IV) "
        "e a solução pacífica de conflitos (art. 4, VII). O Brasil não pode intervir militarmente com base "
        "nesse princípio isolado.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – A denúncia pelo Presidente da República de tratados internacionais aprovados pelo "
        "Congresso Nacional, para que produza efeitos no ordenamento jurídico interno, não prescinde da sua "
        "aprovação pelo Congresso.",
        "<b>CERTO.</b> Segundo o STF (ADI 1625, 2023), a denúncia de tratados pelo Presidente requer "
        "autorização do Congresso Nacional via decreto legislativo, ampliando a competência do art. 49, I, CF/88.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q02-I</i>",
    ),
    (
        "[Exercício] II – A concessão de refúgio, bem como a concessão de asilo político constituem fatores "
        "obstativos da extradição de estrangeiro.",
        "<b>CERTO.</b> Tanto o asilo político (art. 4, X, CF/88) quanto o refúgio (Lei 9.474/1997) "
        "impedem a extradição do beneficiário.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q02-II</i>",
    ),
    (
        "[Exercício] III – Segundo a jurisprudência do STF, os tratados internacionais de proteção ao meio "
        "ambiente e as convenções da Organização Internacional do Trabalho (OIT) possuem status supralegal e "
        "infraconstitucional no ordenamento jurídico brasileiro.",
        "<b>CERTO.</b> O STF consolidou o status supralegal para tratados de DH não aprovados como emenda, "
        "incluindo convenções da OIT e tratados de meio ambiente quando tocam em direitos fundamentais.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q02-III</i>",
    ),
    (
        "[Exercício] IV – A EC nº 45/2004, ao prever que o Brasil se submete à jurisdição de Tribunal Penal "
        "Internacional a cuja criação tenha manifestado adesão, inovou ao prever, pela primeira vez no texto "
        "constitucional, o compromisso da República Federativa do Brasil com a atuação de tribunais internacionais.",
        "<b>ERRADO.</b> O compromisso com o TPI já constava do art. 7 dos ADCT da CF/88 original (1988). "
        "A EC 45/2004 o incorporou ao corpo permanente (art. 5, §4º), mas não inovou.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – De acordo com o STF, a regra internacional imunizante de jurisdição em relação a "
        "atos de império praticados por Estado soberano não alcança graves delitos ocorridos em confronto à "
        "proteção internacional da pessoa natural.",
        "<b>CERTO.</b> O STF (caso Changri-lá) flexibilizou a imunidade de jurisdição: quando atos de "
        "império violam gravemente os DH, o Brasil afasta a imunidade e admite o julgamento do Estado "
        "estrangeiro.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q03-I</i>",
    ),
    (
        "[Exercício] II – Entre os princípios constitucionais que regem as relações internacionais do Brasil, "
        "insere-se o da não intervenção, cuja pedra basilar é a soberania nacional. Por isso, o Brasil não "
        "pode, sozinho ou em grupo com outros países, intervir, direta ou indiretamente, independentemente "
        "do motivo, nos assuntos internos ou externos de qualquer outro país.",
        "<b>ERRADO.</b> A não-intervenção não é absoluta. O Brasil pode apoiar intervenções autorizadas "
        "pelo CSNU, e o próprio art. 4 prevê a prevalência dos DH, que pode justificar ações coletivas "
        "em casos extremos.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q03-II</i>",
    ),
    (
        "[Exercício] III – A concessão de asilo político a estrangeiro é princípio que rege a República "
        "Federativa do Brasil nas suas relações internacionais, mas, como ato de soberania estatal, o Estado "
        "brasileiro não está obrigado a realizá-lo.",
        "<b>CERTO.</b> O asilo político é princípio constitucional (art. 4, X), mas sua concessão é "
        "<b>ato discricionário</b> de soberania — o Brasil não é obrigado a concedê-lo em todo e qualquer "
        "caso.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q03-III</i>",
    ),
    (
        "[Exercício] IV – O pan-americanismo é rigidamente acolhido como norma de política externa, com a "
        "previsão da integração econômica, política, social e cultural de todos os povos do continente, para "
        "o progresso da humanidade, com a formação de blocos econômicos e de associações regionais, como o "
        "MERCOSUL e a UNASUL.",
        "<b>ERRADO.</b> O parágrafo único do art. 4 limita a integração à <b>América Latina</b> (não a "
        "todo o continente americano). Além disso, é objetivo de política externa, não norma rígida.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Ago/2023, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Direito Internacional :: Princípios das Relações Internacionais",
        "Direito Internacional - Principios das Relacoes Internacionais.apkg",
        PRINCIPIOS_RI,
    )
