## Materiais de referência (só local, nunca commitar)
PDFs e lista de temas ficam em: /Users/marantes.isabela/Desktop/CACD/


## ─── TAREFA 1: Notas de aula e materiais → Flash cards ───

**Gatilho:** quando eu pedir para processar uma matéria ou submatéria.

**Fontes a usar (em ordem):**
1. Minhas anotações em .md → /anotações/<materia>/ (no próprio repositório)
2. Materiais do professor em PDF → /Users/marantes.isabela/Desktop/CACD/Aulas/<materia>/Materiais/
3. Livros de referência em PDF → /Users/marantes.isabela/Desktop/CACD/

**O que fazer:**
1. Ler as anotações .md e os materiais .docx da submatéria solicitada
2. Identificar o macro tema e submatéria
3. Gerar flash cards no **estilo TPS** combinando as duas fontes:
   - **Formato padrão para conteúdo das anotações:**
     - Frente: afirmação sobre o tema (não pergunta direta), calibrada à dificuldade real do TPS CACD
     - Verso: CERTO ou ERRADO + explicação **completa** (3–5 linhas): o porquê, a regra geral, a exceção ou o erro típico da banca
   - **Dificuldade calibrada ao TPS real:**
     - **O conteúdo dos cards vem EXCLUSIVAMENTE das anotações .md e dos materiais do professor** — nunca das análises de TPS (`/Analise_Provas/`) nem de outras fontes externas
     - As análises de TPS servem apenas para calibrar o **estilo e a dificuldade** das afirmações (tipo de pegadinha, nível de detalhe), nunca como fonte de conteúdo
     - Priorizar afirmações que testem distinções sutis, exceções e nuances presentes nas próprias anotações
     - Incluir números precisos, prazos e exceções que constem explicitamente no material da aula
     - Evitar afirmações óbvias demais — se qualquer iniciante acertaria, o card não serve
     - Usar o padrão CEBRASPE: a afirmação parece verdadeira mas tem um detalhe errado, ou vice-versa
   - **Foco em tópicos abrangentes** — evitar cards granulares do tipo "liste as N características de X";
     preferir afirmações que testem mecanismos, relações causais, distinções críticas e exceções
   - **Volume total por aula: até 15 cards — contando conteúdo + exercícios + TPs juntos**
   - Exercícios e TPs podem substituir cards de conteúdo se cobrirem os conceitos mais importantes; usar só exercícios é válido se eles fizerem o trabalho de imitar o TPS e focar nos pontos críticos
   - Exercícios encontrados nos materiais do professor (PDFs, PPTs, questões objetivas) → se o exercício for bom (testa distinção relevante, pegadinha real ou conteúdo denso), criar um card reproduzindo o enunciado literalmente
     (frente: enunciado exato; verso: CERTO/ERRADO + explicação do porquê)
   - Questões de TPs oficiais que o professor incluir nos materiais de aula → reproduzir **sempre** e literalmente, sem alteração
4. Exportar como .apkg nomeado: <materia> - <tema_da_aula>.apkg
   onde <tema_da_aula> = nome do arquivo de anotações .md (sem a extensão)
   - Exemplo: se o arquivo é "normas_juridicas.md" → "Direito Interno - Normas Jurídicas.apkg"
   - Usar letras maiúsculas no início de cada palavra
   - Substituir underscores por espaços no nome final
   - O título interno do deck (usado no genanki.Deck) deve seguir o formato:
     REVIEW::<materia>::<titulo das anotações>
     Exemplo: REVIEW::Direito Interno::Normas Jurídicas
