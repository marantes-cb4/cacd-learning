#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Humanitário.

Tema: Conflitos armados e o Direito Internacional. Direito Internacional
Humanitário. Direito Internacional dos Refugiados (Item 29 do Edital
CACD — porção de Direito Internacional Humanitário).

Fontes:
  - Anotações: Direito Internacional Humanitário.md
  - Material do professor: Direito Internacional_Rodada 02_Fevereiro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 02_Fevereiro_2024.pdf
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


DIREITO_INTERNACIONAL_HUMANITARIO = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O Direito de Haia de 1907 e o Direito de Genebra de 1949 disciplinam "
     "o mesmo aspecto dos conflitos armados, qual seja, a proteção dos "
     "indivíduos que se encontram fora de combate — feridos, doentes e "
     "prisioneiros de guerra —, diferenciando-se apenas quanto ao período "
     "histórico de sua adoção.",
     "<b>ERRADO.</b> Regulam aspectos DIFERENTES: o Direito de "
     "<b>Haia</b> disciplina a CONDUÇÃO das hostilidades entre combatentes "
     "ATIVOS (ex.: emprego de armamentos); o Direito de <b>Genebra</b> "
     "protege quem está FORA de combate (feridos, prisioneiros) e a "
     "população civil. [Anotações da aula; Rodada 02/Fev.2024, p.15]"),

    ("O Direito Internacional Humanitário aplica-se de modo uniforme a "
     "toda situação de conflito armado, sendo indiferente, para fins de "
     "definição de quais instrumentos normativos incidem sobre o caso, "
     "tratar-se de guerra entre Estados soberanos, de conflito envolvendo "
     "um Estado e um movimento de libertação nacional, ou de conflito "
     "interno entre forças de um único Estado.",
     "<b>ERRADO.</b> Os instrumentos aplicáveis VARIAM: <b>guerra</b> "
     "(entre Estados) → as 4 Convenções de Genebra completas; "
     "<b>conflito internacional</b> (Estado + outro sujeito do DIP, ex.: "
     "movimento de libertação nacional) → art. 3º comum + Protocolo "
     "Adicional I; <b>conflito não internacional</b> (só atores "
     "intra-estatais) → art. 3º comum + Protocolo Adicional II. "
     "[Anotações da aula; Rodada 02/Fev.2024]"),

    ("No Parecer Consultivo de 1996 sobre a legalidade da ameaça ou do uso "
     "de armas nucleares, a Corte Internacional de Justiça reconheceu que "
     "o Direito de Haia e o Direito de Genebra tornaram-se tão "
     "intimamente inter-relacionados que passaram a constituir um único "
     "sistema complexo, hoje conhecido como direito humanitário "
     "internacional — e que o uso de armas nucleares seria legal apenas "
     "se restrito às hipóteses admitidas pela Carta da ONU e observados os "
     "princípios da proporcionalidade e razoabilidade.",
     "<b>CERTO.</b> A CIJ uniu formalmente os dois ramos no conceito "
     "moderno de direito humanitário internacional (jus in bello), "
     "condicionando a legalidade do uso de armas nucleares às hipóteses da "
     "Carta da ONU (legítima defesa/autorização do CSNU) e aos princípios "
     "da proporcionalidade e razoabilidade. [Anotações da aula; Rodada "
     "02/Fev.2024, p.12]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Fev/2024) ──────────────

    ("01-I – O direito humanitário, a criação da Liga das Nações e a "
     "criação da Organização Internacional do Trabalho são apontados pela "
     "doutrina como antecedentes históricos do moderno direito "
     "internacional dos direitos humanos. (C/E?)",
     "<b>CERTO.</b> O DIDH moderno surge só após 1945, mas DIH (1864), "
     "Liga das Nações (1919) e OIT são citados como antecedentes "
     "históricos importantes. [Exercício Q01-I, Rodada 02 Fev/2024]"),

    ("01-II – O direito internacional de proteção da pessoa humana, como "
     "conceito abrangente, abarca, ao mesmo tempo, a proteção dos direitos "
     "humanos dos refugiados e os direitos humanos em tempos de paz, além "
     "das disposições de proteção aos combatentes postos fora de combate "
     "por captura ou ferimento durante a guerra. (C/E?)",
     "<b>CERTO.</b> É exatamente a soma das 3 subáreas: DIDH (paz), DIH "
     "(combatentes fora de combate) e DIR (refugiados). [Exercício "
     "Q01-II, Rodada 02 Fev/2024]"),

    ("01-III – O direito humanitário abrange as prescrições ligadas à "
     "proteção dos civis durante os conflitos internacionais, conforme se "
     "constata em uma convenção específica sobre o tema adotada em 1949 e "
     "que integra o chamado Direito de Genebra. (C/E?)",
     "<b>CERTO.</b> A 4ª Convenção de Genebra de 1949 trata "
     "especificamente da proteção dos civis em tempo de guerra. "
     "[Exercício Q01-III, Rodada 02 Fev/2024]"),

    ("01-IV – A doutrina estabelece diferenças substanciais entre as "
     "expressões direitos humanos e direito humanitário, tendo este sido "
     "criado a partir da intensa atuação do Comitê Internacional da Cruz "
     "Vermelha, organização governamental, sediada em Genebra. (C/E?)",
     "<b>ERRADO.</b> O CICV NÃO é organização governamental/internacional "
     "— surgiu como entidade da sociedade civil suíça e é hoje "
     "considerado um sujeito secundário do DIP, entidade <i>sui "
     "generis</i>. [Exercício Q01-IV, Rodada 02 Fev/2024]"),

    ("02-I – O direito humanitário foi responsável pelo redimensionamento "
     "das relações do Estado com a pessoa humana, tendo reforçado a "
     "soberania estatal e, ao mesmo tempo, representado sensibilidade por "
     "parte dos Estados em relação às agruras e necessidades de "
     "combatentes e civis envolvidos em guerras. (C/E?)",
     "<b>ERRADO.</b> O DIH (como as demais subáreas de proteção da pessoa "
     "humana) representa um LIMITE à soberania estatal, não um reforço "
     "dela. [Exercício Q02-I, Rodada 02 Fev/2024]"),

    ("02-II – Conforme a doutrina, na ausência de previsão específica em "
     "norma internacional de direito humanitário, deve-se, "
     "subsidiariamente, aplicar as normas internacionais de direitos "
     "humanos, uma vez que estas constituem lex specialis e aquelas lex "
     "generalis. (C/E?)",
     "<b>ERRADO.</b> É o INVERSO: DIDH é <i>lex generalis</i> (aplicado "
     "subsidiariamente), e DIH/DIR são <i>lex specialis</i>. [Exercício "
     "Q02-II, Rodada 02 Fev/2024]"),

    ("02-III – De acordo com a cláusula de Martens, deve-se observar a "
     "proibição universal dos Estados devolverem um refugiado ou "
     "requerente de asilo para um país onde exista o risco de ser "
     "perseguido ou ser sujeito a tortura ou outros tratamentos cruéis, "
     "desumanos e degradantes. (C/E?)",
     "<b>ERRADO.</b> Isso descreve o princípio do <i>non-refoulement</i> "
     "(norma especial do Direito dos Refugiados), não a Cláusula Martens "
     "(que trata da aplicação subsidiária de normas GERAIS quando não há "
     "norma especial). [Exercício Q02-III, Rodada 02 Fev/2024]"),

    ("02-IV – A assistência humanitária, na forma de ações de socorro "
     "emergencial de índole humanitária, imparcial e não-discriminatória, "
     "é direito previsto pelo direito internacional humanitário, que pode "
     "ser levado a cabo por Estados, organizações internacionais e "
     "organizações não-governamentais. (C/E?)",
     "<b>CERTO.</b> Estados, OIs e ONGs (ex.: Médicos Sem Fronteiras) "
     "podem prestar assistência humanitária — o CICV tem atuação "
     "destacada, mas sem exclusividade. [Exercício Q02-IV, Rodada 02 "
     "Fev/2024]"),

    ("03-I – O jus in bello abarca normas internacionais que regulam o "
     "emprego de armas de alto potencial destrutivo em conflitos armados e "
     "abrange as normas de direito humanitário. (C/E?)",
     "<b>CERTO.</b> O jus in bello reúne Direito de Haia de 1907 (conduta "
     "das hostilidades, armamentos) e Direito de Genebra de 1949 "
     "(proteção humanitária). [Exercício Q03-I, Rodada 02 Fev/2024]"),

    ("03-II – O jus ad bellum diz respeito ao direito de promover a guerra "
     "conforme o direito internacional, a saber, nas hipóteses da defesa "
     "de um Estado contra agressões externas e da tomada de decisão do "
     "Conselho de Segurança da ONU para evitar a guerra ou reestabelecer a "
     "paz internacional. (C/E?)",
     "<b>CERTO.</b> Hoje o jus ad bellum só existe nas 2 exceções da Carta "
     "da ONU: legítima defesa e autorização do CSNU (Capítulo VII). "
     "[Exercício Q03-II, Rodada 02 Fev/2024]"),

    ("03-III – O Direito Internacional Humanitário é aplicável aos "
     "conflitos armados nos quais os povos lutam contra a dominação "
     "colonial, a ocupação estrangeira e contra os regimes racistas. (C/E?)",
     "<b>CERTO.</b> É o campo de aplicação do Protocolo Adicional I de "
     "1977 (conflitos internacionais envolvendo movimentos de libertação "
     "nacional). [Exercício Q03-III, Rodada 02 Fev/2024]"),

    ("03-IV – O direito internacional humanitário tem sua implementação "
     "assegurada por tribunais internacionais, a exemplo do Tribunal "
     "Penal Internacional e da Corte Internacional de Justiça, ambos "
     "habilitados a aplicar sanções em relação aos indivíduos que, ao "
     "atuar em guerras, conflitos internacionais e conflitos não "
     "internacionais, violam o conteúdo do direito de Genebra. (C/E?)",
     "<b>ERRADO.</b> A CIJ julga apenas <b>Estados</b> — não julga "
     "indivíduos. Só o <b>TPI</b> julga indivíduos por crimes de guerra "
     "(art. 8º, Estatuto de Roma). [Exercício Q03-IV, Rodada 02 Fev/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Direito Internacional Humanitário",
        "Direito Internacional - Direito Internacional Humanitário.apkg",
        DIREITO_INTERNACIONAL_HUMANITARIO,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
