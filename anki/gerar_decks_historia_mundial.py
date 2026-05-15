import genanki
import random
import os

BASE = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/historia-mundial"
os.makedirs(BASE, exist_ok=True)

def make_deck(deck_title, file_path, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        "CACD História Mundial",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card 1",
            "qfmt": "{{Frente}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Verso}}",
        }],
    )
    deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_title)
    for frente, verso in cards:
        deck.add_note(genanki.Note(model=model, fields=[frente, verso]))
    genanki.Package(deck).write_to_file(file_path)
    print(f"✅ {os.path.basename(file_path)} — {len(cards)} cards")


# ─── 1. ESTRUTURAS E IDEIAS ECONÔMICAS ────────────────────────────────────
make_deck(
    "CACD · História Mundial · Estruturas e Ideias Econômicas",
    f"{BASE}/estruturas_ideias_economicas_hm.apkg",
    [
        ("O que foi a Revolução Industrial e por que começou na Inglaterra (séc. XVIII)?",
         "Mecanização da produção, uso do carvão e vapor, fábrica como unidade produtiva. Inglaterra: capital acumulado, carvão abundante, mercado colonial, estabilidade política. [Hobsbawm, Era das Revoluções, Cap. 2]"),
        ("Quais as fases do desenvolvimento capitalista desde 1780 segundo Hobsbawm?",
         "1) Capitalismo industrial (1780-1848). 2) Capitalismo liberal/concorrencial (1848-75). 3) Capitalismo monopolista/imperialista (1875-1914). 4) Capitalismo organizado/fordista (séc. XX). [Era das Revoluções; Era do Capital; Era dos Impérios]"),
        ("O que é a Fisiocracia e qual sua contribuição às ideias econômicas?",
         "Escola francesa (Quesnay, séc. XVIII): riqueza vem da terra/agricultura; defende laissez-faire. Precursora do liberalismo ao criticar o mercantilismo. [Hobsbawm, Era das Revoluções, Cap. 13]"),
        ("Quais os pilares do liberalismo econômico clássico (Adam Smith, Ricardo)?",
         "Livre mercado, divisão do trabalho, lei da oferta/demanda, mão invisível, livre-comércio. Ricardo: vantagens comparativas. Contra o intervencionismo estatal. [Hobsbawm, Era das Revoluções, Cap. 13]"),
        ("Quais os conceitos centrais do Marxismo como crítica ao capitalismo?",
         "Mais-valia, luta de classes, materialismo histórico, alienação do trabalho, inevitabilidade da revolução proletária. Marx/Engels, O Capital (1867) e Manifesto Comunista (1848). [Hobsbawm, Era do Capital, Cap. 14]"),
        ("O que foi a Crise de 1929 e como ela se propagou globalmente?",
         "Crash da Bolsa de NY (out. 1929): contração do crédito, deflação, desemprego em massa. Propagação pelo sistema financeiro internacional (padrão-ouro interligava economias). [Hobsbawm, Era dos Extremos, Cap. 3]"),
        ("O que foi o New Deal (1933) de Roosevelt e qual sua lógica keynesiana?",
         "Programa de recuperação econômica: obras públicas, regulação financeira, proteção social. Lógica: Estado gasta para estimular demanda e retomar crescimento (Keynes). [Hobsbawm, Era dos Extremos, Caps. 3-4]"),
        ("O que foi o Estado de Bem-Estar Social (Welfare State) e quando entrou em crise?",
         "Modelo pós-WWII: Estado provê saúde, educação, previdência, seguro-desemprego. Prosperidade 1945-73 ('Anos Dourados'). Crise: choque do petróleo (1973), estagflação, crítica neoliberal. [Era dos Extremos, Cap. 9; 14]"),
        ("O que é o Pós-Fordismo e a acumulação flexível?",
         "A partir dos anos 1970: produção just-in-time, terceirização, especialização flexível, declínio do emprego industrial. Substituição do fordismo (produção em massa + consumo de massa). [Hobsbawm, Era dos Extremos, Cap. 14]"),
        ("O que foi a 'Era de Ouro' do capitalismo (1945–1973)?",
         "Crescimento econômico sem precedentes: reconstrução europeia (Plano Marshall), fordismo, pleno emprego, expansão do consumo de massa, Bretton Woods. Encerrou com o choque do petróleo de 1973. [Hobsbawm, Era dos Extremos, Caps. 8-9]"),
        ("Qual a diferença entre capitalismo concorrencial (séc. XIX) e capitalismo monopolista (séc. XX)?",
         "Concorrencial: muitas empresas disputam mercados livres. Monopolista: trustes, cartéis e oligopólios dominam setores; Estado regula ou nacionaliza. Transição marcada pela II Revolução Industrial (1870s). [Hobsbawm, Era dos Impérios, Caps. 1-2]"),
    ]
)

