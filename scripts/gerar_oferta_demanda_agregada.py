#!/usr/bin/env python3
"""Gera deck Anki — Economia: Modelo de Oferta e Demanda Agregada.

Item do edital: 2.1 Contabilidade Nacional (oferta e demanda agregadas —
teorias clássica e keynesiana de determinação da renda no curto prazo).

Fontes:
  - Anotações: Modelo de Oferta e Demanda Agregada.md
  - Sem material do professor em PDF para esta submatéria (só anotação
    própria)
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


OFERTA_DEMANDA_AGREGADA = [

    ("Dentre os três fatos-chave sobre flutuações econômicas identificados "
     "pela literatura macroeconômica, destaca-se que as principais "
     "variáveis macroeconômicas — como produto, emprego e inflação — "
     "tendem a flutuar de forma independente entre si, cada uma reagindo a "
     "choques distintos e em momentos diferentes do ciclo econômico.",
     "<b>ERRADO.</b> É o oposto: um dos 3 fatos-chave é que a "
     "<b>maioria das variáveis macroeconômicas flutua conjuntamente</b> — "
     "produto, emprego e inflação tendem a se mover juntos ao longo do "
     "ciclo. Os outros 2 fatos são: as flutuações são irregulares e "
     "imprevisíveis; e a queda da produção eleva o desemprego. [Anotações "
     "da aula]"),

    ("A inclinação negativa da curva de demanda agregada decorre de três "
     "efeitos que operam simultaneamente diante de uma queda no nível "
     "geral de preços: o efeito riqueza eleva o consumo, o efeito taxa de "
     "juros estimula o investimento e o efeito taxa de câmbio real eleva "
     "as exportações líquidas.",
     "<b>CERTO.</b> Nível de preços menor → riqueza real maior (consumo "
     "sobe); menor demanda por moeda reduz os juros (investimento sobe); "
     "câmbio real deprecia (exportações líquidas sobem) — os 3 efeitos "
     "empurram a demanda agregada na mesma direção. [Anotações da aula]"),

    ("Uma redução do nível geral de preços na economia provoca um "
     "deslocamento da curva de demanda agregada para a direita, já que "
     "estimula simultaneamente o consumo, o investimento e as exportações "
     "líquidas por meio dos efeitos riqueza, taxa de juros e taxa de "
     "câmbio.",
     "<b>ERRADO.</b> Uma variação do <b>nível de preços</b> move a "
     "economia AO LONGO da curva de DA (já existente), não a desloca. "
     "Deslocamentos da DA decorrem de mudanças <b>autônomas</b> em C, I, G "
     "ou EL — não de variações do próprio nível de preços, que é uma das "
     "variáveis do próprio gráfico. [Anotações da aula]"),

    ("A taxa natural de desemprego, conceito atribuído a Milton Friedman, "
     "corresponde ao nível de desemprego que a economia atingiria em pleno "
     "emprego, ou seja, um desemprego próximo de zero, e serve de "
     "referência para medir o quanto uma economia está aquecida ou "
     "desaquecida.",
     "<b>ERRADO.</b> A taxa natural NÃO é desemprego zero — é a taxa que "
     "mantém a <b>inflação CONSTANTE</b>. Desemprego acima da taxa natural "
     "→ economia desaquecida → inflação cai; abaixo → economia aquecida → "
     "inflação sobe. [Anotações da aula]"),

    ("A curva de oferta agregada de longo prazo é vertical na taxa natural "
     "de produto, pois nesse horizonte prevalece a dicotomia clássica — o "
     "nível de preços não afeta variáveis reais —, ao passo que a curva de "
     "oferta agregada de curto prazo apresenta inclinação positiva.",
     "<b>CERTO.</b> No longo prazo, o produto não depende do nível de "
     "preços (dicotomia clássica, moeda neutra) — daí a verticalidade da "
     "AS-LP na taxa natural. No curto prazo, salários/preços rígidos e "
     "percepções equivocadas geram a inclinação positiva da AS-CP. "
     "[Anotações da aula]"),

    ("Dentre as três teorias que explicam a inclinação positiva da curva "
     "de oferta agregada de curto prazo, a teoria dos salários rígidos — "
     "considerada a mais relevante e sólida — sustenta que um nível de "
     "preços inesperadamente baixo eleva o salário real dos trabalhadores, "
     "tornando-os mais caros para as empresas e levando a uma redução do "
     "emprego e da produção.",
     "<b>CERTO.</b> Com salário nominal fixo e preços mais baixos, o "
     "salário real sobe — encarecendo o trabalhador para a empresa, que "
     "reage empregando e produzindo menos. É considerada a teoria mais "
     "sólida entre as três (salários rígidos, preços rígidos, percepções "
     "equivocadas). [Anotações da aula]"),

    ("Segundo a equação da oferta agregada de curto prazo, a quantidade "
     "ofertada de produto se afasta da produção natural na proporção "
     "direta do desvio entre o nível de preços vigente e o nível de "
     "preços esperado, de modo que, quanto maior o parâmetro que mede essa "
     "sensibilidade, menor será a resposta do produto a um dado desvio de "
     "preços.",
     "<b>ERRADO.</b> É o oposto: quanto MAIOR o parâmetro <i>a</i> na "
     "equação Qt = Produção natural + a·(P vigente − P esperado), <b>MAIS "
     "sensível</b> (maior) será a resposta do produto a um dado desvio "
     "entre o nível de preços vigente e o esperado — não menor. "
     "[Anotações da aula]"),

    ("Diante de uma contração da demanda agregada, o modelo de oferta e "
     "demanda agregada prevê que, no curto prazo, tanto a quantidade "
     "produzida quanto o nível de preços caem; no longo prazo, à medida "
     "que os salários se reajustam, o produto retorna à taxa natural, mas "
     "o nível de preços permanece mais baixo do que o inicial.",
     "<b>CERTO.</b> É exatamente o mecanismo do choque de demanda: DA "
     "desloca à esquerda, gerando hiato recessivo (produto e preços caem "
     "no CP); no LP, o reajuste salarial devolve o produto à taxa natural, "
     "mas em um nível de preços permanentemente mais baixo. [Anotações da "
     "aula]"),

    ("Um choque exógeno que contraia a curva de oferta agregada, como um "
     "choque do preço internacional do petróleo, provoca no curto prazo um "
     "novo equilíbrio com produto menor e nível de preços mais alto "
     "simultaneamente — fenômeno conhecido como estagflação.",
     "<b>CERTO.</b> Estagflação é justamente a combinação de queda na "
     "produção (estagnação) com alta do nível de preços (inflação), típica "
     "de um choque de oferta negativo. [Anotações da aula]"),

    ("Diante de um choque de oferta que provoque estagflação, caso o "
     "governo decida acomodar o choque por meio de política fiscal ou "
     "monetária expansionista para devolver o produto à sua taxa natural, "
     "o resultado será um nível de preços de equilíbrio ainda mais alto do "
     "que o observado no ponto de estagflação original.",
     "<b>CERTO.</b> A acomodação expande a demanda agregada até o produto "
     "retornar à taxa natural, mas isso ocorre a um nível de preços ainda "
     "mais elevado do que no ponto de estagflação — trocando menor queda "
     "de produção por mais inflação. [Anotações da aula]"),

    ("No longo prazo, deslocamentos da curva de demanda agregada — "
     "provocados, por exemplo, por políticas fiscais ou monetárias — são "
     "capazes de elevar permanentemente o produto de equilíbrio da "
     "economia, ainda que às custas de um nível de preços mais alto.",
     "<b>ERRADO.</b> No longo prazo, deslocamentos da demanda agregada "
     "afetam APENAS o <b>nível de preços</b>, não a produção — prevalece a "
     "dicotomia clássica. Só deslocamentos da oferta agregada de longo "
     "prazo (trabalho, capital, recursos naturais, tecnologia) alteram o "
     "produto de equilíbrio permanentemente. [Anotações da aula]"),

    ("No processo de crescimento econômico de longo prazo, a curva de "
     "oferta agregada de longo prazo e a curva de demanda agregada tendem "
     "a se deslocar simultaneamente para a direita, já que o aumento da "
     "capacidade produtiva da economia costuma ser acompanhado por maior "
     "oferta de moeda pelo Banco Central, resultando em produto e nível de "
     "preços mais altos ao longo do tempo.",
     "<b>CERTO.</b> Mais trabalho, capital, recursos e tecnologia deslocam "
     "a AS-LP à direita; o BC, acompanhando o maior produto, expande a "
     "oferta de moeda, deslocando também a DA à direita — resultando em "
     "crescimento do produto com alguma inflação ao longo do tempo. "
     "[Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Modelo de Oferta e Demanda Agregada",
        "Economia - Modelo de Oferta e Demanda Agregada.apkg",
        OFERTA_DEMANDA_AGREGADA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
