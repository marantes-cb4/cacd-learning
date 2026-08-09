# Modelo de Solow

Desenvolvido por Robert Solow (anos 1950-60, Prêmio Nobel). Explica como poupança, crescimento demográfico e progresso tecnológico afetam o produto e o produto per capita, e por que há tanta diversidade de padrão de vida entre países. Modelo inspirado na microeconomia clássica.

---

## Hipóteses do Modelo

**Função de produção:**
> Y = F(K, L)

- **Retornos constantes de escala:** zY = F(zK, zL) — multiplicar todos os fatores aumenta o produto na mesma proporção
- **Produtividade marginal decrescente** do capital E do trabalho: a primeira máquina/trabalhador adiciona mais produção do que a décima
- **Pleno emprego:** economia sempre com fatores plenamente utilizados
- **L./L = n** — taxa de crescimento do trabalho = taxa de crescimento populacional

**Remuneração dos fatores no equilíbrio:**
- r = PMgK (taxa de lucro = produto marginal do capital)
- w = PMgL (salário real = produto marginal do trabalho)
- Teorema de exaustão: Y = rK + wL (toda renda distribuída entre K e L)

**Poupança e investimento:**
- S = sY (s = propensão a poupar, constante)
- S = I (economia fechada em pleno emprego)

**Função de produção per capita** (dividindo por L):
> y = f(k), onde y = Y/L e k = K/L

A curva é côncava (PMg decrescente do capital).

---

## Equação de Acumulação de Capital

**Em nível:**
> K̇ = sY − dK

**Per capita:**
> k̇ = sy − (n+d)k

| Termo | Significado |
|-------|-------------|
| k̇ | Variação do estoque de capital per capita |
| sy | Investimento bruto per capita |
| (n+d)k | Investimento necessário: repor depreciação + equipar novos trabalhadores |

---

## Estado Estacionário (Steady State)

**Condição:** k̇ = 0, ou seja:
> sy = (n+d)k

No steady state: K, L, Y crescem todos à mesma taxa n (**balanced growth path**) → razão K/Y permanece constante; renda per capita para de crescer.

**Dinâmica de convergência:**
- Se k < k\*: sy > (n+d)k → k cresce até k\*
- Se k > k\*: sy < (n+d)k → k cai até k\*

### Efeito do Aumento da Taxa de Poupança (s↑)

- Curva sy desloca para cima → novo k\* maior e y\* maior
- Crescimento per capita é apenas **TEMPORÁRIO** — a economia volta a crescer à taxa n no novo steady state
- **Maior s → maior renda per capita no steady state**, mas sem efeito permanente sobre a taxa de crescimento

### Efeito do Aumento do Crescimento Populacional (n↑)

- Reta (n+d)k fica mais inclinada → k\* menor → y\* menor
- **Países com maior crescimento populacional tendem a ter menor renda per capita**

---

## Solução com Função Cobb-Douglas

> Y = K^α L^(1−α)

Per capita: y = k^α

Steady state:
> k\* = (s / (n+d))^(1/(1−α))
> y\* = (s / (n+d))^(α/(1−α))

- k\* e y\* são **positivamente** relacionados com s e **negativamente** relacionados com n e d

---

## Regra de Ouro

Alta taxa de poupança → alta renda per capita, mas ao custo de baixo consumo per capita (pois c = y − i).

**Regra de Ouro:** nível de k per capita que **maximiza o consumo per capita** no steady state.

> **Condição:** PMgK = n + d

Graficamente: ponto onde a inclinação da função de produção iguala a inclinação da reta (n+d)k.

**Dois casos:**
- k\* < k_ouro → "sub-acumulação": elevar s aumenta o consumo per capita no novo steady state
- k\* > k_ouro → **ineficiência dinâmica**: taxa de poupança tão alta que o consumo per capita é menor do que poderia ser; reduzir s aumenta o consumo

---

## Convergência