5. Salvar em /anki/decks/<materia>/
6. Atualizar /Planejamento/PROGRESS_CHECK.md: achar a(s) linha(s) do item do edital coberto(s) pela submatéria processada e marcar completo/parcial, citando o(s) arquivo(s) de anotação — ver regras completas na seção "Progress Check" deste arquivo
7. **Atualizar o app CACD Games (OBRIGATÓRIO a cada anotação nova ou alterada, de qualquer matéria)** — ver seção "App CACD Games". Checklist:
   a. Palavras cruzadas: acrescentar palavras/dicas da anotação nova ao pool do item e do subitem (e criar "parte 2" se sobrarem palavras) e rodar `gerar.py`
   b. Conexões: criar 1–2 jogos (4 grupos × 4 termos) por anotação nova em `scripts/app/conexoes/<materia>.json`
   c. Quem disse?: acrescentar cartas (autores, teorias, casos, súmulas, tratados, ministros) em `scripts/app/quem-disse/<materia>.json`
   d. Linha do tempo: criar/atualizar jogo se a anotação trouxer ≥ 5 datas, em `scripts/app/linha-do-tempo/<materia>.json`
   e. Rodar `python3 scripts/app/build_dados.py` (valida tudo e regenera `app/data/*.json`, incluindo o índice da aba Checagem) e resolver os ERROs; conferir os AVISOs
   f. Se faltar conteúdo para algum jogo, NÃO inventar: terminar com o aviso `⚠️ ATENÇÃO – CONTEÚDO FALTANTE`
8. Fazer commit e push (incluindo a anotação .md, o deck .apkg, o script gerador, o PROGRESS_CHECK.md atualizado e **todos os arquivos do app**: `scripts/app/**`, `app/data/*.json`, pools/grades/HTMLs das palavras cruzadas, `jogos/index.html` e `README.md`) com mensagem:
   "notas+cards: <submateria> (<materia>) — <N> cards gerados"
   (se a matéria for Direito Interno, incluir também o mapa mental atualizado — ver seção "Mapa mental de Direito Interno"; para qualquer matéria, incluir também o jogo de palavras cruzadas do item atualizado — ver seção "Palavras cruzadas por item do edital")

**Sobre exercícios dos materiais do professor:**
- Buscar exercícios em todos os arquivos da aula: PDF principal, PDF de "Questões objetivas", PPT, etc.
- Usar os exercícios como ponto de partida, não como obrigação de reprodução literal
- Se o exercício cobre bem um conceito importante e está no modelo TPS ideal → reproduzir literalmente (frente: enunciado exato; verso: C/E + explicação)
- Se o exercício cobre um tema importante mas está mal formulado, é simples demais ou não tem a pegadinha certa → **editar ou reescrever** o card no estilo TPS calibrado
- Se algum tema importante das anotações não foi coberto pelos exercícios → **criar cards próprios** para preencher a lacuna
- O gabarito está no mesmo PDF de questões ou no PDF principal da rodada
- Usar critério de qualidade: pular exercícios muito simples ou redundantes; nunca incluir só por completude
- Questões de TPs oficiais presentes nos materiais: incluir sempre e literalmente, sem alteração

## ─── TAREFA 2: PDFs → Flash cards por conteúdo programático ───

**Gatilho:** quando eu pedir para processar um conteúdo do edital.

**O que fazer:**
1. Ler a lista de conteúdos em /Editais/Conteudo_Programatico.md do próprio repo
2. Identificar o conteúdo solicitado e a matéria à qual pertence
3. Buscar nos PDFs em /Users/marantes.isabela/Desktop/CACD/ os capítulos relevantes
4. Gerar flash cards objetivos sobre aquele conteúdo
   - Frente: pergunta direta
   - Verso: resposta concisa com referência ao livro/capítulo fonte
5. Exportar como .apkg cujo nome = <conteudo>_<materia>
   - Exemplo: demanda_agregada_economia.apkg
6. Salvar em /anki/decks/<materia>/ (em minúsculas, sem acentos)
   - Exemplo: /anki/decks/economia/demanda_agregada_economia.apkg
   - Criar a pasta da matéria se não existir
7. Atualizar /Editais/Conteudo_Programatico.md adicionando ao lado de cada conteúdo processado:
   - Livro(s) utilizado(s)
   - Capítulo(s) onde o conteúdo foi encontrado
   - Status: ✅ coberto totalmente | ⚠️ coberto parcialmente | ❌ não encontrado nos PDFs
8. Fazer commit e push com a mensagem: "cards: <conteudo> (<materia>) — <N> cards"

## ─── TAREFA 3: Análise de provas anteriores ───

**Gatilho:** quando eu passar provas anteriores em PDF com gabarito oficial e extraoficial.

