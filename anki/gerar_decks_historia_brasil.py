import genanki
import random
import os

BASE = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/historia-br"
os.makedirs(BASE, exist_ok=True)

def make_deck(deck_title, file_path, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        "CACD História do Brasil",
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


# ─── 1. PERÍODO COLONIAL ───────────────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Período Colonial",
    f"{BASE}/periodo_colonial_hb.apkg",
    [
        ("Qual o sistema de administração territorial adotado por Portugal no Brasil em 1534 e por que fracassou?",
         "Capitanias Hereditárias: terras doadas a donatários para colonizar e defender. Fracassou por falta de recursos dos donatários e ataques indígenas. [Fausto, Cap. 2.4]"),
        ("O que foi o Governo Geral (1549) e qual sua função?",
         "Sistema centralizado criado pela Coroa para coordenar a colonização. Tomé de Sousa foi o 1º governador; fundou Salvador como capital. [Fausto, Cap. 2.5]"),
        ("Quais os três ciclos econômicos principais do Brasil colonial e suas regiões?",
         "Açúcar (Nordeste, séc. XVI–XVII), Ouro e Diamantes (Minas Gerais, séc. XVIII), Algodão/Tabaco (secundários). [Fausto, Caps. 2.17–2.21]"),
        ("Como funcionava o 'exclusivo colonial' (pacto colonial)?",
         "Metrópole monopolizava comércio da colônia: Brasil só podia comerciar com Portugal, a preços impostos pela Coroa. Base do mercantilismo português. [Fausto, Cap. 2.10]"),
        ("Qual foi o impacto da mineração (séc. XVIII) na estrutura social e territorial do Brasil?",
         "Deslocou o centro econômico para MG; criou sociedade urbana e mercantil; originou Vila Rica; gerou impostos (quinto) e tensões com a Coroa. [Fausto, Caps. 2.21–2.22]"),
        ("O que caracterizou o trabalho compulsório na América Portuguesa e como evoluiu?",
         "Início: escravidão indígena. Substituída progressivamente pela escravidão africana (séc. XVI–XVII) por pressão jesuíta e lucratividade do tráfico atlântico. [Fausto, Cap. 2.8]"),
        ("Qual foi o papel dos Tratados de Madri (1750) e Santo Ildefonso (1777) na formação do território?",
         "Madri: reconheceu o uti possidetis (posse efetiva), ampliando o Brasil além de Tordesilhas. Ildefonso: reajustou limites com Espanha. [Ricupero, Parte I]"),
        ("O que foi a Inconfidência Mineira (1789) e por que fracassou?",
         "Conspiração em Vila Rica contra o domínio português, inspirada no Iluminismo e na independência americana. Delatada por Silvério dos Reis; Tiradentes foi executado. [Fausto, Cap. 2.24.1]"),
        ("O que foi a Conjuração dos Alfaiates (1798) na Bahia?",
         "Revolta de caráter popular e racial em Salvador: artesãos, soldados e negros libertos pediam fim da escravidão, república e igualdade racial. [Fausto, Cap. 2.24.2]"),
        ("Qual a diferença social entre senhores de engenho, homens livres pobres e escravos no Brasil colonial?",
         "Senhores: elite fundiária branca. Livres pobres: sem acesso à terra, dependentes dos grandes proprietários. Escravos: base da força de trabalho, sem direitos. [Fausto, Cap. 2.15]"),
        ("Como a administração pombalina (1750–1777) reformou as relações metrópole-colônia?",
         "Expulsou os jesuítas (1759), reforçou o monopólio comercial, modernizou a administração e transferiu a capital colonial para Belém do Grão-Pará (norte). [Fausto, Cap. 2.23.1]"),
        ("Qual a importância das invasões holandesas (1624–1654) para a história colonial?",
         "Holanda controlou o Nordeste açucareiro por 30 anos. A reconquista portuguesa (com apoio luso-brasileiro) consolidou a identidade colonial e o domínio no tráfico de escravos. [Fausto, Cap. 2.18]"),
    ]
)

