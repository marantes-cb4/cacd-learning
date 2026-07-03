## Materiais de referência (só local, nunca commitar)
PDFs e lista de temas ficam em: /Users/isabelamarantes/Desktop/CACD/


## ─── TAREFA 1: Notas de aula e materiais → Flash cards ───

**Gatilho:** quando eu pedir para processar uma matéria ou submatéria.

**Fontes a usar (em ordem):**
1. Minhas anotações em .md → /anotações/<materia>/ (no próprio repositório)
2. Materiais do professor em PDF → /Users/isabelamarantes/Desktop/CACD/Aulas/<materia>/Materiais/
3. Livros de referência em PDF → /Users/isabelamarantes/Desktop/CACD/

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
   - **Volume total por aula: máximo 15 cards, idealmente 10 — contando conteúdo + exercícios + TPs juntos**
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
6. Fazer commit e push com mensagem: 
   "notas+cards: <submateria> (<materia>) — <N> cards gerados"

**Sobre exercícios dos materiais do professor:**
- Buscar exercícios em todos os arquivos da aula: PDF principal, PDF de "Questões objetivas", PPT, etc.
- Reproduzir o enunciado de cada item **literalmente**, sem parafrasear
- Cada item (I, II, III, IV) vira um card individual
- Frente: enunciado exato do item
- Verso: resposta correta (C/E) + breve explicação do porquê
- O gabarito está no mesmo PDF de questões ou no PDF principal da rodada
- Usar critério de qualidade: incluir exercícios que testem conteúdo relevante ou pegadinhas reais; pular questões muito simples ou repetitivas em relação a cards de conteúdo já criados
- Questões de TPs oficiais presentes nos materiais: incluir sempre e literalmente, sem alteração

## ─── TAREFA 2: PDFs → Flash cards por conteúdo programático ───

**Gatilho:** quando eu pedir para processar um conteúdo do edital.

**O que fazer:**
1. Ler a lista de conteúdos em /Editais/Conteudo_Programatico.md do próprio repo
2. Identificar o conteúdo solicitado e a matéria à qual pertence
3. Buscar nos PDFs em /Users/isabelamarantes/Desktop/CACD/ os capítulos relevantes
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
Os PDFs estão organizados por matéria em subpastas dentro de /Users/isabelamarantes/Desktop/CACD/,
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

## Regras gerais
- Nunca commitar PDFs ou arquivos acima de 10MB
- Sempre fazer push após cada tarefa concluída
- Em caso de dúvida sobre o macro tema, perguntar antes de commitar
