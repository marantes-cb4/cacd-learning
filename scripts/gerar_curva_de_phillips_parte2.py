#!/usr/bin/env python3
"""Gera deck Anki — Economia: Curva de Phillips - Parte 2.

Itens do edital: 2.8 Emprego e renda; 2.6 Política Monetária; 2.3 Economia do Setor Público e Política Fiscal.

Fontes:
  - Anotações: Macro - Curva de Phillips - Parte 2.md
  - Sem material do professor em PDF/PPT para esta submatéria (só anotação
    própria)
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/economia"
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


CURVA_DE_PHILLIPS_P2 = [

    ("Um governo anuncia hoje um forte corte de gastos que só entrará em "
     "vigor daqui a seis meses. Agentes com expectativas adaptativas só "
     "revisarão a inflação esperada depois de observarem o efeito do corte "
     "sobre os preços, ao passo que agentes com expectativas racionais já "
     "incorporam o anúncio às suas previsões hoje.",
     "<b>CERTO.</b> Expectativas adaptativas são <i>backward-looking</i> "
     "(dependem da inflação e dos erros passados). As racionais são "
     "<i>forward-looking</i>: usam de forma eficiente toda a informação "
     "disponível, inclusive políticas atuais e anunciadas. [Anotações da "
     "aula]"),

    ("Uma autoridade que estima, com dados históricos, a relação entre "
     "inflação e desemprego e passa a explorá-la por meio de política "
     "expansionista tende a ver essa relação permanecer estável, pois os "
     "agentes não alteram seu comportamento em resposta à política.",
     "<b>ERRADO.</b> Essa é justamente a crítica de Lucas (1972): com "
     "expectativas racionais, relações supostas estáveis <b>deixam de ser "
     "estáveis</b>, porque os agentes mudam ações e previsões conforme a "
     "atuação do governo. [Anotações da aula]"),

    ("Se um banco central produz repetidamente inflação superior à "
     "anunciada, os agentes com expectativas racionais acabarão "
     "antecipando o viés, de modo que o desemprego não se mantém "
     "sistematicamente abaixo da taxa natural; sob expectativas "
     "adaptativas, ao contrário, a surpresa funcionaria ao menos no "
     "curto prazo.",
     "<b>CERTO.</b> Sob expectativas racionais os agentes não cometem "
     "erros <b>sistemáticos</b>, e o governo não consegue enganá-los "
     "(reduzir o salário real por inflação surpresa). Nas adaptativas "
     "há erros de previsão no curto prazo, o que permite o efeito "
     "temporário. [Anotações da aula]"),

    ("Friedman e Phelps, de um lado, e Lucas, de outro, concordam que "
     "existe trade-off entre inflação e desemprego no curto prazo, "
     "divergindo apenas quanto à sua inexistência no longo prazo.",
     "<b>ERRADO.</b> Para Friedman e Phelps (adaptativas) o trade-off "
     "existe no curto prazo e some no longo. Para Lucas e os novos "
     "clássicos, com expectativas racionais, a curva de Phillips é "
     "<b>vertical mesmo no curto prazo</b>: o trade-off não existe em "
     "prazo algum. [Anotações da aula]"),

    ("Dois países decidem reduzir a inflação na mesma magnitude: aquele "
     "cujo banco central goza de maior credibilidade tende a enfrentar "
     "menor aumento temporário do desemprego, porque as expectativas de "
     "inflação caem mais rápido e a curva de curto prazo se desloca para "
     "baixo.",
     "<b>CERTO.</b> A credibilidade se constrói pela coerência entre o que "
     "o governo anuncia e o que faz. Quanto maior, <b>menor a taxa de "
     "sacrifício</b>, pois os agentes reduzem suas expectativas de imediato "
     "e a desinflação ocorre sem o custo temporário de desemprego alto. "
     "[Anotações da aula]"),

    ("A desinflação conduzida por Volcker no início dos anos 1980 mostrou "
     "que o anúncio de uma política de combate à inflação é imediatamente "
     "acreditado pelos agentes; a queda da inflação de cerca de 10% para "
     "4% ocorreu sem aumento relevante do desemprego, e a política fiscal "
     "contracionista da época facilitou o ajuste.",
     "<b>ERRADO.</b> A inflação caiu (de ~10% para ~4%), mas com "
     "<b>desemprego alto</b>: os formuladores não podem contar com "
     "crença imediata nos anúncios. A política fiscal era "
     "<b>expansionista</b> (1981–84), exigindo política monetária muito "
     "restritiva. Os juros elevados geraram crise da dívida em países, como "
     "o Brasil, endividados a taxas flutuantes. [Anotações da aula]"),

    ("A chamada grande moderação, de 1984 a 2004, caracterizou-se pela "
     "menor volatilidade da inflação e do produto e, segundo a leitura "
     "apresentada na aula, decorreu principalmente de choques externos "
     "favoráveis, e não de uma melhor condução da política econômica.",
     "<b>ERRADO.</b> A redução da volatilidade (definição de Bernanke) é "
     "atribuída à <b>melhoria da política econômica</b>, em reação ao "
     "aprendizado dos anos 70 (expansão mais choques do petróleo, "
     "inflação alta) e dos 80 (desinflação de Volcker a qualquer custo, "
     "com juros enormes e desemprego alto). [Anotações da aula]"),

    ("No novo consenso macroeconômico, o banco central persegue uma meta "
     "de inflação por considerar que o trade-off com o desemprego é "
     "temporário e depende da credibilidade, e a política fiscal é "
     "preferencialmente usada para estimular a atividade de curto prazo, "
     "dado o elevado multiplicador do gasto.",
     "<b>ERRADO</b> na segunda parte. No novo consenso, a política fiscal "
     "<b>não</b> deve estimular a atividade: o multiplicador de curto prazo "
     "é pequeno (<i>crowding out</i> e maior risco soberano pressionam os "
     "juros) e, no longo prazo, ela não afeta o produto. Seu papel é "
     "reduzir a dívida, o risco-país e os juros. A primeira parte está "
     "correta. [Anotações da aula]"),

    ("Numa economia em que a inflação está acima da meta e, ao mesmo "
     "tempo, o produto está abaixo do nível de pleno emprego, a regra de "
     "Taylor envia sinais opostos para os juros: o hiato da inflação "
     "pede aperto, e o hiato do produto, afrouxamento. A decisão final "
     "depende do peso que o banco central atribui a cada hiato.",
     "<b>CERTO.</b> A regra de Taylor fecha <b>dois hiatos</b>: inflação "
     "acima da meta → elevar juros; PIB abaixo do pleno emprego → reduzir "
     "juros. Quando os hiatos apontam em direções contrárias, as "
     "sensibilidades a cada um determinam o resultado. O BC deve ter "
     "autonomia para segui-la. [Anotações da aula]"),

    ("A crise de 2008, originada na queda dos preços dos imóveis e nas "
     "perdas do setor financeiro, produziu um choque negativo de demanda "
     "agregada e levou à combinação de desemprego mais alto com inflação "
     "mais baixa, semelhante à estagflação dos anos 1970.",
     "<b>ERRADO.</b> Choque de <b>demanda</b> negativo move a economia "
     "ao longo da curva de Phillips: mais desemprego e <b>menos</b> "
     "inflação. A estagflação dos anos 70 (inflação e desemprego juntos) "
     "decorreu de choques de oferta e de expectativas. [Anotações da "
     "aula]"),

    ("Para Blanchard, um dos limites do consenso anterior à crise de 2008 "
     "foi concentrar a política monetária nos preços de bens e serviços, "
     "sem considerar os preços dos ativos financeiros nem a regulação "
     "macroprudencial, apoiando-se na ideia de que mercados financeiros "
     "são sempre eficientes.",
     "<b>CERTO.</b> A grande moderação aceitava a hipótese dos mercados "
     "eficientes, dispensando regulação. Daí a atenção posterior à "
     "regulação macroprudencial (Basileia 3, 2010), às políticas "
     "monetárias não convencionais e à volta da política fiscal. "
     "[Anotações da aula]"),

    ("Numa armadilha de liquidez, em que a taxa de juros já está muito "
     "baixa, a política monetária convencional perde eficácia, razão pela "
     "qual, após 2008, se recorreu a instrumentos não convencionais e "
     "se restabeleceu o papel da política fiscal no combate à recessão.",
     "<b>CERTO.</b> Reduzir ainda mais uma taxa já baixa não tem efeito "
     "sobre a demanda. Por isso Blanchard destaca as medidas monetárias "
     "não convencionais e a volta da política fiscal como ferramenta "
     "anticíclica. [Anotações da aula]"),

    ("Regras fiscais de primeira geração, que impõem limites rígidos de "
     "gasto para reduzir a dívida, ampliam o espaço do governo para "
     "elevar despesas em recessões; as de segunda geração, por sua vez, "
     "restringem esse espaço em nome da estabilidade da dívida.",
     "<b>ERRADO.</b> Está invertido. Na <b>1ª geração</b> os limites "
     "rígidos <b>reduzem</b> a capacidade de gastar em recessão. A "
     "<b>2ª geração</b> dá flexibilidade à política fiscal no curto prazo "
     "e prevê mecanismos de correção para manter a dívida estável no "
     "longo prazo. [Anotações da aula]"),

    ("Uma inflação elevada, mas plenamente antecipada por todos os "
     "agentes, tende a reduzir o desemprego abaixo da taxa natural no "
     "curto prazo, pois o trade-off decorre do nível da inflação.",
     "<b>ERRADO.</b> O trade-off não vem da inflação em si, mas da "
     "<b>inflação não esperada</b>: é o erro de previsão (em geral, "
     "inflação maior que a esperada) que reduz o salário real e o "
     "desemprego no curto prazo. Inflação totalmente antecipada não "
     "produz esse efeito. [Anotações da aula]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Macro - Curva de Phillips - Parte 2",
        "Economia - Macro - Curva de Phillips - Parte 2.apkg",
        CURVA_DE_PHILLIPS_P2,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
