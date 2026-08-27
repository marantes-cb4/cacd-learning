# Modelo IS-LM-BP

## Visão geral

- Versão do modelo IS-LM para **economia aberta** — também chamado de **modelo Mundell-Fleming**
- Permite analisar a eficácia das políticas fiscal, monetária e cambial, bem como o impacto de choques externos sobre a economia doméstica
- A abertura da economia introduz dois novos fluxos ao modelo:
  - Fluxos de bens e serviços (balança comercial)
  - Fluxos de capital (balança de capitais)
- Três mudanças em relação ao IS-LM fechado:
  1. A curva **IS** é ampliada para incorporar os fluxos de bens e serviços
  2. A curva **LM** passa a se deslocar também pela atuação do BC no mercado de câmbio (compra/venda de reservas)
  3. Acrescenta-se a curva **BP**, que representa o equilíbrio do balanço de pagamentos (saldo do BP = 0)

---

## A curva IS na economia aberta

> Y = C + I + G + EL, onde EL = exportações líquidas = X − M

- Exportações: X = f(Y*, E) — renda externa e taxa de câmbio nominal
- Importações: M = f(Y, E) — renda doméstica e taxa de câmbio nominal
- **Aumento de Y\* (renda externa) ou de E (desvalorização cambial)** → EL sobe → **IS desloca para a direita**
- **Redução de Y\* ou de E (apreciação cambial)** → EL cai → **IS desloca para a esquerda**

---

## A curva LM na economia aberta

- Desloca-se não só por operações de mercado aberto com títulos da dívida, mas também pela atuação do BC no **mercado de câmbio**
- BC **compra** dólares → eleva a oferta de moeda doméstica (injeta moeda local na economia) → **LM desloca para a direita**
- BC **vende** dólares → contrai a oferta de moeda doméstica → **LM desloca para a esquerda**

---

## A curva BP

- Representa os pares de taxa de juros (i) e renda (Y) que equilibram o balanço de pagamentos (BP = 0, isto é, saldo comercial + saldo da conta de capital = 0)
- **Mecanismo da inclinação positiva** (mobilidade imperfeita de capitais): renda ↑ → importações ↑ → déficit comercial → para reequilibrar o BP, entrada de capitais é necessária → entrada de capitais exige juros ↑ (paridade de juros) → logo, Y e i se movem na mesma direção
- **Casos-limite de inclinação**:
  - **Perfeita mobilidade de capitais** → BP totalmente **horizontal** na taxa de juros internacional (i = i\*, paridade de juros)
  - **Sem mobilidade de capitais** → BP totalmente **vertical** na renda de equilíbrio comercial — juros doméstico independe do internacional
    - À esquerda da linha BP: Y menor → superávit comercial (menos importações)
    - À direita da linha BP: Y maior → déficit comercial (mais importações)
- **Deslocamentos da curva BP**: aumento de Y\* ou de E (desvalorização) elevam o saldo do BP e deslocam a curva **para a direita**; o inverso desloca **para a esquerda**

### Paridade de juros — versão de curto prazo do modelo

- Modelo assume RLRE (balança de rendas) como **variável exógena** e desconsidera IDE, empréstimos e financiamentos
- **Paridade descoberta** (simplificação usada no curto prazo): i = i\*
  - i > i\* → entrada de capital, apreciação cambial
  - i < i\* → saída de capital, depreciação cambial
  - i = i\* → equilíbrio, sem fluxos de capital
- **Paridade coberta** (mais realista): i = i\* + Ê + PR (Ê = expectativa de depreciação cambial; PR = prêmio de risco de default do país)

---

## Premissas do equilíbrio do modelo

- Nível de preços (P) fixo no curto prazo — oferta agregada horizontal; expansões de demanda geram expansões de oferta (inversão da Lei de Say)
- Logo, mudanças na taxa de câmbio e na taxa de juros nominais equivalem a mudanças nas taxas reais
- A eficácia das políticas depende de duas dimensões:
  1. **Regime de mobilidade de capitais**: perfeita / imperfeita / perfeita imobilidade
  2. **Regime cambial**: fixo / flutuante

---

## Análise de política econômica — método (3 passos)

1. Identificar qual curva se desloca com a política, e para qual lado (fiscal → desloca IS; monetária → desloca LM; contracionista → esquerda; expansionista → direita)
2. No novo ponto de equilíbrio IS-LM, verificar se a taxa de juros está acima ou abaixo do equilíbrio da BP
   - Acima → entrada de capital, apreciação da moeda doméstica
   - Abaixo → saída de capital, depreciação da moeda doméstica
3. Analisar a reação do BC, que depende do regime cambial
   - **Câmbio flexível**: BC não atua, deixa a moeda apreciar/depreciar → impacto no saldo comercial, afetando IS e BP
   - **Câmbio fixo**: BC compra reservas se há tendência de apreciação, ou vende reservas se há tendência de depreciação → impacto na oferta de moeda, afetando a LM

### Casos com perfeita mobilidade de capitais

