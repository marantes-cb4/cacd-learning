#!/usr/bin/env python3
"""Gera deck Anki: Economia - Micro Intro Oferta e Demanda"""

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


MICRO_OFERTA_DEMANDA = [
    # ── 10 PRINCÍPIOS DA ECONOMIA ──────────────────────────────────────────────
    (
        "Quais são os 10 princípios da economia (Mankiw)?",
        "1. Tradeoffs (não se pode ter tudo)<br>"
        "2. Custo de oportunidade<br>"
        "3. Pessoas racionais pensam na margem<br>"
        "4. Pessoas reagem a incentivos<br>"
        "5. Comércio pode ser bom para todos<br>"
        "6. Mercados são uma boa forma de organizar a atividade econômica<br>"
        "7. Governos podem melhorar resultados dos mercados<br>"
        "8. Padrão de vida depende da capacidade produtiva<br>"
        "9. Preços sobem quando o governo emite moeda demais<br>"
        "10. Tradeoff de curto prazo entre inflação e desemprego<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é custo de oportunidade?",
        "É a opção <b>não escolhida</b> — o sacrifício necessário para se obter algo. "
        "Corresponde ao valor da melhor alternativa à qual se renuncia ao tomar uma decisão.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é utilidade marginal e como ela se comporta?",
        "É o benefício (ou custo) <b>adicional</b> de cada unidade extra consumida/produzida. "
        "A utilidade marginal tende a ser <b>decrescente</b>: cada unidade adicional gera menos satisfação "
        "que a anterior (ex: 1ª fatia de pizza satisfaz mais que a 5ª).<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é a Curva de Phillips e qual tradeoff ela representa?",
        "Curva que mostra o <b>tradeoff de curto prazo entre inflação e desemprego</b>: "
        "maior inflação está associada a menor desemprego e vice-versa. "
        "No longo prazo, esse tradeoff desaparece (a curva é vertical).<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda / Slides Aula 01</i>",
    ),

    # ── CONCEITOS BÁSICOS ──────────────────────────────────────────────────────
    (
        "Qual a diferença entre eficiência e equidade na economia?",
        "<b>Eficiência</b>: obter o máximo resultado possível a partir de recursos escassos.<br>"
        "<b>Equidade</b>: distribuir a prosperidade econômica de forma justa entre os membros da sociedade.<br>"
        "Ex.: produzir alimentos em abundância (eficiência) não garante que todos se alimentem (equidade).<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é uma falha de mercado? Quais são os principais tipos?",
        "Situação em que o mercado <b>falha em alocar recursos com eficiência</b>.<br>"
        "Principais tipos:<br>"
        "1. <b>Externalidades</b> (impactos em terceiros não participantes)<br>"
        "2. <b>Poder de mercado</b> (monopólio/oligopólio influencia preços)<br>"
        "3. <b>Bens públicos</b> (não-rivais e não-excludentes — oferta privada insuficiente)<br>"
        "4. <b>Informação assimétrica</b> (agentes não têm conhecimento completo)<br>"
        "<i>Fonte: Slides Aula 01 / Anotações</i>",
    ),
    (
        "O que é externalidade? Dê exemplos positiva e negativa.",
        "Impacto das ações de um agente sobre o bem-estar de <b>terceiros não envolvidos</b> na transação.<br>"
        "<b>Negativa</b>: fábrica polui rio usado por pescadores (custo não pago pelo produtor).<br>"
        "<b>Positiva</b>: vacinação beneficia toda a sociedade além do vacinado.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é poder de mercado?",
        "Capacidade de um <b>único agente</b> (ou pequeno grupo) de influenciar significativamente os "
        "preços de mercado. Empresas com grande market share possuem poder de mercado.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é a Fronteira de Possibilidades de Produção (FPP)?",
        "Gráfico que mostra as combinações máximas de dois bens que uma economia pode produzir com "
        "seus recursos.<br>"
        "• <b>Ponto na curva</b>: eficiente (sem capacidade ociosa)<br>"
        "• <b>Ponto dentro da curva</b>: ineficiente (capacidade ociosa)<br>"
        "• <b>Ponto fora da curva</b>: inviável com os recursos atuais<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Qual a diferença entre análise positiva e análise normativa em economia?",
        "<b>Positiva</b>: descrição de como o mundo <b>é</b> — afirmações verificáveis empiricamente. "
        "Ex.: 'O salário mínimo causa desemprego.'<br>"
        "<b>Normativa</b>: prescrição de como o mundo <b>deveria ser</b> — envolve julgamento de valor. "
        "Ex.: 'O governo deveria aumentar o salário mínimo.'<br>"
        "<i>Fonte: Slides Aula 01</i>",
    ),

    # ── TIPOS DE MERCADO ───────────────────────────────────────────────────────
    (
        "Quais são os 4 tipos de estrutura de mercado?",
        "1. <b>Concorrência perfeita</b>: muitos compradores e vendedores, bens homogêneos, nenhum "
        "influencia o preço (tomadores de preço)<br>"
        "2. <b>Monopólio</b>: único ofertante (ex: distribuidora de energia elétrica)<br>"
        "3. <b>Oligopólio</b>: poucos ofertantes com barreiras de entrada (ex: telefonia)<br>"
        "4. <b>Concorrência monopolística</b>: muitos ofertantes com produtos diferenciados que competem "
        "entre si (ex: calçados)<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é um monopólio natural? Por que pode ser eficiente?",
        "Monopólio que surge quando as <b>barreiras de entrada são tão altas</b> que é mais eficiente "
        "ter uma única empresa oferecendo o bem/serviço do que várias competindo. "
        "Ex.: distribuição de energia elétrica, saneamento básico.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),

    # ── DEMANDA ────────────────────────────────────────────────────────────────
    (
        "O que é a Lei da Demanda?",
        "Tudo mais constante (ceteris paribus), quando o <b>preço de um bem aumenta</b>, "
        "a <b>quantidade demandada cai</b> — relação inversa entre preço e quantidade demandada.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Quais são os determinantes da demanda (além do preço)?",
        "1. <b>Renda</b> (↑ renda → ↑ demanda por bens normais; ↓ demanda por bens inferiores)<br>"
        "2. <b>Preço de bens substitutos</b> (↑ preço do substituto → ↑ demanda do bem)<br>"
        "3. <b>Preço de bens complementares</b> (↑ preço do complementar → ↓ demanda do bem)<br>"
        "4. <b>Gostos/preferências</b><br>"
        "5. <b>Expectativas</b> dos consumidores<br>"
        "6. <b>Número de compradores</b><br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Qual a diferença entre bem normal e bem inferior?",
        "<b>Bem normal</b>: aumento da renda → aumento da quantidade demandada (relação positiva).<br>"
        "<b>Bem inferior</b>: aumento da renda → redução da quantidade demandada "
        "(o consumidor migra para bens de maior qualidade). Ex.: passagem de ônibus.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Qual a diferença entre bens substitutos e bens complementares?",
        "<b>Substitutos</b>: ↑ preço de A → ↑ demanda por B (um pode ser usado no lugar do outro). "
        "Ex.: manteiga e azeite.<br>"
        "<b>Complementares</b>: ↑ preço de A → ↓ demanda por B (são usados juntos). "
        "Ex.: arroz e feijão.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Qual a diferença entre deslocamento da curva de demanda e movimento ao longo da curva?",
        "<b>Movimento ao longo da curva</b>: causado exclusivamente pela variação do <b>preço</b> do bem — "
        "a curva não muda, apenas o ponto sobre ela.<br>"
        "<b>Deslocamento da curva</b>: causado por qualquer outro determinante (renda, gostos, bens "
        "relacionados, expectativas, nº de compradores) — a curva inteira se move para direita (↑ demanda) "
        "ou esquerda (↓ demanda).<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),

    # ── OFERTA ─────────────────────────────────────────────────────────────────
    (
        "O que é a Lei da Oferta?",
        "Tudo mais constante, quando o <b>preço de um bem aumenta</b>, "
        "a <b>quantidade ofertada aumenta</b> — relação positiva entre preço e quantidade ofertada. "
        "A curva de oferta é ascendente.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Quais são os determinantes da oferta (além do preço)?",
        "1. <b>Preço dos insumos</b> (↑ custo dos insumos → ↓ quantidade ofertada)<br>"
        "2. <b>Tecnologia</b> (↑ tecnologia → ↑ produtividade → ↑ quantidade ofertada)<br>"
        "3. <b>Expectativas</b> dos produtores<br>"
        "4. <b>Número de vendedores</b><br>"
        "Todos esses causam <b>deslocamento</b> da curva; o preço causa apenas movimento ao longo dela.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),

    # ── EQUILÍBRIO ─────────────────────────────────────────────────────────────
    (
        "O que é equilíbrio de mercado?",
        "Ponto em que as curvas de oferta e demanda se intersectam: "
        "quantidade ofertada = quantidade demandada. "
        "Determina o <b>preço de equilíbrio</b> e a <b>quantidade de equilíbrio</b>.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é excedente de oferta e como o mercado o corrige?",
        "Ocorre quando o preço está <b>acima do equilíbrio</b>: quantidade ofertada > quantidade demandada. "
        "Vendedores reduzem o preço para escoar o estoque, empurrando o mercado de volta ao equilíbrio.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "O que é escassez (excesso de demanda) e como o mercado a corrige?",
        "Ocorre quando o preço está <b>abaixo do equilíbrio</b>: quantidade demandada > quantidade ofertada. "
        "A pressão dos compradores eleva o preço até o equilíbrio.<br>"
        "<i>Fonte: Anotações – Micro: Intro Oferta e Demanda</i>",
    ),
    (
        "Quais os 3 passos para analisar um deslocamento no modelo de oferta e demanda?",
        "1. Decidir se o evento afeta a curva de <b>oferta</b>, de <b>demanda</b> ou ambas.<br>"
        "2. Decidir em qual <b>direção</b> a curva se desloca (direita ou esquerda).<br>"
        "3. Usar o gráfico para ver como o deslocamento altera o <b>novo ponto de equilíbrio</b> "
        "(preço e quantidade).<br>"
        "<i>Fonte: Slides Aula 01 – Oferta e Demanda</i>",
    ),

    # ── FALHAS DE MERCADO (conceitos) ─────────────────────────────────────────
    (
        "Por que o monopólio é considerado uma falha de mercado?",
        "Porque um único ofertante tem <b>poder de mercado</b> — pode fixar preços acima do nível "
        "competitivo, reduzindo a quantidade produzida abaixo do ótimo social. Isso gera "
        "<b>perda de eficiência</b> (peso morto).<br>"
        "<i>Fonte: Slides Aula 01</i>",
    ),
    (
        "O que são bens públicos e por que o mercado os subprovê?",
        "Bens <b>não-rivais</b> (consumo de um não reduz disponibilidade para outros) e "
        "<b>não-excludentes</b> (não se pode excluir ninguém do consumo). "
        "Como não é possível cobrar por eles eficientemente, o setor privado os subprovê — "
        "justificando intervenção governamental. Ex.: defesa nacional, iluminação pública.<br>"
        "<i>Fonte: Slides Aula 01</i>",
    ),
    (
        "O que é informação assimétrica como falha de mercado?",
        "Ocorre quando os agentes <b>não têm acesso igual à informação</b> sobre um bem/serviço, "
        "impedindo decisões ótimas. Ex.: mercado de seguros — o segurado sabe mais sobre seu risco "
        "do que a seguradora (seleção adversa).<br>"
        "<i>Fonte: Slides Aula 01</i>",
    ),

    # ── TPS 2023 — QUESTÃO 71 ──────────────────────────────────────────────────
    (
        "[TPS 2023 Q71] 1 – O monopólio é uma falha de mercado relacionada à quantidade e à dimensão "
        "dos agentes do lado da oferta.",
        "<b>CERTO.</b> O monopólio é definido pela presença de um único agente vendedor — ou seja, "
        "pela dimensão e quantidade (= 1) dos ofertantes. Essa estrutura configura falha de mercado "
        "por gerar poder de mercado e ineficiência alocativa.<br>"
        "<i>Fonte: TPS 2023 Q71 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2023 Q71] 2 – Quando o preço de equilíbrio não considera custos impostos pela transação "
        "a agentes terceiros, não envolvidos diretamente na transação em estudo, ocorre externalidade "
        "negativa.",
        "<b>CERTO.</b> Externalidade negativa ocorre exatamente quando custos são impostos a terceiros "
        "não participantes da transação e não são internalizados no preço de equilíbrio "
        "(ex.: poluição industrial que prejudica pescadores).<br>"
        "<i>Fonte: TPS 2023 Q71 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2023 Q71] 3 – Bens rivais são uma falha de mercado relativa a marcas concorrentes de "
        "um mesmo produto.",
        "<b>ERRADO.</b> Rivalidade é uma característica de bens: um bem rival é aquele cujo consumo "
        "por uma pessoa reduz a disponibilidade para outros. Isso não é uma falha de mercado nem tem "
        "relação com marcas concorrentes.<br>"
        "<i>Fonte: TPS 2023 Q71 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2023 Q71] 4 – Um bem público é uma falha de mercado originada pela produção do bem "
        "pelo setor público, ou seja, pelo governo.",
        "<b>ERRADO.</b> Bem público se define por ser <b>não-rival</b> e <b>não-excludente</b>, "
        "independentemente de quem o produz. A falha de mercado está na subprovimento pelo setor "
        "privado, não na origem pública da produção.<br>"
        "<i>Fonte: TPS 2023 Q71 – Slides Aula 01 Economia</i>",
    ),

    # ── TPS 2020 — QUESTÃO 70 ──────────────────────────────────────────────────
    (
        "[TPS 2020 Q70] 1 – Se um novo morador migrar para o país e não houver choques exógenos de "
        "oferta e de demanda, pagará o preço de $ 5 por quilo de maçã que adquirir.",
        "<b>CERTO.</b> Em concorrência perfeita, o preço é único e determinado pelo mercado "
        "(lei do preço único). A entrada de um único consumidor não altera o equilíbrio — ele será "
        "tomador de preço e pagará os mesmos $ 5.<br>"
        "<i>Fonte: TPS 2020 Q70 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2020 Q70] 2 – Uma nova mercearia que venda maçãs no pequeno país não terá incentivos "
        "para vender as frutas por menos que $ 5 por quilo, pois obterá lucros menores do que "
        "conseguiria caso mantivesse o preço no nível de equilíbrio.",
        "<b>CERTO.</b> Em concorrência perfeita, o vendedor já consegue vender toda sua produção "
        "ao preço de equilíbrio. Vender abaixo reduz a receita por unidade sem ganho de volume — "
        "resultando em lucros menores.<br>"
        "<i>Fonte: TPS 2020 Q70 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2020 Q70] 3 – Suponha que, no final do ano, haverá a festa nacional das tortas de maçã "
        "não prevista no pequeno país; isso causará uma elevação no preço e um aumento nas quantidades "
        "vendidas de maçãs.",
        "<b>CERTO.</b> A festa aumenta a demanda por maçãs → curva de demanda se desloca para a "
        "direita → novo equilíbrio com preço <b>maior</b> e quantidade <b>maior</b>.<br>"
        "<i>Fonte: TPS 2020 Q70 – Slides Aula 01 Economia</i>",
    ),
    (
        "[TPS 2020 Q70] 4 – Um mês depois da data do texto, uma epidemia assolou o país e reduziu a "
        "população em 40%. Para evitar uma crise no setor de maçãs, o governo fixou o preço das maçãs "
        "em $ 5 por quilo. Com isso, conclui-se que a quantidade semanal vendida de maçãs será a "
        "mesma de antes da epidemia.",
        "<b>ERRADO.</b> A epidemia reduz a demanda (menos compradores) → novo equilíbrio seria em "
        "preço e quantidade menores. O preço fixado em $ 5 fica <b>acima</b> do novo equilíbrio, "
        "criando excedente de oferta. A quantidade efetivamente vendida será <b>menor</b> que antes.<br>"
        "<i>Fonte: TPS 2020 Q70 – Slides Aula 01 Economia</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Economia :: Microeconomia — Introdução, Oferta e Demanda",
        "Economia - Micro Intro Oferta e Demanda.apkg",
        MICRO_OFERTA_DEMANDA,
    )
