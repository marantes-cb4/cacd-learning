#!/usr/bin/env python3
"""Gera deck Anki: Economia - Custos da Tributação, Comércio Internacional, Externalidades e Bens Públicos"""

import genanki
import os
import random

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "anki", "decks", "economia")

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
    # ── TRIBUTAÇÃO ────────────────────────────────────────────────────────────
    (
        "Qual a relação entre elasticidade e peso morto causado por tributos?",
        "• <b>Maior elasticidade → maior peso morto</b>: oferta/demanda reage mais à variação "
        "de preço, então o imposto distorce mais o mercado.<br>"
        "• <b>Curva mais inelástica → absorve mais tributação</b>: quantidade transacionada "
        "cai pouco, o peso morto é menor.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que é a Curva de Laffer e o que ela demonstra?",
        "Curva em <b>U invertido</b> que relaciona:<br>"
        "• Eixo X: montante do imposto (alíquota)<br>"
        "• Eixo Y: receita tributária arrecadada<br>"
        "Demonstra que existe um <b>ponto ótimo</b> de receita máxima: acima dele, aumentar "
        "o imposto faz a quantidade transacionada cair tanto que a receita total diminui.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Por que cobrar impostos muito altos pode reduzir a receita do governo?",
        "Com alíquotas excessivas, a <b>quantidade transacionada cai tanto</b> que o acréscimo "
        "de preço por unidade não compensa a queda no volume — a receita total (preço × "
        "quantidade) diminui. Esse fenômeno é ilustrado pela <b>Curva de Laffer</b>: após o "
        "ponto de receita máxima, mais imposto gera menos arrecadação.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),

    # ── COMÉRCIO INTERNACIONAL — EXPORTAÇÃO ───────────────────────────────────
    (
        "Quais os efeitos no mercado interno quando um bem passa a ser exportado?",
        "O preço doméstico <b>sobe</b> ao nível do preço internacional:<br>"
        "• Demanda interna <b>cai</b><br>"
        "• Quantidade produzida <b>aumenta</b><br>"
        "• A diferença (qt produzida − qt demandada internamente) = <b>exportações</b><br>"
        "• Excedente do produtor cresce; excedente total de mercado é <b>maior</b> com o "
        "comércio — argumento de que exportações beneficiam o país.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Quais os efeitos no mercado interno quando um bem passa a ser importado?",
        "O preço doméstico <b>cai</b> ao nível do preço internacional (análogo a um preço "
        "máximo abaixo do equilíbrio):<br>"
        "• Demanda interna <b>aumenta</b><br>"
        "• Produção nacional <b>cai</b><br>"
        "• A diferença (qt demandada − qt produzida internamente) = <b>importações</b><br>"
        "• Excedente do consumidor cresce; excedente total de mercado é maior.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Qual o efeito econômico das tarifas de importação?",
        "A tarifa eleva o preço do bem importado:<br>"
        "• Excedente do <b>produtor</b> aumenta (preço geral sobe)<br>"
        "• Excedente do <b>consumidor</b> diminui<br>"
        "• Governo <b>arrecada receita</b> (retângulo entre as quantidades antes e após a "
        "tarifa, transferido do excedente do consumidor)<br>"
        "• Gera <b>peso morto</b>: redução do excedente total do mercado.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Qual a diferença entre tarifas e cotas de importação quanto a seus efeitos econômicos?",
        "Efeitos sobre excedente do produtor/consumidor e peso morto são <b>idênticos</b>.<br>"
        "Diferença-chave: <b>quem fica com o retângulo de receita</b>:<br>"
        "• <b>Tarifa</b>: receita vai para o <b>governo</b>.<br>"
        "• <b>Cota</b>: receita vai para as <b>empresas detentoras de licença</b> de importação.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Quais os 5 argumentos a favor de restrições ao comércio internacional?",
        "1. <b>Aumento de empregos internos</b>: protege produção nacional de competidores estrangeiros.<br>"
        "2. <b>Segurança nacional</b>: dependência de bens-chave estrangeiros é perigosa (ex.: chips).<br>"
        "3. <b>Indústria nascente</b>: protege setores ainda incapazes de competir externamente "
        "(pensamento cepalino).<br>"
        "4. <b>Competição desleal</b>: países que não seguem padrões trabalhistas produzem mais barato.<br>"
        "5. <b>Instrumento de barganha</b>: protecionismo como alavanca de negociação política.<br>"
        "Todos têm <b>natureza política</b>.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),

    # ── EXTERNALIDADES ────────────────────────────────────────────────────────
    (
        "O que é uma externalidade?",
        "Impacto das ações de uma pessoa sobre o <b>bem-estar de terceiros</b> que não "
        "participam da transação. Pode ser <b>positiva</b> (benefício) ou <b>negativa</b> "
        "(custo). Causa falha de mercado porque o preço de mercado não reflete o custo/benefício "
        "social total.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Como a externalidade negativa afeta o equilíbrio de mercado e qual a solução?",
        "<b>Custo social excede o custo privado</b> → a quantidade de equilíbrio de mercado "
        "é <b>maior</b> que a quantidade socialmente ótima (produz-se demais).<br>"
        "Solução: <b>internalização da externalidade</b> — o governo (planejador) impõe "
        "normas, impostos ou regulações para deslocar a curva e atingir o ponto ótimo.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Como a externalidade positiva afeta o equilíbrio de mercado e qual a solução?",
        "<b>Valor social excede o valor privado</b> → a quantidade de equilíbrio de mercado "
        "é <b>menor</b> que a quantidade socialmente ótima (produz-se de menos).<br>"
        "Solução: o governo <b>subsidia</b> a atividade para estimular maior produção/consumo "
        "até o ponto ótimo (ex.: subsídios à educação).<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que afirma o Teorema de Coase?",
        "Se os agentes privados puderem <b>negociar sem custo</b> a alocação de recursos, "
        "resolverão por si só o problema de externalidade — independentemente de quem detém "
        "o direito de propriedade sobre o recurso em questão.<br>"
        "Condição necessária: direitos de propriedade <b>bem definidos</b>.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "Quais as principais políticas públicas para corrigir externalidades?",
        "1. <b>Regulamentação</b>: normas que proíbem ou limitam a atividade causadora.<br>"
        "2. <b>Impostos de Pigou</b>: taxam externalidades negativas — definem o <b>preço</b> "
        "da poluição (ex.: imposto por tonelada de CO₂).<br>"
        "3. <b>Subsídios de Pigou</b>: estimulam externalidades positivas.<br>"
        "4. <b>Licenças de poluição (cotas)</b>: definem a <b>quantidade</b> máxima de poluição "
        "permitida. Tanto impostos quanto cotas levam ao mesmo ponto de equilíbrio de preço e "
        "quantidade.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),

    # ── BENS PÚBLICOS E RECURSOS COMUNS ───────────────────────────────────────
    (
        "Como os bens são classificados segundo exclusão e rivalidade?",
        "<table style='border-collapse:collapse'>"
        "<tr><td></td><td><b>Excludente</b></td><td><b>Não excludente</b></td></tr>"
        "<tr><td><b>Rival</b></td><td>Bem privado</td><td>Recurso comum</td></tr>"
        "<tr><td><b>Não rival</b></td><td>Bem de clube</td><td>Bem público</td></tr>"
        "</table><br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que são bens públicos e quais os exemplos relevantes para o CACD?",
        "Bens <b>não excludentes e não rivais</b>: não se pode impedir o uso por ninguém e "
        "o uso por um não reduz a disponibilidade para outros.<br>"
        "Exemplos:<br>"
        "• Defesa nacional<br>"
        "• Pesquisa de base (ex.: vacinas COVID-19)<br>"
        "• Programas de combate à pobreza<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que são recursos comuns e por que geram problema econômico?",
        "Bens <b>rivais mas não excludentes</b>: ninguém pode ser impedido de usá-los, "
        "mas o uso por um reduz a disponibilidade para outros (recurso finito).<br>"
        "Ex.: praia, pesqueiros, pastagens. O problema é o <b>uso excessivo</b>: como ninguém "
        "é dono nem paga pelo uso, os agentes ignoram o custo imposto aos demais — "
        "gerando externalidade negativa (Tragédia dos Comuns).<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que é o problema do free rider (carona) em bens públicos?",
        "Indivíduos usufruem de um bem público <b>sem contribuir</b> para seu financiamento, "
        "pois o bem é não excludente. Como resultado, o mercado privado fornece uma quantidade "
        "<b>inferior</b> à socialmente ótima — justificando a provisão pelo governo.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que é a Tragédia dos Comuns?",
        "Fenômeno em que recursos comuns são <b>utilizados em excesso</b> em relação ao "
        "ótimo social. Como ninguém possui nem gerencia o recurso, os agentes não "
        "internalizam o custo que seu uso impõe aos demais — gerando uma "
        "<b>externalidade negativa</b> que degrada o recurso para todos.<br>"
        "<i>Fonte: Anotações – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Economia::Custos da Tributação, Comércio Internacional, Externalidades e Bens Públicos",
        "Economia - Custos da Tributacao, Comercio Internacional, Externalidades e Bens Publicos.apkg",
        CARDS,
    )
