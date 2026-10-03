#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional dos Direitos Humanos: Sistema Global.

Tema: Direito internacional dos direitos humanos. Sistema global da ONU:
Carta Internacional dos Direitos Humanos, órgãos de tratados, sistemas
convencionais de petições e Conselho de Direitos Humanos (Item 28 do
Edital CACD).

Fontes:
  - Anotações: Sistema Global de Proteção dos Direitos Humanos.md
  - Material do professor: Direito Internacional_Rodada 01_Janeiro_2026_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Janeiro_2026.pdf
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


SISTEMA_GLOBAL_DDHH = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Como o Brasil ratificou, em 1992, o Pacto de Direitos Civis e Políticos "
     "e o Pacto de Direitos Econômicos, Sociais e Culturais, e posteriormente "
     "aderiu ao protocolo facultativo do primeiro, indivíduos e Estados "
     "podem hoje apresentar ao comitê especializado de cada Pacto petições "
     "sobre violações concretas de direitos humanos pelo Brasil.",
     "<b>ERRADO.</b> O Brasil ratificou o Protocolo Facultativo do Pacto "
     "Civil e Político em <b>2009</b> (petições quase judiciais possíveis "
     "para direitos de 1ª geração), mas <b>NÃO ratificou</b> o Protocolo "
     "Facultativo do Pacto DESC: quanto aos direitos de 2ª geração, só se "
     "aplica o mecanismo não contencioso (relatórios periódicos). [Anotações "
     "da aula; Rodada 01/Jan.2026]"),

    ("No procedimento de queixas sigilosas do Conselho de Direitos Humanos "
     "da ONU (procedimento 1503), a confidencialidade da apuração é "
     "mantida até o fim, mesmo que o Estado indicado como violador "
     "descumpra as recomendações do Conselho.",
     "<b>ERRADO.</b> O sigilo é justamente o que dá eficácia ao "
     "procedimento 1503: o Estado pode adotar voluntariamente as "
     "recomendações e <b>manter a confidencialidade</b>; se não as cumprir, "
     "a confidencialidade é <b>retirada</b> e os dados das violações se "
     "tornam públicos. Diferente do procedimento especial público (1235), "
     "sempre público. [Anotações da aula; Rodada 01/Jan.2026]"),

    ("O mecanismo convencional não contencioso, baseado em relatórios "
     "periódicos dos Estados aos comitês especializados, só pode ser acionado "
     "após a constatação de uma violação concreta de direitos humanos, assim "
     "como ocorre com o mecanismo quase judicial de petições.",
     "<b>ERRADO.</b> Só o mecanismo quase judicial (petições de indivíduos ou "
     "Estados) é <b>\"ex post facto\"</b>, exigindo fato concreto de violação. "
     "O não contencioso atua continuamente, <b>mesmo sem violação</b>, "
     "buscando aperfeiçoar a proteção por meio de recomendações não "
     "vinculantes. [Anotações da aula; Rodada 01/Jan.2026]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jan/2026) ───────────────

    ("01-I – A primeira afirmação histórica dos direitos humanos coincide "
     "com a internacionalização desses direitos, materializada por meio da "
     "DUDH, também denominada Declaração de Paris, no contexto da criação da "
     "ONU. (C/E?)",
     "<b>ERRADO.</b> A internacionalização da proteção do indivíduo começa "
     "no século XIX e na 1ª metade do século XX (DIH em 1864, combate à "
     "escravidão, OIT em 1919). O que surge após 1945 são os "
     "<b>sistemas</b> internacionais de proteção. [Exercício Q01-I, Rodada "
     "01 Jan/2026]"),

    ("01-II – A Declaração Universal dos Direitos Humanos, de 1948, apesar "
     "de ter natureza de resolução, não apresenta instrumentos ou órgãos "
     "próprios destinados a tornar compulsória sua aplicação. (C/E?)",
     "<b>CERTO.</b> A DUDH é resolução da AGNU, sem forma vinculante nem "
     "órgãos próprios; seu <b>conteúdo</b> é obrigatório por refletir "
     "costumes e princípios gerais do direito. O primeiro documento da Carta "
     "Internacional a prever órgão de monitoramento foi o Pacto Civil e "
     "Político (1966). [Exercício Q01-II, Rodada 01 Jan/2026]"),

    ("01-III – O conceito de Carta Internacional de Direitos Humanos refere-"
     "se o conjunto de diplomas internacionais que conferem base jurídica ao "
     "sistema global de proteção dos direitos humanos e engloba a Carta de "
     "São Francisco de 1945, a Declaração Universal dos Direitos Humanos de "
     "1948, o Pacto Internacional dos Direitos Civis e Políticos de 1966 e o "
     "Pacto Internacional de Direitos Sociais, Econômicos e Culturais de "
     "1966. (C/E?)",
     "<b>ERRADO.</b> A Carta Internacional é formada por apenas <b>3</b> "
     "documentos: DUDH (1948), Pacto Civil e Político (1966) e Pacto DESC "
     "(1966). A Carta de São Francisco (Carta da ONU, 1945) NÃO integra o "
     "conceito. [Exercício Q01-III, Rodada 01 Jan/2026]"),

    ("01-IV – Na DUDH, encontram-se normas que consubstanciam, além de "
     "direitos e garantias individuais, direitos sociais do homem. (C/E?)",
     "<b>CERTO.</b> A DUDH previu DH de 1ª geração (civis e políticos) e de "
     "2ª geração (sociais, econômicos e culturais), depois detalhados nos 2 "
     "Pactos de 1966. Não prevê direitos de 3ª geração (ex.: meio ambiente), "
     "posteriores aos anos 1970. [Exercício Q01-IV, Rodada 01 Jan/2026]"),

    ("02-I – O Pacto Internacional sobre Direitos Civis e Políticos de 1966 "
     "estabelece mecanismo de monitoramento dos Estados por meio da "
     "apresentação de petições individuais endereçadas à antiga Comissão de "
     "Direitos Humanos da ONU, órgão que foi substituído, em 2006, pelo "
     "Conselho de Direitos Humanos das Nações Unidas. (C/E?)",
     "<b>ERRADO.</b> 2 erros: (i) o Pacto originário previu só o mecanismo "
     "não contencioso (relatórios); o sistema de petições está no "
     "<b>Protocolo Facultativo</b> (ratificado pelo Brasil em 2009); (ii) as "
     "petições vão ao <b>Comitê especializado</b> do Pacto, não à antiga "
     "Comissão. [Exercício Q02-I, Rodada 01 Jan/2026]"),

    ("02-II – O Comitê é um treaty body responsável pela fiscalização dos "
     "direitos humanos relacionados ao Pacto de Direitos Civis e Políticos. "
     "(C/E?)",
     "<b>CERTO.</b> \"Treaty body\" é o órgão previsto no próprio texto do "
     "tratado em relação ao qual atua; o Comitê foi criado pelo Pacto Civil "
     "e Político para monitorar os Estados quanto aos direitos de 1ª "
     "geração. [Exercício Q02-II, Rodada 01 Jan/2026]"),

    ("02-III – O Pacto Internacional de Direitos Sociais, Econômicos e "
     "Culturais de 1966 não prevê o direito de petição da vítima de violação "
     "dos direitos nele protegidos ao comitê especializado. (C/E?)",
     "<b>CERTO.</b> O Pacto DESC nem sequer previu originariamente o comitê "
     "(criado em 1985 pela Res. 1985/17 do ECOSOC); a competência para "
     "receber petições individuais veio com o Protocolo Facultativo, que o "
     "Brasil NÃO ratificou. [Exercício Q02-III, Rodada 01 Jan/2026]"),

    ("02-IV – Entre os diversos órgãos especializados que tratam da "
     "proteção dos direitos humanos, inclui-se a Corte Internacional de "
     "Justiça, órgão das Nações Unidas cuja competência alcança não só os "
     "Estados, mas também quaisquer pessoas físicas e jurídicas, as quais "
     "podem encaminhar suas demandas diretamente à Corte. (C/E?)",
     "<b>ERRADO.</b> A CIJ integra o sistema global (mecanismo judicial), "
     "mas só <b>Estados</b> podem acionar sua competência contenciosa (art. "
     "93 da Carta da ONU) — indivíduos, pessoas jurídicas e ONGs não. "
     "[Exercício Q02-IV, Rodada 01 Jan/2026]"),

    ("03-I – O Conselho de Direitos Humanos da ONU, criado em 2006, "
     "encontra-se vinculado ao Conselho Econômico e Social, tendo "
     "atribuições de órgão de monitoramento dos Estados, o que indica sua "
     "característica de ser desprovido de função jurisdicional. (C/E?)",
     "<b>ERRADO.</b> O Conselho de DH (criado pela Res. 60/251 da AGNU) é "
     "órgão político, sem função jurisdicional, mas é vinculado à "
     "<b>Assembleia Geral</b> — não ao ECOSOC, ao qual era vinculada a "
     "extinta Comissão de DH. [Exercício Q03-I, Rodada 01 Jan/2026; "
     "classificação conforme a explicação da aula]"),

    ("03-II – No Brasil, o Pacto Internacional sobre Direitos Civis e "
     "Políticos e o Pacto Internacional sobre Direitos Econômicos, Sociais e "
     "Culturais são tratados de direitos humanos com status de emenda "
     "constitucional e fazem parte do bloco de constitucionalidade, por "
     "serem considerados normas constitucionais. (C/E?)",
     "<b>ERRADO.</b> Ratificados em 1992, antes da EC 45/2004 (que criou o "
     "art. 5º, §3º, CF/88), têm status <b>supralegal</b> (STF). O 1º tratado "
     "de DH com equivalência de emenda foi a Convenção sobre Pessoas com "
     "Deficiência (2007, promulgada em 2009). [Exercício Q03-II, Rodada 01 "
     "Jan/2026]"),

    ("03-III – O dever ou a obrigação dos Estados-partes na realização "
     "progressiva dos direitos humanos foi consagrado expressamente no Pacto "
     "Internacional dos Direitos Econômicos, Sociais e Culturais. (C/E?)",
     "<b>CERTO.</b> Art. 2º do Pacto DESC — por serem direitos positivos, "
     "que exigem recursos e uma rede de serviços públicos, os Estados devem "
     "assegurá-los de modo <b>progressivo</b>. [Exercício Q03-III, Rodada "
     "01 Jan/2026]"),

    ("03-IV – A Declaração Universal dos Direitos Humanos é o principal "
     "documento do sistema global de proteção dos direitos humanos editado "
     "pela Organização das Nações Unidas, sendo formal e materialmente "
     "obrigatória em razão de tratar da opinio juris construída pela "
     "comunidade internacional ao longo do tempo. (C/E?)",
     "<b>ERRADO.</b> 2 erros: o ponto central é a Carta Internacional dos "
     "DH (DUDH + 2 Pactos), não só a DUDH; e a DUDH NÃO é formalmente "
     "obrigatória (resolução da AGNU sem matéria administrativa) — só "
     "<b>materialmente</b> vinculante, por refletir costume e princípios "
     "gerais. [Exercício Q03-IV, Rodada 01 Jan/2026]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Sistema Global de Proteção dos Direitos Humanos",
        "Direito Internacional - Sistema Global de Proteção dos Direitos Humanos.apkg",
        SISTEMA_GLOBAL_DDHH,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