# ─── 2. PROCESSO DE INDEPENDÊNCIA ─────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Processo de Independência",
    f"{BASE}/processo_independencia_hb.apkg",
    [
        ("Por que a Família Real portuguesa transferiu-se para o Brasil em 1808?",
         "Fuga diante da invasão napoleônica de Portugal (nov. 1807). Escolta da frota britânica; chegou ao Rio em mar. 1808. [Fausto, Cap. 2.25; Ricupero, Parte II]"),
        ("Quais os efeitos imediatos da chegada da Corte ao Rio de Janeiro?",
         "Abertura dos portos às nações amigas (1808); criação do Banco do Brasil, Academia Militar, Imprensa Régia; elevação ao Reino Unido (1815). [Fausto, Cap. 2.25.1–2]"),
        ("O que foi a Revolução do Porto (1820) e como afetou o Brasil?",
         "Revolução liberal em Portugal exigiu retorno de D. João VI e constituição. Pressionou a Coroa, acelerando a crise que levou à independência. [Fausto, Cap. 2.26; Cervo/Bueno, pp. 16-23]"),
        ("O que foi o 'Dia do Fico' (9 jan. 1822) e qual seu significado?",
         "D. Pedro I recusou retornar a Portugal conforme exigência das Cortes. Marcou a ruptura política e o início do processo formal de independência. [Fausto, Cap. 2.26]"),
        ("Quais as principais influências ideológicas do processo de independência brasileiro?",
         "Iluminismo, liberalismo inglês, Independência americana (1776) e Revolução Francesa (1789). Adaptadas pela elite luso-brasileira de forma conservadora. [Fausto, Cap. 2.22.1]"),
        ("Como foi o Constitucionalismo português e sua relação com a independência do Brasil?",
         "Cortes de Lisboa (1821) elaboraram constituição liberal, mas queriam rebaixar o Brasil a colônia. Reação gerou apoio à independência e ao projeto de Pedro I. [Cervo/Bueno, pp. 23-42]"),
        ("Quais os principais movimentos emancipacionistas que precederam a independência?",
         "Inconfidência Mineira (1789), Conjuração dos Alfaiates (1798), Revolução Pernambucana (1817) — todos reprimidos, mas semearam consciência autonomista. [Fausto, Cap. 2.24]"),
        ("O que foi a Revolução Pernambucana de 1817?",
         "Revolta republicana no Nordeste, liderada por padres e proprietários. Proclamou república breve; reprimida por D. João VI em 3 meses. [Fausto, Cap. 2.25.3]"),
        ("Como foi o reconhecimento internacional da independência do Brasil?",
         "EUA: 1824 (1º). Portugal: 1825, com pagamento de indenização (£2 mi) e concessão de título imperial. Reino Unido mediou o acordo e tinha interesses comerciais. [Cervo/Bueno, pp. 27-50; Ricupero, pp. 91-130]"),
        ("O que caracterizou o modelo de independência do Brasil em relação à América Espanhola?",
         "Independência conservadora: sem guerra prolongada, manteve monarquia, escravidão e estrutura fundiária. Evitou fragmentação territorial dos vizinhos hispânicos. [Fausto, Cap. 2.26; Cervo/Bueno, p. 50]"),
    ]
)

# ─── 3. PRIMEIRO REINADO (1822–1831) ──────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Primeiro Reinado 1822-1831",
    f"{BASE}/primeiro_reinado_hb.apkg",
    [
        ("Quais as principais características da Constituição de 1824?",
         "Outorgada por D. Pedro I. Criou o Poder Moderador (acima dos 3 poderes). Monarquia constitucional hereditária, voto censitário, catolicismo como religião oficial. [Fausto, Cap. 3.4]"),
        ("O que foi o Poder Moderador na Constituição de 1824 e por que era polêmico?",
         "4º poder, exercido pelo Imperador: nomear/demitir ministros, dissolver a Câmara, suspender decisões judiciais. Concentrava poder excessivo nas mãos de Pedro I. [Fausto, Cap. 3.4]"),
        ("O que foi a Confederação do Equador (1824) e qual seu desfecho?",
         "Revolta republicana e federalista no Nordeste (PE, CE, RN, PB), liderada por Frei Caneca. Reprimida pelo governo imperial; Frei Caneca fuzilado. [Fausto, Cap. 3.5]"),
        ("Quais as causas da abdicação de D. Pedro I em 1831?",
         "Desgaste com: guerra cisplatina (perda do Uruguai, 1828), impopularidade por nomear portugueses, crise econômica, autoritarismo e conflitos com a Assembleia. [Fausto, Cap. 3.6]"),
        ("Qual foi a política exterior do Primeiro Reinado em relação ao Rio da Prata?",
         "Brasil disputou a Banda Oriental (atual Uruguai) com as Províncias Unidas do Rio da Prata. Guerra (1825-28) terminou com o reconhecimento da independência do Uruguai. [Cervo/Bueno, pp. 93-132; Ricupero, pp. 140-170]"),
        ("Como a questão da Cisplatina (Uruguai) influenciou a política interna do Primeiro Reinado?",
         "A derrota militar e a perda do território cisplatino (1828) enfraqueceu Pedro I internamente, acelerando a oposição que culminou em sua abdicação em 1831. [Fausto, Cap. 3.6]"),
        ("Qual foi o papel da Assembleia Constituinte de 1823 e por que foi dissolvida?",
         "Eleita para redigir a constituição. Dissolvida por Pedro I em nov. 1823 ao apresentar projeto que limitava seus poderes (A. Constituinte 'da mandioca'). [Fausto, Cap. 3.3]"),
        ("Quais as principais tensões políticas internas do Primeiro Reinado?",
         "Conflito entre: absolutistas (Pedro I) × liberais (Constituinte); brasileiros natos × portugueses; centro × províncias. Imprensa livre amplificava os conflitos. [Fausto, Cap. 3.2-3.4]"),
        ("Qual foi o saldo territorial da política exterior do Primeiro Reinado?",
         "Negativo: perda da Cisplatina (Uruguai). Positivo: reconhecimento internacional da independência. O Brasil sai menor, mas internacionalmente reconhecido. [Ricupero, pp. 130-145]"),
    ]
)