# ─── 2. REVOLUÇÕES ────────────────────────────────────────────────────────
make_deck(
    "CACD · História Mundial · Revoluções",
    f"{BASE}/revolucoes_hm.apkg",
    [
        ("Quais as fases da Revolução Francesa (1789) e seus principais resultados?",
         "1) Monarquia Constitucional (1789-92). 2) República/Terror (1792-94). 3) Diretório/Napoleão (1795-1815). Resultados: Declaração dos Direitos do Homem, fim do Antigo Regime, ideais liberais. [Hobsbawm, Era das Revoluções, Cap. 3]"),
        ("O que foram as 'revoluções burguesas' e quais as principais?",
         "Revoluções que substituíram o Antigo Regime pela ordem liberal-burguesa: 1688 (Inglaterra), 1776 (EUA), 1789 (França), 1848 (Europa). Afirmaram direitos civis, propriedade privada e mercado. [Era das Revoluções, Caps. 3-6]"),
        ("O que foram as Revoluções de 1848 na Europa ('Primavera dos Povos')?",
         "Onda revolucionária em França, Alemanha, Áustria, Itália: pediram constituições, unificação nacional, direitos liberais. Quase todas reprimidas. Marcou maturidade do movimento operário. [Hobsbawm, Era do Capital, Cap. 1]"),
        ("O que foram os processos de independência na América (séc. XVIII-XIX)?",
         "EUA (1776): influência iluminista. América Latina (1808-26): crise napoleônica enfraqueceu metrópoles ibéricas; Bolívar e San Martín lideraram independências; Brasil (1822): processo conservador. [Era das Revoluções, Cap. 6]"),
        ("O que é o anarquismo e quais seus principais teóricos?",
         "Corrente que rejeita o Estado como forma de dominação; defende autogestão e abolição da propriedade privada. Teóricos: Proudhon ('A Propriedade é um Roubo'), Bakunin, Kropotkin. [Hobsbawm, Era do Capital, Cap. 6]"),
        ("O que é o socialismo científico e como difere do socialismo utópico?",
         "Marx/Engels: socialismo científico baseia-se em análise material da história (materialismo histórico), luta de classes e revolução proletária. Utópico (Owen, Saint-Simon): projetos ideais sem análise das contradições do capitalismo. [Hobsbawm, Era do Capital, Cap. 14]"),
        ("O que foi a Revolução Russa de 1917 e quais suas fases?",
         "Fevereiro: derruba o Czar (governo provisório liberal). Outubro: bolcheviques (Lenin) tomam o poder — 1º Estado socialista. Causas: WWI, crise econômica, autocracia. [Hobsbawm, Era dos Extremos, Cap. 2]"),
        ("O que foi a Revolução Chinesa (1949) e como ocorreu?",
         "Partido Comunista Chinês (Mao Tsé-tung) derrotou o Kuomintang (Chiang Kai-shek) após guerra civil (1927-49). Proclamou a República Popular da China em 1/out/1949. [Hobsbawm, Era dos Extremos, Caps. 2; 12]"),
        ("O que foi a Revolução Mexicana (1910–1920)?",
         "Derrubou a ditadura de Porfírio Díaz. Líderes: Zapata (reforma agrária), Villa, Carranza. Constituição de 1917: direitos trabalhistas, educação pública, reforma agrária — primeira constituição social do mundo. [Hobsbawm, Era dos Extremos, Cap. 15]"),
        ("O que foi a Revolução Cubana (1959) e qual seu impacto na Guerra Fria?",
         "Fidel Castro e guerrilha derrubaram Batista (1/jan/1959). Cuba alinhou-se à URSS (1961). Precipitou a Crise dos Mísseis (1962) e influenciou movimentos guerrilheiros na AL. [Hobsbawm, Era dos Extremos, Caps. 12; 15]"),
        ("O que foi a I Internacional (AIT) e a II Internacional?",
         "I Internacional (1864): fundada por Marx; dissolve-se após conflitos com anarquistas (1876). II Internacional (1889): socialistas europeus; fragmentou-se com a WWI (cada partido apoiou seu governo). [Hobsbawm, Era do Capital, Cap. 6; Era dos Impérios, Cap. 5]"),
    ]
)

