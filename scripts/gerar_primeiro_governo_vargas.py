#!/usr/bin/env python3
"""Gera deck Anki — Economia: O Primeiro Governo Vargas (1930-1945).

Itens do edital: 4.3 Industrialização 1930–1945 (ISI).

Fontes:
  - Anotações: O Primeiro Governo Vargas (1930-1945).md
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


VARGAS = [

    ('Como a dívida externa brasileira estava denominada em moeda estrangeira, a forte desvalorização do mil-réis em 1930–31 aliviou o ônus do serviço da dívida em termos de moeda nacional, o que reduziu a pressão sobre o governo para decretar moratórias.',
     '<b>ERRADO.</b> A desvalorização <b>encarece</b> a dívida: com o passivo em libras e dólares (65% e 30%), cada unidade a servir custava mais mil-réis. Somada ao esgotamento das reservas (de 31 milhões de libras em 1929 a praticamente zero em 1931), levou às moratórias sucessivas e ao funding loan de 1931. [Anotações da aula]'),

    ('A abolição do monopólio cambial no início do governo provisório refletiu uma opção liberal duradoura, sustentada pela folga de reservas herdada do período anterior, e a liberalização do câmbio permaneceu até meados da década.',
     '<b>ERRADO.</b> O liberalismo inicial foi "retórico e primitivo", logo <b>desmascarado pela realidade</b>: as reservas desabaram e, em 1931, reintroduziu-se o <b>monopólio cambial do Banco do Brasil</b>. A folga de divisas só reapareceu em 1936–37 — e, quando os controles foram relaxados, as reservas foram consumidas de novo. [Anotações da aula]'),

    ('O monopólio cambial reintroduzido em 1931, ao obrigar a venda de cambiais ao Banco do Brasil e priorizar compras do governo, dívida pública e importações essenciais, teve como efeito colateral a proteção da indústria nacional, mantida pelo controle de importações até 1934.',
     '<b>CERTO.</b> Ao racionar divisas, o BB comprimiu importações não essenciais, o que <b>protegeu a indústria</b> sem que essa fosse a finalidade primária (administrar a escassez de reservas). É mais um canal do deslocamento do centro dinâmico para o mercado interno. [Anotações da aula]'),

    ('Pelaez e Dean, ao sustentarem que a política econômica do período foi ortodoxa e que a indústria não foi favorecida, basearam-se nas políticas efetivamente implementadas, razão pela qual a tese de Furtado sobre a política keynesiana avant la lettre foi refutada.',
     '<b>ERRADO.</b> As teses revisionistas se apoiaram nas <b>declarações</b> do governo, e não nas políticas de fato executadas, e foram desmentidas no longo prazo. As evidências posteriores apenas <b>atenuam</b> as conclusões de Furtado (impacto modesto da crise, queda de 5,3% do PIB em 1929–31 e recuperação a partir de 1932), sem refutá-las. [Anotações da aula]'),

    ('Segundo a leitura de Furtado, a crise de 1929 teve efeito prolongado e devastador sobre o produto brasileiro, com recuperação só após 1934, o que decorreria da ausência de qualquer política de sustentação da demanda interna.',
     '<b>ERRADO.</b> O impacto foi <b>modesto e curto</b>: queda de 5,3% do PIB entre 1929 e 1931, recuperação desde o 2º semestre de 1932 e crescimento de 9% em 1933–34, bem menos grave que a recessão dos EUA. A explicação de Furtado é a política de defesa da renda (queima de café financiada por crédito), keynesiana antes de Keynes. [Anotações da aula]'),

    ('A teoria da industrialização induzida pelas exportações sustenta que a indústria crescia sobretudo nos períodos de crise do setor cafeeiro, quando o câmbio desvalorizado e a escassez de divisas encareciam os importados e abriam espaço para a produção nacional.',
     '<b>ERRADO.</b> Esse é o argumento da teoria dos <b>choques adversos</b>. A industrialização <b>induzida por exportações</b> aponta o crescimento industrial nos momentos de <b>expansão</b> cafeeira, com renda, massa salarial e <b>divisas</b> para importar máquinas e equipamentos. A pegadinha é trocar o nome das teorias. [Anotações da aula]'),

    ('Na síntese entre as duas explicações para a industrialização anterior a 1930, a fase de expansão do setor exportador ampliava a capacidade produtiva por meio da importação de máquinas, e a fase de crise permitia ocupar a capacidade ociosa assim formada, de modo que o ciclo industrial ocorria tanto em conjunto quanto em contrafluxo com o setor exportador.',
     '<b>CERTO.</b> As duas teorias são parcialmente corretas: na expansão, divisas e capital permitem investir (surge capacidade ociosa); na crise, câmbio desvalorizado e restrição de divisas induzem a substituição de importados, ocupando essa capacidade. Por isso a indústria acompanha e também contraria o ciclo exportador. [Anotações da aula]'),

    ('O capital industrial brasileiro teve origem predominantemente estrangeira, associada a empresas que se instalaram para suprir o mercado interno, sem vínculos relevantes com o complexo cafeeiro.',
     '<b>ERRADO.</b> A origem do capital industrial está no <b>capital cafeeiro</b>: produtores de café diversificavam suas aplicações e famílias cafeicultoras passaram a investir em ramos industriais. A indústria nasce, portanto, das atividades do complexo cafeeiro, e não à parte dele. [Anotações da aula]'),

    ('Após 1930, a arrecadação passou a depender mais dos impostos de importação, dada a proteção cambial, e a compra de café pelo governo foi financiada sobretudo por investimento estrangeiro, o que reforçou o caráter pré-keynesiano da política de gastos.',
     '<b>ERRADO.</b> As importações despencaram, de modo que os impostos sobre elas deixaram de bastar e ganharam peso o <b>imposto de renda e o de consumo</b>. A compra e a queima do café foram financiadas por <b>expansão do crédito do Banco do Brasil</b>, justamente porque já não havia investimento estrangeiro. [Anotações da aula]'),

    ('Com o abandono do padrão-ouro em 1930, a queda do balanço de pagamentos deixou de forçar a contração monetária, e a base monetária passou a crescer desde o início da crise, enquanto os preços domésticos caíram de forma contínua até 1933.',
     '<b>ERRADO.</b> A base monetária ainda <b>caiu até o 1º trimestre de 1931</b> e só então passou a subir. Os preços caíram em 1930–31 e <b>estabilizaram em 1932–33</b>. É correto que, sem lastro em ouro, o déficit externo deixou de impor contração monetária automática. [Anotações da aula]'),

    ('A folga cambial de 1936–37, obtida com exportações crescentes e importações contidas pelos controles, levou ao relaxamento das restrições de importação e à liberação de remessas de lucros, o que consumiu as reservas acumuladas, gerou descoberto no fim de 1937 e forçou a retomada dos controles cambiais e a desvalorização.',
     '<b>CERTO.</b> Ciclo típico do período: a folga leva à liberalização, que esgota as divisas e obriga a voltar aos controles. O desfecho de 1937 (escassez de divisas, controles e desvalorização) ocorre no mesmo ano da instauração do Estado Novo e do reforço do papel do Estado. [Anotações da aula]'),

    ('No comércio de compensação com a Alemanha, os saldos bilaterais eram liquidados em divisas conversíveis ao final de cada ano, o que reduzia o risco de acumulação de créditos em marcos e favoreceu a expansão da participação alemã no comércio brasileiro.',
     '<b>ERRADO.</b> Os saldos viravam <b>depósitos inconversíveis</b>, a compensar em importações futuras. A prática foi sendo <b>sufocada</b> porque acumular reservas em marcos tornou-se perigoso com a ameaça de guerra. A Alemanha, porém, subiu de 12% para 25% do comércio brasileiro entre 1928 e 1938, à custa do Reino Unido. [Anotações da aula]'),

    ('Em 1939, a produção doméstica já respondia pela maior parte da oferta interna de bens de consumo duráveis e de bens de capital, o que indica que a industrialização do período havia superado a etapa de bens de consumo não duráveis.',
     '<b>ERRADO.</b> A oferta doméstica era dominante nos <b>não duráveis</b> (mais de 90%), mas minúscula em <b>duráveis (2,5%)</b> e <b>bens de capital (4,9%)</b>. A industrialização dos anos 1930 foi, portanto, concentrada em bens leves, e o aprofundamento ficou para o Estado empresário (CSN, Vale, FNM) e para as fases seguintes. [Anotações da aula]'),

    ('Nos primeiros anos da Segunda Guerra, o conflito favoreceu o desenvolvimento industrial brasileiro por reduzir a concorrência de importados, e foi a partir de 1942 que o acúmulo de reservas e o aumento da entrada de capitais americanos tornaram o período mais difícil para a indústria.',
     '<b>ERRADO.</b> No início a guerra <b>prejudicou</b> a indústria, ao dificultar a importação de insumos e equipamentos. O <b>ponto de inflexão foi 1942</b>: aceleração industrial, acúmulo de reservas e entrada de capitais dos EUA, com políticas fiscal, monetária e creditícia expansionistas e déficits financiados por emissão primária. [Anotações da aula]'),

    ('À medida que a guerra se aproximava do fim, os Estados Unidos passaram a ver com hostilidade a substituição de importações, defendendo que os países industrializados durante o conflito voltassem à especialização primária, e se recusaram a reajustar o preço do café.',
     '<b>CERTO.</b> Menor "generosidade" dos EUA: recusa a reajustar o preço do café e pressão para que países como o Brasil se reespecializassem em produtos primários, para que os EUA recuperassem mercados perdidos. No plano teórico, a teoria neoclássica criticava a industrialização por substituição de importações. [Anotações da aula]'),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::O Primeiro Governo Vargas (1930-1945)",
        "Economia - O Primeiro Governo Vargas (1930-1945).apkg",
        VARGAS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
