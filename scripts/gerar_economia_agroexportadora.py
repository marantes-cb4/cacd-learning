#!/usr/bin/env python3
"""Gera deck Anki — Economia: Economia Agroexportadora.

Itens do edital: 4.1 Economia brasileira no século XIX (economia cafeeira); 4.2 Primeira República.

Fontes:
  - Anotações: Economia Agroexportadora.md
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


AGROEXPORTADORA = [

    ("A obra de Celso Furtado sobre a formação econômica do Brasil adota "
     "uma abordagem essencialmente descritiva e cronológica, evitando "
     "formular hipóteses causais; seu foco é a inserção da economia "
     "brasileira nos ciclos de exportação, sem relação com o "
     "subdesenvolvimento.",
     "<b>ERRADO.</b> A abordagem é <b>analítica</b>, não descritiva: busca "
     "nexos causais e lança hipóteses (depois confirmadas, ajustadas ou "
     "negadas pela literatura). O objetivo central é explicar as causas "
     "históricas do <b>subdesenvolvimento</b> brasileiro, com atenção à "
     "inserção externa e ao desequilíbrio externo. Furtado é autor "
     "cepalino. [Anotações da aula]"),

    ("Numa economia escravista, a expansão das exportações levava à "
     "compra de mais escravos e a contração, à migração para a "
     "subsistência, sem alterar a estrutura produtiva; no trabalho "
     "assalariado, o crescimento exportador pode provocar mudanças "
     "estruturais.",
     "<b>CERTO.</b> Sob a escravidão, crescimento e contração se davam "
     "pela escala da produção e do setor de subsistência, <b>sem mudança "
     "estrutural</b>. O trabalho assalariado altera o circuito da renda "
     "(multiplicador, importações, moeda) e permite transformações "
     "estruturais. [Anotações da aula]"),

    ("Quando as exportações de café crescem numa economia de trabalho "
     "assalariado, a renda interna tende a aumentar mais do que as "
     "exportações, e, como o país importava quase todos os manufaturados, "
     "a demanda por importações passa a crescer mais rápido que as "
     "exportações, o que gera tendência ao desequilíbrio externo.",
     "<b>CERTO.</b> É a combinação de dois efeitos: o <b>multiplicador</b> "
     "(a exportação gera consumo de exportadores e assalariados, e o "
     "efeito final supera o inicial) e o <b>elevado coeficiente de "
     "importações</b> (a renda adicional vaza para o exterior). [Anotações "
     "da aula]"),

    ("Numa crise mundial que reduz as exportações, o padrão-ouro atenuava "
     "o choque ao permitir que a oferta de moeda se expandisse para "
     "compensar a queda da demanda externa, evitando que o país tivesse "
     "de abandonar o regime.",
     "<b>ERRADO.</b> No padrão-ouro a oferta de moeda acompanhava o saldo "
     "do balanço de pagamentos: déficit exigia contração monetária, "
     "<b>agravando</b> a queda da demanda. Por isso o país muitas vezes "
     "saía do padrão, desvalorizando a moeda e emitindo sem lastro, o "
     "que gerava inflação via importados. [Anotações da aula]"),

    ("Diante de uma queda do preço internacional do café, a desvalorização "
     "cambial mantém a receita do exportador em moeda doméstica e "
     "preserva o nível de emprego, mas encarece os produtos importados, "
     "gerando inflação.",
     "<b>CERTO.</b> É a chamada <b>defesa do nível de renda</b>: a "
     "desvalorização compensa a queda do preço externo para o exportador. "
     "Seu custo é o encarecimento de importações e de insumos, com "
     "problema crônico de inflação. [Anotações da aula]"),

    ("Como a desvalorização cambial preservava o emprego, seus benefícios "
     "se distribuíam por toda a sociedade, inclusive pelos assalariados "
     "urbanos, que ganhavam poder de compra com a manutenção da atividade "
     "exportadora.",
     "<b>ERRADO.</b> Ocorre <b>socialização das perdas</b>: os ganhos "
     "ficavam com os exportadores e o custo (inflação e perda de poder "
     "de compra no mercado internacional) era repartido por todos. As "
     "transferências de renda iam da subsistência, dos trabalhadores "
     "rurais e das populações urbanas assalariadas para o setor "
     "exportador e seus proprietários. [Anotações da aula]"),

    ("Segundo o raciocínio de Furtado, seria preferível que a queda do "
     "preço do café fosse integralmente absorvida pelos lucros dos "
     "empresários exportadores, pois isso evitaria a desvalorização e "
     "protegeria a coletividade da inflação.",
     "<b>ERRADO.</b> Para Furtado era vantajoso à coletividade manter o "
     "nível das exportações (defendendo o emprego), mas isso exigia que o "
     "impacto da crise <b>não se concentrasse nos lucros</b> dos "
     "empresários; do contrário, parte deles seria forçada a paralisar "
     "as atividades. [Anotações da aula]"),

    ("Com a disseminação do trabalho assalariado no fim do século XIX, "
     "aumentou a demanda por moeda; o sistema bancário concentrado na "
     "capital e a baixa propensão do público a poupar em bancos limitavam "
     "a criação de moeda escritural, que ficava próxima da base monetária, "
     "sem efeito multiplicador bancário.",
     "<b>CERTO.</b> O salário amplia a monetização da economia e a "
     "demanda por moeda. O sistema bancário, precário e vulnerável à "
     "sazonalidade, não conseguia expandir crédito, o que pressionava "
     "por mais emissão de moeda. [Anotações da aula]"),

    ("O retorno do Brasil ao padrão-ouro, em 1889, exigiu forte esforço "
     "deflacionista do governo imperial; ainda assim, a emissão "
     "conversível mostrou-se suficiente para atender à demanda por moeda "
     "gerada pelo trabalho assalariado.",
     "<b>ERRADO.</b> O retorno à paridade de 1846 decorreu de uma situação "
     "cambial muito favorável, <b>sem esforço deflacionista</b>. E a "
     "emissão conversível (lastreada em ouro) <b>não foi suficiente</b>: "
     "já no fim de 1889 se pedia nova emissão. [Anotações da aula]"),

    ("Na disputa dos anos 1890, os papelistas, liderados por Rui Barbosa, "
     "defendiam manter o padrão-ouro, enquanto os metalistas queriam "
     "emissão não conversível para estimular a industrialização; a lei "
     "bancária de 1890 passou a lastrear a emissão em títulos da dívida "
     "pública.",
     "<b>ERRADO</b> na primeira parte: estão trocados. <b>Metalistas</b> "
     "defendiam o padrão-ouro; <b>papelistas</b> queriam emissão não "
     "conversível para estimular a atividade e a industrialização. A "
     "segunda parte está correta: o lastro em dívida pública se "
     "assemelha ao mecanismo moderno do banco central. [Anotações da aula]"),

    ("A interpretação tradicional atribui a crise cambial de 1891 "
     "exclusivamente à expansão monetária das reformas de Rui Barbosa, "
     "desconsiderando fatores externos, como o colapso da casa Baring "
     "Brothers e a moratória da Argentina.",
     "<b>ERRADO.</b> A interpretação tradicional realmente enfatiza a "
     "expansão monetária de 1890 (uma \"bolha\"), mas a queda do câmbio "
     "também é atribuída a hesitações dos sucessores de Rui e a "
     "influências <b>exógenas</b>, como o colapso da Baring e a moratória "
     "argentina. [Anotações da aula]"),

    ("Embora a participação do Brasil no comércio mundial fosse muito "
     "pequena na virada para o século XX, o país era relevante como "
     "destino de investimento estrangeiro, razão pela qual o valor das "
     "exportações per capita, por si só, não o define como economia "
     "aberta.",
     "<b>CERTO.</b> A inserção brasileira era muito mais financeira do "
     "que comercial: comércio mundial inferior a 1% e participação "
     "substancial no investimento internacional (parcela expressiva do "
     "estoque de capital estrangeiro na América Latina). [Anotações da "
     "aula]"),

    ("Os fluxos de capitais externos no Brasil dos anos 1890 eram "
     "estabilizadores, como nos países centrais, em que as saídas de "
     "capital tinham comportamento contracíclico; no Brasil, a saída de "
     "capitais não se associava às crises cambiais.",
     "<b>ERRADO.</b> A tese contrária à visão da conta capital como "
     "estabilizadora é que os fluxos eram <b>pró-cíclicos</b> e "
     "<b>desestabilizadores</b>, com forte correlação entre saída de "
     "capitais e crise cambial. Nos países centrais o comportamento era "
     "contracíclico; nos periféricos, os mesmos mecanismos geravam "
     "instabilidade. [Anotações da aula]"),

    ("O funding scheme negociado com os Rothschild rolou a dívida externa "
     "em troca de saneamento fiscal e monetário; sua execução por "
     "Joaquim Murtinho, vista como seleção natural entre devedores, "
     "provocou falências bancárias, e a apreciação cambial que se seguiu "
     "não pode ser atribuída com certeza apenas à contração monetária.",
     "<b>CERTO.</b> A rolagem foi condicionada à redução do déficit e da "
     "oferta de moeda. A contração gerou uma avalanche de falências "
     "(inclusive do BRB), mas a apreciação cambial também teve relação "
     "com a recuperação das exportações em 1899 (borracha) e com nova "
     "entrada de capitais, pela percepção dos banqueiros. [Anotações da "
     "aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Economia Agroexportadora",
        "Economia - Economia Agroexportadora.apkg",
        AGROEXPORTADORA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
