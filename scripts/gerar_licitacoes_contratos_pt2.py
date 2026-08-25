#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Jan/2026).

Tema: Licitações e Contratos Administrativos — modalidades de licitação e
contratação direta (Item 10 do Edital CACD).

Fontes:
  - Anotações: Licitações e Contratos Administrativos - Parte 2.md
  - Material do professor: Direito Interno_Rodada 01_Janeiro_2026_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Janeiro_2026.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelreichelt/Desktop/cacd-learning/anki/decks/direito interno"
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


LICITACOES_CONTRATOS_PT2 = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("A modalidade de leilão, destinada à alienação de bens imóveis ou de "
     "bens móveis inservíveis ou legalmente apreendidos, admite dois "
     "critérios de julgamento possíveis — maior lance ou maior desconto —, "
     "e o leiloeiro oficial designado para conduzi-lo deve ser previamente "
     "credenciado pela Administração, dispensada a necessidade de licitação "
     "para sua escolha.",
     "<b>ERRADO.</b> Dois erros: (i) o leilão adota um <b>único</b> "
     "critério de julgamento — maior lance; (ii) quando a Administração "
     "opta por leiloeiro oficial, ele deve ser selecionado mediante "
     "credenciamento <b>ou</b> licitação na modalidade pregão — a licitação "
     "não é dispensada, é apenas uma alternativa ao credenciamento. "
     "[Anotações da aula; Rodada 01/Jan.2026, p.4]"),

    ("Nos termos da Lei nº 14.133/2021, é dispensável a licitação para "
     "contratação que envolva valores inferiores a R$ 100.000,00 no caso de "
     "obras e serviços de engenharia, e valores inferiores a R$ 50.000,00 "
     "no caso de outros serviços e compras.",
     "<b>CERTO.</b> Art. 75, I e II, da Lei nº 14.133/2021 — hipóteses de "
     "dispensa de licitação em razão do baixo valor da contratação. "
     "[Anotações da aula; Rodada 01/Jan.2026, p.17]"),

    ("Na hipótese de contratação direta realizada de modo indevido, ainda "
     "que comprovados dolo, fraude ou erro grosseiro do agente público "
     "responsável, apenas este responderá pelo dano causado ao erário, não "
     "se estendendo tal responsabilidade ao particular contratado.",
     "<b>ERRADO.</b> O art. 73 da Lei nº 14.133/2021 prevê que, nesse caso, "
     "o <b>contratado</b> e o <b>agente público</b> responsável respondem "
     "<b>solidariamente</b> pelo dano causado ao erário, sem prejuízo de "
     "outras sanções legais cabíveis. [Anotações da aula; Rodada "
     "01/Jan.2026, p.12]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jan/2026) ──────────────

    ("I – Na contratação de obra pública, o gestor ainda pode optar por "
     "seguir a Lei n.º 8.666/1993 ou a Lei n.º 14.133/2021, conforme o "
     "permitido em período de transição. (C/E?)",
     "<b>ERRADO.</b> O art. 193, II, \"a\", da Lei nº 14.133/2021 revogou "
     "a Lei nº 8.666/1993 em 30/12/2023. Desde então, não há mais opção "
     "entre as duas leis — a Administração deve aplicar apenas a Lei nº "
     "14.133/2021. [Exercício Q01-I, Rodada 01 Jan/2026]"),

    ("II – Excepcionalmente, a administração pública poderá adquirir, desde "
     "que de forma justificada, artigos de luxo ou de qualidade superior "
     "às finalidades a que se destinam. (C/E?)",
     "<b>ERRADO.</b> O art. 20 da Lei nº 14.133/2021 prevê que a "
     "Administração deve adquirir somente itens de consumo de qualidade "
     "<b>comum</b> — a aquisição de produtos de luxo é vedada, sem exceção "
     "por justificativa. [Exercício Q01-II, Rodada 01 Jan/2026]"),

    ("III – São previstas na lei as seguintes modalidades de licitação: "
     "pregão, concorrência, concurso, convite, leilão, tomada de preços e "
     "diálogo competitivo. (C/E?)",
     "<b>ERRADO.</b> O art. 28 prevê apenas 5 modalidades: pregão, "
     "concorrência, concurso, leilão e diálogo competitivo. Convite e "
     "tomada de preços foram <b>extintas</b> com a revogação da Lei nº "
     "8.666/1993. [Exercício Q01-III, Rodada 01 Jan/2026]"),

    ("IV – Não é permitido ao administrador público, com justificativa no "
     "interesse público e na particularidade do caso concreto, combinar "
     "duas das modalidades de licitação previstas em lei. (C/E?)",
     "<b>CERTO.</b> O art. 28, §2º, da Lei nº 14.133/2021 proíbe a "
     "Administração de criar novas modalidades ou combinar as modalidades "
     "existentes, sem exceção por justificativa de interesse público. "
     "[Exercício Q01-IV, Rodada 01 Jan/2026]"),

    ("I – A modalidade de licitação pregão deve ser adotada sempre que o "
     "objeto possuir padrões de desempenho e qualidade que possam ser "
     "objetivamente definidos pelo edital de licitação, por meio de "
     "especificações usuais de mercado. (C/E?)",
     "<b>CERTO.</b> É a definição de bem/serviço comum (art. 29) — cuja "
     "contratação é obrigatoriamente feita por pregão, modalidade vinculada "
     "sempre que houver essa característica. [Exercício Q02-I, Rodada 01 "
     "Jan/2026]"),

    ("II – O pregão é inaplicável à contratação de serviços técnicos "
     "especializados de natureza predominantemente intelectual, salvo em "
     "casos legalmente excepcionados que envolvam determinados serviços de "
     "engenharia. (C/E?)",
     "<b>CERTO.</b> Regra geral do art. 29, parágrafo único: pregão não se "
     "aplica a serviços técnicos intelectuais nem a obras/serviços de "
     "engenharia; exceção: serviço COMUM de engenharia (art. 6º, XXI, "
     "\"a\"). [Exercício Q02-II, Rodada 01 Jan/2026]"),

    ("III – Motivada por estudos preparatórios que antecedem a elaboração "
     "do edital, a Administração Pública pode, excepcionalmente, com "
     "fundamento nas especificidades do objeto a ser contratado, decidir "
     "empregar a concorrência como modalidade de licitação para aquisição "
     "de bens e serviços comuns. (C/E?)",
     "<b>ERRADO.</b> Para bens e serviços comuns, o pregão é modalidade "
     "<b>vinculada e obrigatória</b> (art. 29, caput) — não há "
     "discricionariedade para a Administração optar pela concorrência, "
     "ainda que motivada por estudos preparatórios. [Exercício Q02-III, "
     "Rodada 01 Jan/2026]"),

    ("IV – O diálogo competitivo, modalidade introduzida pela Lei n.º "
     "14.133/2021, destina-se, entre outras hipóteses, a contratações em "
     "que a administração pública não consegue definir, com precisão "
     "suficiente, as especificações técnicas relativas ao objeto que "
     "pretende contratar. (C/E?)",
     "<b>CERTO.</b> É uma das hipóteses do art. 32 que autorizam o emprego "
     "do diálogo competitivo, modalidade inovadora da Lei nº 14.133/2021. "
     "[Exercício Q02-IV, Rodada 01 Jan/2026]"),

    ("I – A contratação direta por inexigibilidade de licitação é admitida "
     "diante da impossibilidade de competição, como na contratação de "
     "profissional do setor artístico consagrado pela crítica ou pela "
     "opinião pública. (C/E?)",
     "<b>CERTO.</b> Art. 74, II, da Lei nº 14.133/2021 — hipótese clássica "
     "de inviabilidade de competição (inexigibilidade). [Exercício Q03-I, "
     "Rodada 01 Jan/2026]"),

    ("II – A licitação será dispensável no caso de aquisição de "
     "equipamentos fornecidos exclusivamente por determinada empresa. "
     "(C/E?)",
     "<b>ERRADO.</b> Fornecedor exclusivo configura hipótese de "
     "<b>inexigibilidade</b> (art. 74, I) — inviabilidade de competição —, "
     "não de dispensa (que pressupõe possibilidade de competição). "
     "[Exercício Q03-II, Rodada 01 Jan/2026]"),

    ("III – A inexigibilidade de licitação ocorre quando a administração "
     "pública decide contratar diretamente por motivos de conveniência, "
     "desde que o valor esteja abaixo dos limites legais. (C/E?)",
     "<b>ERRADO.</b> Isso descreve a <b>dispensa</b> de licitação (juízo de "
     "conveniência/oportunidade, rol taxativo do art. 75). A "
     "inexigibilidade (art. 74) decorre da inviabilidade de competição, não "
     "de um juízo de conveniência. [Exercício Q03-III, Rodada 01 Jan/2026]"),

    ("IV – A Lei n.º 14.133/2021 ampliou a discricionariedade da "
     "administração ao prever hipóteses de dispensa implícita, isto é, "
     "situações em que a ausência de competição justifica a contratação "
     "direta, havendo a possibilidade de se criarem novas hipóteses de "
     "dispensa de licitação, desde que motivadas. (C/E?)",
     "<b>ERRADO.</b> O rol de <b>dispensa</b> (art. 75) é taxativo e "
     "exaustivo — não existem hipóteses implícitas de dispensa. Hipóteses "
     "implícitas são reconhecidas apenas na <b>inexigibilidade</b> (art. 74, "
     "rol exemplificativo), e não na dispensa. [Exercício Q03-IV, Rodada 01 "
     "Jan/2026]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Licitações e Contratos Administrativos - Parte 2",
        "Direito Interno - Licitações e Contratos Administrativos - Parte 2.apkg",
        LICITACOES_CONTRATOS_PT2,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
