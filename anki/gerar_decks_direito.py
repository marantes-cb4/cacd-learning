#!/usr/bin/env python3
"""Gera todos os decks de Anki para Direito do CACD."""
import genanki, random, os

os.makedirs("/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/direito", exist_ok=True)

BASE = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/direito"

def make_deck(deck_title, file_name, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        'CACD Direito',
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
    genanki.Package(deck).write_to_file(f"{BASE}/{file_name}")
    print(f"✅ {file_name} — {len(cards)} cards")


# ══════════════════════════════════════════════════════════════
# DIREITO INTERNO
# ══════════════════════════════════════════════════════════════

# ─── 1. NORMAS JURÍDICAS E PERSONALIDADE JURÍDICA ────────────
make_deck(
    "CACD :: Direito :: Normas Jurídicas e Personalidade Jurídica",
    "normas_juridicas_personalidade_direito.apkg",
    [
        ("Quais são as características básicas das normas jurídicas?",
         "Imperatividade, coercibilidade, abstratividade, bilateralidade e generalidade. [Col. Diplomata Dir. Interno, Cap. 1]"),
        ("O que é a imperatividade de uma norma jurídica?",
         "A norma impõe conduta obrigatória, independentemente da vontade do destinatário — distingue-se da mera sugestão ou recomendação. [Col. Diplomata Dir. Interno, Cap. 1.2.1]"),
        ("O que é coercibilidade?",
         "Possibilidade de o Estado impor o cumprimento da norma pela força; a sanção é o instrumento coercitivo. [Col. Diplomata Dir. Interno, Cap. 1.2.2]"),
        ("O que é validade de uma norma jurídica?",
         "Pertinência da norma ao ordenamento; pode ser material (compatibilidade de conteúdo com norma superior) ou formal (obediência ao processo de criação). [Col. Diplomata Dir. Interno, Cap. 1.3.1]"),
        ("O que é vigência de uma norma?",
         "Qualidade da norma que está apta a produzir efeitos jurídicos por ter sido publicada e não ter sido revogada. [Col. Diplomata Dir. Interno, Cap. 1.3.2]"),
        ("O que é eficácia jurídica de uma norma?",
         "Aptidão para produzir os efeitos jurídicos que lhe são próprios; distingue-se da eficácia social (obediência real pelos destinatários). [Col. Diplomata Dir. Interno, Cap. 1.3.3]"),
        ("Qual é a hierarquia das normas jurídicas brasileiras?",
         "CF/Emendas &gt; Tratados de DH (§ 3º art. 5º) = EC / Tratados DH não aprovados por QE = lei ordinária &gt; leis ordinárias &gt; atos normativos infralegais. [Col. Diplomata Dir. Interno, Cap. 1.4]"),
        ("O que é personalidade jurídica?",
         "Aptidão para ser titular de direitos e obrigações; adquirida pela pessoa natural com o nascimento com vida (art. 2º CC). [Col. Diplomata Dir. Interno, Cap. 3.4.1]"),
        ("Qual a teoria adotada pelo CC/2002 sobre o nascituro?",
         "Teoria da personalidade condicional: o CC 'põe a salvo' direitos do nascituro, mas a personalidade plena só se adquire com o nascimento com vida. [Col. Diplomata Dir. Interno, Cap. 3.4.2.1]"),
        ("O que é um fato jurídico em sentido estrito?",
         "Evento natural com repercussão jurídica, independente da vontade humana (ex.: nascimento, morte, decurso de prazo). [Col. Diplomata Dir. Interno, Cap. 3.2.1]"),
        ("O que é um negócio jurídico?",
         "Manifestação de vontade das partes destinada a produzir efeitos jurídicos desejados (ex.: contrato, testamento). Planos: existência, validade e eficácia. [Col. Diplomata Dir. Interno, Cap. 3.3]"),
        ("Quais são os defeitos do negócio jurídico?",
         "Erro, dolo, coação, estado de perigo, lesão e fraude contra credores — podem gerar anulabilidade; simulação gera nulidade absoluta. [Col. Diplomata Dir. Interno, Cap. 3.3.4]"),
    ]
)

# ─── 2. CONSTITUIÇÃO E CONTROLE DE CONSTITUCIONALIDADE ───────
make_deck(
    "CACD :: Direito :: Constituição e Controle de Constitucionalidade",
    "constituicao_controle_constitucionalidade_direito.apkg",
    [
        ("O que é uma Constituição rígida?",
         "Aquela que exige processo mais solene e difícil para sua alteração do que para leis ordinárias; a CF/88 é rígida (art. 60). [Col. Diplomata Dir. Interno, Cap. 2.2.6]"),
        ("O que é o primado da Constituição?",
         "A CF é a norma suprema do ordenamento; todas as demais devem com ela compatibilidade, sob pena de inconstitucionalidade (Kelsen). [Col. Diplomata Dir. Interno, Cap. 2.3]"),
        ("Qual a diferença entre controle difuso e concentrado de constitucionalidade?",
         "Difuso: qualquer juiz, caso concreto, efeito inter partes. Concentrado: STF, via abstrata (ADI, ADC, ADPF), efeito erga omnes e vinculante. [Col. Diplomata Dir. Interno, Cap. 2.4.5.3]"),
        ("O que é a cláusula de reserva de plenário (full bench)?",
         "Art. 97 CF: declaração de inconstitucionalidade de lei ou ato normativo exige maioria absoluta do plenário ou do órgão especial do tribunal. [Col. Diplomata Dir. Interno, Cap. 2.4.6.5]"),
        ("O que é a ADI (Ação Direta de Inconstitucionalidade)?",
         "Ação de controle concentrado no STF para declarar inconstitucionalidade de lei ou ato normativo federal ou estadual, com efeito erga omnes e vinculante. [Col. Diplomata Dir. Interno, Cap. 2.4.8]"),
        ("O que é a ADC?",
         "Ação Declaratória de Constitucionalidade: busca afirmar a constitucionalidade de lei federal perante o STF, com efeito vinculante e erga omnes. [Col. Diplomata Dir. Interno, Cap. 2.4.9]"),
        ("O que é a ADPF?",
         "Arguição de Descumprimento de Preceito Fundamental: ação subsidiária no STF para proteger preceito fundamental da CF contra ato do poder público. [Col. Diplomata Dir. Interno, Cap. 2.4.11]"),
        ("O que é uma Emenda Constitucional e quais são seus limites?",
         "Alteração formal da CF por quórum de 3/5 de ambas as casas em dois turnos; vedado emendar cláusulas pétreas (art. 60, §4º): forma federativa, voto direto, separação de poderes, direitos fundamentais. [Const. Descomplicado, Cap. 1]"),
        ("O que são cláusulas pétreas?",
         "Núcleo imutável da CF (art. 60, §4º): forma federativa, voto direto/secreto/universal/periódico, separação de poderes e direitos e garantias individuais. [Const. Descomplicado, Cap. 1]"),
        ("O que é a teoria da recepção?",
         "Com a nova Constituição, a lei anterior compatível com ela é recepcionada (mantida em vigor); a incompatível é revogada — não se fala em inconstitucionalidade superveniente. [Const. Descomplicado, Cap. 1]"),
        ("Quais são as classificações das constituições quanto à origem?",
         "Promulgadas (democráticas): votadas por assembleia constituinte. Outorgadas: impostas unilateralmente pelo governante. Ex. CF/88: promulgada. [Col. Diplomata Dir. Interno, Cap. 2.2.3]"),
        ("O que é inconstitucionalidade por omissão?",
         "Ausência de norma regulamentadora que torne inviável o exercício de direito constitucional; remédios: ADO (controle abstrato) e Mandado de Injunção (controle concreto). [Col. Diplomata Dir. Interno, Cap. 2.4.10]"),
    ]
)

# ─── 3. ESTADO, ORGANIZAÇÃO E PODERES ────────────────────────
make_deck(
    "CACD :: Direito :: Estado, Organização e Poderes",
    "estado_organizacao_poderes_direito.apkg",
    [
        ("Quais são os elementos constitutivos do Estado?",
         "Povo (elemento humano), Território (base física), Governo soberano (poder político) e, para alguns, Finalidade (bem comum). [Col. Diplomata Dir. Interno, Cap. 5.1]"),
        ("Quais são as formas de Estado quanto à estrutura interna?",
         "Estado Unitário (poder centralizado) e Estado Federal (divisão constitucional de competências entre entes). O Brasil é República Federativa. [Col. Diplomata Dir. Interno, Cap. 5.1]"),
        ("O que são sistemas de governo?",
         "Presidencialismo: chefe de Estado e governo são o mesmo (Presidente); Parlamentarismo: chefe do governo (Premier) depende de maioria parlamentar. Brasil: presidencialismo. [Col. Diplomata Dir. Interno, Cap. 5.1]"),
        ("O que é Estado Democrático de Direito (art. 1º CF/88)?",
         "Estado que submete o poder ao Direito e à soberania popular: legalidade, separação de poderes, direitos fundamentais e democracia participativa/representativa. [Const. Descomplicado, Cap. 1]"),
        ("Quais são os fundamentos da República Federativa do Brasil (art. 1º CF)?",
         "Soberania, Cidadania, Dignidade da pessoa humana, Valores sociais do trabalho e da livre iniciativa, Pluralismo político. Mnemônico: SCDVP. [Const. Descomplicado, Cap. 1]"),
        ("Quais são os objetivos fundamentais da República (art. 3º CF)?",
         "Construir sociedade livre/justa/solidária; garantir desenvolvimento nacional; erradicar pobreza; promover o bem de todos sem discriminação. [Const. Descomplicado, Cap. 1]"),
        ("Como se divide a competência legislativa entre os entes federativos?",
         "Privativa da União (art. 22), Concorrente União+Estados+DF (art. 24), Reservada aos Estados (art. 25 §1º), Municipal (art. 30). [Col. Diplomata Dir. Interno, Cap. 5.3]"),
        ("Quais são as funções típicas dos três poderes?",
         "Legislativo: elaborar leis. Executivo: administrar, executar políticas públicas. Judiciário: julgar, aplicar o direito ao caso concreto. [Const. Descomplicado, Cap. 1]"),
        ("O que é separação de poderes e qual seu fundamento?",
         "Divisão das funções estatais em órgãos distintos com independência e harmonia; impede concentração de poder e garante liberdades (Montesquieu, art. 2º CF). [Const. Descomplicado, Cap. 1]"),
        ("Quais são as competências do STF?",
         "Guardião da CF: controle concentrado (ADI, ADC, ADPF), julgamento de crimes de altas autoridades (CR), recurso extraordinário; composição de 11 ministros. [Const. Descomplicado, Cap. 1]"),
        ("O que é federalismo cooperativo?",
         "Modelo em que União, Estados e Municípios atuam conjuntamente em áreas de competência concorrente e comum, em lugar de atuação isolada. [Col. Diplomata Dir. Interno, Cap. 5.2]"),
    ]
)

# ─── 4. PROCESSO LEGISLATIVO ─────────────────────────────────
make_deck(
    "CACD :: Direito :: Processo Legislativo Brasileiro",
    "processo_legislativo_direito.apkg",
    [
        ("Quais são as espécies normativas do processo legislativo (art. 59 CF)?",
         "Emendas à CF, leis complementares, leis ordinárias, leis delegadas, medidas provisórias, decretos legislativos e resoluções. [Col. Diplomata Dir. Interno, Cap. 4.6]"),
        ("Qual o quórum para aprovação de lei complementar?",
         "Maioria absoluta (50% + 1 dos membros de cada casa), enquanto lei ordinária exige apenas maioria simples (dos presentes). [Col. Diplomata Dir. Interno, Cap. 4.9]"),
        ("O que é medida provisória (art. 62 CF)?",
         "Ato normativo com força de lei editado pelo Presidente em caso de relevância e urgência; vigência de 60+60 dias; aprovada ou rejeitada pelo CN. [Col. Diplomata Dir. Interno, Cap. 4.11]"),
        ("Quais matérias são vedadas para Medida Provisória?",
         "Nacionalidade, cidadania, direitos políticos, partidos, direito eleitoral, penal/processual, organização do Judiciário/MP, planos plurianuais e legislação de 60 dias antes de eleição. [Col. Diplomata Dir. Interno, Cap. 4.11.2]"),
        ("O que é lei delegada?",
         "Lei elaborada pelo Presidente mediante delegação do Congresso (resolução); vedada para atos de competência exclusiva do CN, legislação sobre matérias de LC e algumas outras. [Col. Diplomata Dir. Interno, Cap. 4.10]"),
        ("Quais são as fases do processo legislativo ordinário?",
         "Fase introdutória (iniciativa), constitutiva (deliberação nas casas + sanção/veto) e complementar (promulgação e publicação). [Col. Diplomata Dir. Interno, Cap. 4.3]"),
        ("O que é iniciativa popular de lei?",
         "Art. 61 §2º CF: projeto pode ser apresentado por 1% do eleitorado nacional distribuído por pelo menos 5 estados, com mínimo de 0,3% em cada. [Col. Diplomata Dir. Interno, Cap. 4.3.2]"),
        ("O que é veto presidencial e como é superado?",
         "Presidente veta o projeto (total ou parcialmente) por inconstitucionalidade ou contrariedade ao interesse público; veto é superado por maioria absoluta do CN em sessão conjunta. [Col. Diplomata Dir. Interno, Cap. 4.3.7.4]"),
        ("O que são decretos legislativos?",
         "Espécie normativa de competência exclusiva do CN, sem sanção presidencial; usados para aprovação de tratados internacionais e julgamento das contas presidenciais. [Col. Diplomata Dir. Interno, Cap. 4.12]"),
        ("O que é a Emenda Constitucional e qual seu quórum de aprovação?",
         "Alteração formal da CF aprovada por 3/5 dos membros de cada casa em dois turnos de votação; matérias pétreas são insuscetíveis de emenda. [Col. Diplomata Dir. Interno, Cap. 4.7]"),
    ]
)

# ─── 5. DIREITOS E GARANTIAS FUNDAMENTAIS ────────────────────
make_deck(
    "CACD :: Direito :: Direitos e Garantias Fundamentais",
    "direitos_garantias_fundamentais_direito.apkg",
    [
        ("O que são direitos fundamentais?",
         "Direitos positivados na CF que protegem a dignidade da pessoa humana; têm aplicabilidade imediata (art. 5º §1º) e não podem ser suprimidos por EC (cláusula pétrea). [Const. Descomplicado, Cap. 1]"),
        ("O que são gerações/dimensões de direitos fundamentais?",
         "1ª (liberdades negativas), 2ª (direitos sociais, econômicos, culturais — obrigações positivas do Estado), 3ª (direitos difusos: meio ambiente, paz), 4ª (democracia, informação). [Const. Descomplicado, Cap. 1]"),
        ("Quais são os remédios constitucionais?",
         "Habeas corpus (liberdade de locomoção), Mandado de segurança (direito líquido e certo), Habeas data (dados pessoais), Mandado de injunção (omissão normativa), Ação popular. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio da dignidade da pessoa humana?",
         "Fundamento da República (art. 1º, III CF); núcleo axiológico que orienta todo o ordenamento: proibição de tratamento degradante, tutela da autonomia individual. [Const. Descomplicado, Cap. 1]"),
        ("O que são direitos sociais (art. 6º CF)?",
         "Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência social, proteção à maternidade/infância e assistência social. [Const. Descomplicado, Cap. 1]"),
        ("O que garante o habeas corpus?",
         "Liberdade de locomoção ameaçada ou violada por ilegalidade ou abuso de poder; pode ser preventivo (salvo-conduto) ou repressivo (liberdade). [Const. Descomplicado, Cap. 1]"),
        ("O que é o mandado de segurança?",
         "Remédio que protege direito líquido e certo (comprovado de plano) não amparado por HC ou HD, violado por ato de autoridade pública ou agente de pessoa jurídica no exercício de atribuições públicas. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio da proporcionalidade no contexto dos direitos fundamentais?",
         "Restrições a direitos fundamentais devem ser adequadas (meio apto), necessárias (menos gravosa) e proporcionais em sentido estrito (vantagem x sacrifício). [Const. Descomplicado, Cap. 1]"),
        ("O que são direitos e garantias individuais (art. 5º CF)?",
         "Direitos: posições subjetivas (vida, liberdade, igualdade, segurança, propriedade). Garantias: instrumentos de proteção desses direitos (HC, MS, ação popular etc.). [Const. Descomplicado, Cap. 1]"),
        ("Qual o tratamento dos tratados internacionais de direitos humanos na CF/88?",
         "Aprovados em cada casa por 3/5 em 2 turnos: equivalem a EC (§3º art. 5º). Demais tratados de DH: supralegal (acima da lei, abaixo da CF) — STF, RE 466.343. [Const. Descomplicado, Cap. 1]"),
        ("O que é a eficácia horizontal dos direitos fundamentais?",
         "Aplicação dos direitos fundamentais nas relações entre particulares (não apenas Estado x indivíduo); reconhecida pelo STF. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio da igualdade (art. 5º caput e I CF)?",
         "Proibição de discriminações arbitrárias: igualdade formal (perante a lei) e igualdade material (tratar desiguais desigualmente na medida de suas desigualdades). [Const. Descomplicado, Cap. 1]"),
    ]
)

# ─── 6. ADMINISTRAÇÃO PÚBLICA, LICITAÇÕES E RESPONSABILIDADE CIVIL ──
make_deck(
    "CACD :: Direito :: Administração Pública, Licitações e Responsabilidade Civil do Estado",
    "administracao_publica_atos_direito.apkg",
    [
        ("Quais são os princípios constitucionais da Administração Pública (art. 37 CF)?",
         "LIMPE: Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência. [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("O que é o princípio da legalidade na Administração Pública?",
         "O administrador só pode fazer o que a lei expressamente autoriza (vinculação positiva à lei); difere do particular, que pode fazer tudo o que a lei não proíbe. [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("O que são atos administrativos?",
         "Manifestações unilaterais da Administração que criam, modificam ou extinguem direitos e obrigações; atributos: presunção de legitimidade, autoexecutoriedade e imperatividade. [Col. Diplomata Dir. Interno, Cap. 6.3]"),
        ("Qual é a teoria da responsabilidade civil objetiva do Estado (art. 37 §6º CF)?",
         "Risco administrativo: o Estado responde por danos causados por seus agentes independentemente de culpa; o lesado prova apenas dano, nexo causal e ação/omissão do agente. [Col. Diplomata Dir. Interno, Cap. 7.2]"),
        ("Quais são as causas excludentes de responsabilidade objetiva do Estado?",
         "Culpa exclusiva da vítima, culpa exclusiva de terceiro e caso fortuito/força maior — rompem o nexo de causalidade. [Col. Diplomata Dir. Interno, Cap. 7.3]"),
        ("Quando se aplica responsabilidade subjetiva do Estado?",
         "Em danos causados por omissão estatal: aplica-se a teoria da culpa administrativa (falta do serviço) — o lesado deve provar culpa ou dolo do agente público. [Col. Diplomata Dir. Interno, Cap. 7.4]"),
        ("O que é licitação pública?",
         "Procedimento administrativo obrigatório para contratações com o poder público que garante igualdade de oportunidade e a proposta mais vantajosa (art. 37 XXI CF; Lei 14.133/21). [Col. Diplomata Dir. Interno, Cap. 6]"),
        ("Quais são as modalidades de licitação (Lei 14.133/2021)?",
         "Pregão, concorrência, concurso, leilão e diálogo competitivo. A Lei 14.133/21 revogou convite, tomada de preços e concorrência da antiga Lei 8.666/93. [Col. Diplomata Dir. Interno, Cap. 6]"),
        ("O que é o poder discricionário da Administração?",
         "Margem de liberdade que a lei confere ao administrador para escolher a melhor solução em termos de oportunidade e conveniência, dentro dos limites legais. [Col. Diplomata Dir. Interno, Cap. 6.3]"),
        ("O que é ato administrativo vinculado?",
         "Ato cujos requisitos são integralmente fixados em lei, sem margem de escolha para o administrador — que é obrigado a praticá-lo quando presentes os pressupostos legais. [Col. Diplomata Dir. Interno, Cap. 6.3]"),
        ("O que é o controle de legalidade dos atos administrativos?",
         "Revisão pelo Judiciário (controle externo) e pela própria Administração (autotutela — anulação de atos ilegais e revogação de inconvenientes). [Col. Diplomata Dir. Interno, Cap. 6.3]"),
    ]
)

# ─── 7. SERVIDOR PÚBLICO E LEI 11.440/2006 ───────────────────
make_deck(
    "CACD :: Direito :: Servidor Público e Regime do Serviço Exterior (Lei 11.440/2006)",
    "servidor_publico_lei_11440_direito.apkg",
    [
        ("Quais são os deveres constitucionais do servidor público?",
         "Legalidade, probidade, eficiência, publicidade (art. 37 CF); Lei 8.112/90: dedicação, lealdade, urbanidade, sigilo, pontualidade, cumprimento das ordens. [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("O que é improbidade administrativa?",
         "Ato de agente público que importa enriquecimento ilícito, causa dano ao erário ou viola princípios da Adm Pública (Lei 8.429/92, alterada pela Lei 14.230/21). [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("Quais são as sanções por improbidade administrativa (Lei 8.429/92)?",
         "Suspensão dos direitos políticos, perda da função pública, indisponibilidade de bens, ressarcimento ao erário, multa e proibição de contratar com o poder público. [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("O que é o processo administrativo disciplinar (PAD)?",
         "Procedimento formal para apurar infrações funcionais de servidor; assegura contraditório e ampla defesa; pode resultar em demissão, suspensão, advertência etc. [Col. Diplomata Dir. Interno, Cap. 6.2]"),
        ("O que regula a Lei 11.440/2006?",
         "Regime Jurídico dos Servidores do Serviço Exterior Brasileiro — estrutura de carreira, atribuições, direitos e deveres dos diplomatas e funcionários do MRE. [Col. Diplomata Dir. Interno — Lei 11.440/2006]"),
        ("Quais são as categorias do Serviço Exterior Brasileiro (Lei 11.440)?",
         "Carreira de Diplomata (Embaixador, Ministro, Conselheiro, Primeiro Secretário, Segundo Secretário, Terceiro Secretário) e cargos de apoio (Oficial de Chancelaria, Assistente de Chancelaria). [Lei 11.440/2006]"),
        ("Quais são os princípios que regem o Serviço Exterior (Lei 11.440)?",
         "Hierarquia, disciplina, lealdade institucional, discrição, sigilo e disponibilidade permanente para o serviço — inclusive em horários especiais no exterior. [Lei 11.440/2006]"),
        ("O que é a disponibilidade do servidor público?",
         "Situação de servidor estável cujo cargo é extinto ou declarado desnecessário; recebe remuneração proporcional e aguarda novo aproveitamento. [Const. Descomplicado, Cap. 1]"),
        ("O que é a estabilidade do servidor público?",
         "Após 3 anos de efetivo exercício e avaliação periódica de desempenho, o servidor só perde o cargo por sentença judicial transitada em julgado, PAD ou excesso de despesa (art. 41 CF). [Const. Descomplicado, Cap. 1]"),
        ("Quais são as hipóteses de perda do cargo estável?",
         "Sentença judicial transitada em julgado, PAD com ampla defesa, avaliação periódica de desempenho insuficiente e excesso de despesa com pessoal (LRF). [Const. Descomplicado, Cap. 1]"),
        ("O que é o regime de dedicação exclusiva no Serviço Exterior?",
         "O servidor do Serviço Exterior não pode exercer atividade privada remunerada; é proibida a acumulação de cargos/empregos, salvo exceções constitucionais (art. 37 XVI CF). [Lei 11.440/2006]"),
    ]
)

# ─── 8. FINANÇAS PÚBLICAS E NORMAS ORÇAMENTÁRIAS ─────────────
make_deck(
    "CACD :: Direito :: Finanças Públicas e Normas Orçamentárias",
    "financas_publicas_orcamento_direito.apkg",
    [
        ("Quais são as três leis orçamentárias previstas na CF/88?",
         "PPA (Plano Plurianual — 4 anos), LDO (Lei de Diretrizes Orçamentárias — metas e prioridades anuais) e LOA (Lei Orçamentária Anual — orçamento de execução). [Const. Descomplicado, Cap. 1]"),
        ("O que é o Plano Plurianual (PPA)?",
         "Lei que estabelece diretrizes, objetivos e metas da Administração para 4 anos; vigora do 2º ano de um mandato ao 1º ano do mandato seguinte (art. 165, I CF). [Const. Descomplicado, Cap. 1]"),
        ("O que é a Lei de Responsabilidade Fiscal (LC 101/2000)?",
         "Estabelece normas de finanças públicas voltadas para responsabilidade na gestão fiscal: metas de resultado, controle de despesas de pessoal, endividamento e transparência. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio da anualidade orçamentária?",
         "O orçamento é elaborado e aprovado para um exercício financeiro (ano calendário); vigência da LOA de 1º de janeiro a 31 de dezembro. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio do equilíbrio orçamentário?",
         "Receitas previstas devem ser iguais às despesas fixadas; a LRF exige metas de resultado primário para controlar déficits. [Const. Descomplicado, Cap. 1]"),
        ("O que são créditos adicionais no orçamento?",
         "Autorizações de despesa não computadas ou insuficientemente dotadas na LOA: suplementares (reforçam dotação), especiais (novas finalidades) e extraordinários (urgência). [Const. Descomplicado, Cap. 1]"),
        ("O que é o controle externo das finanças públicas?",
         "Exercido pelo Congresso Nacional com auxílio do TCU (art. 70 CF); inclui fiscalização contábil, financeira, operacional, patrimonial e orçamentária. [Const. Descomplicado, Cap. 1]"),
        ("O que é a DRU (Desvinculação de Receitas da União)?",
         "Mecanismo constitucional que permite à União utilizar livremente parte das receitas vinculadas a fundos, despesas e órgãos federais — instrumento de flexibilidade fiscal. [Const. Descomplicado, Cap. 1]"),
    ]
)


# ══════════════════════════════════════════════════════════════
# DIREITO INTERNACIONAL PÚBLICO (DIP) ⭐
# ══════════════════════════════════════════════════════════════

# ─── 9. FONTES DO DIP E TRATADOS ─────────────────────────────
make_deck(
    "CACD :: Direito :: Fontes do DIP e Tratados Internacionais",
    "fontes_dip_tratados_direito.apkg",
    [
        ("Quais são as fontes do DIP listadas no art. 38 do Estatuto da CIJ?",
         "Tratados (convenções), costume internacional, princípios gerais de direito, e como meios auxiliares: jurisprudência e doutrina. [Rezek, DIP, Introdução]"),
        ("O que é tratado internacional (Convenção de Viena 1969)?",
         "Acordo internacional concluído por escrito entre Estados e regido pelo DI, sob qualquer denominação (convenção, carta, protocolo, acordo, pacto). [Rezek, DIP, Cap. I — Parte I]"),
        ("Quais são as etapas de celebração de tratado pelo Brasil?",
         "Negociação/assinatura pelo Executivo → aprovação pelo CN (decreto legislativo) → ratificação pelo Presidente → promulgação e publicação (decreto presidencial). [Rezek, DIP, Cap. I — Parte I]"),
        ("O que é jus cogens?",
         "Norma imperativa de DI geral, aceita e reconhecida pela comunidade internacional, que não admite derrogação (ex.: proibição do genocídio, tortura, escravidão). Art. 53 CV 1969. [Rezek, DIP, Cap. III — Parte I]"),
        ("O que são obrigações erga omnes?",
         "Obrigações devidas à comunidade internacional como um todo (ex.: proibição do genocídio, da pirataria); qualquer Estado pode reclamá-las, não apenas o diretamente lesado. [Rezek, DIP, Cap. III — Parte I]"),
        ("O que é costume internacional?",
         "Prática geral e constante dos Estados (elemento material) acompanhada da convicção de sua obrigatoriedade jurídica — opinio juris (elemento psicológico). [Rezek, DIP, Introdução]"),
        ("O que é soft law?",
         "Normas de DI sem força jurídica vinculante (resoluções da AGNU, declarações, códigos de conduta), mas com relevância política e tendência a se tornarem direito costumeiro. [Rezek, DIP — conceito doutrinário]"),
        ("O que são atos unilaterais dos Estados como fonte de DI?",
         "Declarações unilaterais (reconhecimento, promessa, protesto) que criam obrigações para o Estado emissor se feitas publicamente e com intenção de se vincular. [Rezek, DIP, Cap. II — Parte I]"),
        ("O que são reservas a tratados?",
         "Declaração unilateral de um Estado ao assinar/ratificar um tratado multilateral, excluindo ou modificando o efeito jurídico de certas cláusulas; proibidas se incompatíveis com objeto e fim do tratado. [Rezek, DIP, Cap. I — Parte I]"),
        ("O que é a Convenção de Viena sobre o Direito dos Tratados (1969)?",
         "Código de regras sobre celebração, validade, interpretação e extinção de tratados; o Brasil a incorporou via Dec. 7.030/2009. [Rezek, DIP, Cap. I — Parte I]"),
        ("Como os tratados se incorporam ao Direito Brasileiro?",
         "Pelo rito: assinatura (Executivo) → aprovação CN (decreto legislativo) → ratificação → promulgação (decreto presidencial); adquirem hierarquia de lei ordinária, salvo tratados de DH. [Rezek, DIP, Cap. I — Parte I]"),
        ("O que são acordos executivos (executive agreements)?",
         "Acordos celebrados pelo Executivo sem aprovação do CN; válidos em DI mas controversos no DI brasileiro quando extrapolam a competência presidencial ordinária. [Rezek, DIP, Cap. I — Parte I]"),
        ("O que são os princípios gerais de direito como fonte de DI?",
         "Princípios reconhecidos pelas nações civilizadas (boa-fé, proibição de enriquecimento ilícito, res judicata); complementam lacunas dos tratados e do costume. [Rezek, DIP, Introdução]"),
    ]
)

# ─── 10. ESTADO, TERRITÓRIO E POVO NO DIP ────────────────────
make_deck(
    "CACD :: Direito :: Estado, Território e Povo no DIP",
    "estado_territorio_povo_dip_direito.apkg",
    [
        ("Quais são os elementos do Estado segundo a Convenção de Montevidéu (1933)?",
         "População permanente, território definido, governo e capacidade de entrar em relações com outros Estados. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é reconhecimento de Estado?",
         "Ato unilateral pelo qual um Estado existente aceita a personalidade jurídica de um novo Estado; constitutivo (doutrina) ou declaratório (prática predominante). [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é reconhecimento de governo?",
         "Ato pelo qual um Estado aceita interagir com determinado governo (especialmente após ruptura inconstitucional); pode ser expresso ou tácito. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é sucessão de Estados em DI?",
         "Transferência dos direitos e obrigações de um Estado a outro em razão de mudança de soberania sobre território; regida pela CVST 1978 (tratados) e CVSP 1983 (bens, dívidas, arquivos). [Rezek, DIP, Parte II — Cap. IV]"),
        ("Como se forma o território brasileiro?",
         "Tratados de limites (herança colonial + obra de Rio Branco), uti possidetis (ocupação efetiva), princípio do acordo pacífico e atuação do Itamaraty ao longo dos séculos XIX e XX. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é a Doutrina Calvo?",
         "Doutrina latino-americana: estrangeiros só podem reclamar reparação pelos canais jurídicos internos, renunciando à proteção diplomática de seu Estado natal. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é nacionalidade em DI?",
         "Vínculo jurídico-político entre o indivíduo e um Estado; o DI reconhece a competência de cada Estado para definir seus nacionais, mas exige vínculo genuíno (caso Nottebohm). [Rezek, DIP, Parte II — Cap. I]"),
        ("Quais são os critérios de aquisição de nacionalidade?",
         "Jus soli (local de nascimento — regra geral brasileira), jus sanguinis (filiação — aplicada para filhos de brasileiros nascidos no exterior), naturalização. [Const. Descomplicado, Cap. 1]"),
        ("O que é apatridia e como é tratada no DI?",
         "Condição de quem não possui nenhuma nacionalidade; a Convenção de 1954 protege apátridas; a de 1961 busca reduzir casos futuros. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é extradição?",
         "Entrega de indivíduo acusado ou condenado por crime cometido fora do território do Estado requerido ao Estado requerente, com base em tratado ou reciprocidade. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é asilo político?",
         "Proteção conferida por um Estado a estrangeiro perseguido por razões políticas, ideológicas ou de opinião; asilo territorial (em terra) ou diplomático (em sede de missão). [Rezek, DIP, Parte II — Cap. I]"),
        ("Qual é o princípio da autodeterminação dos povos?",
         "Direito dos povos de determinar livremente sua condição política e seu desenvolvimento econômico, social e cultural; previsto na Carta da ONU e nos Pactos de 1966. [Rezek, DIP, Parte II — Cap. I]"),
    ]
)

# ─── 11. RELAÇÕES DIPLOMÁTICAS, CONSULARES E IMUNIDADES ──────
make_deck(
    "CACD :: Direito :: Relações Diplomáticas, Consulares e Imunidades",
    "relacoes_diplomaticas_imunidades_direito.apkg",
    [
        ("O que regula a Convenção de Viena sobre Relações Diplomáticas (1961)?",
         "Estabelecimento e funcionamento de missões diplomáticas, privilégios e imunidades dos agentes diplomáticos, regras de agrément e persona non grata. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é imunidade de jurisdição diplomática?",
         "Agente diplomático não pode ser processado pelos tribunais do Estado acreditado (recebedor); cobre atos em exercício da função e atos privados. [Rezek, DIP, Parte II — Cap. I]"),
        ("Quais são as exceções à imunidade civil do diplomata?",
         "Art. 31 CVRD 1961: ações reais sobre imóvel privado, sucessórias e de atividade profissional ou comercial particular não ligada às funções. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é inviolabilidade da missão diplomática?",
         "Locais da missão (embaixada) não podem ser invadidos pelo Estado recebedor; o Estado acreditante também tem obrigação de protegê-los (art. 22 CVRD). [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é a Convenção de Viena sobre Relações Consulares (1963)?",
         "Regula funções consulares (proteção de nacionais, expedição de documentos, assistência judiciária), privilégios e imunidades dos cônsules — mais restritas que as diplomáticas. [Rezek, DIP, Parte II — Cap. I]"),
        ("Qual a diferença entre missão diplomática e repartição consular?",
         "Missão diplomática: representa o Estado e mantém relações político-diplomáticas. Repartição consular: presta serviços administrativos a nacionais e promove interesses comerciais. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é proteção diplomática?",
         "Ação do Estado em nome de seu nacional que sofreu dano por ato internacionalmente ilícito de outro Estado; requer esgotamento dos recursos internos. [Rezek, DIP, Parte II — Cap. III]"),
        ("O que é responsabilidade internacional do Estado?",
         "Obrigação de reparar o dano causado por ato internacionalmente ilícito; elementos: conduta atribuível ao Estado + violação de obrigação de DI (Projeto CDI 2001). [Rezek, DIP, Parte II — Cap. III]"),
        ("O que são sujeitos especiais do DI?",
         "Entidades com personalidade jurídica internacional parcial: Santa Sé, Ordem de Malta, beligerantes reconhecidos, movimentos de libertação nacional, indivíduos (no plano dos DH). [Rezek, DIP, Parte II — Introdução]"),
        ("O que é a cláusula da nação mais favorecida?",
         "Tratamento conferido a um Estado deve ser estendido a todos os demais com cláusula NMF; pilar do sistema GATT/OMC e de muitos tratados bilaterais de investimento. [Rezek, DIP, Parte II — Cap. I]"),
    ]
)

# ─── 12. ORGANIZAÇÕES INTERNACIONAIS E INTEGRAÇÃO REGIONAL ───
make_deck(
    "CACD :: Direito :: Organizações Internacionais e Integração Regional",
    "organizacoes_internacionais_integracao_direito.apkg",
    [
        ("O que são organizações internacionais (OIs) em DI?",
         "Sujeitos derivados do DI criados por tratado entre Estados, com personalidade jurídica própria, órgãos permanentes e propósitos definidos. Ex.: ONU, OMC, OEA. [Rezek, DIP, Parte II — Cap. II]"),
        ("Quais são os principais órgãos da ONU?",
         "Assembleia Geral, Conselho de Segurança, Conselho Econômico e Social (ECOSOC), Secretariado, CIJ e Conselho de Tutela (inativo desde 1994). [Rezek, DIP, Parte II — Cap. II]"),
        ("Quais são os membros permanentes do Conselho de Segurança da ONU?",
         "EUA, Reino Unido, França, China e Rússia (P5); possuem poder de veto em questões não processuais. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o Capítulo VII da Carta da ONU?",
         "Autoriza o CSNU a tomar medidas coercitivas (sanções econômicas e uso da força) em resposta a ameaças à paz, rupturas da paz ou atos de agressão. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é o sistema interamericano de direitos humanos?",
         "Composto pela CADH (Pacto de São José, 1969), Comissão Interamericana de DH e Corte Interamericana de DH; o Brasil reconhece a jurisdição contenciosa da Corte desde 1998. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o MERCOSUL e qual seu instrumento fundador?",
         "Mercado Comum do Sul criado pelo Tratado de Assunção (1991) entre Brasil, Argentina, Uruguai e Paraguai; objetivo de livre circulação de bens, serviços, capitais e pessoas. [Rezek, DIP, Parte II — Cap. II]"),
        ("Como o MERCOSUL se relaciona com o DI brasileiro?",
         "Normas do MERCOSUL incorporam-se pela via do decreto presidencial após aprovação pelo CN; não há primado automático sobre o direito interno — posição dualista moderada do Brasil. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a Carta Democrática Interamericana (2001)?",
         "Instrumento da OEA que define a democracia representativa como condição essencial para a vida nas Américas; permite suspensão de Estado com ruptura democrática. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o Tribunal Permanente de Revisão do MERCOSUL?",
         "Órgão de solução de controvérsias criado pelo Protocolo de Olivos (2002); revisa laudos dos tribunais ad hoc e emite opiniões consultivas. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a personalidade jurídica das OIs?",
         "Reconhecida pelo DI (parecer CIJ 1949 — Caso Bernadotte): as OIs podem celebrar tratados, reclamar responsabilidade internacional e ser responsabilizadas. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a imunidade das organizações internacionais?",
         "As OIs gozam de imunidade de jurisdição nos Estados membros para exercício de suas funções; baseada em tratado (acordo de sede) e no costume internacional. [Rezek, DIP, Parte II — Cap. II]"),
    ]
)

# ─── 13. SOLUÇÃO PACÍFICA DE CONTROVÉRSIAS ───────────────────
make_deck(
    "CACD :: Direito :: Solução Pacífica de Controvérsias",
    "solucao_controversias_dip_direito.apkg",
    [
        ("Quais são os meios diplomáticos de solução de controvérsias?",
         "Negociação direta, bons ofícios (terceiro facilita comunicação), mediação (terceiro propõe solução), investigação/inquérito e conciliação. [Rezek, DIP, Parte IV — Cap. I]"),
        ("Quais são os meios jurídicos de solução de controvérsias?",
         "Arbitragem (tribunal ad hoc, decisão vinculante) e judiciário internacional (CIJ, TIDM, OMC, TPI, Corte IDH, tribunais regionais). [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é a CIJ (Corte Internacional de Justiça)?",
         "Principal órgão judicial da ONU; 15 juízes; competência contenciosa (disputas entre Estados) e consultiva (opiniões a órgãos da ONU); jurisdição consensual. [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é a cláusula facultativa de jurisdição obrigatória da CIJ?",
         "Declaração unilateral de aceitação antecipada da jurisdição contenciosa da CIJ para disputas com outros Estados que fizeram igual declaração (art. 36 §2º Estatuto CIJ). [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que são bons ofícios em DI?",
         "Terceiro (Estado ou OI) aproxima as partes em conflito e oferece canal de comunicação, sem propor solução; ex.: papel do Brasil na crise entre EUA e Irã (Acordo de Argel, 1981). [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é mediação em DI?",
         "Terceiro não apenas facilita comunicação, mas propõe ativamente uma solução; proposta não é vinculante, mas as partes podem aceitá-la. Ex.: mediação papal nos conflitos. [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é arbitragem internacional?",
         "Mecanismo consensual de solução de controvérsias em que as partes submetem a disputa a um árbitro ou tribunal ad hoc; decisão (laudo) é vinculante e definitiva. [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é o Mecanismo de Solução de Controvérsias da OMC?",
         "Sistema baseado em painel e Órgão de Apelação; mais automatizado que o GATT; decisões quase automáticas via 'consenso negativo'; o Brasil o usa ativamente. [Rezek, DIP, Parte IV — Cap. I]"),
        ("O que é a obrigação de solucionar controvérsias pacificamente?",
         "Art. 2 §3º e Cap. VI Carta ONU: os membros devem resolver disputas por meios pacíficos de modo que a paz, segurança e a justiça não sejam ameaçadas. [Rezek, DIP, Parte IV — Cap. I]"),
    ]
)

# ─── 14. USO DA FORÇA, DIH E REFUGIADOS ──────────────────────
make_deck(
    "CACD :: Direito :: Uso da Força, Direito Internacional Humanitário e Refugiados",
    "uso_forca_dih_direito.apkg",
    [
        ("O que estabelece o art. 2 §4º da Carta da ONU sobre o uso da força?",
         "Proibição geral do uso da força nas relações internacionais; exceções: legítima defesa (art. 51) e autorização do CSNU (Cap. VII). [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é legítima defesa coletiva em DI?",
         "Direito de Estado ou grupo de Estados de usar a força em defesa de outro atacado; base da OTAN (art. 5 Tratado Washington 1949) e do TIAR. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que são as Convenções de Genebra (1949)?",
         "Quatro convenções que codificam o DIH: proteção de feridos/doentes no campo de batalha, no mar, de prisioneiros de guerra e de civis em conflitos armados. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é Direito Internacional Humanitário (DIH)?",
         "Conjunto de normas que limitam os métodos e meios de guerra e protegem as vítimas dos conflitos armados (combatentes fora de combate e civis). [Rezek, DIP, Parte IV — Cap. II]"),
        ("Quais são os princípios fundamentais do DIH?",
         "Distinção (civis x combatentes), proporcionalidade (dano civil x vantagem militar), necessidade militar e humanidade. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é a Convenção dos Refugiados de 1951 e seu Protocolo de 1967?",
         "Define refugiado: quem teme perseguição por raça, religião, nacionalidade, grupo social ou opinião política; estabelece princípio do non-refoulement. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é o princípio do non-refoulement?",
         "Proibição de devolver um refugiado ao território onde sua vida ou liberdade seria ameaçada; considerado norma de jus cogens para muitos autores. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é a Lei do Refúgio no Brasil (Lei 9.474/1997)?",
         "Implementa a Convenção de 1951 e adota a definição ampliada de 1984 (Declaração de Cartagena): inclui grave e generalizada violação de DH como causa de refúgio. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é o CONARE?",
         "Comitê Nacional para os Refugiados (Ministério da Justiça): decide sobre o reconhecimento, cessação e perda do status de refugiado no Brasil. [Lei 9.474/1997]"),
        ("O que é operação de paz da ONU?",
         "Intervenção autorizada pelo CSNU para manutenção ou restabelecimento da paz; princípios tradicionais: consentimento das partes, imparcialidade e uso mínimo da força. [Rezek, DIP, Parte II — Cap. II]"),
    ]
)

# ─── 15. DIREITOS HUMANOS INTERNACIONAIS ─────────────────────
make_deck(
    "CACD :: Direito :: Direito Internacional dos Direitos Humanos",
    "direitos_humanos_internacionais_direito.apkg",
    [
        ("Quais são os Pactos de 1966 que complementam a DUDH?",
         "Pacto Internacional dos Direitos Civis e Políticos (PIDCP) e Pacto Internacional dos Direitos Econômicos, Sociais e Culturais (PIDESC); formam a Carta Internacional dos DH. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é o Sistema Convencional de Petições da ONU?",
         "Mecanismo pelo qual indivíduos ou grupos podem apresentar comunicações (petições) a comitês de tratados de DH da ONU contra Estados que reconheceram tal competência. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o Conselho de Direitos Humanos da ONU?",
         "Órgão subsidiário da AGNU criado em 2006; substituiu a Comissão de DH; realiza o Exame Periódico Universal (EPU) para avaliar o cumprimento dos DH por todos os Estados. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a Convenção Americana sobre DH (CADH/Pacto de São José, 1969)?",
         "Principal instrumento do sistema interamericano; estabelece a Comissão e a Corte IDH; protege direitos civis e políticos; o Brasil a ratificou em 1992. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a Corte Interamericana de Direitos Humanos?",
         "Órgão judicial da OEA com sede em San José (Costa Rica); proferiu condenações ao Brasil (ex.: caso Gomes Lund — Lei de Anistia); competência aceita pelo Brasil desde 1998. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o princípio da exigibilidade dos direitos humanos?",
         "DH são justiciáveis: seu descumprimento pode ser reclamado perante instâncias nacionais e internacionais; há obrigações positivas e negativas do Estado. [Rezek, DIP, Parte II — Cap. I]"),
        ("Quais tratados de DH foram aprovados pelo Brasil com status de EC (§3º art. 5º CF)?",
         "Convenção Internacional sobre os Direitos das Pessoas com Deficiência e seu Protocolo Facultativo (Dec. Leg. 186/2008). Apenas estes, até 2025. [Const. Descomplicado, Cap. 1]"),
        ("O que é o princípio pro homine (pro persona)?",
         "Interpretação e aplicação da norma mais favorável ao indivíduo quando há concurso de normas de DH; orienta tanto o DI quanto o direito interno. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é o Comitê de Direitos Humanos da ONU?",
         "Órgão de tratado criado pelo PIDCP: monitora sua implementação pelos Estados e analisa comunicações individuais (com o Protocolo Facultativo). [Rezek, DIP, Parte II — Cap. II]"),
        ("O que foi o caso Gomes Lund x Brasil (Corte IDH, 2010)?",
         "Condenou o Brasil pela desaparição forçada de membros da Guerrilha do Araguaia; determinou investigação, punição dos responsáveis e incompatibilidade da Lei de Anistia com a CADH. [Jurisprudência Corte IDH]"),
    ]
)

# ─── 16. DIREITO PENAL INTERNACIONAL E TPI ───────────────────
make_deck(
    "CACD :: Direito :: Direito Penal Internacional e TPI",
    "direito_penal_internacional_tpi_direito.apkg",
    [
        ("O que é o Tribunal Penal Internacional (TPI)?",
         "Corte permanente criada pelo Estatuto de Roma (1998, em vigor em 2002) para julgar crimes mais graves: genocídio, crimes contra a humanidade, crimes de guerra e agressão. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que é o princípio da complementaridade do TPI?",
         "O TPI só atua quando o Estado com jurisdição não quer ou não é capaz de genuinamente processar o caso — a soberania penal do Estado tem primazia. [Estatuto de Roma, art. 17]"),
        ("O que é genocídio no DI (Convenção de 1948)?",
         "Atos praticados com intenção de destruir, no todo ou em parte, grupo nacional, étnico, racial ou religioso; punível mesmo em tempo de paz. [Rezek, DIP, Parte IV — Cap. II]"),
        ("O que são crimes contra a humanidade?",
         "Atos (assassinato, extermínio, escravidão, deportação, tortura, perseguição, apartheid) cometidos como parte de ataque sistemático ou generalizado contra população civil. [Estatuto de Roma, art. 7]"),
        ("O que são crimes de guerra no DI?",
         "Violações graves das Convenções de Genebra e das leis e costumes de guerra; o TPI tem jurisdição quando cometidos em escala considerável. [Estatuto de Roma, art. 8]"),
        ("O que é o crime de agressão no Estatuto de Roma?",
         "Planejamento ou execução de uso da força por Estado contra soberania de outro em manifesta violação da Carta da ONU; definido nas Emendas de Kampala (2010). [Estatuto de Roma, art. 8bis]"),
        ("O Brasil aderiu ao TPI? Qual é o status constitucional?",
         "Sim; o Estatuto de Roma foi incorporado em 2002 (Dec. 4.388/2002); art. 5º §4º CF/88 expressamente admite a sujeição do Brasil ao TPI. [Const. Descomplicado, Cap. 1]"),
        ("Quais foram os principais tribunais penais internacionais ad hoc?",
         "TPII (ex-Iugoslávia, 1993) e TPIR (Ruanda, 1994), criados por resolução do CSNU; precursores do TPI permanente. [Rezek, DIP, Parte IV — Cap. II]"),
    ]
)

# ─── 17. DIREITO DO COMÉRCIO INTERNACIONAL E OIT ─────────────
make_deck(
    "CACD :: Direito :: Direito do Comércio Internacional, OMC e OIT",
    "direito_comercio_omc_oit_direito.apkg",
    [
        ("O que é a OMC e quando foi criada?",
         "Organização Mundial do Comércio (1995, sucessora do GATT): foro de negociação e litígio comercial; baseia-se nos acordos da Rodada Uruguai. [Rezek, DIP, Parte II — Cap. II]"),
        ("Quais são os princípios fundamentais do sistema GATT/OMC?",
         "Não discriminação (cláusula NMF e tratamento nacional), reciprocidade, transparência, liberalização progressiva e exceções (segurança nacional, saúde, meio ambiente). [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o Entendimento sobre Solução de Controvérsias da OMC?",
         "Mecanismo com Órgão de Solução de Controvérsias (OSC), painel e Órgão de Apelação; relatórios adotados por 'consenso negativo' — vinculantes na prática. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o TRIPS (Acordo sobre Propriedade Intelectual)?",
         "Acordo de Marraqueche (1994) que estabelece padrões mínimos de proteção de patentes, marcas, direitos autorais e outros DPI para todos os membros da OMC. [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é o GATS (Acordo Geral sobre Comércio de Serviços)?",
         "Primeiro conjunto de regras multilaterais para o comércio de serviços; cobre 4 modos de fornecimento (transfronteiriço, consumo no exterior, presença comercial, presença de pessoas naturais). [Rezek, DIP, Parte II — Cap. II]"),
        ("O que é a OIT e qual seu principal produto normativo?",
         "Organização Internacional do Trabalho (1919); produz convenções (vinculantes após ratificação) e recomendações (orientações não vinculantes) sobre trabalho decente. [Rezek, DIP, Parte II — Cap. II]"),
        ("Quais são as Convenções Fundamentais da OIT (Declaração de 1998)?",
         "8 convenções sobre: trabalho forçado (29 e 105), liberdade sindical (87 e 98), trabalho infantil (138 e 182) e não discriminação (100 e 111). [OIT — Declaração de 1998]"),
        ("O que é o mecanismo de supervisão normativa da OIT?",
         "Relatórios periódicos dos Estados + reclamações (art. 24) e queixas (art. 26 Constituição OIT); monitorados pela Comissão de Peritos e pelo Comitê da Liberdade Sindical. [OIT — Constituição]"),
    ]
)

# ─── 18. DIREITO DO MAR E MEIO AMBIENTE ──────────────────────
make_deck(
    "CACD :: Direito :: Direito Internacional do Mar e Meio Ambiente",
    "direito_mar_meio_ambiente_direito.apkg",
    [
        ("O que é a CONVEMAR (1982)?",
         "Convenção das Nações Unidas sobre o Direito do Mar; codifica os espaços marinhos, direitos de Estados costeiros e comunidade internacional sobre o mar. [Rezek, DIP, Parte III — Cap. I]"),
        ("Quais são os espaços marítimos previstos na CONVEMAR?",
         "Mar territorial (12mn), Zona Contígua (24mn), ZEE (200mn), Plataforma Continental, Alto Mar e Área (fundo oceânico internacional). [Rezek, DIP, Parte III — Cap. I]"),
        ("O que é a Zona Econômica Exclusiva (ZEE)?",
         "200 milhas náuticas a partir das linhas de base; o Estado costeiro tem direitos soberanos sobre recursos naturais (pesca, petróleo), mas sem soberania plena. [Rezek, DIP, Parte III — Cap. I]"),
        ("O que é o TIDM (Tribunal Internacional do Direito do Mar)?",
         "Criado pela CONVEMAR com sede em Hamburgo; julga disputas sobre direito do mar, incluindo pronta liberação de embarcações e medidas cautelares. [Rezek, DIP, Parte III — Cap. I]"),
        ("O que é a 'Área' no Direito do Mar?",
         "Fundo oceânico além das jurisdições nacionais; considerada 'patrimônio comum da humanidade'; gerida pela Autoridade Internacional dos Fundos Marinhos. [Rezek, DIP, Parte III — Cap. I]"),
        ("Quais são os princípios do Direito Internacional do Meio Ambiente?",
         "Desenvolvimento sustentável, prevenção, precaução, poluidor-pagador, responsabilidades comuns mas diferenciadas, soberania sobre recursos naturais e não-dano ao território alheio. [Rezek, DIP — Direito Ambiental Internacional]"),
        ("O que é o princípio das responsabilidades comuns mas diferenciadas?",
         "Todos os Estados têm responsabilidades sobre o ambiente global, mas os países desenvolvidos devem assumir maior parcela em função de sua maior contribuição histórica ao problema. [Declaração do Rio 1992, Princípio 7]"),
        ("O que foi a Convenção-Quadro sobre Mudança do Clima (UNFCCC, 1992) e o Protocolo de Quioto?",
         "UNFCCC: estrutura para negociações climáticas. Quioto (1997): metas vinculantes de redução de emissões apenas para países do Anexo I (desenvolvidos). [Rezek, DIP — Direito Ambiental]"),
        ("O que é o Acordo de Paris (2015)?",
         "Compromisso climático global: limitação do aquecimento a 1,5–2°C; contribuições nacionalmente determinadas (NDCs) voluntárias mas formalmente depositadas na UNFCCC. [Rezek, DIP — Direito Ambiental]"),
        ("O que são áreas além dos limites da jurisdição exclusiva dos Estados?",
         "Alto mar e Área (fundo oceânico): regimes internacionalizados onde nenhum Estado pode reivindicar soberania; Antártida: regida pelo Tratado de 1959. [Rezek, DIP, Parte III]"),
    ]
)

# ─── 19. COOPERAÇÃO JURÍDICA INTERNACIONAL ───────────────────
make_deck(
    "CACD :: Direito :: Cooperação Jurídica Internacional",
    "cooperacao_juridica_internacional_direito.apkg",
    [
        ("O que é cooperação jurídica internacional (CJI)?",
         "Conjunto de mecanismos pelos quais um Estado solicita ou presta assistência a outro para produção de atos jurídicos com efeitos além-fronteiras (cartas rogatórias, homologação de sentença, extradição). [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é carta rogatória?",
         "Pedido de um juízo estrangeiro a autoridade judiciária brasileira para realização de ato processual (citação, coleta de prova); cumprida pelo STJ após exequatur. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é homologação de sentença estrangeira?",
         "Procedimento pelo qual o STJ reconhece decisão judicial de outro país, conferindo-lhe eficácia no Brasil; requisitos: autenticidade, citação válida, coisa julgada, não contrária à ordem pública. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é o MLAT (Mutual Legal Assistance Treaty)?",
         "Tratado de assistência jurídica mútua em matéria penal: permite troca de provas, depoimentos e informações financeiras entre países para investigação de crimes transnacionais. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é o mecanismo de cooperação penal via autoridade central?",
         "Cada país designa uma autoridade central (no Brasil, o DRCI/MJ) para receber e encaminhar pedidos de CJI penal; dispensa a via diplomática para pedidos entre países com tratado. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é a Convenção de Haia sobre Aspectos Civis do Sequestro Internacional de Crianças (1980)?",
         "Obriga o retorno imediato da criança ao país de residência habitual quando removida ilicitamente; o Brasil a incorporou pelo Dec. 3.413/2000. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é o exequatur?",
         "Decisão do STJ que confere eficácia no Brasil à carta rogatória passiva ou à sentença estrangeira homologada; sem exequatur, o ato não pode ser executado por autoridade brasileira. [Rezek, DIP, Parte II — Cap. I]"),
        ("O que é a Convenção de Haia sobre a Supressão do Apostilamento?",
         "Simplifica a autenticação de documentos públicos entre os países signatários: basta apostila do país emissor, sem necessidade de legalização consular. O Brasil aderiu em 2016. [Rezek, DIP, Parte II — Cap. I]"),
    ]
)

print("\n🎉 Todos os 19 decks de Direito criados com sucesso!")
