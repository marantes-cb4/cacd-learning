#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Dez/2025).

Tema: Proibição do Uso da Força. Prática Diplomática Brasileira.
Segurança Coletiva. Operações de Manutenção da Paz (Item 27 do Edital CACD).

Fontes:
  - Anotações: Proibição do Uso da Força.md
  - Material do professor: Direito Internacional_Rodada 01_Dezembro_2025_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Dezembro_2025.pdf
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


PROIBICAO_USO_DA_FORCA = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O jus in bello, enquanto ramo do direito internacional humanitário, deixa "
     "de ser aplicável a um conflito armado sempre que o uso da força por um dos "
     "beligerantes for considerado ilegal perante o Direito Internacional, uma vez "
     "que o direito na guerra pressupõe a licitude do jus ad bellum que o originou.",
     "<b>ERRADO.</b> O jus in bello é aplicável em <b>todas</b> as situações de "
     "conflito armado, sendo irrelevante se o uso da força foi legal (legítima "
     "defesa, operação de paz) ou ilegal. Aplica-se integralmente a combatentes, "
     "população civil e território de todas as partes envolvidas, ainda que uma "
     "delas tenha dado origem ao conflito por violação do jus ad bellum. "
     "[Anotações da aula; Rodada 01/Dez.2025, p.10]"),

    ("A Comissão de Direito Internacional da ONU (CDI), em estudo publicado em "
     "1996, manifestou o entendimento de que a proibição do uso da força "
     "constitui norma de jus cogens, sendo, portanto, vinculante para todos os "
     "Estados soberanos independentemente de seu consentimento (erga omnes).",
     "<b>CERTO.</b> Entendimento defendido por Antônio Augusto Cançado Trindade "
     "no âmbito da CDI. Como norma imperativa (jus cogens), a proibição do uso da "
     "força vincula erga omnes — diferindo das normas dispositivas (voluntarismo), "
     "que só obrigam enquanto houver vontade do Estado. "
     "[Anotações da aula; Rodada 01/Dez.2025, p.1]"),

    ("Na prática recente do Conselho de Segurança da ONU, o conceito de paz "
     "utilizado para autorizar operações de manutenção da paz é restrito à "
     "ausência de conflito armado interestatal, não abrangendo a promoção de "
     "direitos humanos ou do direito internacional humanitário.",
     "<b>ERRADO.</b> O CSNU adota um <b>conceito alargado</b> de paz, que também "
     "engloba a promoção de valores relativos aos direitos humanos e ao direito "
     "humanitário. Isso permite conceder mandato para operações de paz em "
     "contextos de violação de DH mesmo sem risco concreto de uso da força entre "
     "Estados. [Anotações da aula; Rodada 01/Dez.2025, p.11 e 18-19]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Dez/2025) ─────────────────

    ("I – Considere, por hipótese, que o Estado G, prevendo o avanço da indústria "
     "bélica do Estado fronteiriço V, passou a considerá-lo uma futura ameaça à "
     "sua segurança. Nessa hipótese, o Estado G poderá intervir legitimamente no "
     "Estado V. (C/E?)",
     "<b>ERRADO.</b> O direito à legítima defesa (origem consuetudinária, Caso "
     "Caroline) exige <b>necessidade</b> (prova de agressão ou tentativa concreta) "
     "e <b>proporcionalidade</b>. Na hipótese não há ataque nem tentativa "
     "concreta — apenas previsão de ameaça futura —, o que configura legítima "
     "defesa <b>preventiva</b>, vedada pelo Direito Internacional. "
     "[Exercício Q01-I, Rodada 01 Dez/2025]"),

    ("II – Como é vedado o uso da força nas relações internacionais, a Carta da "
     "ONU de 1945 determina que os Estados não podem executar atos beligerantes "
     "com o aval do direito internacional, ressalvada somente as hipóteses de "
     "legítima defesa em caso de agressão externa e de operações de paz caso "
     "sejam determinadas pela Assembleia Geral da ONU. (C/E?)",
     "<b>ERRADO.</b> A Carta proíbe o uso da força (art. 2º, §4º) admitindo duas "
     "exceções: legítima defesa (art. 51) e operações de paz sob mandato das "
     "Nações Unidas (art. 42). A competência primária para autorizar operações de "
     "paz é do <b>CSNU</b>, não da Assembleia Geral — que só atua "
     "excepcionalmente, em caso de paralisia do CSNU (Resolução Unidos pela Paz, "
     "nº 377). [Exercício Q01-II, Rodada 01 Dez/2025]"),

    ("III – Conforme o entendimento amplamente dominante na teoria e na prática "
     "do direito internacional, o direito à legítima defesa, cuja fonte é "
     "consuetudinária, pode ser exercido individual ou coletivamente, sendo "
     "defeso seu empregado por Estados soberanos em face de grupos armados não "
     "estatais. (C/E?)",
     "<b>CERTO.</b> A CIJ tem entendimento consolidado (Casos Nicarágua 1986, "
     "Congo 1993, Opinião Consultiva do Muro 2004) de que a legítima defesa só "
     "pode ser exercida em relações <b>interestatais</b> — ataques por grupos "
     "armados não vinculados a Estados soberanos não autorizam seu exercício. "
     "[Exercício Q01-III, Rodada 01 Dez/2025]"),

    ("IV – Com a evolução da prática e da doutrina internacionais relacionadas ao "
     "direito à legítima defesa consagrado na Carta das Nações Unidas, o conceito "
     "de legítima defesa preventiva passou a ser aceito por crescente número de "
     "países, inclusive pelo Brasil. (C/E?)",
     "<b>ERRADO.</b> A doutrina majoritária e a prática diplomática brasileira "
     "<b>não</b> admitem o exercício da legítima defesa fora das hipóteses "
     "expressas do art. 51 (ataque armado ou tentativa concreta). O Direito "
     "Internacional não chancela a legítima defesa antecipatória — nem preventiva "
     "nem preemptiva. [Exercício Q01-IV, Rodada 01 Dez/2025]"),

    ("I – A aplicação do princípio da defesa da paz evidencia-se, entre outros "
     "meios, pela postura crítica do Brasil às tentativas de avanço das "
     "interpretações expansivas do direito à legítima defesa, previsto na Carta "
     "das Nações Unidas. (C/E?)",
     "<b>CERTO.</b> Em nome do princípio da defesa da paz (art. 4º, VI, CF/88), "
     "o Brasil refuta a ampliação do conceito de legítima defesa (preventiva/"
     "preemptiva) e prima pela interpretação restritiva do art. 51. "
     "[Exercício Q02-I, Rodada 01 Dez/2025]"),

    ("II – Segundo a Carta das Nações Unidas, o exercício do direito à legítima "
     "defesa por Estado-membro das Nações Unidas deve ser informado imediatamente "
     "ao Conselho de Segurança e restringe as ações desse órgão da ONU na tomada "
     "de providências para manter ou restabelecer a paz e a segurança "
     "internacionais. (C/E?)",
     "<b>ERRADO.</b> A comunicação ao CSNU é obrigatória (art. 51), mas as "
     "medidas de legítima defesa adotadas pelo Estado <b>não restringem</b> a "
     "competência decisória do CSNU — pelo contrário, o Conselho mantém plena "
     "autoridade para adotar as medidas que julgar necessárias. "
     "[Exercício Q02-II, Rodada 01 Dez/2025]"),

    ("III – As medidas de retorsão no direito internacional consistem em ações "
     "que produzem efeitos desfavoráveis sobre o Estado visado, mas são lícitas "
     "e oriundas da competência discricionária do Estado prolator da medida. "
     "(C/E?)",
     "<b>CERTO.</b> A retorsão é resposta (contramedida) a um ato <b>lícito</b> "
     "de outro Estado que contraria interesses políticos/econômicos; é ato "
     "unilateral e discricionário do Estado, materializado por medidas "
     "legislativas/administrativas, sem violar o DI. "
     "[Exercício Q02-III, Rodada 01 Dez/2025]"),

    ("IV – Considerando que o governo de dado país passou a restringir a entrada "
     "de cidadãos de outro país em seus controles de imigração por meio de "
     "exigências documentais extensivas e, em resposta, o governo deste tornou "
     "mais rigoroso o controle de imigração para os cidadãos daquele, essa "
     "situação ilustra o meio coercitivo denominado de represália. (C/E?)",
     "<b>ERRADO.</b> A situação descreve resposta a um ato <b>lícito</b> "
     "(controle de imigração é ato lícito do Estado), o que caracteriza "
     "<b>retorsão</b>, não represália — que pressupõe resposta a um ato ilícito. "
     "[Exercício Q02-IV, Rodada 01 Dez/2025]"),

    ("I – Mesmo sem declaração de guerra, o envio de tropas das Forças Armadas "
     "para fora do território nacional só poderá ser realizado com autorização "
     "do Congresso Nacional. (C/E?)",
     "<b>ERRADO.</b> A regra geral exige autorização do CN, mas a Lei nº "
     "2.953/1956 prevê duas exceções que a dispensam: (a) resposta a invasão/"
     "agressão estrangeira (legítima defesa); (b) defesa do litoral brasileiro "
     "dentro da zona de segurança aérea/marítima. O termo \"só poderá\" ignora "
     "essas exceções. [Exercício Q03-I, Rodada 01 Dez/2025]"),

    ("II – Devido à ausência de previsão expressa no texto da Carta da ONU, o "
     "Brasil tem por princípio não participar de operações de paz da ONU ou de "
     "só fazê-lo com autorização do Congresso Nacional. (C/E?)",
     "<b>ERRADO.</b> A doutrina diverge sobre o fundamento jurídico das operações "
     "de paz (poderes implícitos vs. arts. 41/42), mas isso não leva o Brasil a "
     "recusar participação — a prática brasileira é <b>participar</b> de missões "
     "de paz, sempre com a devida autorização do Congresso Nacional. "
     "[Exercício Q03-II, Rodada 01 Dez/2025]"),

    ("III – As operações de manutenção de paz, desde sua origem até os dias de "
     "hoje, podem ser empregadas apenas em situações de conflito entre Estados, "
     "não sendo autorizada sua adoção, pelo Conselho de Segurança, para situações "
     "de conflitos internos ou guerras civis, o que seria considerado ação "
     "intervencionista. (C/E?)",
     "<b>ERRADO.</b> O CSNU adota um <b>conceito alargado</b> de paz, que "
     "autoriza operações também em contextos de conflitos internos, guerras "
     "civis e violação de direitos humanos — não se restringe a conflitos "
     "interestatais. [Exercício Q03-III, Rodada 01 Dez/2025]"),

    ("IV – Consentimento das partes, imparcialidade e proibição do uso da força "
     "– a não ser em legítima defesa e em defesa do mandato – são os três "
     "princípios básicos das operações de manutenção de paz da ONU. (C/E?)",
     "<b>CERTO.</b> Os três fundamentos estruturais das operações de paz da ONU "
     "são exatamente esses: consentimento das partes, não uso da força (salvo "
     "legítima defesa/defesa do mandato) e imparcialidade. "
     "[Exercício Q03-IV, Rodada 01 Dez/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Proibição do Uso da Força",
        "Direito Internacional - Proibição do Uso da Força.apkg",
        PROIBICAO_USO_DA_FORCA,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
