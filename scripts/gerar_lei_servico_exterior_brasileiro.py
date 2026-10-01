#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Junho/2024).

Tema: Regime Jurídico dos Servidores do Serviço Exterior Brasileiro
(Lei nº 11.440/2006) (Item 13 do Edital CACD).

Fontes:
  - Anotações: Lei do Serviço Exterior Brasileiro.md
  - Material do professor: Direito Interno_Rodada 01_Junho_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Junho_2024.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/direito interno"
os.makedirs(DECK_DIR, exist_ok=True)


def make_deck(deck_title, file_name, cards):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        "CACD Direito Rodadas",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card",
            "qfmt": "{{Frente}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Verso}}",
        }],
    )
    deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_title)
    for frente, verso in cards:
        deck.add_note(genanki.Note(model=model, fields=[frente, verso]))
    out = f"{DECK_DIR}/{file_name}"
    genanki.Package(deck).write_to_file(out)
    print(f"✅ {file_name} — {len(cards)} cards")


LEI_SERVICO_EXTERIOR_BRASILEIRO = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Caso um processo judicial seja instaurado no Brasil contra um integrante "
     "do Serviço Exterior Brasileiro que atue no exterior, a citação desse réu "
     "deverá ser feita, como regra, mediante carta rogatória expedida para "
     "cumprimento no Estado estrangeiro de sua residência.",
     "<b>ERRADO.</b> O art. 16, III, Lei 11.440/2006 assegura aos integrantes "
     "do SEB em serviço no exterior o direito de serem citados por "
     "<b>intermédio do MRE</b> — não por carta rogatória. Isso garante o "
     "exercício célere e efetivo da ampla defesa e do contraditório. "
     "[Anotações da aula; Rodada 01/Jun.2024]"),

    ("O processo administrativo disciplinar que tenha como parte um "
     "integrante do Serviço Exterior Brasileiro é instaurado pela "
     "Corregedoria do Serviço Exterior, que pode decidir pelo afastamento do "
     "servidor indiciado, inclusive com a suspensão de seus vencimentos e "
     "vantagens durante o afastamento.",
     "<b>ERRADO.</b> Arts. 31-32, Lei 11.440/2006 — o PAD é instaurado pela "
     "Corregedoria do Serviço Exterior, que designa comissão de <b>3 "
     "membros efetivos</b>, e PODE afastar o servidor indiciado, mas esse "
     "afastamento <b>NÃO</b> pode resultar em suspensão de vencimentos e "
     "vantagens. [Anotações da aula; Rodada 01/Jun.2024]"),

    ("A designação excepcional de brasileiro nato, maior de 35 anos, com "
     "reconhecido mérito e relevantes serviços prestados ao país, para atuar "
     "como chefe de missão diplomática permanente, pressupõe que esse "
     "indivíduo já integre os quadros do Ministério das Relações Exteriores "
     "como Ministro de Primeira ou Segunda Classe.",
     "<b>ERRADO.</b> Art. 41, parágrafo único, Lei 11.440/2006 — essa "
     "exceção se aplica justamente a quem <b>NÃO</b> pertence aos quadros do "
     "MRE (ex.: Itamar Franco, designado embaixador em Roma sem ser "
     "diplomata de carreira). É distinta da exceção do art. 46, §2º, que "
     "permite ao Conselheiro ser comissionado chefe de missão apenas em "
     "postos do grupo D. [Anotações da aula; Rodada 01/Jun.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jun/2024) ───────────────

    ("01-I – O princípio da especialidade não impede a aplicação da Lei nº "
     "8.112, de 11 de dezembro de 1990 (regime jurídico dos servidores "
     "públicos civis da União, das autarquias e das fundações públicas "
     "federais) aos integrantes do Serviço Exterior Brasileiro. (C/E?)",
     "<b>CERTO.</b> Art. 1º, parágrafo único, Lei 11.440/2006 — a Lei do "
     "SEB é lei especial, mas isso não afasta a aplicação da Lei 8.112/1990 "
     "(lei geral), havendo compatibilidade entre ambas. [Exercício Q01-I, "
     "Rodada 01 Jun/2024]"),

    ("01-II – A nomeação para qualquer cargo das carreiras do Serviço "
     "Exterior Brasileiro exige aprovação em concurso público de provas, ou "
     "de provas e títulos. (C/E?)",
     "<b>CERTO.</b> O ingresso em qualquer das 3 carreiras do SEB "
     "(diplomata, oficial e assistente de chancelaria) exige aprovação "
     "prévia em concurso público de provas ou de provas e títulos, como "
     "exige a CF/88 para cargo efetivo. [Exercício Q01-II, Rodada 01 "
     "Jun/2024]"),

    ("01-III – Diplomatas, oficiais de chancelaria e assistentes de "
     "chancelaria deverão solicitar autorização do Ministro de Estado das "
     "Relações Exteriores para casar com pessoa de nacionalidade "
     "estrangeira ou com pessoa empregada de governo estrangeiro ou que dele "
     "receba comissão ou pensão. (C/E?)",
     "<b>CERTO.</b> Arts. 33-34, Lei 11.440/2006 — dever imposto às 3 "
     "carreiras do SEB, cujo descumprimento pode acarretar demissão via "
     "PAD. [Exercício Q01-III, Rodada 01 Jun/2024]"),

    ("01-IV – Os postos no exterior serão classificados, para fins de "
     "movimentação de pessoal, em grupos A, B, C e D, segundo o grau de "
     "representatividade da missão, as condições específicas de vida na "
     "sede e a conveniência da Administração, exigindo-se lei para a "
     "classificação dos postos nesses grupos. (C/E?)",
     "<b>ERRADO.</b> Art. 13, §1º, Lei 11.440/2006 — a classificação dos "
     "postos em grupos A, B, C e D é feita por <b>ato do Ministro das "
     "Relações Exteriores</b>, não exigindo lei. [Exercício Q01-IV, Rodada "
     "01 Jun/2024]"),

    ("02-I – Os servidores integrantes da carreira de Oficial de "
     "Chancelaria, de nível superior, não têm a incumbência de desempenhar "
     "atividades de natureza diplomática e consular, em seus aspectos "
     "específicos de representação, negociação, informação e proteção de "
     "interesses brasileiros no campo internacional. (C/E?)",
     "<b>CERTO.</b> Art. 3º c/c art. 4º, Lei 11.440/2006 — essas atividades "
     "diplomáticas e consulares são atribuição exclusiva da carreira de "
     "<b>Diplomata</b>; ao Oficial de Chancelaria cabem atos de análise "
     "técnica e gestão administrativa da política externa. [Exercício "
     "Q02-I, Rodada 01 Jun/2024]"),

    ("02-II – De acordo com a CF/88, com exceção da carreira diplomática, "
     "os cargos do Serviço Exterior Brasileiro não são privativos de "
     "brasileiros natos. (C/E?)",
     "<b>CERTO.</b> Art. 12, §3º, CF/88 — apenas a carreira de Diplomata é "
     "privativa de brasileiro nato; Oficial e Assistente de Chancelaria "
     "podem ser ocupados também por brasileiros naturalizados. [Exercício "
     "Q02-II, Rodada 01 Jun/2024]"),

    ("02-III – Dentre os diplomatas de carreira, apenas os Ministros de "
     "Primeira Classe, Ministros de Segunda Classe e Conselheiros podem "
     "atuar como chefe de missão diplomática permanente. (C/E?)",
     "<b>CERTO.</b> Arts. 41 e 46, §2º, Lei 11.440/2006 — dentro da "
     "carreira diplomática, a regra geral reserva a chefia a Ministros de "
     "1ª/2ª Classe, e a única exceção interna à carreira é o Conselheiro "
     "comissionado, exclusivamente em postos do grupo D (a outra exceção da "
     "lei, do brasileiro nato de mérito, está FORA da carreira diplomática). "
     "[Exercício Q02-III, Rodada 01 Jun/2024]"),

    ("02-IV – Para a aquisição da vitaliciedade, o servidor nomeado para "
     "cargo inicial das carreiras do Serviço Exterior Brasileiro deverá ser "
     "submetido a estágio probatório de 03 (três) anos de efetivo exercício. "
     "(C/E?)",
     "<b>ERRADO.</b> Art. 8º, Lei 11.440/2006 — o estágio probatório de 3 "
     "anos de efetivo exercício, somado à avaliação especial de desempenho, "
     "é requisito para aquisição da <b>ESTABILIDADE</b>, não da "
     "vitaliciedade (instituto distinto, próprio de outras carreiras, como "
     "magistratura e MP). [Exercício Q02-IV, Rodada 01 Jun/2024]"),

    ("03-I – Cônjuge e filhos de qualquer condição, enteados e adotivos, que "
     "vivam na companhia do servidor do Serviço Exterior Brasileiro têm o "
     "direito à matrícula em estabelecimento de ensino oficial, "
     "independentemente de vaga, sempre que o servidor for removido de "
     "posto do exterior para o Brasil. (C/E?)",
     "<b>ERRADO.</b> Art. 15, Lei 11.440/2006 — esse direito só se aplica "
     "quando a remoção do exterior para o Brasil for <b>\"EX OFFICIO\"</b> "
     "(por determinação da Administração) — não vale para remoção a pedido "
     "do próprio servidor. [Exercício Q03-I, Rodada 01 Jun/2024]"),

    ("03-II – São deveres de todos os servidores do Serviço Exterior "
     "Brasileiro, no Brasil e no exterior, defender os interesses legítimos "
     "de seus subordinados, orientá-los no desempenho de suas tarefas, "
     "estimular-lhes espírito de iniciativa, disciplina e respeito ao "
     "patrimônio público. (C/E?)",
     "<b>ERRADO.</b> Art. 28, Lei 11.440/2006 — esse é dever específico do "
     "servidor <b>no exercício de função de chefia</b>, não de todos os "
     "servidores do SEB indistintamente. [Exercício Q03-II, Rodada 01 "
     "Jun/2024]"),

    ("03-III – Brasileiros e estrangeiros podem ser contratados para atuar "
     "como auxiliares locais no desempenho de serviços ou atividades de "
     "apoio que exijam familiaridade com as condições de vida, os usos e os "
     "costumes do país onde esteja sediado o posto, devendo as relações "
     "trabalhistas e previdenciárias ser regidas pela legislação vigente no "
     "país em que estiver sediada a repartição. (C/E?)",
     "<b>CERTO.</b> Arts. 56-57, Lei 11.440/2006 — auxiliares locais podem "
     "ser brasileiros ou estrangeiros, e suas relações trabalhistas e "
     "previdenciárias seguem a legislação local, salvo a exceção do art. "
     "57, §1º (brasileiro impedido de filiação previdenciária local). "
     "[Exercício Q03-III, Rodada 01 Jun/2024]"),

    ("03-IV – Os servidores inativos das carreiras do Serviço Exterior "
     "Brasileiro têm a prerrogativa de usar dos títulos decorrentes do "
     "exercício do cargo ou função, mas não poderão obter a concessão de "
     "passaporte diplomático ou de serviço, uma vez que deixaram de exercer "
     "suas atribuições funcionais. (C/E?)",
     "<b>ERRADO.</b> Art. 16, parágrafo único, Lei 11.440/2006 — as "
     "prerrogativas dos incisos I (uso de títulos) <b>E</b> II (passaporte "
     "diplomático ou de serviço) se estendem aos inativos — não apenas o "
     "uso de títulos. [Exercício Q03-IV, Rodada 01 Jun/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Lei do Serviço Exterior Brasileiro",
        "Direito Interno - Lei do Serviço Exterior Brasileiro.apkg",
        LEI_SERVICO_EXTERIOR_BRASILEIRO,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
