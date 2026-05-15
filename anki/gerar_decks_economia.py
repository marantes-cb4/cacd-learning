#!/usr/bin/env python3
"""Gera todos os decks de Anki para Economia do CACD."""
import genanki
import random
import os

os.makedirs("/Users/isabelamarantes/Desktop/cacd-learning/anki/decks", exist_ok=True)

def make_deck(deck_title, file_path, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        'CACD Economia',
        fields=[{'name': 'Frente'}, {'name': 'Verso'}],
        templates=[{
            'name': 'Card',
            'qfmt': '{{Frente}}',
            'afmt': '{{FrontSide}}<hr id=answer>{{Verso}}',
        }]
    )
    deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_title)
    for frente, verso in cards:
        deck.add_note(genanki.Note(model=model, fields=[frente, verso]))
    genanki.Package(deck).write_to_file(file_path)
    print(f"✅ {os.path.basename(file_path)} — {len(cards)} cards")
    return len(cards)

BASE = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks"

# ─────────────────────────────────────────────────────────────
# 1.1 DEMANDA DO CONSUMIDOR
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Demanda do Consumidor",
    f"{BASE}/demanda_consumidor_economia.apkg",
    [
        ("O que são preferências do consumidor?",
         "Ordenação subjetiva das cestas de consumo segundo a satisfação (utilidade) que proporcionam. [Manual Candidato Eco, Cap. 1.1.1]"),
        ("O que é uma curva de indiferença?",
         "Conjunto de cestas que proporcionam o mesmo nível de utilidade ao consumidor. [Manual Candidato Eco, Cap. 1.1.1]"),
        ("O que é a Taxa Marginal de Substituição (TMS)?",
         "Quantidade do bem Y que o consumidor cede para obter uma unidade extra do bem X mantendo a utilidade constante. [Manual Candidato Eco, Cap. 1.1.1]"),
        ("O que é utilidade marginal decrescente?",
         "A cada unidade adicional consumida de um bem, o acréscimo de satisfação (utilidade marginal) é menor que o anterior. [Manual Candidato Eco, Cap. 1.1.1]"),
        ("Como se determina o equilíbrio do consumidor?",
         "Maximizando a utilidade sujeita à restrição orçamentária: TMS = Px/Py (tangência entre curva de indiferença e reta orçamentária). [Manual Candidato Eco, Cap. 1.1.2]"),
        ("O que desloca a curva de demanda (vs. movimento ao longo dela)?",
         "Renda, preço de outros bens, expectativas e gostos a deslocam. Variação do próprio preço gera movimento ao longo da curva. [Manual Candidato Eco, Cap. 1.1.3]"),
        ("Defina elasticidade-preço da demanda.",
         "ε = (ΔQ/Q) ÷ (ΔP/P). Mede a sensibilidade da quantidade demandada a variações no preço do bem. [Manual Candidato Eco, Cap. 1.1.4]"),
        ("Quando a demanda é considerada inelástica?",
         "Quando |ε| < 1: a variação percentual na quantidade é menor que a variação percentual no preço. [Manual Candidato Eco, Cap. 1.1.4]"),
        ("Defina elasticidade-renda da demanda.",
         "ε_y = (ΔQ/Q) ÷ (ΔY/Y). Positiva para bens normais, negativa para bens inferiores. [Manual Candidato Eco, Cap. 1.1.4]"),
        ("O que são bens inferiores?",
         "Bens cuja quantidade demandada cai quando a renda aumenta (elasticidade-renda negativa). Ex.: transporte público. [Manual Candidato Eco, Cap. 1.1.3]"),
        ("O que são bens de Giffen?",
         "Bens inferiores cuja demanda aumenta com o aumento do preço (curva de demanda positivamente inclinada), pois o efeito-renda supera o efeito-substituição. [Manual Candidato Eco, Cap. 1.1.3]"),
        ("O que é o efeito substituição de uma alta de preço?",
         "O consumidor substitui o bem que ficou mais caro por outros bens relativamente mais baratos, reduzindo sua demanda. [Manual Candidato Eco, Cap. 1.1.2]"),
        ("O que é o efeito renda de uma alta de preço?",
         "O aumento de preço reduz o poder de compra real do consumidor, alterando as quantidades demandadas de todos os bens. [Manual Candidato Eco, Cap. 1.1.2]"),
        ("O que é elasticidade-preço cruzada?",
         "ε_xy = (ΔQx/Qx) ÷ (ΔPy/Py). Positiva para substitutos, negativa para complementares. [Manual Candidato Eco, Cap. 1.1.4]"),
        ("O que são bens complementares?",
         "Bens consumidos conjuntamente; aumento do preço de um reduz a demanda pelo outro (ε cruzada < 0). Ex.: café e açúcar. [Manual Candidato Eco, Cap. 1.1.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 1.2 OFERTA DO PRODUTOR
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Oferta do Produtor",
    f"{BASE}/oferta_produtor_economia.apkg",
    [
        ("Quais são os principais fatores de produção?",
         "Terra (recursos naturais), Trabalho, Capital (físico e humano) e Tecnologia. [Manual Candidato Eco, Cap. 1.2.1]"),
        ("O que é uma função de produção?",
         "Relação técnica entre insumos (K, L) e produto: Q = f(K, L). Indica o máximo produzível com cada combinação de fatores. [Manual Candidato Eco, Cap. 1.2.2]"),
        ("O que é o produto marginal do trabalho (PML)?",
         "PML = ΔQ/ΔL: aumento no produto decorrente do emprego de uma unidade adicional de trabalho, mantido o capital fixo. [Manual Candidato Eco, Cap. 1.2.4]"),
        ("O que diz a Lei dos Rendimentos Marginais Decrescentes?",
         "Mantidos os demais fatores constantes, o produto marginal de um fator decresce à medida que sua utilização aumenta. [Manual Candidato Eco, Cap. 1.2.4]"),
        ("O que são rendimentos constantes de escala?",
         "Ao dobrar todos os insumos, o produto dobra exatamente: f(tK, tL) = t·f(K, L). [Manual Candidato Eco, Cap. 1.2.5]"),
        ("O que são rendimentos crescentes de escala?",
         "Ao dobrar todos os insumos, o produto mais que dobra: f(tK, tL) > t·f(K, L). Levam à tendência de concentração de mercado. [Manual Candidato Eco, Cap. 1.2.5]"),
        ("O que são custos fixos?",
         "Custos que não variam com a quantidade produzida no curto prazo (ex.: aluguel, deprecição de equipamentos). [Manual Candidato Eco, Cap. 1.2.6]"),
        ("O que é custo marginal (CMg)?",
         "Acréscimo no custo total ao se produzir uma unidade adicional: CMg = ΔCT/ΔQ. [Manual Candidato Eco, Cap. 1.2.6]"),
        ("Qual a relação entre custo marginal e custo médio?",
         "CMg &lt; CMed: CMed decrescente; CMg &gt; CMed: CMed crescente. CMg corta CMed em seu ponto mínimo. [Manual Candidato Eco, Cap. 1.2.6]"),
        ("Como se define a curva de oferta de curto prazo de uma firma competitiva?",
         "É a curva de custo marginal acima do custo variável médio mínimo (ponto de fechamento). [Manual Candidato Eco, Cap. 1.3]"),
        ("O que é elasticidade-preço da oferta?",
         "ε_s = (ΔQ/Q) ÷ (ΔP/P). Mede a resposta da quantidade ofertada a variações no preço; positiva e maior no longo prazo. [Manual Candidato Eco, Cap. 1.2.3]"),
        ("O que desloca a curva de oferta?",
         "Custos dos insumos, tecnologia, expectativas de preços futuros e preços de outros bens que podem ser produzidos. [Manual Candidato Eco, Cap. 1.2.3]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 1.3 TIPOS DE MERCADOS E BENS
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Tipos de Mercados e Bens",
    f"{BASE}/tipos_mercados_bens_economia.apkg",
    [
        ("Quais são as características da concorrência perfeita?",
         "Muitos compradores/vendedores, produto homogêneo, livre entrada/saída, informação perfeita — firma é tomadora de preço. [Manual Candidato Eco, Cap. 1.3]"),
        ("No curto prazo, quando uma firma em concorrência perfeita maximiza lucro?",
         "Quando P = CMg. Se P < CVM mínimo, a firma deve encerrar as atividades. [Manual Candidato Eco, Cap. 1.3.1]"),
        ("No longo prazo, qual o lucro econômico em concorrência perfeita?",
         "Zero: a livre entrada de firmas elimina lucros extraordinários até que P = CMed mínimo. [Manual Candidato Eco, Cap. 1.3.1]"),
        ("O que é monopólio natural?",
         "Ocorre quando os custos fixos são muito elevados e os custos médios decrescentes tornam ineficiente ter múltiplas firmas. Ex.: redes de distribuição. [Manual Candidato Eco, Cap. 1.3]"),
        ("Como o monopolista determina quantidade e preço?",
         "Produz onde RMg = CMg; cobra o preço máximo que o mercado aceita para essa quantidade (poder de mercado). [Manual Candidato Eco, Cap. 1.3.1]"),
        ("O que é perda de bem-estar social (peso morto) do monopólio?",
         "Triângulo entre a curva de demanda, a curva de CMg e a quantidade monopolista — transações mutuamente benéficas não realizadas. [Manual Candidato Eco, Cap. 1.3.1]"),
        ("O que é oligopólio?",
         "Mercado com poucos produtores interdependentes; decisão de cada firma depende da reação das rivais. Ex.: OPEP. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que é equilíbrio de Nash no oligopólio?",
         "Situação em que nenhuma firma tem incentivo a mudar sua estratégia dado o comportamento das demais. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que é um cartel?",
         "Acordo explícito entre oligopolistas para fixar preços e/ou dividir mercado, maximizando lucro conjunto como se fossem um monopólio. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que são bens públicos?",
         "Bens não excludentes (não se pode excluir quem não paga) e não rivais (consumo de um não reduz disponibilidade para outros). Ex.: defesa nacional. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que são recursos comuns (bens comuns)?",
         "Bens rivais mas não excludentes; sujeitos à tragédia dos comuns — tendência à sobreutilização. Ex.: pesca em alto mar. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que é uma externalidade negativa?",
         "Custo imposto a terceiros não envolvidos na transação. Ex.: poluição. Solução: imposto pigouviano = custo marginal externo. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que é uma externalidade positiva?",
         "Benefício gerado a terceiros sem compensação. Ex.: vacinação. Solução: subsídio para elevar produção/consumo ao nível socialmente ótimo. [Manual Candidato Eco, Cap. 1.3]"),
        ("O que diz o Teorema de Coase?",
         "Se direitos de propriedade estão bem definidos e custos de transação são zero, partes negociam e atingem o ótimo social independentemente de quem detém o direito. [Manual Candidato Eco, Cap. 1.3]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.1 CONTABILIDADE NACIONAL
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Contabilidade Nacional",
    f"{BASE}/contabilidade_nacional_economia.apkg",
    [
        ("Qual a fórmula do PIB pela ótica da despesa?",
         "PIB = C + I + G + (X − M), sendo C=consumo, I=investimento, G=gastos do governo, X-M=exportações líquidas. [Manual Candidato Eco, Cap. 2.1.4.1]"),
        ("Qual a diferença entre PIB e PNB?",
         "PIB inclui tudo produzido no território; PNB (= RNB) inclui tudo produzido por residentes, independente do país. PNB = PIB + RLEE. [Manual Candidato Eco, Cap. 2.1.4.2]"),
        ("O que é o deflator do PIB?",
         "Deflator = (PIB nominal / PIB real) × 100. Mede variação do nível geral de preços entre o ano-base e o ano corrente. [Mankiw, Princípios de Macro, Cap. 10]"),
        ("O que é produto potencial?",
         "Nível de produto que a economia alcança quando todos os fatores estão plenamente empregados, sem gerar pressões inflacionárias. [Manual Candidato Eco, Cap. 2.1.4.4]"),
        ("Qual a identidade fundamental das contas nacionais em economia fechada?",
         "Poupança nacional = Investimento: S = I. Na contabilidade nacional, toda poupança é automaticamente investida. [Mankiw, Princípios de Macro, Cap. 13]"),
        ("O que é a teoria keynesiana de determinação da renda?",
         "No curto prazo, a demanda agregada (C+I+G+NX) determina o produto; há desemprego involuntário se DA < produto potencial. [Manual Candidato Eco, Cap. 2.1.2]"),
        ("O que diz a teoria clássica sobre determinação da renda?",
         "No longo prazo, a oferta agregada (fatores e tecnologia) determina o produto; preços e salários são flexíveis, garantindo pleno emprego. [Manual Candidato Eco, Cap. 2.1.2]"),
        ("O que é a curva de oferta agregada de longo prazo?",
         "Vertical no nível do produto potencial: variações na demanda agregada só afetam o nível de preços, não o produto. [Mankiw, Princípios de Macro, Cap. 20]"),
        ("O que desloca a curva de demanda agregada?",
         "Política fiscal (G, T), política monetária (M), confiança do consumidor/investidor, câmbio. Inclinação negativa pelos efeitos riqueza, Pigou e mundell. [Mankiw, Princípios de Macro, Cap. 20]"),
        ("Como se calcula a Renda Nacional Disponível Bruta (RNDB)?",
         "RNDB = PIB + RLEE (rendas líquidas do exterior) + TUC (transferências unilaterais correntes). [Manual Candidato Eco, Cap. 2.1.4.2]"),
        ("O que é PIB per capita e quais suas limitações?",
         "PIB/população — indica renda média, mas não capta distribuição, trabalho doméstico, sustentabilidade ou qualidade de vida. [Mankiw, Princípios de Macro, Cap. 10]"),
        ("Qual a identidade S = I em economia aberta?",
         "Poupança nacional = I + NX: S_priv + S_gov = I + (X−M). Déficit comercial implica poupança externa positiva. [Mankiw, Princípios de Macro, Cap. 18]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.2 CONTAS EXTERNAS
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Contas Externas",
    f"{BASE}/contas_externas_economia.apkg",
    [
        ("Quais são as contas principais do Balanço de Pagamentos?",
         "Transações correntes (balança comercial, serviços, rendas, transferências) e Conta capital e financeira. [Manual Candidato Eco, Cap. 2.1.5]"),
        ("O que compõe a Conta de Transações Correntes?",
         "Balança comercial (X−M de bens), balança de serviços, renda primária (juros, lucros, salários) e renda secundária (remessas). [Manual Candidato Eco, Cap. 2.1.5.1]"),
        ("O que compõe a Conta Capital e Financeira?",
         "Investimento direto estrangeiro (IED), investimento em carteira, derivativos e outros investimentos (créditos comerciais, empréstimos). [Manual Candidato Eco, Cap. 2.1.5.2]"),
        ("Qual a relação entre poupança externa e balanço de pagamentos?",
         "Poupança externa = déficit em conta corrente: quando o país importa mais do que exporta, financia-se com capital externo. [Manual Candidato Eco, Cap. 2.1.5.3]"),
        ("O que são reservas internacionais e qual sua função?",
         "Ativos externos líquidos do Banco Central; garantem liquidez para honrar compromissos externos e defender a moeda. [Manual Candidato Eco, Cap. 2.1.5]"),
        ("O que é um indicador de liquidez externa?",
         "Relação reservas/dívida de curto prazo: mede a capacidade do país de honrar obrigações externas no curto prazo. [Manual Candidato Eco, Cap. 2.1.5]"),
        ("O que é um indicador de solvência externa?",
         "Relação dívida externa total/exportações ou dívida/PIB: avalia a capacidade de longo prazo de geração de divisas para pagamento da dívida. [Manual Candidato Eco, Cap. 2.1.5]"),
        ("O que é a nova metodologia BPM6 do FMI para o Balanço de Pagamentos?",
         "Introduzida em 2014; unifica conta capital com conta financeira e separa renda primária de secundária, alinhando ao padrão SCN 2008. [Manual Candidato Eco, Cap. 2.1.5.4]"),
        ("Superávit ou déficit em conta corrente: o que cada um indica?",
         "Superávit: o país poupa mais do que investe (exportador líquido de capital). Déficit: investe mais do que poupa (importador de capital). [Manual Candidato Eco, Cap. 2.1.5]"),
        ("O que é a conta de Investimento Direto Estrangeiro (IED)?",
         "Fluxo de capital com objetivo de controle (≥ 10% do capital votante); menos volátil que investimento em carteira. [Manual Candidato Eco, Cap. 2.1.5.2]"),
        ("O que é conta financeira no BPM6?",
         "Registra variações em ativos e passivos financeiros externos: IED, carteira, derivativos e outros investimentos, incluindo reservas. [Manual Candidato Eco, Cap. 2.1.5.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.3 SETOR PÚBLICO E POLÍTICA FISCAL
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Setor Público e Política Fiscal",
    f"{BASE}/setor_publico_politica_fiscal_economia.apkg",
    [
        ("O que é o resultado primário do governo?",
         "Receitas − Despesas, excluindo os pagamentos de juros da dívida. Mede o esforço fiscal para pagar a dívida. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que é o resultado nominal (ou resultado fiscal)?",
         "Resultado primário − Juros líquidos da dívida pública. Quando negativo, há déficit nominal (o governo se endivida). [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que é a Equivalência Ricardiana?",
         "Déficit hoje = impostos futuros: agentes racionais poupam o equivalente ao déficit, neutralizando o estímulo fiscal. [Manual Candidato Eco, Cap. 2.3.3]"),
        ("O que é o multiplicador keynesiano de gastos?",
         "k = 1/(1−PMC): aumento de $1 nos gastos públicos eleva o PIB em mais de $1, pois cada rodada de gasto gera nova renda. [Manual Candidato Eco, Cap. 2.3.2]"),
        ("O que é o efeito crowding-out (deslocamento)?",
         "Expansão fiscal aumenta demanda por crédito → eleva taxa de juros → reduz investimento privado, atenuando o efeito expansionista. [Mankiw, Princípios de Macro, Cap. 21]"),
        ("Quais são os instrumentos de política fiscal?",
         "Gastos públicos (G), transferências, impostos (T) e política orçamentária. Podem ser discricionários ou automáticos (estabilizadores). [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que são estabilizadores automáticos?",
         "Mecanismos fiscais que atuam sem decisão política: seguro-desemprego e imposto de renda progressivo reduzem flutuações do PIB. [Mankiw, Princípios de Macro, Cap. 21]"),
        ("Qual a relação entre déficit fiscal e política monetária?",
         "Déficits persistentes podem pressionar o BC a emitir moeda (monetização da dívida), gerando inflação — dominância fiscal. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que é a Lei de Responsabilidade Fiscal (LRF) no Brasil?",
         "Lei Complementar 101/2000: estabelece limites de gasto e endividamento para União, estados e municípios, promovendo equilíbrio fiscal. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que é o superávit primário e por que é monitorado?",
         "É a receita líquida além das despesas (excl. juros); indica capacidade de pagar juros da dívida e controlar a relação dívida/PIB. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("O que são as NFSP (Necessidades de Financiamento do Setor Público)?",
         "Medida do déficit público consolidado brasileiro: primária + juros. Indicam quanto o governo precisa tomar emprestado. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("Como a política fiscal afeta a demanda agregada?",
         "Expansionista (↑G ou ↓T) desloca DA para a direita, elevando produto e preços. Contracionista tem efeito oposto. [Mankiw, Princípios de Macro, Cap. 21]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.4 MODELO IS-LM-BP
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Modelo IS-LM-BP",
    f"{BASE}/modelo_is_lm_bp_economia.apkg",
    [
        ("O que representa a curva IS?",
         "Combinações de (Y, i) que equilibram o mercado de bens e serviços: IS tem inclinação negativa (juros altos → menos investimento → menos Y). [Manual Candidato Eco, Cap. 2.3.7.6]"),
        ("O que representa a curva LM?",
         "Combinações de (Y, i) que equilibram o mercado monetário (oferta = demanda por moeda): LM tem inclinação positiva. [Manual Candidato Eco, Cap. 2.3.7.2]"),
        ("O que desloca a curva IS para a direita?",
         "Aumento dos gastos do governo (G), redução de impostos (T) ou aumento autônomo do investimento/consumo. [Manual Candidato Eco, Cap. 2.3.7.7]"),
        ("O que desloca a curva LM para a direita?",
         "Aumento da oferta de moeda (expansão monetária): para dado nível de renda, os juros de equilíbrio monetário caem. [Manual Candidato Eco, Cap. 2.3.7.3]"),
        ("O que representa a curva BP no modelo IS-LM-BP?",
         "Combinações de (Y, i) que equilibram o balanço de pagamentos (conta corrente + conta capital e financeira = 0). [Manual Candidato Eco, Cap. 2.3.8]"),
        ("Qual a inclinação da curva BP?",
         "Positiva, mas menos inclinada que a LM com alta mobilidade de capital; mais inclinada com baixa mobilidade. Com mobilidade perfeita, é horizontal. [Manual Candidato Eco, Cap. 2.3.8]"),
        ("Sob câmbio fixo e mobilidade perfeita de capital, qual política é mais eficaz?",
         "Política FISCAL: desloca IS → tendência de apreciação → BC vende câmbio → M↑ → LM se desloca até novo equilíbrio com Y mais alto. [Manual Candidato Eco, Cap. 2.3.8.1]"),
        ("Sob câmbio flutuante e mobilidade perfeita de capital, qual política é mais eficaz?",
         "Política MONETÁRIA: M↑ → LM direita → i cai → saída de capital → câmbio deprecia → X↑ → IS direita → Y maior. [Manual Candidato Eco, Cap. 2.3.8.1]"),
        ("Por que a política monetária é ineficaz sob câmbio fixo com mobilidade perfeita?",
         "M↑ → i cai → saída de capital → pressão sobre câmbio → BC compra moeda doméstica para defender paridade → M volta ao nível original. [Manual Candidato Eco, Cap. 2.3.8.1]"),
        ("Por que a política fiscal é ineficaz sob câmbio flutuante com mobilidade perfeita?",
         "G↑ → IS direita → i sobe → entrada de capital → câmbio aprecia → X cai e M sobe → IS volta à posição original (crowding-out externo). [Manual Candidato Eco, Cap. 2.3.8.1]"),
        ("O que é o dilema interno-externo no modelo IS-LM-BP?",
         "Conflito entre metas de desemprego (baixa taxa de juros) e equilíbrio do BP (alta taxa de juros); exige combinação de políticas fiscal e monetária. [Manual Candidato Eco, Cap. 2.3.8]"),
        ("O que significa um ponto acima da curva BP?",
         "Superávit no balanço de pagamentos: juros domésticos altos atraem capital ou renda interna insuficiente para financiar importações. [Manual Candidato Eco, Cap. 2.3.8]"),
        ("O que é o Modelo de Mundell-Fleming?",
         "Extensão do IS-LM para economia aberta com câmbio flexível e mobilidade de capital; base para analisar políticas macro em economias abertas. [Manual Candidato Eco, Cap. 2.3.8]"),
        ("Sob baixa mobilidade de capital e câmbio fixo, qual política é mais eficaz?",
         "Política MONETÁRIA: expansão monetária eleva Y sem pressão sobre câmbio se a conta capital é pouco sensível aos juros. [Manual Candidato Eco, Cap. 2.3.8.1]"),
        ("Qual é a equação de equilíbrio simultâneo no modelo IS-LM-BP?",
         "Interseção das três curvas: ponto (Y*, i*) onde mercado de bens, mercado monetário e BP estão em equilíbrio simultâneo. [Manual Candidato Eco, Cap. 2.3.8]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.5 TEORIA MONETÁRIA
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Teoria Monetária",
    f"{BASE}/teoria_monetaria_economia.apkg",
    [
        ("Quais são as três funções da moeda?",
         "Meio de troca (facilita transações), Unidade de conta (padrão de valor) e Reserva de valor (armazena poder de compra). [Manual Candidato Eco, Cap. 2.1.6.2]"),
        ("O que é M1?",
         "Papel-moeda em poder do público + depósitos à vista nos bancos comerciais. Conceito mais restrito de meios de pagamento. [Manual Candidato Eco, Cap. 2.1.6.3]"),
        ("O que é o multiplicador monetário?",
         "m = 1/r, onde r é a taxa de reservas bancárias. Indica o quanto de depósitos o sistema bancário cria a partir de uma unidade de base monetária. [Manual Candidato Eco, Cap. 2.1.6.4]"),
        ("Qual é a Teoria Quantitativa da Moeda?",
         "MV = PY: quantidade de moeda (M) × velocidade de circulação (V) = nível de preços (P) × produto real (Y). [Mankiw, Princípios de Macro, Cap. 17]"),
        ("O que a TQM implica no longo prazo?",
         "Se V e Y são estáveis, ΔM% ≈ Δπ%: inflação é sempre e em todo lugar um fenômeno monetário (Friedman). [Mankiw, Princípios de Macro, Cap. 17]"),
        ("O que é inflação de demanda?",
         "Causada por excesso de demanda agregada em relação ao produto potencial; normalmente associada a expansão monetária ou fiscal. [Manual Candidato Eco, Cap. 2.2.3]"),
        ("O que é inflação de custos (supply-side)?",
         "Causada por aumento nos custos de produção (ex.: choque de petróleo), que desloca a oferta agregada para a esquerda. [Manual Candidato Eco, Cap. 2.2.3]"),
        ("O que é inflação inercial?",
         "Inflação que se auto-alimenta pela indexação de contratos e expectativas adaptativas; independe de excesso de demanda. [Manual Candidato Eco, Cap. 2.2.3]"),
        ("O que é o Efeito Fisher?",
         "i_nominal = i_real + π_esperada: juros nominais incorporam a inflação esperada, preservando o retorno real do credor. [Mankiw, Princípios de Macro, Cap. 17]"),
        ("O que é a neutralidade da moeda?",
         "No longo prazo, variações na oferta de moeda afetam apenas variáveis nominais (preços), não variáveis reais (produto, emprego). [Mankiw, Princípios de Macro, Cap. 17]"),
        ("Quais são os motivos keynesianos para demandar moeda?",
         "Transação (pagar compras correntes), Precaução (imprevistos) e Especulação (reter liquidez quando juros são muito baixos). [Manual Candidato Eco, Cap. 2.1.6.2]"),
        ("O que é a armadilha da liquidez?",
         "Situação em que os juros estão tão baixos (próximos de zero) que política monetária expansionista não estimula a economia: demanda por moeda torna-se infinita. [Manual Candidato Eco, Cap. 2.3.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.6 POLÍTICA MONETÁRIA
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Política Monetária",
    f"{BASE}/politica_monetaria_economia.apkg",
    [
        ("Quais são os três instrumentos clássicos de política monetária?",
         "Reservas compulsórias (altera multiplicador), taxa de redesconto (custo de refinanciamento) e operações de mercado aberto (compra/venda de títulos). [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que são operações de mercado aberto (open market)?",
         "Compra/venda de títulos públicos pelo BC: compra → injeta moeda → juros caem; venda → retira moeda → juros sobem. [Manual Candidato Eco, Cap. 2.3.5]"),
        ("Qual é o principal objetivo do Banco Central?",
         "Garantir a estabilidade do poder de compra da moeda (controle da inflação) e, secundariamente, manutenção da estabilidade financeira. [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que é o sistema de metas de inflação?",
         "Regime em que o BC define meta explícita para a inflação e usa a taxa de juros para atingi-la; ancora expectativas de inflação. [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que é a Curva de Phillips?",
         "Relação inversa de curto prazo entre inflação e desemprego: menor desemprego → maior pressão inflacionária; no longo prazo, é vertical na NAIRU. [Manual Candidato Eco, Cap. 2.2.3.4]"),
        ("O que é a SELIC e como é usada?",
         "Taxa básica de juros da economia brasileira, definida pelo COPOM; instrumento principal de política monetária do Banco Central do Brasil. [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que é Quantitative Easing (QE)?",
         "Compra em larga escala de ativos (títulos privados ou públicos) pelo BC para injetar liquidez quando os juros já estão em zero (política não convencional). [Manual Candidato Eco, Cap. 2.3.6]"),
        ("O que é forward guidance?",
         "Comunicação do BC sobre a trajetória futura esperada da política monetária, para ancorar expectativas e reduzir incerteza nos mercados. [Manual Candidato Eco, Cap. 2.3.6]"),
        ("O que é dominância fiscal?",
         "Situação em que o BC perde controle da inflação porque o governo financia déficits com emissão monetária; a política fiscal domina a monetária. [Manual Candidato Eco, Cap. 2.3.1]"),
        ("Qual é a Regra de Taylor?",
         "i = r* + π + 0,5·(π−π*) + 0,5·(Y−Y*)/Y*: o BC ajusta juros em resposta a desvios da inflação e do produto de suas metas. [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que é regulação macroprudencial?",
         "Conjunto de políticas para reduzir riscos sistêmicos no sistema financeiro: capital mínimo, alavancagem, reservas anticíclicas. [Manual Candidato Eco, Cap. 2.3.4]"),
        ("O que é taxa de redesconto (taxa básica de refinanciamento)?",
         "Taxa cobrada pelo BC nos empréstimos a bancos comerciais; seu aumento encarece o crédito interbancário e contrai a liquidez. [Manual Candidato Eco, Cap. 2.3.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.7 CRESCIMENTO E DESENVOLVIMENTO ECONÔMICO
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Crescimento e Desenvolvimento Econômico",
    f"{BASE}/crescimento_desenvolvimento_economia.apkg",
    [
        ("O que é o Modelo de Solow?",
         "Modelo neoclássico: crescimento de longo prazo depende de acumulação de capital, crescimento populacional e progresso técnico exógeno. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que é o estado estacionário (steady state) no modelo Solow?",
         "Nível de capital per capita em que investimento = depreciação + crescimento populacional; produto per capita é constante sem progresso técnico. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que é o efeito de alcance (catch-up) ou convergência condicional?",
         "Países mais pobres crescem mais rápido que ricos porque o produto marginal do capital é maior quando K é escasso — convergem ao mesmo steady state. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que é a Regra de Ouro de Solow?",
         "Nível de capital que maximiza o consumo per capita no estado estacionário: PMK = δ + n (produto marginal do capital = taxa de depreciação + crescimento pop.). [Mankiw, Princípios de Macro, Cap. 12]"),
        ("Qual a principal limitação do modelo Solow?",
         "O progresso tecnológico é exógeno (mana do céu): o modelo não explica a fonte do crescimento sustentado de longo prazo. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que são modelos de crescimento endógeno?",
         "Modelos onde o progresso tecnológico é explicado dentro do modelo: P&D, capital humano (Lucas), spillovers de conhecimento (Romer). [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que é a destruição criativa de Schumpeter?",
         "Processo pelo qual inovações eliminam tecnologias e empresas antigas (destruição) enquanto criam novas (criação); motor do capitalismo dinâmico. [Manual Candidato Eco, Cap. 2.2.4.1]"),
        ("O que diferencia crescimento econômico de desenvolvimento econômico?",
         "Crescimento = aumento do PIB; Desenvolvimento inclui melhorias em distribuição de renda, saúde, educação e qualidade de vida (IDH). [Manual Candidato Eco, Cap. 2.2.4]"),
        ("O que é o modelo AK (crescimento endógeno simples)?",
         "Y = AK: sem produto marginal decrescente do capital; crescimento per capita é sustentado mesmo sem progresso técnico exógeno. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("Quais políticas públicas favorecem o crescimento segundo Solow?",
         "Poupança/investimento, educação (capital humano), abertura ao comércio, direitos de propriedade, P&D e controle do crescimento populacional. [Mankiw, Princípios de Macro, Cap. 12]"),
        ("O que é o IDH (Índice de Desenvolvimento Humano)?",
         "Índice composto do PNUD que combina renda per capita, longevidade (saúde) e educação (alfabetização + escolaridade). [Manual Candidato Eco, Cap. 2.2.4]"),
        ("O que é a teoria do big push de Rosenstein-Rodan?",
         "Países pobres ficam presos em equilíbrios de baixo crescimento; um grande impulso simultâneo de investimentos é necessário para decolagem. [Manual Candidato Eco, Cap. 2.2.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 2.8 EMPREGO E RENDA
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Emprego e Renda",
    f"{BASE}/emprego_renda_economia.apkg",
    [
        ("O que é desemprego friccional?",
         "Desemprego temporário de quem está entre empregos, buscando melhores oportunidades; é inevitável e resulta do processo de busca. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("O que é desemprego estrutural?",
         "Ocorre quando há incompatibilidade entre habilidades dos trabalhadores e demanda do mercado, ou entre regiões; exige retreinamento ou migração. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("O que é desemprego cíclico (conjuntural)?",
         "Causado pela insuficiência de demanda agregada durante recessões; é temporário e desaparece com a recuperação econômica. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("O que é a taxa natural de desemprego (NAIRU)?",
         "Taxa de desemprego consistente com a inflação estável; igual à soma do desemprego friccional e estrutural. No Brasil, estimada em ~8-10%. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("Qual é a Lei de Okun?",
         "A cada 1 pp acima da taxa natural de desemprego, o produto cai ~2% abaixo do potencial (razão de Okun ≈ 2). [Manual Candidato Eco, Cap. 2.2.2.1]"),
        ("O que é a PEA (População Economicamente Ativa)?",
         "Parcela da população em idade ativa (≥14 anos) que está ocupada ou desocupada (procurando emprego ativamente). [Manual Candidato Eco, Cap. 2.2.2]"),
        ("Como se calcula a taxa de desocupação?",
         "Taxa = (desocupados / PEA) × 100. Desocupados: quem procurou emprego nos últimos 30 dias e não encontrou. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("O que é subemprego?",
         "Situação de trabalhadores ocupados em jornada menor do que desejam (subocupados por insuficiência de horas) ou em atividades aquém de sua qualificação. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("O que é a teoria dos salários de eficiência?",
         "Firmas pagam salários acima do equilíbrio para aumentar produtividade, reduzir rotatividade e atrair melhores trabalhadores — causa desemprego estrutural. [Mankiw, Princípios de Macro, Cap. 15]"),
        ("Por que o salário mínimo pode gerar desemprego?",
         "Se fixado acima do salário de equilíbrio, gera excesso de oferta de trabalho: Q ofertada > Q demandada pela firma. [Mankiw, Princípios de Macro, Cap. 15]"),
        ("O que são indicadores da PNAD Contínua (Brasil)?",
         "Pesquisa trimestral do IBGE: mede taxa de desocupação, subutilização, participação na força de trabalho e rendimento médio. [Manual Candidato Eco, Cap. 2.2.2]"),
        ("Qual a relação entre curva de Phillips e Lei de Okun?",
         "Okun conecta produto ao desemprego; Phillips conecta desemprego à inflação — juntas formam o mecanismo de transmissão da demanda agregada. [Manual Candidato Eco, Cap. 2.2.3.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 3.1 TEORIAS DE COMÉRCIO INTERNACIONAL
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Teorias de Comércio Internacional",
    f"{BASE}/teorias_comercio_economia.apkg",
    [
        ("O que é vantagem absoluta (Adam Smith)?",
         "Um país tem vantagem absoluta no bem que produz usando menos insumos em termos absolutos. Smith recomenda especialização e comércio. [Manual Candidato Eco, Cap. 3.1.1]"),
        ("O que é vantagem comparativa (David Ricardo)?",
         "País deve especializar-se no bem com menor custo de oportunidade relativo, mesmo sem vantagem absoluta em nenhum bem. [Manual Candidato Eco, Cap. 3.1.1]"),
        ("O que diz o Teorema de Heckscher-Ohlin?",
         "Países exportam bens intensivos no fator de produção abundante domesticamente. Ex.: Brasil exporta bens land-intensive. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é o Paradoxo de Leontief?",
         "EUA, rico em capital, exportavam bens trabalho-intensivos — contradição ao H-O explicada por qualidade do trabalho e tecnologia. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é comércio intrasetorial?",
         "Comércio de bens similares entre países de dotação fatorial parecida (ex.: Alemanha exporta e importa automóveis); explicado por economias de escala e diferenciação. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é a Crítica de Prebisch e a tese centro-periferia?",
         "Países periféricos (produtores de commodities) têm termos de troca deteriorantes frente a países centrais (manufaturados); exige industrialização ativa. [Manual Candidato Eco, Cap. 3.2]"),
        ("O que é a deterioração dos termos de troca?",
         "Tendência de queda dos preços de commodities relativamente aos manufaturados; o mesmo volume de exportações compra menos importações ao longo do tempo. [Manual Candidato Eco, Cap. 3.2.1]"),
        ("O que é comércio intrafirma?",
         "Transações entre subsidiárias de uma mesma multinacional; pode manipular preços de transferência para minimizar tributação global. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que são economias de escala como base do comércio (Krugman)?",
         "Países com grande mercado interno geram economias de escala e se tornam competidores globais mesmo sem vantagem natural — base do novo comércio internacional. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é o Teorema de Stolper-Samuelson?",
         "Abertura comercial eleva a remuneração do fator abundante e reduz a do fator escasso: no Brasil, favorece o trabalho rural e prejudica o capital qualificado? Não — favorece terra. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é o argumento da indústria nascente?",
         "Justifica proteção temporária a indústrias novas que ainda não atingiram escala mínima ou curva de aprendizado para competir internacionalmente. [Manual Candidato Eco, Cap. 3.1.2]"),
        ("O que é a teoria de Linder sobre comércio?",
         "Países com renda per capita similar comercializam mais entre si porque seus consumidores demandam produtos semelhantes — explica comércio Norte-Norte. [Manual Candidato Eco, Cap. 3.1.2]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 3.2 MACROECONOMIA ABERTA
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Macroeconomia Aberta",
    f"{BASE}/macroeconomia_aberta_economia.apkg",
    [
        ("O que é a taxa de câmbio nominal?",
         "Preço de uma moeda estrangeira em termos da moeda doméstica. Ex.: R$/USD = 5,00 significa 5 reais por 1 dólar. [Manual Candidato Eco, Cap. 3.3.3]"),
        ("O que é a taxa de câmbio real?",
         "ε = E × (P*/P): mede o preço relativo dos bens externos em termos dos bens domésticos; indica competitividade das exportações. [Manual Candidato Eco, Cap. 3.3.3]"),
        ("O que é a Paridade do Poder de Compra (PPC)?",
         "Teoria segundo a qual a taxa de câmbio nominal ajusta-se para igualar os preços dos mesmos bens em diferentes países no longo prazo. [Mankiw, Princípios de Macro, Cap. 18]"),
        ("O que é câmbio fixo?",
         "Regime em que o BC mantém a taxa de câmbio num valor pré-determinado, intervindo no mercado cambial para defender a paridade. [Manual Candidato Eco, Cap. 3.3.2]"),
        ("O que é câmbio flutuante (limpo)?",
         "Regime em que a taxa de câmbio é determinada pelo mercado sem intervenção do BC; permite absorver choques externos automaticamente. [Manual Candidato Eco, Cap. 3.3.2]"),
        ("O que é câmbio flutuante sujo?",
         "BC intervém ocasionalmente para suavizar volatilidade excessiva sem defender uma meta específica — posição do Brasil desde 1999. [Manual Candidato Eco, Cap. 3.3.2]"),
        ("O que é paridade descoberta de taxa de juros?",
         "i = i* + (E^e − E)/E: juros domésticos = juros externos + depreciação esperada. Arbitragem iguala retornos ajustados pelo câmbio. [Manual Candidato Eco, Cap. 3.3.4]"),
        ("Como o câmbio afeta a inflação (pass-through)?",
         "Depreciação cambial eleva preços de importados e insumos → pass-through: transmissão parcial para o IPCA, dependente da abertura e credibilidade do BC. [Manual Candidato Eco, Cap. 3.3.4]"),
        ("Qual a relação entre poupança externa e câmbio?",
         "Maior poupança externa (déficit em conta corrente) implica câmbio mais apreciado; país se financia com capital externo para consumir/investir além da produção. [Manual Candidato Eco, Cap. 3.3.1]"),
        ("O que é currency board?",
         "Regime extremamente rígido de câmbio fixo em que a base monetária é 100% lastreada em reservas externas. Ex.: Argentina 1991-2001. [Manual Candidato Eco, Cap. 3.3.2]"),
        ("O que é a Paridade de Juros Coberta (CIP)?",
         "i = i* + f (forward premium): garante arbitragem sem risco usando contratos a termo; válida nos mercados financeiros desenvolvidos. [Manual Candidato Eco, Cap. 3.3.4]"),
        ("Como câmbio depreciado afeta o crescimento econômico?",
         "Melhora a competitividade das exportações e reduz importações → aumenta demanda agregada → estimula crescimento, mas eleva custo das importações e infla. [Manual Candidato Eco, Cap. 3.3]"),
        ("O que é o problema do trilema (impossível trindade)?",
         "Um país não pode ter simultaneamente: câmbio fixo, livre mobilidade de capital E política monetária independente — deve abrir mão de um dos três. [Manual Candidato Eco, Cap. 3.3.2]"),
        ("O que são fluxos internacionais de bens vs. capitais?",
         "Bens: medidos pela balança comercial e de serviços. Capitais: medidos pela conta capital e financeira. Pela identidade BP, se há déficit comercial, há influxo de capital. [Mankiw, Princípios de Macro, Cap. 18]"),
        ("Como a relação câmbio-juros afeta o BP?",
         "Juros altos atraem capital (apreciam câmbio) → piora competitividade das exportações. Dilema: juros baixos para crescimento vs. altos para atrair capital. [Manual Candidato Eco, Cap. 3.3.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 3.3 POLÍTICA COMERCIAL
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Política Comercial",
    f"{BASE}/politica_comercial_economia.apkg",
    [
        ("Quais são os efeitos de uma tarifa de importação?",
         "Eleva preço doméstico, reduz consumo e importações, aumenta produção doméstica, gera receita fiscal. Cria peso morto por ineficiência alocativa. [Manual Candidato Eco, Cap. 3.4.1]"),
        ("O que é uma quota de importação?",
         "Limite quantitativo às importações; efeitos similares à tarifa, mas a renda gerada vai para o importador licenciado, não ao governo. [Manual Candidato Eco, Cap. 3.4.1]"),
        ("O que é um subsídio à exportação?",
         "Pagamento governamental ao exportador para tornar seus produtos mais competitivos; eleva preço doméstico, piora bem-estar do consumidor. [Manual Candidato Eco, Cap. 3.4.1.1]"),
        ("Qual a diferença entre tarifa e quota em termos de flexibilidade?",
         "Tarifa permite ajuste automático às variações de preços externos; quota não — pode gerar escassez se preço mundial subir além do esperado. [Manual Candidato Eco, Cap. 3.4.1]"),
        ("O que é tarifa ótima?",
         "Tarifa que maximiza o bem-estar do país importador: reduz importações → deteriora termos de troca do parceiro → ganho às custas do exportador (política de empobrecer o vizinho). [Manual Candidato Eco, Cap. 3.4.1]"),
        ("O que são barreiras não tarifárias?",
         "Normas técnicas, sanitárias, fitossanitárias, licenças de importação e subsídios que restringem o comércio sem serem tarifas explícitas. [Manual Candidato Eco, Cap. 3.4.1]"),
        ("O que é a OMC e qual seu papel?",
         "Organização Mundial do Comércio (1995, sucessora do GATT): foro de negociação e solução de controvérsias para redução de barreiras ao comércio. [Manual Candidato Eco, Cap. 3.4.3]"),
        ("O que foi a Rodada Uruguai do GATT?",
         "1986-1994: criou a OMC, incorporou agricultura e serviços (GATS), propriedade intelectual (TRIPS) e mecanismo de solução de controvérsias. [Manual Candidato Eco, Cap. 3.4.5]"),
        ("O que é desvio de comércio num bloco econômico?",
         "Situação em que a criação do bloco leva a importar de um parceiro ineficiente (dentro do bloco) em vez do fornecedor mais eficiente de fora. [Manual Candidato Eco, Cap. 3.5.5.2]"),
        ("O que é criação de comércio num bloco econômico?",
         "O bloco leva à substituição de produção doméstica cara por importações mais baratas de um parceiro eficiente — aumento do bem-estar. [Manual Candidato Eco, Cap. 3.5.5]"),
        ("O que é protecionismo e quais seus efeitos?",
         "Proteção da produção doméstica via tarifas, quotas etc.; eleva preços ao consumidor, reduz eficiência alocativa, mas pode preservar empregos no curto prazo. [Manual Candidato Eco, Cap. 3.5.3]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.1-4.2 HISTÓRIA ECONÔMICA SEC XIX E PRIMEIRA REPÚBLICA
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: História Econômica Séc XIX e Primeira República",
    f"{BASE}/historia_economica_sec19_republica_economia.apkg",
    [
        ("Qual era a base da economia brasileira no séc. XIX?",
         "Agroexportação escravista: ciclo do café (Sul/Sudeste) e declínio do açúcar (Nordeste); economia dual com grande setor de subsistência. [Manual Candidato Eco, Cap. 4.1]"),
        ("Por que o café se tornou o produto central da economia brasileira no séc. XIX?",
         "Expansão da demanda europeia/americana, condições edafoclimáticas do Vale do Paraíba e depois do Oeste Paulista, disponibilidade de terras baratas. [Manual Candidato Eco, Cap. 4.1.3]"),
        ("O que foi a Política do Encilhamento (1889-1891)?",
         "Reforma financeira de Rui Barbosa: emissão de moeda e crédito fácil para promover industrialização → especulação, inflação e crise bancária. [Manual Candidato Eco, Cap. 4.2.2]"),
        ("O que foi o Funding Loan de 1898?",
         "Acordo de refinanciamento da dívida externa com banqueiros ingleses: o Brasil suspendeu o serviço da dívida e comprometeu receitas aduaneiras como garantia. [Manual Candidato Eco, Cap. 4.2.3]"),
        ("O que foi o Convênio de Taubaté (1906)?",
         "Acordo entre SP, MG e RJ para valorizar o café: governo compraria excedentes com empréstimos externos, sustentando os preços. [Manual Candidato Eco, Cap. 4.2.8]"),
        ("O que é valorização do café?",
         "Política de compra de excedentes pelo governo para sustentar os preços internacionais; financia os cafeicultores mas incentiva superprodução crônica. [Manual Candidato Eco, Cap. 4.2.8]"),
        ("Qual foi o impacto da Primeira Guerra Mundial sobre a economia brasileira?",
         "Interrupção do crédito externo e das importações → oportunidade para a indústria doméstica substituir bens importados; aumento da produção industrial. [Manual Candidato Eco, Cap. 4.2.4]"),
        ("O que explica o crescimento industrial na Primeira República?",
         "Duas teorias: (1) Industrialização induzida por exportações (renda cafeeira financia importações de capital); (2) Teoria dos choques adversos (guerras/crises impõem substituição de importações). [Manual Candidato Eco, Cap. 4.2.9]"),
        ("Como era o padrão monetário do Brasil na Primeira República?",
         "Tentativas de adotar padrão-ouro para estabilizar a taxa de câmbio; recorrentes crises cambiais por déficits no BP cafeeiro. [Manual Candidato Eco, Cap. 4.2.7]"),
        ("O que foi o boom-and-bust da borracha amazônica?",
         "Ciclo 1879-1912: Brasil monopolizava a borracha natural; colapso após plantações britânicas na Malásia derrubarem preços no início do séc. XX. [Formação Eco do Brasil, Furtado, Cap. XV]"),
        ("Qual a relação entre economia cafeeira e industrialização no Brasil?",
         "O complexo cafeeiro gerou demanda por serviços, criou mão de obra assalariada, financiou infraestrutura (ferrovias) e acumulou capital para investimento industrial. [Manual Candidato Eco, Cap. 4.2.9]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.3 INDUSTRIALIZAÇÃO POR SUBSTITUIÇÃO DE IMPORTAÇÕES (ISI)
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Industrialização por Substituição de Importações (ISI)",
    f"{BASE}/industrializacao_isi_1930_economia.apkg",
    [
        ("O que é o modelo de Industrialização por Substituição de Importações (ISI)?",
         "Estratégia de desenvolvimento que substitui importações por produção doméstica via proteção tarifária, crédito subsidiado e câmbio administrado. [Manual Candidato Eco, Cap. 4.4]"),
        ("Quais são as fases do ISI?",
         "Fase fácil: bens de consumo não-duráveis; Fase difícil: bens intermediários e de capital. Cada fase exige mais capital e tecnologia. [Manual Candidato Eco, Cap. 4.4.2.3]"),
        ("Qual foi o papel da CEPAL na defesa do ISI?",
         "Prebisch e a CEPAL argumentavam que a deterioração dos termos de troca exigia industrialização ativa para romper com a dependência de exportações primárias. [Manual Candidato Eco, Cap. 4.4.2.1]"),
        ("Como a crise de 1929 impulsionou o ISI no Brasil?",
         "Colapso das exportações de café → queda da renda e das importações → proteção cambial involuntária estimulou produção industrial para consumo interno. [Manual Candidato Eco, Cap. 4.3]"),
        ("Quais são as críticas ao modelo ISI?",
         "Indústrias ineficientes e de altíssimo custo; proteção excessiva sem incentivo para exportações; desbalanceamento setorial; gerou inflação e restrição externa crônica. [Manual Candidato Eco, Cap. 4.4.3]"),
        ("Qual foi o papel do Estado na industrialização da Era Vargas (1930-1945)?",
         "Estado como empresário direto: criação da CSN (aço), CVRD (minério), FNM (motores) e Petrobras (petróleo) como empresas estatais estratégicas. [Manual Candidato Eco, Cap. 4.5]"),
        ("O que foi o Estado Novo (1937-1945) em termos econômicos?",
         "Centralização política e econômica: criação de empresas estatais, controle cambial, política salarial, industrialização pesada com apoio estatal. [Manual Candidato Eco, Cap. 4.5.1.3]"),
        ("O que é a tese do 'choques adversos' para a industrialização brasileira?",
         "Crises externas (guerras, depressão) forçaram substituição de importações, criando janelas de oportunidade para a indústria doméstica crescer. [Manual Candidato Eco, Cap. 4.2.9.2]"),
        ("Como o ISI afetou a distribuição de renda no Brasil?",
         "Concentração industrial no Sudeste aprofundou desigualdades regionais; protecionismo criou rendas para industriais ao custo dos consumidores e do campo. [Manual Candidato Eco, Cap. 4.4.3]"),
        ("O que foi o Acordo de Bretton Woods e seu impacto para o ISI?",
         "1944: criou FMI e Banco Mundial; permitiu controles de capital e câmbio → deu espaço para políticas protecionistas do ISI em países em desenvolvimento. [Manual Candidato Eco, Cap. 3.6.2]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.4 DÉCADA DE 1950 / PLANO DE METAS
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Década de 1950 e Plano de Metas",
    f"{BASE}/decada_1950_plano_metas_economia.apkg",
    [
        ("O que foi o Plano SALTE (1950)?",
         "Plano do governo Dutra: priorizava Saúde, Alimentação, Transporte e Energia; fracassou por falta de financiamento e coordenação administrativa. [Manual Candidato Eco, Cap. 4.6.1]"),
        ("O que foi o Plano de Metas de JK (1956-1960)?",
         "Programa de desenvolvimento de JK com 31 metas em 5 setores + construção de Brasília; slogan '50 anos em 5'. [Manual Candidato Eco, Cap. 4.7]"),
        ("Quais eram os cinco setores prioritários do Plano de Metas?",
         "Energia (40% dos investimentos), Transportes (29%), Indústrias de base (20%), Alimentação (6%) e Educação (5%). [Manual Candidato Eco, Cap. 4.7.2]"),
        ("Como o Plano de Metas foi financiado?",
         "Capital estrangeiro (multinacionais atraídas por incentivos) + emissão monetária (inflação) + crédito do BNDE. Levou ao desequilíbrio inflacionário. [Manual Candidato Eco, Cap. 4.7.3]"),
        ("Qual o resultado macroeconômico do Plano de Metas?",
         "Crescimento médio do PIB de ~8%/ano; infraestrutura expandida; mas inflação acelerada (de 12% para 30%) e crise do BP ao final do governo. [Manual Candidato Eco, Cap. 4.7.4]"),
        ("O que foi a Instrução 113 da SUMOC (1955)?",
         "Permitiu importação de equipamentos sem cobertura cambial pelo capital estrangeiro — instrumento chave para atrair multinacionais ao Brasil. [Manual Candidato Eco, Cap. 4.7.3]"),
        ("O que foi o 'no' de JK ao FMI?",
         "Em 1959, JK rompeu as negociações com o FMI para evitar ajuste recessivo e manter o ritmo do Plano de Metas, acelerando a inflação. [Manual Candidato Eco, Cap. 4.8.1]"),
        ("O que foi o segundo governo Vargas (1951-1954) em termos econômicos?",
         "Criação da Petrobras (1953) e BNDE; conflito entre expansionistas e ortodoxos (Eugênio Gudin); crise cambial e inflação crescentes. [Manual Candidato Eco, Cap. 4.6.2]"),
        ("O que foi a Lei do Petróleo de 1953 e a criação da Petrobras?",
         "Monopólio estatal do petróleo com criação da Petrobras; motivado por nacionalismo econômico e para reduzir dependência de divisas para importar petróleo. [Manual Candidato Eco, Cap. 4.6.2]"),
        ("Qual o legado do Plano de Metas para a industrialização brasileira?",
         "Consolidou a indústria pesada (automóveis, eletrodomésticos, construção naval, siderurgia); aprofundou a integração vertical da economia brasileira. [Manual Candidato Eco, Cap. 4.7.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.5 PERÍODO 1962-1967 / PLANO TRIENAL / PAEG
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Período 1962-1967: Plano Trienal e PAEG",
    f"{BASE}/periodo_1962_1967_paeg_economia.apkg",
    [
        ("Por que houve desaceleração do crescimento em 1962-1964?",
         "Esgotamento do ISI de bens de consumo, crise fiscal herdada de JK, inflação acima de 50%, tensões políticas e resistência ao ajuste externo. [Manual Candidato Eco, Cap. 4.8]"),
        ("O que foi o Plano Trienal de 1963 (Celso Furtado)?",
         "Tentou conciliar estabilização (corte do déficit, câmbio realista) com crescimento; fracassou por resistência política e hiperinflação iminente. [Manual Candidato Eco, Cap. 4.8.2]"),
        ("O que foi o PAEG (1964-1967)?",
         "Programa de Ação Econômica do Governo Castelo Branco; estabilização ortodoxa com reformas institucionais profundas que moldaram a economia brasileira. [Manual Candidato Eco, Cap. 4.9]"),
        ("Quais foram as principais reformas institucionais do PAEG?",
         "Reforma tributária (novos impostos, SIMPLES fiscal), reforma financeira (criação do Banco Central e CMN), FGTS (fim da estabilidade no emprego), correção monetária. [Manual Candidato Eco, Cap. 4.9.2]"),
        ("O que foi a criação do Banco Central do Brasil (1964)?",
         "Separação do BC do Banco do Brasil; passou a ter controle da política monetária, câmbio e regulação financeira, antes fragmentados. [Manual Candidato Eco, Cap. 4.9.2.2]"),
        ("O que foi a correção monetária (ORTN) criada pelo PAEG?",
         "Indexação automática de contratos, dívidas e títulos públicos à inflação; permitiu o mercado de capitais funcionar com inflação alta. [Manual Candidato Eco, Cap. 4.9.2.2]"),
        ("O que foi o FGTS e como mudou as relações de trabalho?",
         "Fundo de Garantia do Tempo de Serviço (1966): substituiu a estabilidade no emprego após 10 anos por fundo de indenização; reduziu custo de demissão para as firmas. [Manual Candidato Eco, Cap. 4.9.2.4]"),
        ("Como o PAEG preparou o terreno para o 'milagre econômico'?",
         "Reduziu inflação de 80% (1964) para 20% (1968), reformou o sistema financeiro e criou base infraestrutural e institucional para o crescimento acelerado. [Manual Candidato Eco, Cap. 4.9.3]"),
        ("Qual foi o resultado da política salarial do PAEG?",
         "Contenção dos salários reais abaixo da inflação (via fórmula de reajuste subestimada); redistribuiu renda do trabalho para o capital — crítica histórica ao governo militar. [Manual Candidato Eco, Cap. 4.9.2.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.6 MILAGRE ECONÔMICO 1968-1973
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Milagre Econômico (1968-1973)",
    f"{BASE}/milagre_economico_1968_1973_economia.apkg",
    [
        ("O que foi o 'milagre econômico' brasileiro?",
         "Período 1968-1973 com crescimento médio do PIB de ~11% ao ano, inflação declinante e diversificação das exportações. [Manual Candidato Eco, Cap. 4.10]"),
        ("Quais foram as causas do milagre econômico?",
         "Base institucional do PAEG, liquidez internacional abundante (petrodólares), termos de troca favoráveis, câmbio competitivo (minidesvalorizações) e demanda reprimida. [Manual Candidato Eco, Cap. 4.10.1]"),
        ("O que foram as minidesvalorizações cambiais?",
         "Política de desvalorizações frequentes e pequenas da taxa de câmbio para manter competitividade das exportações, introduzida em 1968. [Manual Candidato Eco, Cap. 4.10.3]"),
        ("Qual foi o I PND (Primeiro Plano Nacional de Desenvolvimento)?",
         "Lançado em 1972 (governo Médici): acelerava crescimento via exportações industriais e integração nacional (Transamazônica, eletrificação). [Manual Candidato Eco, Cap. 4.10.2]"),
        ("Qual foi o debate sobre a distribuição de renda no milagre?",
         "Simonsen vs. Fishlow: Simonsen atribuía concentração à educação (questão estrutural); Fishlow criticava a política salarial repressora do regime militar. [Manual Candidato Eco, Cap. 4.10.5]"),
        ("O que foi o 'crescimento com endividamento externo'?",
         "Financiamento do investimento com empréstimos externos baratos; funcionou enquanto os juros eram baixos, mas gerou vulnerabilidade à elevação dos juros americanos. [Manual Candidato Eco, Cap. 4.10.4]"),
        ("Por que o milagre não foi sustentável?",
         "Dependência de capitais externos, concentração de renda, desequilíbrios regionais e ausência de base tecnológica doméstica; choque do petróleo (1973) marcou o fim. [Manual Candidato Eco, Cap. 4.10.6]"),
        ("Qual era a taxa de inflação durante o milagre?",
         "Caiu de ~20% ao ano em 1967 para ~15% em 1972/73 — inflação relativamente baixa para padrões brasileiros — graças às reformas do PAEG e à demanda administrada. [Manual Candidato Eco, Cap. 4.10.3]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.7 DESACELERAÇÃO E II PND
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Desaceleração e II PND (1974-1979)",
    f"{BASE}/desaceleracao_ii_pnd_economia.apkg",
    [
        ("O que foi o Primeiro Choque do Petróleo (1973) e seu impacto no Brasil?",
         "Quadruplicação do preço do petróleo pela OPEP; o Brasil importava ~80% do petróleo consumido → déficit externo grave e pressão inflacionária. [Manual Candidato Eco, Cap. 4.11.1]"),
        ("O que foi o II PND (1975-1979)?",
         "Segundo Plano Nacional de Desenvolvimento do governo Geisel: 'fuga para a frente' com investimentos pesados em petroquímica, hidrelétricas, aço, álcool e transporte. [Manual Candidato Eco, Cap. 4.11.2]"),
        ("Qual era o objetivo do II PND?",
         "Completar a industrialização pesada (bens de capital e insumos básicos), reduzindo a dependência de importações de energia e de insumos industriais. [Manual Candidato Eco, Cap. 4.11.2]"),
        ("Como o II PND foi financiado?",
         "Endividamento externo maciço via empréstimos bancários internacionais (petrodólares reciclados); as estatais foram o veículo principal de captação. [Manual Candidato Eco, Cap. 4.11.3]"),
        ("Qual foi o papel das estatais no II PND?",
         "Estatais (Petrobras, CVRD, Eletrobras, Embraer) foram o braço executor do plano: captaram recursos externos e realizaram os investimentos estratégicos. [Manual Candidato Eco, Cap. 4.11.3]"),
        ("Quais foram os resultados do II PND?",
         "Diversificação industrial, criação do setor de bens de capital, Proálcool (etanol); mas gerou dívida externa elevada e vulnerabilidade ao choque de juros de 1979. [Manual Candidato Eco, Cap. 4.11.4]"),
        ("O que foi o Proálcool (1975)?",
         "Programa Nacional do Álcool: produção em massa de etanol de cana para substituir gasolina, resposta ao choque do petróleo; base da atual liderança brasileira em biocombustíveis. [Manual Candidato Eco, Cap. 4.11.2]"),
        ("Por que a estratégia do II PND foi controversa?",
         "Aprofundou a dívida externa em vez de ajustar a demanda; o 'ajustamento com crescimento' funcionou até 1979 mas tornou a crise seguinte mais severa. [Manual Candidato Eco, Cap. 4.11.4]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.8 CRISE DOS ANOS 1980
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Crise dos Anos 1980",
    f"{BASE}/crise_1980_inflacao_economia.apkg",
    [
        ("O que foi o Choque Volcker (1979-1982)?",
         "O Fed elevou drasticamente as taxas de juros americanas para combater a inflação → dívida externa de países em desenvolvimento explodiu. [Manual Candidato Eco, Cap. 4.12.3]"),
        ("O que foi a crise da dívida de 1982?",
         "Moratória do México (agosto 1982) interrompeu o crédito voluntário para a América Latina → Brasil sofreu corte súbito do financiamento externo. [Manual Candidato Eco, Cap. 4.13]"),
        ("Como o Brasil se ajustou à crise externa nos anos 1980?",
         "Ajuste recessivo: corte drástico de importações, desvalorização cambial, geração de superávit comercial para pagar juros — recessão 1981-83. [Manual Candidato Eco, Cap. 4.13.1]"),
        ("O que é inflação inercial e por que foi central nos anos 1980 no Brasil?",
         "Inflação que se auto-reproduz por mecanismos de indexação (ORTN, salários, contratos); independe de excesso de demanda — debatida por Bresser-Pereira, Bacha, Dornbusch. [Manual Candidato Eco, Cap. 4.14.7]"),
        ("O que foi o Plano Cruzado (1986)?",
         "Congelamento de preços, salários e câmbio; criação do Cruzado; fracassou por excesso de demanda, desindexação incompleta e eleições de 1986. [Manual Candidato Eco, Cap. 4.14.1]"),
        ("O que foi o Plano Bresser (1987)?",
         "Mini-congelamento de preços com ajuste fiscal parcial; durou poucos meses antes de nova aceleração inflacionária. [Manual Candidato Eco, Cap. 4.14.2]"),
        ("O que foi o Plano Collor I (1990)?",
         "Confisco temporário de depósitos bancários e aplicações (bloqueio de cruzados novos) para comprimir a demanda; hiperinflação cedeu temporariamente mas voltou. [Manual Candidato Eco, Cap. 4.14.4]"),
        ("Qual era a natureza da inflação brasileira nos anos 1980 segundo os heterodoxos?",
         "Predominantemente inercial: inflação passada se transmite para inflação futura via contratos indexados; solução = coordenação de preços, não apenas ajuste fiscal. [Manual Candidato Eco, Cap. 4.14.7]"),
        ("Qual era a natureza da inflação brasileira nos anos 1980 segundo os ortodoxos?",
         "Predominantemente fiscal: déficit público financiado por emissão monetária é a causa primária; solução = ajuste fiscal rígido, sem congelamentos. [Manual Candidato Eco, Cap. 4.14.7]"),
        ("O que foi a 'década perdida' dos anos 1980 para o Brasil?",
         "PIB per capita de 1990 era menor que o de 1980; inflação crônica, dívida externa impagável e instabilidade macroeconômica persistente. [Manual Candidato Eco, Cap. 4.12]"),
        ("Como o Brasil gerou superávit comercial nos anos 1980?",
         "Combinação de ajuste cambial (desvalorização), recessão (comprimiu importações) e expansão das exportações agropecuárias e industriais. [Manual Candidato Eco, Cap. 4.13.1]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 4.9 ANOS 1990 / PLANO REAL
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Anos 1990 e Plano Real",
    f"{BASE}/anos_1990_plano_real_economia.apkg",
    [
        ("O que foi a abertura comercial dos anos Collor (1990-1992)?",
         "Redução unilateral e acelerada das tarifas de importação: alíquota média caiu de ~45% para ~14% em 1993; forçou modernização ou fechamento de indústrias domésticas. [Manual Candidato Eco, Cap. 4.15]"),
        ("O que foi o Plano Real (1994)?",
         "Programa de estabilização em três fases: (1) ajuste fiscal, (2) URV (indexador de transição), (3) nova moeda — o Real, com âncora cambial. [Manual Candidato Eco, Cap. 4.14.6]"),
        ("O que foi a URV (Unidade Real de Valor)?",
         "Indexador de transição que converteu todos os preços à mesma velocidade, quebrando a inércia inflacionária antes da introdução do Real em julho de 1994. [Manual Candidato Eco, Cap. 4.14.6]"),
        ("Como o Plano Real controlou a inflação?",
         "Âncora cambial (R$ ≈ US$1) + abertura comercial (disciplinou preços via concorrência externa) + juros reais elevados (atraíram capital e seguraram demanda). [Manual Candidato Eco, Cap. 4.14.6]"),
        ("Qual foi o custo do Plano Real?",
         "Câmbio sobrevalorizado deteriorou a balança comercial e a conta corrente; vulnerabilidade a choques externos (México 1994, Ásia 1997, Rússia 1998). [Manual Candidato Eco, Cap. 4.16.1]"),
        ("O que foi a crise cambial de 1999?",
         "Ataques especulativos forçaram o abandono da âncora cambial em janeiro de 1999; adoção do câmbio flutuante, metas de inflação e metas de superávit primário. [Manual Candidato Eco, Cap. 4.16.2]"),
        ("O que é o tripé macroeconômico adotado em 1999?",
         "Câmbio flutuante + metas de inflação (IPCA) + superávit primário fiscal: novo arcabouço de credibilidade macro. [Manual Candidato Eco, Cap. 4.16.3]"),
        ("O que foram as privatizações dos anos 1990 no Brasil?",
         "Venda de estatais: USIMINAS, CSN, EMBRAER, Vale do Rio Doce, sistema Telebrás; reduziram dívida pública e trouxeram eficiência, mas geraram críticas sobre desnacionalização. [Manual Candidato Eco, Cap. 4.16.4]"),
        ("O que foi o Plano Real do ponto de vista distributivo?",
         "Ganho real dos mais pobres (maior parte da renda em bens de consumo; inflação é imposto regressivo); ampliou demanda interna e consumo da base da pirâmide. [Manual Candidato Eco, Cap. 4.14.6]"),
        ("O que foi o Proer (1995)?",
         "Programa de Estabilização e Reestruturação do Sistema Financeiro: evitou crise bancária após o Plano Real, recapitalizando bancos com problemas de inadimplência. [Manual Candidato Eco, Cap. 4.16.1]"),
    ]
)

# ─────────────────────────────────────────────────────────────
# 5 SÉCULO XXI: MOEDA DIGITAL E BANCOS DIGITAIS
# ─────────────────────────────────────────────────────────────
make_deck(
    "CACD :: Economia :: Século XXI: Moeda Digital e Bancos Digitais",
    f"{BASE}/seculo_xxi_moeda_digital_economia.apkg",
    [
        ("O que são fintechs?",
         "Empresas de tecnologia que oferecem serviços financeiros digitais (crédito, pagamentos, investimentos) com modelos de negócio mais ágeis e baratos que os bancos tradicionais. [Manual Candidato Eco, Cap. 5]"),
        ("O que são bancos digitais (neobancos)?",
         "Bancos sem agências físicas que operam exclusivamente via aplicativos; ex.: Nubank, Banco Inter. Reduziram tarifas e democratizaram o acesso financeiro no Brasil. [Manual Candidato Eco, Cap. 5]"),
        ("O que é o PIX?",
         "Sistema brasileiro de pagamentos instantâneos do Banco Central, lançado em novembro de 2020; transferências 24/7 gratuitas para pessoas físicas. [Manual Candidato Eco, Cap. 5]"),
        ("O que é Open Banking (Open Finance)?",
         "Compartilhamento padronizado de dados financeiros do cliente entre instituições, com seu consentimento; estimula concorrência e inovação no setor financeiro. [Manual Candidato Eco, Cap. 5]"),
        ("O que é uma CBDC (Central Bank Digital Currency)?",
         "Moeda digital emitida diretamente por um banco central, com curso legal; pode ser de varejo (para o público) ou de atacado (entre instituições financeiras). [Manual Candidato Eco, Cap. 5]"),
        ("O que é o Drex?",
         "CBDC brasileira em desenvolvimento pelo Banco Central; versão digital do real — permitirá programação financeira (smart contracts) e transações tokenizadas. [Manual Candidato Eco, Cap. 5]"),
        ("Como as criptomoedas diferem das CBDCs?",
         "Criptomoedas (Bitcoin, Ethereum) são descentralizadas, sem lastro e emitidas por algoritmos; CBDCs são emitidas e garantidas pelo Estado, com política monetária centralizada. [Manual Candidato Eco, Cap. 5]"),
        ("O que é dinheiro de plástico vs. dinheiro digital?",
         "Dinheiro de plástico = cartões de crédito/débito (anos 1990-2010); dinheiro digital = smartphones, pagamentos instantâneos, QR codes — transição em curso nos anos 2020. [Manual Candidato Eco, Cap. 5]"),
        ("Quais são os riscos dos bancos digitais para a estabilidade financeira?",
         "Corrida bancária digital mais rápida, menor capitalização, risco cibernético e possível concentração de dados em poucas plataformas tecnológicas. [Manual Candidato Eco, Cap. 5]"),
        ("Como o Pix afetou o setor bancário brasileiro?",
         "Reduziu uso de DOC/TED e cheques; aumentou inclusão financeira (sem taxa para PF); obrigou bancos tradicionais a adotar inovações e reduzir tarifas. [Manual Candidato Eco, Cap. 5]"),
    ]
)

print("\n🎉 Todos os 23 decks criados com sucesso!")
