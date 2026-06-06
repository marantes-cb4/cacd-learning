#!/usr/bin/env python3
"""Gera deck Anki: Direito Interno - Estado Democrático de Direito"""

import genanki
import os
import random

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "anki", "decks", "direito")

STYLE = """
.card { font-family: Arial, sans-serif; font-size: 16px; text-align: left; padding: 12px; }
.front { font-weight: bold; }
"""

def make_deck(title, filename, cards):
    model_id = random.randrange(1_000_000_000, 2_000_000_000)
    deck_id = random.randrange(1_000_000_000, 2_000_000_000)

    model = genanki.Model(
        model_id,
        "CACD Basic",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card",
            "qfmt": '<div class="front">{{Frente}}</div>',
            "afmt": '{{FrontSide}}<hr>{{Verso}}',
        }],
        css=STYLE,
    )

    deck = genanki.Deck(deck_id, title)
    for front, back in cards:
        deck.add_note(genanki.Note(model=model, fields=[front, back]))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename)
    genanki.Package(deck).write_to_file(out_path)
    print(f"✅ {filename} — {len(cards)} cards")
    print(f"🎉 Deck gerado em {OUTPUT_DIR}")


CARDS = [
    # ── ESTADO DEMOCRÁTICO DE DIREITO ─────────────────────────────────────────
    (
        "O que é o Estado Democrático de Direito segundo José Afonso da Silva e a CF/88?",
        "Conceito <b>inovador</b> previsto no art. 1º caput CF/88 que <b>supera</b> a mera soma "
        "de Estado de Direito + Estado Democrático. Traço estrutural: compromisso em proteger o "
        "indivíduo independentemente de ele integrar maioria ou minoria, com ampla participação "
        "cidadã nas decisões políticas.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "O que é a democracia semidireta prevista no art. 1º parágrafo único da CF/88?",
        "O povo exerce o poder de <b>2 modos combinados</b>:<br>"
        "1. <b>Democracia indireta/representativa</b>: via representantes eleitos por tempo "
        "determinado<br>"
        "2. <b>Democracia direta/participativa</b>: o povo governa diretamente por instrumentos "
        "específicos<br>"
        "A CF/88 não adota democracia pura (direta) nem pura representativa.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "Quais são os 2 instrumentos principais da democracia indireta (representativa)?",
        "1. <b>Eleições periódicas</b>: garantem a alternância do poder<br>"
        "2. <b>Mandatos políticos por tempo determinado</b>: viabilizam a responsabilização "
        "política — representante que não atendeu às expectativas não é reeleito (responsabilização "
        "pelo voto)<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "Quais são os 4 instrumentos típicos da democracia direta na CF/88?",
        "1. <b>Plebiscito</b>: consulta popular prévia (antes da lei/decisão)<br>"
        "2. <b>Referendo</b>: consulta popular posterior (após elaboração da lei/decisão)<br>"
        "3. <b>Ação popular</b> (art. 5, LXXIII): ação judicial do cidadão-eleitor para "
        "anular ato lesivo ao patrimônio público<br>"
        "4. <b>Iniciativa popular de projeto de lei</b>: cidadãos apresentam PL diretamente "
        "ao Legislativo<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "Qual a diferença entre plebiscito e referendo? Quem tem competência para convocá-los?",
        "<b>Plebiscito</b>: consulta popular <i>prévia</i> — ocorre antes da elaboração da "
        "lei ou decisão política.<br>"
        "<b>Referendo</b>: consulta popular <i>posterior</i> — ocorre após a elaboração.<br>"
        "Ambos só se distinguem pelo <b>momento</b>. Competência exclusiva do "
        "<b>Congresso Nacional</b> (art. 49, XV CF/88): convoca plebiscito e autoriza referendo.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "O que é a ação popular e quem pode ajuizá-la?",
        "Ação judicial prevista no art. 5º, LXXIII CF/88. Apenas o <b>cidadão (eleitor)</b> "
        "pode ajuizá-la — visa <b>anular ato lesivo ao patrimônio público</b> ou a entidade "
        "de que o Estado participe. Não é qualquer pessoa: exige-se a condição de eleitor.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "Quais os requisitos para iniciativa popular de projeto de lei nos âmbitos federal, "
        "estadual e municipal?",
        "<b>Federal</b> (art. 61, §2º): 1% do eleitorado nacional, distribuídos em ≥5 estados, "
        "cada um com ≥0,3% dos eleitores<br>"
        "<b>Municipal</b> (art. 29, XIII): mínimo 5% do eleitorado<br>"
        "<b>Estadual</b> (art. 27, §4º): cada Estado define normas próprias — a CF/88 não "
        "fixa parâmetros<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),

    # ── PRINCÍPIOS FUNDAMENTAIS ────────────────────────────────────────────────
    (
        "Quais são os 5 fundamentos da República Federativa do Brasil (art. 1º CF/88)?",
        "1. <b>Soberania</b><br>"
        "2. <b>Cidadania</b><br>"
        "3. <b>Dignidade da pessoa humana</b><br>"
        "4. <b>Valores sociais do trabalho e da livre iniciativa</b><br>"
        "5. <b>Pluralismo político</b><br>"
        "Mnemônico: <i>SOCDIVAPLU</i> | Atenção: são <i>sociais</i> (não econômicos); é "
        "<i>pluralismo político</i> (não pluripartidarismo).<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito / Art. 1º CF/88</i>",
    ),
    (
        "Qual a diferença entre pluralismo político (art. 1º) e pluripartidarismo (art. 17)?",
        "<b>Pluralismo político</b> (fundamento, art. 1º, V): garante que indivíduos adotem "
        "posições políticas divergentes — diversidade de pensamento político.<br>"
        "<b>Pluripartidarismo</b> (art. 17 caput): proíbe partido único nas eleições, exigindo "
        "pluralidade partidária. Não é fundamento da RFB.<br>"
        "Pluralismo político ≠ pluripartidarismo — são institutos distintos.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito</i>",
    ),
    (
        "Quais são os 5 objetivos fundamentais da República Federativa do Brasil (art. 3º CF/88)?",
        "Todos com <b>verbos no infinitivo</b>:<br>"
        "1. <b>Construir</b> sociedade livre, justa e solidária<br>"
        "2. <b>Garantir</b> o desenvolvimento nacional<br>"
        "3. <b>Erradicar</b> a pobreza e a marginalização<br>"
        "4. <b>Reduzir</b> as desigualdades sociais e regionais<br>"
        "5. <b>Promover</b> o bem de todos, sem discriminação<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito / Art. 3º CF/88</i>",
    ),
    (
        "Quais são os 10 princípios das relações internacionais do Brasil (art. 4º CF/88)?",
        "Mnemônico: <b>Conde Preso Não Reina, Coopera Igual</b><br>"
        "<b>Con</b>cessão de asilo político | <b>De</b>fesa da paz | <b>Pre</b>valência dos "
        "direitos humanos | <b>Sol</b>ução pacífica de conflitos | <b>Não</b> intervenção | "
        "<b>Re</b>púdio ao terrorismo e ao racismo | <b>I</b>ndependência nacional | "
        "<b>A</b>utodeterminação dos povos | <b>Co</b>operação entre povos | "
        "<b>Igua</b>ldade entre os Estados<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito / Art. 4º CF/88</i>",
    ),
    (
        "O que prevê o art. 4º parágrafo único da CF/88 sobre integração regional? "
        "Qual é a interpretação do STF?",
        "Prevê norma <b>programática</b>: o Brasil buscará integração econômica, política, "
        "social e cultural com os povos da <b>América Latina</b> (não América do Sul, não "
        "Américas). Os 3 Poderes têm o dever de atuar constantemente para isso.<br>"
        "Atenção: <b>não há previsão</b> de integração militar ou monetária.<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito / Art. 4º, par. único CF/88</i>",
    ),
    (
        "O art. 2º da CF/88 (separação dos poderes) é fundamento, objetivo ou princípio das RI?",
        "Nenhum dos três. A separação dos Poderes (Legislativo, Executivo e Judiciário) é "
        "somente um <b>princípio fundamental</b> previsto no art. 2º, mas <b>não se enquadra</b> "
        "nas 3 subespécies dos arts. 1º, 3º ou 4º. Os poderes são "
        "<b>independentes e harmônicos</b> entre si (não dependentes).<br>"
        "<i>Fonte: Anotações – Estado Democrático de Direito / Art. 2º CF/88</i>",
    ),

    # ── EXERCÍCIOS — Q01 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – A soberania, a separação dos poderes, a garantia do desenvolvimento "
        "nacional e a independência nacional são exemplos de princípios fundamentais, porém "
        "apenas a soberania constitui fundamento da República Federativa do Brasil.",
        "<b>CERTO.</b> Soberania: fundamento (art. 1º, I). Separação dos poderes: princípio "
        "fundamental (art. 2º). Garantia do desenvolvimento nacional: objetivo fundamental "
        "(art. 3º, II). Independência nacional: princípio das RI (art. 4º, I). Apenas a "
        "soberania é fundamento (art. 1º).<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q01-I</i>",
    ),
    (
        "[Exercício] II – São fundamentos da República Federativa do Brasil, entre outros, os "
        "valores econômicos do trabalho e da livre iniciativa e o pluripartidarismo.",
        "<b>ERRADO.</b> Dois erros: (1) são <i>valores sociais</i> (não econômicos) do trabalho "
        "e da livre iniciativa (art. 1º, IV); (2) o fundamento é <i>pluralismo político</i> "
        "(art. 1º, V), não pluripartidarismo — este está no art. 17 e não é fundamento da RFB.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q01-II</i>",
    ),
    (
        "[Exercício] III – É um dos objetivos fundamentais da República Federativa do Brasil "
        "previsto na Constituição Federal de 1988 a garantia do desenvolvimento nacional.",
        "<b>CERTO.</b> Previsto no art. 3º, II CF/88 como objetivo fundamental. Os objetivos "
        "são normas pragmáticas com verbos no infinitivo: construir, garantir, erradicar, "
        "reduzir, promover.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q01-III</i>",
    ),
    (
        "[Exercício] IV – A concessão de asilo político consiste em um direito fundamental da "
        "pessoa humana, e é protegido por cláusula pétrea.",
        "<b>ERRADO.</b> A concessão de asilo político é um <b>princípio das relações "
        "internacionais</b> (art. 4º, X CF/88), não um direito fundamental. Portanto, não "
        "integra as cláusulas pétreas do art. 60, §4º.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – A Constituição Federal de 1988 prevê expressamente a defesa da paz "
        "como um dos fundamentos da República Federativa do Brasil.",
        "<b>ERRADO.</b> A defesa da paz é um <b>princípio das relações internacionais</b> "
        "(art. 4º, VI), não fundamento da RFB (art. 1º). Os fundamentos são: soberania, "
        "cidadania, dignidade da pessoa humana, valores sociais do trabalho e da livre "
        "iniciativa, e pluralismo político.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q02-I</i>",
    ),
    (
        "[Exercício] II – A soberania e a dignidade da pessoa humana não são princípios que "
        "regem as relações internacionais da República Federativa do Brasil.",
        "<b>CERTO.</b> Soberania e dignidade da pessoa humana são <b>fundamentos da RFB</b> "
        "(art. 1º). Nas relações internacionais (art. 4º), os equivalentes são "
        "<i>independência nacional</i> e <i>prevalência dos direitos humanos</i> — "
        "nomenclaturas distintas.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q02-II</i>",
    ),
    (
        "[Exercício] III – É a eletividade dos cargos públicos a característica que define "
        "de forma essencial o regime republicano.",
        "<b>ERRADO.</b> A característica essencial da república é a <b>responsabilidade e "
        "temporariedade dos mandatos</b> (alternância do poder e prestação de contas), não "
        "a eletividade em si — há cargos eletivos em monarquias constitucionais, e cargos "
        "republicanos não eletivos (STF, por exemplo).<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q02-III</i>",
    ),
    (
        "[Exercício] IV – A criação de organizações internacionais regionais, a exemplo do "
        "MERCOSUL e da Unasul, encontra amparo na CF/88, cujo texto prevê a norma programática "
        "de que a República Federativa do Brasil deve atuar para viabilizar formação de uma "
        "comunidade de nações por meio da integração econômica, política, social e cultural "
        "dos povos da América do Sul.",
        "<b>ERRADO.</b> O art. 4º, parágrafo único refere-se à <b>América Latina</b>, não "
        "à América do Sul. São conceitos geográficos distintos: América Latina é mais ampla "
        "e inclui países que não fazem parte da América do Sul.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – O princípio democrático é compreendido como um princípio normativo "
        "multiforme. De um lado, surge como um processo de democratização da ordem política, "
        "econômica, social e cultural. De outro, revela a sua total contradição, pois associa "
        "conceitos da teoria representativa e a democracia participativa, a qual se esgota "
        "com as eleições diretas.",
        "<b>ERRADO.</b> A democracia participativa <b>não se esgota</b> com as eleições diretas "
        "— ela se concretiza também por plebiscito, referendo, ação popular e iniciativa popular. "
        "Além disso, a combinação de democracia representativa e participativa não é uma "
        "\"contradição\", mas complementação (democracia semidireta).<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q03-I</i>",
    ),
    (
        "[Exercício] II – Os Poderes Legislativo, Executivo e Judiciário são poderes da União, "
        "dependentes e harmônicos entre si.",
        "<b>ERRADO.</b> O art. 2º CF/88 estabelece que os Poderes são <b>independentes e "
        "harmônicos</b> entre si, não dependentes. A independência garante o sistema de freios "
        "e contrapesos; a harmonia assegura o funcionamento coordenado.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q03-II</i>",
    ),
    (
        "[Exercício] III – O constituinte originário alçou o repúdio ao terrorismo a objetivo "
        "fundamental da República Federativa do Brasil.",
        "<b>ERRADO.</b> O repúdio ao terrorismo (e ao racismo) é um <b>princípio das relações "
        "internacionais</b> (art. 4º, VIII), não objetivo fundamental (art. 3º). Os objetivos "
        "fundamentais usam verbos no infinitivo: construir, garantir, erradicar, reduzir, "
        "promover.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q03-III</i>",
    ),
    (
        "[Exercício] IV – A CF/88 atribui apenas ao Congresso Nacional a competência para "
        "autorizar referendo e convocar plebiscito.",
        "<b>CERTO.</b> Conforme o art. 49, XV CF/88, é competência exclusiva do "
        "<b>Congresso Nacional</b> autorizar referendo e convocar plebiscito. Nenhum outro "
        "órgão tem essa atribuição — é competência indelegável do Poder Legislativo federal.<br>"
        "<i>Fonte: Exercícios objetivos – DI Rodada 01 Mar/2025, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Interno::Estado Democrático de Direito",
        "Direito Interno - Estado Democrático de Direito.apkg",
        CARDS,
    )