# ─── 4. REGÊNCIA (1831–1840) ───────────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Regência 1831-1840",
    f"{BASE}/regencia_hb.apkg",
    [
        ("O que foi o período Regencial (1831–1840) e quais suas fases?",
         "Governo em nome de Pedro II (menor de idade). Fases: Regência Trina (1831-34), Una Permanente (1834-40). Marcado por revoltas e debate centralização × descentralização. [Fausto, Cap. 4]"),
        ("O que foi o Ato Adicional de 1834 e quais suas principais mudanças?",
         "Reforma constitucional: criou Assembleias Provinciais, extinguiu Conselho de Estado, substituiu Regência Trina pela Una. Tendência descentralizadora. [Fausto, Cap. 4.1]"),
        ("O que foi a Interpretação do Ato Adicional (1840) e qual seu efeito político?",
         "Lei que reinterpretou o Ato de 1834 de modo centralizador. Precedeu o 'Golpe da Maioridade', permitindo centralização antes de Pedro II completar 18 anos. [Fausto, Cap. 4.1]"),
        ("Quais as principais revoltas provinciais do período Regencial e suas causas?",
         "Cabanagem (PA/AM), Balaiada (MA), Sabinada (BA), Farroupilha (RS) — mistura de insatisfação social, federalismo e crise econômica. [Fausto, Cap. 4.2]"),
        ("O que foi a Guerra dos Farrapos (1835–1845) no Rio Grande do Sul?",
         "Revolta separatista de estancieiros gaúchos contra impostos imperiais sobre o charque. Proclamou a República Rio-Grandense. Encerrada pelo Duque de Caxias (1845). [Fausto, Cap. 4.2.2]"),
        ("O que foi o 'Golpe da Maioridade' (1840)?",
         "Antecipação da maioridade de Pedro II (14 anos) pelo Parlamento, pondo fim à Regência. Articulado pelos liberais para acabar com a instabilidade política. [Fausto, Cap. 4.3]"),
        ("Quais os principais partidos políticos que emergiram na Regência?",
         "Partido Liberal (descentralistas, federalistas) × Partido Conservador (centralistas, monarquistas). Disputa moldou a política do II Reinado. [Fausto, Cap. 4.3]"),
        ("Qual foi a dimensão externa do período Regencial?",
         "Brasil negociou fim do tráfico de escravos com a GB (Tratado Husskinson, 1826/Lei Eusébio de Queiroz 1850). Relações externas instáveis por fragilidade interna. [Cervo/Bueno, pp. 133-160]"),
        ("Como o debate centralização × descentralização se manifestou na Regência?",
         "Liberais: federalismo + mais poder às províncias. Conservadores: unidade nacional + Poder Moderador. O equilíbrio centralista venceu com o II Reinado. [Fausto, Cap. 4.1; 4.3]"),
    ]
)

