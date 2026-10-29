#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Janeiro/2025).

Tema: Direito do Comércio Internacional e OMC (Item 31 do Edital CACD).

Fontes:
  - Anotações: Direito do Comércio Internacional e OMC.md
  - Material do professor: Direito Internacional_Rodada 01_Janeiro_2025_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Janeiro_2025.pdf
"""
import genanki
import random
import os

DECK_DIR = "/Users/marantes.isabela/Desktop/cacd-learning/anki/decks/direito internacional"
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


OMC = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O Mercosul concede a seus membros vantagens comerciais que, por força "
     "da cláusula da nação mais favorecida do GATT, devem ser estendidas "
     "automaticamente a todos os demais Estados-partes do GATT; em "
     "contrapartida, as preferências a Estados em desenvolvimento só "
     "valem se estendidas a todos.",
     "<b>ERRADO.</b> A cláusula da nação mais favorecida (art. 1º) tem "
     "<b>exceções</b>: (i) acordos regionais, como o Mercosul, cujos "
     "benefícios <b>não</b> se estendem automaticamente; (ii) o Sistema "
     "Geral de Preferências (cláusula de habilitação), que favorece "
     "Estados em desenvolvimento sem que os demais possam exigir o mesmo "
     "regime; e (iii) as exceções gerais do art. 20. [Anotações da aula; "
     "Rodada 01/Jan.2025]"),

    ("Um Estado pode proibir a importação de suínos de determinado país "
     "por risco de peste suína, com base nas exceções gerais do art. 20 "
     "do GATT, desde que a medida não configure discriminação arbitrária "
     "ou injustificada nem restrição disfarçada ao comércio; já para "
     "conservar recursos naturais esgotáveis, a restrição à exportação "
     "dispensa medidas equivalentes no plano interno.",
     "<b>ERRADO</b> na parte final. O art. 20 admite exceções para "
     "proteger bens jurídicos igualmente relevantes (moralidade pública, "
     "saúde e vida de pessoas, animais e vegetais, tesouros nacionais, "
     "reservas de ouro e prata etc.). Para conservar recursos esgotáveis, "
     "as restrições comerciais devem vir <b>acompanhadas de restrições "
     "internas</b> (produção e consumo nacionais). [Anotações da aula; "
     "Rodada 01/Jan.2025]"),

    ("O Órgão de Apelação da OMC, composto por sete juízes com mandato de "
     "quatro anos renovável uma única vez, pode reexaminar os fatos do "
     "litígio e proferir novo julgamento do caso, uma vez que atua como "
     "segunda instância do sistema.",
     "<b>ERRADO.</b> Embora seja a segunda instância (duplo grau), o Órgão "
     "de Apelação analisa <b>exclusivamente questões de direito</b>: verifica "
     "se o painel aplicou corretamente as normas internacionais. <b>Não "
     "analisa fatos</b> nem rejulga o caso. Seu relatório também precisa "
     "ser aprovado pelo OSC (consenso negativo). [Anotações da aula; "
     "Rodada 01/Jan.2025]"),

    ("Se o membro derrotado e o vencedor não chegam a acordo sobre o prazo "
     "para implementar a decisão, instaura-se arbitragem que define o "
     "prazo e as medidas a serem adotadas; descumprido o prazo, o "
     "vencedor pode impor retaliações por conta própria, preferencialmente "
     "no mesmo setor, ou em outro setor se aquele for irrelevante.",
     "<b>ERRADO.</b> A arbitragem define <b>apenas o prazo</b>; o árbitro "
     "não decide quais medidas o derrotado adotará. E o vencedor precisa "
     "<b>solicitar autorização do OSC</b> para retaliar. Em regra, a "
     "retaliação ocorre no mesmo setor; só se ineficaz admitem-se "
     "retaliações cruzadas, com autorização do OSC. [Anotações da aula; "
     "Rodada 01/Jan.2025]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jan/2025) ───────────────

    ("01-I – Sucessora do GATT, a OMC é uma das mais conhecidas instâncias "
     "multilaterais dos dias atuais, tendo, entre outras, a missão de "
     "elaborar as normas reguladoras do comércio mundial, zelar pela sua "
     "observância e julgar os contenciosos entre os atores do mercado "
     "mundial. (C/E?)",
     "<b>CERTO.</b> Há <b>sucessão normativa</b> entre GATT/47 e OMC (não "
     "sucessão entre OIs, pois o GATT, mero tratado, não tinha "
     "personalidade). A OMC inovou com um sistema de solução de "
     "controvérsias de competência compulsória, cujas decisões são "
     "implementadas pelos próprios litigantes. [Exercício Q01-I, Rodada "
     "01 Jan/2025]"),

    ("01-III – Os pilares fundamentais do sistema multilateral de "
     "comércio GATT/OMC (normas que fundaram o Direito do Comércio "
     "Internacional) incluem a cláusula de nação mais favorecida (NMF), o "
     "princípio de tratamento nacional, a defesa dos consumidores e a "
     "primazia à proteção do meio ambiente. (C/E?)",
     "<b>ERRADO.</b> Os pilares de 1947 são a <b>nação mais favorecida</b> "
     "(art. 1º) e o <b>tratamento nacional</b> (mesmo tratamento a "
     "produtos nacionais e importados no mercado interno). Defesa do "
     "consumidor e primazia ambiental não eram preocupações do DI nos anos "
     "1940; o meio ambiente só ganha relevo a partir da década de 1970. "
     "[Exercício Q01-III, Rodada 01 Jan/2025]"),

    ("01-IV – O Sistema Geral de Preferências (também chamado de cláusula "
     "de habilitação) permite que países desenvolvidos concedam "
     "tratamento tarifário preferencial para produtos oriundos de países "
     "em desenvolvimento e de países de menor desenvolvimento relativo. "
     "(C/E?)",
     "<b>CERTO.</b> É uma das exceções à nação mais favorecida: os "
     "benefícios concedidos a Estados menos desenvolvidos <b>não</b> se "
     "estendem a todos os Estados-partes do GATT. [Exercício Q01-IV, "
     "Rodada 01 Jan/2025]"),

    ("02-I – Inovador em muitos sentidos, o SSC admite a participação de "
     "blocos econômicos, como a União Europeia, e a participação de "
     "organizações não governamentais, as quais podem iniciar um litígio "
     "junto a essa instância de solução de controvérsias, desde que "
     "exista aderência com o tema discutido e a área de atuação da "
     "organização não governamental. (C/E?)",
     "<b>ERRADO.</b> Só os <b>membros</b> da OMC (Estados e a União "
     "Europeia) acionam o SSC. As ONGs não iniciam litígios, mas podem "
     "atuar como <i>amicus curiae</i>, com autorização do OSC, emitindo "
     "pareceres técnicos não vinculantes. [Exercício Q02-I, Rodada 01 "
     "Jan/2025]"),

    ("02-II – As conclusões dos relatórios finais dos painéis, embora "
     "conformem decisões notadamente jurídicas, dependem de convalidação "
     "política. (C/E?)",
     "<b>CERTO.</b> O relatório do painel é jurídico, mas precisa ser "
     "submetido ao OSC. A regra do consenso negativo (só a unanimidade "
     "rejeita) reduz o componente político, que ainda existe: os membros "
     "do OSC poderiam, em tese, rejeitar o relatório. [Exercício Q02-II, "
     "Rodada 01 Jan/2025]"),

    ("02-III – A adoção da regra do consenso invertido, uma diferença "
     "significativa em relação ao sistema de solução de controvérsias "
     "adotado pelo GATT 1947, baseia-se na exigência de que, no SSC da "
     "OMC, exige-se unanimidade para rejeitar os relatórios produzidos "
     "pelos painéis e pelo Órgão de Apelação. (C/E?)",
     "<b>CERTO.</b> No GATT/47 vigorava o consenso <b>positivo</b>: todos, "
     "inclusive o infrator, tinham de concordar para a decisão vincular. "
     "Na OMC, o consenso é <b>negativo (invertido ou reverso)</b>: só a "
     "unanimidade rejeita o relatório. [Exercício Q02-III, Rodada 01 "
     "Jan/2025]"),

    ("02-IV – As atribuições do órgão de solução de controvérsias, no "
     "âmbito da OMC, incluem a criação de painéis, a adoção do relatório "
     "do painel, o acompanhamento da implementação das recomendações "
     "sugeridas pelo relatório do painel, bem como a autorização da "
     "imposição de sanções aos Estados que não se adequarem ao relatório. "
     "(C/E?)",
     "<b>CERTO.</b> O OSC, função especializada do Conselho Geral, institui "
     "o painel, aprova os relatórios (do painel e do Órgão de Apelação), "
     "acompanha a implementação e autoriza o vencedor a retaliar quando o "
     "derrotado não cumpre. [Exercício Q02-IV, Rodada 01 Jan/2025]"),

    ("03-I – No âmbito da Organização Mundial Comércio (OMC), é permitido "
     "à Conferência Ministerial decidir a derrogação de uma obrigação de "
     "um membro em virtude do acordo constitutivo da OMC. (C/E?)",
     "<b>CERTO.</b> A Conferência Ministerial é o órgão supremo: reúne os "
     "Ministros das Relações Exteriores ou do Comércio Exterior, reúne-se "
     "ordinariamente a cada 2 anos e adota novos acordos e também pode "
     "derrogar (revogar) obrigações vigentes. [Exercício Q03-I, Rodada 01 "
     "Jan/2025]"),

    ("03-II – Entre os princípios básicos da Organização Mundial do "
     "Comércio, estão a imposição de barreiras não comerciais e a "
     "discriminação comercial em função do nível de desenvolvimento dos "
     "países. (C/E?)",
     "<b>ERRADO.</b> A OMC busca a <b>liberalização</b>, proibindo "
     "barreiras que inviabilizem o comércio, como as quotas (barreiras "
     "quantitativas). A diferenciação em favor de países em "
     "desenvolvimento existe como exceção favorável (SGP), não como "
     "discriminação em função do desenvolvimento. [Exercício Q03-II, "
     "Rodada 01 Jan/2025]"),

    ("03-III – A estrutura da OMC prevê um Conselho do Grupo Comum, que "
     "se reúne para desempenhar as funções do Órgão de Solução de "
     "Controvérsias estabelecido no entendimento sobre solução de "
     "controvérsias. (C/E?)",
     "<b>ERRADO.</b> O OSC é uma <b>função especializada do Conselho "
     "Geral</b> da OMC, composto por representantes de todos os membros. "
     "Não existe \"Conselho do Grupo Comum\". [Exercício Q03-III, Rodada "
     "01 Jan/2025]"),

    ("03-IV – Organização Mundial do Comércio (OMC) é uma agência "
     "vinculada à ONU, com personalidade jurídica própria de direito "
     "internacional, criada para regular o comércio internacional e "
     "assegurar um aperfeiçoamento institucional do processo de "
     "regulação iniciado com o GATT 1947. (C/E?)",
     "<b>ERRADO.</b> A OMC é OI com personalidade própria, criada pelo "
     "Acordo de Marraquexe (1994), mas <b>não está vinculada à ONU</b> e "
     "não é agência especializada: atua de forma independente desde a "
     "concepção. [Exercício Q03-IV, Rodada 01 Jan/2025]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Direito do Comércio Internacional e OMC",
        "Direito Internacional - Direito do Comércio Internacional e OMC.apkg",
        OMC,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
