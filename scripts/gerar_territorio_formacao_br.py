#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Território e Formação BR"""

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


TERRITORIO = [
    # ── CONCEITO E CARACTERÍSTICAS DO TERRITÓRIO ──────────────────────────────
    (
        "Quais as 2 características que definem um território 'determinado' no Direito Internacional?",
        "<b>1. Delimitado</b>: espaço jurídico no qual incide a soberania do Estado.<br>"
        "<b>2. Estável</b>: limites fronteiriços não mudam constantemente — assegura segurança "
        "jurídica e evita guerras. Decorre da fixação de limites por princípios jurídicos com "
        "consenso entre os Estados envolvidos.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Quais os 2 critérios adotados pelo Brasil para delimitação de fronteiras em rios contíguos?",
        "<b>Linha mediana</b>: equidistante entre as duas margens — usada em rios de volume "
        "constante (sem secas ou enchentes sazonais).<br>"
        "<b>Talvegue (thalweg)</b>: 'caminho do vale' — linha no meio do canal navegável, "
        "usada em rios com volume variável; garante o mesmo proveito econômico a ambas as "
        "comunidades ribeirinhas.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Quais os 2 critérios adotados pelo Brasil para delimitação de fronteiras em montanhas?",
        "<b>Linha de cumeeiras</b>: une os cumes mais altos das cadeias de montanhas "
        "(ex.: fronteiras com Argentina e Paraguai).<br>"
        "<b>Divisor de águas</b>: local onde se dividem as bacias hidrográficas "
        "(ex.: fronteiras com Guianas, Venezuela e Colômbia).<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Quais critérios de delimitação o Brasil expressamente NÃO adota?",
        "• <b>Condomínio</b> (rios): critério pelo qual o rio pertence em comum a ambos os "
        "Estados, permitindo aplicar indistintamente a lei de cada um em todo o rio.<br>"
        "• <b>Linha do sopé</b> (montanhas): usa as bases das montanhas como fator limitador "
        "das fronteiras.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),

    # ── DISCIPLINA JURÍDICA DA ESTABILIDADE TERRITORIAL ───────────────────────
    (
        "Quais instrumentos jurídicos disciplinam a estabilidade territorial e o que preveem?",
        "<b>Convenção de Montevidéu 1933, art. 11</b>: proíbe expressamente o reconhecimento "
        "de territórios adquiridos por uso da força.<br>"
        "<b>Convenção de Viena sobre Sucessão de Estados em Matéria de Tratados 1978, "
        "arts. 11-12</b>: Estado sucessor deve respeitar tratados que definem fronteiras e "
        "direitos de uso do território celebrados pelo Estado sucedido — a teoria da "
        "<i>tabula rasa</i> (clean slate) não se aplica a fronteiras.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),

    # ── PRINCÍPIO UTI POSSIDETIS ───────────────────────────────────────────────
    (
        "O que é o princípio uti possidetis e qual sua origem?",
        "Princípio do Direito Internacional que busca assegurar a manutenção do "
        "<i>status quo ante</i>, impedindo mudanças em situações já existentes.<br>"
        "Significado: <b>'quem usa de fato, deve possuir o direito'</b>.<br>"
        "Origem: Direito Romano. Primeira aplicação no DI: <b>Tratado de Madrid de 1750</b> "
        "(limites entre América Portuguesa e Espanhola), defendido por <b>Alexandre Gusmão</b>.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Qual a diferença entre uti possidetis de facto e uti possidetis juris?",
        "<b>De facto</b>: território pertence a quem tiver posse efetiva e real no momento "
        "da independência — mantém-se o território como está sendo usado. "
        "Adotado pelo <b>Brasil</b> em sua independência.<br>"
        "<b>Juris</b>: mantêm-se as divisões administrativas feitas pela metrópole "
        "anteriormente à independência. Adotado na <b>América espanhola (séc. XIX)</b> e "
        "países <b>africanos e asiáticos (séc. XX)</b>.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Em quais contextos históricos o uti possidetis foi empregado no Direito Internacional?",
        "1. <b>Descolonização da América</b> — século XIX<br>"
        "2. <b>Descolonização da África e Ásia</b> — século XX<br>"
        "3. <b>Desmembramento da União Soviética e Iugoslávia</b> — 1990<br>"
        "Reconhecido como <b>princípio geral do direito</b> pela CIJ.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Qual o status atual do uti possidetis no Direito Internacional?",
        "Reconhecido como <b>princípio geral do direito pela CIJ</b>.<br>"
        "Aplicação atual <b>residual</b>: a maioria dos limites territoriais já está definida "
        "por tratados celebrados entre os Estados envolvidos.<br>"
        "Continua aplicável na <b>ausência de normas convencionais específicas</b> para "
        "definição de fronteiras.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Quais são os 3 mecanismos alternativos ao uti possidetis para resolver controvérsias "
        "territoriais, segundo a CIJ?",
        "1. <b>Tratados internacionais</b>: solução diplomática com critérios específicos para "
        "delimitação do território.<br>"
        "2. <b>Princípio do controle efetivo</b>: titular é quem exercia atos de soberania "
        "(defesa externa, serviços à população) — aplica-se quando não há uti possidetis "
        "verificável nem tratado.<br>"
        "3. <b>Equidade (ex aequo et bono)</b>: solução justa para todas as partes; só pode "
        "ser empregada pela CIJ com <b>concordância expressa</b> dos Estados (art. 38 Estatuto CIJ).<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),
    (
        "Caso Ilha das Palmas (1928): qual foi a controvérsia, quem julgou e qual o resultado?",
        "<b>Partes</b>: EUA v. Holanda.<br>"
        "<b>Fato</b>: EUA firmaram tratado com a Espanha para assumir controle da ilha; "
        "contudo, a Holanda exercia controle efetivo contínuo e pacífico sobre ela.<br>"
        "<b>Julgamento</b>: <b>Tribunal Permanente de Arbitragem</b> (não a CPJI/CIJ).<br>"
        "<b>Resultado</b>: decisão a favor da <b>Holanda</b>, com base no princípio do "
        "controle efetivo — exercício contínuo e pacífico de autoridade prevaleceu sobre "
        "o título contratual com a Espanha.<br>"
        "<i>Fonte: Anotações – Território e Formação BR</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – O princípio do uti possidetis iuris é uma norma de jus cogens, sendo, "
        "portanto, imperativa e inderrogável no direito internacional.",
        "<b>ERRADO.</b> O uti possidetis é um <b>princípio geral do direito</b> reconhecido "
        "pela CIJ, mas não é norma de <i>jus cogens</i>. Normas de jus cogens são imperativas "
        "e inderrogáveis (ex.: proibição de genocídio, escravidão, uso da força); o uti "
        "possidetis pode ser afastado por acordo entre os Estados.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q01-I</i>",
    ),
    (
        "[Exercício] II – O princípio do uti possidetis surgiu no direito internacional no "
        "contexto da descolonização das Américas no século XIX.",
        "<b>ERRADO.</b> Embora o uti possidetis tenha sido largamente empregado na "
        "descolonização das Américas no século XIX, sua origem no Direito Internacional "
        "remonta ao <b>Tratado de Madrid de 1750</b> (limites entre América Portuguesa e "
        "Espanhola, defendido por Alexandre Gusmão) — anterior à independência das colônias.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q01-II</i>",
    ),
    (
        "[Exercício] III – O uti possidetis iuris determina que as fronteiras sejam delimitadas "
        "com base na posse efetiva dos territórios no momento da independência; ao passo que o "
        "uti possidetis de facto determina que as fronteiras sejam fixadas de acordo com as "
        "divisões administrativas coloniais preexistentes.",
        "<b>ERRADO.</b> As definições estão <b>invertidas</b>:<br>"
        "• <i>Uti possidetis de facto</i>: posse efetiva e real no momento da independência.<br>"
        "• <i>Uti possidetis juris</i>: divisões administrativas coloniais preexistentes.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q01-III</i>",
    ),
    (
        "[Exercício] IV – O princípio do uti possidetis pode ser aplicado quando as fronteiras "
        "são definidas por rios.",
        "<b>CERTO.</b> O uti possidetis é aplicável a qualquer tipo de fronteira na ausência "
        "de norma convencional específica, incluindo fronteiras fluviais. Os critérios para "
        "rios (linha mediana, talvegue) são formas técnicas de delimitar a fronteira, mas "
        "o uti possidetis pode ser o princípio de base que determina a titularidade do "
        "território ribeirinho.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – A Convenção de Montevidéu de 1933 exige que o território do Estado "
        "seja 'determinado', mas não 'definitivamente delimitado'.",
        "<b>CERTO.</b> A Convenção de Montevidéu prevê apenas que o território seja "
        "<b>'determinado'</b> — um conceito jurídico que não exige fronteiras definitiva e "
        "formalmente fixadas por tratado. Basta que o espaço territorial seja identificável "
        "e estável, ainda que haja disputas pontuais sobre determinados limites.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q02-I</i>",
    ),
    (
        "[Exercício] II – A Carta das Nações Unidas de 1945 inovou no direito internacional ao "
        "proibir a aquisição de territórios pelo uso ou ameaça da força.",
        "<b>ERRADO.</b> A proibição não foi inovação da Carta da ONU (1945). A "
        "<b>Convenção de Montevidéu de 1933</b>, em seu art. 11, já proibia expressamente "
        "o reconhecimento de territórios adquiridos por meio do uso da força — doze anos antes.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q02-II</i>",
    ),
    (
        "[Exercício] III – De acordo com a Convenção de Viena sobre Sucessão de Estados em "
        "matéria de Tratados de 1978, a sucessão de Estados não afeta as fronteiras "
        "demarcadas por tratado.",
        "<b>CERTO.</b> A Convenção de Viena 1978, arts. 11-12, estabelece que o Estado "
        "sucessor deve respeitar os tratados que definem fronteiras e direitos de uso do "
        "território celebrados pelo Estado sucedido. A teoria da <i>tabula rasa</i> (clean "
        "slate) <b>não se aplica</b> em matéria de delimitação territorial.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q02-III</i>",
    ),
    (
        "[Exercício] IV – O direito internacional obriga os novos Estados a adotarem o "
        "princípio do uti possidetis como critério para a definição de suas fronteiras.",
        "<b>ERRADO.</b> O uti possidetis é um princípio geral aplicável na <b>ausência</b> "
        "de normas convencionais específicas — não é obrigatório. Os Estados podem fixar "
        "suas fronteiras por outros mecanismos igualmente válidos: tratados, princípio do "
        "controle efetivo ou equidade (<i>ex aequo et bono</i>).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – No Caso do Templo de Preah Vihear (Camboja v. Tailândia, CIJ, 1962), "
        "a CIJ reconheceu a soberania do Camboja sobre o templo com base no princípio do "
        "estoppel, pois a Tailândia havia aceitado, por décadas, um mapa que atribuía o "
        "templo ao Camboja.",
        "<b>CERTO.</b> A CIJ aplicou o <b>estoppel</b>: a Tailândia aceitou durante décadas "
        "um mapa colonial francês que situava Preah Vihear no território cambojano e não "
        "objetou a esse mapeamento. Por isso, não podia posteriormente contestar a soberania "
        "cambojana sem contrariar sua própria conduta anterior.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q03-I</i>",
    ),
    (
        "[Exercício] II – No Caso da Disputa Territorial (Líbia v. Chade, CIJ, 1994), a CIJ "
        "determinou que, uma vez que o tratado que havia demarcado a fronteira entre os dois "
        "países expirou, a delimitação fronteiriça a ele relacionada também deixou de ter "
        "validade.",
        "<b>ERRADO.</b> A CIJ decidiu o oposto: uma vez estabelecida por tratado, a "
        "<b>fronteira é permanente e sobrevive à extinção do tratado</b>. A delimitação "
        "territorial tem natureza diferente de outras obrigações convencionais — não caduca "
        "com o término da vigência do tratado que a criou.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q03-II</i>",
    ),
    (
        "[Exercício] III – No Caso da Ilha das Palmas (EUA v. Holanda, 1928), a Corte "
        "Permanente de Justiça Internacional decidiu que a Holanda tinha soberania sobre a "
        "ilha em razão do exercício contínuo e pacífico de autoridade.",
        "<b>ERRADO.</b> O caso foi julgado pelo <b>Tribunal Permanente de Arbitragem</b> "
        "(árbitro: Max Huber), <b>não pela CPJI</b>. O mérito está correto: a Holanda venceu "
        "com base no controle efetivo — exercício contínuo e pacífico de autoridade "
        "prevaleceu sobre o título contratual EUA-Espanha.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q03-III</i>",
    ),
    (
        "[Exercício] IV – O princípio do uti possidetis foi rejeitado no processo de "
        "desmembramento da União Soviética e da Iugoslávia, por não ser aplicável em "
        "contextos de secessão.",
        "<b>ERRADO.</b> O uti possidetis foi <b>aplicado</b> (não rejeitado) no "
        "desmembramento da URSS e da Iugoslávia (1990), para manter as divisões "
        "administrativas internas como fronteiras dos novos Estados independentes — "
        "evitando assim conflitos gerados por reivindicações territoriais sobrepostas.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Out/2023, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Internacional::Território e Formação BR",
        "Direito Internacional - Território e Formação BR.apkg",
        TERRITORIO,
    )
