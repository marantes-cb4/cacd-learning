#!/usr/bin/env python3
"""Gera deck Anki — Economia: Governo Jânio Quadros e João Goulart (1961-1964).

Itens do edital: 4.5 Período 1962–1967 (parcial: falta PAEG).
Fonte: Anotações — Governo Jânio Quadros e João Goulart (sem material do professor).
"""
import genanki, random, os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/economia"
os.makedirs(DECK_DIR, exist_ok=True)


def make_deck(deck_title, file_name, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31), "CACD Direito Rodadas",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{"name": "Card", "qfmt": "{{Frente}}",
                    "afmt": "{{FrontSide}}<hr id=answer>{{Verso}}"}])
    deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_title)
    for f, v in cards:
        deck.add_note(genanki.Note(model=model, fields=[f, v]))
    genanki.Package(deck).write_to_file(f"{DECK_DIR}/{file_name}")
    print(f"✅ {file_name} — {len(cards)} cards")


F = "[Anotações da aula]"
CARDS = [
    ('O período de 1961 a 1965 combinou desaceleração do produto e da produção industrial com inflação crescente, configurando estagflação; a explicação de Jânio Quadros para esse quadro atribuía a deterioração do balanço de pagamentos à recessão herdada do governo JK.',
     f'<b>ERRADO.</b> A estagflação é correta, mas Jânio culpava JK por <b>aceleração inflacionária</b> (moeda emitida para financiar o Plano de Metas), <b>indisciplina fiscal</b> (dívida pública) e <b>deterioração do BP</b> causada pelo <b>aumento das importações</b> com o crescimento — não por recessão. Não havia recessão em 1961: o PIB crescera forte. {F}'),

    ('A Instrução 204 da SUMOC buscou desvalorizar o câmbio para reequilibrar o balanço de pagamentos e unificar o mercado cambial, indo além da simplificação de JK: a categoria geral foi para o mercado livre e restou uma categoria protegida para equipamentos e insumos intermediários da indústria.',
     f'<b>CERTO.</b> Os dois objetivos eram desvalorizar o câmbio (exportações mais atrativas) e unificar o mercado, acabando com as categorias de leilão. A categoria geral da reforma de JK migrou para o câmbio livre, preservando proteção só para bens ligados à industrialização. A armadilha é dizer que a Instrução 204 manteve o sistema de leilões. {F}'),

    ('Com a Instrução 204, a desvalorização do câmbio de custo das importações preferenciais barateou trigo e petróleo em cruzeiros, o que aliviou a inflação, enquanto as Letras de Importação passaram a substituir a postergação da entrega de divisas aos importadores.',
     f'<b>ERRADO.</b> O câmbio de custo era o mais baixo da economia; desvalorizá-lo <b>encareceu</b> trigo e petróleo em cruzeiros (dólar mais caro), pressionando preços. A segunda parte está certa: o importador passou a pagar as divisas e receber um <b>título</b> (letra de importação), em vez de esperar meses pelos dólares. {F}'),

    ('Instruções posteriores da SUMOC extinguiram o câmbio de custo e fixaram retenção por saca de café exportada, com exportação à taxa do mercado livre, o que na prática equivaleu a um novo imposto sobre o café.',
     f'<b>CERTO.</b> Todas as medidas da Instrução 204 e das posteriores visavam unificar o câmbio e torná-lo livre. A retenção por saca de café funcionou como tributo sobre o principal produto de exportação, e a exportação passou ao câmbio livre. Cuidado com a ideia de subsídio ao café: foi o oposto. {F}'),

    ('O governo Jânio obteve reescalonamento da dívida externa que vencia no início da década e adotou política externa independente, com aproximação da URSS, apoio à descolonização africana e recusa em endossar o isolamento de Cuba, sem que o programa de estabilização sobrevivesse à sua renúncia.',
     f'<b>CERTO.</b> Em 1961 houve sucesso com credores norte-americanos e europeus (novos empréstimos, adiamento de pagamentos e menor serviço da dívida). A política externa independente seguiu no gabinete de Tancredo Neves. Pela curta duração do mandato, o programa de estabilização caiu com a renúncia, em agosto de 1961. {F}'),

    ('No gabinete parlamentarista de Tancredo Neves, o programa do Ministro Moreira Salles foi concretamente implementado e ancorou-se em medidas fiscais detalhadas de contenção do déficit, o que explica os bons resultados de inflação em 1961-62.',
     f'<b>ERRADO.</b> O programa foi <b>extremamente genérico</b>, uma carta de intenções; as medidas de emergência e reformas institucionais <b>não foram implementadas</b> pela curta duração do gabinete. Moreira Salles era banqueiro, escolhido para tranquilizar conservadores. A inflação, aliás, subiu (47%) e o déficit público cresceu, puxado por RFFSA e Lloyd. {F}'),

    ('O programa do gabinete Tancredo Neves era contraditório na política cambial: defendia taxa única fixada em nível realista e, ao mesmo tempo, enfatizava manter o controle quantitativo de importações não essenciais.',
     f'<b>CERTO.</b> A contradição está em pregar câmbio único e realista e, ao mesmo tempo, restringir quantitativamente importações. Na monetária houve controles quantitativos de crédito e depósito compulsório sobre depósitos à vista de bancos privados. A banca pode inverter, dizendo que o programa abandonava controles quantitativos. {F}'),

    ('A deterioração das relações Brasil-EUA durante o parlamentarismo teve como um dos marcos uma nova lei de remessa de lucros, que dificultava o envio de lucros das empresas americanas ao exterior, além do cancelamento de concessões a certas companhias dos EUA.',
     f'<b>CERTO.</b> O governo manteve a política externa independente (não alinhamento e postura negativa a propostas dos EUA). A lei de remessa de lucros é aprovada nesse período, mas só foi <b>regulamentada em janeiro de 1964</b>, com limite de 10% do capital registrado — o que impedia remessa associada a reinvestimento. {F}'),

    ('O Plano Trienal combinou diagnóstico ortodoxo da inflação (gasto público e expansão monetária e creditícia) com diagnóstico estruturalista de causas de longo prazo combatidas por reformas de base, e a correção de tarifas públicas defasadas era inflacionária no curto prazo, mas reduziria a inflação futura ao diminuir o déficit das estatais.',
     f'<b>CERTO.</b> Idealizado por Celso Furtado (Planejamento) e Santiago Dantas (Fazenda), buscava agradar o FMI e renegociar a dívida externa. A inflação corretiva eleva preços agora, mas reduz o déficit das empresas públicas depois. Incluía fim de subsídios ao trigo e petróleo, corte do déficit, controle do crédito privado e alta do compulsório. {F}'),

    ('O fracasso do Plano Trienal decorreu do seu caráter excessivamente heterodoxo, com controle de preços e expansão do crédito, que gerou salto inflacionário imediato e levou Goulart a abandoná-lo ainda em 1962.',
     f'<b>ERRADO.</b> O plano era <b>ortodoxo</b> (corte de déficit, crédito restrito, fim de subsídios). Houve salto de preços por atacado após o anúncio, talvez por expectativa de controle de preços, e o crédito real caiu fortemente (recessão). Goulart reverteu a política só no <b>final de abril de 1963</b>, por pressão da esquerda e dos conservadores. {F}'),

    ('Ao reverter a política ortodoxa em 1963, Goulart reintroduziu subsídios ao trigo e ao petróleo, concedeu reajustes ao funcionalismo e ao salário mínimo e expandiu o crédito a partir de julho, o que reacelerou a inflação e contribuiu para o crescimento do produto praticamente nulo naquele ano.',
     f'<b>CERTO.</b> A reversão atendeu pressões trabalhistas e populistas, mas a inflação voltou a acelerar em junho de 1963 e o PIB cresceu apenas 0,6%. Antes, em 1962, a tentativa de conter a inflação já fora frustrada pelo 13º salário. O erro típico é associar a aceleração a corte de gastos. {F}'),

    ('No processo de substituição de importações descrito por Tavares, o estrangulamento externo era o motor dinâmico: a queda das exportações com renda doméstica mantida gerava demanda por bens industriais sem divisas para importá-los, e a proteção à indústria decorrente dos controles cambiais e tarifários era uma consequência não intencional, pelo menos no início.',
     f'<b>CERTO.</b> A proteção surgia como efeito colateral da contenção das importações. A industrialização de bens de consumo criava novo estrangulamento, pela necessidade de importar bens intermediários e de capital, reiniciando o ciclo em outros setores. A banca costuma tratar a proteção como política deliberada de industrialização desde o início. {F}'),

    ('Segundo a interpretação de Tavares, o PSI ocorreu em etapas rigidamente sequenciais, sem sobreposição entre setores, e a indústria de bens intermediários, por seus ganhos de escala, tendia a ser iniciada pelo setor privado, que antecipava a demanda.',
     f'<b>ERRADO.</b> As etapas (consumo leve, duráveis, depois intermediários e capital) indicam apenas a <b>predominância</b>: na prática os setores se substituem ao mesmo tempo. E os bens intermediários, com escala elevada, operam ociosos e com prejuízo no início; por isso o <b>Estado</b> costumava iniciá-los, assim como a infraestrutura. {F}'),

    ('Entre os problemas do PSI apontados por Furtado e Tavares estão a tecnologia poupadora de mão de obra numa economia dual com oferta abundante de trabalho, a concentração de renda limitando o mercado interno e a proteção prolongada que reduzia a competição e o esforço de ganho de produtividade.',
     f'<b>CERTO.</b> Em economia dual, equipamentos importados poupam trabalho em vez de gerar empregos, ampliando desigualdades. A renda concentrada barra os ganhos de escala. A proteção contínua gera indústria ineficiente. Soma-se a tese estruturalista da oferta agrícola insuficiente (latifúndio improdutivo) e a dependência financeira externa. {F}'),

    ('A tese estagnacionista (Furtado e Tavares) explica a desaceleração dos anos 60 pelo esgotamento do PSI, e a visão de Tavares de 1982 a rejeita ao atribuir a crise a um choque externo de estrangulamento, já que a economia teria permanecido na fase de industrialização restringida.',
     f'<b>ERRADO.</b> Em 1982 Tavares revisou suas teses: a economia já superara a industrialização restringida e tinha dinâmica de <b>inter-relações entre setores internos</b>. A crise decorreu da desaceleração do investimento em bens de capital, após o grande bloco de investimentos do Plano de Metas gerar <b>excesso de capacidade</b> à frente da demanda. Não era choque externo. {F}'),
]

if __name__ == "__main__":
    make_deck("REVIEW::Economia::Governo Jânio Quadros e João Goulart - Estagnação, inflação e ruptura (1961-1964)",
              "Economia - Governo Jânio Quadros e João Goulart - Estagnação, Inflação e Ruptura (1961-1964).apkg", CARDS)
