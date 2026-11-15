#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Setembro/2026).

Tema: Direito Internacional do Meio Ambiente (Item 32 do Edital CACD).

Fontes:
  - Anotações: Direito Internacional do Meio Ambiente.md
  - Material do professor: Direito Internacional_Rodada 01_Setembro_2026_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Setembro_2026.pdf
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


CARDS = [

    # ---- Exercícios do professor (enunciado e gabarito literais) ----
    ('Julgue o item abaixo sobre o Direito Internacional do Meio Ambiente: O direito ao meio ambiente equilibrado está previsto na ordem internacional desde a Declaração Universal dos Direitos Humanos.',
     '<b>ERRADO.</b> A DUDH (1948) só consagra direitos de 1ª geração (civis e políticos) e de 2ª geração (sociais, econômicos e culturais). O meio ambiente é direito de 3ª geração e só entrou na pauta da ONU após a década de 1970. Atenção: o laudo da Fundição Trail (1941) tampouco reconheceu esse direito; reconheceu a proibição de danos transfronteiriços. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Julgue o item abaixo sobre o Direito Internacional do Meio Ambiente: A terceira geração dos direitos humanos diz respeito aos direitos de titularidade coletiva, a exemplo da paz mundial e do meio ambiente equilibrado, consagrando o princípio da igualdade.',
     '<b>ERRADO.</b> A titularidade coletiva (direitos difusos ou transindividuais) está correta, mas a 3ª geração consagra a <b>fraternidade ou solidariedade</b>. O princípio da <b>igualdade</b> é o lema da 2ª geração (sociais, econômicos e culturais); a 1ª é a liberdade. A banca troca o lema da geração. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Julgue o item abaixo sobre o Direito Internacional do Meio Ambiente: O surgimento do direito do desenvolvimento, a partir da década de 1960, marcado essencialmente pelo processo de descolonização, impulsionou a transformação do direito internacional do meio ambiente em uma área de interesse global.',
     '<b>CERTO.</b> A descolonização da Ásia e da África trouxe novos Estados à ONU, que diversificaram a pauta da Assembleia Geral e levaram o tema ambiental a ela. O direito do desenvolvimento (tratamento não idêntico entre Estados desenvolvidos e não desenvolvidos) potencializou o caminho até Estocolmo (1972). [Anotações da aula; Rodada 01 Set/2026]'),

    ('Sobre os elementos definidores dos tratados e convenções internacionais em matéria de meio ambiente, julgue a assertiva que segue: Nas convenções-quadros, há a perfeita identidade entre as partes do tratado originário e dos tratados regulamentadores criados posteriormente para assegurar a especificação dos seus termos.',
     '<b>CERTO.</b> Na convenção-quadro, todos os Estados-partes estão representados na Conferência das Partes (COP), que elabora as normas complementares. Por isso todos acabam se vinculando aos tratados regulamentadores (relação harmônica). Nos tratados guarda-chuva é o oposto: as partes dos tratados-anexo não precisam ser as mesmas. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Sobre os elementos definidores dos tratados e convenções internacionais em matéria de meio ambiente, julgue a assertiva que segue: Os tratados guarda-chuvas (umbrella treaty) são caracterizados por conter em cláusulas vagas e abertas, o que demanda regulamentação posterior a ser realizada por meio reuniões periódicas e regulares realizadas por um órgão composto de representantes dos Estados-partes denominado de Conferência das Partes (COP).',
     '<b>ERRADO.</b> Cláusulas gerais e abertas existem nos dois tipos, mas a <b>COP é própria da convenção-quadro</b>. O guarda-chuva cobre um extenso domínio temático que não interessa a todos com a mesma intensidade, então não há órgão representando todos os Estados. Os tratados-anexo são negociados só pelos Estados interessados. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Sobre os elementos definidores dos tratados e convenções internacionais em matéria de meio ambiente, julgue a assertiva que segue: Segundo a doutrina, as convenções-quadros e os tratados guarda-chuvas adotam o chamado enfoque fracionado como estratégia negocial, de modo que são elaborados com base em previsões genéricas e abertas com disposições sobre as quais existe acordo entre os Estados, deixando para negociações posteriores e específicas a disciplina jurídica de pontos polêmicos.',
     '<b>CERTO.</b> O enfoque fracionado (piecemeal approach) é comum aos dois tipos: fecha-se tratado sobre o consenso político e científico e adia-se o controverso. Exemplo: a Convenção-Quadro do Clima (1992) obrigou à redução de emissões, e só o Protocolo de Quioto (1997) fixou metas e parâmetros. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Acerca do Direito Internacional do Meio Ambiente, julgue o item a seguir: A Declaração do Rio sobre Meio Ambiente e Desenvolvimento de 1992, por conter uma série de princípios, tem a natureza de norma internacional positiva.',
     '<b>ERRADO.</b> A Declaração do Rio (ECO-92) tem a <b>forma de soft law</b>, não vinculante, embora reproduza princípios gerais do DIP. Se um Estado os viola, o ilícito decorre do princípio geral (que é norma positiva e vinculante) e não da Declaração. Conteúdo de princípio não transforma o documento em hard law. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Acerca do Direito Internacional do Meio Ambiente, julgue o item a seguir: De acordo com o princípio da precaução, as partes se comprometem a adotar medidas protetivas em face de provas científicas de danos sérios e irreversíveis ao meio ambiente.',
     '<b>ERRADO.</b> Havendo <b>certeza científica</b> do dano, aplica-se o princípio da <b>prevenção</b>. A <b>precaução</b> incide quando há <b>dúvida</b>: a ausência de certeza científica absoluta não justifica adiar medidas (Declaração do Rio, princípio 15), e exige-se prova de que a atividade não é danosa. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Acerca do Direito Internacional do Meio Ambiente, julgue o item a seguir: A Convenção das Nações Unidas sobre o Direito do Mar de 1982 (CNUDM) tem a natureza jurídica de tratado guarda-chuva, sendo o Acordo sobre Conservação e Uso Sustentável da Biodiversidade Marinha em Áreas Além da Jurisdição Nacional (BBNJ) exemplo de tratado que a complementa.',
     '<b>CERTO.</b> A CNUDM (Montego Bay) é o exemplo de umbrella treaty: seus acordos complementares (Parte XI de 1994, peixes transzonais de 1995 e BBNJ de 2023) não vinculam todos os seus Estados-partes. O Brasil ratificou o BBNJ em 2025, e o acordo entrou em vigor em janeiro de 2026. [Anotações da aula; Rodada 01 Set/2026]'),

    ('Acerca do Direito Internacional do Meio Ambiente, julgue o item a seguir: Não obstante o Direito Internacional do Meio Ambiente ser considerado uma área recente do Direito das Gentes, admite-se o emprego de normas costumeiras para disciplinar temas relacionados à proteção do meio ambiente, a exemplo do que consta na Opinião Consultiva emitida em 2025 pela Corte Internacional de Justiça (CIJ) sobre as Obrigações dos Estados em relação à Mudança do Clima.',
     '<b>CERTO.</b> O ramo admite costume e princípios gerais, além de tratados, atos unilaterais e decisões vinculantes de OIs. Na OC de 2025, a CIJ aplicou o costume sobre responsabilidade do Estado por ato ilícito (reparação), porque os tratados climáticos não tratam disso. Os regimes devem ser lidos sistemicamente, sem lex specialis. [Anotações da aula; Rodada 01 Set/2026]'),

    # ---- Cards próprios (lacunas das anotações) ----
    ('A arbitragem da Fundição Trail (EUA x Canadá, 1941), apontada como a primeira manifestação solene do Direito Internacional do Meio Ambiente, baseou-se em tratado bilateral e inaugurou, em sentença arbitral, o reconhecimento do direito humano ao meio ambiente ecologicamente equilibrado.',
     '<b>ERRADO.</b> O tribunal ad hoc fundou-se em <b>princípios gerais do DIP</b> e reconheceu que o Estado não pode usar seu território de modo que cause dano ao território de outro (<b>proibição de danos transfronteiriços</b>). Esse princípio foi replicado em Estocolmo (1972) e na Declaração do Rio (1992). Responsabilizou-se o Estado sede da empresa poluidora. [Anotações da aula]'),

    ('A Conferência de Estocolmo (1972) inaugurou o período em que o Direito Internacional do Meio Ambiente passa a ser produzido sobretudo por normas vinculantes globais, razão pela qual a Convenção-Quadro do Clima de 1992 já é considerada o ponto de partida da atuação das organizações internacionais no tema.',
     '<b>ERRADO.</b> Estocolmo abre o <b>2º período</b>: multilateralismo, protagonismo das OIs (em especial a ONU) e <b>soft law</b>. As normas vinculantes globais (hard law) formam o <b>3º período</b> (CNUDM 1982; Convenção-Quadro do Clima e Convenção da Biodiversidade, ligadas à ECO-92). O 1º período (1919-1945) é difuso e bilateral, sem OIs. [Anotações da aula]'),

    ('Para Guido Soares, as normas de soft law em matéria ambiental criam obrigações jurídicas imperfeitas, de modo que sua violação gera responsabilidade internacional atenuada, e servem para fixar metas e orientar a adaptação do direito interno dos Estados, como ocorreu com a Agenda 21.',
     '<b>ERRADO.</b> A soft law cria apenas <b>obrigações morais</b>: sua violação <b>não configura ilícito internacional</b>, nem sequer de forma atenuada. As duas finalidades indicadas (fixar metas futuras e orientar a adoção de normas internas, preparando o terreno para a hard law) estão corretas, e a Agenda 21 (ECO-92) é o exemplo. [Anotações da aula]'),

    ('As ONGs, embora sem personalidade jurídica internacional, são consideradas atores não estatais internacionalmente relevantes no Direito Internacional do Meio Ambiente, em razão de sua atuação como observadoras em negociações, de seu suporte técnico-científico e de sua função de grupos de pressão.',
     '<b>CERTO.</b> A prevalência é de que ONGs <b>não são sujeitos de DIP</b> (a personalidade das OIs foi reconhecida pela CIJ no caso Bernadotte, 1949), mas elas observam conferências patrocinadas por OIs, fornecem informação científica e mobilizam a opinião pública contra Estados infratores. Isso mostra que o meio ambiente interessa à humanidade, e não só aos Estados. [Anotações da aula]'),

    ('Segundo André de Carvalho Ramos, o racismo ambiental limita-se à incidência desproporcional dos danos ambientais sobre grupos definidos por critérios raciais biológicos ou fenotípicos, ao passo que o neocolonialismo ambiental decorre da migração de indústrias poluentes dos Estados em desenvolvimento para os desenvolvidos.',
     '<b>ERRADO.</b> Duas inversões. O racismo ambiental tem <b>dimensão social</b>: atinge os vulneráveis, para além de aspectos biológicos ou fenotípicos. No neocolonialismo ambiental (plano interestatal), regras mais rígidas dos <b>desenvolvidos</b> empurram indústrias poluentes para os <b>não desenvolvidos</b>, de normas mais flexíveis. Ambos formam a injustiça ambiental, que afeta o direito à igualdade. [Anotações da aula]'),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Direito Internacional do Meio Ambiente",
        "Direito Internacional - Direito Internacional do Meio Ambiente.apkg",
        CARDS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
