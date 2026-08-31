#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Dez/2024).

Tema: Primado da Constituição. Controle de Constitucionalidade — controle
concreto/difuso, direito pré-constitucional e cláusula de reserva de
plenário (Item 3 do Edital CACD). Continuação de
gerar_controle_constitucionalidade_parte2.py (Parte 2).

Fontes:
  - Anotações: Controle de Constitucionalidade - Parte 3.md
  - Material do professor: Direito Interno_Rodada 01_Dezembro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Dezembro_2024.pdf
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


CONTROLE_CONSTITUCIONALIDADE_PARTE3 = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O controle concreto ou difuso de constitucionalidade, surgido nos "
     "Estados Unidos a partir do julgamento do caso Marbury vs. Madison em "
     "1803, decorreu da aplicação de dispositivo expresso da Constituição "
     "norte-americana de 1787 que atribuía à Suprema Corte a competência "
     "para declarar leis inconstitucionais.",
     "<b>ERRADO.</b> A Constituição dos EUA de 1787 NÃO previa "
     "expressamente esse controle — foi <b>construção jurisprudencial</b> "
     "da própria Suprema Corte, a partir do reconhecimento pretoriano do "
     "princípio da supremacia da constituição. [Anotações da aula; Rodada "
     "01/Dez.2024]"),

    ("A declaração de não recepção constitucional e a declaração de "
     "inconstitucionalidade de uma lei pré-constitucional produzem os "
     "mesmos efeitos jurídicos, já que ambas reconhecem que a norma "
     "pré-constitucional é incompatível com uma Constituição e não pode "
     "mais ser aplicada.",
     "<b>ERRADO.</b> Os efeitos são diferentes: a <b>não recepção</b> "
     "(parâmetro = CF/88) equivale a uma <b>revogação</b>, com efeitos "
     "<b>ex-nunc</b>; a <b>inconstitucionalidade</b> (parâmetro = "
     "Constituição vigente à época da criação da lei) equivale a "
     "<b>nulidade</b>, com efeitos <b>ex-tunc</b>. [Anotações da aula; "
     "Rodada 01/Dez.2024]"),

    ("Sempre que um órgão fracionário de tribunal se depara com questão de "
     "inconstitucionalidade em um caso concreto, deve necessariamente "
     "suspender o julgamento e instaurar incidente de inconstitucionalidade "
     "perante o plenário, ainda que já exista decisão prévia do próprio "
     "plenário do tribunal ou do STF sobre a mesma lei.",
     "<b>ERRADO.</b> Se já existe decisão PRÉVIA do plenário/órgão "
     "especial do próprio tribunal, ou do STF, sobre a MESMA lei, o órgão "
     "fracionário pode aplicar essa decisão diretamente, sem novo "
     "incidente — porque está apenas implementando entendimento já "
     "fixado (\"cascateamento\"), e não decidindo a inconstitucionalidade "
     "por si só. [Anotações da aula; Rodada 01/Dez.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Dez/2024) ──────────────

    ("01-I – No controle incidental ou concreto, a questão de "
     "constitucionalidade somente pode ser suscitada pelas partes da "
     "relação processual. (C/E?)",
     "<b>ERRADO.</b> Além das partes, pode ser suscitada pelo Ministério "
     "Público (<i>custus legis</i>) ou reconhecida <b>de ofício</b> pelo "
     "juiz. [Exercício Q01-I, Rodada 01 Dez/2024]"),

    ("01-II – O ordenamento jurídico nacional admite o controle concreto "
     "ou difuso de constitucionalidade de normas produzidas tanto pelo "
     "poder constituinte originário, quanto pelo derivado. (C/E?)",
     "<b>ERRADO.</b> Normas constitucionais <b>originárias</b> NUNCA podem "
     "ser declaradas inconstitucionais (poder constituinte originário é "
     "ilimitado); apenas normas <b>derivadas</b> (emendas, Constituições "
     "estaduais) podem. [Exercício Q01-II, Rodada 01 Dez/2024]"),

    ("01-III – O STF admite a modulação dos efeitos temporais da "
     "declaração de inconstitucionalidade no controle concreto ou difuso. "
     "(C/E?)",
     "<b>CERTO.</b> Embora o art. 27 da Lei 9.868/99 trate da modulação no "
     "âmbito da ADI (exigindo 2/3 dos Ministros do STF), o STF admite que "
     "<b>qualquer juiz</b>, em qualquer grau, module temporalmente os "
     "efeitos de sua sentença no controle difuso, por decisão monocrática, "
     "para preservar segurança jurídica ou interesse social excepcional. "
     "[Exercício Q01-III, Rodada 01 Dez/2024]"),

    ("01-IV – O controle difuso de constitucionalidade, que é exercido "
     "somente perante caso concreto, pode ocorrer por meio das ações "
     "constitucionais do habeas corpus e do mandado de segurança. (C/E?)",
     "<b>CERTO.</b> No controle difuso não há ação típica (via de defesa "
     "ou exceção) — qualquer ação, inclusive HC e MS, pode veicular a "
     "questão incidental de inconstitucionalidade. [Exercício Q01-IV, "
     "Rodada 01 Dez/2024]"),

    ("02-I – O modelo norte-americano de controle de constitucionalidade "
     "é classificado em concreto, incidental e repressivo. (C/E?)",
     "<b>CERTO.</b> Surgido em Marbury vs. Madison (1803), é controle "
     "concreto (caso real), incidental (questão prejudicial ao mérito) e "
     "repressivo (após a vigência da lei). [Exercício Q02-I, Rodada 01 "
     "Dez/2024]"),

    ("02-II – O sistema jurisdicional instituído com a CF, influenciado "
     "pelo constitucionalismo norte-americano, acolheu exclusivamente o "
     "critério de controle de constitucionalidade difuso, ou seja, por via "
     "de exceção. (C/E?)",
     "<b>ERRADO.</b> A CF/88 adota <b>2 sistemas concomitantes</b>: "
     "difuso/concreto (efeitos inter partes, não retira a lei) e "
     "abstrato/concentrado (efeitos erga omnes, retira a lei do "
     "ordenamento) — não é exclusivamente difuso. [Exercício Q02-II, "
     "Rodada 01 Dez/2024]"),

    ("02-III – O controle difuso de constitucionalidade somente pode ser "
     "realizado pelos tribunais do Poder Judiciário, em atenção à cláusula "
     "de reserva de plenário. (C/E?)",
     "<b>ERRADO.</b> Qualquer órgão do Judiciário, em qualquer grau — "
     "inclusive juízes de 1º grau — pode realizar o controle difuso; não "
     "é exclusivo dos tribunais. [Exercício Q02-III, Rodada 01 Dez/2024]"),

    ("02-IV – Conforme a cláusula de reserva de plenário, o juiz singular "
     "de primeiro grau não pode, incidentalmente, declarar a "
     "inconstitucionalidade de lei ou ato normativo em um caso concreto, "
     "salvo se já houver precedente no mesmo sentido do pleno ou órgão "
     "especial do tribunal ao qual o magistrado se encontre vinculado ou "
     "do STF. (C/E?)",
     "<b>ERRADO.</b> A cláusula de reserva de plenário (art. 97) só se "
     "aplica a <b>Tribunais</b> — o juiz singular pode SEMPRE declarar "
     "inconstitucionalidade por decisão monocrática, sem qualquer "
     "restrição ou necessidade de precedente. [Exercício Q02-IV, Rodada "
     "01 Dez/2024]"),

    ("03-I – Se uma turma de um tribunal regional federal, ainda que não "
     "tenha declarado expressamente determinada lei inconstitucional, "
     "afastar a sua aplicação em julgamento de um caso concreto, tal "
     "decisão violará cláusula constitucional de reserva de plenário. "
     "(C/E?)",
     "<b>CERTO.</b> Súmula Vinculante 10/STF: viola a reserva de plenário "
     "afastar a incidência da lei, no todo ou em parte, mesmo sem "
     "declaração expressa de inconstitucionalidade. [Exercício Q03-I, "
     "Rodada 01 Dez/2024]"),

    ("03-II – A cláusula de reserva de plenário não deve ser observada "
     "nos casos em que o tribunal conclua que determinada norma "
     "pré-constitucional não foi recepcionada pela CF/88. (C/E?)",
     "<b>CERTO.</b> Não recepção equivale a revogação, não a declaração "
     "de inconstitucionalidade/nulidade — por isso dispensa a reserva de "
     "plenário. [Exercício Q03-II, Rodada 01 Dez/2024]"),

    ("03-III – O controle incidental de constitucionalidade de uma lei "
     "somente pode ser realizado em face da Constituição vigente, e não de "
     "Constituição anterior, já revogada. (C/E?)",
     "<b>ERRADO.</b> Para o direito pré-constitucional, a declaração de "
     "<b>inconstitucionalidade</b> usa como parâmetro a Constituição "
     "vigente NO MOMENTO da criação da lei (já revogada), não a atual — "
     "só é possível via controle concreto/difuso. [Exercício Q03-III, "
     "Rodada 01 Dez/2024]"),

    ("03-IV – O controle incidental de constitucionalidade pode ser "
     "exercido em relação a normas emanadas dos três níveis de poder, de "
     "qualquer hierarquia, inclusive às anteriores à Constituição Federal. "
     "(C/E?)",
     "<b>CERTO.</b> Abrange inclusive o direito pré-constitucional — seja "
     "para declará-lo não recepcionado (parâmetro CF/88) seja "
     "inconstitucional (parâmetro Constituição da época). [Exercício "
     "Q03-IV, Rodada 01 Dez/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Controle de Constitucionalidade - Parte 3",
        "Direito Interno - Controle de Constitucionalidade - Parte 3.apkg",
        CONTROLE_CONSTITUCIONALIDADE_PARTE3,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
