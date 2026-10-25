#!/usr/bin/env python3
"""Gera deck Anki — Economia: Balança de Pagamentos.

Item do edital: 2.2 Contas externas.

Fontes:
  - Anotações: Macro - Balança de Pagamentos.md
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


BALANCA_PAGAMENTOS = [

    ("Uma transação entre uma montadora de capital estrangeiro instalada "
     "no Brasil, há décadas, e um fornecedor brasileiro residente é "
     "registrada na balança de pagamentos do Brasil, por envolver agente "
     "de nacionalidade estrangeira.",
     "<b>ERRADO.</b> O critério é a <b>residência</b>, não a nacionalidade: "
     "só se registra a operação entre <b>residentes e não residentes</b>. "
     "A montadora estrangeira instalada de forma permanente no Brasil é "
     "residente; logo, a transação entre ela e o fornecedor nacional não "
     "entra na BP. [Anotações da aula]"),

    ("Quando uma empresa brasileira exporta mercadorias, a receita "
     "registrada em transações correntes é acompanhada de um lançamento "
     "de contrapartida na conta financeira, em razão do princípio das "
     "partidas dobradas adotado pelo BPM6.",
     "<b>CERTO.</b> Toda operação tem duplo registro: a exportação gera "
     "um crédito em transações correntes e uma variação de ativo na conta "
     "financeira (exportação de 100 = crédito de 100 e débito de 100 em "
     "ativo financeiro). [Anotações da aula]"),

    ("Na balança comercial, as importações são contabilizadas pelo valor "
     "CIF, razão pela qual os gastos com frete e seguro internacional "
     "integram esse saldo e não aparecem na balança de serviços.",
     "<b>ERRADO.</b> A balança comercial usa o valor <b>FOB</b> (só a "
     "mercadoria). Frete e seguro de transporte são registrados na "
     "<b>balança de serviços</b>. O valor CIF inclui custo, seguro e "
     "frete. [Anotações da aula]"),

    ("Um residente que adquire ações de uma empresa estrangeira e passa a "
     "receber dividendos tem tanto a compra das ações quanto os "
     "dividendos registrados na conta financeira da balança de "
     "pagamentos.",
     "<b>ERRADO.</b> A compra das ações é um investimento em carteira, "
     "registrado na <b>conta financeira</b> (aumento de ativo). Os "
     "dividendos são <b>renda do capital</b>, ou seja, renda primária em "
     "transações correntes, e derivam do investimento registrado na conta "
     "financeira. [Anotações da aula]"),

    ("O salário pago por uma empresa estrangeira a um trabalhador "
     "residente no Brasil é uma renda secundária, ao passo que o dinheiro "
     "que um brasileiro que trabalha nos EUA envia à família é renda "
     "primária do trabalho.",
     "<b>ERRADO.</b> Estão trocadas. O salário é <b>renda primária</b> "
     "(remuneração do trabalho). O dinheiro enviado à família é "
     "transferência sem contrapartida, ou seja, <b>renda secundária</b> "
     "(transferência unilateral corrente). [Anotações da aula]"),

    ("Um saldo negativo em transações correntes sinaliza, por si só, "
     "deterioração da posição externa do país, devendo ser sempre "
     "corrigido, já que nenhum déficit contribui para ampliar a "
     "capacidade produtiva.",
     "<b>ERRADO.</b> Resultado negativo <b>não é necessariamente mau "
     "sinal</b>: em país em desenvolvimento pode refletir ampliação do "
     "estoque de capital. Torna-se preocupante se indica que os "
     "residentes compram muito do exterior sem que os não residentes "
     "comprem produtos nacionais, e, se persistir, pode gerar crises por "
     "desequilíbrio da BP. [Anotações da aula]"),

    ("A aquisição definitiva de uma marca ou patente de um não residente "
     "é registrada como despesa na conta capital, ao passo que os "
     "royalties pagos pelo uso de propriedade intelectual aparecem na "
     "balança de serviços.",
     "<b>CERTO.</b> A conta capital registra aquisições e cessões de "
     "ativos não financeiros não produzidos (patentes, marcas, direitos "
     "autorais, recursos naturais): aquisição = despesa, cessão = receita. "
     "Já royalties são serviços, em transações correntes. [Anotações da "
     "aula]"),

    ("Quando um investidor estrangeiro compra ações na B3, aumenta o "
     "ativo externo do Brasil; quando o mesmo investidor vende essas "
     "ações, a conta financeira registra a operação com sinal negativo.",
     "<b>ERRADO</b> na primeira parte. A compra de ações brasileiras por "
     "não residente eleva o <b>passivo</b> do país (sinal positivo). A "
     "venda é registrada com sinal negativo, seja de ativo ou de passivo. "
     "Ativo é a aquisição de investimento por residente no exterior. "
     "[Anotações da aula]"),

    ("Uma empresa residente celebra contrato futuro de venda de dólares "
     "com contraparte no exterior; a balança de pagamentos registra o "
     "valor nocional do contrato no momento da celebração, e não o "
     "resultado financeiro da liquidação.",
     "<b>ERRADO.</b> Nos derivativos, a BP registra <b>apenas as "
     "liquidações</b>: os ganhos e perdas efetivos. Ganhos e perdas de "
     "residentes em mercados estrangeiros são ativos; os de não "
     "residentes em mercados nacionais, passivos. [Anotações da aula]"),

    ("Quando um importador residente antecipa o pagamento de uma "
     "importação, aumenta o passivo externo do país, e quando um "
     "exportador recebe adiantamento por exportação futura, aumenta o "
     "ativo externo.",
     "<b>ERRADO.</b> Está invertido. Importador que <b>adianta</b> "
     "pagamento eleva o <b>ativo</b> (reduzido quando recebe a "
     "mercadoria). Exportador que <b>recebe adiantamento</b> aumenta o "
     "<b>passivo</b> (reduzido quando entrega). Parcelamento: exportador "
     "eleva o ativo; importador, o passivo. [Anotações da aula]"),

    ("Os ativos de reserva sob controle do Banco Central abrangem apenas "
     "moeda estrangeira em espécie, sendo os títulos de alta liquidez, "
     "o ouro e os direitos especiais de saque contabilizados em outros "
     "investimentos.",
     "<b>ERRADO.</b> Ativos de reserva incluem moeda estrangeira "
     "(inclusive <b>títulos de alta liquidez</b>), reservas e <b>direitos "
     "especiais de saque</b> junto ao FMI, <b>ouro</b> e outros ativos "
     "líquidos em moeda estrangeira. Quando o BC compra moeda estrangeira, "
     "registra-se sinal positivo. [Anotações da aula]"),

    ("Como a conta financeira, que inclui os ativos de reserva, acomoda "
     "o resultado das transações correntes e da conta capital, uma "
     "diferença residual que impeça o fechamento da balança é lançada em "
     "erros e omissões, indicando falhas ou lacunas de registro.",
     "<b>CERTO.</b> Erros e omissões é o <b>valor de chegada</b>: o que "
     "sobra para fechar a conta quando a conta financeira não coincide "
     "com transações correntes mais conta capital. Reservas positivas "
     "acompanham BP superavitária; negativas, BP deficitária. "
     "[Anotações da aula]"),

    ("Na passagem do PIB para a renda nacional bruta incorpora-se a renda "
     "primária líquida do balanço de pagamentos, e na passagem da renda "
     "nacional bruta para a renda disponível bruta incorpora-se a renda "
     "secundária, de modo que a poupança doméstica do SCN depende "
     "dessas contas externas.",
     "<b>CERTO.</b> A renda líquida recebida do exterior (RLRE) "
     "corresponde à <b>renda primária</b> da BP, e as transações "
     "unilaterais correntes à <b>renda secundária</b>. Da RDB, deduzido o "
     "consumo, sai a poupança bruta doméstica, que, menos o "
     "investimento, é o saldo em transações correntes. [Anotações da "
     "aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Macro - Balança de Pagamentos",
        "Economia - Macro - Balança de Pagamentos.apkg",
        BALANCA_PAGAMENTOS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