# ─── 5. SEGUNDO REINADO (1840–1889) ───────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Segundo Reinado 1840-1889",
    f"{BASE}/segundo_reinado_hb.apkg",
    [
        ("Como funcionava o sistema político do Segundo Reinado?",
         "Monarquia parlamentarista com o Poder Moderador. Pedro II alternava liberais e conservadores no poder ('parlamentarismo às avessas'). Coronelismo nas províncias. [Fausto, Cap. 5.1-5.4]"),
        ("Quais as características da economia cafeeira do Segundo Reinado?",
         "Expansão do café do Vale do Paraíba para o Oeste Paulista. Trabalho escravo → imigração europeia (subsidiada). Latifúndio, monocultura, dependência do mercado externo. [Fausto, Cap. 5.6.1]"),
        ("Como foi abolido o tráfico de escravos no Brasil (1850)?",
         "Lei Eusébio de Queiroz (1850): proibiu o tráfico transatlântico sob pressão inglesa (navios britânicos abordavam navios negreiros). Escravidão interna continuou por 38 anos. [Fausto, Cap. 5.6.2]"),
        ("O que foi a Guerra do Paraguai (1864–1870) e suas consequências?",
         "Tríplice Aliança (Brasil, Argentina, Uruguai) × Paraguai. Maior guerra sul-americana: ~300 mil mortos paraguaios. Brasil saiu endividado; exército fortalecido. [Fausto, Cap. 5.7]"),
        ("Quais as causas da crise do Estado monárquico nos anos 1870–1889?",
         "Questão militar (status do exército), questão religiosa (conflito Maçonaria-Igreja), questão abolicionista. Abolição da escravidão (1888) alienou a elite rural. [Fausto, Cap. 5.8]"),
        ("O que foi a Lei do Ventre Livre (1871) e a Lei dos Sexagenários (1885)?",
         "Ventre Livre: filhos de escravas nascem livres (mas servem até 21 anos). Sexagenários: liberta escravos acima de 60 anos (com indenização ao senhor). Passos graduais à abolição. [Fausto, Cap. 5.8.1]"),
        ("Quando e como foi abolida a escravidão no Brasil?",
         "Lei Áurea (13 mai. 1888): abolição incondicional, sem indenização aos proprietários. Assinada pela Princesa Isabel. Reação dos fazendeiros contribuiu para a queda da monarquia. [Fausto, Cap. 5.8.1-5.8.2]"),
        ("Qual foi a política exterior do Segundo Reinado em relação ao Rio da Prata?",
         "Intervenções no Uruguai (1864) e Guerra do Paraguai (1864-70). Pós-guerra: negociações de paz; Brasil ficou sem ganhos territoriais significativos. [Cervo/Bueno, pp. 126-160]"),
        ("Qual o papel do Barão do Rio Branco na diplomacia do Segundo Reinado?",
         "Filho de Paranhos, iniciou a carreira como cônsul. Defendeu o Brasil em arbitragens de fronteira (Missões, 1895; Amapá, 1900). Rio Branco começou no Império. [Ricupero, pp. 233-253]"),
        ("Quais foram as manifestações culturais e científicas do Segundo Reinado?",
         "Romantismo literário (José de Alencar, Gonçalves Dias), Escola Recife (positivismo), fundação do IHGB (1838), Abolicionismo intelectual (Nabuco, Patrocínio). [Fausto, Cap. 5.9]"),
        ("O que foi a Proclamação da República (15 nov. 1889)?",
         "Golpe militar liderado por Deodoro da Fonseca. Pedro II foi exilado sem resistência. Causas: crise da monarquia, fortalecimento do exército, insatisfação dos fazendeiros. [Fausto, Cap. 5.8.9]"),
    ]
)

# ─── 6. PRIMEIRA REPÚBLICA (1889–1930) ────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Primeira República 1889-1930",
    f"{BASE}/primeira_republica_hb.apkg",
    [
        ("Quais as principais características da Constituição de 1891?",
         "Federalismo, presidencialismo, separação Estado-Igreja, voto masculino (exceto analfabetos), fim do Poder Moderador. Modelo americano adaptado. [Fausto, Cap. 6.1]"),
        ("O que foi a 'Política dos Governadores' (ou 'política dos estados')?",
         "Acordo de Campos Sales (1898): presidente apoia oligarquias estaduais, que em troca sustentam o governo federal. Base do coronelismo e do clientelismo republicano. [Fausto, Cap. 6.7.1]"),
        ("O que foi o coronelismo na Primeira República?",
         "Sistema de poder local baseado no 'coronel' (grande proprietário) que controlava votos, empregos e favores em troca de apoio político ao governo estadual e federal. [Fausto, Cap. 6.8.2]"),
        ("Quais os principais feitos diplomáticos do Barão do Rio Branco (1902–1912)?",
         "Resolveu 7 disputas de fronteira: Missões (árbitro Cleveland, 1895), Amapá (árbitro suíço, 1900), Acre (Tratado de Petrópolis, 1903), fronteiras com Colômbia, Venezuela, Holanda. [Cervo/Bueno, pp. 192-215; Ricupero, pp. 276-330]"),
        ("O que foi o Tratado de Petrópolis (1903) sobre o Acre?",
         "Brasil comprou o Acre da Bolívia por £2 mi e compensações territoriais. Rio Branco conduziu as negociações; território rico em borracha foi incorporado ao Brasil. [Cervo/Bueno, p. 203; Ricupero, p. 297]"),
        ("Qual foi a participação do Brasil na I Guerra Mundial (1914–1918)?",
         "Inicialmente neutro; após afundamento de navios por submarinos alemães, declarou guerra à Alemanha (1917). Enviou missão naval (DNOG) e missão médica. [Fausto, Cap. 6.10.7; Cervo/Bueno, pp. 228-243]"),
        ("Qual foi o papel do Brasil na II Conferência de Paz da Haia (1907) e na Liga das Nações?",
         "Haia: Rui Barbosa defendeu igualdade entre nações (sem distinção entre grandes e pequenas). Liga das Nações: Brasil foi membro fundador, pleiteou assento permanente e saiu em 1926. [Cervo/Bueno, pp. 243-254]"),
        ("O que foi o tenentismo nos anos 1920?",
         "Movimento de jovens oficiais do Exército contra a oligarquia. Revoltas: Forte de Copacabana (1922), Coluna Prestes (1924-27). Questionavam a ordem política da República Velha. [Fausto, Cap. 6.12.1]"),
        ("O que foi a Semana de Arte Moderna (1922) e qual seu significado?",
         "Evento em SP que rompeu com o academicismo: Modernismo brasileiro. Oswald de Andrade, Mário de Andrade, Villa-Lobos. Influenciou política e cultura da Era Vargas. [Fausto, Cap. 6.11]"),
        ("Quais as causas imediatas da Revolução de 1930?",
         "Rompimento do pacto SP-MG: Getúlio Vargas (RS/MG) foi preterido por Júlio Prestes (SP). Aliança Liberal + tenentes + exército: golpe derrubou Washington Luís. [Fausto, Cap. 6.13]"),
        ("O que foi a política de valorização do café na Primeira República?",
         "Governos compravam café excedente para sustentar preços (Convênio de Taubaté, 1906). Beneficiou fazendeiros paulistas; criou dívida externa e dependência monoprodutora. [Fausto, Cap. 6.9]"),
        ("Qual foi a evolução demográfica e migratória da Primeira República?",
         "Grande imigração europeia (italianos, espanhóis, alemães, japoneses): +4 milhões entre 1880-1930. Concentrada em SP e RS. Transformou mercado de trabalho e urbanização. [Fausto, Cap. 6.10.1]"),
    ]
)

