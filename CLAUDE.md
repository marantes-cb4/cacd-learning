## Materiais de referência (só local, nunca commitar)
PDFs e lista de temas ficam em: /Users/isabelamarantes/Desktop/CACD/

## ─── TAREFA 1: Notas de aula → Flash cards ───

**Gatilho:** quando eu passar um arquivo .md com notas de aula.

**O que fazer:**
1. Ler o arquivo .md
2. Identificar o macro tema (Economia, Direito, História, etc.)
3. Gerar flash cards objetivos sobre os conceitos presentes nas notas
   - Frente: pergunta direta sobre o conceito
   - Verso: resposta concisa, sem rodeios
4. Exportar como .apkg cujo nome = título do documento .md
5. Salvar o .apkg em /anki/decks/
6. Mover o arquivo .md de notas para /notas/<macro-tema>/ (em minúsculas)
7. Fazer commit e push com a mensagem: "notas: <título do documento> + <N> cards gerados"

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
6. Salvar em /anki/decks/
7. Atualizar /Editais/Conteudo_Programatico.md adicionando ao lado de cada conteúdo processado:
   - Livro(s) utilizado(s)
   - Capítulo(s) onde o conteúdo foi encontrado
   - Status: ✅ coberto totalmente | ⚠️ coberto parcialmente | ❌ não encontrado nos PDFs
8. Fazer commit e push com a mensagem: "cards: <conteudo> (<materia>) — <N> cards"

## Sobre os materiais de referência
Os PDFs estão organizados por matéria em subpastas dentro de /Users/isabelamarantes/Desktop/CACD/,
mas um livro pode ser relevante para mais de uma matéria. Ao buscar conteúdo,
varrer todas as subpastas independentemente do conteúdo solicitado, e ao atualizar
o Conteudo_Programatico.md, registrar o livro fonte real mesmo que esteja em
uma pasta de matéria diferente.

## Padrão dos flash cards
- Sempre em português
- Objetivos e diretos — sem enrolação
- Máximo 2 linhas no verso
- Nunca criar cards sem identificar a fonte (livro + capítulo)
- Verificar duplicatas antes de criar novos cards para o mesmo tema

## Regras gerais
- Nunca commitar PDFs ou arquivos acima de 10MB
- Sempre fazer push após cada tarefa concluída
- Em caso de dúvida sobre o macro tema, perguntar antes de commitar
