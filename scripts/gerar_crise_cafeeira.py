#!/usr/bin/env python3
"""Gera deck Anki — Economia: Crise da Economia Cafeeira e Deslocamento do Centro Dinâmico.

Itens do edital: 4.2 Primeira República; 4.3 Industrialização 1930–1945 (ISI).

Fontes:
  - Anotações: Crise da Economia Cafeeira e Deslocamento do Centro Dinâmico.md
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


F = "[Anotações da aula]"

CAFE = [

    ("Diante da queda do preço internacional do café após a crise "
     "norte-americana de 1893, a depreciação cambial preservava a receita "
     "do cafeicultor em moeda nacional, e o custo do ajuste recaía "
     "principalmente sobre os próprios produtores de café.",
     "<b>ERRADO.</b> A desvalorização mantinha a receita do cafeicultor "
     "em moeda nacional, mas <b>transferia o custo</b> para o restante da "
     "sociedade: importados mais caros e perda de poder de compra dos "
     "assalariados urbanos (socialização das perdas). Foi esse custo "
     "social que, mais tarde, tornou o instrumento politicamente "
     "inviável. " + F),

    ("O abandono da desvalorização cambial como instrumento de defesa do "
     "café, por volta de 1897, decorreu sobretudo do esgotamento das "
     "reservas em ouro do país, e não de pressões de grupos sociais "
     "internos.",
     "<b>ERRADO.</b> O obstáculo foi <b>político-social</b>: surgiram "
     "novos grupos de pressão — trabalhadores urbanos e industrialistas — "
     "que perdiam poder de compra de importados a cada desvalorização, "
     "gerando intranquilidade social. A pegadinha troca a causa interna "
     "(coalizão de perdedores) por uma restrição de reservas. " + F),

    ("Se a superprodução cafeeira fosse deixada ao ajuste espontâneo do "
     "mercado, a eliminação dos produtores menos eficientes e a redução "
     "das plantações recomporiam os preços, sem maiores efeitos sobre o "
     "mercado interno, pois a queda das exportações não se propagaria "
     "pela economia.",
     "<b>ERRADO.</b> O ajuste natural passaria pelo preço baixo, falência "
     "dos ineficientes e corte de investimentos, mas o <b>multiplicador "
     "opera em sentido inverso</b>: a queda das exportações se propaga ao "
     "mercado interno com força ainda maior. Seria um movimento "
     "<b>recessivo</b>, e é isso que a defesa estatal buscou evitar. " + F),

    ("No Convênio de Taubaté (1906), a retirada dos excedentes de café do "
     "mercado foi financiada principalmente pela emissão de moeda "
     "inconversível, ao passo que o capital estrangeiro só passou a ser "
     "utilizado nas operações de defesa posteriores à Grande Depressão.",
     "<b>ERRADO.</b> Em 1906 as compras foram financiadas por "
     "<b>empréstimos estrangeiros</b>, cujo serviço seria coberto por "
     "imposto sobre o café exportado. A <b>emissão de moeda</b> aparece na "
     "defesa de 1917–20; após 1929 os empréstimos externos desapareceram "
     "e o crédito interno passou a financiar as compras. A banca "
     "inverte a ordem das fontes de financiamento. " + F),

    ("A garantia estatal de compra dos excedentes reduzia o risco do "
     "cafeicultor e, por isso, estimulava a expansão da capacidade "
     "produtiva, agravando o excesso de oferta que a política pretendia "
     "corrigir — o que Furtado descreve como transferência para o futuro "
     "da solução de um problema crescente.",
     "<b>CERTO.</b> Com o governo como garantidor, investir em café "
     "tornava-se seguro, o que reforçava a fonte do desequilíbrio. Além "
     "disso, o preço sustentado estimulava a oferta de <b>outros "
     "países</b>, corroendo o poder de monopólio brasileiro (mais de 75% "
     "da produção mundial). O êxito inicial consolidou o poder dos "
     "cafeicultores até a década de 1930. " + F),

    ("A forte alta da renda per capita norte-americana nos anos 1920 "
     "elevou na mesma direção o consumo de café, o que atenuou o "
     "problema de excesso de oferta enfrentado pelo Brasil.",
     "<b>ERRADO.</b> A renda dos EUA subiu cerca de 35%, mas o consumo "
     "por habitante ficou praticamente estável (cerca de 12 libras): a "
     "demanda por café é <b>inelástica em relação à renda</b>. O "
     "crescimento da renda externa, portanto, não absorvia a supersafra, "
     "e os estoques só cresciam — mais de 10% do PIB brasileiro em 1929. "
     + F),

    ("O acúmulo de divisas decorrente dos empréstimos da defesa de 1927 "
     "e do preço artificialmente sustentado do café permitiu a "
     "readoção da conversibilidade; com a crise de 1929, essa mesma "
     "regra acelerou a perda das reservas, pois a conversão em ouro "
     "estava disponível a todos.",
     "<b>CERTO.</b> A situação confortável do balanço de pagamentos "
     "levou ao retorno ao padrão-ouro, mas, quando a crise começou, "
     "<b>todos converteram</b> e as reservas sumiram em poucos meses. O "
     "mecanismo é o mesmo do padrão-ouro em Furtado: a regra cambial "
     "amplifica o choque externo em vez de amortecê-lo. " + F),

    ("Após 1929, a queda de cerca de 60% no preço do café foi "
     "acompanhada de retração das quantidades vendidas ao exterior "
     "entre 1929 e 1937, de modo que a receita de exportação se "
     "contraiu apenas pelo efeito-quantidade.",
     "<b>ERRADO.</b> O preço caiu cerca de 60%, mas as <b>vendas "
     "aumentaram cerca de 25%</b> entre 1929 e 1937: a receita caiu pelo "
     "efeito-preço, com quantidade maior. Somada à desvalorização de "
     "cerca de 40% após o fim da conversibilidade, a política reeditou a "
     "socialização das perdas em favor da elite cafeeira. " + F),

    ("A compra e a destruição dos estoques de café após 1929, se "
     "financiadas por empréstimos externos, teriam produzido o mesmo "
     "estímulo sobre o mercado interno que o financiamento por expansão "
     "do crédito doméstico.",
     "<b>ERRADO.</b> O efeito keynesiano decorreu de o programa ser "
     "financiado por <b>crédito interno</b>: gerou renda e sustentou a "
     "demanda agregada. Dinheiro externo não teria esse efeito — e, de "
     "todo modo, os empréstimos externos haviam desaparecido com a "
     "crise. A política antecipou o raciocínio de Keynes, antes da "
     "publicação da <i>Teoria Geral</i>. " + F),

    ("Na década de 1930, a manutenção da renda interna combinada com a "
     "forte restrição da capacidade de importar redirecionou a demanda "
     "por manufaturados para a produção doméstica e atraiu para a "
     "indústria o capital que antes iria à cafeicultura.",
     "<b>CERTO.</b> É a essência do <b>deslocamento do centro "
     "dinâmico</b>: a renda sustentada mantinha a demanda por "
     "manufaturados; sem poder importá-los, abriam-se oportunidades "
     "para o setor interno. O novo investimento migrou para algodão e, "
     "sobretudo, para a indústria voltada ao mercado interno, que passou "
     "a ser a fonte principal de dinamismo. " + F),

    ("A recuperação industrial brasileira após 1929 dependeu "
     "essencialmente da importação de equipamentos novos financiada por "
     "capital estrangeiro, que permitiu ampliar a capacidade produtiva "
     "instalada.",
     "<b>ERRADO.</b> A queda industrial foi de apenas cerca de 10%, e "
     "em 1933 a produção já se recuperara por meio de: (i) uso da "
     "<b>capacidade já instalada nos anos 1920</b>; (ii) compra de "
     "<b>máquinas de segunda mão muito baratas</b>, vendidas por países "
     "desenvolvidos em crise. A escassez de divisas e de capital externo "
     "era justamente a restrição, não o motor. " + F),

    ("Num país subdesenvolvido, a criação de uma indústria doméstica de "
     "bens de capital é em geral passo muito difícil; no Brasil dos "
     "anos 1930, a persistente falta de capacidade de importar atuou "
     "como proteção que favoreceu esse desenvolvimento.",
     "<b>CERTO.</b> A restrição às importações valia também para "
     "<b>máquinas e equipamentos</b>, de modo que o setor interno passou "
     "a suprir essa demanda (ex.: máquinas de costura para a indústria "
     "têxtil). Como a capacidade de importar não se recuperou, a "
     "restrição funcionou como defesa natural da indústria nascente. "
     + F),

    ("Com a Grande Depressão, a defesa do café deixou de ser conduzida "
     "pelo Instituto Paulista de Defesa Permanente do Café e passou ao "
     "governo federal, porque a crise combinou queda de demanda "
     "externa e excesso de oferta decorrente de supersafra e estoques.",
     "<b>CERTO.</b> Em 1929/30 houve crise de <b>demanda</b> (Depressão, "
     "preços baixos) e de <b>oferta</b> (supersafra e estoque enorme, "
     "com produção exportável dobrada entre 1925 e 1929). O esquema "
     "paulista deixa de ser suficiente e a defesa passa à esfera "
     "federal, agora sem empréstimos externos. " + F),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Crise da Economia Cafeeira e Deslocamento do Centro Dinâmico",
        "Economia - Crise da Economia Cafeeira e Deslocamento do Centro Dinâmico.apkg",
        CAFE,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