# ─── 7. ERA VARGAS (1930–1945) ─────────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Era Vargas 1930-1945",
    f"{BASE}/era_vargas_hb.apkg",
    [
        ("Quais as fases políticas da Era Vargas (1930–1945)?",
         "Governo Provisório (1930-34), Governo Constitucional (1934-37), Estado Novo (1937-45). Concentração progressiva de poder em Getúlio Vargas. [Fausto, Cap. 7]"),
        ("O que foi a Constituição de 1934 e qual seu caráter?",
         "Liberal-social: introduziu voto feminino, voto secreto, Justiça Eleitoral, direitos trabalhistas. Influenciada pelo constitucionalismo europeu pós-WWI (Weimar). [Fausto, Cap. 7.6.3]"),
        ("O que foi o Estado Novo (1937–1945) e qual a Constituição de 1937?",
         "Ditadura implantada por Vargas com apoio do Exército. Constituição 'polaca' (inspirada no fascismo polonês): centralizou poder, fechou parlamento, proibiu partidos. [Fausto, Cap. 7.8]"),
        ("O que foi o Integralismo no Brasil dos anos 1930?",
         "Movimento fascista de Plínio Salgado (AIB): uniformes verdes, sigma como símbolo, anti-semitismo, autoritarismo. Tentativa de golpe contra Vargas (1938) fracassou. [Fausto, Cap. 7.7.1]"),
        ("Quais os pilares da legislação trabalhista varguista?",
         "CLT (1943), carteira de trabalho, salário mínimo, férias, jornada de 8h, sindicatos atrelados ao Estado (peleguismo). Vargas como 'pai dos pobres'. [Fausto, Cap. 7.4; 7.8.2]"),
        ("Como foi a industrialização durante o Estado Novo?",
         "ISI (Industrialização por Substituição de Importações): Volta Redonda (CSN, 1941), Vale do Rio Doce (CVRD, 1942). Papel central do Estado no desenvolvimento industrial. [Fausto, Cap. 7.9.3]"),
        ("Qual foi a posição do Brasil no início da II Guerra Mundial?",
         "Neutralidade oportunista até 1942: Vargas negociou com EUA (bases em Natal) e Alemanha (financiamento de Volta Redonda). Afundamento de navios (1942) precipitou a entrada. [Cervo/Bueno, pp. 273-292]"),
        ("Como e quando o Brasil entrou na II Guerra Mundial?",
         "Agosto-setembro 1942: submarinos alemães afundaram navios brasileiros, matando +600 civis. Brasil declarou guerra ao Eixo; FEB lutou na Itália (1944-45). [Fausto, Cap. 7.8.4; Cervo/Bueno, p. 273]"),
        ("O que foi a Revolução Constitucionalista de 1932?",
         "Revolta de SP contra o governo provisório de Vargas: exigia constituição e eleições. Derrota militar em 3 meses, mas Vargas convocou Constituinte em 1933. [Fausto, Cap. 7.6.2]"),
        ("Como terminou o Estado Novo e o que foi a 'redemocratização' de 1945?",
         "Pressão interna e desgaste com a guerra: Vargas convocou eleições, anistiou presos. Exército o depôs em out. 1945. Eleições deram vitória a Dutra (PSD). [Fausto, Cap. 7.8.4]"),
        ("Qual foi a política externa do Estado Novo?",
         "Equidistância pragmática: Vargas negociou simultaneamente com EUA e Alemanha. Alinhamento com EUA após Pearl Harbor (1941) em troca de financiamento industrial. [Cervo/Bueno, pp. 268-292]"),
    ]
)