| Regime cambial | Política fiscal | Política monetária |
|---|---|---|
| **Fixo** | **EFICAZ** — sem crowding out | **INEFICAZ** — LM se torna endógena |
| **Flutuante** | **INEFICAZ** — neutralizada pelo câmbio | **EFICAZ** — potencializada pelo câmbio |

- **Fiscal expansionista + câmbio fixo**: IS desloca à direita → juros sobem acima do equilíbrio BP → entrada de capital → para manter o câmbio fixo, o BC compra dólares → isso expande a LM endogenamente → novo equilíbrio com juros no mesmo patamar (sem crowding out) e renda maior → **máxima eficácia fiscal**
- **Monetária expansionista + câmbio fixo**: LM desloca à direita → juros caem abaixo do equilíbrio BP → saída de capital → BC vende reservas para segurar o câmbio → isso contrai a LM de volta ao ponto original → **política monetária totalmente ineficaz**, e o país ainda perde reservas internacionais
- **Fiscal expansionista + câmbio flutuante**: IS desloca à direita → juros sobem → entrada de capital, apreciação cambial → câmbio mais valorizado encarece exportações e barateia importações → déficit comercial → IS volta ao ponto de partida → **política fiscal ineficaz**
- **Monetária expansionista + câmbio flutuante**: LM desloca à direita → juros caem → fuga de capital, depreciação cambial → câmbio depreciado eleva EL → IS desloca à direita → **máxima eficácia monetária**, com efeito potencializado pelo canal cambial

### Trindade impossível

- Um país não pode ter simultaneamente: (i) câmbio fixo, (ii) livre mobilidade de capitais, (iii) autonomia da política monetária — só é possível ter 2 dos 3
- **Padrão-ouro**: câmbio fixo + livre mobilidade de capitais → sem autonomia da política monetária
- **Bretton Woods**: câmbio fixo + autonomia da política monetária (necessária para a reconstrução pós-Segunda Guerra) → sem livre mobilidade de capitais
- **Atualidade**: autonomia da política monetária + livre mobilidade de capitais → sem câmbio fixo (moedas flutuam entre si)

---

## Choques externos (taxa de juros externa, expectativa de depreciação ou risco-país)

- Distinção: políticas econômicas são escolhas do governo; choques são variáveis exógenas que o governo não controla (mudanças em i\*, Ê ou PR na paridade coberta)
- **Aumento de i\*, Ê ou PR em câmbio FIXO**:
  1. A curva BP do país sobe
  2. Para manter o câmbio fixo, o BC vende reservas em dólar (valorizando o real) → contrai a LM
  3. Juros domésticos sobem até o novo equilíbrio da BP, mas o **produto contrai**
- **Aumento de i\*, Ê ou PR em câmbio FLUTUANTE**:
  1. A curva BP do país sobe; juros domésticos ficam abaixo do novo equilíbrio → fuga de capital, depreciação cambial automática
  2. A depreciação eleva as exportações líquidas → IS desloca à direita
  3. Novo equilíbrio na mesma taxa de juros internacional, mas com **produto maior**
- Logo: o mesmo choque externo tem efeitos **opostos** sobre o produto dependendo do regime cambial — câmbio flutuante funciona como amortecedor do choque, câmbio fixo amplifica seu custo em termos de produto

---

## Exercícios (revisão em aula)

Considere o modelo IS-LM-BP para uma pequena economia aberta:

1. Em uma economia de câmbio fixo e perfeita mobilidade de capitais, uma política monetária contracionista provoca uma **redução** no estoque de reservas internacionais em poder do Banco Central. **ERRADO** — o efeito é o oposto: o aperto monetário eleva os juros domésticos acima do equilíbrio da BP, atraindo capital estrangeiro; para não deixar o câmbio apreciar, o BC precisa **comprar** reservas (aumentando o estoque), o que expande a LM de volta à posição original — a política monetária é neutralizada.
2. Se não há mobilidade de capitais, a função BP é uma linha vertical no plano (Y, i). **CERTO**
3. Em uma economia sem mobilidade de capitais, quanto maior o grau de abertura comercial, menor o impacto de políticas fiscais sobre o produto. **CERTO** — maior abertura comercial implica maior propensão marginal a importar, o que reduz o multiplicador keynesiano (mais vazamento da demanda para fora) — efeito válido independentemente do regime de mobilidade de capitais.
4. Em regime de câmbio fixo com perfeita mobilidade de capitais, a oferta de moeda é uma variável **endógena**. **CERTO** — o compromisso de manter o câmbio fixo obriga o BC a ajustar reservas (e, portanto, a base monetária) para acomodar os fluxos de capital; o BC perde o controle autônomo da oferta de moeda.
5. Em uma economia com câmbio fixo, quanto maior a mobilidade de capitais, maior o efeito de uma expansão fiscal sobre o produto. **CERTO** — mais mobilidade de capitais aumenta a resposta do influxo de capital à alta de juros, ampliando a expansão endógena da LM e reduzindo o crowding out.
