#!/usr/bin/env python3
"""Gera deck Anki: Economia - Micro - Teoria da Firma"""

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
    # ── CONCEITO GERAL ────────────────────────────────────────────────────────
    (
        "Qual o objetivo central da firma na Teoria da Firma e como se calcula seu lucro?",
        "Firmas são <b>maximizadoras de lucro</b>.<br>"
        "<b>Lucro = Receita Total (RT) − Custo Total (CT)</b><br>"
        "RT = Preço × Quantidade; CT = valor de mercado de todos os insumos.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── CUSTOS ────────────────────────────────────────────────────────────────
    (
        "O que são custos explícitos e custos implícitos?",
        "<b>Custos explícitos</b>: exigem desembolso de dinheiro (ex.: salários, aluguel).<br>"
        "<b>Custos implícitos</b>: não exigem desembolso, mas representam custo de oportunidade "
        "(ex.: tempo do proprietário, capital próprio que poderia render juros).<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Qual a diferença entre lucro econômico e lucro contábil? Qual é sempre maior?",
        "<b>Lucro contábil</b>: RT − custos explícitos → considera apenas desembolsos reais.<br>"
        "<b>Lucro econômico</b>: RT − (custos explícitos + implícitos) → inclui custo de oportunidade.<br>"
        "O <b>lucro contábil é sempre maior</b> que o lucro econômico.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── FUNÇÃO DE PRODUÇÃO ────────────────────────────────────────────────────
    (
        "O que é a função de produção e qual é o formato da sua curva?",
        "Relação entre a <b>quantidade de insumos</b> usada e a <b>quantidade de bens produzidos</b>.<br>"
        "Curva <b>crescente com inclinação decrescente</b>: à medida que se adicionam trabalhadores, "
        "a produção aumenta cada vez menos (produto marginal decrescente).<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "O que é produto marginal do trabalho e por que ele é decrescente?",
        "<b>Produto marginal do trabalho</b>: aumento da produção com cada trabalhador adicional.<br>"
        "É <b>decrescente</b> porque cada trabalhador novo tem menos capacidade produtiva que o anterior "
        "— limitações físicas da fábrica e das máquinas. Em algum ponto, mais um trabalhador não "
        "adiciona produtividade.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "O que mede a inclinação da função de produção?",
        "A inclinação da função de produção mede o <b>produto marginal do trabalho</b> "
        "(para cada trabalhador adicionado). À medida que o número de trabalhadores cresce, "
        "a curva fica menos inclinada, refletindo o produto marginal decrescente.<br>"
        "<i>Fonte: PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── CURVA DE CUSTO TOTAL ──────────────────────────────────────────────────
    (
        "Qual o formato da curva de custo total e o que determina esse formato?",
        "Curva <b>crescente com inclinação crescente</b>: produzir mais unidades custa proporcionalmente "
        "mais quando a produção já está elevada.<br>"
        "Isso decorre diretamente do <b>produto marginal decrescente</b> do trabalho.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── TIPOS DE CUSTO (CP) ───────────────────────────────────────────────────
    (
        "Defina: custo fixo, custo variável, custo total médio, custo fixo médio, custo variável médio e custo marginal.",
        "<b>CF</b>: não varia com Qt (ex.: aluguel).<br>"
        "<b>CV</b>: varia com Qt (ex.: trabalhadores).<br>"
        "<b>CTMe</b> = CT / Qt → curva em U.<br>"
        "<b>CFMe</b> = CF / Qt → sempre decrescente.<br>"
        "<b>CVMe</b> = CV / Qt → crescente.<br>"
        "<b>CMg</b> = ΔCT / ΔQt → curva em U, mais acentuada.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Por que o custo fixo médio (CFMe) é sempre decrescente?",
        "O custo fixo não muda com a quantidade produzida. Ao dividir o mesmo valor fixo por uma "
        "quantidade crescente de unidades, o custo por unidade <b>diminui continuamente</b>.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Por que o custo variável médio (CVMe) é crescente?",
        "À medida que a produção aumenta, o produto marginal do trabalho <b>diminui</b>. "
        "É preciso adicionar mais insumos (trabalhadores) para cada unidade extra, elevando "
        "o custo variável por unidade produzida.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── CTMe EM U ─────────────────────────────────────────────────────────────
    (
        "Por que a curva de Custo Total Médio (CTMe) tem formato de U?",
        "CTMe = CFMe + CVMe.<br>"
        "No início: o <b>CFMe</b> cai rapidamente (domina) → CTMe cai.<br>"
        "Depois: o <b>CVMe</b> sobe (domina) → CTMe sobe.<br>"
        "A combinação gera o formato de U, com mínimo na <b>escala eficiente</b>.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "O que é a escala eficiente de uma empresa?",
        "A quantidade que <b>minimiza o custo total médio</b> (CTMe), correspondente ao ponto mais "
        "baixo da curva em U do CTMe. Nesse ponto, o custo por unidade é o menor possível.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Qual a relação entre custo marginal (CMg) e custo total médio (CTMe)? Onde as curvas se cruzam?",
        "• CMg &lt; CTMe → CTMe está <b>caindo</b><br>"
        "• CMg &gt; CTMe → CTMe está <b>subindo</b><br>"
        "• CMg = CTMe → CTMe está no <b>mínimo</b><br>"
        "As duas curvas se cruzam exatamente no <b>ponto mínimo do CTMe</b> (escala eficiente).<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),

    # ── LONGO PRAZO ───────────────────────────────────────────────────────────
    (
        "Qual a diferença entre curto prazo e longo prazo na análise de custos da firma?",
        "<b>Curto prazo</b>: custos fixos são constantes (fábrica, equipamentos).<br>"
        "<b>Longo prazo</b>: todos os custos são variáveis — a empresa pode expandir ou reduzir "
        "capacidade instalada (ex.: comprar nova fábrica). A curva de CTMe de LP difere da de CP.<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Defina economias de escala, deseconomias de escala e retornos constantes de escala.",
        "<b>Economias de escala</b>: CTMe de LP <b>decresce</b> com o aumento de Qt "
        "(expansão reduz custo por unidade).<br>"
        "<b>Retornos constantes de escala</b>: CTMe de LP <b>estável</b> com aumento de Qt.<br>"
        "<b>Deseconomias de escala</b>: CTMe de LP <b>aumenta</b> com Qt "
        "(ex.: burocracia e coordenação em empresas grandes).<br>"
        "<i>Fonte: Anotações + PPT Aula 05 – Teoria da Firma</i>",
    ),
    (
        "Uma firma sempre produz no ponto de maior eficiência de custos (economia de escala)? Por quê?",
        "<b>Não.</b> A quantidade produzida é determinada pela <b>demanda de mercado</b>, não apenas "
        "pelos custos. Ex.: alta demanda pode levar a firma a produzir na fase de retorno constante "
        "mesmo sem incentivo de custo para isso.<br>"
        "<i>Fonte: Anotações – Micro - Teoria da Firma</i>",
    ),

    # ── ISOQUANTAS E ISOCUSTO ─────────────────────────────────────────────────
    (
        "O que é uma isoquanta? Com o que ela se assemelha na teoria do consumidor?",
        "Curva que mostra todas as <b>combinações de dois insumos</b> que geram a <b>mesma "
        "quantidade de produto</b> (iso = igual, quanta = quantidade).<br>"
        "Análoga à <b>curva de indiferença</b> do consumidor (que mantém satisfação constante).<br>"
        "Formato: <b>decrescente e curvada</b>. Representa o <b>output</b> (produção).<br>"
        "<i>Fonte: Anotações – Micro - Teoria da Firma</i>",
    ),
    (
        "O que é uma linha de isocusto? Como se diferencia da isoquanta?",
        "Mostra todas as <b>combinações de dois insumos</b> com o <b>mesmo nível de custo total</b>.<br>"
        "Formato: <b>linha reta decrescente</b> (diferente da isoquanta, que é curvada).<br>"
        "Representa o <b>input</b> (orçamento de insumos). Válida no longo prazo (dois insumos variáveis).<br>"
        "<i>Fonte: Anotações – Micro - Teoria da Firma</i>",
    ),
    (
        "Como se determina o ponto ótimo de produção com isoquantas e isocusto?",
        "O ponto ótimo é onde a <b>isoquanta é tangente à linha de isocusto</b> de menor nível possível.<br>"
        "Nesse ponto a firma produz determinada quantidade ao <b>menor custo possível</b> "
        "(minimização de custo). Se a isoquanta cruza uma isocusto superior, o custo é desnecessariamente alto.<br>"
        "<i>Fonte: Anotações – Micro - Teoria da Firma</i>",
    ),

    # ── RESUMO DAS 3 CARACTERÍSTICAS DAS CURVAS DE CUSTO ────────────────────
    (
        "Quais as 3 características comuns das curvas de custo reveladas graficamente?",
        "1. O <b>CMg aumenta</b> com a quantidade (produtividade marginal decrescente).<br>"
        "2. A curva de <b>CTMe tem formato de U</b>.<br>"
        "3. A curva de <b>CMg cruza a de CTMe no ponto mínimo</b> do CTMe.<br>"
        "<i>Fonte: PPT Aula 05 – Teoria da Firma (Slide 11)</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Economia::Micro - Teoria da Firma",
        "Economia - Micro - Teoria da Firma.apkg",
        CARDS,
    )