# ─── 3. RELAÇÕES INTERNACIONAIS ───────────────────────────────────────────
make_deck(
    "CACD · História Mundial · Relações Internacionais",
    f"{BASE}/relacoes_internacionais_hm.apkg",
    [
        ("O que foi o Concerto Europeu (1815) e como funcionava?",
         "Sistema de equilíbrio de poder criado pelo Congresso de Viena: GB, Áustria, Prússia, Rússia (+ França depois) geriam a ordem europeia. Manteve paz relativa por 100 anos até 1914. [Hobsbawm, Era das Revoluções, Cap. 5]"),
        ("Quais as causas imediatas e estruturais da I Guerra Mundial (1914)?",
         "Imediata: assassinato do Arquiduque Franz Ferdinand (Sarajevo, jun. 1914). Estruturais: rivalidades imperialistas, sistema de alianças (Tríplice vs. Entente), corrida armamentista, nacionalismo balcânico. [Hobsbawm, Era dos Impérios, Cap. 13]"),
        ("O que foram os 14 Pontos de Wilson (1918) e qual seu objetivo?",
         "Programa de paz do presidente americano: autodeterminação dos povos, liberdade de navegação, desarmamento, Liga das Nações. Visava ordem liberal internacional. Parcialmente ignorado em Versalhes. [Hobsbawm, Era dos Extremos, Cap. 1]"),
        ("O que foi a Paz de Versalhes (1919) e por que foi criticada?",
         "Tratado que encerrou a WWI: Alemanha perdeu territórios, colônias, exército e pagou reparações (132 bi marcos-ouro). Keynes: injusta e economicamente destrutiva. Gerou ressentimento que alimentou o nazismo. [Hobsbawm, Era dos Extremos, Caps. 1; 4]"),
        ("O que foi a Liga das Nações e por que fracassou?",
         "Organização criada em 1920 (Versalhes): segurança coletiva, arbitragem de conflitos. EUA não aderiram (Senado rejeitou). Impotente diante da agressão japonesa (1931), italiana (1935) e alemã (1936-39). [Hobsbawm, Era dos Extremos, Cap. 4]"),
        ("Quais as causas da II Guerra Mundial (1939)?",
         "Versalhes humilhante, ascensão do nazismo, política de apaziguamento (Munique, 1938), pacto Molotov-Ribbentrop (ago. 1939). Início: invasão da Polônia (1/set/1939). [Hobsbawm, Era dos Extremos, Caps. 4-5]"),
        ("O que foram as Conferências de Teerã, Ialta e Potsdam e o que decidiram?",
         "Teerã (1943): invasão da Normandia. Ialta (fev/1945): divisão da Europa em zonas de influência, criação da ONU. Potsdam (jul/1945): ocupação da Alemanha, reparações, Japão. [Hobsbawm, Era dos Extremos, Cap. 5]"),
        ("O que foi Bretton Woods (1944) e que instituições criou?",
         "Conferência que reorganizou o sistema financeiro internacional pós-WWII: criou o FMI, Banco Mundial e o padrão dólar-ouro. Base da ordem econômica liberal do pós-guerra. [Hobsbawm, Era dos Extremos, Cap. 8]"),
        ("O que foi o Plano Marshall (1947) e qual seu duplo objetivo?",
         "EUA ofereceram US$ 13 bi para reconstrução da Europa Ocidental. Objetivo declarado: reconstrução econômica. Objetivo estratégico: evitar avanço do comunismo em países empobrecidos. [Hobsbawm, Era dos Extremos, Cap. 8]"),
        ("Como a ONU foi criada e quais seus órgãos principais?",
         "Conferência de São Francisco (abr-jun/1945): 51 membros fundadores. Órgãos: Assembleia Geral, Conselho de Segurança (5 membros permanentes com veto), Secretariado, CIJ, ECOSOC. [Hobsbawm, Era dos Extremos, Cap. 8]"),
        ("O que foi a Guerra Fria e quais suas características principais?",
         "Rivalidade EUA × URSS (1947-1991): confronto ideológico, nuclear, econômico e geopolítico sem guerra direta. Marcos: Doutrina Truman, NATO, Pacto de Varsóvia, Corrida Espacial, Crise dos Mísseis (1962). [Hobsbawm, Era dos Extremos, Cap. 8]"),
        ("O que foi a Détente (distensão) nos anos 1970?",
         "Redução das tensões EUA-URSS: acordos SALT I (1972), visita de Nixon à China (1972), Acordos de Helsinque (1975). Fim da détente: invasão soviética do Afeganistão (1979). [Hobsbawm, Era dos Extremos, Caps. 8; 14]"),
        ("O que foi a 'Segunda Guerra Fria' (Reagan, 1981–1989)?",
         "Reagan retomou a retórica belicista ('Império do Mal'), IDS (Guerra nas Estrelas), apoio a guerrilhas anticomunistas (Doutrina Reagan). URSS sobre pressão econômica e tecnológica. [Hobsbawm, Era dos Extremos, Cap. 16]"),
        ("Como ocorreu a desagregação do bloco soviético (1989–1991)?",
         "Gorbachev: Glasnost e Perestroika. Queda do Muro de Berlim (9/nov/1989). Revoluções no Leste Europeu. Dissolução da URSS (25/dez/1991): 15 repúblicas independentes. [Hobsbawm, Era dos Extremos, Cap. 16]"),
    ]
)

