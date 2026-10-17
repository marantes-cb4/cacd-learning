#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Julho/2023).

Tema: Direito Internacional do Mar (parte do Item 32 do Edital CACD).

Fontes:
  - Anotações: Direito Internacional do Mar.md
  - Material do professor: Direito Internacional_Rodada 01_Julho_2023_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Internacional_Rodada 01_Julho_2023.pdf
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


MAR = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("O direito de perseguição de navio estrangeiro suspeito de violar as "
     "leis do Estado costeiro pode ser iniciado na zona contígua, no mar "
     "territorial ou na zona econômica exclusiva, e, uma vez iniciado, "
     "pode prosseguir pelo alto-mar.",
     "<b>ERRADO.</b> A perseguição (art. 111 da CNUDM) pode se estender pela "
     "ZEE e pelo alto-mar, mas só pode ser <b>iniciada</b> no mar "
     "territorial ou na zona contígua; é vedado iniciá-la na ZEE. Na zona "
     "contígua o Estado exerce apenas parcela da soberania (vigilância e "
     "fiscalização aduaneira, sanitária, imigratória e administrativa). "
     "[Anotações da aula; Rodada 01/Jul.2023]"),

    ("Na zona econômica exclusiva, apenas o Estado costeiro exerce direitos, "
     "ficando vedada aos demais Estados a livre navegação e a colocação de "
     "cabos e dutos submarinos; contudo, Estados sem litoral e "
     "geograficamente desfavorecidos podem explorar, de modo equânime, o "
     "excedente dos recursos vivos da ZEE de Estados costeiros da mesma "
     "região.",
     "<b>ERRADO</b> na primeira parte. Pelos arts. 55, 56 e 58, os demais "
     "Estados têm direito à <b>livre navegação e sobrevoo</b> e à colocação "
     "de dutos e cabos submarinos na ZEE alheia. A segunda parte está "
     "correta (arts. 69 e 70): o acesso ao excedente é restrito aos "
     "recursos <b>vivos</b>. [Anotações da aula; Rodada 01/Jul.2023]"),

    ("Na plataforma continental, o Estado costeiro tem o direito de "
     "explorar recursos minerais e outros recursos não vivos do leito e do "
     "subsolo, inclusive todos os recursos vivos ali existentes, podendo "
     "estender sua largura até 350 milhas marítimas sem necessidade de "
     "qualquer apreciação internacional.",
     "<b>ERRADO.</b> Entre os recursos vivos, o Estado costeiro só explora "
     "os <b>imóveis</b> (art. 76 e seguintes). A extensão além de 200 "
     "milhas, até 350, exige que o Estado informe sua pretensão à "
     "<b>Comissão de Limites da Plataforma Continental</b> (21 peritos em "
     "geologia, geofísica ou hidrografia), que avalia os dados. "
     "[Anotações da aula; Rodada 01/Jul.2023]"),

    ("O alto-mar é espaço coletivo comum, em que todos os Estados, "
     "inclusive os sem litoral, têm as mesmas liberdades, entre elas a de "
     "pesca, desde que não predatória, e a de investigação científica, "
     "desde que voltada ao progresso da humanidade, sendo seu uso restrito "
     "a fins pacíficos.",
     "<b>CERTO.</b> Alto-mar é conceito subsidiário (o que não é mar "
     "territorial, zona contígua nem ZEE). O art. 87 assegura a todos os "
     "Estados as liberdades de navegação, sobrevoo, dutos e cabos, ilhas "
     "artificiais, pesca não predatória e investigação científica; nenhum "
     "Estado pode invocar direitos preferenciais. [Anotações da aula; "
     "Rodada 01/Jul.2023]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Jul/2023) ───────────────

    ("01-I – A doutrina majoritária converge em adotar os conceitos de "
     "Direito do Mar e Direito Marítimo como sinônimos para se referir ao "
     "conjunto de normas internacionais – a exemplo de tratados, costumes e "
     "atos unilaterais de Estado – que estabelece mecanismos de delimitação "
     "do espaço marítimo entre os Estados, fixando os limites "
     "internacionais, sua utilização e a extensão da responsabilidade dos "
     "Estados em seu uso pacífico (DIREITO DO MAR). (C/E?)",
     "<b>ERRADO.</b> Os conceitos são distintos. <b>Direito do Mar</b> é "
     "ramo do DIP (desenvolvido na ONU) sobre o uso dos espaços marítimos "
     "pelos Estados. <b>Direito Marítimo</b> é segmento do Direito "
     "Internacional <b>Privado</b>: transporte de cargas, contratos, portos, "
     "interesses de particulares. [Exercício Q01-I, Rodada 01 Jul/2023]"),

    ("01-II – Nos casos em que as costas de dois Estados são adjacentes ou "
     "se encontram situadas frente a frente, nenhum desses Estados tem o "
     "direito de estender o seu mar territorial além da linha mediana cujos "
     "pontos são equidistantes dos pontos mais próximos das linhas de base, "
     "exceto apenas se houver motivo de existência de títulos históricos. "
     "(C/E?)",
     "<b>ERRADO.</b> O art. 15 da CNUDM fixa a linha mediana como regra "
     "geral, mas admite <b>duas</b> exceções: (i) acordo ou tratado "
     "específico entre os Estados, que prevalece sobre a Convenção; e (ii) "
     "razões históricas <b>ou outras circunstâncias especiais</b>. O "
     "\"exceto apenas\" torna o item errado. [Exercício Q01-II, Rodada 01 "
     "Jul/2023]"),

    ("01-III – Os navios de guerra e os navios utilizados unicamente em "
     "serviço oficial não comercial gozam, no alto mar, de completa "
     "imunidade de jurisdição relativamente a qualquer outro Estado que não "
     "seja o da sua bandeira. (C/E?)",
     "<b>CERTO.</b> Arts. 95 e 96 da CNUDM: imunidade completa no alto-mar, "
     "de modo que não podem ser vistoriados nem aprisionados por outro "
     "Estado. No mar territorial, a mesma imunidade explica por que o "
     "Estado costeiro só pode exigir sua saída imediata. [Exercício "
     "Q01-III, Rodada 01 Jul/2023]"),

    ("01-IV – No âmbito da ONU, foram realizadas três Conferências sobre "
     "Direito do Mar até que se adotasse a Convenção das Nações Unidas sobre "
     "o Direito do Mar (CNUDM) em 1982, o que não impediu que os Estados "
     "soberanos, por meio de atos unilaterais, buscassem resguardar seus "
     "interesses jurídicos sobre recursos da zona marítima, como ocorreu "
     "com os Estados Unidos que, em 1945, pronunciou-se sobre a exploração "
     "de sua zona econômica exclusiva. (C/E?)",
     "<b>ERRADO.</b> A declaração de Truman (1945) tratou da "
     "<b>plataforma continental</b>, não da ZEE. Além disso, a ZEE só "
     "passou a existir no DI com a CNUDM de 1982 (bases definidas na 3ª "
     "Conferência, convocada em 1970); antes só havia mar territorial, "
     "zona contígua e alto-mar. [Exercício Q01-IV, Rodada 01 Jul/2023]"),

    ("02-I – De acordo com a Convenção das Nações Unidas sobre o Direito do "
     "Mar, o Estado costeiro não deve parar nem desviar da sua rota um "
     "navio estrangeiro que passe pelo mar territorial, a fim de exercer a "
     "sua jurisdição civil em relação a uma pessoa que se encontre a "
     "bordo. (C/E?)",
     "<b>CERTO.</b> Art. 28: a regra é a imunidade de jurisdição civil de "
     "quem está a bordo de navio em passagem inocente (citação, intimação, "
     "apreensão de documentos). A exceção são fatos ocorridos em navio que "
     "venha de águas interiores do Estado costeiro, como poluição nelas. "
     "[Exercício Q02-I, Rodada 01 Jul/2023]"),

    ("02-II – A soberania de Estado costeiro sobre o seu mar territorial "
     "abrange não apenas as águas, mas também o leito do mar, seu subsolo e "
     "o espaço aéreo correspondente, devendo tal Estado, contudo, admitir "
     "o direito de passagem inocente de navios mercantes ou de guerra de "
     "qualquer outro Estado. (C/E?)",
     "<b>CERTO.</b> Art. 2º: o mar territorial abrange águas, espaço "
     "aéreo, leito e subsolo. A passagem inocente alcança navios mercantes, "
     "de guerra, oficiais não comerciais e submarinos (na superfície e com "
     "bandeira). Quanto a navios de guerra, o Estado costeiro só pode "
     "exigir a saída imediata (art. 30). [Exercício Q02-II, Rodada 01 "
     "Jul/2023]"),

    ("02-IV – Um navio de guerra de qualquer Estado pode abordar e "
     "inspecionar um navio estrangeiro em alto mar, desde que tal "
     "embarcação não seja um navio de guerra ou utilizado em serviço oficial "
     "não comercial, quando se tratar de navio que se dedica à pirataria ou "
     "ao tráfico de escravos. Nesses casos, tem-se a hipótese de exercício "
     "da jurisdição universal pelo Estado da bandeira do navio de guerra. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 110 (direito de visita): pirataria, tráfico de "
     "escravos, transmissões não autorizadas, navio sem nacionalidade ou "
     "de mesma nacionalidade do navio de guerra. Não alcança navios de "
     "guerra e oficiais não comerciais (imunidade completa, arts. 95 e 96). "
     "Pirataria e tráfico de pessoas envolvem normas de <i>jus cogens</i> "
     "(jurisdição universal). [Exercício Q02-IV, Rodada 01 Jul/2023]"),

    ("03-I – Segundo a CNUDM, todo Estado tem o dever de fixar a largura "
     "do seu mar territorial em 12 milhas marítimas, medidas a partir de "
     "linhas de base determinadas em conformidade com a CNUDM. (C/E?)",
     "<b>ERRADO.</b> O art. 3º estabelece que o Estado fixa a largura por "
     "ato unilateral, <b>não podendo ultrapassar</b> 12 milhas. Doze é o "
     "máximo, não uma obrigação: pode-se fixar menos. O Brasil adotou o "
     "máximo. [Exercício Q03-I, Rodada 01 Jul/2023]"),

    ("03-II – A Comissão de Limites da Plataforma Continental (CLPC), "
     "composta por 21 membros peritos em geologia, geofísica ou "
     "hidrografia, tem por função, entre outras, examinar os dados e "
     "outros elementos de informação, apresentados pelos Estados costeiros "
     "acerca dos limites exteriores da plataforma continental nas zonas em "
     "que tais limites se estenderem além de 200 milhas marítimas. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 76: regra geral, plataforma de até 200 milhas; "
     "exceção, até 350 milhas para quem comprovar as características "
     "geológicas, geofísicas ou hidrográficas, o que exige apreciação da "
     "CLPC. [Exercício Q03-II, Rodada 01 Jul/2023]"),

    ("03-III – A área e seus recursos, nela compreendidos ainda os "
     "recursos genéticos decorrentes da biodiversidade marinha para além "
     "dos limites de jurisdição nacional, são considerados patrimônio "
     "comum da humanidade em conformidade com o art. 136 da CNUDM. "
     "(C/E?)",
     "<b>ERRADO.</b> A Área é patrimônio comum da humanidade, mas o art. "
     "133 limita os \"recursos\" aos <b>minerais</b> (sólidos, líquidos, "
     "gasosos e nódulos polimetálicos). A Autoridade Internacional dos "
     "Fundos Marinhos não disciplina a exploração de recursos genéticos, "
     "que ficam fora da Convenção. [Exercício Q03-III, Rodada 01 "
     "Jul/2023]"),

    ("03-IV – De acordo com a Convenção das Nações Unidas sobre Direito do "
     "Mar, o Brasil não pode exercer jurisdição penal em navio mercantil "
     "estrangeiro que realize passagem inocente pelo mar territorial, "
     "mesmo que seja para fim de repressão do tráfico ilícito de "
     "estupefacientes. (C/E?)",
     "<b>ERRADO.</b> Art. 27: a regra é a imunidade penal, mas há exceções, "
     "entre elas a <b>repressão ao tráfico de drogas</b>, além de "
     "consequências para o Estado costeiro, perturbação da paz ou da ordem, "
     "pedido do capitão ou de autoridade do Estado de bandeira e crimes "
     "cometidos em águas interiores. [Exercício Q03-IV, Rodada 01 "
     "Jul/2023]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Direito Internacional do Mar",
        "Direito Internacional - Direito Internacional do Mar.apkg",
        MAR,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