# ─── 8. REPÚBLICA LIBERAL (1945–1964) ─────────────────────────────────────
make_deck(
    "CACD · História do Brasil · República Liberal 1945-1964",
    f"{BASE}/republica_liberal_hb.apkg",
    [
        ("Quais os principais partidos políticos criados em 1945 e suas bases?",
         "PSD (elites rurais varguistas), UDN (liberais antivarguistas, classe média urbana), PTB (trabalhadores, legado Vargas). Tripartismo estruturou a política 1945-64. [Fausto, Cap. 8.1-8.2]"),
        ("Quais as principais características da Constituição de 1946?",
         "Democrática e liberal: restabeleceu direitos civis, autonomia dos estados, voto universal (exceto analfabetos), pluripartidarismo, federalismo. [Fausto, Cap. 8.2]"),
        ("O que foi a Operação Pan-Americana (OPA, 1958) proposta por JK?",
         "Iniciativa de Juscelino Kubitschek: desenvolvimento econômico como solução ao comunismo na AL. Precursora da Aliança para o Progresso. EUA resistiram inicialmente. [Cervo/Bueno, pp. 313-334; Ricupero, pp. 387-415]"),
        ("O que foi o Programa de Metas de JK (1956–1960)?",
         "50 anos em 5: 31 metas industriais, construção de Brasília. Modelo desenvolvimento + abertura ao capital estrangeiro. Crescimento ~8% ao ano; inflação crescente. [Fausto, Cap. 8.6.2]"),
        ("O que foi a Política Externa Independente (PEI, 1961–1964)?",
         "Governo Jânio/Goulart: aproximação com países socialistas, defesa da autodeterminação, anticolonialismo, não-alinhamento. Ruptura com alinhamento automático com EUA. [Cervo/Bueno, pp. 336-410; Ricupero, pp. 419-470]"),
        ("Por que Jânio Quadros renunciou à presidência em 1961?",
         "25 ago. 1961: renúncia por 'forças ocultas' (motivo obscuro). Possivelmente calculou que o Congresso rejeitaria. Abriu crise com Goulart (vice) e militares. [Fausto, Cap. 8.8.3]"),
        ("O que foi o Parlamentarismo (1961–1963) no governo Goulart?",
         "Solução de compromisso para permitir posse de Goulart (resistido pelos militares). Goulart como presidente com poderes limitados; PM eleito pelo Congresso. Revogado em plebiscito (jan. 1963). [Fausto, Cap. 8.10.7-8]"),
        ("Qual foi a posição do Brasil em relação a Cuba na OEA (1962)?",
         "San Tiago Dantas tentou posição intermediária. Brasil se absteve na votação de expulsão de Cuba da OEA em Punta del Este. Gerou desgaste interno e com EUA. [Cervo/Bueno, pp. 348-364; Ricupero, pp. 424-436]"),
        ("O que foram as 'Reformas de Base' de Goulart e por que geraram crise?",
         "Reforma agrária, reforma urbana, nacionalização de refinarias, reforma universitária. Polarizaram: esquerda via como mínimo; direita e militares como comunismo. [Fausto, Cap. 8.10.4]"),
        ("Como os EUA se relacionaram com o Brasil no contexto da Guerra Fria (1945-64)?",
         "Dutra: alinhamento total. Vargas (1950-54): tensão (Petrobrás). JK: parceria com OPA. Goulart: desconfiança crescente; EUA apoiaram o golpe de 1964. [Cervo/Bueno, pp. 293-410]"),
        ("O que foi o Golpe de 1964 e quais suas causas imediatas?",
         "31 mar./1 abr. 1964: militares derrubaram Goulart. Causas: medo do comunismo, polarização política, discurso de Goulart no Automóvel Clube, motim dos marinheiros. [Fausto, Cap. 8.10.9]"),
    ]
)

