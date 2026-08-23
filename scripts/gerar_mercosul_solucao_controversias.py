#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 02 (Abr/2025).

Tema: Direito da Integração Regional. MERCOSUL. Relação com o Direito
Brasileiro. Órgão de Solução de Controvérsias. Jurisprudência (Item 26 do
Edital CACD).

Fontes:
  - Anotações: Mercosul - Sistema de Solução de Controvérsias.md
  - Material do professor: Direito Internacional_Rodada 02_Abril_2025_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 02_Abril_2025.pdf
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


MERCOSUL_SOLUCAO_CONTROVERSIAS = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Caso o tribunal arbitral \"ad hoc\" constituído no âmbito do Mercosul "
     "profira laudo arbitral fundamentado exclusivamente em equidade (decisão "
     "\"ex aequo et bono\"), tal decisão poderá ser objeto de recurso de "
     "revisão perante o Tribunal Permanente de Revisão, desde que a parte "
     "sucumbente demonstre a existência de questão de direito não apreciada.",
     "<b>ERRADO.</b> Pelo art. 17, §3º do Protocolo de Olivos, laudo fundado "
     "em equidade <b>não</b> pode ser objeto de recurso de revisão ao TPR, "
     "independentemente de qualquer questão de direito — a aplicação da "
     "equidade requer consentimento de ambas as partes, e não há norma "
     "jurídica a ser revisada. [Anotações da aula; Rodada 02/Abr.2025, p.4]"),

    ("O Tribunal Permanente de Revisão do Mercosul é composto por cinco "
     "árbitros, cada Estado-parte designando um árbitro e seu suplente por "
     "período de dois anos renovável por no máximo dois períodos "
     "consecutivos, ao passo que o tribunal arbitral \"ad hoc\" é composto "
     "por apenas três árbitros designados especificamente para cada "
     "controvérsia.",
     "<b>CERTO.</b> Art. 18 do Protocolo de Olivos: o TPR tem <b>5 "
     "árbitros</b> (4 designados pelos Estados-partes por 2 anos renováveis "
     "por até 2 períodos, mais o quinto árbitro por 3 anos não renovável); "
     "o tribunal ad hoc tem <b>3 árbitros</b> (art. 10), sem caráter "
     "permanente. [Anotações da aula; Rodada 02/Abr.2025, p.12-13]"),

    ("Caso um Estado-parte descumpra total ou parcialmente o laudo proferido "
     "pelo tribunal arbitral do Mercosul, a única via jurídica disponível ao "
     "Estado prejudicado é iniciar novo procedimento de negociações diretas "
     "visando à renegociação do cumprimento da decisão.",
     "<b>ERRADO.</b> O art. 31 do Protocolo de Olivos prevê que o Estado "
     "beneficiado pelo laudo tem a faculdade de aplicar <b>medidas "
     "compensatórias</b> (suspensão de concessões ou obrigações "
     "equivalentes), independentemente de recorrer a outros procedimentos, "
     "dentro do prazo de 1 ano do descumprimento. "
     "[Anotações da aula; Rodada 02/Abr.2025, p.15]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Abr/2025) ──────────────

    ("I – As controvérsias que surjam entre os Estados-membros do Mercosul "
     "acerca da interpretação, aplicação ou não cumprimento de atos "
     "normativos desse bloco regional poderão ser solucionadas segundo os "
     "procedimentos estabelecidos no Protocolo de Olivos, o que não exclui, "
     "se for o caso, a possibilidade de acionar de outros sistemas de "
     "solução de controvérsias. (C/E?)",
     "<b>CERTO.</b> Pelo art. 1º, nº 2, do Protocolo de Olivos, os "
     "Estados-membros têm <b>liberdade de escolha</b> quanto ao sistema de "
     "solução de controvérsias antes de iniciar o procedimento — podendo "
     "optar pelo sistema do Mercosul, da OMC, da CIJ, ou por arbitragem "
     "específica. [Exercício Q01-I, Rodada 02 Abr/2025]"),

    ("II – Para a solução de controvérsias no âmbito do Mercosul, qualquer "
     "dos Estados-parte pode recorrer ao procedimento arbitral perante o "
     "Tribunal ad hoc independentemente de qualquer procedimento anterior. "
     "(C/E?)",
     "<b>ERRADO.</b> O art. 4º do Protocolo de Olivos exige que, antes do "
     "emprego do GMC, do tribunal ad hoc ou do TPR, os Estados-membros "
     "realizem <b>negociações diretas</b> — a única etapa obrigatória e que "
     "não pode ser suprimida. [Exercício Q01-II, Rodada 02 Abr/2025]"),

    ("III – O Grupo Mercado Comum, embora não tenha a natureza de órgão "
     "jurisdicional, pode ser empregado no âmbito do sistema de solução de "
     "controvérsias do Mercosul, mediante negociação entabulada entre os "
     "Estados litigantes. (C/E?)",
     "<b>CERTO.</b> O GMC pode ser acionado, desde que exista negociação "
     "entre os Estados litigantes que defina, de comum acordo, o "
     "acionamento desse mecanismo <b>político</b> de solução de "
     "controvérsias (arts. 6º e 7º do Protocolo de Olivos), emitindo "
     "recomendação não vinculante. [Exercício Q01-III, Rodada 02 Abr/2025]"),

    ("IV – No Protocolo de Olivos para a Solução de Controvérsias no "
     "Mercosul, há previsão de adoção de medidas provisórias por tribunal ad "
     "hoc constituído no âmbito do referido tratado. (C/E?)",
     "<b>CERTO.</b> O art. 15 do Protocolo de Olivos prevê que o Estado "
     "litigante interessado pode solicitar que o tribunal ad hoc emita "
     "medidas provisórias antes da confecção do laudo, para prevenir danos "
     "irreparáveis — desde que provocado pela parte interessada (não pode "
     "ser de ofício). [Exercício Q01-IV, Rodada 02 Abr/2025]"),

    ("I – O Protocolo de Olivos de 2002 inovou no Direito Internacional ao "
     "instituir, de modo inédito, a noção de duplo grau de jurisdição para "
     "solução de controvérsias entre Estados soberanos, o que pode ocorrer "
     "por meio do emprego do direito de recurso endereçado ao Tribunal "
     "Permanente de Revisão (TPR) para os contenciosos do bloco. (C/E?)",
     "<b>ERRADO.</b> O duplo grau de jurisdição não foi criado pelo "
     "Protocolo de Olivos — já existia no sistema de solução de "
     "controvérsias da <b>OMC</b> desde meados da década de 1990, exercido "
     "pelo Órgão de Apelação. [Exercício Q02-I, Rodada 02 Abr/2025]"),

    ("II – O Protocolo de Olivos para a Solução de Controvérsias no Mercosul "
     "não permite que uma decisão adotada por órgão de solução de "
     "controvérsias do Mercosul seja objeto de recurso ao Órgão de Apelação "
     "da OMC. (C/E?)",
     "<b>CERTO.</b> Pelo art. 1º, nº 2, uma vez escolhido o sistema de "
     "solução de controvérsias do Mercosul, não se pode empregar outros "
     "mecanismos — a liberdade de escolha é prévia ao início da análise da "
     "controvérsia. [Exercício Q02-II, Rodada 02 Abr/2025]"),

    ("III – Segundo esse tratado, os Estados-parte é permitido recorrer, de "
     "comum acordo, diretamente ao Tribunal Permanente de Revisão, desde que "
     "ocorra o esgotamento da via arbitral ad hoc. (C/E?)",
     "<b>ERRADO.</b> O art. 23 prevê o <b>acesso direto</b> ao TPR: os "
     "Estados, de comum acordo, decidem NÃO empregar o tribunal ad hoc, "
     "acessando o TPR diretamente como instância única — o esgotamento do "
     "ad hoc é exigido apenas para acionar a instância revisora (duplo grau), "
     "não o acesso direto. [Exercício Q02-III, Rodada 02 Abr/2025]"),

    ("IV – Nesse protocolo, é vedado, assim como na Corte Internacional de "
     "Justiça (CIJ), o uso por particulares do mecanismo de solução de "
     "controvérsias. (C/E?)",
     "<b>ERRADO.</b> Embora particulares não tenham acesso ao tribunal ad "
     "hoc nem ao TPR (assim como na CIJ, restrita a Estados), o Protocolo de "
     "Olivos (arts. 39-44) permite que particulares apresentem "
     "<b>reclamação</b> ao Grupo Mercado Comum — via que não existe na CIJ. "
     "[Exercício Q02-IV, Rodada 02 Abr/2025]"),

    ("I – As reclamações de particulares são analisadas pela Seção Nacional "
     "do Grupo Mercado Comum (GMC) e posteriormente encaminhadas ao Grupo de "
     "Especialistas designado pelo GMC, se consideradas procedentes. (C/E?)",
     "<b>CERTO.</b> Fluxo correto: (i) reclamação à Seção Nacional do GMC; "
     "(ii) consultas entre seções nacionais; (iii) se não resolvido, "
     "submissão ao GMC; (iv) se admitida, constituição de Grupo de "
     "Especialistas que emite parecer não vinculante. "
     "[Exercício Q03-I, Rodada 02 Abr/2025]"),

    ("II – Compete ao Tribunal Permanente de Revisão do Mercosul, instituído "
     "por meio do Protocolo de Ouro Preto, julgar, em última instância, os "
     "recursos interpostos contra decisões de tribunais ad hoc prolatadas em "
     "procedimentos de arbitragem instaurados para a solução de "
     "controvérsias entre os Estados-partes do Mercosul relativas à "
     "interpretação, à aplicação ou ao não cumprimento das normas desse "
     "bloco econômico. (C/E?)",
     "<b>ERRADO.</b> O TPR não foi criado pelo Protocolo de Ouro Preto "
     "(1994) — foi previsto pelo <b>Protocolo de Olivos</b> (2002). A "
     "função revisora descrita está correta, mas a origem normativa "
     "apontada está errada. [Exercício Q03-II, Rodada 02 Abr/2025]"),

    ("III – As controvérsias entre Estados-Membros sobre a interpretação ou "
     "a aplicação do Tratado de Assunção e do Protocolo de Ouro Preto são "
     "sempre decididas pela unanimidade dos seus membros. (C/E?)",
     "<b>ERRADO.</b> É preciso distinguir: o órgão <b>político</b> (GMC) "
     "decide por consenso/unanimidade (art. 37, Protocolo de Ouro Preto), "
     "mas os órgãos <b>jurisdicionais</b> (tribunal ad hoc e TPR) decidem "
     "por <b>maioria</b> (art. 25, Protocolo de Olivos) — não há regra "
     "única de unanimidade para todas as controvérsias. "
     "[Exercício Q03-III, Rodada 02 Abr/2025]"),

    ("IV – A legitimidade para provocar a competência consultiva atribuída "
     "ao Tribunal Permanente de Revisão (TPR), na atualidade, não se "
     "restringe aos órgãos com capacidade decisória do Mercosul e aos "
     "Tribunais Superiores dos Estados-membros do bloco regional. (C/E?)",
     "<b>CERTO.</b> Pelas Decisões CMC nº 05/2022 e nº 06/2022, também têm "
     "legitimidade os Estados-partes atuando conjuntamente e o "
     "<b>Parlasul</b> (Parlamento do Mercosul), além dos órgãos decisórios "
     "e dos tribunais superiores com jurisdição nacional. "
     "[Exercício Q03-IV, Rodada 02 Abr/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Mercosul - Sistema de Solução de Controvérsias",
        "Direito Internacional - Mercosul - Sistema de Solução de Controvérsias.apkg",
        MERCOSUL_SOLUCAO_CONTROVERSIAS,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
