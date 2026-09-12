#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 02 (Fev/2024).

Tema: Direitos, deveres e responsabilidades do servidor público. Regime
disciplinar e processo administrativo disciplinar (Item 12 do Edital
CACD).

Fontes:
  - Anotações: Direitos, Deveres e Responsabilidades dos Servidores.md
  - Material do professor: Direito Interno_Rodada 02_Fevereiro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 02_Fevereiro_2024.pdf
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


DIREITOS_DEVERES_SERVIDORES = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("A responsabilidade do servidor público por danos causados a terceiros "
     "no exercício de suas atribuições é objetiva, tal como a "
     "responsabilidade do próprio Estado, dispensando-se a comprovação de "
     "culpa ou dolo para a sua caracterização.",
     "<b>ERRADO.</b> A responsabilidade do <b>Estado</b> é objetiva, mas a "
     "responsabilidade do <b>servidor</b> é sempre <b>SUBJETIVA</b> — "
     "exige comprovação de culpa (negligência, imprudência, imperícia) ou "
     "dolo, nos termos do exercício IRREGULAR das atribuições exigido pelo "
     "art. 121 da Lei 8.112/1990. [Anotações da aula; Rodada 02/Fev.2024]"),

    ("No âmbito da Administração Pública federal, um Ministro de Estado "
     "jamais poderá aplicar a penalidade de demissão a um servidor público "
     "estatutário vinculado ao seu Ministério, pois essa competência é "
     "exclusiva e indelegável do Presidente da República.",
     "<b>ERRADO.</b> Embora o art. 141, I, da Lei 8.112/90 atribua ao "
     "Presidente da República a competência para demitir, o art. 84, "
     "parágrafo único, CF/88 permite que essa competência (\"prover "
     "cargos públicos federais\", que o STF interpreta como nomear E "
     "demitir) seja <b>DELEGADA</b> a Ministros de Estado, ao "
     "Advogado-Geral da União ou ao Procurador-Geral da República. "
     "[Anotações da aula; Rodada 02/Fev.2024]"),

    ("A Lei nº 8.112/1990 constitui o regime jurídico único aplicável a "
     "todos os agentes que prestam serviço à União, suas autarquias e "
     "fundações públicas, incluindo os empregados públicos de empresas "
     "públicas e sociedades de economia mista federais.",
     "<b>ERRADO.</b> A Lei 8.112/90 aplica-se apenas aos servidores "
     "<b>ESTATUTÁRIOS</b> (cargo público efetivo, inclusive diplomatas). "
     "Os <b>empregados públicos</b> de empresas públicas e sociedades de "
     "economia mista são regidos pela <b>CLT</b>, não pelo Estatuto. "
     "[Anotações da aula; Rodada 02/Fev.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Fev/2024) ──────────────

    ("01-I – O servidor responde apenas administrativamente pelo "
     "exercício irregular de suas atribuições, o qual pode ensejar a "
     "aplicação de penalidade disciplinar – até mesmo de demissão –, que "
     "deve, sempre, mencionar o fundamento legal e a causa da sanção. "
     "(C/E?)",
     "<b>ERRADO.</b> O art. 121 prevê responsabilização TRÍPLICE — civil, "
     "administrativa E penal —, não apenas administrativa. [Exercício "
     "Q01-I, Rodada 02 Fev/2024]"),

    ("01-II – Um processo administrativo disciplinar instaurado para "
     "apurar possíveis irregularidades cometidas por um servidor público "
     "federal revelou o desvio de verbas públicas. Nessa situação, o "
     "eventual ajuizamento da ação penal não extinguirá o procedimento "
     "administrativo contra o servidor. (C/E?)",
     "<b>CERTO.</b> Art. 125: as esferas civil, penal e administrativa são "
     "independentes e cumuláveis — o ajuizamento de ação penal não "
     "extingue o PAD em curso. [Exercício Q01-II, Rodada 02 Fev/2024]"),

    ("01-III – Caso o servidor público tenha causado danos ao poder "
     "público, a obrigação de reparar tais danos estende-se aos seus "
     "sucessores e contra eles será executada, até o limite do valor da "
     "herança recebida. (C/E?)",
     "<b>CERTO.</b> Art. 122, §3º, Lei 8.112/90 (em paralelo ao art. 5º, "
     "XLV, CF/88) — obrigação de reparar se estende aos herdeiros até o "
     "limite da herança recebida. [Exercício Q01-III, Rodada 02 Fev/2024]"),

    ("01-IV – Apesar de as instâncias administrativa e penal serem "
     "independentes entre si, a eventual responsabilidade administrativa "
     "do servidor será afastada se, na esfera criminal, ele for "
     "beneficiado por absolvição decorrente da ausência de provas sobre "
     "existência do fato ou a sua autoria. (C/E?)",
     "<b>ERRADO.</b> Só a absolvição por NEGAR a existência do fato ou a "
     "autoria (art. 126) afasta a responsabilidade administrativa — a "
     "absolvição por mera AUSÊNCIA/INSUFICIÊNCIA de provas NÃO produz "
     "esse efeito. [Exercício Q01-IV, Rodada 02 Fev/2024]"),

    ("02-I – É dever do servidor público obedecer às ordens superiores, "
     "exceto quando contaminadas de algum vício ilegal. Nessa situação, o "
     "servidor tem por obrigação descumprir a ordem e representar contra "
     "seu superior hierárquico. (C/E?)",
     "<b>CERTO.</b> Art. 116, IV (obedecer, exceto ordem manifestamente "
     "ilegal) combinado com o inciso XII (dever de representar contra "
     "ilegalidade, omissão ou abuso de poder). [Exercício Q02-I, Rodada 02 "
     "Fev/2024]"),

    ("02-II – O agente público, no exercício das funções administrativas "
     "legalmente atribuídas a si, responde tanto por suas ações quanto por "
     "suas omissões, em decorrência do seu múnus público. (C/E?)",
     "<b>CERTO.</b> Art. 122, caput — responsabilidade abrange atos "
     "COMISSIVOS (ações) e OMISSIVOS (omissões). [Exercício Q02-II, Rodada "
     "02 Fev/2024]"),

    ("02-III – Somente excepcionalmente, se grave a imputação e se houver "
     "fundamentos mínimos, admitir-se-á a instauração de processo "
     "administrativo disciplinar com base em denúncia anônima. (C/E?)",
     "<b>ERRADO.</b> Súmula 611/STJ não exige gravidade da imputação nem "
     "elementos probatórios mínimos na denúncia — basta que o PAD seja "
     "motivado e apoiado em investigação/sindicância. [Exercício Q02-III, "
     "Rodada 02 Fev/2024]"),

    ("02-IV – No entendimento do STF, a garantia do devido processo legal "
     "não torna obrigatória a defesa técnica por advogado no âmbito dos "
     "processos administrativos disciplinares que envolvam servidores "
     "públicos. (C/E?)",
     "<b>CERTO.</b> Súmula Vinculante 5 — falta de defesa técnica por "
     "advogado no PAD não ofende a Constituição; a autodefesa é "
     "suficiente. [Exercício Q02-IV, Rodada 02 Fev/2024]"),

    ("03-I – O processo disciplinar é o instrumento destinado a apurar "
     "responsabilidade de servidor por infração praticada no exercício de "
     "suas atribuições, ou que tenha relação com as atribuições do cargo "
     "em que se encontre investido. (C/E?)",
     "<b>CERTO.</b> É a definição do PAD — instrumento de responsabilização "
     "administrativa por infrações ligadas ao cargo/função. [Exercício "
     "Q03-I, Rodada 02 Fev/2024]"),

    ("03-II – A sindicância prevista na Lei n.º 8.112/1990, da qual pode "
     "resultar tão somente a aplicação de penalidade de advertência ou "
     "suspensão de até trinta dias, constitui procedimento preliminar e "
     "inquisitório que dispensa a observância do princípio da ampla defesa "
     "e do contraditório. (C/E?)",
     "<b>ERRADO.</b> Quando a sindicância PODE resultar em sanção "
     "(advertência/suspensão ≤30 dias), ela se equipara ao PAD e EXIGE "
     "ampla defesa e contraditório — dispensa só ocorre na sindicância "
     "meramente preliminar (sem aplicação de sanção). [Exercício Q03-II, "
     "Rodada 02 Fev/2024]"),

    ("03-III – Em inquérito administrativo instaurado contra servidor, é "
     "dispensável a observância do contraditório e da ampla defesa por "
     "constituir fase prévia e inquisitiva do processo administrativo "
     "disciplinar. (C/E?)",
     "<b>ERRADO.</b> O inquérito administrativo é fase do PAD (não uma "
     "etapa \"prévia\" como a sindicância) e EXIGE contraditório e ampla "
     "defesa obrigatoriamente, sob pena de nulidade. [Exercício Q03-III, "
     "Rodada 02 Fev/2024]"),

    ("03-IV – A autoridade julgadora do processo administrativo "
     "disciplinar instaurado contra o servidor deve acatar, em regra, o "
     "relatório final da comissão processante. (C/E?)",
     "<b>CERTO.</b> Art. 168 — regra geral é acatar o relatório; só se as "
     "provas dos autos forem incompatíveis com ele, a autoridade pode, "
     "motivadamente, agravar, abrandar ou isentar a pena. [Exercício "
     "Q03-IV, Rodada 02 Fev/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Direitos, Deveres e Responsabilidades dos Servidores",
        "Direito Interno - Direitos, Deveres e Responsabilidades dos Servidores.apkg",
        DIREITOS_DEVERES_SERVIDORES,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