# ─── 4. COLONIALISMO, IMPERIALISMO, POLÍTICAS DE DOMINAÇÃO ────────────────
make_deck(
    "CACD · História Mundial · Colonialismo e Imperialismo",
    f"{BASE}/colonialismo_imperialismo_hm.apkg",
    [
        ("O que foi o 'Novo Imperialismo' do séc. XIX e como diferiu do colonialismo anterior?",
         "Colonialismo antigo: exploração comercial/mercantil com presença limitada. Novo Imperialismo (1870-1914): domínio territorial direto, exportação de capital, 'missão civilizatória'. [Hobsbawm, Era dos Impérios, Cap. 3]"),
        ("Quais as principais teorias sobre a natureza do imperialismo?",
         "Hobson (1902): superprodução + exportação de capital. Lenin (1916): imperialismo como fase superior do capitalismo (monopólios). Schumpeter: imperialismo como atavismo pré-capitalista. [Hobsbawm, Era dos Impérios, Caps. 3; 11]"),
        ("O que foi a Conferência de Berlim (1884-85) e o que decidiu?",
         "Potências europeias dividiram a África entre si ('partilha da África') sem considerar populações locais. Estabeleceu regras para ocupação efetiva. 90% da África sob controle europeu em 1914. [Hobsbawm, Era dos Impérios, Cap. 3]"),
        ("Como a Índia respondeu ao imperialismo britânico no séc. XIX e XX?",
         "Motim dos Cipaios (1857): violentamente reprimido → domínio direto da Coroa. Congresso Nacional Indiano (1885): elite intelectual. Gandhi: desobediência civil, não-violência; independência em 1947. [Hobsbawm, Era dos Extremos, Cap. 7]"),
        ("Como a China reagiu ao imperialismo europeu e japonês?",
         "Guerras do Ópio (1839-42; 1856-60): tratados desiguais. Revolta dos Boxer (1900). Queda da dinastia Qing (1911). República de Sun Yat-sen. Ocupação japonesa (1931-45) → Revolução de 1949. [Hobsbawm, Era dos Impérios, Caps. 3; 12]"),
        ("Como o Japão reagiu ao imperialismo ocidental e qual sua estratégia?",
         "Era Meiji (1868): modernização acelerada, industrialização, exército ocidentalizado. Tornou-se potência imperial: venceu a China (1895) e a Rússia (1905). Único país não-ocidental a industrializar-se no séc. XIX. [Hobsbawm, Era dos Impérios, Cap. 3]"),
        ("O que foi a descolonização e em que contexto ocorreu?",
         "Processo de independência das colônias afro-asiáticas, principalmente após a WWII (1945-1975). Impulsionado por: enfraquecimento das metrópoles, movimentos nacionalistas, pressão da ONU e da Guerra Fria. [Hobsbawm, Era dos Extremos, Cap. 7]"),
        ("O que foi a Conferência de Bandung (1955) e qual sua importância?",
         "29 países afro-asiáticos em Bandung (Indonésia): princípios de coexistência pacífica, condenação do colonialismo, não-alinhamento. Marco do Terceiro Mundo como ator político. [Hobsbawm, Era dos Extremos, Cap. 12]"),
        ("O que foi o Movimento dos Não-Alinhados e quando foi formalizado?",
         "Criado na Conferência de Belgrado (1961): países que recusavam alinhamento automático com EUA ou URSS. Líderes: Nasser, Nehru, Tito, Sukarno. Base política: autodeterminação e anti-imperialismo. [Hobsbawm, Era dos Extremos, Cap. 12]"),
        ("O que é o conceito de 'Terceiro Mundo' e como surgiu?",
         "Termo cunhado por Alfred Sauvy (1952): países não alinhados nem ao capitalismo (1º Mundo) nem ao socialismo (2º Mundo). Conotação: subdesenvolvimento + colonialismo + libertação. [Hobsbawm, Era dos Extremos, Cap. 12]"),
        ("Quais foram os principais movimentos de resistência ao imperialismo na África antes de 1945?",
         "Resistência armada: Etiópia (1896, batalha de Adwa contra Itália), Zulus (GB), Hereros (Alemanha). Movimentos intelectuais: Pan-Africanismo (Du Bois, Garvey). Organização política pós-1945. [Hobsbawm, Era dos Impérios, Cap. 3; Era dos Extremos, Cap. 7]"),
    ]
)

