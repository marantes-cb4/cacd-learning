#!/usr/bin/env python3
"""Gera deck Anki: Economia - Micro Elasticidade"""

import genanki
import os
import random

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "anki", "decks", "economia")

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


ELASTICIDADE = [
    # ── CONCEITOS ──────────────────────────────────────────────────────────────
    (
        "O que é elasticidade em economia?",
        "Medida da <b>resposta da quantidade demandada ou ofertada</b> a variações em seus "
        "determinantes (preço, renda, preço de bens relacionados etc.). Indica o grau de "
        "reatividade do mercado a mudanças.<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade</i>",
    ),
    (
        "O que é elasticidade-preço da demanda? Como é calculada e interpretada?",
        "<b>Fórmula</b>: |Var. % na Qt. demandada / Var. % no preço|<br>"
        "• |e| &gt; 1 → demanda <b>elástica</b> (↑P → ↓RT)<br>"
        "• |e| = 1 → elasticidade <b>unitária</b> (↑P → RT constante)<br>"
        "• |e| &lt; 1 → demanda <b>inelástica</b> (↑P → ↑RT)<br>"
        "Usa-se módulo pois a relação preço-quantidade é inversa.<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Quais são os 5 fatores que afetam a elasticidade-preço da demanda?",
        "1. <b>Necessidade vs. supérfluos</b>: necessidades → inelástica; supérfluos → elástica<br>"
        "2. <b>Substitutos próximos</b>: mais substitutos → mais elástica<br>"
        "3. <b>Peso no orçamento</b>: maior peso → mais elástica<br>"
        "4. <b>Definição do mercado</b>: mais restrita → mais elástica (ex.: sorvete vs. comida)<br>"
        "5. <b>Horizonte temporal</b>: longo prazo → mais elástica<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Qual a relação entre elasticidade-preço da demanda e receita total (RT)?",
        "RT = P × Qd<br>"
        "• Demanda <b>elástica</b> (|e|&gt;1): ↑P → ↓RT; ↓P → ↑RT<br>"
        "• Elasticidade <b>unitária</b> (|e|=1): variação no preço não altera RT<br>"
        "• Demanda <b>inelástica</b> (|e|&lt;1): ↑P → ↑RT; ↓P → ↓RT<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Quais são os casos extremos de elasticidade-preço da demanda?",
        "• <b>Perfeitamente inelástica</b> (e = 0): quantidade não muda com o preço — curva "
        "vertical. Ex.: insulina.<br>"
        "• <b>Perfeitamente elástica</b> (e = ∞): consumidores aceitam apenas um preço único — "
        "curva horizontal. Qualquer preço diferente → demanda vai a zero.<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Por que se usa o método do ponto médio no cálculo da elasticidade?",
        "Porque a elasticidade calculada entre dois pontos varia conforme a <b>direção</b> da mudança "
        "(A→B dá resultado diferente de B→A). O método do ponto médio usa as <b>médias</b> de preço "
        "e quantidade como base, obtendo um valor único e simétrico.<br>"
        "Fórmula: e = (ΔQd/ΔP) × (P̄/Q̄d), onde P̄ e Q̄d são as médias dos dois pontos.<br>"
        "<i>Fonte: Slides Aula 02 – Elasticidade</i>",
    ),
    (
        "O que é elasticidade-renda da demanda? Como o resultado classifica o bem?",
        "<b>Fórmula</b>: Var. % na Qt. demandada / Var. % na renda<br>"
        "• εR &gt; 0 → bem <b>normal</b><br>"
        "• εR &lt; 0 → bem <b>inferior</b><br>"
        "• εR &gt; 1 → bem de <b>luxo</b> (participação no orçamento cresce com a renda)<br>"
        "• 0 &lt; εR &lt; 1 → bem <b>essencial</b> (participação no orçamento cai com a renda)<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "O que é um bem de Giffen? Por que sua curva de demanda é invertida?",
        "Bem <b>inferior e essencial</b> com grande participação no orçamento. "
        "Quando o preço sobe, o consumidor interpreta como aumento geral de preços e concentra "
        "consumo nesse bem básico, reduzindo outros — logo ↑P → ↑Qd (curva de demanda positiva).<br>"
        "Ex.: arroz — se o preço sobe, compra-se mais arroz e menos outros alimentos.<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "O que é elasticidade-preço cruzada da demanda? Como interpreta-se o resultado?",
        "<b>Fórmula</b>: Var. % na Qt. do bem 1 / Var. % no preço do bem 2<br>"
        "• ε &lt; 0 → bens <b>complementares</b> (↑preço do bem 2 → ↓demanda do bem 1)<br>"
        "• ε &gt; 0 → bens <b>substitutos</b> (↑preço do bem 2 → ↑demanda do bem 1)<br>"
        "• ε = 0 → bens <b>independentes</b><br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "O que é elasticidade-preço da oferta e quais fatores a determinam?",
        "Sensibilidade da <b>quantidade ofertada</b> a variações no preço.<br>"
        "Fatores que aumentam a elasticidade da oferta:<br>"
        "• <b>Horizonte temporal</b> maior (longo prazo = mais elástica)<br>"
        "• Fatores de produção <b>menos específicos</b> (mais fáceis de obter/substituir)<br>"
        "• Definição de produto <b>mais específica</b><br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Como a incidência de impostos se relaciona com a elasticidade de oferta e demanda?",
        "O imposto é arcado <b>proporcionalmente pela curva mais inelástica</b>:<br>"
        "• Demanda inelástica + oferta elástica → consumidor arca mais<br>"
        "• Oferta inelástica + demanda elástica → produtor arca mais<br>"
        "• Demanda perfeitamente elástica → produtor arca com todo o imposto<br>"
        "• Oferta perfeitamente inelástica → produtor arca com todo o imposto<br>"
        "<i>Fonte: Anotações – Micro: Elasticidade / Slides Aula 02</i>",
    ),
    (
        "Por que uma safra excepcional pode ser ruim para os agricultores?",
        "Se a demanda por alimentos é <b>inelástica</b>, uma safra excepcional (↑oferta) reduz "
        "o preço mais do que aumenta a quantidade vendida → <b>RT total cai</b>. "
        "A queda no preço supera o ganho em volume.<br>"
        "<i>Fonte: Slides Aula 02 – Elasticidade</i>",
    ),

    # ── TPS 2023 — QUESTÃO 72 ──────────────────────────────────────────────────
    (
        "[TPS 2023 Q72] 1 – Um aumento no imposto sobre o consumo de um bem com demanda "
        "perfeitamente preço-elástica e oferta preço-inelástica terá incidência apenas sobre o "
        "bem-estar dos produtores, pois os consumidores somente adquirem o bem a um preço único "
        "de equilíbrio.",
        "<b>CERTO.</b> Com demanda perfeitamente elástica (horizontal), qualquer elevação de preço "
        "elimina a demanda — os consumidores pagam o mesmo preço. Com oferta inelástica, são os "
        "produtores que absorvem integralmente o imposto.<br>"
        "<i>Fonte: TPS 2023 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2023 Q72] 2 – Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta "
        "tenham elasticidades unitárias incidirá apenas sobre o bem-estar do consumidor, pois as "
        "firmas conseguem repassar o tributo totalmente no novo preço de equilíbrio.",
        "<b>ERRADO.</b> Com elasticidades unitárias e simétricas, o imposto é dividido entre "
        "consumidores e produtores. As firmas não conseguem repassar o tributo integralmente.<br>"
        "<i>Fonte: TPS 2023 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2023 Q72] 3 – Um imposto sobre o consumo de produtos viciantes tem redução pequena "
        "no bem-estar dos consumidores, uma vez que a demanda desses produtos é altamente elástica.",
        "<b>ERRADO.</b> Dois erros: a demanda de produtos viciantes é altamente <b>inelástica</b> "
        "(não elástica); e com demanda inelástica, o imposto recai principalmente sobre os "
        "consumidores, reduzindo significativamente seu bem-estar.<br>"
        "<i>Fonte: TPS 2023 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2023 Q72] 4 – Uma redução no imposto sobre o consumo de um bem com demanda "
        "preço-inelástica e oferta preço-elástica terá incidência maior sobre o bem-estar dos "
        "consumidores do que sobre o bem-estar das firmas.",
        "<b>CERTO.</b> A curva mais inelástica (demanda) arca mais com o imposto. Logo, a "
        "redução do imposto beneficia proporcionalmente mais quem antes arcava mais — os "
        "consumidores.<br>"
        "<i>Fonte: TPS 2023 Q72 – Slides Aula 02 Economia</i>",
    ),

    # ── TPS 2022 — QUESTÃO 69 ──────────────────────────────────────────────────
    (
        "[TPS 2022 Q69] 1 – Bens de consumo essencial tendem a ter elasticidade-preço da demanda "
        "menor do que bens de consumo supérfluo.",
        "<b>CERTO.</b> Bens essenciais têm demanda inelástica (menor elasticidade em módulo), pois "
        "os consumidores os adquirem independentemente do preço. Supérfluos têm demanda elástica "
        "(maior elasticidade).<br>"
        "<i>Fonte: TPS 2022 Q69 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2022 Q69] 2 – Por ser um serviço vital aos seus usuários, a hemodiálise pode ser "
        "considerada um serviço de oferta preço-inelástica.",
        "<b>ERRADO.</b> O caráter vital de um serviço implica demanda inelástica, não oferta "
        "inelástica. A elasticidade da oferta depende de fatores como horizonte temporal e "
        "especificidade dos insumos, não da essencialidade do serviço ao usuário.<br>"
        "<i>Fonte: TPS 2022 Q69 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2022 Q69] 3 – Tributos mais altos em bens que causam vício, como cigarros e bebidas "
        "alcoólicas, têm a quase-totalidade de seu efeito sobre o bem-estar do consumidor.",
        "<b>CERTO.</b> Bens viciantes têm demanda altamente inelástica — os consumidores continuam "
        "comprando mesmo com preço mais alto. Por isso, o imposto é arcado quase integralmente "
        "pelo consumidor, reduzindo seu bem-estar.<br>"
        "<i>Fonte: TPS 2022 Q69 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2022 Q69] 4 – Um produto ter elasticidade-renda unitária significa que um aumento "
        "de percentual na renda do consumidor não produzirá efeito na receita total auferida pelo "
        "vendedor.",
        "<b>ERRADO.</b> Elasticidade-renda unitária (εR = 1) significa que a quantidade demandada "
        "cresce na mesma proporção que a renda — a participação no orçamento permanece constante. "
        "Mas a receita total (P × Qd) aumenta, pois Qd cresce.<br>"
        "<i>Fonte: TPS 2022 Q69 – Slides Aula 02 Economia</i>",
    ),

    # ── TPS 2018 — QUESTÃO 72 ──────────────────────────────────────────────────
    (
        "[TPS 2018 Q72] 1 – A tendência à deterioração dos termos de troca afetou as economias "
        "latino-americanas durante todo o século XIX em seu período agroexportador. Esse foi o "
        "motivo pelo qual o Brasil abandonou esse modelo na década de 30 do século XX em prol de "
        "uma política industrial que favorecia bens com forte desempenho no mercado internacional.",
        "<b>ERRADO.</b> A política de substituição de importações (a partir dos anos 1930) visava "
        "desenvolver indústria para o mercado <b>interno</b>, não para exportação. O impulso "
        "imediato foi a Grande Depressão (1929) e o colapso das exportações de café, não apenas "
        "a deterioração dos termos de troca.<br>"
        "<i>Fonte: TPS 2018 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2018 Q72] 2 – Quando o módulo da elasticidade preço da demanda de um produto for "
        "inferior a um, um aumento no seu preço tenderá a reduzir a receita do monopolista.",
        "<b>ERRADO.</b> |e| &lt; 1 = demanda inelástica. Com demanda inelástica, ↑P → ↑RT. "
        "O monopolista aumentaria sua receita ao elevar o preço, não a reduziria.<br>"
        "<i>Fonte: TPS 2018 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2018 Q72] 3 – De acordo com a regra de mark-up, quanto mais preço-elástica for a "
        "curva de demanda do mercado, maior será o poder de mercado do monopolista.",
        "<b>ERRADO.</b> É o inverso: quanto mais elástica a demanda, <b>menor</b> o poder de "
        "mercado. A regra de mark-up mostra que o mark-up ótimo é inversamente proporcional à "
        "elasticidade — demanda elástica limita a capacidade de cobrar acima do custo marginal.<br>"
        "<i>Fonte: TPS 2018 Q72 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2018 Q72] 4 – Curva de demanda de mercado com módulo da elasticidade preço da "
        "demanda inferior a um pode ser indicativa da presença de barreiras à entrada.",
        "<b>CERTO.</b> Baixa elasticidade indica ausência de substitutos próximos — condição "
        "consistente com barreiras à entrada que impedem a concorrência de ofertar alternativas "
        "ao bem.<br>"
        "<i>Fonte: TPS 2018 Q72 – Slides Aula 02 Economia</i>",
    ),

    # ── TPS 2017 — QUESTÃO 67 ──────────────────────────────────────────────────
    (
        "[TPS 2017 Q67] 1 – Um bem de Giffen é um bem com elasticidade-renda da demanda maior "
        "que 1.",
        "<b>ERRADO.</b> Bem de Giffen é um bem <b>inferior</b> (εR &lt; 0), não um bem de luxo "
        "(εR &gt; 1). É um bem inferior e essencial com grande participação no orçamento, cuja "
        "demanda aumenta quando o preço sobe.<br>"
        "<i>Fonte: TPS 2017 Q67 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2017 Q67] 2 – Para os ofertantes de um bem essencial não vale a pena reduzir a "
        "oferta desse bem para forçar o aumento do preço, uma vez que a sua receita total "
        "diminuirá ao fim do processo.",
        "<b>ERRADO.</b> É o contrário: bens essenciais têm demanda <b>inelástica</b>. Com "
        "demanda inelástica, reduzir a oferta eleva o preço mais do que cai a quantidade → "
        "↑RT. Logo, SIM vale a pena reduzir a oferta para aumentar a receita.<br>"
        "<i>Fonte: TPS 2017 Q67 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2017 Q67] 3 – No inverno, uma cidade onde as pessoas disponham de sistemas a gás "
        "para aquecimento de água deve apresentar elasticidade-preço da demanda por eletricidade "
        "maior que a de outra cidade em que haja somente sistemas elétricos de aquecimento de água.",
        "<b>CERTO.</b> Onde há sistemas a gás disponíveis, a eletricidade possui um substituto "
        "próximo para aquecimento. Maior disponibilidade de substitutos → maior "
        "elasticidade-preço da demanda por eletricidade.<br>"
        "<i>Fonte: TPS 2017 Q67 – Slides Aula 02 Economia</i>",
    ),
    (
        "[TPS 2017 Q67] 4 – Se a oferta de um bem tiver elasticidade zero em relação ao preço, "
        "a demanda determinará unicamente o preço de equilíbrio da transação.",
        "<b>CERTO.</b> Com oferta perfeitamente inelástica (curva vertical), a quantidade é fixa "
        "independentemente do preço. O preço de equilíbrio é determinado exclusivamente pelo "
        "ponto em que a curva de demanda intercepta a oferta vertical.<br>"
        "<i>Fonte: TPS 2017 Q67 – Slides Aula 02 Economia</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Economia::Micro Elasticidade",
        "Economia - Micro Elasticidade.apkg",
        ELASTICIDADE,
    )
