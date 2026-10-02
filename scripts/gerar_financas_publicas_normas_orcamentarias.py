#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 02 (Janeiro/2024).

Tema: Finanças Públicas. Normas Orçamentárias (Item 14 do Edital CACD).

Fontes:
  - Anotações: Finanças Públicas e Normas Orçamentárias.md
  - Material do professor: Direito Interno_Rodada 02_Janeiro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 02_Janeiro_2024.pdf
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


FINANCAS_PUBLICAS_NORMAS_ORCAMENTARIAS = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Como as leis orçamentárias trazem previsões específicas sobre as "
     "receitas e despesas do Poder Legislativo e do Poder Judiciário, os "
     "chefes desses Poderes têm legitimidade para propor diretamente ao "
     "Congresso Nacional os respectivos projetos de lei orçamentária, "
     "cabendo ao Presidente da República apenas sancioná-los.",
     "<b>ERRADO.</b> A iniciativa das leis orçamentárias (PPA, LDO e LOA) é "
     "<b>privativa do chefe do Executivo</b> (art. 165, I a III, CF/88), que "
     "é quem tem estrutura para calcular a arrecadação real. Os chefes do "
     "Legislativo e do Judiciário elaboram apenas <b>propostas "
     "orçamentárias</b>, que o Presidente verifica frente à LDO e consolida "
     "no projeto de LOA. [Anotações da aula; Rodada 02/Jan.2024]"),

    ("As emendas parlamentares ao projeto de lei orçamentária anual podem "
     "indicar como fonte de custeio de nova despesa a previsão de "
     "arrecadação adicional, desde que sejam compatíveis com o plano "
     "plurianual e com a lei de diretrizes orçamentárias.",
     "<b>ERRADO.</b> Além da compatibilidade com PPA e LDO, a emenda "
     "parlamentar deve indicar os recursos necessários, sendo admitida "
     "apenas a <b>anulação de despesas</b> previstas no projeto (art. 166, "
     "§3º, CF/88) — não se pode apenas aumentar o gasto, pois quem projeta a "
     "arrecadação é o Presidente. [Anotações da aula; Rodada 02/Jan.2024]"),

    ("Como a criação de um fundo público não altera o montante de receitas "
     "que poderão ser alocadas na lei orçamentária anual, a CF/88 admite "
     "sua instituição por ato do chefe do Poder Executivo, sem necessidade "
     "de prévia autorização legislativa.",
     "<b>ERRADO.</b> O art. 167, IX, CF/88 veda a instituição de fundos de "
     "qualquer natureza <b>sem prévia autorização legislativa</b>. A razão: "
     "fundo criado por lei obriga o custeio das despesas previstas enquanto "
     "vigorar a lei instituidora, <b>reduzindo</b> as receitas alocáveis na "
     "LOA e a liberdade do Presidente (ex.: FUNDEB). [Anotações da aula; "
     "Rodada 02/Jan.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Jan/2024) ───────────────

    ("01-I – Normas de direito financeiro que regulamentam o orçamento "
     "público são privativas da União. (C/E?)",
     "<b>ERRADO.</b> Art. 24, I e II, CF/88 — a competência para legislar "
     "sobre direito financeiro e orçamento é <b>CONCORRENTE</b> (União, "
     "Estados e DF). O Município legisla de modo suplementar, no interesse "
     "local (art. 30, II). [Exercício Q01-I, Rodada 02 Jan/2024]"),

    ("01-II – A Constituição Federal de 1988 veda expressamente a "
     "transferência voluntária de recursos financeiros pelo governo estadual "
     "para fins de pagamento de despesas com pessoal ativo dos municípios. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 167, X, CF/88 veda a transferência voluntária de "
     "recursos (e a concessão de empréstimos) pelos Governos Federal e "
     "Estaduais e suas instituições financeiras para pagamento de despesas "
     "com pessoal ativo, inativo e pensionista de Estados, DF e Municípios. "
     "[Exercício Q01-II, Rodada 02 Jan/2024]"),

    ("01-III – É vedada a concessão de empréstimos pelas instituições "
     "financeiras públicas para pagamento de despesas com pessoal ativo e "
     "inativo dos estados, do DF e dos municípios. (C/E?)",
     "<b>CERTO.</b> Art. 167, X, CF/88. Atenção: a vedação alcança as "
     "instituições financeiras <b>públicas</b> (ex.: BB, Caixa); o STF "
     "admite que Estados, DF e Municípios tomem empréstimos de <b>bancos "
     "privados</b> para pagar pessoal, pois o risco é assumido pelo capital "
     "privado. [Exercício Q01-III, Rodada 02 Jan/2024]"),

    ("01-IV – Lei de iniciativa do Poder Executivo federal que estabelecer, "
     "de forma regionalizada, diretrizes, objetivos e metas da administração "
     "pública federal para as despesas de capital e outras delas "
     "decorrentes, bem como para as despesas relativas aos programas de "
     "duração continuada, instituirá o plano plurianual. (C/E?)",
     "<b>CERTO.</b> Art. 165, I e §1º, CF/88 — o PPA é de iniciativa "
     "privativa do Executivo e fixa Diretrizes, Objetivos e Metas (DOM) de "
     "forma regionalizada. [Exercício Q01-IV, Rodada 02 Jan/2024]"),

    ("02-I – Cabe à lei complementar dispor sobre o exercício financeiro, a "
     "vigência, os prazos, a elaboração e a organização do plano plurianual, "
     "da lei de diretrizes orçamentárias e da lei orçamentária anual. (C/E?)",
     "<b>CERTO.</b> Art. 165, §9º, I, CF/88. Essa lei complementar é a Lei "
     "4.320/1964, editada como lei ordinária e recepcionada pela CF/88 com "
     "status de lei complementar. [Exercício Q02-I, Rodada 02 Jan/2024]"),

    ("02-II – A transposição, o remanejamento ou a transferência de recursos "
     "de uma categoria de programação para outra ou de um órgão para outro "
     "não depende de prévia autorização legislativa. (C/E?)",
     "<b>ERRADO.</b> Art. 167, VI, CF/88 veda essas operações <b>sem prévia "
     "autorização legislativa</b>, pois alteram o conteúdo da LOA que fixou "
     "receitas e autorizou despesas (ex.: tirar recursos do MRE para o "
     "Ministério da Justiça). [Exercício Q02-II, Rodada 02 Jan/2024]"),

    ("02-III – Leis orçamentárias, por constituírem atos de natureza "
     "concreta, a despeito de sua forma legislativa, não podem ser objeto de "
     "controle concentrado de constitucionalidade. (C/E?)",
     "<b>ERRADO.</b> O STF revisou sua jurisprudência (ADI 4.048-MC): "
     "embora sejam leis de efeitos concretos, PPA, LDO e LOA podem ser "
     "objeto tanto de controle <b>concreto/difuso</b> quanto "
     "<b>abstrato/concentrado</b> (ADI, ADPF, ADO), pois sua invalidade pode "
     "inviabilizar direitos sociais. [Exercício Q02-III, Rodada 02 Jan/2024]"),

    ("02-IV – O início de programas e projetos governamentais não será "
     "possível sem a inclusão deles na LOA (lei orçamentária anual). (C/E?)",
     "<b>CERTO.</b> Art. 167, I, CF/88 veda o início de programas ou "
     "projetos não incluídos na LOA. O descumprimento pode configurar crime "
     "de responsabilidade do Presidente (art. 85, VI). [Exercício Q02-IV, "
     "Rodada 02 Jan/2024]"),

    ("03-I – Leis de iniciativa parlamentar poderão estabelecer o plano "
     "plurianual, as diretrizes orçamentárias e os orçamentos anuais. (C/E?)",
     "<b>ERRADO.</b> Art. 165, I a III, CF/88 — PPA, LDO e LOA são leis de "
     "iniciativa do chefe do Poder Executivo. Os parlamentares só podem "
     "propor <b>emendas</b>, nos limites do art. 166, §3º. [Exercício "
     "Q03-I, Rodada 02 Jan/2024]"),

    ("03-II – Em matéria orçamentária, medida provisória apenas poderá "
     "tratar da abertura de crédito extraordinário para atender a despesas "
     "imprevisíveis e urgentes. (C/E?)",
     "<b>CERTO.</b> Regra geral: art. 62, §1º, I, \"d\", CF/88 veda MP sobre "
     "PPA, LDO, orçamento e créditos adicionais/suplementares. Exceção: art. "
     "167, §3º — MP para crédito <b>extraordinário</b> (guerra, calamidade "
     "pública, comoção interna). [Exercício Q03-II, Rodada 02 Jan/2024]"),

    ("03-III – O presidente da República pode propor modificação no projeto "
     "de lei do orçamento anual enquanto não for iniciada a votação na "
     "comissão mista do Congresso Nacional da parte cuja alteração é "
     "proposta. (C/E?)",
     "<b>CERTO.</b> Art. 166, §5º, CF/88 — o Presidente pode enviar "
     "mensagem propondo modificação apenas até o início da votação, na "
     "Comissão Mista, da parte a ser alterada; depois, só parlamentares "
     "podem emendar. [Exercício Q03-III, Rodada 02 Jan/2024]"),

    ("03-IV – A CF/88 veda expressamente os denominados orçamentos "
     "rabilongos. (C/E?)",
     "<b>CERTO.</b> Art. 165, §8º, CF/88 (princípio da exclusividade ou "
     "pureza): a LOA só pode conter receita, despesa, autorização de "
     "créditos suplementares e de operações de crédito. Incluir temas "
     "estranhos (\"jabutis\") configura orçamento rabilongo. [Exercício "
     "Q03-IV, Rodada 02 Jan/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Finanças Públicas e Normas Orçamentárias",
        "Direito Interno - Finanças Públicas e Normas Orçamentárias.apkg",
        FINANCAS_PUBLICAS_NORMAS_ORCAMENTARIAS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
