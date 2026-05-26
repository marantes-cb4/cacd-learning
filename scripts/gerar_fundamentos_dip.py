#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Fev/2024).

Tema: Fundamentos e Validade do DIP — Voluntarismo, Objetivismo,
Monismo, Dualismo e aplicação no Brasil (Item 15 do Edital CACD).

Fontes:
  - Anotações: Fundamentos DIP.md
  - Material do professor: Direito Internacional_Rodada 01_Fevereiro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Fevereiro_2024.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/direito"
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


FUNDAMENTOS_DIP = [

    # ── VOLUNTARISMO ──────────────────────────────────────────────────────────

    ("Quais são as duas correntes que justificam o caráter jurídico do DIP?",
     "<b>Voluntarismo</b> e <b>Objetivismo</b>. São aplicadas de modo combinado — "
     "o DIP atual não pode ser compreendido por completo por apenas uma delas. "
     "[Portela, Dir. Int. Público e Privado, Cap. I, Item 5]"),

    ("Qual o pressuposto central do voluntarismo?",
     "Normas internacionais só são válidas e existentes se refletirem a <b>vontade dos "
     "Estados soberanos</b> que participaram de sua criação ou a ela aderiram. "
     "Apregoa a imprescindibilidade do consentimento estatal. "
     "[Portela, Cap. I, Item 5]"),

    ("O que é consentimento criativo e quais suas duas formas? (voluntarismo)",
     "Consentimento dos Estados para que uma norma internacional seja criada: "
     "<b>expresso</b> → explica o surgimento de <b>tratados</b>; "
     "<b>tácito</b> → explica o surgimento do <b>costume internacional</b>. "
     "[Portela, Cap. I, Item 5]"),

    ("O que são normas internacionais dispositivas? A qual corrente se ligam?",
     "Normas vinculantes <b>apenas enquanto existir vontade</b> dos Estados; "
     "podem ser denunciadas (ex.: retirada de tratado) ou substituídas por novo costume. "
     "Ligam-se ao <b>voluntarismo</b>. "
     "Atenção: nas provas, voluntarismo = consentimento criativo = normas dispositivas. "
     "[Portela, Cap. I, Item 5]"),

    ("Qual a crítica central ao voluntarismo? (Guido Fernando Silva Soares)",
     "Exacerba a noção de soberania a ponto de minimizar conceitos como interesse "
     "comum da humanidade e comunidade internacional; não consegue explicar como "
     "costumes e princípios gerais obrigam Estados que não participaram de sua formação. "
     "[Soares, Curso de Dir. Int. Público, vol. 1, pp. 52-53]"),

    # ── OBJETIVISMO ───────────────────────────────────────────────────────────

    ("Qual o pressuposto central do objetivismo?",
     "Existem normas internacionais obrigatórias <b>independentemente da vontade dos "
     "Estados soberanos</b>; fundamentam-se em <b>valores jurídicos</b> que permeiam "
     "a comunidade internacional como um todo. "
     "[Portela, Cap. I, Item 5]"),

    ("O que é consentimento perceptivo? (objetivismo)",
     "Critério pelo qual normas criadas pelos Estados (tratados, costumes) só são válidas "
     "se <b>não contrariarem os valores jurídicos objetivos da sociedade internacional</b>. "
     "É o conceito central do objetivismo. "
     "Atenção: objetivismo = consentimento perceptivo = normas imperativas/jus cogens. "
     "[Portela, Cap. I, Item 5]"),

    ("Qual o resultado jurídico do objetivismo no direito positivo?",
     "A consagração do <b>jus cogens</b> (normas imperativas / peremptórias): "
     "art. 53 CVDT/1969 — tratados que conflitem com jus cogens são nulos; "
     "art. 64 CVDT/1969 — nova jus cogens torna nulos os tratados preexistentes contrários. "
     "[Portela, Cap. I, Item 5]"),

    ("Quais são exemplos de normas de jus cogens apontados pela doutrina?",
     "Pacta sunt servanda; proibição do uso da força; soberania e igualdade dos Estados; "
     "autodeterminação dos povos; proibição do tráfico de seres humanos; proibição da "
     "pirataria; proibição do genocídio; crimes contra a humanidade; DIH (Convenções de "
     "Genebra); princípios fundamentais de DH e do meio ambiente. "
     "[Nasser, Jus Cogens, Revista Dir. FGV, v.1, n.2, 2005, p. 165]"),

    # ── TERMINOLOGIA ──────────────────────────────────────────────────────────

    ("Qual a relação entre normas positivas, dispositivas e imperativas?",
     "<b>Positivas</b> = gênero: normas obrigatórias/vinculantes. "
     "Espécies: <b>dispositivas</b> (vinculam enquanto houver vontade — voluntarismo) e "
     "<b>imperativas/jus cogens</b> (vinculam independentemente da vontade — objetivismo). "
     "Normas codificadas = escritas (tratados, resoluções). "
     "Não codificadas = não escritas (costumes, atos unilaterais). "
     "[Portela, Cap. I, Item 6]"),

    # ── MONISMO ───────────────────────────────────────────────────────────────

    ("O que é monismo e quais suas duas consequências jurídicas?",
     "Concepção de que existe uma <b>única ordem jurídica</b> congregando normas internas "
     "e internacionais. Consequências: (i) norma internacional tem <b>aplicação imediata</b> "
     "(sem processo de incorporação); (ii) surgem <b>antinomias</b> entre normas internas "
     "e internacionais, resolvidas conforme a variação adotada. "
     "[Portela, Cap. I, Item 8]"),

    ("Quais são as três variações do monismo?",
     "<b>Nacionalista</b>: antinomia resolvida com prevalência da norma <b>interna</b> "
     "(Kelsen — vertente nacional). "
     "<b>Internacionalista</b>: prevalece a norma <b>internacional</b> (Kelsen — vertente "
     "internacionalista; expoente maior). "
     "<b>Internacionalista dialógico</b>: em matéria de DH, aplica-se a norma <b>mais "
     "favorável ao indivíduo</b> (pro homine), seja interna ou internacional. "
     "[Portela, Cap. I, Item 8]"),

    ("O que é o princípio pro homine e a qual corrente se liga?",
     "Em conflitos normativos envolvendo <b>direitos humanos</b>, aplica-se sempre a norma "
     "mais favorável ao indivíduo, independentemente de ser interna ou internacional. "
     "Fundamenta o <b>monismo internacionalista dialógico</b>. Base: CADH art. 29(b). "
     "[Mazzuoli, Curso de Dir. Int. Público, 7ª ed., p. 102]"),

    # ── DUALISMO ──────────────────────────────────────────────────────────────

    ("O que é dualismo e quais suas duas consequências jurídicas?",
     "Concepção de que existem <b>duas ordens jurídicas totalmente estanques e "
     "incomunicáveis</b>: interna e internacional. Consequências: (i) <b>não há antinomias</b> "
     "entre normas internacionais e internas (pertencem a ordens distintas); "
     "(ii) norma internacional <b>precisa ser transformada</b> em norma interna para ter "
     "aplicação no plano doméstico. "
     "[Portela, Cap. I, Item 8]"),

    ("Quais são as duas variações do dualismo?",
     "<b>Radical</b>: transformação exige elaboração de <b>lei formal</b> (todo o processo "
     "legislativo — proposta, discussão, votação, sanção, promulgação). "
     "<b>Moderado</b>: transformação por ato mais simples, como <b>decreto presidencial</b>. "
     "Principais teóricos dualistas: Triepel (Alemanha) e Anzilotti (Itália). "
     "[Portela, Cap. I, Item 8]"),

    # ── BRASIL ────────────────────────────────────────────────────────────────

    ("Como o Brasil trata normas internacionais NÃO CODIFICADAS (não escritas)?",
     "<b>Monismo nacionalista</b>: aplicação <b>imediata</b>, sem necessidade de incorporação. "
     "São elas: costumes, princípios gerais do direito das nações civilizadas e atos "
     "unilaterais de Estado (ex.: declarações orais de chefes de Estado). "
     "Em caso de antinomia, prevalece a <b>CF/88</b> (não há normas supraconstitucionais no BR). "
     "[Portela, Cap. I, Item 8; STF]"),

    ("Como o Brasil trata normas internacionais CODIFICADAS (escritas)?",
     "<b>Dualismo moderado</b>: exigem processo de incorporação por <b>decreto presidencial</b>. "
     "Aplicável a: (a) tratados e convenções internacionais; "
     "(b) resoluções/decisões de organizações internacionais (ONU-AG, CSNU, OIT, Mercosul etc.). "
     "[Portela, Cap. I, Item 8; STF]"),

    ("Qual a exceção ao dualismo moderado no Brasil? (norma codificada com aplicação imediata)",
     "Resoluções do <b>Conselho de Segurança da ONU para combate ao terrorismo</b>: "
     "dotadas de <b>executoriedade imediata</b> na ordem jurídica brasileira, "
     "sem necessidade de decreto presidencial. "
     "Base: art. 6º da Lei nº 13.810/2019. "
     "→ Brasil adota <b>monismo nacionalista</b> especificamente para esse caso. "
     "[Lei 13.810/2019, art. 6º]"),

    ("Quais são as 4 etapas de incorporação de tratados ao ordenamento jurídico brasileiro?",
     "1. Negociação e assinatura (Poder Executivo); "
     "2. Referendo/aprovação pelo Congresso Nacional (decreto legislativo — art. 49, I CF); "
     "3. Ratificação internacional (ato do Executivo no plano internacional); "
     "4. Promulgação interna por <b>decreto presidencial</b> (art. 84, IV CF). "
     "[Portela, Cap. I, Item 8; STF]"),

    ("O Direito Constitucional contemporâneo rechaça totalmente normas supraconstitucionais?",
     "<b>Não</b>. Embora o Brasil não admita normas supraconstitucionais, o DC contemporâneo "
     "não exclui essa possibilidade: (i) Estados que adotam monismo internacionalista "
     "admitem prevalência de normas internacionais sobre a CF; "
     "(ii) a União Europeia consagra primado das normas comunitárias sobre as constituições "
     "nacionais (monismo internacionalista regional). "
     "[Portela, Cap. I, Item 8]"),

    # ── JURISPRUDÊNCIA ────────────────────────────────────────────────────────

    ("Crimes contra a humanidade têm caráter de jus cogens no sistema interamericano?",
     "<b>Sim</b> — a Corte IDH reconhece o caráter de jus cogens dos crimes contra a "
     "humanidade (Caso Goiburú, Chitay Nech, Ibsen Cárdenas). Como consequência, "
     "graves violações de DH resultantes desses crimes devem ser investigadas, "
     "processadas e punidas. (STF, Ext 1362, rel. Edson Fachin/Teori Zavascki, 2016)"),

    ("Qual o método hermenêutico para concretizar a liberdade de expressão segundo o STJ?",
     "O postulado <b>pro homine</b>, composto por dois princípios: dignidade da pessoa "
     "humana e prevalência dos direitos humanos. A adesão ao Pacto de São José significa "
     "a transposição de critérios recíprocos de interpretação à ordem jurídica interna. "
     "(STJ, REsp 1.640.084/SP, rel. min. Ribeiro Dantas, 2016)"),

    # ── EXERCÍCIOS DO PROFESSOR (literal) ────────────────────────────────────

    ("I – O consentimento criativo da corrente voluntarista significa que a normatividade "
     "jurídica do direito internacional nasce da pura vontade dos Estados. (C/E?)",
     "<b>CERTO.</b> O voluntarismo tem como ponto central que as normas internacionais são "
     "obrigatórias e vinculantes se refletirem a vontade dos Estados soberanos. "
     "A norma surge a partir do consentimento criativo (expresso → tratados; tácito → "
     "costume), gerando normas dispositivas vinculantes enquanto existir vontade. "
     "[Exercício Q01-I, Rodada 01 Fev/2024]"),

    ("II – Para o objetivismo, as normas internacionais são fundamentadas na noção de "
     "consentimento perceptivo, o que permite afirmar que a obrigatoriedade dessas normas "
     "depende da vontade dos Estados soberanos. (C/E?)",
     "<b>ERRADO.</b> Consentimento perceptivo é conceito do <b>objetivismo</b> — correto. "
     "Mas a obrigatoriedade das normas objetivistas é <b>independente</b> da vontade dos "
     "Estados. O objetivismo afirma que normas que reflitam os valores da comunidade "
     "internacional vinculam os Estados independentemente de seu consentimento. "
     "[Exercício Q01-II, Rodada 01 Fev/2024]"),

    ("III – A existência de normas internacionais dispositivas decorre da concepção "
     "objetivista sobre a validade e existência do direito internacional. (C/E?)",
     "<b>ERRADO.</b> Normas dispositivas decorrem do <b>voluntarismo</b> (consentimento "
     "criativo): vinculam os Estados enquanto existir vontade. "
     "O objetivismo fundamenta as normas <b>imperativas</b> (jus cogens), que vinculam "
     "independentemente da vontade. "
     "[Exercício Q01-III, Rodada 01 Fev/2024]"),

    ("IV – Com a previsão das normas imperativas no art. 53 da Convenção de Viena sobre o "
     "Direito dos Tratados de 1969, a doutrina internacionalista, de modo unânime, adotou "
     "a corrente objetivista para explicar a validade e existência do direito internacional. (C/E?)",
     "<b>ERRADO.</b> As duas correntes são aplicadas de modo <b>combinado</b> — não houve "
     "adoção unânime do objetivismo. O voluntarismo explica a criação de normas por vontade "
     "dos Estados; o objetivismo (art. 53 CVDT) limita essa vontade pelo jus cogens. "
     "As concepções são complementares. "
     "[Exercício Q01-IV, Rodada 01 Fev/2024]"),

    ("I – As correntes teóricas dualistas, ainda que moderadas, apregoam uma visão que "
     "engloba de forma indistinta tratados internacionais, costumes e princípios gerais "
     "de direito. (C/E?)",
     "<b>ERRADO.</b> O dualismo distingue normas conforme o procedimento de incorporação: "
     "tratados → incorporação (ex: decreto presidencial no BR); "
     "costumes e princípios gerais → no Brasil, seguem o monismo nacionalista (aplicação "
     "imediata). O Brasil trata de forma diferenciada cada tipo de norma, não de modo indistinto. "
     "[Exercício Q02-I, Rodada 01 Fev/2024]"),

    ("II – O Direito Constitucional contemporâneo rechaça a existência de normas "
     "supraconstitucionais. (C/E?)",
     "<b>ERRADO.</b> O DC contemporâneo <b>não rechaça totalmente</b> normas "
     "supraconstitucionais. Dois fatores: (i) Estados que adotam monismo internacionalista "
     "admitem primado da norma internacional sobre a CF; (ii) na União Europeia, as normas "
     "comunitárias prevalecem sobre as constituições nacionais — monismo internacionalista "
     "regional. No Brasil, contudo, não há normas supraconstitucionais. "
     "[Exercício Q02-II, Rodada 01 Fev/2024]"),

    ("III – As resoluções do Conselho de Segurança da ONU são dotadas de executoriedade "
     "imediata na ordem jurídica brasileira. (C/E?)",
     "<b>ERRADO.</b> A <b>regra geral</b> é o dualismo moderado: resoluções de OIs "
     "(incluindo o CSNU) exigem decreto presidencial para aplicação interna. "
     "<b>Exceção</b>: apenas as resoluções do CSNU para o <b>combate ao terrorismo</b> "
     "têm executoriedade imediata (art. 6º, Lei 13.810/2019) — monismo nacionalista. "
     "[Exercício Q02-III, Rodada 01 Fev/2024]"),

    ("IV – Considera-se o monismo do tipo internacionalista dialógico uma corrente adequada "
     "para tratar de conflitos normativos que envolvam direitos humanos, visto que poderia "
     "haver a aplicação da norma de direito interno em detrimento da de direito internacional "
     "ou vice-versa. (C/E?)",
     "<b>CERTO.</b> O monismo internacionalista dialógico aplica o princípio <b>pro homine</b>: "
     "em conflitos que envolvam DH, aplica-se a norma mais favorável ao indivíduo, "
     "seja ela interna ou internacional. Pode-se aplicar a norma interna em detrimento "
     "da internacional, ou vice-versa. Base: CADH art. 29(b). "
     "[Exercício Q02-IV, Rodada 01 Fev/2024]"),

    ("I – A corrente objetivista sobre a validade e existência do direito internacional "
     "preconiza que o direito interno e o direito internacional constituem uma única "
     "ordem jurídica. (C/E?)",
     "<b>ERRADO.</b> A proposta de <b>única ordem jurídica</b> é do <b>monismo</b>, "
     "que trata da <b>relação</b> entre DI e DI. O objetivismo trata do <b>fundamento</b> "
     "(validade e existência) das normas internacionais — afirma que certas normas vinculam "
     "independentemente da vontade dos Estados, mas não fala em ordem jurídica única. "
     "[Exercício Q03-I, Rodada 01 Fev/2024]"),

    ("II – A teoria adotada no Brasil no que respeita à aplicação de normas internacionais "
     "não codificadas é o monismo, segundo a qual é prescindível promover a incorporação de "
     "normas internacionais em normas internas, tendo o STF decidido pela prevalência das "
     "normas internas sobre o direito internacional. (C/E?)",
     "<b>CERTO.</b> Para normas não codificadas (costumes, princípios gerais, atos "
     "unilaterais), o Brasil adota <b>monismo nacionalista</b>: aplicação imediata "
     "(prescinde de incorporação) e, em caso de antinomia com normas internas, "
     "prevalece a <b>CF/88</b> — não há normas supraconstitucionais no ordenamento brasileiro. "
     "[Exercício Q03-II, Rodada 01 Fev/2024]"),

    ("III – Os postulados do dualismo convergem para a conclusão de que não é possível "
     "existir conflitos entre as normas internacionais e as normas internas. (C/E?)",
     "<b>CERTO.</b> No dualismo, as duas ordens são totalmente estanques e incomunicáveis — "
     "não há antinomia direta entre norma internacional e norma interna. "
     "Os conflitos que surgem no dualismo opõem <b>duas normas internas</b>: "
     "a norma interna pura e a norma interna criada a partir da transformação de uma "
     "norma internacional incorporada. "
     "[Exercício Q03-III, Rodada 01 Fev/2024]"),

    ("IV – Conforme a concepção dualista, o ato de ratificação de tratado internacional "
     "permite a aplicação das normas convencionais no plano interno, desde que não haja "
     "violação das normas constitucionais vigentes. (C/E?)",
     "<b>ERRADO.</b> Para o dualismo, a ratificação (ato internacional que torna o Estado "
     "parte do tratado) <b>não basta</b> para aplicação interna. "
     "É necessária a <b>transformação</b> em norma interna. No Brasil: decreto presidencial "
     "(4ª etapa do processo de incorporação). Ratificação ≠ promulgação interna. "
     "[Exercício Q03-IV, Rodada 01 Fev/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Direito Internacional :: Fundamentos do DIP",
        "Direito Internacional - Fundamentos DIP.apkg",
        FUNDAMENTOS_DIP,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
