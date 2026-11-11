#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Julho/2026).

Tema: Contratos Administrativos (Item 10 do Edital CACD).

Fontes:
  - Anotações: Contratos Administrativos.md
  - Material do professor: Direito Interno_Rodada 01_Julho_2026_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Julho_2026.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/direito interno"
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

CONTRATOS = [

    ('No que concerne às licitações e aos contratos administrativos no ordenamento jurídico brasileiro, julgue: Na formalização dos contratos administrativos, deve-se observar, como regra geral, a edição de cláusula que declare competente o foro da sede da administração envolvida no contrato a ser celebrado, para dirimir qualquer questão contratual.',
     '<b>CERTO.</b> Art. 92, §1º, Lei 14.133/2021: a regra é o <b>foro da sede da Administração</b>, mesmo para contratados domiciliados no exterior (reflexo do desequilíbrio). Só há 3 exceções, ligadas a relações internacionais: licitação internacional paga com recursos de organismo internacional do qual o Brasil é parte, compra de equipamentos fabricados e entregues no exterior (com autorização do chefe do Executivo) e aquisições de unidades com sede no exterior (embaixadas e consulados). [Anotações da aula; Rodada 01 Jul/2026]'),

    ('No que concerne às licitações e aos contratos administrativos, julgue: O contrato administrativo é sempre consensual e, em regra, formal, oneroso e comutativo, mas não é personalíssimo.',
     '<b>ERRADO.</b> O contrato administrativo <b>é personalíssimo</b> (<i>intuitu personae</i>): o licitante vencedor deve executá-lo, e a cessão da posição contratual a terceiro é vedada fora das hipóteses legais (ex.: subcontratação parcial autorizada). Também é bilateral, comutativo, de formalismo moderado, instável e marcado pelo desequilíbrio das cláusulas exorbitantes. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('No que concerne às licitações e aos contratos administrativos, julgue: O reequilíbrio econômico-financeiro poderá ser concedido de forma automática sempre que houver aumento de custos do contratado comprovado por índices oficiais adotados pela administração pública para orientar sua execução orçamentária.',
     '<b>ERRADO.</b> O reequilíbrio exige <b>fato superveniente e imprevisível</b> que altere as condições iniciais e depende de <b>acordo</b> entre as partes (art. 104, §§1º e 2º): as cláusulas econômico-financeiras não se alteram unilateralmente. Não é cláusula exorbitante; é <b>direito do contratado</b> e dever da Administração. Aumento de custo medido por índice não gera reequilíbrio automático. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Acerca das licitações e dos contratos administrativos, considerando-se o disposto na Lei nº 14.133/2021, julgue: O contrato de uma obra de reforma de um edifício público poderá ser alterado tanto quantitativa quanto qualitativamente, de forma unilateral, pela administração pública, desde que as alterações não transfigurem o objeto da contratação e observem o limite de acréscimos e supressões de 50% do valor contratado atualizado.',
     '<b>ERRADO.</b> O limite de <b>50%</b> vale para reforma de edifício ou equipamento, mas <b>somente para acréscimos</b>: nesse tipo de contrato <b>não se admite supressão</b> unilateral. Nos demais contratos (obras, serviços e compras), o limite é de <b>25%</b>, para mais ou para menos (art. 125). A pegadinha troca "somente acréscimos" por "acréscimos e supressões". [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Acerca das licitações e dos contratos administrativos, julgue: Se tributo for criado após a assinatura do contrato administrativo e isso tiver repercussão no valor da execução do objeto, o contratante não terá direito à alteração unilateral do contrato.',
     '<b>CERTO.</b> A criação de tributo posterior é <b>fato do príncipe</b>: alteração superveniente e imprevisível decorrente de decisão do Estado, que exige <b>reequilíbrio por acordo</b> (art. 124, II, "d"), e não alteração unilateral pela Administração. Aqui, a Administração não pode usar cláusula exorbitante. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Acerca das licitações e dos contratos administrativos, julgue: As questões relacionadas ao restabelecimento do equilíbrio econômico-financeiro do contrato não poderão ser objeto de cláusula contratual que preveja a conciliação como meio alternativo de resolução da controvérsia, por tratar de fatos imprevisíveis ou de fatos previsíveis de consequências incalculáveis.',
     '<b>ERRADO.</b> O art. 151, parágrafo único, admite meios alternativos (mediação, conciliação, comitê de disputas, arbitragem) para <b>direitos patrimoniais disponíveis</b>, expressamente incluindo o <b>restabelecimento do equilíbrio econômico-financeiro</b>, o inadimplemento e o cálculo de indenizações. Como o reequilíbrio exige acordo, os meios alternativos ajudam a obtê-lo. Eles não são cláusula obrigatória. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Sobre os contratos administrativos, julgue: As sanções administrativas aplicáveis ao responsável por infrações em licitações e contratos incluem advertência, multa, suspensão dos direitos políticos, impedimento de licitar, declaração de inidoneidade.',
     '<b>ERRADO.</b> O art. 156 prevê <b>4 sanções</b>: advertência, multa, impedimento de licitar e contratar e declaração de inidoneidade. Suspensão de direitos políticos não é sanção da lei de licitações. São aplicadas em processo administrativo, com contraditório e ampla defesa, <b>sem intervenção do Judiciário</b>, e a aplicação é poder-dever. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Sobre os contratos administrativos, julgue: A aplicação da pena de multa não tem caráter substitutivo em relação à obrigação de reparação integral do dano causado à administração pública.',
     '<b>CERTO.</b> Art. 156, §9º: qualquer sanção administrativa <b>não exclui a reparação integral do dano</b>. A multa é sanção administrativa; a reparação tem natureza civil. Podem coexistir, e uma não substitui a outra. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Sobre os contratos administrativos, julgue: Não há responsabilidade solidária entre o contratado e a administração pública em relação aos encargos trabalhistas, fiscais e comerciais resultantes da execução do contrato.',
     '<b>CERTO.</b> Regra do art. 121: esses encargos recaem <b>só sobre o contratado</b>. Mesmo na terceirização com dedicação exclusiva, a solidariedade alcança apenas os <b>previdenciários</b>; quanto aos <b>trabalhistas</b>, a responsabilidade é <b>subsidiária</b> e depende de falha na fiscalização. Para fiscais e comerciais não há responsabilidade da Administração. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Sobre os contratos administrativos, julgue: Na contratação de serviços contínuos com dedicação exclusiva de mão de obra, é permitido o compartilhamento simultâneo de recursos materiais disponíveis com outros contratos.',
     '<b>ERRADO.</b> O art. 6º, XVI exige empregados à disposição da Administração <b>em suas dependências</b> e <b>veda o compartilhamento</b> de recursos humanos <b>e materiais</b> da empresa com outros contratos administrativos. Justifica-se porque o terceirizado deve se fixar no órgão e conhecer sua rotina. É esse perfil que atrai a responsabilidade solidária (previdenciária) e subsidiária (trabalhista). [Anotações da aula; Rodada 01 Jul/2026]'),

    ('Havendo matriz de risco no contrato administrativo, a ocorrência do risco nela alocado não autoriza pedido de reequilíbrio, salvo em duas situações: quando a Administração determinar alterações unilaterais e quando legislação superveniente aumentar ou reduzir tributos diretamente pagos pelo contratado em razão do contrato.',
     '<b>CERTO.</b> Art. 103, §5º: a matriz de risco (cláusula <b>facultativa</b>) é <b>renúncia</b> ao reequilíbrio quanto aos riscos que alocou (ex.: custos adicionais por sítio arqueológico atribuídos ao contratado). As exceções são as alterações unilaterais do art. 124, I, e as variações tributárias por lei superveniente. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('As cláusulas exorbitantes só podem ser exercidas pela Administração quando previstas expressamente no contrato ou no edital, pois, se o contratado não as conheceu na proposta, sua aplicação violaria a comutatividade do contrato administrativo.',
     '<b>ERRADO.</b> Elas estão <b>na lei</b> (art. 104) e valem independentemente de previsão contratual ou editalícia; o contratado as conhece desde a proposta, por isso <b>não ferem a comutatividade</b>. Exigem decisão motivada, contraditório e ampla defesa. Ficam de fora: cláusulas econômico-financeiras e monetárias e o reequilíbrio, que dependem de concordância do contratado. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('A Administração pode extinguir unilateralmente o contrato administrativo sempre que verificar descumprimento do contratado previsto em lei, ainda que o inadimplemento decorra de omissão da própria Administração, como a não obtenção de licença ambiental necessária ao início da obra.',
     '<b>ERRADO.</b> A extinção unilateral e escrita (art. 138, I) exige que o descumprimento <b>não tenha sido causado pela Administração</b>. Quando ela deu causa, resta o <b>acordo consensual</b> ou, não havendo acordo, <b>arbitragem</b> (só se houver cláusula compromissória) ou <b>decisão judicial</b>. É cláusula exorbitante, com contraditório e ampla defesa. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('A declaração de inidoneidade para licitar e contratar, a sanção mais grave da Lei 14.133/2021, produz efeitos apenas no ente federado que a aplicou, por prazo máximo de três anos; já o impedimento de licitar tem abrangência nacional, com prazo mínimo de três anos.',
     '<b>ERRADO.</b> Os atributos estão trocados. <b>Impedimento</b>: vale no <b>ente que aplicou</b>, por <b>até 3 anos</b> (sanção da União não impede de contratar com Estado, DF ou Município). <b>Inidoneidade</b>: vale em <b>todos os entes</b>, por <b>3 a 6 anos</b>. [Anotações da aula; Rodada 01 Jul/2026]'),

    ('A alteração unilateral que a Administração impõe ao contratado para substituir material por outro tecnicamente mais adequado dispensa o contratado de aceitá-la caso lhe seja desfavorável, devendo a Administração obter seu consentimento prévio, pois a medida altera aspecto econômico-financeiro do contrato.',
     '<b>ERRADO.</b> A alteração <b>qualitativa</b> (projeto ou especificações) é a 1ª cláusula exorbitante (art. 124): o contratado é <b>obrigado a aceitar</b>, sob pena de inadimplemento, e a Administração paga o insumo ou a diferença. O que exige consentimento são as cláusulas econômico-financeiras e o reequilíbrio (art. 104, §§1º e 2º). Daí a distinção entre alterar o objeto e alterar a equação financeira. [Anotações da aula; Rodada 01 Jul/2026]'),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Contratos Administrativos",
        "Direito Interno - Contratos Administrativos.apkg",
        CONTRATOS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
