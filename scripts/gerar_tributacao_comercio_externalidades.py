#!/usr/bin/env python3
"""Gera deck Anki: Economia - Custos da Tributação, Comércio Internacional, Externalidades e Bens Públicos"""

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
    # ── TRIBUTAÇÃO ────────────────────────────────────────────────────────────
    (
        "Qual a relação entre elasticidade e peso morto causado por tributos?",
        "• <b>Maior elasticidade → maior peso morto</b>: oferta/demanda reage mais à variação "
        "de preço, então o imposto distorce mais o mercado.<br>"
        "• <b>Curva mais inelástica → absorve mais tributação</b>: quantidade transacionada "
        "cai pouco, o peso morto é menor.<br>"
        "<i>Fonte: Anotações + PPT Aula 04 – Tributação, Comércio Internacional, Externalidades e Bens Públicos</i>",
    ),
    (
        "O que é a Curva de Laffer e o que ela demonstra?",
        "Curva em <b>U invertido</b> que relaciona:<br>"
        "• Eixo X: montante do imposto (alíquota)<br>"
        "• Eixo Y: receita tributária arrecadada<br>"
        "Demonstra que existe um <b>ponto ótimo</b> de receita máxima: acima dele, aumentar "
        "o imposto faz a quantidade transacionada cair tanto que a receita total diminui.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Como imposto pequeno, médio e muito grande afetam peso morto e receita do governo?",
        "• <b>Imposto pequeno</b>: receita pequena, peso morto pequeno.<br>"
        "• <b>Imposto médio</b>: receita maior, peso morto maior.<br>"
        "• <b>Imposto muito grande</b>: receita cai (quantidade despenca), peso morto muito "
        "grande — ponto além do ótimo da Curva de Laffer.<br>"
        "<i>Fonte: PPT Aula 04 – Tributação</i>",
    ),

    # ── COMÉRCIO INTERNACIONAL — EXPORTAÇÃO ───────────────────────────────────
    (
        "Quais os efeitos no mercado interno quando um bem passa a ser exportado?",
        "O preço doméstico <b>sobe</b> ao nível do preço internacional:<br>"
        "• Demanda interna <b>cai</b><br>"
        "• Quantidade produzida <b>aumenta</b><br>"
        "• Diferença (qt produzida − qt demandada internamente) = <b>exportações</b><br>"
        "• Excedente do produtor cresce; excedente total de mercado é <b>maior</b>.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Quais os efeitos no mercado interno quando um bem passa a ser importado?",
        "O preço doméstico <b>cai</b> ao nível do preço internacional (análogo a um preço "
        "máximo abaixo do equilíbrio):<br>"
        "• Demanda interna <b>aumenta</b><br>"
        "• Produção nacional <b>cai</b><br>"
        "• Diferença (qt demandada − qt produzida internamente) = <b>importações</b><br>"
        "• Excedente do consumidor cresce; excedente total de mercado é maior.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Qual o efeito econômico das tarifas de importação?",
        "A tarifa eleva o preço do bem importado:<br>"
        "• Excedente do <b>produtor</b> aumenta (preço geral sobe)<br>"
        "• Excedente do <b>consumidor</b> diminui<br>"
        "• Governo <b>arrecada receita</b> (retângulo entre as quantidades antes e após a tarifa)<br>"
        "• Gera <b>peso morto</b> D + F: excedente total do mercado cai.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Qual a diferença entre tarifas e cotas de importação quanto a seus efeitos econômicos?",
        "Efeitos sobre excedente do produtor/consumidor e peso morto são <b>idênticos</b> "
        "(ambos elevam preço interno e criam peso morto D + F).<br>"
        "Diferença-chave — <b>quem fica com o retângulo de receita (E)</b>:<br>"
        "• <b>Tarifa</b>: receita vai para o <b>governo</b>.<br>"
        "• <b>Cota</b>: receita vai para as <b>empresas detentoras de licença</b> de importação.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Quais os 5 argumentos a favor de restrições ao comércio internacional?",
        "1. <b>Aumento de empregos internos</b>: protege produção nacional.<br>"
        "2. <b>Segurança nacional</b>: dependência de bens-chave estrangeiros é perigosa (ex.: chips).<br>"
        "3. <b>Indústria nascente</b>: protege setores ainda incapazes de competir externamente "
        "(pensamento cepalino).<br>"
        "4. <b>Competição desleal</b>: países sem padrões trabalhistas produzem mais barato.<br>"
        "5. <b>Instrumento de barganha</b>: protecionismo como alavanca de negociação política.<br>"
        "Todos têm <b>natureza política</b>.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),

    # ── EXTERNALIDADES ────────────────────────────────────────────────────────
    (
        "O que é uma externalidade?",
        "Impacto das ações de uma pessoa sobre o <b>bem-estar de terceiros</b> que não "
        "participam da transação. Pode ser <b>positiva</b> (benefício) ou <b>negativa</b> "
        "(custo). Causa falha de mercado porque o preço de mercado não reflete o custo/benefício "
        "social total.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Como a externalidade negativa afeta o equilíbrio de mercado e qual a solução?",
        "<b>Custo social excede o custo privado</b> → quantidade de equilíbrio de mercado "
        "é <b>maior</b> que a socialmente ótima (produz-se demais).<br>"
        "Solução: <b>internalização da externalidade</b> — imposto ou regulação que desloca "
        "a curva de oferta para refletir o custo social e atingir o ponto ótimo.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Como a externalidade positiva afeta o equilíbrio de mercado e qual a solução?",
        "<b>Valor social excede o valor privado</b> → quantidade de equilíbrio de mercado "
        "é <b>menor</b> que a socialmente ótima (produz-se de menos).<br>"
        "Solução: o governo <b>subsidia</b> a atividade para estimular maior produção/consumo "
        "até o ponto ótimo (ex.: subsídios à educação, P&D).<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "O que afirma o Teorema de Coase?",
        "Se os agentes privados puderem <b>negociar sem custo</b> a alocação de recursos, "
        "resolverão por si só o problema de externalidade — independentemente de quem detém "
        "o direito de propriedade sobre o recurso em questão.<br>"
        "Condição necessária: direitos de propriedade <b>bem definidos</b>.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Por que o Teorema de Coase nem sempre funciona na prática?",
        "<b>Custos de transação</b>: quando há muitos agentes afetados pela externalidade "
        "(ex.: poluição do ar em uma cidade), os custos de coordenação e negociação tornam "
        "a solução privada inviável — os agentes privados não conseguem chegar a um acordo "
        "sem intervenção do governo.<br>"
        "<i>Fonte: PPT Aula 04 – Externalidades</i>",
    ),
    (
        "Quais as principais políticas públicas para corrigir externalidades?",
        "1. <b>Regulamentação</b>: normas que proíbem ou limitam a atividade.<br>"
        "2. <b>Impostos de Pigou</b>: taxam externalidades negativas — definem o <b>preço</b> "
        "da poluição por unidade emitida.<br>"
        "3. <b>Subsídios de Pigou</b>: estimulam externalidades positivas.<br>"
        "4. <b>Licenças de poluição (cap-and-trade)</b>: definem a <b>quantidade</b> total "
        "permitida; ex.: <b>Mercado de Créditos de Carbono</b>. Tanto impostos quanto licenças "
        "levam ao mesmo ponto de equilíbrio de preço e quantidade.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),

    # ── BENS PÚBLICOS E RECURSOS COMUNS ───────────────────────────────────────
    (
        "Como os bens são classificados segundo exclusão e rivalidade?",
        "<table style='border-collapse:collapse'>"
        "<tr><td></td><td><b>Excludente</b></td><td><b>Não excludente</b></td></tr>"
        "<tr><td><b>Rival</b></td><td>Bem privado</td><td>Recurso comum</td></tr>"
        "<tr><td><b>Não rival</b></td><td>Bem de clube</td><td>Bem público</td></tr>"
        "</table><br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "O que são bens públicos e quais os exemplos relevantes para o CACD?",
        "Bens <b>não excludentes e não rivais</b>: não se pode impedir o uso por ninguém e "
        "o uso por um não reduz a disponibilidade para outros.<br>"
        "Exemplos: defesa nacional; pesquisa de base (ex.: vacinas COVID-19); programas de "
        "combate à pobreza; sirene de risco de desabamento.<br>"
        "<b>Dificuldade</b>: provisão ótima requer análise de custo-benefício complexa, pois "
        "não há mecanismo de mercado para revelar as preferências dos indivíduos.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "Como o sistema de patentes afeta a classificação da pesquisa científica?",
        "• <b>Pesquisa de base</b> (conhecimento geral): bem público — não excludente e "
        "não rival; qualquer um pode usar sem custo adicional.<br>"
        "• <b>Inovação tecnológica específica</b>: com patente, torna-se <b>excludente</b> "
        "(bem de clube) — terceiros precisam de licença. Permanece não rival.<br>"
        "O sistema de patentes cria incentivos à inovação ao tornar temporariamente "
        "excludente o resultado do P&D.<br>"
        "<i>Fonte: PPT Aula 04 – Bens Públicos</i>",
    ),
    (
        "O que são recursos comuns e por que geram problema econômico?",
        "Bens <b>rivais mas não excludentes</b>: ninguém pode ser impedido de usá-los, "
        "mas o uso por um reduz a disponibilidade para outros.<br>"
        "Problema: <b>uso excessivo</b> — como ninguém é dono nem paga pelo uso, os agentes "
        "ignoram o custo imposto aos demais (externalidade negativa).<br>"
        "Ex.: pesqueiros, pastagens, praia lotada → Tragédia dos Comuns.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "O que é o problema do free rider (carona) em bens públicos?",
        "Indivíduos usufruem de um bem público <b>sem contribuir</b> para seu financiamento, "
        "pois o bem é não excludente. Resultado: o mercado privado fornece uma quantidade "
        "<b>inferior</b> à socialmente ótima — justificando a provisão pelo governo.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),
    (
        "O que é a Tragédia dos Comuns?",
        "Fenômeno em que recursos comuns são <b>utilizados em excesso</b> em relação ao "
        "ótimo social. Como ninguém possui nem gerencia o recurso, os agentes não "
        "internalizam o custo que seu uso impõe aos demais — gerando uma "
        "<b>externalidade negativa</b> que degrada o recurso para todos.<br>"
        "<i>Fonte: Anotações + PPT Aula 04</i>",
    ),

    # ── TPS 2023 – Q70 (TARDE, TIPO A) ────────────────────────────────────────
    (
        "[TPS 2023 – Q70] O mercado doméstico de um bem é descrito por P = 100 − 5Q (demanda) "
        "e P = 10 + 4Q (oferta). Item 1: Caso o preço praticado no mercado internacional seja "
        "de 50 unidades monetárias, o país importará 150 unidades do bem.",
        "<b>ERRADO.</b> O preço de equilíbrio doméstico é P* = 50 (igualando oferta e demanda: "
        "100 − 5Q = 10 + 4Q → Q* = 10, P* = 50). Com preço internacional <b>igual</b> ao preço "
        "de equilíbrio, não há vantagem em importar nem exportar: Q_d = Q_s = 10. "
        "Importações = 0, não 150.<br>"
        "<i>Fonte: TPS 2023 – Q70 / Gabarito definitivo IADES (E)</i>",
    ),
    (
        "[TPS 2023 – Q70] Item 2: Caso seja imposta uma cota de 9 unidades de importação, o "
        "preço praticado no mercado internacional será de 70 unidades monetárias.",
        "<b>ERRADO.</b> Cotas afetam o <b>preço doméstico</b>, não o preço internacional "
        "(hipótese de pequeno país). Com cota = 9, o preço doméstico seria: "
        "(100−P)/5 − (P−10)/4 = 9 → P = 30 UM, não 70. Além disso, o mercado internacional "
        "não é afetado pelas decisões de importação de um pequeno país.<br>"
        "<i>Fonte: TPS 2023 – Q70 / Gabarito definitivo IADES (E)</i>",
    ),
    (
        "[TPS 2023 – Q70] Item 3: Caso seja imposta uma tarifa lump sum no valor de 50 unidades "
        "de importação, a quantidade consumida no mercado doméstico será superior a 20 unidades "
        "do bem.",
        "<b>ERRADO.</b> Com P* = 50 (equilíbrio sem comércio), qualquer tarifa que eleve o "
        "preço doméstico ao nível do equilíbrio ou acima dele elimina as importações. A "
        "quantidade demandada <b>sem comércio</b> é Q* = 10. Com tarifa, o preço doméstico "
        "é maior que o de livre comércio, reduzindo Q_d abaixo da quantidade de livre comércio "
        "— jamais superior a 20.<br>"
        "<i>Fonte: TPS 2023 – Q70 / Gabarito definitivo IADES (E)</i>",
    ),
    (
        "[TPS 2023 – Q70] Item 4: Quanto maior a tarifa imposta, maior a tendência de perda "
        "de eficiência e maior o ganho de excedente do consumidor verificado.",
        "<b>ERRADO.</b> Maior tarifa → maior peso morto (perda de eficiência) ✓. Porém, "
        "maior tarifa também <b>eleva</b> o preço doméstico → excedente do consumidor "
        "<b>diminui</b> (não aumenta). O item erra ao afirmar que o consumidor <i>ganha</i> "
        "com tarifas mais altas — ocorre exatamente o contrário.<br>"
        "<i>Fonte: TPS 2023 – Q70 / Gabarito definitivo IADES (E)</i>",
    ),

    # ── TPS 2019 – Q67 (TARDE, TIPO A) ────────────────────────────────────────
    (
        "[TPS 2019 – Q67] Item 1: Para o bem-estar dos consumidores, os efeitos negativos da "
        "imposição de uma tarifa ad valorem sobre as importações podem ser compensados por ganhos "
        "nos termos de troca, quando a demanda do país que impõe a tarifa é capaz de influenciar "
        "os preços mundiais de um produto.",
        "<b>CERTO.</b> Argumento dos <b>termos de troca</b> (large country): um país grande "
        "o suficiente para influenciar o preço mundial pode, ao impor tarifas, reduzir o preço "
        "de importação — o exportador estrangeiro absorve parte da tarifa. Esse ganho nos termos "
        "de troca pode compensar a perda de excedente do consumidor doméstico.<br>"
        "<i>Fonte: TPS 2019 – Q67 / Gabarito definitivo IADES (C)</i>",
    ),
    (
        "[TPS 2019 – Q67] Item 2: A concessão de um subsídio às exportações de um produto "
        "resulta em ganhos para os exportadores e em perdas para o governo em razão dos custos "
        "do subsídio, sem efeitos negativos para o bem-estar dos consumidores do país exportador.",
        "<b>ERRADO.</b> O subsídio à exportação eleva o preço recebido pelos exportadores, "
        "o que também eleva o <b>preço doméstico</b> do bem (oferta é desviada para o "
        "exterior). Os <b>consumidores domésticos perdem</b> excedente por pagar mais pelo "
        "produto. O item ignora esse efeito negativo sobre os consumidores do país exportador.<br>"
        "<i>Fonte: TPS 2019 – Q67 / Gabarito definitivo IADES (E)</i>",
    ),
    (
        "[TPS 2019 – Q67] Item 3: Do ponto de vista do governo, os efeitos da imposição de "
        "uma tarifa ou de uma cota de importação são equivalentes, uma vez que o resultado "
        "final de ambos os instrumentos de política comercial é a elevação dos preços internos "
        "do bem importado.",
        "<b>ERRADO.</b> Do ponto de vista do <b>governo</b>, os instrumentos <b>não são "
        "equivalentes</b>: a tarifa gera <b>receita para o governo</b>, enquanto a cota "
        "transfere essa receita (retângulo E) para os <b>detentores de licenças de importação</b>. "
        "O efeito sobre o preço doméstico pode ser equivalente, mas não do ponto de vista fiscal.<br>"
        "<i>Fonte: TPS 2019 – Q67 / Gabarito definitivo IADES (E)</i>",
    ),
    (
        "[TPS 2019 – Q67] Item 4: A imposição de tarifas à exportação é adotada, em certos "
        "casos, como mecanismo de estabilização dos preços internos e contenção de pressões "
        "inflacionárias, mas, em longo prazo, pode resultar em desestímulo à produção e "
        "consequente redução da oferta.",
        "<b>CERTO.</b> Tarifa de exportação → bem fica no mercado doméstico → preço interno "
        "cai → controle inflacionário no curto prazo ✓. No longo prazo, o menor preço reduz "
        "o retorno do produtor, desestimulando investimento e produção → oferta cai ✓.<br>"
        "<i>Fonte: TPS 2019 – Q67 / Gabarito definitivo IADES (C)</i>",
    ),

    # ── TPS 2018 – Q66 (TARDE) ────────────────────────────────────────────────
    (
        "[TPS 2018 – Q66] Trecho 1: Caso Cooke versus Forbes — vapores de sulfato de amônia "
        "produzidos por Forbes escureciam os tapetes que Cooke pendurava para secar. "
        "Item 1: O problema apresentado no primeiro trecho, que se refere ao julgamento do "
        "processo de Cooke contra Forbes, é conhecido como externalidade.",
        "<b>CERTO.</b> A atividade de Forbes (produção de sulfato de amônia) impõe um custo "
        "à atividade de Cooke (tingimento de tapetes) sem que haja compensação de mercado — "
        "definição clássica de <b>externalidade negativa</b>. O custo social de Forbes "
        "excede seu custo privado.<br>"
        "<i>Fonte: TPS 2018 – Q66 / Gabarito definitivo CESPE/Cebraspe (C)</i>",
    ),
    (
        "[TPS 2018 – Q66] Item 2: A solução para o problema apresentado no primeiro trecho, "
        "de acordo com o teorema de Coase, é a correta atribuição dos direitos de propriedade "
        "envolvidos no caso, desde que não haja custos de transação.",
        "<b>CERTO.</b> O Teorema de Coase afirma que, com <b>direitos de propriedade bem "
        "definidos</b> e <b>ausência de custos de transação</b>, Cooke e Forbes negociarão "
        "privadamente e chegarão ao resultado eficiente — independentemente de quem detém o "
        "direito (ao ar limpo ou à poluição).<br>"
        "<i>Fonte: TPS 2018 – Q66 / Gabarito definitivo CESPE/Cebraspe (C)</i>",
    ),
    (
        "[TPS 2018 – Q66] Item 3: O teorema de Coase permite inferir que, eliminados os custos "
        "de transação, seria possível Cooke vender para Forbes o seu direito a ter ar limpo, "
        "de modo que este pudesse emitir os vapores de sulfato de amônia.",
        "<b>CERTO.</b> Se Cooke detém o direito ao ar limpo (direito de propriedade definido), "
        "Forbes pode <b>comprar</b> esse direito de Cooke pagando uma compensação adequada. "
        "Com custo de transação zero, a negociação ocorre e o resultado é eficiente. "
        "O Teorema de Coase prevê exatamente esse tipo de solução privada.<br>"
        "<i>Fonte: TPS 2018 – Q66 / Gabarito definitivo CESPE/Cebraspe (C)</i>",
    ),
    (
        "[TPS 2018 – Q66] Item 4: No segundo trecho, faz-se referência ao tributo (ou imposto) "
        "Tobin.",
        "<b>ERRADO.</b> O tributo adequado para corrigir externalidades negativas é o "
        "<b>imposto de Pigou</b> (Pigouvian tax) — taxa cobrada do poluidor por unidade de "
        "externalidade gerada, internalizando o custo social. O <b>imposto Tobin</b> é "
        "proposta distinta: taxa sobre transações financeiras internacionais, sem relação com "
        "externalidades de produção.<br>"
        "<i>Fonte: TPS 2018 – Q66 / Gabarito definitivo CESPE/Cebraspe (E)</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Economia::Custos da Tributação, Comércio Internacional, Externalidades e Bens Públicos",
        "Economia - Custos da Tributacao, Comercio Internacional, Externalidades e Bens Publicos.apkg",
        CARDS,
    )
