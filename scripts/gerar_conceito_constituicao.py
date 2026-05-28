#!/usr/bin/env python3
"""Gera deck Anki: Direito Interno - Conceito e Classificação da Constituição"""

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


CONCEITO_CONSTITUICAO = [
    # ── CONCEITO E SUPREMACIA ──────────────────────────────────────────────────
    (
        "O que é uma Constituição no conceito moderno (séc. XVIII)?",
        "Documento jurídico de <b>maior hierarquia</b> no ordenamento nacional, elaborado por representantes do povo, que <b>organiza os poderes do Estado</b> e <b>limita o poder estatal</b> (garantias fundamentais).<br>"
        "Marcos: EUA 1787 e França 1791.<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "O que o constitucionalismo moderno acrescentou ao papel da constituição (em relação à Idade Média)?",
        "Na Idade Média a constituição apenas <b>organizava</b> o poder estatal. A partir do séc. XVIII passou também a <b>limitar</b> o poder, assegurando direitos e garantias fundamentais ao povo.<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "O que é o Princípio da Supremacia Formal da Constituição?",
        "Todas as normas constitucionais — inclusive as que não versam sobre organização/limitação do Estado — gozam de <b>máxima hierarquia</b> no ordenamento, garantida pelo processo especial de elaboração (não pelo conteúdo).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),

    # ── 7 CRITÉRIOS DE CLASSIFICAÇÃO ──────────────────────────────────────────
    (
        "Critério 01 — Mutabilidade: como a CF/88 é classificada? Quais as outras opções?",
        "<b>Rígida</b>: exige processo mais solene e difícil para alteração (emendas = art. 60, regra 2-2-⅗).<br>"
        "Também existe: <b>flexível</b> (alterável por lei ordinária) e <b>semirrígida</b> (parte exige emenda, parte não — ex: Constituição do Império 1824).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 02 — Origem: como a CF/88 é classificada? Quais as outras opções?",
        "<b>Promulgada/democrática</b>: elaborada com participação indireta do povo via representantes eleitos para a Assembleia Constituinte.<br>"
        "Também existe: <b>outorgada</b> (sem participação popular, regimes autoritários) e <b>cesarista</b> (elaborada sem participação, mas submetida a referendo/plebiscito — ex: czars russos).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 03 — Forma: como a CF/88 é classificada?",
        "<b>Escrita/instrumental e codificada</b>: normas constitucionais reunidas em um único documento escrito.<br>"
        "Também existe: <b>não escrita/costumeira</b> (maioria das normas advém dos costumes — ex: Inglaterra/Magna Carta 1215) e <b>escrita não codificada</b> (normas em documentos distintos — argumento do bloco de constitucionalidade na CF/88).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 04 — Modo de elaboração: como a CF/88 é classificada?",
        "<b>Dogmática</b>: elaborada com base nos dogmas da ciência política predominantes no momento histórico por um órgão constituinte específico (ex: separação de poderes, garantias fundamentais).<br>"
        "Também existe: <b>histórica</b> (sedimentação gradual ao longo do tempo, sem órgão constituinte — acompanha a forma costumeira; ex: Inglaterra).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 05 — Conteúdo: como a CF/88 é classificada? Qual a diferença entre normas materiais e formais?",
        "<b>Formal</b>: contém dois tipos de normas:<br>"
        "• <b>Materialmente constitucionais</b>: organizam/limitam o poder estatal (ex: art. 2 — separação dos poderes).<br>"
        "• <b>Formalmente constitucionais</b>: estão na CF mas poderiam ser lei ordinária (ex: art. 242 — Colégio Pedro II).<br>"
        "Também existe: <b>material</b> (só normas típicas do DC — ex: EUA 1787).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 06 — Extensão: como a CF/88 é classificada?",
        "<b>Analítica</b>: grande extensão (250 artigos). Geralmente acompanha o conteúdo formal (mais matérias constitucionalizadas).<br>"
        "Também existe: <b>sintética</b> (ex: EUA — 7 artigos + 27 emendas). Geralmente acompanha o conteúdo material.<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Critério 07 — Finalidade: como a CF/88 é classificada?",
        "<b>Dirigente</b>: além de organizar/limitar o poder, dirige o Estado para objetivos sociais de longo prazo — direitos de 2ª geração (saúde, educação, moradia) concretizados por programas estatais (SUS, Prouni, MCMV).<br>"
        "Também existe: <b>garantia</b> (Estado liberal mínimo — apenas direitos individuais de 1ª geração, sem mandamentos sociais — ex: EUA 1787).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "O que é a Constituição Cesarista? Dê um exemplo.",
        "Constituição elaborada <b>sem participação popular</b> na construção do texto, mas submetida a <b>referendo/plebiscito</b> para aprovação. O povo não redige, mas pode votar contra a adoção.<br>"
        "Ex: czars russos criavam o texto constitucional e depois enviavam ao povo para votação.<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),
    (
        "Qual a relação típica entre os critérios de conteúdo e extensão das constituições?",
        "Constituições de <b>conteúdo material</b> (só normas típicas do DC) tendem a ser <b>sintéticas</b> (menos matérias → texto menor).<br>"
        "Constituições de <b>conteúdo formal</b> (normas típicas + outras) tendem a ser <b>analíticas</b> (mais matérias → texto maior).<br>"
        "<i>Fonte: Anotações – Conceito e Classificação da Constituição</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Sob o critério da mutabilidade, também denominado alterabilidade, são consideradas "
        "como rígidas as constituições que exigem, para sua alteração, um processo legislativo mais solene e "
        "dificultoso que o processo para alteração das normas não constitucionais.",
        "<b>CERTO.</b> Constituição rígida é exatamente aquela cujo processo de alteração é mais solene e "
        "dificultoso que o processo legislativo ordinário. Na CF/88: art. 60, regra 2-2-⅗.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q01-I</i>",
    ),
    (
        "[Exercício] II – A rigidez das constituições é atributo absolutamente independente do princípio da "
        "supremacia da constituição.",
        "<b>ERRADO.</b> Há relação direta: a rigidez é um dos <b>fundamentos da supremacia formal</b>. "
        "Justamente porque o processo de alteração é mais difícil, as normas constitucionais ocupam posição "
        "hierárquica superior às demais.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q01-II</i>",
    ),
    (
        "[Exercício] III – Constituição dogmática é definida como aquela resultante de um trabalho "
        "legislativo específico, refletindo as ideias e conceitos de um momento específico da sociedade.",
        "<b>CERTO.</b> A constituição dogmática é elaborada por um órgão constituinte específico, com base "
        "nos dogmas da ciência política predominantes naquele momento histórico.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q01-III</i>",
    ),
    (
        "[Exercício] IV – Quanto à estabilidade, a Constituição flexível não se compatibiliza com a forma "
        "escrita, ainda que seu eventual texto admitisse livre alteração do conteúdo por meio de processo "
        "legislativo ordinário.",
        "<b>ERRADO.</b> Flexibilidade (critério de mutabilidade) e forma escrita (critério de forma) são "
        "critérios <b>independentes</b>. Uma constituição pode ser simultaneamente escrita e flexível.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – O constitucionalismo moderno, identificado nas Constituições dos Estados Unidos da "
        "América de 1787 e da França de 1791, caracteriza-se pela vinculação à ideia de constituição escrita "
        "e rígida, com força para limitar e vincular os órgãos do poder político.",
        "<b>CERTO.</b> O constitucionalismo moderno (séc. XVIII) consagrou constituições escritas e rígidas "
        "como instrumentos de organização E limitação do poder estatal, vinculando todos os órgãos públicos.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q02-I</i>",
    ),
    (
        "[Exercício] II – As Constituições costumeiras têm como característica fundamental o surgimento "
        "informal, originando-se da sociedade; ao passo que a Constituição histórica é aquela resultante da "
        "gradativa sedimentação jurídica de um povo, por meio de suas tradições.",
        "<b>CERTO.</b> Costumeira (critério de forma) = normas constitucionais advêm dos costumes e "
        "tradições. Histórica (critério de modo de elaboração) = sedimentação gradual ao longo do tempo. "
        "As duas classificações geralmente coexistem (ex: Inglaterra).<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q02-II</i>",
    ),
    (
        "[Exercício] III – Do ponto de vista material, o que vai importar para definirmos se uma norma tem "
        "caráter constitucional ou não será o seu conteúdo, pouco importando a forma pela qual foi essa "
        "norma introduzida no ordenamento jurídico.",
        "<b>CERTO.</b> No critério de conteúdo material, são constitucionais as normas que versam sobre "
        "organização/limitação do poder estatal, independentemente de estarem ou não no texto da "
        "constituição formal.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q02-III</i>",
    ),
    (
        "[Exercício] IV – O conceito de Constituição em sentido formal é apresentado como sendo um documento "
        "escrito e solene que positiva as normas jurídicas superiores da comunidade do Estado, elaboradas "
        "por um processo constituinte específico.",
        "<b>CERTO.</b> Constituição em sentido formal = documento escrito e solene, elaborado por processo "
        "constituinte específico. Todas as normas nele inseridas são constitucionais pela <b>forma</b> "
        "(posição no texto), não pelo conteúdo.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – A ideia de Constituição dirigente determina que, além de organizar e limitar o "
        "poder, a Constituição também preordena a atuação governamental por meio de planos e programas.",
        "<b>CERTO.</b> A constituição dirigente (critério de finalidade) vai além da organização/limitação "
        "do poder: dirige o Estado para objetivos sociais de longo prazo por meio de direitos de 2ª geração "
        "e programas estatais (ex: SUS, Prouni).<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q03-I</i>",
    ),
    (
        "[Exercício] II – As constituições do tipo analítico, como é o caso da Constituição Federal de 1988, "
        "além de retirarem da disposição do legislador ordinário um conjunto bem maior de matérias, em geral "
        "são também mais frequentemente reformadas, pois quanto mais regras contemplam, mais se torna difícil "
        "a atualização da constituição mediante o processo legislativo ordinário e a interpretação.",
        "<b>CERTO.</b> Constituições analíticas constitucionalizam mais matérias — o que exige mais emendas "
        "para atualização, pois essas matérias saem do alcance do legislador ordinário.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q03-II</i>",
    ),
    (
        "[Exercício] III – Quanto à forma, considera-se a CF/88 um texto promulgado, haja vista que suas "
        "normas constitucionais foram adotadas por um órgão constituinte composto por representantes "
        "legítimos do povo.",
        "<b>ERRADO.</b> 'Promulgada' é classificação pelo critério de <b>origem</b>, não de forma. "
        "Quanto à <b>forma</b>, a CF/88 é <b>escrita/instrumental e codificada</b>. O enunciado confunde "
        "os dois critérios.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q03-III</i>",
    ),
    (
        "[Exercício] IV – A Constituição Federal de 1988 pode ser classificada corretamente como escrita, "
        "analítica, garantia, dogmática e rígida.",
        "<b>ERRADO.</b> A CF/88 é <b>dirigente</b> (não garantia) quanto à finalidade. A constituição de "
        "garantia visa apenas o Estado liberal mínimo, sem direitos sociais como mandamento constitucional "
        "(ex: EUA 1787). A CF/88 possui extenso rol de direitos sociais e objetivos de longo prazo.<br>"
        "<i>Fonte: Exercícios objetivos – Direito Interno Rodada 01 Fev/2024, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Direito Interno :: Conceito e Classificação da Constituição",
        "Direito Interno - Conceito e Classificacao da Constituicao.apkg",
        CONCEITO_CONSTITUICAO,
    )
