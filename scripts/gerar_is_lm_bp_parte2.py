#!/usr/bin/env python3
"""Gera deck Anki — Economia: Modelo IS-LM-BP - Parte 2.

Item do edital: 2.4 O modelo IS-LM-BP (continuação — mobilidade imperfeita
e ausência de mobilidade de capitais; complementa a Parte 1, que tratou só
o caso de perfeita mobilidade).

Fontes:
  - Anotações: Modelo IS-LM-BP - Parte 2.md
  - Exercícios: 2 questões oficiais de TP CACD 2016, incluídas literalmente
    nas anotações da aula
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


IS_LM_BP_PARTE2 = [

    # ── CONTEÚDO ──────────────────────────────────────────────────────────

    ("Em um regime de câmbio fixo, a política monetária é ineficaz para "
     "expandir o produto apenas nos casos de perfeita mobilidade de "
     "capitais, uma vez que, sob mobilidade nula ou imperfeita de "
     "capitais, o Banco Central não é obrigado a intervir no mercado de "
     "câmbio para neutralizar o efeito da expansão monetária.",
     "<b>ERRADO.</b> A regra é mais ampla: <b>sempre que o câmbio é fixo</b>, "
     "a política monetária é ineficaz, <b>qualquer que seja o grau de "
     "mobilidade de capitais</b> — o BC sempre precisa ajustar reservas "
     "(vender/comprar) para defender a paridade, tornando a oferta de "
     "moeda endógena em todos os regimes de mobilidade. [Anotações da "
     "aula]"),

    ("Em uma economia sem qualquer mobilidade de capitais, tanto a política "
     "monetária quanto a política fiscal são totalmente ineficazes para "
     "expandir o produto sob regime de câmbio fixo, ao passo que ambas se "
     "tornam eficazes sob regime de câmbio flexível.",
     "<b>CERTO.</b> Sem mobilidade de capitais e câmbio fixo, qualquer "
     "expansão de demanda gera déficit comercial que obriga o BC a vender "
     "reservas, neutralizando ambas as políticas; sob câmbio flexível, a "
     "depreciação cambial resultante amplia as exportações líquidas e "
     "torna ambas eficazes. [Anotações da aula]"),

    ("A política fiscal expansionista sob regime de câmbio flexível é "
     "ineficaz sempre que houver algum grau de mobilidade de capitais no "
     "país, independentemente de essa mobilidade ser perfeita, forte ou "
     "fraca, pois a entrada de capital estrangeiro provocada pela alta dos "
     "juros sempre aprecia a moeda o suficiente para neutralizar o "
     "estímulo fiscal inicial.",
     "<b>ERRADO.</b> A ineficácia da política fiscal sob câmbio flexível "
     "ocorre <b>apenas no caso de mobilidade PERFEITA</b> de capitais — sob "
     "mobilidade forte, fraca ou mesmo nula, a política fiscal permanece "
     "<b>eficaz</b> sob câmbio flexível (em alguns casos até potencializada "
     "pela depreciação cambial). [Anotações da aula]"),

    ("Em uma economia com forte (porém imperfeita) mobilidade de capitais e "
     "câmbio fixo, uma política fiscal expansionista é eficaz e "
     "potencializada pela compra de reservas internacionais realizada pelo "
     "Banco Central diante da entrada de capitais, ainda que com eficácia "
     "inferior à observada sob perfeita mobilidade de capitais.",
     "<b>CERTO.</b> A alta dos juros provocada pela expansão fiscal atrai "
     "capital sob forte mobilidade, levando o BC a comprar reservas para "
     "manter o câmbio, o que expande a LM endogenamente — mas como a "
     "mobilidade não é perfeita, a expansão da LM é parcial, resultando em "
     "juros finais mais altos do que sob mobilidade perfeita. [Anotações "
     "da aula]"),

    ("Em uma economia com fraca mobilidade de capitais e câmbio fixo, uma "
     "política fiscal expansionista tem sua eficácia reduzida em "
     "comparação a uma economia fechada, pois o déficit comercial gerado "
     "pelo aumento da renda obriga o Banco Central a vender reservas "
     "internacionais, contraindo parcialmente a oferta de moeda.",
     "<b>CERTO.</b> Com mobilidade fraca, prevalece o efeito do saldo "
     "comercial (regra de leitura da BP quase vertical): o aumento da "
     "renda gera déficit comercial, levando o BC a vender reservas para "
     "manter o câmbio fixo — isso contrai parcialmente a LM, reduzindo "
     "(mas não anulando) a eficácia fiscal. [Anotações da aula]"),

    ("Em uma economia com forte mobilidade de capitais e câmbio flexível, "
     "uma política monetária expansionista é ampliada pelo canal cambial, "
     "já que a queda da taxa de juros doméstica, além de estimular a "
     "demanda interna, deprecia a moeda e eleva as exportações líquidas, "
     "resultando em um produto de equilíbrio maior do que se obteria em "
     "uma economia fechada.",
     "<b>CERTO.</b> A dupla via de estímulo (juros mais baixos elevam "
     "investimento doméstico E depreciam o câmbio, elevando exportações) "
     "amplia o efeito da política monetária além do que ocorreria numa "
     "economia fechada, sem esse canal cambial adicional. [Anotações da "
     "aula]"),

    # ── EXERCÍCIOS OFICIAIS (TP CACD 2016 — reprodução literal) ─────────────

    ("Considere que o referido país esteja em recessão e seja uma economia "
     "aberta, com câmbio flutuante e mobilidade de capitais forte, porém "
     "não perfeita. Nesse caso, de acordo com o modelo IS-LM-BP, a "
     "implementação de uma política fiscal expansionista, para tentar "
     "impulsionar a atividade econômica, seria ineficaz. (C/E?)",
     "<b>ERRADO.</b> Câmbio flutuante + mobilidade forte (mas não "
     "perfeita) → política fiscal expansionista é <b>eficaz</b>. Só sob "
     "mobilidade <b>perfeita</b> de capitais a política fiscal seria "
     "ineficaz em câmbio flutuante. [TP CACD 2016]"),

    ("Considere que o referido país esteja em recessão e seja uma economia "
     "aberta, com câmbio fixo e fraca mobilidade de capitais. Nesse caso, "
     "de acordo com o modelo IS-LM-BP, a implementação de uma política "
     "fiscal expansionista, para tentar impulsionar a atividade econômica, "
     "seria ineficaz. (C/E?)",
     "<b>ERRADO.</b> Câmbio fixo + fraca mobilidade de capitais → política "
     "fiscal expansionista é <b>eficaz</b>, ainda que com eficácia "
     "reduzida em relação à economia fechada. Só a <b>ausência total</b> "
     "de mobilidade de capitais tornaria a fiscal ineficaz sob câmbio "
     "fixo. [TP CACD 2016]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Economia::Modelo IS-LM-BP - Parte 2",
        "Economia - Modelo IS-LM-BP - Parte 2.apkg",
        IS_LM_BP_PARTE2,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