# ─── 5. EVOLUÇÃO POLÍTICA E ECONÔMICA NAS AMÉRICAS ────────────────────────
make_deck(
    "CACD · História Mundial · Evolução Política e Econômica nas Américas",
    f"{BASE}/americas_politica_economia_hm.apkg",
    [
        ("Como ocorreu a expansão territorial dos EUA no séc. XIX?",
         "Doutrina do 'Destino Manifesto': compra da Louisiana (1803), da Flórida (1819), Texas (1845), Oregon (1846), guerra com México (1848, California + NM), compra do Alasca (1867). [Hobsbawm, Era do Capital, Cap. 3]"),
        ("O que foi a Guerra de Secessão (1861-1865) e quais suas causas?",
         "Guerra entre Norte (União) e Sul (Confederação). Causas: escravidão como questão moral e econômica, tensão tarifária (protecionismo × livre-comércio), expansão da escravidão para novos territórios. [Hobsbawm, Era do Capital, Cap. 4]"),
        ("Quais os resultados da Guerra de Secessão para os EUA?",
         "Abolição da escravidão (13ª Emenda, 1865). Unidade nacional preservada. Industrialização acelerada do Norte. Início da segregação racial no Sul (leis Jim Crow). Lincoln assassinado. [Hobsbawm, Era do Capital, Cap. 4]"),
        ("Como se formaram as identidades nacionais na América Latina no séc. XIX?",
         "Elites crioulas construíram estados nacionais frágeis: militarismo, caudilhismo, instabilidade. Identidade nacional fragmentada por regionalismos e diversidade étnica; economia primário-exportadora. [Hobsbawm, Era do Capital, Cap. 5]"),
        ("O que é a Doutrina Monroe (1823) e como foi aplicada?",
         "'América para os americanos': EUA opõem-se à recolonização europeia nas Américas. Aplicações: Corolário Roosevelt (1904, intervencionismo), Doutrina Truman (1947), Cuba (1962). [Hobsbawm, Era do Capital, Cap. 3]"),
        ("O que foi o Pan-Americanismo e quando foi institucionalizado?",
         "Ideia de cooperação entre os países do hemisfério ocidental. I Conferência Internacional Americana (Washington, 1889-90). Tornou-se a Organização dos Estados Americanos (OEA) em 1948. [contexto: Cervo & Bueno]"),
        ("O que é a OEA e o que é o Tratado do Rio de Janeiro (TIAR)?",
         "OEA (1948, Bogotá): organização política hemisférica — defesa da democracia e direitos humanos. TIAR (1947): defesa coletiva hemisférica ('ataque a um é ataque a todos'). Base da segurança coletiva interamericana. [contexto]"),
        ("Quais foram as principais experiências de integração nas Américas?",
         "ALALC (1960) → ALADI (1980): integração comercial latino-americana. MERCOSUL (1991). NAFTA (1994) → USMCA (2020): EUA-Canadá-México. ALCA (proposta, 2005): fracassou. UNASUL (2008). [Hobsbawm, Era dos Extremos, Cap. 19]"),
        ("O que foi o imperialismo dos EUA na América Latina no séc. XX?",
         "Corolário Roosevelt (1904): EUA como 'gendarme' do hemisfério. Intervenções militares: Nicarágua, Haiti, Cuba, República Dominicana. Guerra Fria: apoio a ditaduras militares contra o comunismo. [Hobsbawm, Era dos Extremos, Caps. 8; 15]"),
    ]
)