| Tipo | Descrição |
|------|-----------|
| **Absoluta** | Países com as mesmas características (mesma s, n, d, tecnologia) convergem para a MESMA renda per capita de equilíbrio; os mais atrasados crescem mais rápido até alcançar os adiantados |
| **Condicional** | Cada país converge para o seu próprio steady state; países com maior s e menor n têm k\* e y\* maiores; todos alcançam o steady state, mas com rendas per capita distintas |

Evidência empírica favorece a convergência condicional.

---

## Modelo de Solow com Progresso Tecnológico

Função de produção:
> Y = F(K, AL)

Onde A = nível tecnológico, crescendo à taxa g: Ȧ/A = g.

**Trabalho efetivo = AL** (estoque de trabalho × produtividade).

Variáveis por unidade de trabalho efetivo:
> k = K/(AL), y = Y/(AL)

Equação de acumulação per trabalho efetivo:
> k̇ = sy − (n+d+g)k

**Estado estacionário:** sy = (n+d+g)k\*

| Variável | Taxa de crescimento no steady state |
|---------|-------------------------------------|
| Y, K (em nível) | n + g |
| Y/L, K/L (per capita) | **g** |
| Y/AL, K/AL (por trabalho efetivo) | 0 |

- O produto per capita cresce à taxa g mesmo no estado estacionário → explica o crescimento sustentado de longo prazo
- **Regra de Ouro com progresso:** PMgK = n + d + g

---

## Resultados e Conclusões

1. O crescimento do produto no longo prazo é determinado por variáveis **exógenas**: n (sem progresso) ou n+g (com progresso)
2. Políticas que elevam s aumentam **temporariamente** o crescimento e **permanentemente** o nível de renda per capita
3. Maior n → menor y\* de equilíbrio
4. O modelo é de **crescimento exógeno** — g não é explicado por variáveis econômicas internas

---

## Críticas ao Modelo de Solow

### Resíduo de Solow (PTF — Produtividade Total dos Fatores)

- Decomposição do crescimento dos EUA: parte explicada por K e L, resto atribuído ao progresso tecnológico
- ~30% do crescimento não é explicado pelos fatores → PTF
- Edward Dennison chamou esse resíduo de **"medida da nossa ignorância"**
- O resíduo pode refletir imprecisão na mensuração de K e L ou retornos crescentes de escala

### Tecnologia como Bem Público

- O modelo assume que A está disponível para todos, sem rivalidade nem exclusão
- Sob concorrência perfeita e retornos constantes de escala: Y = rK + wL (teorema de exaustão do produto) → **nada sobra para remunerar a inovação**
- Inconsistência: a principal fonte de crescimento (g) é exógena e não explicada pelo modelo
- Motivou os modelos de **crescimento endógeno** (Romer, Lucas): endogenizam a inovação via P&D e capital humano

---

## Exercícios do Professor — Questões CACD

1. Aumentos da taxa de poupança, no modelo de Solow, resultam em uma aceleração apenas temporária do crescimento de uma economia, uma vez que a função de produção apresenta retornos decrescentes de escala no capital. **ERRADO**
2. De acordo com o modelo de Solow, quando a economia se encontra em crescimento balanceado, o estoque de capital e o produto crescem à mesma taxa, o que implica que a relação capital-produto permanece constante. **CERTO**
3. No modelo de Solow sem progresso tecnológico, uma vez que, no longo prazo, a taxa de crescimento do produto per capita é igual à taxa de crescimento populacional, países com maior crescimento da população tendem a ter maior nível de renda per capita. **ERRADO**
4. Se um país tem um estoque de capital per capita abaixo do nível da regra de ouro, então este país precisa elevar sua taxa de poupança para elevar o consumo per capita. **CERTO**
5. No modelo de Solow com progresso tecnológico, o equilíbrio de longo prazo se dará com uma taxa de crescimento do produto per capita igual à taxa de progresso tecnológico mais a taxa de crescimento populacional, se não houver depreciação. **ERRADO**
