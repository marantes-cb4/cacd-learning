#!/usr/bin/env python3
"""Gera deck Anki — Economia: A Política Econômica na República Velha (1889-1930).

Itens do edital: 4.2 Primeira República.

Fontes:
  - Anotações: A Política Econômica na República Velha (1889-1930).md
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


REPUBLICA_VELHA = [

    ('O padrão-ouro funcionava como estabilizador automático para uma economia agroexportadora como a brasileira: em déficit no balanço de pagamentos, a perda de reservas contraía a moeda e restabelecia o equilíbrio sem aprofundar a recessão.',
     '<b>ERRADO.</b> Embora garantisse estabilidade de preços, o padrão-ouro era <b>pró-cíclico</b>: déficit → perda de reservas → contração monetária, o que piorava os momentos ruins (e melhorava os bons). Gerava rigidez excessiva, perda de autonomia monetária e dependência extrema do setor externo (no Brasil, do café). [Anotações da aula]'),

    ("No vocabulário monetário do século XIX, 'desvalorizar' a moeda significava deixar a taxa de câmbio flutuar para baixo no mercado, sem alterar o conteúdo de ouro legalmente associado ao mil-réis.",
     '<b>ERRADO.</b> A <b>desvalorização</b> era a redução do teor de ouro de cada moeda (menos ouro por papel-moeda), vista como confisco, num mundo em que o padrão-ouro era pilar da civilização. A queda cambial de mercado era <b>depreciação</b>. A banca explora a troca entre os dois termos. [Anotações da aula]'),

    ('Na disputa entre metalistas e papelistas, a tese de que a oferta de moeda deve acompanhar a demanda, sem efeito inflacionário (real bills doctrine), era sustentada por um corpo doutrinário sólido de matriz ricardiana, ao passo que o argumento metalista era meramente intuitivo.',
     '<b>ERRADO.</b> Inverte os campos. Os <b>papelistas</b> ("homens práticos", comerciantes e banqueiros) defendiam ampliar a moeda diante da demanda crescente do trabalho assalariado, com argumento <b>intuitivo e doutrinariamente pobre</b>. Os <b>metalistas</b> é que se apoiavam em David Ricardo, propondo superávit fiscal para resgatar e queimar o excesso de papel-moeda. [Anotações da aula]'),

    ('A lei bancária de Rui Barbosa (1890) manteve a paridade de 1846 e o lastro em ouro, limitando-se a multiplicar o número de bancos habilitados a emitir moeda conversível.',
     '<b>ERRADO.</b> A lei criou emissões <b>inconversíveis</b>, lastreadas em <b>dívida pública</b> (sistema norte-americano), configurando moeda fiduciária pura e câmbio flutuante sem compromisso com a paridade de 1846. O total autorizado era cerca de 2,5 vezes o papel-moeda existente, e as autorizações foram depois ampliadas (dobro e triplo do lastro em ouro, sem conversibilidade). [Anotações da aula]'),

    ('O Encilhamento pode ser explicado como boom de empreendimentos viáveis, favorecido pela facilidade de abertura de sociedades anônimas, cujo desfecho em 1891 decorreu exclusivamente do choque externo, sem relação com a expansão monetária.',
     '<b>ERRADO.</b> Houve bolha: algumas empresas eram viáveis, mas muitas eram <b>fantasmas</b> criadas para lucrar na bolsa, e a especulação só foi possível pela <b>forte expansão monetária</b> das emissões sem lastro. A crise cambial de 1891 foi uma "tempestade perfeita": crise política, especulação na bolsa e choque externo. [Anotações da aula]'),

    ('A crise da Baring Brothers, originada em empréstimo malsucedido à Argentina e seguida de socorro do Banco da Inglaterra, reduziu bruscamente a entrada de capitais no Brasil, combinando choque financeiro internacional com fragilidades internas da política monetária e da bolsa.',
     '<b>CERTO.</b> A Baring é o canal externo da crise de 1890–91: sem capitais, o câmbio não se sustentou. A banca costuma pedir a combinação de causas externas e internas, e não uma causa isolada. Rui Barbosa deixou a Fazenda em 1891. [Anotações da aula]'),

    ('Entre 1889 e 1894, a expansão monetária do período Deodoro–Floriano foi acompanhada de inflação de cerca de 20% ao ano e de depreciação cambial de ordem moderada, com o mil-réis recuando de 27 para cerca de 25 pence.',
     '<b>ERRADO.</b> A depreciação foi <b>forte</b>: de 27 para cerca de <b>11,5 pence</b> por mil-réis, com moeda multiplicada por 3,5 e inflação de 20% a.a. O desalento resultante levou Floriano a deixar o mandato. A pegadinha é manter o número da inflação correto e adulterar a magnitude do câmbio. [Anotações da aula]'),

    ('O plano de saneamento bancário de 1896, no governo Prudente de Morais, transferiu ao Tesouro o monopólio da emissão, mas o objetivo de plena conversibilidade não foi alcançado, em parte porque os bancos carregavam carteiras comprometidas por créditos a empresas fantasmas.',
     '<b>CERTO.</b> A encampação substituiu as emissões bancárias por papel-moeda do Tesouro. A meta (unificação da moeda e conversibilidade plena) falhou por: bancos com deficiências patrimoniais, despesas da guerra de Canudos e queda do preço do café. O câmbio ficou abaixo de 10 pence. [Anotações da aula]'),

    ('No funding loan do governo Campos Salles, a suspensão de juros e amortizações teve como única contrapartida a hipoteca das receitas da alfândega do Rio de Janeiro, sem condicionar a política fiscal e monetária interna.',
     '<b>ERRADO.</b> Além da <b>hipoteca da alfândega do RJ</b>, exigiu-se <b>severo ajuste fiscal e monetário</b>, executado por Murtinho. Foi a contrapartida que moldou a política econômica do período: aumento de arrecadação, queda do consumo público (44%) e do investimento (2/3). [Anotações da aula]'),

    ('A criação do imposto de consumo no início do século XX respondeu à necessidade de ampliar a arrecadação quando a principal fonte, os tributos sobre importados, perdeu força com o avanço da indústria nacional e o encarecimento dos produtos externos; foi o primeiro tributo sobre a circulação de produtos nacionais.',
     '<b>CERTO.</b> Até então a receita dependia de impostos de importação; com indústria nacional crescendo e importados mais caros, passou-se a taxar produtos como fumo, bebidas e calçados (10%). Integra o saneamento fiscal da era Campos Salles/Murtinho. [Anotações da aula]'),

    ('A melhora da situação externa no governo Rodrigues Alves (1902–1906) é explicada pela exportação de borracha e pela entrada de capitais, fatores desvinculados do ajuste ortodoxo do governo anterior, que teria sido irrelevante para o retorno de empréstimos e investimentos estrangeiros.',
     '<b>ERRADO.</b> A volta de empréstimos e investimentos externos só foi possível <b>por causa da política ortodoxa de Campos Salles</b>, que restabeleceu a credibilidade. A estabilidade permitiu obras públicas (reforma do Rio, portos, ferrovias) e a apreciação cambial. A borracha foi o outro motor externo. [Anotações da aula]'),

    ('A Caixa de Conversão (1906) assegurava a manutenção da paridade fixa em qualquer circunstância: em déficit no balanço de pagamentos, a troca de notas por ouro era sustentada indefinidamente por empréstimos externos.',
     '<b>ERRADO.</b> Em superávit, o ouro entrava, emitiam-se notas conversíveis e evitava-se a valorização; em déficit, trocavam-se notas por ouro, contraindo a moeda <b>até o esgotamento das reservas</b>, quando o país passava automaticamente ao câmbio flutuante com desvalorização. Era adesão ao ouro com <b>mecanismo automático de saída</b>. [Anotações da aula]'),

    ('A combinação entre o Convênio de Taubaté e a Caixa de Conversão tinha efeito contracíclico, pois sustentar o preço do café e manter o câmbio competitivo atenuava a superprodução cafeeira.',
     '<b>ERRADO.</b> Ambos eram <b>pró-cíclicos</b> e agravavam a superprodução: o governo comprava mesmo sem demanda externa (preço estabilizado) e o câmbio baixo mantinha alto o poder de compra do cafeicultor. Eram estímulo à oferta justamente na fonte do problema. [Anotações da aula]'),

    ('A contração monetária e a recessão profunda de 1913 decorreram da eclosão da Primeira Guerra Mundial, que impediu a manutenção da Caixa de Conversão.',
     '<b>ERRADO.</b> A recessão veio <b>antes da guerra</b>: com déficit no BP (antitruste dos EUA contra o café, queda da borracha, empréstimos difíceis), as pessoas trocavam papel por ouro e o governo recolhia notas para manter o padrão-ouro. A guerra frustrou novo empréstimo e levou ao fechamento da Caixa, feriado bancário (evitar <i>bank run</i>) e segundo funding loan. [Anotações da aula]'),

    ('Diante do colapso do crédito externo e da queda do preço do café em 1929, o governo federal da Velha República abandonou prontamente o padrão-ouro para sustentar a renda interna, extinguindo a Caixa de Estabilização antes da Revolução de 1930.',
     '<b>ERRADO.</b> O governo <b>insistiu no padrão-ouro</b>, esperando empréstimos de estabilização, o que aprofundou a contração monetária e a recessão (fim da Velha República). A Caixa de Estabilização foi extinta só <b>após</b> a vitória de Vargas, em 1930; em 1931 veio o 3º funding loan. A revelação foi a insustentabilidade do ouro e da defesa do café diante da reversão externa. [Anotações da aula]'),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::A Política Econômica na República Velha (1889-1930)",
        "Economia - A Política Econômica na República Velha (1889-1930).apkg",
        REPUBLICA_VELHA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
