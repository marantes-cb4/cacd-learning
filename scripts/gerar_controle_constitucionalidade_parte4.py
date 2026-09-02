#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Jan/2025).

Tema: Primado da Constituição. Controle de Constitucionalidade — controle
abstrato ou concentrado (Item 3 do Edital CACD). Continuação de
gerar_controle_constitucionalidade_parte3.py (Parte 3).

Fontes:
  - Anotações: Controle de Constitucionalidade - Parte 4.md
  - Material do professor: Direito Interno_Rodada 01_Janeiro_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Janeiro_2025.pdf
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


CONTROLE_CONSTITUCIONALIDADE_PARTE4 = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O controle abstrato ou concentrado de constitucionalidade, idealizado "
     "por Hans Kelsen e adotado pela primeira vez na Constituição austríaca "
     "de 1920, compartilha a mesma lógica do controle difuso "
     "norte-americano quanto aos efeitos da declaração de "
     "inconstitucionalidade: em ambos os modelos, apenas quem provocou o "
     "Poder Judiciário fica isento de cumprir a lei declarada "
     "inconstitucional.",
     "<b>ERRADO.</b> É o oposto: no modelo <b>kelseniano</b>, lei "
     "declarada inconstitucional deixa de valer para TODOS (garantindo "
     "igualdade entre os sujeitos); no modelo <b>norte-americano</b> "
     "(difuso), só quem processou fica isento — os demais continuam "
     "sujeitos à lei. [Anotações da aula; Rodada 01/Jan.2025]"),

    ("Para o ajuizamento de ação declaratória de constitucionalidade "
     "(ADC), a Lei 9.868/99 exige que o legitimado comprove a existência de "
     "divergência judicial relevante sobre a aplicação da lei federal "
     "questionada, prova que pode ser feita mediante a apresentação de "
     "julgados contraditórios expedidos por, pelo menos, dois tribunais "
     "distintos.",
     "<b>CERTO.</b> Art. 14, III, Lei 9.868/99 — requisito específico de "
     "admissibilidade da ADC, cuja finalidade é resolver divergência já "
     "instalada entre tribunais sobre a constitucionalidade de uma lei "
     "federal. [Anotações da aula; Rodada 01/Jan.2025]"),

    ("Julgada procedente a ação direta de inconstitucionalidade por "
     "omissão (ADO), a sentença do STF produzirá sempre a mesma "
     "consequência jurídica, independentemente de a omissão inconstitucional "
     "consistir na ausência de lei regulamentadora ou na ausência de ato "
     "administrativo: em ambos os casos, o STF apenas dará ciência ao poder "
     "competente para que este adote as providências necessárias, sem "
     "fixação de prazo.",
     "<b>ERRADO.</b> A consequência VARIA conforme o tipo de omissão (art. "
     "103, §2º, CF/88): se a omissão é LEGISLATIVA, o STF só dá ciência ao "
     "poder competente (por separação de poderes); se a omissão é de ATO "
     "ADMINISTRATIVO, o STF fixa PRAZO DE 30 DIAS para o órgão "
     "administrativo suprir a falta. [Anotações da aula; Rodada "
     "01/Jan.2025]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jan/2025) ──────────────

    ("01-I – Caracterizará exercício do controle abstrato de "
     "constitucionalidade a apreciação da constitucionalidade das leis e "
     "atos normativos do poder público pelos tribunais de contas, desde "
     "que no exercício de suas atribuições. (C/E?)",
     "<b>ERRADO.</b> Só STF (parâmetro CF) e TJ estadual (parâmetro "
     "Constituição estadual) fazem controle abstrato. Tribunais de Contas "
     "(Súmula 347/STF) atuam apenas no controle <b>concreto/difuso</b>. "
     "[Exercício Q01-I, Rodada 01 Jan/2025]"),

    ("01-II – O advogado-geral da União tem legitimidade universal para "
     "ajuizar ADPF. (C/E?)",
     "<b>ERRADO.</b> O AGU NÃO consta no rol do art. 103, CF/88 — não pode "
     "ajuizar nenhuma das 5 ações típicas. Sua função é defender a lei "
     "impugnada na ADI (curador da norma), salvo se já houver decisão "
     "prévia do STF pela inconstitucionalidade. [Exercício Q01-II, Rodada "
     "01 Jan/2025]"),

    ("01-III – Ao governador de estado é permitido questionar, por via "
     "principal e concentrada, a validade de determinada lei, ainda que "
     "não tenha vetado, na ocasião própria, o projeto dessa lei. (C/E?)",
     "<b>CERTO.</b> Governador é legitimado especial (art. 103) para ADI "
     "de lei estadual — é irrelevante ele ter sancionado a lei "
     "anteriormente. [Exercício Q01-III, Rodada 01 Jan/2025]"),

    ("01-IV – Na ADI, a causa de pedir é aberta, e a decisão de mérito "
     "proferida nessa ação tem natureza dúplice, ou seja, produz eficácia "
     "jurídica, seja quando é dado provimento à ação, seja quando lhe é "
     "negado provimento. (C/E?)",
     "<b>CERTO.</b> Procedência (inconstitucional) ou improcedência "
     "(constitucional) — ambas produzem efeitos erga omnes/vinculantes; é "
     "a natureza dúplice/ambivalente da ADI (espelhada na ADC). [Exercício "
     "Q01-IV, Rodada 01 Jan/2025]"),

    ("02-I – As decisões de mérito em ADPF não vinculam o Poder Legislativo "
     "em sua função típica de legislar. (C/E?)",
     "<b>CERTO.</b> Os efeitos vinculantes do art. 102, §2º excluem o "
     "LEGISLADOR — o Legislativo pode criar nova lei de teor idêntico a "
     "outra já declarada inconstitucional. [Exercício Q02-I, Rodada 01 "
     "Jan/2025]"),

    ("02-II – Declarada no todo ou em parte a inconstitucionalidade em "
     "abstrato de lei ou ato normativo estadual ou municipal, o Poder "
     "Legislativo responsável pela sua emissão terá de ser comunicado com "
     "vistas à suspensão da execução dos textos invalidados. (C/E?)",
     "<b>ERRADO.</b> Como o STF atua como \"legislador negativo\" "
     "(Kelsen), a própria sentença RETIRA a lei do ordenamento — não há "
     "necessidade de comunicar o Legislativo para suspender a execução. "
     "[Exercício Q02-II, Rodada 01 Jan/2025]"),

    ("02-III – Tratando-se de controle concentrado de constitucionalidade "
     "de leis ou atos normativos, o requerente da ação ajuizada não pode "
     "pleitear a desistência do pedido. (C/E?)",
     "<b>CERTO.</b> Princípio da indisponibilidade — ações do controle "
     "concentrado, uma vez ajuizadas, não admitem desistência. [Exercício "
     "Q02-III, Rodada 01 Jan/2025]"),

    ("02-IV – Dado o princípio da unidade da CF, norma constitucional "
     "originária não pode ser objeto de ADI. (C/E?)",
     "<b>CERTO.</b> Normas constitucionais originárias nunca podem ser "
     "declaradas inconstitucionais; só as derivadas (emendas, "
     "Constituições estaduais) podem. [Exercício Q02-IV, Rodada 01 "
     "Jan/2025]"),

    ("03-I – A ação de inconstitucionalidade interventiva, que tem como "
     "único legitimado ativo o procurador-geral da República, está "
     "fundamentada na violação de um princípio sensível por parte de "
     "estado-membro ou do DF. (C/E?)",
     "<b>CERTO.</b> IF (art. 36, III): único legitimado é o PGR; cabível "
     "por recusa a executar lei federal OU violação de princípio "
     "constitucional sensível (art. 34, VII). [Exercício Q03-I, Rodada 01 "
     "Jan/2025]"),

    ("03-II – No âmbito do STF, não é cabível ADI em face de lei distrital "
     "cuja matéria seja derivada de competência legislativa municipal, "
     "entretanto podem ser impugnadas mediante ADI as leis distritais "
     "editadas pelo DF no desempenho de sua competência estadual. (C/E?)",
     "<b>CERTO.</b> Lei distrital de matéria ESTADUAL → ADI no STF; lei "
     "distrital de matéria MUNICIPAL → ADPF no STF (nunca ADI). [Exercício "
     "Q03-II, Rodada 01 Jan/2025]"),

    ("03-III – São objeto de ADI: atos normativos primários; tratados "
     "internacionais, atos normativos federais, regimento interno, decreto "
     "autônomo; leis ou atos normativos anteriores a 5/10/1988; "
     "constituições e leis estaduais, decretos (com força de lei) e atos "
     "normativos estaduais. (C/E?)",
     "<b>ERRADO.</b> ADI tem como objeto só leis/atos FEDERAIS e "
     "ESTADUAIS — direito PRÉ-CONSTITUCIONAL (anterior a 5/10/1988) NÃO "
     "pode ser objeto de ADI, pois é caso de não recepção (revogação), "
     "questionável via ADPF. [Exercício Q03-III, Rodada 01 Jan/2025]"),

    ("03-IV – É cabível a arguição de descumprimento de preceito "
     "fundamental (ADPF) para se obter a revisão ou o cancelamento de "
     "súmula vinculante, haja vista os efeitos erga omnes e a eficácia "
     "vinculante desses enunciados. (C/E?)",
     "<b>ERRADO.</b> Súmula vinculante não é lei/ato normativo — não pode "
     "ser objeto de nenhuma das 5 ações típicas. Revisão/cancelamento se "
     "dá por via administrativa do próprio STF (art. 103-A, CF/88). "
     "[Exercício Q03-IV, Rodada 01 Jan/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Controle de Constitucionalidade - Parte 4",
        "Direito Interno - Controle de Constitucionalidade - Parte 4.apkg",
        CONTROLE_CONSTITUCIONALIDADE_PARTE4,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
