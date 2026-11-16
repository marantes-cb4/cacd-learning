#!/usr/bin/env python3
"""Gera deck Anki — Economia: Pós-Guerra: Dutra, Vargas e Café Filho (1946-1955).

Itens do edital: 4.4 Década de 1950 (SALTE, Plano de Metas) — parcial: sem Plano de Metas.

Fontes:
  - Anotações: Pós-Guerra: Dutra, Vargas e Café Filho (1946-1955).md
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


CARDS = [

    ('A abertura cambial do governo Dutra foi abandonada em 1947 porque o êxito em atrair capitais estrangeiros sobrecarregou o balanço de pagamentos e passou a exigir controles para conter a entrada de divisas.',
     "<b>ERRADO.</b> O abandono decorreu da <b>frustração</b> da chamada 'ilusão de divisas': o Brasil se via como credor dos EUA pela guerra e esperava apoio e capitais, mas a entrada foi muito menor, o Plano Marshall não chegou à América Latina e houve déficit com a área de moeda conversível. Voltaram os controles cambiais e de importação, no espírito de Bretton Woods. [Anotações da aula]"),

    ('Mesmo com o discurso liberal de Dutra, a manutenção do câmbio fixo e valorizado favoreceu os exportadores tradicionais, pois estimulava o ingresso de capitais e ampliava a receita em cruzeiros das vendas externas.',
     '<b>ERRADO.</b> O câmbio valorizado <b>beneficiou os industriais</b> (matérias-primas e bens de capital importados mais baratos, e importados contendo a inflação por concorrência) e <b>prejudicou os exportadores</b>, que recebiam menos cruzeiros por dólar. A liberalização da saída de capitais buscava reduzir o risco de investir no Brasil. [Anotações da aula]'),

    ('O forte crescimento industrial do período Dutra é atribuído a uma política deliberada de industrialização, com incentivos diretos do governo ao setor.',
     "<b>ERRADO.</b> A industrialização foi consequência <b>não intencional</b> dos controles cambiais e de importações adotados para resolver problemas do balanço de pagamentos (restrição ao que tinha similar nacional, câmbio barato para máquinas), somada ao crédito do Banco do Brasil. O próprio projeto liberal de Dutra foi 'atropelado' pelo quadro externo. [Anotações da aula]"),

    ('Nos governos Dutra e do segundo Vargas, a contenção monetária e fiscal anunciada pelo Ministério da Fazenda foi reforçada pela atuação do Banco do Brasil, que restringia o crédito para evitar a aceleração da inflação.',
     '<b>ERRADO.</b> O Banco do Brasil agia em <b>contramão</b>: enquanto a Fazenda tentava reduzir moeda e gasto, o BB expandia o crédito, sobretudo à indústria (e, em 1951-52, com Ricardo Jafet, neutralizava a orientação contracionista de Lafer). Por isso a inflação não cedeu. A troca de Corrêa Castro por Guilherme da Silveira marcou a inflexão expansionista sob Dutra. [Anotações da aula]'),

    ('Com câmbio nominal fixo e inflação doméstica superior à americana, o câmbio real do período Dutra se desvalorizou, o que favoreceu as exportações industriais brasileiras para a Europa e para os Estados Unidos.',
     '<b>ERRADO.</b> A inflação interna maior que a dos EUA com câmbio fixo gerou <b>apreciação cambial real</b>: exportações ficaram mais caras em dólar e importações mais baratas. O resultado foi a perda de competitividade e a contração das exportações industriais no fim dos anos 1940. [Anotações da aula]'),

    ('O Plano SALTE, coordenado pelo DASP, previa investimento privado em saúde, transporte e assistência ao trabalhador rural, e investimento público em energia elétrica, e não saiu do papel por completo, razão pela qual não deixou nenhuma obra.',
     '<b>ERRADO.</b> Há duas falhas. A divisão está invertida: o <b>público</b> cuidaria de saúde, transporte, assistência rural e crédito ao produtor, e o <b>privado</b> da energia elétrica. E, apesar da baixa implementação (falta de recursos e de interesse privado), deixou legados, como a Rodovia Rio-Bahia, a Presidente Dutra e o complexo de Paulo Afonso. [Anotações da aula]'),

    ('A Comissão Mista Brasil-Estados Unidos, derivada do Ponto 4 de Truman, elaborou projetos de infraestrutura para financiamento do Eximbank e do Banco Mundial, financiamento que foi mantido após a eleição de Eisenhower e só não se concretizou por falhas brasileiras de execução.',
     '<b>ERRADO.</b> Com Eisenhower (1953) os EUA <b>abandonaram as promessas</b> de financiar os projetos da Comissão Mista, mudando de postura em relação à América Latina. Esse foi um dos fatores do fracasso do projeto inicial do governo, ao lado do baixo influxo de capital estrangeiro e da crise cambial. [Anotações da aula]'),

    ('O projeto do segundo governo Vargas previa, antes dos grandes empreendimentos de infraestrutura, saneamento financeiro ortodoxo para demonstrar austeridade a investidores e organismos multilaterais, em lógica comparável à de Rodrigues Alves, seguida pela de Campos Sales.',
     '<b>ERRADO.</b> A ordem da comparação está invertida: saneamento primeiro (<b>Campos Sales</b>) e obras públicas depois (<b>Rodrigues Alves</b>). Em Vargas, a 1ª etapa era estabilização (menos moeda e gasto) e a 2ª, os grandes empreendimentos para vencer os pontos de estrangulamento, dependendo de capital externo. [Anotações da aula]'),

    ('A crise cambial de 1952 resultou do endurecimento precoce do regime de licenças de importação, que reduziu as exportações e esgotou as reservas em moeda conversível.',
     '<b>ERRADO.</b> O regime de licenças foi <b>frouxo</b> nos primeiros meses, diante de perspectivas favoráveis de divisas. A rápida alta das importações (sobretudo bens de capital), somada à queda das exportações, produziu déficit comercial, esgotamento das reservas conversíveis e atrasados cambiais. A liberalização foi a causa, não o endurecimento. [Anotações da aula]'),

    ('A Instrução 70 da SUMOC, editada na reforma ministerial de 1953 com a entrada de Osvaldo Aranha, preservou o controle quantitativo de importações por cotas, mas unificou a taxa de câmbio e eliminou qualquer tratamento diferenciado para as exportações.',
     '<b>ERRADO.</b> A Instrução 70 criou o <b>monopólio cambial do Banco do Brasil</b>, <b>extinguiu o controle quantitativo</b> (cotas) e instituiu <b>leilões de câmbio</b> por categorias de essencialidade para importar. Nas exportações, trocou as taxas mistas por <b>bonificações</b> sobre a taxa oficial, mantendo tratamento diferenciado por produto. [Anotações da aula]'),

    ('Nos leilões da Instrução 70, as importações de maior essencialidade pagavam as maiores sobretaxas, o que transferia renda da indústria para o setor agrícola exportador e reduzia a arrecadação do setor público com a venda de divisas.',
     '<b>ERRADO.</b> Quanto mais <b>essencial</b> o bem, <b>menor</b> a sobretaxa (a categoria de supérfluos pagava a mais alta). O sistema funcionava como tarifa de importação, alocava divisas conforme a necessidade industrial, <b>transferia renda da agricultura exportadora para a indústria</b> e gerava forte receita ao governo, que comprava dólares barato e os vendia caro. [Anotações da aula]'),

    ('A criação do BNDE e da Petrobras ocorreu no governo Dutra, como desdobramento do Plano SALTE, e consolidou a opção liberal de reduzir a presença do Estado no financiamento de longo prazo e na matriz energética.',
     '<b>ERRADO.</b> BNDE (1952) e Petrobras (1953) são do <b>segundo governo Vargas</b>, parte da política industrial que incluiu os incentivos protecionistas da Instrução 70. Reforçaram o papel do Estado: o BNDE virou o grande financiador de longo prazo (principalmente a partir do Plano de Metas) e a Petrobras tornou-se central na matriz energética. [Anotações da aula]'),

    ('A SUMOC, criada em 1945, funcionava como banco central pleno, com monopólio da emissão de papel-moeda e autonomia para decidir sozinha sobre emissões.',
     '<b>ERRADO.</b> A SUMOC (Estado Novo, 1945) tinha por finalidade normatizar as políticas monetária, creditícia e cambial, <b>preparando a criação de um Banco Central</b>. Exercia funções de banco central (depósitos de bancos, redesconto e juros, orientação do câmbio), mas <b>requeria a emissão de papel-moeda ao Tesouro</b>, e não a decidia sozinha. [Anotações da aula]'),

    ('A Instrução 113 da SUMOC, de 1955, beneficiou sobretudo empresas nacionais ao exigir que máquinas importadas passassem pelos leilões de câmbio, o que protegia a indústria local contra o capital estrangeiro.',
     '<b>ERRADO.</b> A Instrução 113 favoreceu o <b>investidor estrangeiro</b>: a CACEX podia emitir licenças de importação <b>sem cobertura cambial</b> para máquinas e equipamentos, evitando o leilão (mais caro que a taxa livre aplicada à entrada de capitais). Estimulou o IDE das multinacionais, sobretudo no período seguinte, com o setor automobilístico. Veio na gestão ortodoxa de Gudin, com Café Filho. [Anotações da aula]'),

    ("O ministro Whitaker, no governo Café Filho, criticou o 'confisco cambial' sobre os exportadores de café e propôs a unificação cambial, o que implicaria valorizar a moeda doméstica; o projeto foi aprovado rapidamente pela Câmara.",
     '<b>ERRADO.</b> A unificação cambial acabaria com as taxas múltiplas da Instrução 70 e levaria à <b>desvalorização</b> da moeda doméstica. Café Filho enviou o projeto à Câmara, o que significou o <b>seu sepultamento</b>. Whitaker renunciou, e seu substituto, Mário Câmara, pouco pôde fazer nos meses restantes. [Anotações da aula]'),

]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Pós-Guerra - Dutra, Vargas e Café Filho (1946-1955)",
        "Economia - Pós-Guerra - Dutra, Vargas e Café Filho (1946-1955).apkg",
        CARDS,
    )