# ─── 6. IDEIAS E REGIMES POLÍTICOS ────────────────────────────────────────
make_deck(
    "CACD · História Mundial · Ideias e Regimes Políticos",
    f"{BASE}/ideias_regimes_politicos_hm.apkg",
    [
        ("O que é o liberalismo político do séc. XIX e quais seus pilares?",
         "Liberdade individual, direitos civis, propriedade privada, governo representativo, separação de poderes, rule of law. Locke, Montesquieu, Mill. Opõe-se ao absolutismo e ao coletivismo. [Hobsbawm, Era das Revoluções, Cap. 13]"),
        ("O que é o nacionalismo do séc. XIX e como se relaciona com a formação de Estados?",
         "Princípio de que cada nação (povo com língua, cultura, história comuns) deve ter seu próprio Estado. Hobsbawm: nações são 'comunidades imaginárias'. Motor das unificações alemã e italiana. [Hobsbawm, Era do Capital, Cap. 5; Era dos Impérios, Cap. 6]"),
        ("Como foi a unificação da Alemanha (1871) e quem a liderou?",
         "Bismarck (Prússia): unificação 'pelo ferro e pelo sangue' — guerras contra Dinamarca (1864), Áustria (1866) e França (1870-71). Proclamação do Império Alemão em Versalhes (jan. 1871). [Hobsbawm, Era do Capital, Cap. 5]"),
        ("Como foi a unificação da Itália (Risorgimento, 1861–1870)?",
         "Cavour (diplomacia/Piemonte), Garibaldi (Expedição dos Mil, 1860). Unificação gradual: Reino da Itália (1861). Roma incorporada em 1870 com a queda do Estado Papal. [Hobsbawm, Era do Capital, Cap. 5]"),
        ("O que é o fascismo e quais suas características centrais?",
         "Ultranacionalismo, corporativismo, culto ao líder, violência política, anti-marxismo e anti-liberalismo, expansionismo. Mussolini (Itália, 1922), Hitler (Alemanha, 1933). [Hobsbawm, Era dos Extremos, Cap. 4]"),
        ("Quais as especificidades do nazismo em relação ao fascismo genérico?",
         "Nazismo adiciona: racismo científico, antissemitismo, teoria do espaço vital (Lebensraum), hierarquia racial, Holocausto. Hitler como Führer do III Reich. [Hobsbawm, Era dos Extremos, Caps. 4-5]"),
        ("O que é o comunismo enquanto regime político (marxismo-leninismo)?",
         "Ditadura do proletariado, partido único, planificação central, coletivização da propriedade. Lenin adaptou o marxismo: partido de vanguarda conduz a revolução. Stalin: socialismo num só país, terror. [Hobsbawm, Era dos Extremos, Caps. 2; 13]"),
        ("O que é o liberalismo do séc. XX e como evoluiu diante das crises?",
         "Democracia liberal + economia de mercado regulada. New Deal e Welfare State incorporaram elementos intervencionistas. Neoliberalismo (Thatcher/Reagan, anos 1980): retorno ao liberalismo clássico com desregulação e privatizações. [Hobsbawm, Era dos Extremos, Caps. 4; 14]"),
        ("O que é o 'novo nacionalismo' e o fundamentalismo contemporâneo?",
         "Novo nacionalismo pós-Guerra Fria: étnico-religioso (Iugoslávia, Ruanda). Fundamentalismo: islâmico (Irã 1979, Al-Qaeda, ISIS), cristão, Hindu. Reação à globalização e ao secularismo. [Hobsbawm, Era dos Extremos, Cap. 19]"),
        ("O que foi a social-democracia europeia e como se distingue do comunismo?",
         "Aceita a democracia representativa e a economia de mercado; busca reformas graduais (não revolução) para redistribuição. Bismarck criou primeiros seguros sociais; SPD alemã como modelo. Base do Welfare State. [Hobsbawm, Era dos Impérios, Cap. 5]"),
        ("O que foi a III Internacional (Comintern, 1919) e qual seu papel?",
         "Fundada por Lenin para coordenar partidos comunistas mundiais sob liderança soviética. Stalin dissolveu o Comintern (1943) como gesto de boa vontade para com os Aliados ocidentais. [Hobsbawm, Era dos Extremos, Cap. 2]"),
    ]
)

