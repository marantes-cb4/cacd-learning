#!/usr/bin/env python3
"""Gera deck Anki — Economia: Políticas Fiscal e Monetária e a Demanda Agregada.

Itens do edital: 2.3 Economia do Setor Público e Política Fiscal; 2.6
Política Monetária.

Fontes:
  - Anotações: Macro - Políticas Fiscal e Monetária e a Demanda Agregada.md
  - Sem material do professor em PDF/PPT para esta submatéria (só anotação
    própria)
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/economia"
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


POLITICAS_FISCAL_MONETARIA_DA = [

    ("Dado que a oferta de moeda é fixada pelo banco central e, portanto, "
     "inelástica à taxa de juros, um aumento do nível de preços eleva a "
     "demanda por moeda e reduz a taxa de juros de equilíbrio, o que "
     "estimula o investimento e amplia a quantidade demandada ao longo da "
     "curva de demanda agregada.",
     "<b>ERRADO.</b> Com oferta de moeda vertical, o aumento do nível de "
     "preços eleva a demanda por moeda e, no novo equilíbrio, a taxa de "
     "juros <b>sobe</b> — o que <b>reduz</b> o investimento e a quantidade "
     "demandada. É esse o efeito taxa de juros que dá inclinação negativa à "
     "DA. [Anotações da aula]"),

    ("A substituição das metas para agregados monetários (M1, M2) por metas "
     "para a taxa de juros decorreu, entre outros fatores, de a moeda "
     "escritural ser inferior à base monetária, o que facilita o controle "
     "dos agregados pelo banco central.",
     "<b>ERRADO.</b> A moeda escritural <b>supera</b> a base monetária, e "
     "múltiplos fatores fora do controle do BC (quanto os bancos querem "
     "emprestar, quanto as famílias querem poupar) tornam os agregados "
     "difíceis de controlar — daí a adoção de metas para a taxa de juros. "
     "[Anotações da aula]"),

    ("Para expandir a demanda agregada, o banco central pode adquirir "
     "títulos da dívida pública diretamente do Tesouro Nacional no mercado "
     "primário, o que eleva a oferta de moeda e reduz a taxa de juros.",
     "<b>ERRADO.</b> O BC <b>não pode atuar no mercado primário</b> (comprar "
     "títulos diretamente do governo). Sua atuação se dá no <b>mercado "
     "secundário</b>, por operações de mercado aberto: comprar título "
     "expande a oferta de moeda; vender, contrai. [Anotações da aula]"),

    ("Quando o banco central vende títulos públicos no mercado secundário, "
     "o papel fica com o BC e o dinheiro vai para a economia, o que amplia "
     "a oferta de moeda, reduz a taxa de juros e desloca a demanda agregada "
     "para a direita.",
     "<b>ERRADO.</b> Na <b>venda</b> de título o papel vai para a economia "
     "e o BC guarda o dinheiro — a oferta de moeda se <b>contrai</b>, os "
     "juros sobem e a DA tende a se deslocar para a esquerda. Quem expande "
     "a oferta de moeda é a <b>compra</b> de títulos. [Anotações da aula]"),

    ("Em uma economia aberta em que a propensão marginal a consumir é 0,8 e "
     "a propensão marginal a importar é 0,2, o multiplicador dos gastos é "
     "igual a 2,5, ou seja, metade do valor do multiplicador da economia "
     "fechada com a mesma propensão a consumir.",
     "<b>CERTO.</b> Economia aberta: 1/(1 − c + m) = 1/(1 − 0,8 + 0,2) = "
     "1/0,4 = <b>2,5</b>. Economia fechada: 1/(1 − c) = 1/0,2 = <b>5</b>. "
     "Parte do aumento da renda vaza para o exterior via importações, "
     "reduzindo o multiplicador — e quanto maior m, menor ele. [Anotações "
     "da aula]"),

    ("Se o governo aumenta os gastos e os impostos no mesmo montante, o "
     "multiplicador do orçamento equilibrado é igual a 1/(1 − c), de modo "
     "que o produto cresce em valor superior ao do gasto adicional.",
     "<b>ERRADO.</b> Com ΔG = ΔT, ΔY = [1/(1 − c)]ΔG + [−c/(1 − c)]ΔG = "
     "[(1 − c)/(1 − c)]ΔG = ΔG. O multiplicador do orçamento equilibrado é "
     "<b>1</b>: o produto cresce apenas o valor do gasto, <b>sem efeito "
     "multiplicador</b>. [Anotações da aula]"),

    ("Em uma economia fechada em que a propensão marginal a consumir é de "
     "0,75, uma redução de 100 nos tributos eleva o produto de equilíbrio em "
     "400, valor idêntico ao efeito de um aumento de 100 nos gastos do "
     "governo.",
     "<b>ERRADO.</b> O multiplicador tributário é −c/(1 − c) = −0,75/0,25 = "
     "−3: reduzir T em 100 eleva Y em <b>300</b>. O de gastos é 1/(1 − c) = "
     "4, logo +100 em G gera +400. Gasto e tributo têm multiplicadores "
     "diferentes (o do tributo é menor em módulo em 1 unidade). [Anotações da "
     "aula]"),

    ("Uma redução de impostos percebida pelas famílias como temporária tende "
     "a deslocar a demanda agregada mais do que uma redução percebida como "
     "permanente, pois as famílias aproveitam o período limitado para "
     "ampliar o consumo.",
     "<b>ERRADO.</b> O impacto sobre a DA depende da duração percebida: "
     "redução <b>permanente</b> → maior impacto; <b>temporária</b> → menor "
     "impacto (coerente com a teoria da renda permanente de Friedman, em que "
     "ganhos temporários elevam a poupança, não o consumo). [Anotações da "
     "aula]"),

    ("Os estabilizadores automáticos são medidas de política fiscal "
     "adotadas deliberadamente pelos formuladores de política durante "
     "recessões — como o aumento do gasto com seguro-desemprego —, de modo "
     "a estimular a demanda agregada.",
     "<b>ERRADO.</b> Estabilizadores automáticos estimulam a DA na recessão "
     "<b>sem ação deliberada</b> dos formuladores: a arrecadação cai e as "
     "despesas com seguro-desemprego e assistência social sobem por "
     "força das regras já existentes. [Anotações da aula]"),

    ("Os críticos da política de estabilização ativa apontam que a política "
     "fiscal produz efeitos lentos sobre a demanda agregada após ser "
     "implementada, enquanto a política monetária, por atuar sobre a taxa "
     "de juros, produz efeitos imediatos.",
     "<b>ERRADO.</b> Está invertido. A política <b>monetária</b> afeta a "
     "economia com grande atraso (bancos não repassam de imediato a queda da "
     "Selic; consumo e investimento demoram a reagir). A <b>fiscal</b> tem "
     "eficácia rápida <b>quando implementada</b>, mas sua aprovação "
     "legislativa pode levar meses ou anos. [Anotações da aula]"),

    ("Segundo a equivalência ricardiana, o financiamento de um aumento dos "
     "gastos públicos por emissão de dívida eleva a taxa de juros e reduz a "
     "poupança privada, o que gera efeito deslocamento sobre o "
     "investimento.",
     "<b>ERRADO.</b> Para a equivalência ricardiana (Barro-Ricardo), os "
     "consumidores antecipam o aumento futuro de impostos e <b>elevam a "
     "poupança privada</b> no mesmo montante do déficit — a taxa de juros "
     "fica inalterada e financiar por dívida equivale a financiar por "
     "impostos, sem multiplicador. [Anotações da aula]"),

    ("De acordo com a teoria da renda permanente de Milton Friedman, quando "
     "a renda dos consumidores aumenta apenas temporariamente, o consumo "
     "varia na mesma proporção da renda corrente, mantendo-se constante a "
     "propensão a consumir.",
     "<b>ERRADO.</b> Essa é a visão <b>keynesiana</b> do consumo (função da "
     "renda corrente), criticada por Friedman. Pela renda permanente, os "
     "consumidores suavizam o consumo com base na renda média do ciclo de "
     "vida: aumentos temporários elevam a <b>poupança</b>, não o consumo. "
     "[Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Macro - Políticas Fiscal e Monetária e a Demanda Agregada",
        "Economia - Macro - Políticas Fiscal e Monetária e a Demanda Agregada.apkg",
        POLITICAS_FISCAL_MONETARIA_DA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