**O que fazer:**
1. Extrair todas as questões e gabaritos
2. Classificar cada questão por tópico do Conteudo_Programatico.md
3. Identificar padrões de formulação, termos recorrentes e pegadinhas típicas da banca
4. Comparar gabarito oficial vs. extraoficial e identificar padrões de anulação/alteração
5. Atualizar /Editais/Conteudo_Programatico.md com frequência de cobrança por tópico
6. Salvar relatório de análise em /Analise_Provas/<materia>_<anos>.md contendo:
   - Tópicos mais cobrados
   - Pegadinhas recorrentes da banca
   - Padrões de formulação de questões corretas vs. incorretas
   - Tópicos que nunca caíram
7. Gerar cards sobre os TÓPICOS abordados nas questões — nunca reproduzir
   as questões literalmente para preservar os TPs como simulados
8. Commit e push com mensagem: "analise: TP <ano> — <materia>"

**REGRA CRÍTICA:** Nunca criar cards com o enunciado exato ou
alternativas das questões. Os TPs antigos são reservados como simulados.

## ─── TAREFA 4: Análise de provas discursivas ───

**Gatilho:** quando eu passar provas discursivas em PDF com o Guia do Candidato.

**O que fazer:**
1. Extrair todas as questões discursivas e classificar por matéria e tópico
2. Ler as melhores respostas do Guia do Candidato como referência de qualidade —
   não como gabarito único, mas como exemplo do que a banca valoriza
3. Identificar padrões das melhores respostas:
   - Estrutura de argumento (como abrem, desenvolvem e concluem)
   - Conceitos e autores que aparecem nas respostas de referência
   - Nível de profundidade esperado por matéria
   - Conexões interdisciplinares que a banca valoriza
   - Vocabulário e terminologia técnica recorrente
4. Identificar padrões das perguntas discursivas:
   - Verbos de comando mais usados (discuta, analise, compare, explique)
   - Se a banca privilegia respostas cronológicas, temáticas ou argumentativas
   - Temas transversais que conectam mais de uma matéria
5. Salvar relatório em /Analise_Provas/discursivas/<materia>_<anos>.md contendo:
   - Padrões de pergunta e estrutura esperada de resposta
   - Autores e conceitos recorrentes nas melhores respostas
   - Tópicos mais cobrados nas discursivas
   - Conexões interdisciplinares identificadas
6. Atualizar /Editais/Conteudo_Programatico.md com frequência de cobrança
   nas discursivas por tópico
7. Gerar cards sobre os TÓPICOS e AUTORES abordados — nunca reproduzir
   as questões literalmente para preservar as provas como simulados
8. Commit e push com mensagem: "analise: discursivas <ano> — <materia>"

**REGRAS CRÍTICAS:**
- As respostas do Guia do Candidato são referência de qualidade, não gabarito único
- Nunca criar cards com enunciados exatos das questões
- Ao identificar padrões, sempre considerar que boas respostas podem ter
  abordagens diferentes das do Guia
  

## Sobre os materiais de referência
Os PDFs estão organizados por matéria em subpastas dentro de /Users/marantes.isabela/Desktop/CACD/,
mas um livro pode ser relevante para mais de uma matéria. Ao buscar conteúdo,
varrer todas as subpastas independentemente do conteúdo solicitado, e ao atualizar
o Conteudo_Programatico.md, registrar o livro fonte real mesmo que esteja em
uma pasta de matéria diferente.

## Padrão dos flash cards
- Sempre em português
- **Estilo TPS:** frente é uma afirmação (não pergunta); verso é CERTO/ERRADO + explicação completa
- **Dificuldade calibrada ao TPS CACD real (CEBRASPE):** afirmações com pegadinhas sutis, exceções, números precisos e distinções entre conceitos próximos — nunca afirmações óbvias
- **Tópicos abrangentes:** testar mecanismos, relações causais, distinções críticas e exceções — não listas de características
- **~10 cards de conteúdo por aula** (excluindo exercícios do professor, que são todos incluídos)
- **Verso: 3–5 linhas** — explicar o erro ou acerto, citar a regra geral, mencionar a exceção ou a armadilha típica da banca
- Nunca criar cards sem identificar a fonte (livro + capítulo ou "Anotações da aula")
- Verificar duplicatas antes de criar novos cards para o mesmo tema

