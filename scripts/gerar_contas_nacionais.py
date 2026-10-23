#!/usr/bin/env python3
"""Gera deck Anki — Economia: Contas Nacionais.

Itens do edital: 2.1 Contabilidade Nacional; 2.2 Contas externas.

Fontes:
  - Anotações: Macro - Contas Nacionais.md
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


CONTAS_NACIONAIS = [

    ("Num país cujo investimento doméstico supera a poupança nacional, a "
     "diferença é financiada com poupança externa, o que se traduz em "
     "investimento externo líquido negativo, em entrada líquida de "
     "capitais e em exportações líquidas positivas.",
     "<b>ERRADO.</b> Quando a poupança é menor que o investimento, o país "
     "<b>importa poupança</b>: o IEL é negativo (ativos estrangeiros "
     "entram), mas, como IEL e exportações líquidas são iguais por "
     "identidade contábil, as exportações líquidas também são "
     "<b>negativas</b> (importa mais do que exporta). [Anotações da aula]"),

    ("Se uma empresa brasileira importa máquinas e as paga com ativos que "
     "passam a pertencer a estrangeiros, as exportações líquidas e o "
     "investimento externo líquido do país diminuem na mesma medida, pois "
     "a igualdade entre ambos decorre da contabilidade das transações, "
     "não de um ajuste de mercado.",
     "<b>CERTO.</b> Toda transação que afeta um lado da igualdade afeta o "
     "outro pelo mesmo montante. O Brasil recebe o bem (menos exportações "
     "líquidas) e entrega ativos ao exterior (menos IEL, isto é, entrada "
     "líquida de capital). [Anotações da aula]"),

    ("O Sistema de Contas Nacionais limita-se a medir o PIB do país, "
     "deixando para outros instrumentos o registro da distribuição e do "
     "uso da renda, da acumulação de capital e das relações com o "
     "exterior.",
     "<b>ERRADO.</b> O SCN (padrão ONU, seguido pelo Brasil) informa a "
     "<b>geração, distribuição e uso da renda</b>, a <b>acumulação de "
     "capital</b> e as relações com o exterior. Sua Tabela de Recursos e "
     "Usos, produzida pelo IBGE, também mostra a capacidade ou necessidade "
     "de financiamento e as transações correntes. [Anotações da aula]"),

    ("Na conta de produção, o consumo intermediário é deduzido da "
     "produção para chegar ao PIB a custo de fatores; para obter o PIB a "
     "preços de mercado, somam-se os subsídios e subtraem-se os impostos "
     "sobre produtos.",
     "<b>ERRADO.</b> A primeira parte está correta. Mas, do custo de "
     "fatores para preços de mercado, <b>somam-se os impostos e "
     "subtraem-se os subsídios</b> sobre produtos: os impostos elevam o "
     "preço pago pelo comprador; os subsídios o reduzem. [Anotações da "
     "aula]"),

    ("Um país cujos residentes enviam ao exterior mais renda de capital "
     "e de trabalho do que recebem de fora terá renda nacional bruta "
     "inferior ao seu PIB.",
     "<b>CERTO.</b> A RNB é o PIB acrescido das rendas recebidas do "
     "exterior menos as enviadas. Se a renda líquida recebida do exterior "
     "é negativa, a RNB fica abaixo do PIB (produção no território não "
     "equivale à renda dos residentes). [Anotações da aula]"),

    ("Na distribuição secundária da renda, a renda disponível bruta resulta "
     "da renda nacional bruta acrescida das transferências correntes "
     "líquidas, como as remessas de brasileiros que vivem no exterior e "
     "o dinheiro enviado ao exterior por imigrantes que trabalham no "
     "Brasil; já a poupança bruta é o que resta da RDB após o consumo "
     "final de famílias e governo.",
     "<b>CERTO.</b> Distribuição primária (mercado) → RNB. Distribuição "
     "secundária (transferências correntes) → RDB. Uso da renda: RDB menos "
     "consumo final = poupança bruta. Por isso a poupança do SCN parte da "
     "RDB, não do PIB. [Anotações da aula]"),

    ("Como a poupança do Sistema de Contas Nacionais é calculada a partir "
     "da renda disponível bruta, e não do PIB, a diferença entre poupança "
     "e investimento corresponde ao saldo em transações correntes, e não "
     "às exportações líquidas da identidade contábil usual.",
     "<b>CERTO.</b> No SCN, poupança menos investimento equivale às "
     "transações correntes, que incorporam rendas e transferências do "
     "exterior. Na identidade contábil, partindo do PIB, a diferença é "
     "igual às exportações líquidas. As \"poupanças\" são calculadas de "
     "modo diferente. [Anotações da aula]"),

    ("A compra, por um residente, de uma marca ou patente de uma empresa "
     "estrangeira é registrada como transferência de renda corrente, "
     "compondo o saldo em transações correntes.",
     "<b>ERRADO.</b> A venda de bens <b>intangíveis</b> (marcas, patentes) "
     "é uma <b>transferência de capital</b>, registrada na conta capital: "
     "não é envio de renda nem venda de bens e serviços. Entra como "
     "capital tanto para o vendedor quanto para o comprador. [Anotações "
     "da aula]"),

    ("Um país com poupança inferior ao investimento e sem transferências "
     "de capital apresenta necessidade líquida de financiamento, que "
     "coincide com um saldo negativo em transações correntes.",
     "<b>CERTO.</b> A capacidade ou necessidade de financiamento mede o "
     "que falta ou sobra da poupança, somada à conta capital, em relação "
     "ao investimento. Sem transferências de capital, ela é igual ao saldo "
     "em transações correntes (negativo = poupança menor que investimento). "
     "[Anotações da aula]"),

    ("Na conta de transações correntes do resto do mundo com a economia "
     "nacional, as importações são tratadas como usos e as exportações "
     "como recursos, de modo coerente com a ótica da economia nacional "
     "em que exportação é positiva e importação, negativa.",
     "<b>ERRADO.</b> A ótica é <b>inversa</b>: exportações entram como "
     "<b>usos</b> e importações como <b>recursos</b> (importar significa "
     "haver mais a consumir). O resultado é o saldo externo de bens e "
     "serviços. [Anotações da aula]"),

    ("O saldo em transações correntes reúne a balança comercial, a "
     "balança de serviços, a balança de rendas e as transferências "
     "unilaterais correntes, não abrangendo as transferências de capital "
     "nem os fluxos financeiros.",
     "<b>CERTO.</b> TC = balança comercial + serviços + rendas + "
     "transferências unilaterais correntes. Transferências de capital "
     "(saldo da conta capital) e transações financeiras ficam em outras "
     "contas do balanço de pagamentos. [Anotações da aula]"),

    ("Numa economia fechada, a poupança iguala o investimento; ao se abrir, "
     "a economia que poupa mais do que investe exporta o excedente, o que "
     "se registra como saída líquida de capitais, de modo que o mesmo "
     "volume de produto pode ser medido pelas óticas do produto, da renda "
     "ou do dispêndio.",
     "<b>CERTO.</b> No fluxo circular, produto, renda e dispêndio se "
     "equivalem, e o PIB pode ser medido por qualquer ótica. Em economia "
     "aberta a poupança excedente (S > I) corresponde a IEL positivo, "
     "isto é, capital saindo do país. [Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Macro - Contas Nacionais",
        "Economia - Macro - Contas Nacionais.apkg",
        CONTAS_NACIONAIS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
