#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Reconhecimento de Estado e Governo"""

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


RECONHECIMENTO = [
    # ── SUJEITOS DE DIREITO INTERNACIONAL ─────────────────────────────────────
    (
        "Qual a diferença entre sujeitos primários e secundários do Direito Internacional?",
        "<b>Primários/originários — Estados soberanos</b>:<br>"
        "• Personalidade jurídica independe de reconhecimento por outros Estados<br>"
        "• Capacidade internacional plena (celebrar tratados, atribuir nacionalidade, ingressar em OIs etc.)<br>"
        "<b>Secundários/derivados</b> (OIs, Santa Sé, Soberana Ordem de Malta, CICV, movimentos de "
        "libertação, beligerantes, indivíduo):<br>"
        "• Precisam de reconhecimento por Estados para adquirir personalidade jurídica<br>"
        "• Capacidade internacional limitada<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Quais entidades NÃO possuem personalidade jurídica internacional?",
        "Empresas multinacionais, ONGs, FIFA, FIA e COI são <b>atores internacionais</b>, "
        "não sujeitos de DI — não possuem personalidade jurídica internacional.<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Quais são os 4 elementos constitutivos dos Estados soberanos segundo a Convenção de "
        "Montevidéu (1933)?",
        "1. <b>População permanente</b><br>"
        "2. <b>Território determinado</b><br>"
        "3. <b>Governo</b><br>"
        "4. <b>Capacidade para manter relações internacionais</b><br>"
        "A soberania <b>não</b> é elemento constitutivo — é atributo que decorre da verificação "
        "dos 4 elementos. O reconhecimento por outros Estados também não é requisito constitutivo.<br>"
        "<i>Fonte: Art. 1 Convenção de Montevidéu 1933 / Anotações</i>",
    ),
    (
        "O que defende a teoria declaratória e a teoria constitutiva do reconhecimento de Estado?",
        "<b>Declaratória</b> (adotada desde Montevidéu 1933, e pela Carta da OEA 1948):<br>"
        "O Estado existe pelos 4 elementos constitutivos, independentemente do reconhecimento. "
        "O reconhecimento é ato político-declaratório, não condição para existência.<br>"
        "<b>Constitutiva</b> (histórica — Europa séc. XIX, não aplicada atualmente):<br>"
        "O reconhecimento pelos Estados já existentes é condição para a personalidade jurídica. "
        "Usada pelas metrópoles europeias para manter poder sobre colônias.<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Quais são as características do ato de reconhecimento de Estado?",
        "• <b>Discricionário</b>: não há obrigatoriedade — é ato unilateral e opcional<br>"
        "• <b>Irrevogável</b>: não pode ser retirado após concedido (mas pode caducar se o Estado "
        "perder um dos 4 elementos constitutivos)<br>"
        "• <b>Expresso ou tácito</b>: pode ser explícito (declaração formal) ou implícito "
        "(manutenção de relações diplomáticas)<br>"
        "• <b>Retroativo (ex tunc)</b>: certifica que os 4 elementos já existiam desde a origem<br>"
        "• <b>Incondicional</b>: não se pode impor condições (violaria igualdade soberana)<br>"
        "• <b>Vedado</b> quando o Estado foi criado por emprego da força<br>"
        "• Adesão a uma OI <b>não</b> equivale a reconhecimento pelos membros da OI<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Por que o Brasil não adota a prática de reconhecimento de governo? Quais os fundamentos?",
        "1. <b>Princípio da não-intervenção</b>: o Brasil não emite julgamento sobre questões "
        "internas de outros países, como mudanças de governo.<br>"
        "2. <b>Princípio da continuidade do Estado</b>: o DI vincula Estados, não governos — "
        "mudanças de governo não afetam direitos e obrigações internacionais do Estado soberano.<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Quais são as 5 doutrinas de reconhecimento de governo?",
        "1. <b>Jefferson</b> (EUA, séc. XVIII): reconhecer apenas governos com apoio popular<br>"
        "2. <b>Tobar</b> (Equador, 1907): reconhecer apenas se seguirem postulados democráticos<br>"
        "3. <b>Wilson</b> (EUA, 1913): releitura da Tobar — não reconhecer governos criados por "
        "golpe com uso da força<br>"
        "4. <b>Estrada</b> (México, 1930): reconhecimento tácito via manutenção de relações "
        "diplomáticas (ruptura diplomática = não reconhecimento tácito)<br>"
        "5. <b>Betancourt</b> (Venezuela, 1959): não reconhecer governos advindos de movimentos "
        "revolucionários que rompam a ordem constitucional<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),
    (
        "Qual o papel da autodeterminação dos povos nos elementos constitutivos do Estado?",
        "A autodeterminação dos povos <b>não é elemento constitutivo</b> do Estado segundo a "
        "Convenção de Montevidéu. Contudo, como <b>jus cogens</b> (norma imperativa) pós-1945, "
        "é fator adicional para aferir a legitimidade do <i>governo</i>: se o governo não "
        "respeita a autodeterminação internamente, pode-se questionar se ele é efetivo e "
        "legítimo representante da população.<br>"
        "<i>Fonte: Anotações – Reconhecimento de Estado e Governo</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Para o Direito das Gentes, o ingresso nas Nações Unidas é requisito "
        "prescindível para que um Estado possa ser considerado sujeito de direito internacional.",
        "<b>CERTO.</b> Os 4 elementos constitutivos (Convenção de Montevidéu) não incluem a "
        "adesão à ONU. O Estado adquire personalidade jurídica internacional pelos 4 elementos, "
        "independentemente de reconhecimento ou de pertencer a qualquer OI.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q01-I</i>",
    ),
    (
        "[Exercício] II – A personalidade jurídica internacional de um Estado é constituída antes "
        "do seu reconhecimento pelos demais Estados da sociedade internacional, por isso o ato de "
        "reconhecimento de um Estado produz efeitos 'ex nunc' ou não retroativos.",
        "<b>ERRADO.</b> A primeira parte é correta (teoria declaratória). Mas justamente porque "
        "o Estado já existia antes do reconhecimento, o ato produz efeitos <b>ex tunc</b> "
        "(retroativos) — certifica que os 4 elementos existiam desde a origem, não apenas "
        "desde o reconhecimento.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q01-II</i>",
    ),
    (
        "[Exercício] III – O Estado X tornou-se independente em 2000. Em 2003, o Estado Y "
        "declarou o reconhecimento do Estado X. Nessa situação, somente a partir do referido "
        "reconhecimento os atos emanados pelo Estado X serão aceitos como válidos pelos "
        "tribunais do Estado Y.",
        "<b>ERRADO.</b> O reconhecimento tem efeitos <b>ex tunc</b> (retroativos). Os atos do "
        "Estado X desde 2000 são válidos perante o Estado Y — o reconhecimento em 2003 certifica "
        "a existência do Estado X desde sua independência.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q01-III</i>",
    ),
    (
        "[Exercício] IV – A irrevogabilidade do reconhecimento de Estado determina que, uma vez "
        "reconhecida a personalidade internacional de um Estado soberano, esse reconhecimento não "
        "poderá ser retirado, a menos que se verifique a ocorrência de caducidade.",
        "<b>CERTO.</b> O reconhecimento é irrevogável. A caducidade ocorre quando o Estado perde "
        "um dos 4 elementos constitutivos e deixa de existir — não é retirada do reconhecimento, "
        "mas extinção do próprio Estado reconhecido.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Caso não ocorra o reconhecimento formal de um novo Estado, o simples "
        "estabelecimento de relações diplomáticas com o país recém-criado produz o mesmo efeito "
        "jurídico do reconhecimento.",
        "<b>CERTO.</b> O reconhecimento de Estado pode ser <b>tácito</b>: manter relações "
        "diplomáticas com um Estado implica reconhecê-lo, pois relações diplomáticas só ocorrem "
        "entre Estados soberanos.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q02-I</i>",
    ),
    (
        "[Exercício] II – Um Estado é recém-independente. Dois outros Estados podem, segundo o "
        "Direito Internacional, exprimir o reconhecimento conjunto do Estado recém-independente, "
        "desde que celebrem um tratado internacional para tanto.",
        "<b>ERRADO.</b> O reconhecimento de Estado é um ato <b>unilateral</b> de cada Estado "
        "soberano — não pode ser realizado via tratado. Além disso, o reconhecimento é "
        "incondicional: vincular o reconhecimento a condições violaria a igualdade soberana.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q02-II</i>",
    ),
    (
        "[Exercício] III – Antes de reconhecer um novo Estado, a República Federativa do Brasil "
        "deve considerar, em sua avaliação das circunstâncias, se a nova entidade possui território "
        "definido, população permanente, governo efetivo, bem como se existe promessa de "
        "estabelecer relações diplomáticas com o Brasil.",
        "<b>ERRADO.</b> O reconhecimento é <b>incondicional</b> — não se pode impor condições "
        "como 'promessa de relações diplomáticas'. Os 4 elementos da Convenção de Montevidéu são: "
        "população, território, governo e capacidade para relações internacionais (não "
        "'promessa de relações com o Brasil').<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q02-III</i>",
    ),
    (
        "[Exercício] IV – A Convenção de Montevidéu sobre Direitos e Deveres dos Estados de 1933 "
        "não acata a autodeterminação dos povos como critério para o surgimento da personalidade "
        "estatal.",
        "<b>CERTO.</b> A Convenção de Montevidéu prevê apenas 4 elementos constitutivos "
        "(população, território, governo, capacidade para relações internacionais). A "
        "autodeterminação dos povos não figura entre eles — tornou-se relevante como jus cogens "
        "somente após 1945.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – O Estado brasileiro tem a prática de, além de reconhecer Estados, "
        "proceder igualmente ao reconhecimento formal de novos governos, exceto quando oriundos "
        "de revolução ou golpe de Estado, o que exprime um juízo de valor acerca da legitimidade "
        "do novo regime.",
        "<b>ERRADO.</b> O Brasil <b>não adota</b> a prática de reconhecimento de governos "
        "— independentemente de como tenham chegado ao poder. Os fundamentos são o princípio "
        "da não-intervenção e o princípio da continuidade do Estado.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q03-I</i>",
    ),
    (
        "[Exercício] II – A doutrina Tobar, com referência a Carlos Tobar, ministro das relações "
        "exteriores do Equador, surgiu em 1907 e pautava-se no princípio da não intervenção.",
        "<b>ERRADO.</b> A doutrina Tobar (1907) condiciona o reconhecimento ao respeito aos "
        "postulados democráticos — o que representa justamente uma <b>intervenção</b> nos assuntos "
        "internos de outros Estados. É o oposto do princípio da não-intervenção, razão pela qual "
        "o Brasil não a adota.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q03-II</i>",
    ),
    (
        "[Exercício] III – O reconhecimento de governo, nos moldes defendido por Genaro Estrada, "
        "chanceler mexicano em 1930, está indissociavelmente vinculado ao exercício das relações "
        "diplomáticas e das relações consulares.",
        "<b>ERRADO.</b> A Doutrina Estrada vincula o reconhecimento tácito à manutenção de "
        "<b>relações diplomáticas</b> — não das relações consulares. As relações consulares têm "
        "natureza distinta (comercial, proteção de nacionais) e podem ser mantidas de forma "
        "independente.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q03-III</i>",
    ),
    (
        "[Exercício] IV – O reconhecimento de governo deve ser tratado diferentemente do "
        "reconhecimento de Estado, considerando-se que os efeitos jurídicos são diversos no "
        "direito internacional.",
        "<b>CERTO.</b> São institutos distintos: o reconhecimento de <b>Estado</b> cria/certifica "
        "personalidade jurídica internacional (efeitos ex tunc, irrevogável); o reconhecimento de "
        "<b>governo</b> versa sobre a legitimidade do poder executivo e não cria nova "
        "personalidade jurídica — os efeitos e a prática variam entre os Estados.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mai/2024, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Internacional::Reconhecimento de Estado e Governo",
        "Direito Internacional - Reconhecimento de Estado e Governo.apkg",
        RECONHECIMENTO,
    )
