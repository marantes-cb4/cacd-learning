#!/usr/bin/env python3
"""Gera deck Anki — Economia: Modelo IS-LM (Keynesiano Generalizado).

Modelo de economia fechada (Hicks-Hansen), pré-requisito conceitual do
IS-LM-BP. Toca 3 itens do edital:
  - 2.1 Contabilidade Nacional (ótica keynesiana: multiplicador, função
    consumo, demanda efetiva)
  - 2.5 Teoria da Moeda (teoria da procura de moeda, preferência pela
    liquidez)
  - 2.6 Política Monetária (políticas monetárias não convencionais)

Fontes:
  - Anotações: Modelo IS-LM (Keynesiano Generalizado).md
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


IS_LM_KEYNESIANO = [

    ("O modelo IS-LM foi originalmente formulado pelo próprio John Maynard "
     "Keynes na Teoria Geral do Emprego, do Juro e da Moeda, tendo sido "
     "posteriormente rebatizado de modelo Hicks-Hansen em homenagem aos "
     "economistas que o popularizaram no meio acadêmico.",
     "<b>ERRADO.</b> O modelo foi criado por <b>John Hicks</b> como síntese "
     "matemática das ideias da Teoria Geral — não por Keynes. Foi "
     "posteriormente <b>expandido por Alvin Hansen</b>, passando a ser "
     "chamado de modelo Hicks-Hansen (ou síntese neoclássica). [Anotações "
     "da aula]"),

    ("A política fiscal, ao deslocar a curva IS, afeta simultaneamente o "
     "mercado de bens e o mercado financeiro, razão pela qual seus efeitos "
     "sobre a taxa de juros são diretos e não meramente uma consequência "
     "indireta do ajuste no mercado de bens.",
     "<b>ERRADO.</b> A política fiscal desloca <b>apenas a IS</b>, afetando "
     "diretamente só o mercado de <b>bens</b>. O efeito sobre a taxa de "
     "juros é indireto: o aumento de Y eleva a demanda por moeda que, dada "
     "a oferta de moeda constante, pressiona os juros para cima (efeito "
     "crowding out). [Anotações da aula]"),

    ("Em uma expansão fiscal, o efeito multiplicador e o efeito "
     "crowding-out atuam simultaneamente e em sentidos opostos sobre o "
     "produto, mas o efeito líquido pode ser uma redução do produto caso o "
     "crowding-out seja suficientemente intenso.",
     "<b>ERRADO.</b> No modelo IS-LM padrão (fora dos casos extremos de "
     "elasticidade), o efeito do <b>multiplicador sempre supera</b> o "
     "crowding-out — o resultado líquido de uma expansão fiscal é sempre "
     "IS deslocada à direita, com produto E taxa de juros mais altos. "
     "[Anotações da aula]"),

    ("A principal inovação de Keynes na teoria da demanda por moeda foi "
     "reconhecer, além do motivo transacional já identificado pelos "
     "clássicos, os motivos precaucional e especulativo — este último "
     "ligado à função da moeda como reserva de valor frente à incerteza "
     "sobre o comportamento futuro da taxa de juros.",
     "<b>CERTO.</b> A teoria clássica só reconhecia a demanda "
     "<b>transacional</b>; Keynes acrescenta a <b>precaucional</b> (reserva "
     "para imprevistos) e a <b>especulativa</b> (reserva de valor, baseada "
     "na comparação entre reter moeda ou títulos). [Anotações da aula]"),

    ("Segundo a teoria dos ativos de Keynes, o retorno de um ativo é dado "
     "por a+q-c+l, sendo que a moeda, por não gerar rendimento (q=0) nem "
     "incorrer em custo de carregamento (c=0), possui como único componente "
     "de retorno o prêmio de liquidez (l), atributo que nenhum outro ativo "
     "possui na mesma intensidade.",
     "<b>CERTO.</b> A moeda tem q=0, c=0 e a=0 — seu retorno resume-se ao "
     "prêmio de liquidez (l), atributo exclusivo da moeda. Já títulos "
     "rendem a+q, e ativos reais (sem liquidez, l=0) rendem a+q-c. "
     "[Anotações da aula]"),

    ("Uma expectativa de queda futura da taxa de juros de mercado eleva a "
     "demanda especulativa por títulos e reduz a demanda por moeda, pois o "
     "preço dos títulos — inversamente relacionado à taxa de juros — tende "
     "a subir nesse cenário.",
     "<b>CERTO.</b> Preço do título = Valor de Face/(1+i). Se i deve cair, "
     "o preço do título deve subir — logo, vale a pena comprar títulos "
     "agora (antes da alta de preço), elevando sua demanda e reduzindo a "
     "demanda especulativa por moeda. [Anotações da aula]"),

    ("Na chamada armadilha de liquidez, representada no modelo IS-LM por "
     "uma curva LM horizontal, a política monetária é totalmente ineficaz "
     "para expandir o produto, ao passo que a política fiscal atinge sua "
     "eficácia máxima, já que não há efeito crowding-out nesse cenário.",
     "<b>CERTO.</b> Com LM horizontal, qualquer moeda adicional ofertada é "
     "inteiramente entesourada (política monetária ineficaz), enquanto a "
     "política fiscal não eleva a taxa de juros — sem crowding out, atinge "
     "eficácia máxima. [Anotações da aula]"),

    ("No caso oposto à armadilha de liquidez — uma curva LM totalmente "
     "vertical, refletindo uma demanda por moeda exclusivamente "
     "transacional nos moldes clássicos —, a política fiscal é totalmente "
     "ineficaz para expandir o produto, pois todo o efeito do multiplicador "
     "é anulado pelo crowding-out.",
     "<b>CERTO.</b> Com LM vertical (demanda por moeda dependente só da "
     "renda), uma expansão fiscal desloca a IS mas só eleva a taxa de "
     "juros, sem alterar o produto de equilíbrio — 100% de crowding out. A "
     "política monetária, nesse caso, tem eficácia máxima. [Anotações da "
     "aula]"),

    ("A taxa de juros nominal, no modelo IS-LM, pode assumir valores "
     "negativos sem qualquer limite teórico, tendo em vista que o retorno "
     "de um título é sempre superior ao de reter moeda, independentemente "
     "do nível da taxa de juros de mercado.",
     "<b>ERRADO.</b> Existe o <b>zero lower bound</b>: a taxa nominal não "
     "pode ficar significativamente negativa, pois nesse caso reter moeda "
     "(retorno nulo) supera comprar um título (retorno negativo). "
     "Exceções aparentes (Suíça, Suécia, Japão) ocorrem porque "
     "investidores estrangeiros esperam valorização cambial suficiente "
     "para tornar o retorno total positivo. [Anotações da aula]"),

    ("Dentre as políticas monetárias não convencionais adotadas pelo Fed "
     "após 2008, o afrouxamento quantitativo (quantitative easing) "
     "restringiu-se à compra de títulos públicos, dado que a compra de "
     "títulos privados por um banco central desvirtuaria sua função e não "
     "foi utilizada nas rodadas de QE da crise financeira.",
     "<b>ERRADO.</b> O QE incluiu justamente a compra de <b>títulos "
     "PRIVADOS</b>, com o objetivo de reduzir os spreads elevados em "
     "momentos de turbulência e evitar uma deflação abrupta no preço "
     "desses ativos. [Anotações da aula]"),

    ("A operação conhecida como \"Operation Twist\", lançada pelo Fed em "
     "2011, consistiu na compra simultânea de títulos de curto e longo "
     "prazo em volumes equivalentes, com o objetivo de reduzir "
     "uniformemente toda a estrutura a termo das taxas de juros.",
     "<b>ERRADO.</b> A Operation Twist consistiu em <b>vender</b> títulos "
     "de curto prazo e <b>comprar</b> títulos de longo prazo — não uma "
     "compra simultânea de ambos — visando reduzir especificamente os "
     "juros de <b>longo prazo</b>, mais relevantes para a decisão de "
     "investimento privado. [Anotações da aula]"),

    ("A sinalização de juros futuros (forward guidance) busca combater a "
     "armadilha de liquidez ao reduzir a incerteza dos agentes quanto à "
     "trajetória futura da taxa de juros, por meio do anúncio antecipado de "
     "grandes volumes de compras de ativos.",
     "<b>CERTO.</b> Ao prometer manter os juros baixos por um período "
     "prolongado, o forward guidance reduz a expectativa de alta futura dos "
     "juros que alimenta a retenção especulativa de moeda característica da "
     "armadilha de liquidez. [Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Modelo IS-LM (Keynesiano Generalizado)",
        "Economia - Modelo IS-LM (Keynesiano Generalizado).apkg",
        IS_LM_KEYNESIANO,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