# ─── 9. REGIME MILITAR (1964–1985) ────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Regime Militar 1964-1985",
    f"{BASE}/regime_militar_hb.apkg",
    [
        ("Quais os Atos Institucionais mais importantes do Regime Militar e seus efeitos?",
         "AI-1 (1964): cassações. AI-2 (1965): extinção dos partidos, bipartidarismo ARENA/MDB. AI-5 (1968): suspendeu habeas corpus, permitiu cassações em massa. [Fausto, Cap. 9.1; 9.3.3]"),
        ("O que foi o AI-5 (1968) e qual seu impacto?",
         "Ato mais duro do regime: fechou o Congresso, suspendeu garantias individuais, permitiu censura total. Inaugurou os 'anos de chumbo' (1968-74). [Fausto, Cap. 9.3.3]"),
        ("O que foi a Constituição de 1967 e a Emenda de 1969?",
         "CF/1967: concentrou poder no executivo, legitimou o regime. EC nº 1/1969: praticamente nova constituição, aumentou penas para crimes políticos, institucionalizou repressão. [Fausto, Cap. 9.2.2]"),
        ("O que foi o 'Milagre Econômico' (1968–1973)?",
         "Crescimento médio de 10% ao ano: industrialização pesada, grandes obras (Transamazônica, Itaipu), crédito fácil. Sustentado por endividamento externo e repressão política. [Fausto, Cap. 9.5.3]"),
        ("O que foi o 'Pragmatismo Responsável' na política externa do regime militar?",
         "Governo Geisel/Azeredo da Silveira (1974-79): diversificação de parceiros (China, URSS, África, Oriente Médio), independência relativa dos EUA, busca de mercados para exportações. [Cervo/Bueno, pp. 442-475]"),
        ("Quais foram as relações do Brasil com a África durante o regime militar?",
         "Abertura na era Geisel: reconhecimento do MPLA em Angola (1975), relações com Moçambique e outros Estados africanos. Ruptura com Portugal salazarista e aproximação com ex-colônias. [Cervo/Bueno, pp. 462-474]"),
        ("O que foi a luta armada contra o regime militar (1968–1974)?",
         "Organizações como ALN (Carlos Marighella), MR-8, VPR: guerrilha urbana, sequestros de embaixadores. Reprimidas com tortura pelo DOI-CODI; derrotadas até 1974. [Fausto, Cap. 9.3.2; 9.5.1]"),
        ("O que foi a 'abertura lenta, gradual e segura' de Geisel?",
         "1974-79: revogação gradual das medidas mais duras; eleições para o MDB (1974 com grande vitória oposicionista); Lei da Anistia (1979); fim do bipartidarismo. [Fausto, Cap. 9.6.1-9.6.2]"),
        ("O que foi a Lei da Anistia (1979) e quais suas limitações?",
         "Anistiou presos políticos e exilados, mas também agentes do Estado que cometeram tortura ('crimes conexos'). Impede até hoje punição de torturadores do regime. [Fausto, Cap. 9.7.2]"),
        ("O que foi a campanha 'Diretas Já' (1983–1984)?",
         "Maior mobilização popular da história do Brasil: milhões nas ruas pedindo eleição direta para presidente. Emenda Dante de Oliveira foi derrotada no Congresso (abril 1984). [Fausto, Cap. 9.7.3]"),
        ("Como terminou o Regime Militar e quem foi eleito no Colégio Eleitoral (1985)?",
         "Tancredo Neves (PMDB) eleito indiretamente pelo Colégio Eleitoral em jan. 1985. Morreu antes da posse; José Sarney assumiu. Fim formal do regime em 15 mar. 1985. [Fausto, Cap. 9.7.4; 9.9]"),
    ]
)

# ─── 10. PROCESSO DEMOCRÁTICO A PARTIR DE 1985 ────────────────────────────
make_deck(
    "CACD · História do Brasil · Processo Democrático a partir de 1985",
    f"{BASE}/processo_democratico_hb.apkg",
    [
        ("Quais as principais características da Constituição de 1988?",
         "Constituição Cidadã: amplos direitos sociais e individuais, SUS, Previdência Social, democracia participativa (plebiscitos, referendos), autonomia municipal, STF fortalecido. [Fausto, Cap. 10.4]"),
        ("O que foi o Plano Cruzado (1986) e por que fracassou?",
         "Congelamento de preços e salários para combater inflação inercial. Funcionou por 8 meses; pressão de demanda e falta de ajuste fiscal levaram à explosão inflacionária em 1987. [Fausto, Cap. 10.1-10.2]"),
        ("Quais os planos econômicos anti-inflacionários do período 1986–1994 e seus resultados?",
         "Cruzado (1986), Bresser (1987), Verão (1989), Collor I e II (1990-91): todos fracassaram. Plano Real (1994): único a debelar a inflação de forma duradoura. [Cervo/Bueno, pp. 509-530]"),
        ("O que foi o Plano Real (1994) e como funcionou?",
         "Ministro FHC: desindexação, âncora cambial (R$ = US$), abertura comercial. Derrubou inflação de ~50%/mês para menos de 1%. Base eleitoral de FHC. [Cervo/Bueno, p. 517]"),
        ("O que foi o impeachment de Collor (1992) e qual sua importância histórica?",
         "Fernando Collor renunciou antes da votação do impeachment (dez. 1992) por corrupção (PC Farias). 1ª vez na história brasileira que presidente foi afastado por processo constitucional. [Fausto, Cap. 12]"),
        ("Como evoluiu a política externa do Brasil a partir de 1985?",
         "Sarney: reaproximação com Argentina (PICE/1986). FHC: autonomia pela participação (multilateralismo, TNP). Lula: protagonismo Sul-Sul, BRICS, IBAS. [Cervo/Bueno, pp. 540-585; Ricupero, pp. 609-660]"),
        ("O que foi o MERCOSUL, quando foi criado e quais seus objetivos?",
         "Criado pelo Tratado de Assunção (1991): Argentina, Brasil, Uruguai e Paraguai. Objetivo: união aduaneira, livre circulação de bens, serviços e fatores de produção. [Cervo/Bueno, pp. 572-580]"),
        ("Qual foi o papel do Brasil na ONU a partir de 1985?",
         "Candidatura ao assento permanente no CS (reforma da ONU), participação em operações de paz (MINUSTAH no Haiti, 2004-2017), defesa do multilateralismo. [Cervo/Bueno, pp. 549-572]"),
        ("Quais as transformações econômicas dos anos 1990 no Brasil?",
         "Abertura comercial (Collor), privatizações (CSN, CVRD, telecomunicações, energia), Plano Real, Lei de Responsabilidade Fiscal (2000). Fim do modelo ISI. [Cervo/Bueno, pp. 509-540]"),
        ("Quais as mudanças sociais mais significativas no Brasil pós-1985?",
         "Redemocratização, Constituição de 1988 (direitos sociais), Bolsa Família (2003), aumento da classe média, expansão da educação superior (PROUNI, REUNI), queda da desigualdade (Gini). [Fausto, Cap. 12]"),
        ("O que foi o governo Lula (2003–2010) em termos de política externa?",
         "Diplomacia protagônica: BRICS, IBAS, G-20 comercial, UNASUL, relações Sul-Sul. FHC havia aderido ao TNP; Lula buscou assento permanente na ONU. [Ricupero, pp. 639-660]"),
    ]
)