## Estrutura de anotações no repositório
As anotações de aula ficam versionadas no próprio repo em:
/anotações/<materia>/<topico>.md

- Sempre commitar as anotações .md junto com os decks gerados a partir delas
- Quando receber novas anotações (arquivo .md ou conteúdo colado), salvar em /anotações/<materia>/ antes de processar
- Nunca deixar anotações apenas no desktop — o repo é a fonte de verdade

## Progress Check (/Planejamento/PROGRESS_CHECK.md)
Rastreia o progresso real de aulas/anotações próprias contra os itens oficiais do edital — uma tabela por matéria, uma linha por ponto do edital, com status (✅ completo / 🟡 parcial / em branco) e as anotações que cobrem cada ponto.

- Só existe tabela para matérias que já têm pasta em `/anotações/<materia>/`
- **Quando a primeira anotação de uma matéria nova for processada** (matéria ainda sem tabela nesta página), criar a tabela dela em `PROGRESS_CHECK.md` nesse mesmo commit, seguindo o mesmo formato das existentes (itens exatos do edital, extraídos de `Editais/Edital CACD 2026.pdf`)
- **Obrigatório a cada execução da TAREFA 1** (toda vez que eu processar uma aula/submatéria nova): atualizar a linha correspondente na tabela da matéria, marcando completo/parcial e citando o(s) arquivo(s) de anotação — nunca pular esse passo, mesmo que a mudança de status seja pequena (ver passo 6 da TAREFA 1)
- Status aqui reflete SOMENTE anotação de aula própria — nunca marcar completo/parcial com base apenas em deck gerado de livro de referência (isso fica só no `Conteudo_Programatico.md`)
- Commitar a atualização da tabela junto com a anotação/deck da tarefa que a gerou

## Mapa mental de Direito Interno (/mapas mentais/direito-interno.html)
Mapa mental interativo (HTML único, sem dependências) com os 14 itens do edital → leis → artigos/incisos. Os dados ficam inline no próprio HTML, no bloco `<script>` com chamadas `T.push(tema(...))` / `n(título, descrição, [filhos])`.
- **Todo conteúdo novo de Direito Interno** (TAREFA 1 de qualquer submatéria de Direito Interno, ou qualquer nova anotação da matéria) **deve também ser incorporado ao mapa mental** no mesmo commit: acrescentar/atualizar leis, artigos, incisos e pegadinhas no ramo do item do edital correspondente
- Atualizar o status do item (`"ok"` completo / `"part"` parcial) e a lista de anotações do ramo, de acordo com o `PROGRESS_CHECK.md`
- **Fontes permitidas: SOMENTE as anotações (`/anotações/Direito Interno/`) e os materiais do professor (`Aulas/Direito Interno/Materiais`: rodadas, textos de lei anexados, exercícios).** Nunca incluir no mapa conteúdo de conhecimento geral, de outras fontes ou de livros — se um ponto do edital ainda não tem material, o ramo fica enxuto (a lacuna é indicada pelo status "parcial")
- Commitar o mapa junto com a anotação, o deck e o `PROGRESS_CHECK.md`

