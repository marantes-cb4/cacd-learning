#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Out/2024).

Tema: Primado da Constituição. Controle de Constitucionalidade
(Item 3 do Edital CACD).

Fontes:
  - Anotações: Controle de Constitucionalidade.md
  - Material do professor: Direito Interno_Rodada 01_Outubro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Outubro_2024.pdf
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


CONTROLE_DE_CONSTITUCIONALIDADE = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Diante de uma hipótese de inconstitucionalidade por omissão, tanto a ação "
     "direta de inconstitucionalidade por omissão (ADO) quanto o mandado de "
     "injunção configuram instrumentos de controle concentrado ou abstrato de "
     "constitucionalidade, sendo ambos julgados exclusivamente pelo STF.",
     "<b>ERRADO.</b> A ADO (art. 103, §2º, CF/88) é julgada exclusivamente pelo "
     "STF, no controle <b>concentrado/abstrato</b>. Já o mandado de injunção "
     "(art. 5º, LXXI, CF/88) pode ser ajuizado perante qualquer órgão do Poder "
     "Judiciário, no caso concreto, integrando o controle <b>difuso/concreto</b> "
     "de constitucionalidade. [Anotações da aula; Rodada 01/Out.2024, p.5-6]"),

    ("Segundo entendimento consolidado do STF, as normas constitucionais "
     "originárias — criadas pelo poder constituinte originário na Assembleia "
     "Nacional Constituinte de 1987/1988 — podem ser declaradas "
     "inconstitucionais caso contrariem cláusulas pétreas previstas na própria "
     "Constituição, tese conhecida como \"normas constitucionais "
     "inconstitucionais\".",
     "<b>ERRADO.</b> O STF rechaça a tese das \"normas constitucionais "
     "inconstitucionais\" (Otto Bachof). As normas constitucionais originárias "
     "são <b>imunes</b> ao controle de constitucionalidade, por serem fruto do "
     "poder constituinte originário, juridicamente ilimitado (STF, ADI 815). "
     "Apenas as normas constitucionais <b>derivadas</b> (emendas, Constituições "
     "Estaduais, emendas de revisão) se submetem ao controle. "
     "[Anotações da aula; Rodada 01/Out.2024, p.2 e 9]"),

    ("O paradigma ou parâmetro do controle de constitucionalidade no Brasil é "
     "formado exclusivamente pelo texto da Constituição Federal de 1988, não "
     "sendo admitida a inclusão de tratados internacionais de direitos humanos "
     "nesse parâmetro, ainda que aprovados pelo rito do art. 5º, §3º, CF/88.",
     "<b>ERRADO.</b> A doutrina utiliza o conceito de <b>bloco de "
     "constitucionalidade</b> como parâmetro do controle: além do texto "
     "constitucional, integram-no os tratados de direitos humanos equiparados a "
     "emenda constitucional — isto é, aprovados em 2 turnos, nas 2 Casas do "
     "Congresso, por quórum de 3/5 dos respectivos membros (art. 5º, §3º, "
     "CF/88). [Anotações da aula; Rodada 01/Out.2024, p.1]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Out/2024) ──────────────────

    ("I – Mesmo que a CF/88 fosse classificada como flexível, seria legítimo o "
     "controle de constitucionalidade de seu sistema jurídico. (C/E?)",
     "<b>ERRADO.</b> O controle de constitucionalidade exige 02 pressupostos: "
     "supremacia da Constituição e <b>rigidez constitucional</b>. Uma "
     "Constituição flexível — alterável por lei ordinária ou complementar — não "
     "admite a realização do controle de constitucionalidade das leis e atos "
     "normativos. [Exercício Q01-I, Rodada 01 Out/2024]"),

    ("II – O controle de constitucionalidade está ligado à supremacia da CF/88 "
     "sobre todas as leis e normas jurídicas. (C/E?)",
     "<b>CERTO.</b> Por força do princípio da supremacia da Constituição, todas "
     "as leis e atos normativos que integram o ordenamento jurídico devem ser "
     "compatíveis com a Constituição, sob pena de serem considerados "
     "inconstitucionais ou nulos. [Exercício Q01-II, Rodada 01 Out/2024]"),

    ("III – Atos de particular (ex. contratos) que descumpram preceito "
     "constitucional fundamental, em detrimento de direito subjetivo, estão "
     "sujeitos ao controle de constitucionalidade por meio de arguição de "
     "descumprimento de preceito fundamental. (C/E?)",
     "<b>ERRADO.</b> O objeto do controle de constitucionalidade são as leis e "
     "atos normativos emanados do <b>Poder Público</b>. Atos e contratos de "
     "particulares não se submetem ao controle de constitucionalidade — apenas a "
     "instrumentos jurídicos genéricos (ex. ação anulatória de contrato), que "
     "não integram o conjunto de ferramentas do controle de constitucionalidade. "
     "[Exercício Q01-III, Rodada 01 Out/2024]"),

    ("IV – Os atos jurídicos normativos devem estar em conformidade com os "
     "preceitos constitucionais. No que diz respeito aos atos jurídicos de "
     "efeito concreto, estão sujeitos à autoridade normativa da CF os atos "
     "praticados na esfera dos Poderes Legislativo, Executivo e Judiciário, mas "
     "não os praticados por particulares. (C/E?)",
     "<b>ERRADO.</b> Os atos praticados por particulares (ex. contratos, "
     "promessas de recompensa) TAMBÉM devem ser compatíveis com a Constituição — "
     "estão sujeitos à força normativa da CF/88. O que os diferencia é que, "
     "embora devam respeitar a Constituição, tais atos <b>não se submetem ao "
     "controle de constitucionalidade</b>, cujo objeto são apenas leis e atos "
     "normativos do Poder Público. [Exercício Q01-IV, Rodada 01 Out/2024]"),

    ("I – No ordenamento jurídico brasileiro, é possível a modulação dos "
     "efeitos de uma decisão do STF que declara a inconstitucionalidade de uma "
     "norma, estabelecendo que sua eficácia somente venha a ocorrer a partir do "
     "trânsito em julgado da decisão (efeitos \"ex nunc\" ou não retroativos), "
     "ou de outro momento que venha a ser fixado (efeitos \"pro futuro\" ou "
     "prospectivos), desde que a decisão tenha sido tomada pela maioria absoluta "
     "dos votos dos integrantes do tribunal. (C/E?)",
     "<b>ERRADO.</b> A modulação temporal de efeitos (art. 27, Lei nº "
     "9.868/1999) exige quórum específico de <b>2/3 dos ministros do STF</b> "
     "(8 dos 11 Ministros) — e não maioria absoluta — além de razões de "
     "segurança jurídica ou excepcional interesse social. "
     "[Exercício Q02-I, Rodada 01 Out/2024]"),

    ("II – O STF, de forma excepcional, tem admitido eficácia ex tunc às "
     "declarações de inconstitucionalidade para resguardar a segurança jurídica "
     "ou excepcional interesse social. (C/E?)",
     "<b>ERRADO.</b> A regra geral já é a eficácia <b>ex tunc</b> (retroativa) "
     "para as sentenças declaratórias do controle de constitucionalidade. "
     "Excepcionalmente, para resguardar segurança jurídica ou interesse social, "
     "é que o STF module os efeitos para \"ex nunc\" ou \"pro futuro\" — não o "
     "contrário. [Exercício Q02-II, Rodada 01 Out/2024]"),

    ("III – Caso seja julgada procedente a ADI, há possibilidade de modulação "
     "dos efeitos da decisão do STF, não sendo possível, contudo, a declaração "
     "de inconstitucionalidade com efeitos prospectivos (pro futuro). (C/E?)",
     "<b>ERRADO.</b> Com fundamento no art. 27 da Lei nº 9.868/1999, a "
     "modulação temporal de efeitos da sentença do controle de "
     "constitucionalidade admite dois efeitos excepcionais: \"ex nunc\" (não "
     "retroativo) OU \"pro futuro\" (prospectivo) — este último é plenamente "
     "possível. [Exercício Q02-III, Rodada 01 Out/2024]"),

    ("IV – Conforme entendimento do STF, a técnica de se conferir efeitos ex "
     "nunc às decisões proferidas em sede de controle concentrado (modulação "
     "temporal de efeitos da sentença do controle de constitucionalidade) "
     "também pode ser utilizada no âmbito do controle difuso. (C/E?)",
     "<b>CERTO.</b> Embora a literalidade do art. 27 da Lei nº 9.868/1999 "
     "restrinja a modulação ao STF (por 2/3 dos Ministros), o próprio STF "
     "interpretou o dispositivo no sentido de que os juízes de 1º grau, ao "
     "realizar o controle concreto/difuso, também podem modular temporalmente os "
     "efeitos de suas decisões. [Exercício Q02-IV, Rodada 01 Out/2024]"),

    ("I – A inobservância da competência constitucional de um ente federativo "
     "para a elaboração de determinada lei enseja a declaração da "
     "inconstitucionalidade material do ato normativo. (C/E?)",
     "<b>ERRADO.</b> A hipótese em que um ente federado legisla sobre tema para "
     "o qual não possui competência configura <b>inconstitucionalidade formal "
     "orgânica</b> — e não material —, pois o vício está na falta de competência "
     "do órgão legislativo que atuou, não no conteúdo da norma. "
     "[Exercício Q03-I, Rodada 01 Out/2024]"),

    ("II – A inconstitucionalidade formal se verifica quando a lei ou ato "
     "normativo apresenta algum vício em seu processo de formação. O "
     "desrespeito a um quórum de aprovação previsto no texto constitucional "
     "constitui exemplo de vício formal objetivo. (C/E?)",
     "<b>CERTO.</b> A inconstitucionalidade formal (nomodinâmica) ocorre quando "
     "não se observam as regras do processo legislativo previstas na CF/88. O "
     "desrespeito a quórum de aprovação é exemplo de <b>inconstitucionalidade "
     "formal objetiva</b>, uma das 3 subespécies (ao lado de vício de iniciativa "
     "e orgânica). [Exercício Q03-II, Rodada 01 Out/2024]"),

    ("III – A sanção presidencial a projeto de lei não supre vícios de "
     "iniciativa, padecendo de vício formal a lei sancionada, a ser declarado "
     "por meio de ação judicial própria. (C/E?)",
     "<b>CERTO.</b> O STF tem entendimento sedimentado de que, nos casos de "
     "inconstitucionalidade formal por vício de iniciativa, a eventual sanção "
     "(concordância) do Presidente da República <b>não convalida, não supre, "
     "não corrige</b> o vício formal de iniciativa. "
     "[Exercício Q03-III, Rodada 01 Out/2024]"),

    ("IV – Por serem consideradas normas derivadas, as emendas constitucionais "
     "são passíveis de controle de constitucionalidade apenas no caso de serem "
     "tendentes a abolir cláusulas pétreas. (C/E?)",
     "<b>ERRADO.</b> A emenda constitucional, por ser norma constitucional "
     "<b>derivada</b>, submete-se ao controle de constitucionalidade de modo "
     "geral — tanto por inconstitucionalidade <b>material</b> (ex. tender a "
     "abolir cláusula pétrea) quanto <b>formal</b> (ex. votada em turno único, "
     "quando a CF exige 2 turnos). Não se restringe à hipótese de cláusulas "
     "pétreas. [Exercício Q03-IV, Rodada 01 Out/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Controle de Constitucionalidade",
        "Direito Interno - Controle de Constitucionalidade.apkg",
        CONTROLE_DE_CONSTITUCIONALIDADE,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
