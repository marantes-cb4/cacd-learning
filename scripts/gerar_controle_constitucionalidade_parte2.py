#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 02 (Out/2024).

Tema: Primado da Constituição. Controle de Constitucionalidade — momento
de realização: preventivo x repressivo (Item 3 do Edital CACD).
Continuação de gerar_controle_constitucionalidade.py (Parte 1).

Fontes:
  - Anotações: Controle de Constitucionalidade - Parte 2.md
  - Material do professor: Direito Interno_Rodada 02_Outubro_2024_Anotada e Atualizada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 02_Outubro_2024.pdf
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


CONTROLE_CONSTITUCIONALIDADE_PARTE2 = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("No sistema concreto ou difuso de controle de constitucionalidade, a "
     "declaração de inconstitucionalidade proferida pelo Poder Judiciário "
     "retira a lei ou ato normativo do ordenamento jurídico com efeitos "
     "erga omnes, distinguindo-se do sistema abstrato ou concentrado "
     "apenas quanto ao órgão julgador competente.",
     "<b>ERRADO.</b> É o oposto: no controle <b>difuso</b>, a decisão tem "
     "efeitos <b>inter partes</b> e NÃO retira a lei do ordenamento — só "
     "impede sua aplicação ao caso julgado. É o controle <b>abstrato ou "
     "concentrado</b> que produz efeitos <b>erga omnes e vinculantes</b>, "
     "retirando a lei do ordenamento jurídico. [Anotações da aula; Rodada "
     "02/Out.2024, p.6-7]"),

    ("Dentre os instrumentos de controle repressivo de constitucionalidade "
     "exercidos pelo Poder Legislativo, a rejeição de conversão de medida "
     "provisória inconstitucional em lei configura hipótese de revogação "
     "de ato normativo pelo Congresso Nacional.",
     "<b>ERRADO.</b> Nenhum dos instrumentos do Legislativo no controle "
     "repressivo é revogação. Lei ou ato normativo <b>inconstitucional é "
     "NULO</b> (efeito ex-tunc) — nunca ingressou validamente no "
     "ordenamento — e só normas <b>válidas e existentes</b> podem ser "
     "revogadas por norma posterior. [Anotações da aula; Rodada "
     "02/Out.2024, p.5]"),

    ("De acordo com o entendimento atual do STF, formado a partir de "
     "agosto de 2025, o chefe do Poder Executivo, ao identificar lei ou "
     "ato normativo flagrantemente inconstitucional, pode determinar, por "
     "autotutela, que os órgãos subalternos da Administração Pública "
     "deixem de cumpri-lo, sem necessidade de provocar o Poder Judiciário.",
     "<b>ERRADO.</b> Esse era o entendimento <b>anterior</b>, hoje "
     "superado. Pelo novo entendimento do STF, o Executivo NÃO pode mais "
     "exercer autotutela para sustar lei inconstitucional por conta "
     "própria — deve <b>ajuizar ação judicial</b> e pedir ao Judiciário "
     "decisão liminar ou cautelar de suspensão, em respeito ao princípio "
     "da separação dos poderes. [Anotações da aula; Rodada 02/Out.2024, "
     "p.4]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Out/2024) ──────────────

    ("01-I – O fato de uma proposta de emenda constitucional ser aprovada "
     "e, após seu encaminhamento para sanção do presidente da República, "
     "sofrer veto presidencial com fundamento na inconstitucionalidade do "
     "ato objeto de deliberação comprova a existência, no ordenamento "
     "legislativo brasileiro, de controle preventivo de "
     "constitucionalidade, ao lado do consagrado sistema jurisdicional, "
     "normalmente de caráter repressivo. (C/E?)",
     "<b>ERRADO.</b> Sanção e veto presidenciais (art. 66, CF/88) alcançam "
     "apenas <b>projetos de lei</b> — PEC nunca se submete a sanção/veto do "
     "Presidente. [Exercício Q01-I, Rodada 02 Out/2024]"),

    ("01-II – O controle de constitucionalidade no Brasil parte da "
     "premissa de que compete exclusivamente ao Poder Judiciário a guarda "
     "da Constituição. (C/E?)",
     "<b>ERRADO.</b> Os 3 Poderes atuam no controle preventivo, e "
     "Legislativo e Judiciário atuam no controle repressivo — a guarda da "
     "Constituição não é exclusiva do Judiciário. [Exercício Q01-II, "
     "Rodada 02 Out/2024]"),

    ("01-III – O exercício pelo Poder Legislativo do controle preventivo "
     "de constitucionalidade ocorre exclusivamente pelas comissões de "
     "constituição e justiça. (C/E?)",
     "<b>ERRADO.</b> Há 2 instrumentos: além da CCJ, há também a "
     "<b>votação em Plenário</b>, que pode rejeitar inconstitucionalidades "
     "não apontadas pela CCJ. [Exercício Q01-III, Rodada 02 Out/2024]"),

    ("01-IV – O controle prévio ou preventivo de constitucionalidade "
     "realizado pelo Poder Legislativo incide sobre todos os projetos de "
     "atos normativos. (C/E?)",
     "<b>ERRADO.</b> Só incide sobre <b>projeto de lei e PEC</b>. Medidas "
     "provisórias, leis delegadas, decretos legislativos e resoluções não "
     "têm \"projeto\" e por isso não se submetem ao controle preventivo. "
     "[Exercício Q01-IV, Rodada 02 Out/2024]"),

    ("02-I – Somente parlamentar tem legitimidade para impetrar mandado de "
     "segurança contra atos ditos incompatíveis com disposições "
     "constitucionais sobre processo legislativo e praticados durante o "
     "trâmite de proposta de emenda constitucional (PEC). (C/E?)",
     "<b>CERTO.</b> O controle preventivo jurisdicional só se dá por "
     "mandado de segurança impetrado exclusivamente por <b>parlamentar</b>. "
     "[Exercício Q02-I, Rodada 02 Out/2024]"),

    ("02-II – O controle preventivo de constitucionalidade busca impedir a "
     "produção de normas jurídicas contrárias à Constituição, a fim de "
     "evitar que produzam efeitos. (C/E?)",
     "<b>CERTO.</b> É exatamente a finalidade do controle preventivo: "
     "abortar o processo legislativo antes da promulgação da norma "
     "inconstitucional. [Exercício Q02-II, Rodada 02 Out/2024]"),

    ("02-III – O controle de constitucionalidade preventivo é realizado "
     "durante a etapa de formação do ato normativo, com o objetivo de "
     "resguardar o processo legislativo hígido. Caso haja proposta de "
     "emenda constitucional tendente a abolir cláusula pétrea, qualquer "
     "legitimado à propositura de ação direta de inconstitucionalidade "
     "poderá ajuizar, ainda durante o processo legislativo, perante o STF "
     "a referida ação judicial para impedir o trâmite dessa emenda. (C/E?)",
     "<b>ERRADO.</b> O controle preventivo jurisdicional só se dá por "
     "<b>mandado de segurança impetrado por parlamentar</b> — a ADI é "
     "instrumento do controle <b>repressivo</b> abstrato/concentrado, não "
     "cabível durante o processo legislativo. [Exercício Q02-III, Rodada "
     "02 Out/2024]"),

    ("02-IV – Projetos de lei não podem sofrer controle de "
     "constitucionalidade preventivo jurisdicional em razão de seu "
     "conteúdo. (C/E?)",
     "<b>CERTO.</b> O MS contra projeto de lei só pode questionar "
     "<b>vício formal</b>, nunca o conteúdo (vício material) — este fica a "
     "cargo do veto presidencial. [Exercício Q02-IV, Rodada 02 Out/2024]"),

    ("03-I – No Brasil, o denominado controle repressivo de "
     "constitucionalidade, também denominado sucessivo ou a posteriori, "
     "foi conferido com exclusividade ao Poder Judiciário. (C/E?)",
     "<b>ERRADO.</b> O controle repressivo é exercido por <b>Legislativo e "
     "Judiciário</b> — não é exclusivo do Judiciário (e, desde a mudança "
     "jurisprudencial do STF em 2025, o Executivo está excluído dessa "
     "atuação, restando apenas os 2 Poderes citados). [Exercício Q03-I, "
     "Rodada 02 Out/2024]"),

    ("03-II – O Tribunal de Contas pode exercer administrativamente o "
     "controle repressivo de constitucionalidade, ocorrendo a "
     "transcendência dos efeitos com o afastamento da aplicação da lei "
     "para toda a administração pública. (C/E?)",
     "<b>ERRADO.</b> Pela Súmula 347/STF, o TC só declara "
     "inconstitucionalidade no caso concreto que analisa (controle "
     "difuso) — NÃO pode dar efeitos erga omnes/vinculantes, nem afastar a "
     "lei para toda a Administração. [Exercício Q03-II, Rodada 02 "
     "Out/2024]"),

    ("03-III – O controle repressivo político inclui a competência do "
     "Congresso Nacional para sustar atos normativos do Poder Executivo "
     "que exorbitem do poder regulamentar ou dos limites de delegação "
     "legislativa. (C/E?)",
     "<b>CERTO.</b> Art. 49, V, CF/88 — competência exclusiva do CN, "
     "considerada controle <b>político</b> por bastar o quórum, sem "
     "necessidade de fundamentar a inconstitucionalidade. [Exercício "
     "Q03-III, Rodada 02 Out/2024]"),

    ("03-IV – A medida provisória rejeitada pelo Congresso Nacional por "
     "inconstitucionalidade configura hipótese de controle repressivo de "
     "constitucionalidade exercido pelo Poder Legislativo. (C/E?)",
     "<b>CERTO.</b> A MP já vigora com força de lei desde a publicação; "
     "sua rejeição por inconstitucionalidade impede a conversão em lei e "
     "retira a MP do ordenamento — configura controle repressivo. "
     "[Exercício Q03-IV, Rodada 02 Out/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Controle de Constitucionalidade - Parte 2",
        "Direito Interno - Controle de Constitucionalidade - Parte 2.apkg",
        CONTROLE_CONSTITUCIONALIDADE_PARTE2,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
