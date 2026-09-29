#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 02 (Abril/2025).

Tema: Processo Administrativo Disciplinar (Itens 9 e 12 do Edital CACD).

Fontes:
  - Anotações: Processo Administrativo Disciplinar.md
  - Material do professor: Direito Interno_Rodada 02_Abril_2025_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 02_Abril_2025.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/direito interno"
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


PROCESSO_ADMINISTRATIVO_DISCIPLINAR = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O estágio probatório de 03 anos exigido para a aquisição de estabilidade "
     "conta-se a partir da posse do servidor público efetivo no cargo, de modo "
     "que eventuais períodos de licença gozados nesse intervalo são computados "
     "normalmente para fins de estágio probatório.",
     "<b>ERRADO.</b> O estágio probatório exige 03 anos de <b>EFETIVO "
     "EXERCÍCIO</b> — não de posse. Em regra, os períodos de licença do "
     "servidor durante o estágio probatório NÃO são computados como efetivo "
     "exercício para a aquisição da estabilidade. [Anotações da aula; Rodada "
     "02/Abr.2025]"),

    ("Caso a autoridade administrativa tenha ciência de irregularidade "
     "praticada por servidor público, a instauração de sindicância prévia ao "
     "processo administrativo disciplinar é sempre obrigatória, ainda que já "
     "existam provas suficientes para a imediata apuração da infração "
     "funcional.",
     "<b>ERRADO.</b> A sindicância prévia (art. 143, Lei 8.112/1990) é "
     "FACULTATIVA — só se justifica quando NÃO há provas suficientes para "
     "instaurar o PAD diretamente, servindo para produzi-las. Havendo provas "
     "suficientes, o PAD pode ser instaurado diretamente, sem sindicância "
     "prévia. [Anotações da aula; Rodada 02/Abr.2025]"),

    ("Na hipótese de extinção do cargo público ocupado por servidor que ainda "
     "não completou o estágio probatório, aplica-se o mesmo regime "
     "constitucional do servidor estável, sendo-lhe assegurado o direito de "
     "ser aproveitado em outro cargo compatível, em vez de perder o cargo.",
     "<b>ERRADO.</b> A garantia de disponibilidade e aproveitamento do art. "
     "41, §3º, CF/88 só se aplica ao servidor <b>ESTÁVEL</b>. Se o cargo "
     "extinto era ocupado por servidor ainda em estágio probatório (não "
     "estável), haverá <b>PERDA DO CARGO</b>, sem direito a aproveitamento. "
     "[Anotações da aula; Rodada 02/Abr.2025]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Abr/2025) ───────────────

    ("01-I – Após entrar em exercício, o servidor nomeado para cargo efetivo "
     "ou cargo em comissão de livre nomeação e exoneração ficará sujeito a "
     "estágio probatório, durante o qual a sua aptidão e capacidade serão "
     "objeto de avaliação para o desempenho do cargo. (C/E?)",
     "<b>ERRADO.</b> O estágio probatório (art. 41, \"caput\", CF/88) é "
     "requisito para aquisição de estabilidade pelo servidor EFETIVO — NÃO "
     "se aplica a ocupantes de cargo em comissão, contratados temporários ou "
     "empregados públicos, que não gozam de estabilidade. [Exercício Q01-I, "
     "Rodada 02 Abr/2025]"),

    ("01-II – O tempo de serviço prestado a um ente da federação não deve "
     "ser computado no estágio probatório do servidor aprovado para cargo de "
     "outro ente. (C/E?)",
     "<b>CERTO.</b> Os 03 anos de efetivo exercício devem se referir ao "
     "CARGO PARA O QUAL se pretende adquirir estabilidade — ao ser aprovado "
     "em concurso para novo cargo, o prazo de estágio probatório recomeça. "
     "[Exercício Q01-II, Rodada 02 Abr/2025]"),

    ("01-III – Cumprido o requisito temporal para a obtenção da estabilidade, "
     "será garantido ao servidor público tal benefício. (C/E?)",
     "<b>ERRADO.</b> A estabilidade exige 02 requisitos CUMULATIVOS: (i) 03 "
     "anos de efetivo exercício (art. 41, \"caput\") e (ii) aprovação em "
     "avaliação especial de desempenho por comissão instituída para essa "
     "finalidade (art. 41, §4º). O requisito temporal isolado não basta. "
     "[Exercício Q01-III, Rodada 02 Abr/2025]"),

    ("01-IV – A perda do cargo por servidor público estável poderá ocorrer "
     "mediante procedimento de avaliação periódica de desempenho, assegurada "
     "ampla defesa. (C/E?)",
     "<b>CERTO.</b> Art. 41, §1º, III, CF/88 — uma das 03 hipóteses "
     "taxativas de perda do cargo pelo servidor estável, ao lado de sentença "
     "judicial transitada em julgado e de PAD com ampla defesa. [Exercício "
     "Q01-IV, Rodada 02 Abr/2025]"),

    ("02-I – O servidor público estável manterá o vínculo com a "
     "administração pública, mesmo que o seu cargo seja extinto. (C/E?)",
     "<b>CERTO.</b> Art. 41, §3º, CF/88 — o servidor estável, em caso de "
     "extinção do cargo, fica em disponibilidade com remuneração "
     "proporcional até seu aproveitamento em outro cargo, sem perder o "
     "vínculo com a administração. [Exercício Q02-I, Rodada 02 Abr/2025]"),

    ("02-II – O servidor estável colocado em disponibilidade faz jus à "
     "remuneração integral até o seu adequado aproveitamento em outro cargo. "
     "(C/E?)",
     "<b>ERRADO.</b> Art. 41, §3º, CF/88 — a remuneração em disponibilidade "
     "é <b>PROPORCIONAL AO TEMPO DE SERVIÇO</b>, não integral. [Exercício "
     "Q02-II, Rodada 02 Abr/2025]"),

    ("02-III – Na hipótese de invalidação da demissão de servidor estável, "
     "por sentença judicial, este deverá ser reintegrado. O eventual "
     "ocupante da vaga, se estável, deverá ser reconduzido ao cargo de "
     "origem, com direito à respectiva indenização. (C/E?)",
     "<b>ERRADO.</b> Art. 41, §2º, CF/88 — o ocupante da vaga que for "
     "reconduzido ao cargo de origem por ser estável NÃO tem direito a "
     "indenização; a recondução se dá SEM indenização. [Exercício Q02-III, "
     "Rodada 02 Abr/2025]"),

    ("02-IV – É possível a exoneração de servidor estável por excesso de "
     "despesa com pessoal. (C/E?)",
     "<b>CERTO.</b> Art. 169, §4º, CF/88 — se a redução de cargos em "
     "comissão (mín. 20%) e a exoneração de servidores não estáveis não "
     "forem suficientes, é possível exonerar servidores estáveis, com "
     "direito a indenização de 1 mês de remuneração por ano de serviço. "
     "[Exercício Q02-IV, Rodada 02 Abr/2025]"),

    ("03-I – Diante de informação de que determinado servidor público "
     "federal favorecia um grupo de empresários estrangeiros que tinham "
     "interesse em investir no Brasil, a autoridade competente instaurou o "
     "processo administrativo cabível para apuração das possíveis "
     "irregularidades e eventual aplicação de pena. Nessa situação "
     "hipotética, a autoridade exerceu o poder disciplinar, que é vinculado "
     "quanto à obrigatoriedade de apurar a infração. (C/E?)",
     "<b>CERTO.</b> Art. 143, Lei 8.112/1990 — a autoridade que toma ciência "
     "de irregularidade tem o DEVER (poder-dever de autotutela) de apurá-la "
     "via sindicância ou PAD; o poder disciplinar é vinculado quanto a essa "
     "obrigatoriedade de apuração. [Exercício Q03-I, Rodada 02 Abr/2025]"),

    ("03-II – A instauração de processo administrativo disciplinar com base "
     "em denúncia anônima é permitida desde que devidamente motivada e com "
     "amparo em investigação ou sindicância. (C/E?)",
     "<b>CERTO.</b> Súmula 611, STJ — denúncia anônima pode fundamentar a "
     "instauração de PAD, desde que motivada e amparada em investigação ou "
     "sindicância que confirme indícios de regularidade da denúncia. "
     "[Exercício Q03-II, Rodada 02 Abr/2025]"),

    ("03-III – É obrigatória a presença de advogado em todas as fases do "
     "processo administrativo disciplinar. (C/E?)",
     "<b>ERRADO.</b> Súmula Vinculante 5, STF — a falta de defesa técnica "
     "por advogado no PAD NÃO ofende a Constituição; cabe ao servidor optar "
     "por autodefesa isolada ou também por defesa técnica. [Exercício "
     "Q03-III, Rodada 02 Abr/2025]"),

    ("03-IV – O fim do regime jurídico único na Administração Pública "
     "direta, autárquica e fundacional da União, Estados, DF e Municípios "
     "não implicou o fim da garantia da estabilidade para os servidores e "
     "empregados públicos. (C/E?)",
     "<b>ERRADO.</b> A ADI 2135 (STF) validou o fim da obrigatoriedade do "
     "regime jurídico único, mas a estabilidade do art. 41 CF/88 permanece "
     "apenas para servidores ESTATUTÁRIOS — os EMPREGADOS PÚBLICOS "
     "admitidos nesse novo regime NÃO gozam de estabilidade. [Exercício "
     "Q03-IV, Rodada 02 Abr/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Processo Administrativo Disciplinar",
        "Direito Interno - Processo Administrativo Disciplinar.apkg",
        PROCESSO_ADMINISTRATIVO_DISCIPLINAR,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
