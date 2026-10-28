#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Abril/2025).

Tema: Extradição e Cooperação Penal (Itens 20 e 35 do Edital CACD).

Fontes:
  - Anotações: Extradição e Cooperação Penal.md
  - Material do professor: Direito Internacional_Rodada 01_Abril_2025_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Abril_2025.pdf
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


EXTRADICAO = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("A entrega (surrender) de um indivíduo ao Tribunal Penal Internacional "
     "equivale, para fins jurídicos, a uma extradição, de modo que sua "
     "tramitação no Brasil segue o processo trifásico da Lei de Migração, "
     "com juízo de delibação do STF.",
     "<b>ERRADO.</b> Extradição e entrega não se confundem: a extradição é "
     "a remessa a outro <b>Estado soberano</b>; a entrega (<i>surrender</i>, "
     "art. 102 do Estatuto de Roma) é a remessa ao <b>TPI</b>. O próprio "
     "STF as trata como institutos distintos. [Anotações da aula; Rodada "
     "01/Abr.2025]"),

    ("Para que o STF autorize a extradição, o Estado requerente deve já "
     "ter proferido sentença penal condenatória contra o extraditando, "
     "pois a extradição instrutória só é cabível para réus em processos "
     "em fase de execução.",
     "<b>ERRADO.</b> Há duas modalidades: a <b>instrutória</b> (responder a "
     "processo criminal no Estado requerente) e a <b>executória</b> "
     "(cumprir sentença já proferida). Não se exige condenação prévia para "
     "o STF autorizar a extradição. [Anotações da aula; Rodada 01/Abr.2025]"),

    ("Um estrangeiro que, em seu país, integrou ação armada voltada a "
     "derrubar um regime ditatorial não pode ser extraditado, pois a "
     "Constituição veda a extradição por crime político e de opinião, "
     "conceitos que o STF identifica com atos contra regimes autoritários.",
     "<b>CERTO.</b> Art. 5º, LII, CF/88. A definição de crime político foi "
     "construída pela jurisprudência do STF: atos praticados para "
     "enfraquecer ou encerrar regime de exceção e restabelecer valores "
     "democráticos. [Anotações da aula; Rodada 01/Abr.2025]"),

    ("No sistema belga adotado pelo Brasil, o STF reexamina o mérito do "
     "crime praticado no exterior para garantir os direitos do "
     "extraditando; se julgar procedente o pedido, o Presidente da "
     "República fica obrigado a entregar o indivíduo ao Estado requerente.",
     "<b>ERRADO.</b> O STF não julga o crime: faz juízo de delibação "
     "(contenciosidade limitada), verificando requisitos formais. Seu "
     "juízo <b>negativo vincula</b> o Presidente, mas o <b>positivo não "
     "o obriga</b>: a entrega é ato discricionário e fundamentado do chefe "
     "de Estado. [Anotações da aula; Rodada 01/Abr.2025]"),

    ("A transferência de execução de pena busca evitar a impunidade de "
     "quem foi condenado no exterior e se encontra no Brasil sem poder ser "
     "extraditado, exigindo que o condenado seja nacional ou tenha "
     "residência habitual ou vínculo pessoal no país, que a sentença tenha "
     "transitado em julgado e que haja tratado ou reciprocidade.",
     "<b>CERTO.</b> Arts. 100 a 102 da Lei de Migração. O caso típico é o "
     "brasileiro nato condenado no exterior (Robinho, Itália). O STJ "
     "homologa a sentença, só verificando requisitos formais, e a Justiça "
     "Federal de 1º grau executa a pena. [Anotações da aula; Rodada "
     "01/Abr.2025]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Abr/2025) ───────────────

    ("01-I – Paula, brasileira naturalizada, ingressou no serviço público "
     "federal mediante aprovação em concurso público. Ocorre que, após "
     "regular ação penal que tramitava perante a justiça americana, "
     "restou comprovado seu envolvimento em tráfico ilícito de "
     "entorpecentes naquele país. Nesse caso, considerando que o tráfico "
     "foi cometido depois de sua naturalização, Paula não poderá ser "
     "extraditada. (C/E?)",
     "<b>ERRADO.</b> O brasileiro naturalizado pode ser extraditado em duas "
     "hipóteses (art. 5º, LI): crime comum anterior à naturalização, ou "
     "<b>tráfico ilícito de entorpecentes a qualquer tempo</b>, antes ou "
     "depois da naturalização. [Exercício Q01-I, Rodada 01 Abr/2025]"),

    ("01-II – A jurisprudência do STF veda a extradição de estrangeiro que "
     "tiver filho brasileiro sob sua guarda ou dependência econômica ou "
     "socioafetiva. (C/E?)",
     "<b>ERRADO.</b> A Súmula 421 do STF afirma que ter cônjuge ou filho "
     "brasileiro <b>não impede</b> a extradição. A guarda ou dependência de "
     "filho brasileiro impede apenas a <b>expulsão</b> (art. 55, II, \"a\", "
     "da Lei 13.445/2017). [Exercício Q01-II, Rodada 01 Abr/2025]"),

    ("01-III – Ainda que o estrangeiro manifeste de modo inequívoco o seu "
     "desejo de ser extraditado, não ficarão dispensadas as formalidades "
     "inerentes ao processo de extradição. (C/E?)",
     "<b>CERTO.</b> O STF atua como garantidor de direitos fundamentais "
     "indisponíveis e irrenunciáveis do extraditando (ex.: prescrição, "
     "<i>bis in idem</i>, tribunais de exceção); a vontade dele não "
     "dispensa as etapas. Nada impede, porém, que ele se apresente "
     "voluntariamente ao Estado requerente. [Exercício Q01-III, Rodada 01 "
     "Abr/2025]"),

    ("01-IV – A extradição poderá ser concedida quando o governo "
     "requerente se fundamentar em tratado ou ainda quando prometer ao "
     "Brasil a reciprocidade, ficando o Estado brasileiro impedido de "
     "realizar, no primeiro caso, a negativa do pedido de extradição se "
     "existir decisão favorável do STF. (C/E?)",
     "<b>ERRADO.</b> Com tratado, o Brasil não pode fazer <b>negativa "
     "sumária</b> na 1ª etapa, mas, mesmo com decisão favorável do STF, a "
     "entrega final continua sendo decisão <b>discricionária</b> do "
     "Presidente (3ª etapa). Com mera promessa de reciprocidade, a "
     "negativa sumária é possível. [Exercício Q01-IV, Rodada 01 Abr/2025]"),

    ("02-I – O acordo de extradição do Mercosul não prevê a denegação da "
     "extradição por delitos políticos, em virtude do paradigma da "
     "confiança que deve imperar na cooperação jurídica internacional em "
     "blocos de integração econômica. (C/E?)",
     "<b>ERRADO.</b> Nenhum tratado de extradição, bilateral ou "
     "multilateral, pode prever a extradição por crime político ou de "
     "opinião para o Brasil, por força do art. 5º, LII, CF/88; norma "
     "assim seria inconstitucional. [Exercício Q02-I, Rodada 01 Abr/2025]"),

    ("02-III – A Emenda Constitucional no 45/2004 atribuiu ao Superior "
     "Tribunal de Justiça a competência para homologar sentenças "
     "estrangeiras e conceder exequatur a cartas rogatórias, em "
     "substituição ao Supremo Tribunal Federal (STF). Assim, o STF não "
     "realiza mais juízos de delibação em nenhum tipo de processo. (C/E?)",
     "<b>ERRADO.</b> A EC 45/2004 transferiu ao STJ a homologação de "
     "sentenças estrangeiras e o <i>exequatur</i> a cartas rogatórias, "
     "mas o STF conserva o juízo de delibação nos pedidos de "
     "<b>extradição</b> (art. 102, I, \"g\", CF/88). [Exercício Q02-III, "
     "Rodada 01 Abr/2025]"),

    ("03-I – No pedido de transferência da execução da pena aplicada por "
     "autoridade estrangeira, após exame da presença dos pressupostos "
     "formais de admissibilidade exigidos em lei ou em tratado, "
     "encaminhado ao STJ para decisão quanto à homologação, a execução "
     "penal será da competência da Justiça Federal. (C/E?)",
     "<b>CERTO.</b> Procedimento em três etapas: o Executivo recebe o "
     "pedido (tratado ou reciprocidade) e o envia ao STJ; o STJ homologa "
     "(delibação); a execução fica a cargo da Justiça Federal de 1º grau "
     "(art. 102). [Exercício Q03-I, Rodada 01 Abr/2025]"),

    ("03-II – Uma vez que o brasileiro nato não pode ser extraditado, o "
     "STJ adotou o entendimento de que é vedada a homologação de sentença "
     "estrangeira que tenha condenado tal indivíduo por crime praticado "
     "no exterior. (C/E?)",
     "<b>ERRADO.</b> É justamente porque o brasileiro nato não pode ser "
     "extraditado que se admite a transferência de execução de pena, para "
     "evitar impunidade. A nacionalidade originária não consta entre os "
     "requisitos impeditivos do art. 100. [Exercício Q03-II, Rodada 01 "
     "Abr/2025]"),

    ("03-III – Na cooperação jurídica internacional em matéria penal, a "
     "transferência de execução de pena exige, além da anuência do Estado "
     "sentenciador e do Estado recebedor, a concordância do indivíduo "
     "condenado. (C/E?)",
     "<b>ERRADO.</b> A manifestação de vontade do condenado é exigida na "
     "<b>transferência de pessoa condenada</b> (preso que já cumpre pena "
     "no exterior, art. 104, V), de caráter humanitário. A transferência "
     "de <b>execução de pena</b> (arts. 100–102) não a exige. [Exercício "
     "Q03-III, Rodada 01 Abr/2025]"),

    ("03-IV – A aplicação do instituto de transferência de pessoa "
     "condenada (transferência de presos) apresenta-se como um mecanismo "
     "no qual apenas o Poder Executivo atua, de modo que é prescindível a "
     "homologação de sentença estrangeira pelo STJ. (C/E?)",
     "<b>CERTO.</b> Na transferência de pessoa condenada todo o trâmite "
     "ocorre no Poder Executivo, sem juízo de delibação do STJ; a "
     "homologação pelo STJ é própria da transferência de execução de "
     "pena. [Exercício Q03-IV, Rodada 01 Abr/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Extradição e Cooperação Penal",
        "Direito Internacional - Extradição e Cooperação Penal.apkg",
        EXTRADICAO,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
