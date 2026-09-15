#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Set/2024).

Tema: Improbidade Administrativa (Item 12 do Edital CACD).

Fontes:
  - Anotações: Improbidade Administrativa.md
  - Material do professor: Direito Interno_Rodada 01_Setembro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Setembro_2024.pdf
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


IMPROBIDADE_ADMINISTRATIVA = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Dentre as sanções previstas no art. 37, §4º, da CF/88 para os atos de "
     "improbidade administrativa, encontra-se a cassação dos direitos "
     "políticos do agente condenado, medida que se distingue da suspensão "
     "por seu caráter definitivo e mais gravoso.",
     "<b>ERRADO.</b> A CF/88 só prevê <b>SUSPENSÃO</b> dos direitos "
     "políticos em improbidade — nunca perda ou cassação. O art. 15, "
     "\"caput\", CF/88 VEDA a cassação de direitos políticos em QUALQUER "
     "hipótese. [Anotações da aula; Rodada 01/Set.2024]"),

    ("As sanções aplicáveis aos atos de improbidade administrativa "
     "possuem os mesmos limites máximos de suspensão de direitos "
     "políticos e de proibição de contratar com o poder público, "
     "independentemente de o ato configurar enriquecimento ilícito, dano "
     "ao erário ou mera violação aos princípios da Administração Pública.",
     "<b>ERRADO.</b> Os tetos VARIAM conforme o artigo: <b>art. 9º</b> "
     "(enriquecimento ilícito) — suspensão até 14 anos; <b>art. 10</b> "
     "(dano ao erário) — até 12 anos; <b>art. 11</b> (atenta contra "
     "princípios) — SEM suspensão de direitos políticos, apenas multa "
     "civil (até 24x a remuneração) e proibição de contratar por até 4 "
     "anos. [Anotações da aula; Rodada 01/Set.2024]"),

    ("A ação de improbidade administrativa, por envolver a tutela do "
     "patrimônio público, pode ser utilizada para promover o controle de "
     "legalidade de políticas públicas e para a proteção de interesses "
     "difusos e coletivos relacionados ao meio ambiente, de forma análoga "
     "a uma ação civil pública.",
     "<b>ERRADO.</b> O art. 17-D, incluído pela Lei 14.230/2021, define a "
     "ação de improbidade como REPRESSIVA/sancionatória, de caráter "
     "PESSOAL — é expressamente VEDADO seu uso para controle de "
     "legalidade de políticas públicas ou proteção de interesses difusos, "
     "coletivos ou individuais homogêneos em geral. [Anotações da aula; "
     "Rodada 01/Set.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Set/2024) ──────────────

    ("01-I – A ausência de ato doloso com fim ilícito no exercício de "
     "função pública afasta de imediato a responsabilidade por ato de "
     "improbidade administrativa. (C/E?)",
     "<b>CERTO.</b> Improbidade exige DOLO ESPECÍFICO (art. 1º, §§1º-3º) "
     "— sem ato doloso com fim ilícito, não há responsabilização. "
     "[Exercício Q01-I, Rodada 01 Set/2024]"),

    ("01-II – Como regra, não pode haver posse de servidor público sem "
     "que ele apresente a declaração de imposto de renda transmitida à "
     "Receita Federal, a qual deve ser atualizada todos os anos. (C/E?)",
     "<b>CERTO.</b> Art. 13 — declaração de IR é condição de posse, "
     "atualizada anualmente; a omissão ou falsidade gera DEMISSÃO. "
     "[Exercício Q01-II, Rodada 01 Set/2024]"),

    ("01-III – O agente político está excluído do conceito de agente "
     "público adotado pela Lei n.º 8.429/1992. (C/E?)",
     "<b>ERRADO.</b> O art. 2º adota conceito AMPLO, que inclui "
     "expressamente o agente político (exceção única: Presidente da "
     "República, sujeito a impeachment). [Exercício Q01-III, Rodada 01 "
     "Set/2024]"),

    ("01-IV – Um ato de improbidade administrativa praticado por servidor "
     "público não pode ser simultaneamente enquadrado como um ilícito "
     "administrativo, o que exime a autoridade competente de instaurar "
     "qualquer procedimento para apuração de responsabilidade de natureza "
     "disciplinar. (C/E?)",
     "<b>ERRADO.</b> As instâncias civil (improbidade), penal e "
     "administrativa (PAD) são INDEPENDENTES e cumuláveis — o mesmo fato "
     "pode gerar responsabilização nas 3. [Exercício Q01-IV, Rodada 01 "
     "Set/2024]"),

    ("02-I – Segundo entendimento do STF, a partir das recentes alterações "
     "na legislação que dispõe sobre improbidade, deixou de existir, no "
     "ordenamento jurídico brasileiro, a tipificação para atos culposos de "
     "improbidade administrativa, de maneira que a nova regra retroage "
     "para absolver pessoas que já tenham sido condenadas em sentença com "
     "trânsito em julgado. (C/E?)",
     "<b>ERRADO.</b> A extinção da modalidade culposa (Lei 14.230/2021) é "
     "<b>IRRETROATIVA</b> — não beneficia quem já tem condenação "
     "transitada em julgado, pois a lei é CIVIL, não penal (não se aplica "
     "o art. 5º, XL, CF/88). [Exercício Q02-I, Rodada 01 Set/2024]"),

    ("02-II – A legitimidade para a propositura de ação por ato de "
     "improbidade administrativa é disjuntiva e concorrente entre a "
     "fazenda pública e o Ministério Público. (C/E?)",
     "<b>CERTO.</b> STF (ADI 7.043): legitimidade concorrente e "
     "disjuntiva — MP e Fazenda Pública podem atuar isoladamente. "
     "[Exercício Q02-II, Rodada 01 Set/2024]"),

    ("02-III – A autoridade que identificar indícios de atos ou fatos de "
     "improbidade administrativa deve representar ao tribunal de contas "
     "competente para a adoção das providências necessárias. (C/E?)",
     "<b>ERRADO.</b> Art. 7º — a representação vai ao <b>Ministério "
     "Público</b>, não ao Tribunal de Contas (que não tem legitimidade "
     "para ajuizar ação de improbidade). [Exercício Q02-III, Rodada 01 "
     "Set/2024]"),

    ("02-IV – Caso haja prova suficiente dos atos de improbidade e as "
     "respectivas punições estejam prescritas, a ação judicial poderá "
     "prosseguir pelo pedido de ressarcimento ao erário, o qual é "
     "imprescritível. (C/E?)",
     "<b>CERTO.</b> Prazo geral de 8 anos (art. 23) para as sanções, mas o "
     "ressarcimento ao erário por ato DOLOSO é IMPRESCRITÍVEL (STF, Tema "
     "897). [Exercício Q02-IV, Rodada 01 Set/2024]"),

    ("03-I – As sanções previstas na Lei nº 8.429/1992 se aplicam aos "
     "atos praticados contra o patrimônio de entidade privada que seja "
     "custeada pelo erário. (C/E?)",
     "<b>CERTO.</b> Art. 1º, §6º — a Lei alcança excepcionalmente "
     "entidades privadas que recebam subvenção, benefício ou incentivo "
     "público. [Exercício Q03-I, Rodada 01 Set/2024]"),

    ("03-II – As ações de improbidade administrativa admitem a solução "
     "pela via consensual, sendo legalmente prevista a possibilidade de "
     "celebração de acordo de não persecução cível, que pode ser proposta "
     "por qualquer uma das partes da ação judicial. (C/E?)",
     "<b>ERRADO.</b> O acordo de não persecução civil (art. 17-B) só pode "
     "ser PROPOSTO pelo MP ou pela Fazenda Pública — o RÉU não tem "
     "legitimidade para propô-lo. [Exercício Q03-II, Rodada 01 Set/2024]"),

    ("03-III – Aplica-se a lei de improbidade administrativa ao "
     "parlamentar, de qualquer dos níveis de governo, nos casos de crimes "
     "de opinião. (C/E?)",
     "<b>ERRADO.</b> A ação de improbidade é CIVIL — não pode ser usada "
     "para promover responsabilidade PENAL (crime de opinião é matéria "
     "penal). [Exercício Q03-III, Rodada 01 Set/2024]"),

    ("03-IV – São elementos essenciais para a configuração do ato de "
     "improbidade administrativa: sujeito ativo, sujeito passivo, dolo, "
     "além de ato tipificado como ilícito do qual decorram dano ao "
     "erário, enriquecimento ilícito ou conduta que atente contra os "
     "princípios da administração. (C/E?)",
     "<b>CERTO.</b> Síntese dos elementos: sujeito ativo (MP/Fazenda), "
     "sujeito passivo (agente público ou particular que induziu/concorreu), "
     "dolo específico, e enquadramento nos arts. 9º, 10 ou 11. [Exercício "
     "Q03-IV, Rodada 01 Set/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Improbidade Administrativa",
        "Direito Interno - Improbidade Administrativa.apkg",
        IMPROBIDADE_ADMINISTRATIVA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
