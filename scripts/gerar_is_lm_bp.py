#!/usr/bin/env python3
"""Gera deck Anki — Economia: Modelo IS-LM-BP.

Item do edital: 2.4 O modelo IS-LM-BP.

Fontes:
  - Anotações: Modelo IS-LM-BP.md
  - Sem material do professor em PDF para esta submatéria (só anotação própria,
    incluindo exercícios de revisão ditados em aula)
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelreichelt/Desktop/cacd-learning/anki/decks/economia"
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


IS_LM_BP = [

    # ── CONTEÚDO ──────────────────────────────────────────────────────────

    ("Na versão de economia aberta do modelo IS-LM (modelo Mundell-Fleming), "
     "a curva IS passa a incorporar as exportações líquidas como componente "
     "da demanda agregada, de modo que um aumento da renda externa ou uma "
     "desvalorização da taxa de câmbio nominal deslocam essa curva para a "
     "esquerda, reduzindo o produto de equilíbrio.",
     "<b>ERRADO.</b> O deslocamento é para a <b>direita</b>, não para a "
     "esquerda. Com Y=C+I+G+EL e EL=X-M, um aumento de Y* ou de E "
     "(desvalorização) eleva as exportações líquidas, deslocando a IS para "
     "a direita e aumentando o produto de equilíbrio. [Anotações da aula]"),

    ("No modelo IS-LM-BP, a curva LM passa a se deslocar não apenas em "
     "função de operações de mercado aberto com títulos públicos, mas "
     "também em razão da atuação do Banco Central no mercado de câmbio, de "
     "modo que a compra de dólares pelo Banco Central contrai a oferta de "
     "moeda doméstica e desloca a curva LM para a esquerda.",
     "<b>ERRADO.</b> A compra de dólares pelo BC <b>eleva</b> a oferta de "
     "moeda doméstica — ao comprar dólares, o BC injeta moeda local na "
     "economia — deslocando a LM para a <b>direita</b>. É a <b>venda</b> de "
     "dólares que contrai a LM. [Anotações da aula]"),

    ("A curva BP, que representa os pares de taxa de juros e renda que "
     "equilibram o balanço de pagamentos, apresenta inclinação positiva sob "
     "mobilidade imperfeita de capitais, pois um aumento da renda eleva as "
     "importações e gera déficit comercial, exigindo uma elevação da taxa "
     "de juros doméstica para atrair capital e restaurar o equilíbrio do "
     "BP.",
     "<b>CERTO.</b> Renda ↑ → importações ↑ → déficit comercial → é "
     "necessária entrada de capital para reequilibrar o BP → entrada de "
     "capital exige juros ↑ (paridade de juros) — daí a inclinação "
     "positiva. [Anotações da aula]"),

    ("Sob perfeita mobilidade de capitais, a curva BP é totalmente "
     "vertical, pois a taxa de juros doméstica torna-se completamente "
     "independente da taxa de juros internacional; já na ausência de "
     "mobilidade de capitais, a curva BP é horizontal na taxa de juros "
     "internacional, dado que qualquer diferencial de juros provoca fluxos "
     "infinitos de capital.",
     "<b>ERRADO.</b> É o oposto: com <b>perfeita mobilidade</b> de "
     "capitais, a BP é <b>horizontal</b> na paridade de juros (i=i*); "
     "<b>sem mobilidade</b> de capitais, a BP é <b>vertical</b> na renda de "
     "equilíbrio comercial, com o juro doméstico independente do "
     "internacional. [Anotações da aula]"),

    ("A trindade impossível estabelece que um país não pode manter "
     "simultaneamente câmbio fixo, livre mobilidade de capitais e "
     "autonomia da política monetária; o padrão-ouro exemplifica a "
     "combinação de câmbio fixo com autonomia da política monetária, "
     "abrindo mão da livre mobilidade de capitais.",
     "<b>ERRADO.</b> O padrão-ouro combinava <b>câmbio fixo + livre "
     "mobilidade de capitais</b>, abrindo mão da autonomia monetária. Foi o "
     "sistema de <b>Bretton Woods</b> que combinou câmbio fixo + autonomia "
     "monetária, abrindo mão da livre mobilidade de capitais (necessária à "
     "reconstrução pós-Segunda Guerra). [Anotações da aula]"),

    ("Em um regime de câmbio fixo com perfeita mobilidade de capitais, uma "
     "política fiscal expansionista é maximamente eficaz sobre o produto, "
     "pois a necessidade de o Banco Central comprar reservas internacionais "
     "para manter o câmbio fixo, diante da entrada de capitais provocada "
     "pela alta da taxa de juros, expande endogenamente a oferta monetária "
     "e evita o efeito crowding-out.",
     "<b>CERTO.</b> A expansão fiscal eleva os juros acima do equilíbrio da "
     "BP, atraindo capital; para manter o câmbio, o BC compra dólares, "
     "expandindo a LM endogenamente até os juros retornarem ao patamar "
     "internacional — sem crowding out, a política fiscal atinge máxima "
     "eficácia. [Anotações da aula]"),

    ("Em um regime de câmbio fixo com perfeita mobilidade de capitais, uma "
     "política monetária expansionista é eficaz para elevar permanentemente "
     "o produto, uma vez que a queda da taxa de juros doméstica abaixo do "
     "patamar internacional provoca fuga de capitais que obriga o Banco "
     "Central a vender reservas, elevando ainda mais a renda de equilíbrio.",
     "<b>ERRADO.</b> A venda de reservas pelo BC <b>contrai</b> a oferta "
     "monetária, revertendo a LM ao ponto original — a política monetária é "
     "<b>totalmente ineficaz</b> nesse regime, e o país ainda perde "
     "reservas internacionais no processo. [Anotações da aula]"),

    ("Em regime de câmbio flutuante com perfeita mobilidade de capitais, a "
     "política monetária expansionista é a mais eficaz para elevar o "
     "produto, enquanto a política fiscal expansionista tende a ser "
     "ineficaz, pois a apreciação cambial provocada pela entrada de "
     "capitais reduz as exportações líquidas e neutraliza o estímulo fiscal "
     "inicial.",
     "<b>CERTO.</b> No câmbio flutuante, a expansão fiscal aprecia o câmbio "
     "e reduz EL, anulando o efeito sobre a IS; já a expansão monetária "
     "deprecia o câmbio, eleva EL e desloca a IS na mesma direção — "
     "potencializando o efeito sobre o produto. [Anotações da aula]"),

    ("Um choque de alta na taxa de juros internacional provoca, tanto em "
     "regime de câmbio fixo quanto em regime de câmbio flutuante, uma "
     "contração do produto doméstico, já que em ambos os casos a taxa de "
     "juros interna deve subir para restabelecer o equilíbrio do balanço de "
     "pagamentos.",
     "<b>ERRADO.</b> Os efeitos sobre o <b>produto</b> são opostos: em "
     "câmbio <b>fixo</b>, o BC vende reservas para segurar o câmbio, "
     "contraindo a LM e reduzindo o produto; em câmbio <b>flutuante</b>, a "
     "fuga de capital deprecia a moeda automaticamente, elevando as "
     "exportações líquidas e <b>expandindo</b> o produto. [Anotações da "
     "aula]"),

    ("A paridade de juros descoberta, adotada como simplificação no modelo "
     "IS-LM-BP de curto prazo, estabelece que a taxa de juros doméstica "
     "deve igualar a taxa de juros internacional (i=i*), ao passo que a "
     "paridade de juros coberta, mais realista, acrescenta a essa igualdade "
     "a expectativa de desvalorização cambial e o prêmio de risco do país "
     "(i=i*+Ê+PR).",
     "<b>CERTO.</b> A versão coberta é mais completa: soma à paridade "
     "simples (i=i*) a expectativa de depreciação cambial (Ê) e o prêmio de "
     "risco de default do país (PR). [Anotações da aula]"),

    # ── EXERCÍCIOS (revisão ditada em aula) ─────────────────────────────────

    ("Em uma economia de câmbio fixo e perfeita mobilidade de capitais, uma "
     "política monetária contracionista provoca uma redução no estoque de "
     "reservas internacionais em poder do Banco Central. (C/E?)",
     "<b>ERRADO.</b> O efeito é o oposto: o aperto monetário eleva os juros "
     "domésticos acima do equilíbrio da BP, atraindo capital estrangeiro; "
     "para não deixar o câmbio apreciar, o BC precisa <b>comprar</b> "
     "reservas (aumentando o estoque), o que expande a LM de volta à "
     "posição original — a política monetária acaba neutralizada. "
     "[Anotações da aula, exercício de revisão]"),

    ("Se não há mobilidade de capitais, a função BP é representada por uma "
     "linha vertical no plano (Y, i), sendo Y a renda e i a taxa de juros. "
     "(C/E?)",
     "<b>CERTO.</b> Sem mobilidade de capitais, o equilíbrio do BP depende "
     "apenas do saldo comercial — fixado em uma dada renda Y — e não "
     "responde a variações da taxa de juros. [Anotações da aula, exercício "
     "de revisão]"),

    ("Em uma economia sem mobilidade de capitais, quanto maior o grau de "
     "abertura comercial, menor será o impacto de políticas fiscais sobre o "
     "produto. (C/E?)",
     "<b>CERTO.</b> Maior abertura comercial implica maior propensão "
     "marginal a importar, o que reduz o multiplicador keynesiano (mais "
     "vazamento da demanda para o exterior) — efeito válido "
     "independentemente do regime de mobilidade de capitais. [Anotações da "
     "aula, exercício de revisão]"),

    ("Em um regime de câmbio fixo com perfeita mobilidade de capitais, a "
     "oferta de moeda é uma variável endógena. (C/E?)",
     "<b>CERTO.</b> O compromisso de manter o câmbio fixo obriga o BC a "
     "ajustar reservas — e, portanto, a base monetária — para acomodar os "
     "fluxos de capital, de modo que o BC perde o controle autônomo sobre a "
     "oferta de moeda. [Anotações da aula, exercício de revisão]"),

    ("Em uma economia com taxa de câmbio fixa, quanto maior for a "
     "mobilidade de capitais, maior será o efeito de uma expansão fiscal "
     "sobre o produto. (C/E?)",
     "<b>CERTO.</b> Mais mobilidade de capitais amplia a resposta da "
     "entrada de capital à alta dos juros provocada pela expansão fiscal, "
     "ampliando a expansão endógena da LM e reduzindo o crowding out. "
     "[Anotações da aula, exercício de revisão]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Modelo IS-LM-BP",
        "Economia - Modelo IS-LM-BP.apkg",
        IS_LM_BP,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
