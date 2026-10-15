#!/usr/bin/env python3
"""Gera deck Anki — Economia: Curva de Phillips.

Item do edital: 2.8 Emprego e renda (Lei de Okun e curva de Phillips).

Fontes:
  - Anotações: Macro - Curva de Phillips.md
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


CURVA_DE_PHILLIPS = [

    ("Na formulação original de 1958, Phillips relacionou a taxa de "
     "inflação ao desemprego no Reino Unido; coube a Samuelson e Solow, em "
     "1960, estender a análise para os EUA, substituindo a inflação pelo "
     "crescimento do salário nominal.",
     "<b>ERRADO.</b> A ordem das variáveis está invertida: Phillips (1958) "
     "correlacionou negativamente o crescimento do <b>salário nominal</b> "
     "com o desemprego no Reino Unido. Samuelson e Solow (1960) encontraram "
     "a correlação negativa entre <b>inflação</b> e desemprego nos EUA e "
     "a chamaram de curva de Phillips. [Anotações da aula]"),

    ("Uma expansão da demanda agregada, que eleva a produção e o nível de "
     "preços ao longo da oferta agregada de curto prazo, desloca para a "
     "direita a curva de Phillips, pois combina menos desemprego e mais "
     "inflação.",
     "<b>ERRADO.</b> Choques de demanda movem a economia <b>ao longo</b> da "
     "OA de curto prazo e, de forma correspondente, <b>ao longo</b> da curva "
     "de Phillips (negativamente inclinada): mais inflação e menos "
     "desemprego. Deslocar a curva exige outros fatores, como mudança na "
     "inflação esperada ou choques de oferta. [Anotações da aula]"),

    ("Segundo a Lei de Okun, formulada em 1962 por assessor econômico de "
     "Kennedy, o hiato do produto é proporcional à diferença entre a taxa "
     "de desemprego efetiva e a taxa natural, de modo que o crescimento do "
     "produto se associa a variações do desemprego em sentido inverso.",
     "<b>CERTO.</b> A Lei de Okun propõe relação <b>inversa</b> entre "
     "desemprego e PIB. O hiato do produto (produto efetivo menos "
     "potencial) é proporcional ao hiato do emprego (desemprego efetivo "
     "menos taxa natural): os dois hiatos andam juntos. Na aula, a "
     "fórmula é &Delta;u = &minus;g<sub>y</sub>. [Anotações da aula]"),

    ("Se uma variação de 3 pontos percentuais no desemprego está associada "
     "a uma variação de 4 pontos percentuais na inflação, em sentido "
     "oposto, a taxa de sacrifício é de 0,75: para reduzir a inflação em "
     "1 ponto percentual, o desemprego precisa aumentar 0,75 ponto "
     "percentual.",
     "<b>CERTO.</b> A taxa de sacrifício mede o <b>custo da "
     "desinflação</b> na curva de Phillips: variação do desemprego dividida "
     "pela variação da inflação (aqui, 3/4 = 0,75). Na curva original esse "
     "custo seria permanente; para Friedman e Phelps ele é apenas "
     "temporário. [Anotações da aula]"),

    ("Para Friedman, o governo pode manter o desemprego permanentemente "
     "abaixo da taxa natural, desde que aceite um nível de inflação "
     "elevado, porém estável, pois o trade-off entre inflação e desemprego "
     "é um dado estrutural da economia.",
     "<b>ERRADO.</b> Para manter o desemprego abaixo da taxa natural o "
     "governo precisaria provocar inflação <b>cada vez maior</b> "
     "(aceleração da inflação). O trade-off vale apenas no <b>curto "
     "prazo</b>; por isso a taxa natural é a NAIRU, a taxa que não acelera "
     "a inflação. [Anotações da aula]"),

    ("A curva de Phillips de longo prazo é vertical sobre a taxa natural "
     "de desemprego e equivale à oferta agregada de longo prazo; nela, a "
     "inflação é determinada pelas condições de oferta, enquanto a taxa "
     "natural depende da oferta de moeda.",
     "<b>ERRADO.</b> As determinações estão trocadas. A curva vertical de "
     "longo prazo corresponde, de fato, à OA de longo prazo, mas é a "
     "<b>inflação</b> que é determinada pela <b>oferta de moeda</b>, "
     "enquanto o desemprego flutua em torno da taxa natural, que pode mudar "
     "por condições de oferta (tecnologia e função de produção), embora "
     "tenda a ser estável. [Anotações da aula]"),

    ("Na curva de Phillips com expectativas, em que o desemprego é igual à "
     "taxa natural menos a vezes a diferença entre inflação efetiva e "
     "esperada, uma inflação efetiva superior à esperada eleva o salário "
     "real e reduz o desemprego para abaixo da taxa natural.",
     "<b>ERRADO.</b> Se a inflação efetiva supera a esperada, os salários "
     "são reajustados abaixo da inflação, o <b>salário real cai</b>, os "
     "empresários contratam mais e o desemprego fica abaixo da natural. "
     "O erro de previsão é o que explica o desvio; sem ele, o desemprego "
     "iguala a taxa natural. [Anotações da aula]"),

    ("Quando o Banco Central expande a demanda agregada a partir de um "
     "ponto de baixa inflação e desemprego na taxa natural, a elevação "
     "subsequente da inflação esperada desloca a curva de Phillips de curto "
     "prazo para a esquerda e para baixo, reconduzindo a economia ao "
     "desemprego natural com a inflação original.",
     "<b>ERRADO.</b> Primeiro há movimento ao longo da curva (menos "
     "desemprego, mais inflação). Depois, como a inflação esperada sobe, a "
     "curva se desloca para a <b>direita e para cima</b>. O novo equilíbrio "
     "está na taxa natural, mas com <b>inflação mais alta</b>, igual à "
     "alcançada após a expansão. [Anotações da aula]"),

    ("A taxa natural de desemprego, também denominada NAIRU, é a taxa de "
     "longo prazo em torno da qual o desemprego oscila independentemente "
     "da inflação; ela tende a ser estável, mas pode se alterar por "
     "condições de oferta, como a tecnologia.",
     "<b>CERTO.</b> Hipótese da taxa natural: no longo prazo o desemprego "
     "oscila em torno da taxa normal, qualquer que seja a inflação. A "
     "NAIRU é a taxa que <b>não acelera</b> a inflação. Efetiva abaixo da "
     "natural indica economia aquecida; acima, desaquecida (ciclos "
     "econômicos). [Anotações da aula]"),

    ("O aumento simultâneo de inflação e desemprego nos anos 1970 só pode "
     "ser explicado por choques de demanda, já que choques de oferta, como "
     "o aumento do preço do petróleo pela OPEP, apenas movimentam a "
     "economia ao longo da curva de Phillips.",
     "<b>ERRADO.</b> Choques de oferta (OPEP, 1973 e 1979) elevam custos e "
     "preços para qualquer nível de produto e <b>deslocam</b> a OA e a "
     "curva de Phillips. Friedman e Phelps ainda explicaram o fenômeno "
     "pelas expectativas adaptativas: os agentes aprenderam e a economia "
     "voltou à taxa natural, com inflação mais alta. [Anotações da aula]"),

    ("Para Friedman e Phelps, como o desemprego retorna à taxa natural no "
     "longo prazo, o custo da desinflação é apenas temporário, e uma "
     "redução da inflação de 10% para 5% ao ano configura deflação, pois "
     "o nível de preços passa a subir menos.",
     "<b>ERRADO.</b> A primeira parte está certa (custo temporário, não "
     "permanente como na curva original). Mas cair de 10% para 5% é "
     "<b>desinflação</b>: os preços ainda sobem, a uma taxa menor. "
     "<b>Deflação</b> é queda do nível de preços (inflação negativa). "
     "[Anotações da aula]"),

    ("Incorporada ao IS-LM nos anos 1960, a curva de Phillips complementa "
     "o modelo ao mostrar os efeitos da expansão da demanda agregada, "
     "decorrente de políticas fiscal e monetária, sobre a inflação, em "
     "uma inversão da lei de Say, pois a demanda passa a afetar a oferta "
     "agregada.",
     "<b>CERTO.</b> O IS-LM descreve os movimentos da DA a partir das "
     "políticas fiscal e monetária; a curva de Phillips mostra como essa "
     "expansão afeta a inflação, invertendo a lógica da lei de Say. A "
     "instabilidade dos anos 1970 (Nixon rompe com o padrão-ouro em 1971; "
     "inflação e desemprego crescem juntos) abalou a curva e deu força a "
     "monetaristas e novos clássicos. [Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Macro - Curva de Phillips",
        "Economia - Macro - Curva de Phillips.apkg",
        CURVA_DE_PHILLIPS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