# ─── 11. SÉCULO XXI ────────────────────────────────────────────────────────
make_deck(
    "CACD · História do Brasil · Século XXI",
    f"{BASE}/seculo_xxi_hb.apkg",
    [
        ("Como as redes sociais transformaram a política brasileira no século XXI?",
         "Mobilizações de 2013 (Jornadas de Junho) foram organizadas via Facebook/WhatsApp. Em 2018, WhatsApp foi vetor de fake news na campanha eleitoral de Bolsonaro. [Cervo/Bueno, pp. 549ss.]"),
        ("O que foram as Jornadas de Junho de 2013 e qual seu legado político?",
         "Protestos que começaram contra aumento do transporte em SP; se espalharam pelo país, pedindo melhores serviços públicos. Fragmentaram o PT e aceleraram a crise política. [Fausto, Cap. 12]"),
        ("O que foi a Operação Lava Jato (2014–2021) e seu impacto político-social?",
         "Maior investigação de corrupção do Brasil: desmantelou esquemas na Petrobras; prendeu Lula (2018); elegeu Bolsonaro indiretamente. Questionada por parcialidade do juiz Moro. [contexto contemporâneo]"),
        ("O que foi o impeachment de Dilma Rousseff (2016) e qual sua justificativa?",
         "Afastada por 'pedaladas fiscais' (manipulação de contas públicas). Contexto: recessão, escândalo da Lava Jato, polarização política. Michel Temer assumiu. [contexto contemporâneo]"),
        ("Quais os impactos da pandemia de Covid-19 (2020–2022) no Brasil?",
         "~700 mil mortos (2ª maior em números absolutos no mundo). CPI da Covid revelou irregularidades na vacinação. PIB caiu 4,1% em 2020; Auxílio Emergencial sustentou pobres. [contexto contemporâneo]"),
        ("Como a transformação digital afetou a economia e a sociedade brasileira no séc. XXI?",
         "Plataformização do trabalho (Uber, iFood), PIX como sistema de pagamentos instantâneos (2020), expansão do e-commerce, desafios para tributação e regulação de Big Techs. [contexto contemporâneo]"),
        ("Qual foi a evolução da política externa brasileira nos governos do século XXI?",
         "Lula I-II (2003-10): ativismo Sul-Sul. Dilma (2011-16): retração. Temer (2016-18): ocidentalização. Bolsonaro (2019-22): alinhamento EUA/Israel, afastamento de multilaterais. Lula III (2023+): retorno ao multilateralismo. [Ricupero, pp. 639-660]"),
        ("O que é o BRICS e qual o papel do Brasil?",
         "Grupo criado em 2009 (Brasil, Rússia, Índia, China, África do Sul). Brasil como voz do Sul Global. Agenda: reforma do FMI/Banco Mundial, moeda alternativa ao dólar. [Ricupero, pp. 642-660]"),
        ("Como as tecnologias digitais impactaram as eleições brasileiras?",
         "2014: primeiro uso massivo de WhatsApp em campanhas. 2018: disparos em massa de fake news. TSE regulamentou uso de IA em 2024. Debates sobre desinformação e democracia. [contexto contemporâneo]"),
    ]
)

print("\n🎉 Todos os 11 decks de História do Brasil criados com sucesso!")
