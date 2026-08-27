#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional dos Direitos Humanos: Sistema Interamericano.

Tema: Direito internacional dos direitos humanos. Sistema Interamericano
(Item 28 do Edital CACD).

Fontes:
  - Anotações: Sistema Interamericano de Direitos Humanos.md
  - Material do professor: Direito Internacional_Rodada 02_Janeiro_2024 _Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 02_Janeiro_2024 .pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelreichelt/Desktop/cacd-learning/anki/decks/direito internacional"
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


SISTEMA_INTERAMERICANO_DDHH = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("A Comissão Interamericana de Direitos Humanos e a Corte Interamericana de "
     "Direitos Humanos possuem composição idêntica quanto ao número de membros "
     "e à duração do mandato, ambas compostas por sete integrantes eleitos a "
     "título pessoal pela Assembleia-Geral da OEA, com mandato de seis anos e "
     "admitida uma única reeleição.",
     "<b>ERRADO.</b> Ambas têm <b>7 integrantes</b>, mas o mandato difere: a "
     "Comissão tem mandato de <b>4 anos</b> (art. 37 do Pacto), e a Corte, de "
     "<b>6 anos</b> (art. 54) — em ambos os casos admitida uma reeleição. "
     "[Anotações da aula; Rodada 02/Jan.2024, arts. 34, 37, 52, 54]"),

    ("Para que a Comissão Interamericana de Direitos Humanos receba uma "
     "petição interestatal, na qual um Estado-parte denuncia outro por "
     "violação da Convenção Americana, é necessário que ambos os Estados "
     "envolvidos — denunciante e denunciado — tenham manifestado previamente "
     "sua concordância com essa competência da Comissão, ao passo que a "
     "petição individual dispensa qualquer aceitação prévia do Estado "
     "denunciado.",
     "<b>CERTO.</b> Art. 45 do Pacto de San José: a petição interestatal "
     "exige declaração PRÉVIA de reconhecimento da competência da Comissão, "
     "tanto pelo Estado que denuncia quanto pelo denunciado; já a petição "
     "individual (art. 44) não exige nenhuma aceitação do Estado para ser "
     "recebida pela Comissão. [Anotações da aula; Rodada 02/Jan.2024, "
     "arts. 44-45]"),

    ("Caso um Estado-parte pretenda arguir a ausência de esgotamento dos "
     "recursos internos como óbice à admissibilidade de um litígio no "
     "sistema interamericano, deve fazê-lo perante a Corte Interamericana de "
     "Direitos Humanos, órgão competente para apreciar tal requisito no "
     "momento do julgamento do mérito da causa.",
     "<b>ERRADO.</b> Somente a <b>Comissão Interamericana</b> tem "
     "competência para verificar o requisito da subsidiariedade (art. 61, "
     "§2º do Pacto). Se o Estado só alegar a ausência de esgotamento perante "
     "a Corte, configura-se <b>estoppel</b> (vedação de comportamento "
     "contraditório) — presume-se desistência tácita da objeção. "
     "[Anotações da aula; Rodada 02/Jan.2024, p.17]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Jan/2024) ──────────────

    ("01-I – A Convenção Interamericana de Direitos Humanos, pelo seu "
     "conteúdo, teve aplicação imediata no Brasil, sem necessidade do "
     "processo constitucional de internalização de convenções. (C/E?)",
     "<b>ERRADO.</b> O STF exige 4 etapas para incorporar tratados "
     "internacionais, inclusive de direitos humanos: (i) negociação e "
     "assinatura pelo Presidente (art. 84, VIII, CF); (ii) aprovação pelo "
     "Congresso via decreto legislativo (art. 49, I, CF); (iii) ratificação "
     "internacional pelo Presidente; (iv) promulgação por decreto "
     "presidencial. [Exercício Q01-I, Rodada 02 Jan/2024]"),

    ("01-II – Para que os estrangeiros residentes no Brasil possam invocar "
     "as garantias da Convenção Interamericana em seu favor, há necessidade "
     "de reciprocidade pelo país de nacionalidade do estrangeiro. (C/E?)",
     "<b>ERRADO.</b> Direitos humanos regem-se pelo princípio da "
     "<b>universalidade</b> — são assegurados independentemente de "
     "nacionalidade, residência ou reciprocidade — e criam obrigações "
     "<b>erga omnes</b>, que permitem, inclusive, que sujeitos alheios ao "
     "tratado exijam sua observância. [Exercício Q01-II, Rodada 02 Jan/2024]"),

    ("01-III – Qualquer pessoa ou grupo de pessoas, ou entidade "
     "não-governamental legalmente reconhecida em um ou mais "
     "Estados-Membros da OEA, pode apresentar à Corte petições que "
     "contenham denúncias ou queixas de violação da Convenção Americana "
     "sobre Direitos Humanos por um Estado-Parte. (C/E?)",
     "<b>ERRADO.</b> O art. 44 do Pacto reconhece o direito de petição "
     "junto à <b>Comissão</b> Interamericana — não perante a Corte. "
     "Indivíduos, grupos e ONGs nunca peticionam diretamente à Corte. "
     "[Exercício Q01-III, Rodada 02 Jan/2024]"),

    ("01-IV – Para que uma petição contendo denúncia ou queixa de violação "
     "da Convenção Americana sobre Direitos Humanos por um Estado Parte seja "
     "admitida pela Comissão é necessário, como regra geral, que tenham "
     "sido interpostos e esgotados os recursos da jurisdição interna, de "
     "acordo com os princípios de direito internacional geralmente "
     "reconhecidos. (C/E?)",
     "<b>CERTO.</b> É a regra geral do princípio da subsidiariedade (art. "
     "46). Exceção: ineficiência dos recursos internos, hipótese em que a "
     "Comissão pode atuar mesmo sem esgotamento prévio. "
     "[Exercício Q01-IV, Rodada 02 Jan/2024]"),

    ("02-I – Nas sentenças proferidas pela Corte Interamericana pode haver a "
     "condenação de pessoa física ou jurídica responsável pela violação de "
     "direito previsto na Convenção Americana sobre Direitos Humanos. (C/E?)",
     "<b>ERRADO.</b> A Corte exerce jurisdição internacional <b>civil</b> "
     "sobre <b>Estados</b> — nunca julga indivíduos ou pessoas jurídicas. "
     "Só tribunais penais internacionais (TPI, tribunais ad hoc) julgam "
     "indivíduos. [Exercício Q02-I, Rodada 02 Jan/2024]"),

    ("02-II – O quórum para as deliberações da Corte Interamericana de "
     "Direitos Humanos é constituído por cinco juízes. (C/E?)",
     "<b>CERTO.</b> Art. 56 do Pacto: quórum de <b>5 juízes</b> — mesmo a "
     "Corte tendo 7 juízes no total (art. 52), eleitos por mandato de 6 "
     "anos com uma reeleição admitida. [Exercício Q02-II, Rodada 02 Jan/2024]"),

    ("02-III – No caso \"Gomes Lund\" a Corte declarou que as disposições da "
     "Lei de Anistia brasileira, no ponto em que impedem a investigação e "
     "sanção de graves violações de direitos humanos, são incompatíveis com "
     "a Convenção Americana sobre Direitos Humanos, porém se absteve de "
     "determinar que o Estado brasileiro reconheça sua responsabilidade, "
     "por se tratar de atos cometidos por regime de exceção. (C/E?)",
     "<b>ERRADO.</b> A Corte <b>condenou</b> o Brasil em 2010 pela violação "
     "da Convenção — não se absteve de nada. Os ilícitos (não investigar, "
     "não indenizar, não elucidar) são <b>permanentes</b> e permitiram a "
     "atuação da Corte mesmo tendo ocorrido antes do reconhecimento da "
     "jurisdição obrigatória em 1998. [Exercício Q02-III, Rodada 02 Jan/2024]"),

    ("02-IV – Em relação ao caso Maria da Penha Maia Fernandes, a Comissão "
     "Interamericana de Direitos Humanos reconheceu que o Estado brasileiro "
     "descumpriu o dever de garantir às pessoas sujeitas à sua jurisdição o "
     "exercício livre e pleno de seus direitos humanos e recomendou que o "
     "Brasil simplificasse os procedimentos judiciais penais. (C/E?)",
     "<b>CERTO.</b> A Comissão recomendou o aperfeiçoamento da legislação "
     "penal para proteger vítimas de violência doméstica; o Brasil acatou, "
     "resultando na Lei Maria da Penha, sem que o caso chegasse à Corte. "
     "[Exercício Q02-IV, Rodada 02 Jan/2024]"),

    ("03-I – A Comissão Interamericana de Direitos Humanos ostenta "
     "competência para receber denúncias ou queixas de violações de "
     "direitos humanos, apresentadas por indivíduos ou entidade não "
     "governamental legalmente reconhecida por um ou mais Estados-membros "
     "da OEA, contra atos dos Estados que violem a Convenção Americana "
     "sobre Direitos Humanos. (C/E?)",
     "<b>CERTO.</b> Art. 44 do Pacto: competência da Comissão para receber "
     "petições individuais de indivíduos, grupos ou ONGs. "
     "[Exercício Q03-I, Rodada 02 Jan/2024]"),

    ("03-II – Cabe à Comissão Interamericana de Direitos Humanos proceder ao "
     "juízo de admissibilidade das petições ou comunicações apresentadas, e "
     "à Corte Interamericana de Direitos Humanos julgar a ação eventualmente "
     "proposta pela Comissão. Não há, no sistema regional interamericano, "
     "viabilidade de acesso direto do indivíduo à Corte. (C/E?)",
     "<b>CERTO.</b> Fluxo correto: Comissão analisa admissibilidade "
     "(subsidiariedade) e submete à Corte; indivíduo nunca acessa a Corte "
     "diretamente — apenas participa do processo já instaurado (art. 25 do "
     "Regulamento da Corte de 2009). [Exercício Q03-II, Rodada 02 Jan/2024]"),

    ("03-III – A sentença proferida pela Corte Interamericana de Direitos "
     "Humanos será definitiva e inapelável. Na hipótese de divergência "
     "sobre o sentido ou alcance da sentença, a Corte interpretá-la-á, a "
     "pedido de qualquer das partes, desde que o pedido seja apresentado "
     "dentro de 90 dias a partir da notificação da sentença. A parte da "
     "sentença que determinar indenização compensatória poderá ser "
     "executada no país respectivo pelo processo interno vigente para a "
     "execução de sentenças contra o Estado. (C/E?)",
     "<b>CERTO.</b> Reproduz fielmente os arts. 67 e 68 do Pacto de San "
     "José: sentença definitiva/inapelável, pedido de esclarecimento em 90 "
     "dias, execução interna da indenização sem homologação. "
     "[Exercício Q03-III, Rodada 02 Jan/2024]"),

    ("03-IV – A decisão proferida pela Corte Interamericana de Direitos "
     "Humanos submete-se ao procedimento homologatório de sentenças "
     "estrangeiras, pelo Superior Tribunal de Justiça, previsto na "
     "Constituição da República (artigo 105, I, \"i\"). (C/E?)",
     "<b>ERRADO.</b> Não se confunde sentença <b>internacional</b> (de "
     "tribunal cuja jurisdição o Brasil reconheceu, como a Corte "
     "Interamericana) com sentença <b>estrangeira</b> (de autoridade de "
     "outro país). Sentenças internacionais são executadas <b>sem</b> "
     "homologação do STJ. [Exercício Q03-IV, Rodada 02 Jan/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Sistema Interamericano de Direitos Humanos",
        "Direito Internacional - Sistema Interamericano de Direitos Humanos.apkg",
        SISTEMA_INTERAMERICANO_DDHH,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
