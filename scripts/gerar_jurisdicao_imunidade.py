#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Jurisdição e Imunidade"""

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
    # ── CONCEITO GERAL ────────────────────────────────────────────────────────
    (
        "O que é imunidade em Direito Internacional e quais os dois tipos de processos que podem ser ajuizados contra Estados/OIs?",
        "Proteção de Estados e OIs contra processos judiciais perante o poder judiciário nacional de outro Estado.<br>"
        "Dois tipos: <b>processo de conhecimento</b> (produção de provas, sentença) → imunidade de jurisdição; "
        "<b>processo de execução</b> (penhora de bens para cumprir sentença) → imunidade de execução.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),

    # ── IMUNIDADE DE JURISDIÇÃO DOS ESTADOS ──────────────────────────────────
    (
        "Qual o fundamento e a fonte da imunidade de jurisdição dos Estados soberanos?",
        "<b>Fonte</b>: norma costumeira (não há tratado que a regule).<br>"
        "<b>Fundamento</b>: aforismo <i>par in parem non habet judicium</i> (entre iguais não há juiz) — princípio da igualdade soberana.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "A imunidade de jurisdição dos Estados soberanos é absoluta ou relativa? Por quê?",
        "<b>Relativa</b> — aplica-se a Teoria dos Atos de Gestão vs. Atos de Império:<br>"
        "• Atos de gestão → <b>sem imunidade</b><br>"
        "• Atos de império → <b>com imunidade</b><br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "O que são Atos de Gestão? Há imunidade de jurisdição para atos de gestão?",
        "Atos que não denotam soberania; particulares também os praticam "
        "(contratar pessoal, gerir patrimônio, serviços de consumo).<br>"
        "<b>NÃO há imunidade de jurisdição</b> — Estado estrangeiro pode ser réu e condenado.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "O que são Atos de Império? Há imunidade de jurisdição para atos de império?",
        "Atos típicos do Estado soberano que particulares não podem praticar "
        "(atos de guerra, negativa de visto, relatórios de atividades diplomáticas/consulares).<br>"
        "<b>HÁ imunidade de jurisdição</b> — salvo exceções.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Qual caso paradigmático no STF relativizou a imunidade de jurisdição de Estado estrangeiro?",
        "<b>Caso Geny de Oliveira (STF, anos 1980)</b>: Embaixada da Alemanha foi condenada a pagar "
        "verbas trabalhistas a ex-empregados domésticos. Ato de gestão → sem imunidade.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Quais as exceções à imunidade de jurisdição em Atos de Império?",
        "1. <b>Renúncia expressa</b> pelo Estado estrangeiro.<br>"
        "2. <b>Violação de DH</b>: STF (e tribunais da Itália e Coreia do Sul) não acatam imunidade se "
        "o ato viola direitos humanos (ex. Caso Changri-La).<br>"
        "⚠️ <b>CIJ diverge</b>: entende que a imunidade persiste mesmo com violação de DH.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Qual a posição do STF vs. CIJ sobre imunidade de jurisdição quando há violação de DH em Atos de Império?",
        "<b>STF</b> (e Itália, Coreia do Sul): <b>não acata</b> a imunidade se há violação de DH.<br>"
        "<b>CIJ</b>: a imunidade <b>persiste</b> mesmo quando o ato de império viola direitos humanos.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),

    # ── IMUNIDADE DE EXECUÇÃO DOS ESTADOS ────────────────────────────────────
    (
        "Qual a fonte e a natureza (absoluta/relativa) da imunidade de execução dos Estados soberanos?",
        "<b>Fonte</b>: convencional — Convenção de Viena sobre Relações Diplomáticas (1961) e "
        "Convenção de Viena sobre Relações Consulares (1963).<br>"
        "<b>Natureza</b>: <b>ABSOLUTA</b> — a teoria dos atos de gestão/império NÃO se aplica aqui.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Quais as exceções à imunidade de execução dos Estados soberanos?",
        "1. <b>Renúncia expressa específica para execução</b> (a renúncia à jurisdição NÃO se estende à execução).<br>"
        "2. <b>Bens desafetos</b>: bens do Estado estrangeiro no Brasil não vinculados a atividades "
        "diplomáticas/consulares (ex. imóveis desocupados, aplicações financeiras) podem ser penhorados.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "A renúncia à imunidade de jurisdição implica renúncia à imunidade de execução?",
        "<b>Não</b>. São renúncias independentes. A renúncia no processo de conhecimento não produz efeitos "
        "no processo de execução — exige-se nova renúncia expressa específica para a execução.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),

    # ── IMUNIDADE DE OIs ──────────────────────────────────────────────────────
    (
        "Por que a teoria dos Atos de Gestão vs. Atos de Império NÃO se aplica às OIs?",
        "OIs <b>não exercem soberania</b> — atos de império demandam exercício de soberania, "
        "qualidade que apenas Estados possuem. Portanto, não há distinção de atos para fins de imunidade das OIs.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Qual o entendimento do STF/TST sobre imunidade de jurisdição das OIs?",
        "OIs <b>só gozam de imunidade de jurisdição</b> se houver tratado internacional incorporado ao ordenamento "
        "brasileiro (não se aplica a norma costumeira).<br>"
        "TST (OJ 416, confirmada pelo STF): com tratado → OI tem imunidade <b>ABSOLUTA</b> de jurisdição.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "O que é o TANU e qual sua relevância para a imunidade de OIs?",
        "<b>TANU</b> = Tribunal Administrativo das Nações Unidas (1949): tribunal próprio das OIs "
        "para resolver questões trabalhistas de seus funcionários; decisões vinculantes.<br>"
        "Funcionários de OIs devem recorrer ao TANU, não à Justiça nacional. Isso não viola o direito "
        "de acesso à justiça (os tribunais próprios das OIs são 'justiça' nesse caso).<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),
    (
        "Qual o status da imunidade de execução das OIs?",
        "<b>Absoluta</b>, desde que prevista em tratado internacional com conteúdo específico sobre imunidade de execução. "
        "Os bens das OIs são invioláveis de forma absoluta quando amparados por tratado.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),

    # ── RESUMO COMPARATIVO ────────────────────────────────────────────────────
    (
        "Compare: imunidade de jurisdição de Estados vs. OIs (fonte, natureza e aplicação da teoria dos atos).",
        "<b>Estados</b>: fonte costumeira; relativa (gestão = sem imunidade; império = com imunidade).<br>"
        "<b>OIs</b>: fonte convencional (tratado); absoluta se houver tratado; teoria dos atos NÃO se aplica.<br>"
        "<i>Fonte: Anotações – Jurisdição e Imunidade</i>",
    ),

    # ── EXERCÍCIOS — Q01 (Rodada 01 – Jan/2024) ──────────────────────────────
    (
        "[Exercício] I – Com fundamento no costume internacional e no aforismo 'par in parem non habet "
        "judicium', o Direito Internacional definiu os parâmetros da norma que dispõe acerca de "
        "imunidade de <u>execução</u> estatal.",
        "<b>ERRADO.</b> O aforismo <i>par in parem...</i> e a norma costumeira fundamentam a imunidade de "
        "<b>jurisdição</b>, não de execução. A imunidade de <b>execução</b> tem fonte <b>convencional</b> "
        "(Convenções de Viena de 1961 e 1963).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q01-I</i>",
    ),
    (
        "[Exercício] II – O silêncio do Estado-réu, que não atende ao chamamento judicial, não configura, "
        "nos termos de jurisprudência do STF, renúncia à imunidade de jurisdição.",
        "<b>CERTO.</b> A renúncia à imunidade de jurisdição deve ser <b>expressa</b>. O silêncio do Estado "
        "não equivale a renúncia, segundo o STF.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q01-II</i>",
    ),
    (
        "[Exercício] III – O Estado estrangeiro poderá renunciar à imunidade estatal em ação trabalhista "
        "movida por ex-empregado da embaixada, com o objetivo de viabilizar a tramitação e conclusão "
        "desse processo perante o Poder Judiciário brasileiro.",
        "<b>ERRADO.</b> Em ações trabalhistas de ex-empregados de embaixada (ato de gestão), "
        "<b>não há imunidade de jurisdição a renunciar</b> — a jurisdição já é do judiciário brasileiro "
        "pela teoria dos atos. A renúncia é desnecessária porque a imunidade simplesmente não se aplica.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q01-III</i>",
    ),
    (
        "[Exercício] IV – A CF estabelece que compete à Justiça do Trabalho julgar os dissídios entre "
        "trabalhadores e empregadores, abrangidos os entes de direito público externo. Disso decorre "
        "que a imunidade do Estado estrangeiro não é mais absoluta no Brasil para processo de "
        "conhecimento em demanda trabalhista.",
        "<b>CERTO.</b> A competência da JT abrange entes de direito público externo (art. 114 CF/88). "
        "Combinada à relativização da imunidade de jurisdição (teoria dos atos), a imunidade não é "
        "absoluta em demandas trabalhistas.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – A competência para conhecer da ação de brasileiro contra Estado estrangeiro "
        "pelo descumprimento de direitos trabalhistas é da Justiça Federal.",
        "<b>ERRADO.</b> A competência é da <b>Justiça do Trabalho</b> (art. 114 CF/88), não da Justiça "
        "Federal. A JT abrange expressamente os entes de direito público externo.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q02-I</i>",
    ),
    (
        "[Exercício] II – Normas convencionais asseguram aos Estados soberanos imunidade absoluta "
        "de execução.",
        "<b>CERTO.</b> As Convenções de Viena (1961 e 1963) asseguram imunidade <b>absoluta</b> de "
        "execução sobre bens ligados a atividades diplomáticas e consulares. A imunidade de execução "
        "tem fonte convencional e é absoluta (ao contrário da de jurisdição).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q02-II</i>",
    ),
    (
        "[Exercício] III – Nos termos da jurisprudência do STF <u>e</u> da CIJ, os atos de império "
        "praticados por Estados estrangeiros não gozam de imunidade de jurisdição se houver "
        "violação aos direitos humanos.",
        "<b>ERRADO.</b> O STF afasta a imunidade em atos de império que violam DH, mas a <b>CIJ "
        "discorda</b>: para a CIJ, a imunidade persiste mesmo com violação de DH. O item erra ao "
        "equiparar as posições do STF e da CIJ.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q02-III</i>",
    ),
    (
        "[Exercício] IV – Eventual renúncia à imunidade de jurisdição realizada por Estado estrangeiro "
        "não produz efeitos no consequente processo de execução decorrente do descumprimento "
        "de sentença condenatória.",
        "<b>CERTO.</b> Renúncia à imunidade de jurisdição (processo de conhecimento) <b>não se estende</b> "
        "ao processo de execução. São renúncias independentes; exige-se nova renúncia expressa "
        "específica para a execução.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – A imunidade de jurisdição de organismos internacionais é absoluta por força "
        "de uma norma 'jus cogens'.",
        "<b>ERRADO.</b> A imunidade de jurisdição de OIs não decorre de <i>jus cogens</i> (norma "
        "peremptória). Decorre de <b>norma convencional</b> (tratado internacional). Sem tratado, "
        "não há imunidade.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q03-I</i>",
    ),
    (
        "[Exercício] II – Segundo o TST, a imunidade à execução de crédito na justiça do trabalho "
        "alcança os bens de missão diplomática, inclusive os bens que não estejam afetos às "
        "atividades da missão.",
        "<b>ERRADO.</b> A imunidade de execução protege apenas os bens <b>afetos às atividades "
        "diplomáticas e consulares</b> (Convenções de Viena). Bens desafetos (imóveis desocupados, "
        "aplicações financeiras) podem ser penhorados.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q03-II</i>",
    ),
    (
        "[Exercício] III – No caso de empregado da ONU que pretenha receber haveres trabalhistas, "
        "deverá seguir o procedimento descrito na Convenção das Nações Unidas sobre Imunidades de "
        "Jurisdição e Execução dos Estados.",
        "<b>ERRADO.</b> Funcionários da ONU devem recorrer ao <b>TANU</b> (Tribunal Administrativo "
        "das Nações Unidas), não à Convenção sobre Imunidades de Jurisdição dos Estados (que regula "
        "relações entre Estados, não funcionários de OIs).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q03-III</i>",
    ),
    (
        "[Exercício] IV – As organizações internacionais gozam de imunidade absoluta de jurisdição "
        "quando amparadas por norma internacional incorporada ao ordenamento jurídico brasileiro, "
        "não se lhes aplicando a regra consuetudinária relativa à natureza dos atos praticados.",
        "<b>CERTO.</b> Se há tratado internacional incorporado: OI tem imunidade <b>absoluta</b> de "
        "jurisdição. A distinção costumeira entre atos de gestão e império aplica-se a <b>Estados</b>, "
        "não a OIs (que não exercem soberania).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01, Jan/2024, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Internacional::Jurisdição e Imunidade",
        "Direito Internacional - Jurisdição e Imunidade.apkg",
        CARDS,
    )