# ─── 7. A VIDA CULTURAL ───────────────────────────────────────────────────
make_deck(
    "CACD · História Mundial · A Vida Cultural",
    f"{BASE}/vida_cultural_hm.apkg",
    [
        ("O que foi o Romantismo e em que contexto histórico surgiu?",
         "Movimento artístico-cultural (fins séc. XVIII – meados XIX): valorização da emoção, natureza, história nacional, individualismo. Reação ao Iluminismo e à industrialização. Goethe, Byron, Delacroix, Beethoven. [Hobsbawm, Era das Revoluções, Cap. 14]"),
        ("O que foi o Realismo e o Naturalismo no séc. XIX?",
         "Reação ao Romantismo: representação objetiva da realidade social, inclusive a miséria. Realismo: Balzac, Flaubert, Dickens. Naturalismo: Zola (determinismo biológico e social). Reflete a industrialização. [Hobsbawm, Era do Capital, Cap. 15]"),
        ("O que foi a 'cultura do imperialismo' no séc. XIX?",
         "Ideologia que legitimava a dominação colonial: 'missão civilizatória', darwinismo social (raças superiores/inferiores), orientalismo (Said). Literatura, arte e museus exaltavam o Império. [Hobsbawm, Era dos Impérios, Caps. 3; 7]"),
        ("O que foram as vanguardas europeias (fins séc. XIX – 1ª metade séc. XX)?",
         "Movimentos de ruptura com o classicismo: Impressionismo, Expressionismo, Cubismo (Picasso), Futurismo, Dadaísmo, Surrealismo. Refletem crise da modernidade e traumas da WWI. [Hobsbawm, Era dos Impérios, Cap. 9; Era dos Extremos, Cap. 6]"),
        ("O que foi o Modernismo cultural e como se manifesta?",
         "Ruptura com tradições do séc. XIX: experimentalismo formal, fragmentação narrativa, stream of consciousness. Joyce, Woolf, Kafka, Le Corbusier (arquitetura), Stravinsky (música). Parallelo político: busca de novas ordens. [Hobsbawm, Era dos Extremos, Cap. 6]"),
        ("O que é a Pós-modernidade e como se distingue da modernidade?",
         "A partir dos anos 1960-70: ceticismo às 'metanarrativas' (Lyotard), relativismo cultural, pluralidade de verdades, pastiche. Fim das grandes ideologias; cultura do consumo e da imagem. [Hobsbawm, Era dos Extremos, Cap. 17]"),
        ("Qual o impacto da indústria cultural do séc. XX na sociedade de massas?",
         "Rádio, cinema, TV: homogeneização cultural e propaganda política (Goebbels, Hollywood). Escola de Frankfurt (Adorno, Horkheimer): 'indústria cultural' como dominação ideológica. [Hobsbawm, Era dos Extremos, Cap. 11]"),
        ("O que foi a 'Revolução Cultural' dos anos 1960?",
         "Transformação de costumes: contracultura, feminismo de 2ª onda, movimentos pelos direitos civis (EUA), Maio de 68 (França). Questionou autoridades tradicionais (família, Igreja, Estado). [Hobsbawm, Era dos Extremos, Cap. 11]"),
    ]
)

