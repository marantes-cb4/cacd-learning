#!/usr/bin/env python3
"""Gera deck Anki — Economia: Conceitos Básicos de Economias Abertas.

Item do edital: 3.2 Macroeconomia aberta.

Fontes:
  - Anotações: Macro - Conceitos Básicos de Economias Abertas.md
  - Sem material do professor em PDF para esta submatéria (só anotação própria)
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelreichelt/Desktop/cacd-learning/anki/decks/economia"
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


ECONOMIAS_ABERTAS = [

    ("Em uma economia aberta, o investimento externo líquido (IEL) e as "
     "exportações líquidas (EL) constituem duas variáveis macroeconômicas "
     "distintas e independentes, de modo que um aumento das exportações "
     "líquidas de um país não implica necessariamente uma variação equivalente "
     "do seu investimento externo líquido.",
     "<b>ERRADO.</b> Para a economia como um todo, IEL = EL é uma "
     "<b>identidade contábil</b>: toda transação que afeta um lado do balanço "
     "de pagamentos afeta o outro no mesmo montante. Não são variáveis "
     "independentes. [Anotações da aula]"),

    ("O grau de abertura de uma economia é medido pela razão entre o saldo da "
     "balança comercial (exportações líquidas) e o PIB, sendo tanto maior "
     "quanto maior for o superávit comercial do país.",
     "<b>ERRADO.</b> Grau de abertura = (exportações + importações) / PIB — "
     "mede o total de fluxo comercial (entrada e saída) como percentual do "
     "PIB, não o saldo (superávit/déficit) comercial. [Anotações da aula]"),

    ("A poupança nacional de uma economia aberta é igual à soma do "
     "investimento interno com o investimento externo líquido, de modo que "
     "S = I + IEL.",
     "<b>CERTO.</b> Decorre da identidade Y = C+I+G+EL e da definição de "
     "poupança nacional: S = I + EL = I + IEL, já que IEL = EL. "
     "[Anotações da aula]"),

    ("Em regimes de câmbio flexível, o termo técnico correto para designar o "
     "aumento do valor de uma moeda em relação à moeda estrangeira é "
     "valorização, reservando-se o termo apreciação para os regimes de câmbio "
     "fixo.",
     "<b>ERRADO.</b> É o oposto: <b>apreciação/depreciação</b> são os termos "
     "usados para câmbio flexível; <b>valorização/desvalorização</b> são "
     "usados para câmbio fixo. [Anotações da aula]"),

    ("Segundo a teoria da paridade do poder de compra, no longo prazo a taxa "
     "de câmbio nominal se ajusta de modo que a taxa de câmbio real tenda a 1, "
     "e países com inflação doméstica mais alta que a externa tendem a "
     "registrar depreciação de sua moeda.",
     "<b>CERTO.</b> É exatamente a conclusão da PPC: E = P/P*, logo quanto "
     "maior a inflação doméstica em relação à externa, maior a taxa de câmbio "
     "nominal (mais desvalorização/depreciação). [Anotações da aula]"),

    ("A teoria da paridade do poder de compra é uma explicação precisa e "
     "universalmente válida da determinação da taxa de câmbio, aplicando-se "
     "igualmente bem a bens de consumo de baixa comercializabilidade e a "
     "commodities internacionais homogêneas.",
     "<b>ERRADO.</b> A PPC tem limitações: nem todos os bens são facilmente "
     "comercializáveis (tarifas, custo de transporte) nem substitutos "
     "perfeitos entre países; aplica-se melhor a <b>commodities</b> "
     "(ex.: petróleo) do que a bens de consumo de baixa comercialização. "
     "[Anotações da aula]"),

    ("A paridade de juros coberta estabelece que a taxa de juros doméstica "
     "deve igualar a taxa de juros internacional, sem considerar prêmios "
     "adicionais por risco cambial ou risco de calote do país.",
     "<b>ERRADO.</b> Isso descreve a paridade de juros <b>descoberta</b> "
     "(i = i*). A paridade <b>coberta</b> é i = i* + Ê + PR, incluindo "
     "expectativa de depreciação cambial (Ê) e prêmio de risco (PR). "
     "[Anotações da aula]"),

    ("Caso a taxa de juros doméstica supere a soma entre a taxa de juros "
     "internacional, a expectativa de depreciação cambial e o prêmio de risco "
     "do país, espera-se entrada de capitais estrangeiros e consequente "
     "apreciação da moeda doméstica.",
     "<b>CERTO.</b> Quando i > i* + Ê + PR, o investimento doméstico se torna "
     "mais atrativo, atraindo capital estrangeiro, o que eleva a demanda pela "
     "moeda doméstica e a aprecia. [Anotações da aula]"),

    ("Dentre os regimes cambiais, o currency board caracteriza-se pela fixação "
     "do câmbio por meio de lei doméstica, o que dificulta sua alteração, "
     "enquanto a dolarização consiste na adoção do dólar como moeda de curso "
     "interno na economia doméstica.",
     "<b>CERTO.</b> Definições corretas de ambos os regimes, situados nos "
     "extremos mais rígidos do espectro de regimes cambiais. "
     "[Anotações da aula]"),

    ("O regime de flutuação suja (ou administrada) é, dentre os regimes "
     "cambiais, o mais próximo do câmbio fixo, já que o governo intervém "
     "sistematicamente para manter a moeda dentro de bandas predeterminadas "
     "por lei.",
     "<b>ERRADO.</b> A flutuação suja está mais próxima do câmbio "
     "<b>flexível</b>: o câmbio é geralmente determinado pelo mercado, com "
     "intervenção do governo apenas em casos de apreciação/depreciação "
     "excessiva — não há bandas fixadas em lei (isso caracteriza o regime de "
     "bandas, que é distinto). [Anotações da aula]"),

    ("No curto prazo, os fluxos de capitais de curto prazo (investimentos de "
     "carteira) tendem a ser mais voláteis que os fluxos comerciais e de "
     "renda, de modo que acabam predominando na determinação da taxa de "
     "câmbio nominal no curto prazo.",
     "<b>CERTO.</b> Os fluxos comerciais/de renda são mais estáveis, enquanto "
     "os fluxos de capital de curto prazo (carteira) são mais voláteis e "
     "acabam definindo a taxa de câmbio no curto prazo. "
     "[Anotações da aula]"),

    ("Uma queda da bolsa de valores brasileira tende a provocar, no curto "
     "prazo, apreciação do real frente ao dólar, na medida em que "
     "investidores estrangeiros liquidam suas posições em ações e migram "
     "para outros ativos domésticos.",
     "<b>ERRADO.</b> O contrário: queda da bolsa leva estrangeiros a "
     "<b>vender</b> ações brasileiras e <b>comprar</b> dólares (para levar o "
     "capital para fora), aumentando a demanda por dólar e "
     "<b>depreciando</b> o real. [Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Conceitos Básicos de Economias Abertas",
        "Economia - Conceitos Básicos de Economias Abertas.apkg",
        ECONOMIAS_ABERTAS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
