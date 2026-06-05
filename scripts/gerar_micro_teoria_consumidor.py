#!/usr/bin/env python3
"""Gera deck Anki: Economia - Micro Teoria do Consumidor e Política Econômica"""

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


CARDS = [
    # ── POLÍTICA ECONÔMICA ─────────────────────────────────────────────────────
    (
        "O que ocorre quando um governo fixa um preço máximo abaixo do preço de equilíbrio?",
        "Gera <b>gap de escassez</b>: quantidade ofertada &lt; quantidade demandada naquele preço. "
        "Os excedentes do consumidor e do produtor combinados diminuem, criando <b>peso morto</b>. "
        "Se o preço máximo for acima do equilíbrio, não exerce efeito.<br>"
        "<i>Fonte: Anotações – Micro Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que ocorre quando o governo fixa um preço mínimo acima do preço de equilíbrio?",
        "Gera <b>excedente de oferta</b>: quantidade ofertada &gt; quantidade demandada. "
        "Ex: salário mínimo acima do equilíbrio gera excedente de mão de obra (<b>desemprego</b>). "
        "Se o preço mínimo for abaixo do equilíbrio, não exerce efeito.<br>"
        "<i>Fonte: Anotações – Micro Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "Como a elasticidade das curvas de oferta e demanda determina a incidência tributária?",
        "A curva <b>mais inelástica</b> arca com maior parte do imposto. Por ser mais resistente "
        "à mudança de preço, ela absorve maior % do ônus tributário.<br>"
        "• Demanda inelástica → consumidores arcam com mais<br>"
        "• Oferta inelástica → produtores arcam com mais<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "A distribuição do ônus do imposto sobre a folha de pagamento depende de quem o governo "
        "cobra formalmente — trabalhadores ou empresas?",
        "<b>Não.</b> A divisão do ônus entre trabalhadores e empresas não depende de quem o "
        "governo cobra formalmente. Depende das <b>elasticidades</b> das curvas de oferta e "
        "demanda de mão de obra — o mercado determina quem efetivamente paga.<br>"
        "<i>Fonte: Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que é o excedente do consumidor e como ele se representa graficamente?",
        "<b>Excedente do consumidor</b> = disposição a pagar − preço efetivamente pago.<br>"
        "Graficamente: área abaixo da curva de demanda e acima do preço de mercado.<br>"
        "Quando o preço cai, novos consumidores entram e os existentes ganham excedente adicional.<br>"
        "<i>Fonte: Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que é o excedente do produtor e como ele se representa graficamente?",
        "<b>Excedente do produtor</b> = preço recebido − custo de produção (inclui custo de "
        "oportunidade).<br>"
        "Graficamente: área abaixo do preço de mercado e acima da curva de oferta.<br>"
        "<i>Fonte: Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que é o excedente total e por que mercados livres são considerados eficientes?",
        "<b>Excedente total</b> = valor para os compradores − custo para os vendedores "
        "(= excedente do consumidor + excedente do produtor).<br>"
        "Mercados livres são eficientes porque maximizam o excedente total: alocam oferta aos "
        "compradores de maior valor e demanda aos vendedores de menor custo.<br>"
        "<i>Fonte: Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    # ── TEORIA DO CONSUMIDOR ───────────────────────────────────────────────────
    (
        "O que é a restrição orçamentária na teoria do consumidor?",
        "Representa o <b>limite das combinações de consumo possíveis</b> dada a renda. "
        "É uma reta cuja inclinação reflete o <b>preço relativo</b> dos bens (Px/Py): a taxa "
        "a que o mercado permite trocar um bem pelo outro.<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "Quais são as 4 propriedades das curvas de indiferença?",
        "1. <b>Curvas mais elevadas são preferíveis</b> às mais baixas<br>"
        "2. <b>Inclinam-se para baixo</b>: reduzir um bem exige mais do outro para manter utilidade<br>"
        "3. <b>Não se cruzam</b>: cruzamento violaria a monotonicidade da função utilidade<br>"
        "4. <b>São convexas</b>: utilidade marginal decrescente → maior disposição de abrir mão "
        "do bem em excesso<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que caracteriza o ponto ótimo do consumidor (união de restrição orçamentária e "
        "curvas de indiferença)?",
        "É o ponto de <b>tangência</b> entre a curva de indiferença mais elevada atingível e "
        "a restrição orçamentária. Nesse ponto:<br>"
        "• TMgS = Px/Py (preço relativo)<br>"
        "• UMgX/Px = UMgY/Py (utilidade marginal por dólar gasto é igual nos dois bens)<br>"
        "A avaliação subjetiva do consumidor coincide com a avaliação do mercado.<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que é a Taxa Marginal de Substituição (TMgS) e o que ela indica no ponto ótimo?",
        "TMgS: taxa à qual o consumidor está disposto a trocar um bem pelo outro mantendo "
        "a mesma utilidade. Depende das utilidades marginais: TMgS = UMgX/UMgY.<br>"
        "No ponto ótimo: TMgS = Px/Py — a avaliação subjetiva coincide com o preço relativo "
        "de mercado.<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "Qual a diferença entre efeito renda e efeito substituição na teoria do consumidor?",
        "<b>Efeito substituição</b>: variação no consumo quando a mudança de preço move o "
        "consumidor ao longo de <i>uma mesma</i> curva de indiferença até nova TMgS.<br>"
        "<b>Efeito renda</b>: variação no consumo quando a mudança de preço move o consumidor "
        "para <i>outra</i> curva de indiferença (como variação do poder aquisitivo).<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "Como o aumento de renda afeta o consumo de bens normais e bens inferiores?",
        "<b>Bem normal</b>: consumo aumenta com aumento de renda.<br>"
        "<b>Bem inferior</b>: consumo <i>diminui</i> com aumento de renda (ex: transporte coletivo "
        "para quem passa a ganhar mais). No efeito renda, se quantidade de um bem cai quando "
        "renda sobe, esse bem é inferior.<br>"
        "<i>Fonte: Anotações + Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),
    (
        "O que é um bem de Giffen e como ele viola a lei da demanda?",
        "Bem de Giffen: bem inferior em que o <b>efeito renda supera o efeito substituição</b>. "
        "Quando o preço sobe:<br>"
        "• Efeito substituição → menos consumo<br>"
        "• Efeito renda (consumidor mais pobre → consome mais do bem inferior) → mais consumo<br>"
        "Resultado: demanda aumenta com o preço — curva de demanda com inclinação positiva.<br>"
        "<i>Fonte: Aula 03 Teoria do Consumidor e Política Econômica</i>",
    ),

    # ── TPS 2019 Q69 ──────────────────────────────────────────────────────────
    (
        "[TPS 2019 Q69] 1 – O pressuposto de que \"quanto mais de um bem, melhor\" é tratado "
        "no axioma da monotonicidade das preferências.",
        "<b>CERTO.</b> O axioma da monotonicidade afirma exatamente isso: mais de um bem é sempre "
        "preferível. Ele explica por que curvas de indiferença mais elevadas são preferidas e por "
        "que elas têm inclinação negativa.<br>"
        "<i>Fonte: TPS 2019 Q69-1</i>",
    ),
    (
        "[TPS 2019 Q69] 2 – A satisfação adicional a cada unidade adicional adquirida do bem é "
        "reflexo da lei da utilidade marginal decrescente.",
        "<b>CERTO.</b> A utilidade marginal decrescente estabelece que cada unidade adicional de "
        "um bem gera menor satisfação do que a anterior — a curva de utilidade total cresce mas "
        "com inclinação cada vez menor.<br>"
        "<i>Fonte: TPS 2019 Q69-2</i>",
    ),
    (
        "[TPS 2019 Q69] 3 – A quantidade máxima que pode ser adquirida de um bem sem reduzir a "
        "utilidade total do consumidor, quando existe, marca um ponto de saciedade.",
        "<b>CERTO.</b> O ponto de saciedade é aquele em que a utilidade marginal é zero — a "
        "partir daí, qualquer unidade adicional gera utilidade marginal negativa, reduzindo a "
        "utilidade total.<br>"
        "<i>Fonte: TPS 2019 Q69-3</i>",
    ),
    (
        "[TPS 2019 Q69] 4 – Bens que apresentam nível de quantidade a partir do qual a satisfação "
        "adicional é negativa têm curva de demanda crescente a partir dessa quantidade.",
        "<b>ERRADO.</b> Se a satisfação adicional é negativa (bem que \"enjoa\"), o consumidor "
        "racional não adquirirá mais desse bem além do ponto de saciedade. A demanda é zero (ou "
        "cessa), não crescente. Curva de demanda crescente violaria a racionalidade.<br>"
        "<i>Fonte: TPS 2019 Q69-4</i>",
    ),

    # ── TPS 2018 Q73 ──────────────────────────────────────────────────────────
    (
        "[TPS 2018 Q73] 1 – Caso as preferências do indivíduo sejam representadas por uma função "
        "de utilidade linear, é possível que ele escolha não consumir um dos bens.",
        "<b>CERTO.</b> Com função de utilidade linear, os bens são substitutos perfeitos e as "
        "curvas de indiferença são retas. O ponto ótimo pode ser uma <b>solução de canto</b> "
        "(corner solution): consumidor gasta toda a renda em apenas um dos bens.<br>"
        "<i>Fonte: TPS 2018 Q73-1</i>",
    ),
    (
        "[TPS 2018 Q73] 2 – Dependendo do formato da curva de indiferença de um consumidor para "
        "dois bens, um deslocamento paralelo de sua restrição orçamentária para cima e para a "
        "direita poderá provocar queda no consumo de um dos bens em questão.",
        "<b>CERTO.</b> Se um dos bens for <b>inferior</b>, o aumento de renda (deslocamento da "
        "restrição orçamentária para fora) leva à redução do consumo desse bem. O \"formato\" "
        "das curvas de indiferença reflete as preferências e determina se o bem é normal ou "
        "inferior.<br>"
        "<i>Fonte: TPS 2018 Q73-2</i>",
    ),
    (
        "[TPS 2018 Q73] 3 – Se o aumento do preço de um bem deixar o consumo inalterado, esse "
        "bem deverá ser um bem normal.",
        "<b>ERRADO.</b> Para consumo inalterado com aumento de preço, os efeitos renda e "
        "substituição devem se cancelar. Isso ocorre tipicamente com <b>bens inferiores</b> "
        "(efeito renda ↑ consumo compensa efeito substituição ↓ consumo). Para bens normais, "
        "ambos os efeitos reduzem o consumo quando o preço sobe.<br>"
        "<i>Fonte: TPS 2018 Q73-3</i>",
    ),
    (
        "[TPS 2018 Q73] 4 – Um aumento no consumo de um bem pode não aumentar o nível de "
        "utilidade de um indivíduo.",
        "<b>CERTO.</b> Bens que causam desutilidade além do ponto de saciedade geram utilidade "
        "marginal negativa — consumir mais reduz (ou não aumenta) a utilidade total. Também "
        "ocorre em situações em que o bem \"enjoa\" (utilidade marginal = 0 ou negativa).<br>"
        "<i>Fonte: TPS 2018 Q73-4</i>",
    ),

    # ── TPS 2013 Q65 ──────────────────────────────────────────────────────────
    (
        "[TPS 2013 Q65] 1 – Se a elasticidade-preço da demanda for infinita, os vendedores "
        "abandonarão o mercado.",
        "<b>CERTO.</b> Com demanda perfeitamente elástica, todo o ônus tributário recai sobre "
        "os vendedores (o preço dos compradores não pode subir). Em concorrência perfeita, o "
        "lucro econômico de longo prazo é zero; o imposto gera lucro negativo e os vendedores "
        "saem do mercado.<br>"
        "<i>Fonte: TPS 2013 Q65-1</i>",
    ),
    (
        "[TPS 2013 Q65] 2 – Vendedores e consumidores arcarão com o peso do imposto, conforme a "
        "sensibilidade das curvas de oferta e demanda às variações de preço.",
        "<b>CERTO.</b> A incidência tributária é dividida conforme as elasticidades relativas: "
        "a curva mais inelástica arca com maior parcela do imposto. Essa distribuição independe "
        "de sobre quem o imposto é formalmente cobrado.<br>"
        "<i>Fonte: TPS 2013 Q65-2</i>",
    ),
    (
        "[TPS 2013 Q65] 3 – Vendedores irão transferir aos compradores o valor relativo a toda "
        "incidência do novo imposto, o que aumentará o preço do bem.",
        "<b>ERRADO.</b> A transferência integral do imposto aos compradores só ocorre se a "
        "demanda for <b>perfeitamente inelástica</b>. Em geral, o ônus é compartilhado: quanto "
        "mais elástica a demanda e mais inelástica a oferta, menor a parcela transferida ao "
        "consumidor.<br>"
        "<i>Fonte: TPS 2013 Q65-3</i>",
    ),
    (
        "[TPS 2013 Q65] 4 – Quanto menor for a elasticidade-preço da demanda, maior será a "
        "incidência do tributo para os consumidores.",
        "<b>CERTO.</b> Demanda menos elástica (mais inelástica) → consumidores menos sensíveis "
        "ao preço → absorvem maior parcela do imposto sem reduzir muito o consumo. Resultado "
        "padrão da teoria de incidência tributária.<br>"
        "<i>Fonte: TPS 2013 Q65-4</i>",
    ),

    # ── TPS 2010 Q54 ──────────────────────────────────────────────────────────
    (
        "[TPS 2010 Q54] 1 – A fixação de um preço mínimo para determinado produto agrícola "
        "resulta em excedentes agrícolas, que serão tanto mais elevados quanto mais inelástica "
        "for a curva de oferta de mercado do produto beneficiado por esse tipo de política.",
        "<b>ERRADO.</b> O excedente é maior quanto mais <b>elástica</b> for a oferta. Com "
        "oferta mais elástica, a quantidade ofertada aumenta mais acima do equilíbrio com o "
        "preço mínimo, ampliando o excedente (Qs − Qd). Oferta inelástica limita o aumento "
        "de Qs, reduzindo o excedente.<br>"
        "<i>Fonte: TPS 2010 Q54-1</i>",
    ),
    (
        "[TPS 2010 Q54] 2 – Supondo-se que, no Brasil, o uso de transporte coletivo seja um bem "
        "inferior, conclui-se que o efeito renda decorrente do aumento do preço das passagens de "
        "ônibus contribui para reforçar o efeito substituição, o que reduz a demanda por esse "
        "tipo de transporte.",
        "<b>ERRADO.</b> Para bem inferior, quando o preço sobe: efeito substituição reduz o "
        "consumo, mas efeito renda age no sentido <i>oposto</i> (consumidor mais pobre → consome "
        "mais do bem inferior). O efeito renda <b>contrabalança</b> (não reforça) o efeito "
        "substituição.<br>"
        "<i>Fonte: TPS 2010 Q54-2</i>",
    ),
    (
        "[TPS 2010 Q54] 3 – Campanhas publicitárias bem-sucedidas, além de deslocarem, para cima "
        "e para a direita, a curva de demanda de mercado do produto anunciado, contribuem, quando "
        "promovem a fidelização do cliente, para tornar essa curva mais preço-inelástica.",
        "<b>CERTO.</b> Publicidade eficaz desloca a demanda para a direita (mais consumidores, "
        "maior disposição a pagar). Ao criar lealdade à marca (fidelização), torna os clientes "
        "menos sensíveis ao preço — demanda mais <b>inelástica</b>.<br>"
        "<i>Fonte: TPS 2010 Q54-3</i>",
    ),
    (
        "[TPS 2010 Q54] 4 – Nos mercados competitivos, a escolha ótima a ser feita por "
        "determinado consumidor corresponde à escolha em que a taxa marginal de substituição "
        "entre dois bens quaisquer é igual para todos os consumidores.",
        "<b>CERTO.</b> Em mercados competitivos, todos os consumidores enfrentam os mesmos "
        "preços. No ponto ótimo de cada um: TMgS = Px/Py. Como o preço relativo é igual para "
        "todos, a TMgS é a mesma para todos os consumidores no equilíbrio.<br>"
        "<i>Fonte: TPS 2010 Q54-4</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Economia::Micro - Teoria do Consumidor e Política Econômica",
        "Economia - Micro Teoria do Consumidor e Politica Economica.apkg",
        CARDS,
    )
