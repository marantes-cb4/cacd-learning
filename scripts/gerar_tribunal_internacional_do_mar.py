#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 02 (Julho/2023).

Tema: Tribunal Internacional do Mar e solução de controvérsias (parte do Item 32 do Edital CACD).

Fontes:
  - Anotações: Tribunal Internacional do Mar.md
  - Material do professor: Direito Internacional_Rodada 02_Julho_2023_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 02_Julho_2023.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/direito internacional"
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


TIDM = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Antes de acionar qualquer meio jurisdicional previsto na CNUDM, os "
     "Estados em litígio devem tentar consultas ou conciliação; cumprida "
     "essa etapa, só podem levar o caso ao Tribunal Internacional do Mar, "
     "que detém competência exclusiva sobre controvérsias de direito do "
     "mar, e a opção deve constar de declaração escrita.",
     "<b>ERRADO.</b> A etapa diplomática vem antes (arts. 283–284) e a "
     "escolha se faz por declaração escrita (art. 287), mas o TIDM "
     "<b>não tem competência exclusiva</b>: o Estado pode optar também pela "
     "CIJ, por tribunal arbitral ou por tribunal arbitral especializado, "
     "sem hierarquia entre eles. [Anotações da aula; Rodada 02/Jul.2023]"),

    ("O tribunal arbitral previsto na CNUDM é constituído para um único "
     "litígio e composto por cinco árbitros, emitindo laudo vinculante; já "
     "o tribunal arbitral especializado é reservado a temas recorrentes, "
     "como pesca, preservação do meio marinho, pesquisa científica "
     "marinha e navegação, inclusive poluição por embarcações.",
     "<b>CERTO.</b> O tribunal arbitral comum é <i>ad hoc</i> (5 árbitros, "
     "sentença obrigatória). O especializado atua nas quatro matérias "
     "frequentes listadas. Ambos são alternativas ao TIDM e à CIJ no "
     "sistema do art. 287. [Anotações da aula; Rodada 02/Jul.2023]"),

    ("O Acordo BBNJ (2023), por tratar de biodiversidade marinha, aplica-se "
     "a todos os espaços marítimos, inclusive à zona econômica exclusiva e "
     "à plataforma continental, e atribui à Autoridade Internacional dos "
     "Fundos Marinhos a gestão dos recursos genéticos da Área.",
     "<b>ERRADO.</b> O BBNJ vale apenas <b>além da jurisdição nacional</b>: "
     "alto-mar e Área. E <b>não amplia</b> as funções da AIFM, que continua "
     "restrita aos recursos minerais (art. 133 da CNUDM). Para a doutrina "
     "citada na aula, o material genético explorado deve ser "
     "partilhado, ao contrário da liberdade de pesca (art. 87). "
     "[Anotações da aula; Rodada 02/Jul.2023]"),

    ("A Câmara de Controvérsias dos Fundos Marinhos integra o Tribunal "
     "Internacional do Mar, é composta por onze juízes escolhidos pelos "
     "vinte e um juízes do Tribunal e não pode se pronunciar sobre decisões "
     "discricionárias da Autoridade Internacional dos Fundos Marinhos.",
     "<b>CERTO.</b> Arts. 186–191: a Câmara é órgão especializado do TIDM "
     "(11 juízes eleitos entre os 21). Atua em litígios sobre a Área e a "
     "AIFM, mas o art. 189 proíbe que revise os atos discricionários "
     "(políticos) da Autoridade. [Anotações da aula; Rodada 02/Jul.2023]"),

    ("Dentro da estrutura da Autoridade Internacional dos Fundos Marinhos, "
     "a Empresa é o órgão encarregado de transporte, processamento e "
     "comercialização dos minerais extraídos da Área, e a Autoridade, com "
     "sede na Jamaica, atua como representante da humanidade na extração "
     "de minérios.",
     "<b>CERTO.</b> A AIFM (sede na Jamaica) tem Assembleia (arts. "
     "159–160), Conselho (161–162), Secretariado (166) e a Empresa (art. "
     "170), que desenvolve as atividades econômicas com os minerais da "
     "Área. Atua em nome da humanidade e redistribui riqueza e "
     "conhecimento. [Anotações da aula; Rodada 02/Jul.2023]"),

    ("O Acordo de 1994, relativo à Parte XI da CNUDM, e o Acordo de 1995, "
     "sobre peixes transzonais e altamente migratórios, foram adotados "
     "para suprir lacunas da Convenção de 1982: o primeiro para superar "
     "impasses sobre a exploração da Área e o segundo em razão do avanço "
     "do conhecimento científico sobre a proteção desses estoques.",
     "<b>CERTO.</b> Com o BBNJ (2023), são os três tratados que "
     "complementam a CNUDM, a qual não é aplicada isoladamente. O de 1994 "
     "trata da Área e da AIFM; o de 1995, dos peixes transzonais e "
     "altamente migratórios. [Anotações da aula; Rodada 02/Jul.2023]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Jul/2023) ───────────────

    ("01-II – Se reconhecida a jurisdição do Tribunal Internacional do "
     "Direito do Mar (TIDM) acerca de controvérsia relativa à "
     "interpretação ou aplicação da CNUDM, em virtude do art. 288 da "
     "CNUDM, o TIDM deve aplicar a CNUDM e outras normas de direito "
     "internacional que não forem incompatíveis com a CNUDM na resolução "
     "da controvérsia jurídico-internacional. (C/E?)",
     "<b>CERTO.</b> Art. 288: o órgão jurisdicional aplica a própria CNUDM, "
     "outros tratados correlatos aos seus objetivos e outras fontes do DIP "
     "compatíveis (costumes, princípios gerais; o rol do art. 38 da CIJ não "
     "é taxativo). [Exercício Q01-II, Rodada 02 Jul/2023]"),

    ("01-III – Um Estado, ao assinar ou ratificar a Convenção das Nações "
     "Unidas sobre o Direito do Mar ou a ela aderir, ou em qualquer momento "
     "ulterior, pode escolher livremente, por meio de declaração escrita, "
     "um ou mais meios para a solução das controvérsias relativas à "
     "interpretação ou à aplicação da referida convenção, entre os quais, "
     "a Corte Internacional de Justiça, o Tribunal Internacional do Direito "
     "do Mar, um tribunal arbitral constituído em conformidade com o Anexo "
     "VII da referida convenção e o Órgão de Apelação da Organização "
     "Mundial do Comércio. (C/E?)",
     "<b>ERRADO.</b> O art. 287 admite quatro meios: TIDM, CIJ, tribunal "
     "arbitral e tribunal arbitral especial. O Órgão de Apelação da OMC não "
     "está entre eles; ele só atua como segunda instância dentro do "
     "sistema de solução de controvérsias da própria OMC. [Exercício "
     "Q01-III, Rodada 02 Jul/2023]"),

    ("01-IV – Empresas estatais e pessoas físicas ou jurídicas podem "
     "figurar como partes em controvérsias instauradas perante o Tribunal "
     "Internacional sobre o Direito do Mar, especificamente por meio da "
     "atuação da Câmara de Controvérsias dos Fundos Marinhos. (C/E?)",
     "<b>CERTO.</b> Art. 187: a Câmara decide litígios sobre contratos de "
     "exploração dos recursos minerais da Área, dos quais podem ser partes "
     "Estados, a AIFM, a Empresa, empresas estatais e pessoas físicas e "
     "jurídicas. Fora dessa matéria contratual, indivíduos e empresas não "
     "acessam o TIDM. [Exercício Q01-IV, Rodada 02 Jul/2023]"),

    ("02-I – A Comissão de Limites da Plataforma Continental (CLPC), "
     "organização intergovernamental, é composta por 21 membros peritos em "
     "geologia, geofísica ou hidrografia. Sua principal função é examinar "
     "os dados e outros elementos de informação, apresentados pelos Estados "
     "costeiros acerca dos limites exteriores da plataforma continental nas "
     "zonas em que tais limites podem chegar até 350 milhas marítimas. "
     "(C/E?)",
     "<b>ERRADO.</b> A CLPC <b>não é organização internacional nem "
     "intergovernamental</b>: não tem personalidade jurídica própria nem "
     "representa Estados. É órgão técnico de 21 peritos que atuam a título "
     "pessoal (art. 76). A descrição das funções está correta. [Exercício "
     "Q02-I, Rodada 02 Jul/2023]"),

    ("02-II – A Comissão de Limites da Plataforma Continental (CLPC) fará "
     "recomendações aos Estados costeiros sobre questões relacionadas com "
     "o estabelecimento de limites exteriores da plataforma continental. "
     "Os limites da plataforma continental estabelecidos pelo Estado "
     "costeiro com base nessas recomendações serão definitivos e "
     "obrigatórios. (C/E?)",
     "<b>CERTO.</b> Art. 76, §8º: os limites fixados com base nas "
     "recomendações da CLPC são obrigatórios e definitivos. Em seguida "
     "(§9º), o Estado deposita os mapas e informações junto ao "
     "Secretário-Geral da ONU, que lhes dá publicidade. [Exercício Q02-II, "
     "Rodada 02 Jul/2023]"),

    ("02-IV – Acordo sobre Utilização Sustentável e Conservação da "
     "Biodiversidade Marinha para Além da Jurisdição Nacional (BBNJ), "
     "concluído em 2023, prevê sua aplicação na Área, em conformidade com "
     "o princípio do patrimônio comum da humanidade, sem chamar a "
     "Autoridade Internacional dos Fundos Marinhos para fazer a gestão do "
     "patrimônio genético. (C/E?)",
     "<b>CERTO.</b> O BBNJ vale para alto-mar e Área e não altera as "
     "atribuições da AIFM: ela segue restrita aos recursos minerais (art. "
     "133 da CNUDM) e não tem papel na biodiversidade e no patrimônio "
     "genético da Área. [Exercício Q02-IV, Rodada 02 Jul/2023]"),

    ("03-I – Apresentando como órgãos principais uma assembleia, um "
     "conselho e um secretariado, a Autoridade Internacional dos Fundos "
     "Marinhos (ISBA) tem jurisdição limitada à área (zona) abrangendo o "
     "leito do mar, os fundos marinhos e o seu subsolo, além dos limites "
     "da jurisdição nacional. (C/E?)",
     "<b>CERTO.</b> A AIFM é OI com personalidade própria, sede em "
     "Kingston (Jamaica), e atua exclusivamente na exploração de minerais "
     "da Área. Não exerce nenhuma atribuição no alto-mar, outro espaço além "
     "da jurisdição nacional. [Exercício Q03-I, Rodada 02 Jul/2023]"),

    ("03-III – Nos termos da Convenção das Nações Unidas sobre o Direito "
     "do Mar (CNUDM), todos os Estados-partes são ipso facto membros da "
     "Autoridade Internacional dos Fundos Marinhos, organização "
     "internacional dotada de personalidade jurídica internacional. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 176: a AIFM é OI com personalidade jurídica "
     "própria (sujeito derivado). Art. 156: todos os Estados-partes da "
     "CNUDM são automaticamente (<i>ipso facto</i>) seus membros. "
     "[Exercício Q03-III, Rodada 02 Jul/2023]"),

    ("03-IV – A Câmara de Controvérsias dos Fundos Marinhos emitirá, com "
     "caráter de urgência, a pedido da Assembleia ou do Conselho, "
     "pareceres consultivos sobre questões jurídicas que se suscitem no "
     "âmbito das suas atividades. Excepcionalmente, admite-se também a "
     "possibilidade de a Câmara de Controvérsias dos Fundos Marinhos "
     "substituir a Autoridade Internacional dos Fundos Marinhos no "
     "exercício dos poderes discricionários desta. (C/E?)",
     "<b>ERRADO.</b> A primeira parte está certa (art. 191: só a "
     "Assembleia e o Conselho da AIFM pedem pareceres, com urgência). Mas "
     "o art. 189 proíbe expressamente que a Câmara controle ou substitua a "
     "AIFM em decisões discricionárias, que se baseiam em conveniência e "
     "oportunidade. [Exercício Q03-IV, Rodada 02 Jul/2023]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Tribunal Internacional do Mar",
        "Direito Internacional - Tribunal Internacional do Mar.apkg",
        TIDM,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