## Palavras cruzadas por item do edital (/jogos/ e /scripts/palavras_cruzadas/)
Uma palavra cruzada (jogar no navegador + versão para imprimir) para cada item do edital que já tem anotações de aula — ✅ completo ou 🟡 parcial — em Direito Interno, Direito Internacional e Economia. Saída em `/jogos/<materia>/item-<N>-<slug>.html` e `...-impressao.html`; índice em `/jogos/index.html`; tabelas no `README.md` (seção entre os marcadores `palavras-cruzadas:inicio/fim`, gerada por script — nunca editar à mão).
- Fonte das dicas: **SOMENTE as anotações (`/anotações/<materia>/`) e os materiais do professor** (`Aulas/<materia>/Materiais`). Nunca conteúdo externo. A dica nunca pode conter a própria resposta
- Cada jogo vem de `scripts/palavras_cruzadas/pools/<chave>.json` (campos: `chave`, `materia`, `item`, `status` "completo"|"parcial", `titulo`, `descricao`, `notas`, `palavras` = lista de `[RESPOSTA, "dica", "arquivo de anotação"]`). Resposta em maiúsculas, sem acento, espaço ou hífen, com 3+ letras; dica como definição ou frase com `___`
- **Quando eu adicionar conteúdo novo (nova anotação ou material) sobre um item do edital, refazer também o jogo daquele item**: (1) achar o(s) item(ns) coberto(s) pela nova anotação no `PROGRESS_CHECK.md`; (2) abrir o JSON do item e acrescentar palavras e dicas tiradas do conteúdo novo (e corrigir as que ficaram desatualizadas); (3) rodar `python3 scripts/palavras_cruzadas/gerar.py <chave>` — refaz a grade, os dois HTMLs, o índice e o README (`--todas` refaz tudo); (4) se o item passou de parcial para completo no `PROGRESS_CHECK.md`, trocar `status` para "completo" e tirar "(parcial)" do `titulo` no JSON antes de gerar; (5) se o item ainda não tem JSON, criar um seguindo os existentes (chave `diNN-slug` ou `ecN-N-slug`) e rodar `gerar.py <chave>`
- **Subitens de Direito Interno:** além do jogo de cada item, há jogos extras por cláusula/subitem do edital (pools `diNN-S-slug.json`, `item` "N.S", ex.: `di03-2-primado-da-constituicao`, 17 jogos no total; itens 1, 2, 6, 7, 8, 11 e 13 e as cláusulas sem anotação — elementos do Estado e processo administrativo — não têm subitem). **Quando entrar conteúdo novo, atualizar também o pool do subitem correspondente** (mesmas regras: só anotações e materiais do professor, dica sem a resposta) e rodar `gerar.py <chave>`; commitar JSON, grade, HTMLs, índice e README junto
- Commitar junto com a anotação, o deck e o `PROGRESS_CHECK.md`: JSON do pool, `grades/<chave>.json`, os HTMLs em `/jogos/`, o índice e o `README.md`

## Regras gerais
- Nunca commitar PDFs ou arquivos acima de 10MB
- Sempre fazer push após cada tarefa concluída
- Em caso de dúvida sobre o macro tema, perguntar antes de commitar

