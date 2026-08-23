#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Nov/2023).

Tema: Responsabilidade Civil do Estado (Item 11 do Edital CACD).

Fontes:
  - Anotações: Responsabilidade Civil do Estado.md
  - Material do professor: Direito Interno_Rodada 01_Novembro 2023_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Novembro 2023.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelreichelt/Desktop/cacd-learning/anki/decks/direito interno"
os.makedirs(DECK_DIR, exist_ok=True)


def make_deck(deck_title, file_name, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        "CACD Direito Rodadas",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card",
            "qfmt": "{{Frente}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Verso}}",
        }],
    )
    deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_title)
    for frente, verso in cards:
        deck.add_note(genanki.Note(model=model, fields=[frente, verso]))
    out = f"{DECK_DIR}/{file_name}"
    genanki.Package(deck).write_to_file(out)
    print(f"✅ {file_name} — {len(cards)} cards")


RESPONSABILIDADE_CIVIL_ESTADO = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O Estado responde objetivamente por todo e qualquer dano decorrente de "
     "atos praticados por magistrados no exercício da função jurisdicional, "
     "sendo dispensável a demonstração de culpa ou dolo do juiz para a "
     "configuração do dever de indenizar.",
     "<b>ERRADO.</b> Embora o STF entenda que o Estado responde objetivamente "
     "por atos judiciais, o dever de indenizar só se configura nas duas "
     "hipóteses expressamente previstas no art. 5º, LXXV, CF/88: "
     "<b>erro judiciário</b> e <b>prisão que extrapole o tempo fixado na "
     "sentença</b> — não qualquer dano decorrente de ato jurisdicional. "
     "[Anotações da aula; Rodada 01/Nov.2023, p.6]"),

    ("O ordenamento jurídico brasileiro prevê expressamente a aplicação da "
     "teoria do risco integral em duas hipóteses: danos nucleares e danos "
     "decorrentes de atentados terroristas, atos de guerra ou eventos "
     "correlatos contra aeronaves de empresas aéreas brasileiras.",
     "<b>CERTO.</b> Art. 21, XXIII, \"d\", CF/88 (dano nuclear) e Leis nº "
     "10.309/2001 e 10.744/2003 (aeronaves) — casos em que o Estado é "
     "<b>garantidor universal</b> e não se admite nenhuma causa excludente "
     "ou minorante. [Anotações da aula; Rodada 01/Nov.2023, p.4-5]"),

    ("Nos termos do art. 37, §6º, CF/88, a vítima de dano causado por agente "
     "público pode optar por ajuizar a ação de indenização diretamente "
     "contra o agente causador do dano ou contra o Estado, sendo ambos "
     "partes legítimas passivas para a demanda.",
     "<b>ERRADO.</b> Segundo o STF (RE 1.027.633), a ação por danos causados "
     "por agente público deve ser ajuizada contra o Estado ou a pessoa "
     "jurídica de direito privado prestadora do serviço público, sendo o "
     "autor do ato (agente) parte <b>ilegítima</b> passiva — a vítima não "
     "pode demandar diretamente o agente. "
     "[Anotações da aula; Rodada 01/Nov.2023, p.4]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Nov/2023) ──────────────

    ("I – Para a configuração da obrigação da administração pública de "
     "reparar os danos eventualmente causados a terceiros é dispensável o "
     "elemento subjetivo da conduta do agente estatal. (C/E?)",
     "<b>CERTO.</b> A responsabilidade objetiva do Estado exige apenas 3 "
     "elementos cumulativos: (i) ato/fato administrativo; (ii) dano ou "
     "prejuízo; (iii) nexo de causalidade. Não se exige dolo ou culpa "
     "(elemento subjetivo) do agente causador. "
     "[Exercício Q01-I, Rodada 01 Nov/2023]"),

    ("II – A responsabilidade civil do Estado por ato comissivo é objetiva e "
     "baseada na teoria do risco administrativo, não se exigindo do "
     "particular, que foi a vítima, a comprovação da culpa ou dolo do agente "
     "público. (C/E?)",
     "<b>CERTO.</b> Nos termos do art. 37, §6º, CF/88, o Estado responde "
     "objetivamente pelos danos causados por seus agentes por ato comissivo "
     "— a vítima só precisa provar ato/fato administrativo, dano e nexo de "
     "causalidade. [Exercício Q01-II, Rodada 01 Nov/2023]"),

    ("III – Antes da Constituição Federal de 1988, adotava-se, no Brasil, a "
     "teoria do risco integral. (C/E?)",
     "<b>ERRADO.</b> De 1824 a 1946 vigoravam as teorias civilistas "
     "(responsabilidade subjetiva); de 1946 em diante, a teoria do "
     "<b>risco administrativo</b> (responsabilidade objetiva, art. 37, §6º). "
     "A teoria do risco integral só foi adotada a partir de 1988 (dano "
     "nuclear) e depois em 2001/2003 (aeronaves) — nunca antes de 1988. "
     "[Exercício Q01-III, Rodada 01 Nov/2023]"),

    ("IV – Em caso de dano causado a terceiros, responderá o servidor "
     "subjetivamente perante a fazenda pública, em ação regressiva. (C/E?)",
     "<b>CERTO.</b> A vítima não pode ajuizar ação diretamente contra o "
     "agente público — a ação principal é contra o Estado (responsabilidade "
     "objetiva). Em ação de regresso posterior, o agente só responde perante "
     "a Fazenda Pública se comprovada culpa ou dolo — responsabilidade "
     "<b>subjetiva</b>. [Exercício Q01-IV, Rodada 01 Nov/2023]"),

    ("I – Em virtude da observância do princípio da supremacia do interesse "
     "público, será integralmente excluída a responsabilidade civil do "
     "Estado nos casos de culpa – seja exclusiva, seja concorrente – da "
     "vítima atingida pelo dano. (C/E?)",
     "<b>ERRADO.</b> A culpa <b>exclusiva</b> da vítima é causa excludente "
     "(exclui totalmente); mas a culpa <b>concorrente</b> da vítima é apenas "
     "causa <b>minorante</b> — reduz proporcionalmente o valor da "
     "indenização, sem excluí-la integralmente. "
     "[Exercício Q02-I, Rodada 01 Nov/2023]"),

    ("II – Na realização de obra pública pelo próprio Estado, se, por fato "
     "natural ou imprevisível, for causado dano a terceiro, não haverá "
     "responsabilidade civil do Estado caso tenham sido observados todos os "
     "limites e os deveres pertinentes ao dever de diligência. Nesse "
     "sentido, certos eventos danosos, tais como tempestades e terremotos, "
     "são fatos capazes de gerar a exclusão da responsabilidade civil do "
     "Estado. (C/E?)",
     "<b>CERTO.</b> Caso fortuito ou força maior (evento imprevisível e "
     "incontrolável, como terremotos e tempestades) é uma das 3 causas "
     "excludentes da responsabilidade objetiva do Poder Público, por romper "
     "o nexo de causalidade. [Exercício Q02-II, Rodada 01 Nov/2023]"),

    ("III – A responsabilidade extracontratual do Estado corresponde à "
     "obrigação de reparar danos causados a terceiros em decorrência de "
     "comportamentos comissivos ou omissivos, materiais ou jurídicos, "
     "lícitos ou ilícitos, imputáveis aos agentes públicos. (C/E?)",
     "<b>CERTO.</b> A responsabilidade objetiva do Estado alcança tanto atos "
     "lícitos quanto ilícitos, comissivos (regra geral objetiva) quanto "
     "omissivos (regra geral subjetiva, salvo dever de atuação específico, "
     "como em estabelecimentos prisionais, onde é objetiva). "
     "[Exercício Q02-III, Rodada 01 Nov/2023]"),

    ("IV – Determinado detento que cumpria pena privativa de liberdade em "
     "regime fechado praticou suicídio. Segundo o entendimento do STF, "
     "considerando que o preso já vinha apresentando indícios de que "
     "poderia agir assim, o Estado deverá ser condenado a indenizar seus "
     "familiares. (C/E?)",
     "<b>CERTO.</b> O STF entende que a responsabilidade civil do Estado é "
     "<b>objetiva</b> no caso de omissão no cuidado de detentos em "
     "estabelecimentos prisionais, dado o dever de proteção do detento que o "
     "Estado não pode deixar de cumprir. [Exercício Q02-IV, Rodada 01 "
     "Nov/2023]"),

    ("I – Em regra, os atos de multidão ensejam a responsabilidade objetiva "
     "do Estado, em razão do dever de vigilância permanente da "
     "administração pública. (C/E?)",
     "<b>ERRADO.</b> Danos provocados por atos de multidão ensejam "
     "responsabilidade civil <b>subjetiva</b> do Estado — só há "
     "responsabilização se comprovado que o Estado não adotou medidas para "
     "conter a multidão (negligência) ou que agentes estatais estimularam a "
     "atuação danosa (dolo). O dever de vigilância permanente (objetivo) "
     "aplica-se a estabelecimentos prisionais, não a atos de multidão. "
     "[Exercício Q03-I, Rodada 01 Nov/2023]"),

    ("II – As empresas públicas e as sociedades de economia mista que se "
     "dediquem à exploração da atividade econômica estarão sujeitas à "
     "responsabilidade subjetiva comum do Direito Civil. (C/E?)",
     "<b>CERTO.</b> Empresas estatais que exploram atividade econômica "
     "(não prestam serviço público) respondem pelos danos causados por seus "
     "agentes do mesmo modo que as empresas privadas — responsabilidade "
     "civil subjetiva, sem aplicação da teoria do risco administrativo. "
     "[Exercício Q03-II, Rodada 01 Nov/2023]"),

    ("III – Caso lei impessoal, abstrata, dotada de generalidades e que não "
     "tenha sido julgada inconstitucional pelo STF gere dano a cidadão, ele "
     "não terá direito à indenização do Estado. (C/E?)",
     "<b>CERTO.</b> A responsabilidade subjetiva do Estado por atos "
     "legislativos exige 2 requisitos cumulativos: declaração de "
     "inconstitucionalidade da lei/ato normativo, e prova de culpa ou dolo "
     "do legislador. Sem a declaração de inconstitucionalidade, não cabe "
     "ação de indenização. [Exercício Q03-III, Rodada 01 Nov/2023]"),

    ("IV – A alegação de caso fortuito ou força maior constitui hipótese de "
     "exclusão da responsabilidade civil do Estado, na modalidade de risco "
     "integral. (C/E?)",
     "<b>ERRADO.</b> Na teoria do <b>risco integral</b>, não se admitem "
     "causas excludentes nem minorantes — o Estado responde integralmente "
     "mesmo havendo caso fortuito, força maior, culpa exclusiva ou "
     "concorrente da vítima ou de terceiro. Caso fortuito/força maior só é "
     "excludente na teoria do <b>risco administrativo</b> (regra geral). "
     "[Exercício Q03-IV, Rodada 01 Nov/2023]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Responsabilidade Civil do Estado",
        "Direito Interno - Responsabilidade Civil do Estado.apkg",
        RESPONSABILIDADE_CIVIL_ESTADO,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
