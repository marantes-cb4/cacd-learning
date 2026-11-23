#!/usr/bin/env python3
"""Gera deck Anki — Economia: Governo JK e Plano de Metas (1956-1960).

Itens do edital: 4.4 Década de 1950 (SALTE, Plano de Metas).

Fontes:
  - Anotações: Governo JK e Plano de Metas (1956-1960).md
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

    ('O Plano de Metas apoiou-se em diagnósticos produzidos no segundo governo Vargas, como os da CEPAL-BNDE e da Comissão Mista Brasil-Estados Unidos, e a construção de Brasília, embora fosse sua meta mais simbólica, não estava orçada no plano.',
     '<b>CERTO.</b> O Conselho de Desenvolvimento, criado por JK no início de 1956, elaborou o plano a partir desses diagnósticos, que apontavam gargalos e áreas-chave de investimento. As cinco áreas principais eram energia, transporte, alimentação, indústria de base e educação; Brasília ficou fora do orçamento. A armadilha é tratá-la como 6ª meta orçada. [Anotações da aula]'),

    ('Segundo Lessa, o Plano de Metas combinou tratamento especial ao capital estrangeiro, financiamento dos gastos por expansão dos meios de pagamento e do crédito, ampliação da participação pública na formação bruta de capital e estímulo à iniciativa privada, sem que nenhum desses pontos gerasse pressão inflacionária relevante.',
     '<b>ERRADO.</b> Os quatro pontos básicos de Lessa estão corretos, mas o financiamento via <b>expansão dos meios de pagamento e do crédito</b> provocou <b>forte pressão inflacionária</b>. O estímulo privado se deu por reserva de mercado (lei do similar nacional), câmbio preferencial para bens de capital em setores especiais e crédito subsidiado do BNDE e do BB. [Anotações da aula]'),

    ('O Plano de Metas visava à industrialização de bens de consumo leves, setor em que a substituição de importações ainda era incipiente, e por isso dedicou a maior parte dos recursos a esse segmento.',
     '<b>ERRADO.</b> Os bens de consumo leves já tinham sido industrializados nas fases anteriores. O objetivo era construir os <b>estágios superiores da pirâmide industrial</b>: acelerar a substituição de bens <b>intermediários e de capital</b> e dos duráveis (mais complexos), integrando a estrutura industrial. Também buscava a infraestrutura básica e eliminar pontos de estrangulamento. [Anotações da aula]'),

    ('Ponto de estrangulamento, ponto de germinação e ponto de estrangulamento externo designam, no Plano de Metas, respectivamente: áreas de demanda insatisfeita por desequilíbrio do desenvolvimento; áreas que geram demanda derivada para outras indústrias; e áreas de grande peso na pauta de importações.',
     '<b>CERTO.</b> Energia e transporte recebiam a maior parte dos investimentos por serem pontos de estrangulamento. A indústria automobilística é exemplo de ponto de germinação (demanda por peças, borracha etc.). O estrangulamento externo refere-se a produtos quase inteiramente importados. A banca costuma trocar as definições entre si. [Anotações da aula]'),

    ('No investimento planejado do Plano de Metas, energia e transportes concentraram a maior parte dos recursos por serem pontos de germinação, e a origem dos recursos foi majoritariamente privada, com participação residual do setor público.',
     '<b>ERRADO.</b> Energia e transporte lideraram o investimento por serem <b>pontos de estrangulamento</b> (não de germinação). E a origem majoritária foi o <b>setor público</b> (cerca da metade), seguido do privado (cerca de um terço) e das agências internacionais. Alimentação e educação receberam fatias pequenas. [Anotações da aula]'),

    ('A participação do Estado no Plano de Metas restringiu-se à criação de incentivos à iniciativa privada, já que os investimentos diretos em siderurgia, petróleo, minério e energia eram deixados ao setor privado nacional.',
     '<b>ERRADO.</b> O comprometimento do Estado foi total e tinha 3 frentes: <b>investimento direto</b> (siderúrgicas como CSN, Cosipa e Usiminas; Petrobras; Vale do Rio Doce; CHESF e Furnas; RFFSA), <b>incentivos e protecionismo</b> (BNDE e lei do similar nacional) e <b>incentivo ao capital estrangeiro</b>, com endividamento externo crescente. [Anotações da aula]'),

    ('A reforma cambial de 1957 manteve as cinco categorias de leilão de importação da Instrução 70, mas liberou imediatamente as exportações para o câmbio livre.',
     '<b>ERRADO.</b> A reforma <b>simplificou</b> o sistema: restaram duas categorias de leilão (geral, para bens essenciais; específica, para supérfluos) e uma terceira, sem leilão, ao câmbio de custo (petróleo, trigo, papel, fertilizantes). Nas exportações mantiveram-se inicialmente as 4 categorias anteriores, migrando gradualmente ao câmbio livre (Instruções 167 e 192). [Anotações da aula]'),

    ('A Instrução 113 da SUMOC foi editada no governo JK para atrair o capital externo ao Plano de Metas, e o principal beneficiário do mecanismo foi a indústria automobilística, que respondeu por mais da metade do investimento direto estrangeiro entre 1955 e 1960.',
     '<b>ERRADO.</b> A Instrução 113 é <b>anterior</b> ao governo JK, do governo Café Filho (1955), embora tenha sido usada intensamente no período. Permitia importar equipamentos sem cobertura cambial (até 45% mais barato) e a indústria automobilística foi mesmo a grande beneficiária. Ela completou o <b>tripé</b>: capital nacional (consumo não durável), estatais (insumos e infraestrutura) e multinacionais (duráveis). [Anotações da aula]'),

    ('As metas relegadas a plano secundário no Plano de Metas, como agropecuária, educação e saúde, tiveram participação simbólica, e o plano ampliou a concentração de renda pessoal e regional, com foco no Sudeste e no Sul.',
     '<b>CERTO.</b> Eram secundários agropecuária (armazenagem, trigo, mecanização), distribuição de renda, políticas sociais e equilíbrio de preços e balanço de pagamentos. O plano intensificou desequilíbrios já presentes: a renda se concentrou pessoal e regionalmente. Educação, apesar de ser uma das 5 áreas, recebeu fatia pequena. [Anotações da aula]'),

    ('No arranjo monetário da época, o Banco do Brasil emitia o papel-moeda por conta própria, e a cobertura dos déficits do Tesouro com crédito no BB não afetava a base monetária, pois se tratava de moeda escritural.',
     '<b>ERRADO.</b> Como o BB exercia funções de banco central e comercial, qualquer crédito contra ele virava <b>base monetária</b>, e não moeda escritural. Cobrir déficits do Tesouro com crédito no BB significava <b>expansão primária dos meios de pagamento</b> (financiamento inflacionário). O papel-moeda era produzido pela Caixa de Amortização, do Tesouro; a SUMOC cuidava da parte normativa. [Anotações da aula]'),

    ('Os instrumentos tradicionais de política monetária tinham pouca eficácia na época: o open market era quase inexistente porque os títulos do Tesouro eram pouco atrativos diante de juros reais negativos, o compulsório era evitado por ser lento e de grande impacto, e o redesconto era pouco usado pelos grandes bancos.',
     '<b>CERTO.</b> O teto de 12% ao ano (Lei da Usura) com inflação acima disso tornava os juros reais negativos e os títulos desinteressantes. Compulsório: lento e de grande impacto. Redesconto: grandes bancos evitavam recorrer a ele para não manchar a imagem. Por isso o governo tinha dificuldade em conter o crédito. [Anotações da aula]'),

    ('O Programa de Estabilização Monetária, conduzido por Lucas Lopes após a inflação saltar de 7% para 24%, foi bem recebido por estar alinhado ao FMI, o que permitiu sua plena vigência durante o auge do Plano de Metas.',
     "<b>ERRADO.</b> O programa, de viés ortodoxo e associado ao FMI, sofreu <b>rápido desgaste</b> com a classe política e a opinião pública em plena euforia do '50 em 5'. Lucas Lopes foi substituído na Fazenda por Sebastião Paes de Almeida (então presidente do BB), e Roberto Campos deixou o BNDE, dando lugar a Lúcio Meira. O plano <b>nem chegou a vigorar</b>. [Anotações da aula]"),

    ('Entre os resultados do Plano de Metas, houve pequena aceleração do PIB e do crescimento industrial, mas mudanças muito significativas na estrutura produtiva, com duráveis e bens de capital, e a diferenciação industrial foi conduzida diretamente pelo Estado, apesar de deficiências de oferta no fim do período em metalurgia, química básica, borracha e papel.',
     '<b>CERTO.</b> A aceleração do PIB foi pequena porque a taxa já era alta; a mudança estrutural é que foi grande, com instalação de automobilística, construção naval, material elétrico pesado e máquinas. A diferenciação foi toda planejada pelo Estado, nada orgânico. Os duráveis (geladeira, TV) focavam a classe média, sem crédito para as classes C e D. [Anotações da aula]'),

    ('Entre os problemas do Plano de Metas, o sobreinvestimento decorreu de a oferta de bens de capital, insumos e duráveis ter avançado à frente da demanda, gerando capacidade ociosa, agravado pela ausência de crédito ao consumidor para as classes de menor renda.',
     '<b>CERTO.</b> O padrão de financiamento era frágil: sem mercado de capitais de médio e longo prazo (concentrado no BNDE), sistema financeiro pouco desenvolvido, sistema tributário ineficiente e Lei da Usura. Soma-se a inflação por emissão (arranjo SUMOC-BB-Tesouro), rápido endividamento externo e crise do setor externo (termos de troca, balança de serviços de fatores). [Anotações da aula]'),

    ('A crise do setor externo ao final do Plano de Metas decorreu de melhora dos termos de troca com o café e de empréstimos externos de longo prazo de maturação, apesar do crescimento do déficit na balança de serviços de fatores.',
     '<b>ERRADO.</b> Houve novo ciclo de <b>deterioração dos termos de troca</b> (baixa de preços do café) e os empréstimos externos tinham <b>curto</b> período de maturação. O déficit na balança de serviços de fatores (hoje, renda primária) também cresceu. Esses fatores, com o rápido endividamento, sustentaram a crise externa. [Anotações da aula]'),

]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Governo JK e Plano de Metas (1956-1960)",
        "Economia - Governo JK e Plano de Metas (1956-1960).apkg",
        CARDS,
    )