## App CACD Games (/app/) — PWA de jogos de estudo
App estático instalável (celular e navegador), publicado pelo GitHub Pages em https://marantes-cb4.github.io/cacd-learning/app/ (Settings → Pages → Deploy from branch → `main` / root). Sem servidor: o progresso (streak, jogos concluídos) fica no `localStorage` de cada pessoa; há exportar/importar código na aba Progresso.
- **Arquivos:** `app/index.html`, `app/app.js`, `app/style.css`, `app/sw.js` (service worker: rede primeiro, cache offline), `app/manifest.webmanifest`, `app/icons/` (gerados por `scripts/app/icones.py`) e `app/data/jogos.json`
- **Dados:** `app/data/jogos.json` é GERADO por `scripts/app/build_dados.py` a partir dos pools e grades das palavras cruzadas — nunca editar à mão. `gerar.py` já chama o build ao final, então **refazer um jogo de palavras cruzadas atualiza o app**; commitar `app/data/jogos.json` junto
- **Paleta e telas:** laranja, roxo e azul (tokens em `app/style.css`). Home = jogo do dia (tipo rotativo entre os jogos) + botões dos jogos; as matérias/dropdowns só aparecem ao tocar no jogo. Abas: Jogos, Checagem e Progresso
- **Checagem (busca nas anotações):** `app/data/anotacoes.json` é GERADO por `build_dados.py` a partir de `anotações/**/*.md` (seções por título; busca por palavras com AND, sem acento). Ao adicionar anotação nova, rodar o build e commitar o JSON. **Materiais do professor (PDFs/PPTs) NÃO entram no índice**: o repositório e o app são públicos e os materiais são de terceiros; a Checagem cobre só as anotações próprias (decisão do usuário: sem materiais do professor, nem importação privada). Cada resultado tem o botão “Ver anotação completa de <arquivo>”, que abre a anotação inteira (rota `#/nota?m=&a=&q=&s=`) já rolada até a seção encontrada
- **Regra de manutenção (reforço):** toda anotação nova ou editada em `anotações/<materia>/` exige, no MESMO commit, a atualização do app (palavras cruzadas, Conexões, Quem disse?, Linha do tempo, índice da Checagem). Nunca commitar anotação sem rodar `scripts/app/build_dados.py`. Cobertura-alvo: cada anotação deve aparecer em pelo menos 1 Conexões, e em Quem disse?/Linha do tempo sempre que houver autores, casos, tratados, súmulas ou datas
- **Palavras cruzadas "parte 2":** pools `<chave>-parte-2` reúnem as palavras que não couberam na grade do item (o gerador só encaixa ~25 por grade); ao acrescentar palavras a um item, refazer também a parte 2 (recalcular as palavras não colocadas) e rodar `gerar.py`
- **Fontes dos jogos: SOMENTE anotações e materiais do professor.** Nunca conteúdo externo
- **Conexões (já no ar):** grade de 16 termos em 4 grupos de 4 (4 erros permitidos). Fonte editável em `scripts/app/conexoes/<materia>.json` (lista de jogos: `id`, `materia`, `item`, `titulo`, `grupos` = 4 × {`tema`, `termos` (4), `fonte` = arquivo .md em `anotações/<materia>/`}); `build_dados.py` valida (4×4, termos únicos, fonte existente, termo presente nas anotações da matéria) e gera `app/data/conexoes.json`. Termo que só aparece no material do professor gera AVISO (conferir no material). **Ao processar uma aula (TAREFA 1), criar/atualizar 1 Conexões do item quando o conteúdo tiver 4 categorias claras com 4 termos cada**; senão, aviso de conteúdo faltante. Rodar `python3 scripts/app/build_dados.py` e commitar `app/data/*.json`
- **Quem disse? (já no ar):** quiz de múltipla escolha (4 opções, as 3 erradas vêm das outras respostas do baralho): enunciado → autor/pessoa. Fonte editável em `scripts/app/quem-disse/<materia>.json` (lista de baralhos: `id`, `materia`, `titulo`, `cartas` ≥ 5 × {`q`, `r`, `chave` (sobrenome que deve estar na anotação), `fonte` (.md), `exp`}). Só entram autores e fatos que constam nas anotações/materiais; **nenhum primeiro nome ou data de fora** (usar o nome como aparece nas anotações). O enunciado não pode conter a resposta (o `build_dados.py` confere). Ao processar uma aula que cite autores, teorias ou ministros/figuras, acrescentar cartas ao baralho da matéria
- **Linha do tempo (já no ar):** ordenar de 5 a 8 eventos do mais antigo ao mais recente (setas ▲▼, "Verificar" marca em verde/vermelho; ao acertar mostra as datas e as fontes). Fonte editável em `scripts/app/linha-do-tempo/<materia>.json` (lista de jogos: `id`, `materia`, `titulo`, `eventos` ≥ 5 × {`ano`, `d` (data exibida), `t` (texto SEM a data), `chave`, `fonte` (.md)}), em ordem cronológica estrita e sem anos repetidos. O `build_dados.py` confere ano e chave na anotação citada e rejeita texto que entregue a data. **Só datas que constem nas anotações/materiais**: nada de data de memória ou de fora. Ao processar uma aula com datas (História do Brasil, Política Internacional, Economia, DIP), criar/atualizar o jogo; se faltarem datas, aviso de conteúdo faltante
- **Aviso obrigatório:** se a aula não tiver conteúdo suficiente para um jogo (ex.: poucas datas para a Linha do tempo, sem autores para Quem disse), NÃO inventar nem buscar fora: terminar a tarefa com um aviso bem visível, no formato `⚠️ ATENÇÃO – CONTEÚDO FALTANTE: <aula> → <jogo>: preciso de <o que falta>`, para eu pesquisar e mandar o conteúdo, que entra no jogo e na anotação juntos