# ─── 8. SÉCULO XXI ────────────────────────────────────────────────────────
make_deck(
    "CACD · História Mundial · Século XXI",
    f"{BASE}/seculo_xxi_hm.apkg",
    [
        ("Como as redes sociais transformaram as relações internacionais no séc. XXI?",
         "Diplomacia digital: líderes usam Twitter/X para comunicação direta. Mobilizações: Primavera Árabe (2010-11) via Facebook/Twitter. Desinformação como arma geopolítica. [Hobsbawm, Era dos Extremos, Cap. 19 — atualizado]"),
        ("O que é a 'era pós-verdade' e qual seu impacto político?",
         "Conceito pós-2016 (Brexit, Trump): crenças e emoções prevalecem sobre fatos verificáveis. Fake news, câmaras de eco e algoritmos amplificam polarização. Desafio para democracias liberais. [contexto contemporâneo]"),
        ("O que foi a Primavera Árabe (2010–2012) e qual seu legado?",
         "Onda de protestos e revoluções no mundo árabe (Tunísia, Egito, Líbia, Síria): mobilizados via redes sociais. Resultado misto: democracia na Tunísia; guerras civis na Síria e Líbia; autoritarismo no Egito. [contexto contemporâneo]"),
        ("Como as tecnologias digitais afetam a soberania dos Estados e a diplomacia?",
         "Ciberataques como instrumento de política externa (Stuxnet, Rússia × Ucrânia). Espionagem digital (NSA, PRISM, Snowden 2013). Regulação de plataformas como questão soberana. [contexto contemporâneo]"),
        ("O que é a multipolaridade do séc. XXI e como difere da bipolaridade da Guerra Fria?",
         "EUA como potência declinante; China como concorrente sistêmico; Rússia revisionista; BRICS como bloco alternativo. Sem polaridade clara: múltiplos centros de poder competem. [contexto contemporâneo]"),
        ("Qual o impacto da Inteligência Artificial nas relações internacionais?",
         "Corrida tecnológica EUA-China (chips, LLMs, armamento autônomo). IA em campanhas eleitorais (deepfakes, microtargeting). Debates sobre regulação multilateral (análogo ao TNP para armas nucleares). [contexto contemporâneo]"),
        ("O que foi o ataque de 11 de setembro (2001) e quais suas consequências geopolíticas?",
         "Al-Qaeda derrubou as Torres Gêmeas. EUA invadiram Afeganistão (2001) e Iraque (2003). Doutrina Bush: guerra preventiva. Criação do DHS, PATRIOT Act. Reorientação da política de segurança global. [contexto contemporâneo]"),
        ("Como a pandemia de Covid-19 (2020–2022) impactou a ordem internacional?",
         "Acelerou desglobalização, expôs fragilidade das cadeias de suprimento, aumentou poder estatal. Vacinas como geopolítica (diplomacia das vacinas). Aprofundou rivalidade EUA-China (origem do vírus). [contexto contemporâneo]"),
    ]
)

print("\n🎉 Todos os 8 decks de História Mundial criados com sucesso!")
