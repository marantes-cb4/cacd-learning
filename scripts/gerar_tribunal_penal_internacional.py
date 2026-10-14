#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 02 (Abril/2024).

Tema: Direito Penal Internacional. Tribunais Penais Internacionais. TPI (Item 30 do Edital CACD).

Fontes:
  - Anotações: Tribunal Penal Internacional.md
  - Material do professor: Direito Internacional_Rodada 02_Abril_2024_Anotada.pdf
  - Exercícios: Questões objetivas_Direito Internacional_Rodada 02_Abril_2024.pdf
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


TPI = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Em razão do princípio da complementaridade, o Tribunal Penal "
     "Internacional exerce jurisdição concorrente com a justiça nacional dos "
     "Estados-partes e prevalece sobre ela, a exemplo dos tribunais penais "
     "ad hoc da ex-Iugoslávia e de Ruanda.",
     "<b>ERRADO.</b> Os tribunais <i>ad hoc</i> têm jurisdição concorrente e "
     "<b>prevalecem</b> sobre a justiça nacional. O TPI, ao contrário, tem "
     "jurisdição <b>complementar</b> (Preâmbulo do Estatuto de Roma): só atua "
     "quando a justiça nacional é inerte ou incapaz de julgar o indivíduo. "
     "[Anotações da aula; Rodada 02/Abr.2024]"),

    ("Os Tribunais de Nuremberg e de Tóquio são unanimemente considerados "
     "tribunais internacionais, e sua contribuição histórica foi demonstrar "
     "que a punição de indivíduos dependia da criação prévia de normas "
     "penais convencionais.",
     "<b>ERRADO.</b> Foram criados pelos vencedores da 2ª GM, não pelo "
     "sistema internacional como um todo, e por isso há discordância "
     "doutrinária sobre sua natureza (alguns os chamam de tribunais de "
     "exceção, <i>post factum</i>). Os juízes reconheceram que <b>normas "
     "costumeiras</b> já proibiam os crimes — o que afasta a tese de que a "
     "punição exigiria norma prévia. [Anotações da aula; Rodada 02/Abr.2024]"),

    ("O Tribunal Penal Internacional não pode julgar quem tenha cometido o "
     "crime com menos de dezoito anos, ainda que já seja maior de idade ao "
     "tempo do julgamento, e os crimes de sua competência são "
     "imprescritíveis.",
     "<b>CERTO.</b> Art. 26: o TPI não tem jurisdição sobre pessoa menor de "
     "18 anos na <b>data do crime</b>, ainda que hoje seja adulta. Art. 29: "
     "os crimes de competência do Tribunal são <b>imprescritíveis</b>, sem "
     "perda do direito de ação com o passar do tempo (respeitada a vigência "
     "do Estatuto, desde 2002). [Anotações da aula; Rodada 02/Abr.2024]"),

    ("As declarações apresentadas pela Ucrânia ao TPI em 2014–15, embora "
     "esse Estado não seja parte do Estatuto de Roma, permitem ao Tribunal "
     "julgar crimes de guerra e contra a humanidade ocorridos em seu "
     "território, mas não o crime de agressão.",
     "<b>CERTO.</b> O art. 12 admite que Estado não parte reconheça a "
     "jurisdição do TPI por declaração. A Ucrânia o fez em 2014–15 (anexação "
     "da Crimeia), mas as declarações <b>não incluem agressão</b>. A Rússia "
     "também não é parte do Estatuto. [Anotações da aula; Rodada "
     "02/Abr.2024]"),

    ("Segundo o Estatuto de Roma, a pena de prisão por tempo determinado "
     "aplicada pelo TPI deve ser reexaminada após o cumprimento de dois "
     "terços da pena, e a prisão perpétua, após o cumprimento de vinte e "
     "cinco anos, sendo também admitida a pena de morte para os crimes de "
     "genocídio.",
     "<b>ERRADO.</b> O reexame (art. 110) ocorre após <b>2/3</b> da pena em "
     "anos e após <b>25 anos</b> na perpétua — essa parte está correta. Mas "
     "a pena de morte é <b>vedada</b> (art. 77): o TPI aplica prisão de até "
     "30 anos ou perpétua, além de multa e perdimento de bens. [Anotações "
     "da aula; Rodada 02/Abr.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 02, Abr/2024) ───────────────

    ("01-I – A sede do Tribunal Penal Internacional é em Haia, podendo, no "
     "entanto, sempre que entender conveniente, funcionar em outro local, "
     "desde que o acusado sempre esteja presente no julgamento. (C/E?)",
     "<b>CERTO.</b> Arts. 62 e 63 do Estatuto de Roma: regra geral, o "
     "julgamento ocorre em Haia; excepcionalmente o TPI pode decidir julgar "
     "em outro local. A presença do réu é obrigatória, para garantir ampla "
     "defesa e contraditório (se causar tumulto, vai a outra sala, com "
     "comunicação com o defensor). [Exercício Q01-I, Rodada 02 Abr/2024]"),

    ("01-II – Os Estados partes ao Estatuto de Roma devem adaptar suas "
     "legislações para estarem normativamente aptos a processar e julgar "
     "chefes militares e superiores hierárquicos nas condições previstas "
     "pelo Tribunal Penal Internacional. (C/E?)",
     "<b>CERTO.</b> Pela complementaridade (Preâmbulo), cabe primeiro à "
     "justiça nacional julgar os crimes do Estatuto; logo, os ordenamentos "
     "internos precisam estar adaptados. Pelo art. 27, não há imunidade "
     "oficial que impeça a atuação do TPI sobre chefes militares, de Estado "
     "ou de governo. [Exercício Q01-II, Rodada 02 Abr/2024]"),

    ("01-IV – A Organização das Nações Unidas criou o Estatuto de Roma do "
     "Tribunal Penal Internacional por resolução do Conselho de Segurança "
     "para, ao lado da Corte Internacional de Justiça (CIJ) compor seus "
     "órgãos com funções judiciárias. O TPI tem competência para investigar, "
     "processar e julgar indivíduos pelos mais graves crimes internacionais "
     "e a CIJ tem competência para julgar controvérsias entre os Estados, "
     "além de oferecer pareceres consultivos sobres questões legais "
     "apresentadas por órgãos autorizados e agências especializadas. (C/E?)",
     "<b>ERRADO.</b> O TPI nasceu de um <b>tratado</b> (Estatuto de Roma, "
     "1998), não de resolução do CSNU — esta criou os tribunais <i>ad hoc</i> "
     "da ex-Iugoslávia e de Ruanda. O TPI é uma <b>organização internacional "
     "com personalidade própria</b> (art. 4), não órgão da ONU, ao contrário "
     "da CIJ. [Exercício Q01-IV, Rodada 02 Abr/2024]"),

    ("02-I – O Conselho de Segurança da ONU, agindo nos termos do Capítulo "
     "VII da Carta das Nações Unidas, poderá ampliar a competência do TPI "
     "referindo ao Procurador qualquer situação em que haja indício de ter "
     "ocorrido a prática dos crimes de competência do Tribunal, mesmo que "
     "o caso envolva um Estado que não seja parte ao Estatuto de Roma. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 13 do Estatuto: por resolução vinculante fundada "
     "no Capítulo VII, o CSNU pode acionar o TPI para crimes praticados no "
     "território de <b>qualquer Estado</b> ou por indivíduos de <b>qualquer "
     "nacionalidade</b>, mesmo não partes. Isso dispensa a criação de novos "
     "tribunais <i>ad hoc</i>. [Exercício Q02-I, Rodada 02 Abr/2024]"),

    ("02-II – O poder de o Conselho de Segurança solicitar adiamento do "
     "inquérito e do procedimento criminal no Tribunal Penal Internacional, "
     "por meio de resolução aprovada nos termos do disposto no Capítulo VII "
     "da Carta das Nações Unidas, está consignado no Estatuto de Roma. "
     "(C/E?)",
     "<b>CERTO.</b> Art. 16: o CSNU, com base no Capítulo VII e por "
     "resolução, pode determinar o adiamento ou a suspensão de inquérito ou "
     "processo no TPI por até 12 meses, renovável nas mesmas condições. "
     "[Exercício Q02-II, Rodada 02 Abr/2024]"),

    ("02-III – A jurisdição do Tribunal Penal Internacional, de acordo com "
     "o Estatuto de Roma, só pode ser exercida quando o crime sujeito à "
     "jurisdição do Tribunal for cometido no território de um Estado parte, "
     "ou por um nacional de um Estado parte ou ainda por meio de declaração "
     "específica de Estado não contratante. (C/E?)",
     "<b>ERRADO.</b> Há <b>4 hipóteses</b>: crime no território de "
     "Estado-parte; crime por nacional de Estado-parte; declaração de "
     "Estado não parte (art. 12); e <b>resolução do CSNU</b> com base no "
     "Capítulo VII (art. 13). O item omitiu a quarta, por isso o \"só\" "
     "torna a afirmação errada. [Exercício Q02-III, Rodada 02 Abr/2024]"),

    ("02-IV – O Tribunal Penal Internacional é um tribunal independente da "
     "Organização das Nações Unidas (ONU), mas, devido a seus objetivos, "
     "possui uma relação especial com a ONU, que consiste, por exemplo, no "
     "envio de relatórios anuais à Assembleia Geral e na obediência a "
     "determinadas ordens do Conselho de Direitos Humanos. (C/E?)",
     "<b>ERRADO.</b> A independência e a relação especial com a ONU são "
     "reais, mas o Estatuto de Roma <b>não atribui nenhum papel ao Conselho "
     "de Direitos Humanos</b>. As atribuições são do <b>Conselho de "
     "Segurança</b> (arts. 13 e 16). Na falta de cooperação (art. 87), o TPI "
     "informa a Assembleia dos Estados Partes ou o CSNU. [Exercício Q02-IV, "
     "Rodada 02 Abr/2024]"),

    ("03-I – O dever de colaboração do Estado parte com o Tribunal Penal "
     "Internacional não é absoluto, podendo o Estado Parte não entregar "
     "estrangeiro ao Tribunal, caso o Estado Parte tenha firmado acordos de "
     "imunidade com Estado terceiro. (C/E?)",
     "<b>CERTO.</b> Regra: a entrega ao TPI deve ser cumprida pelos "
     "Estados-partes. Exceção do art. 98: o Estado pode deixar de entregar "
     "se isso violar tratado com terceiro Estado. Isso não cria imunidade "
     "perante o TPI (art. 27); o Estado deve julgar o indivíduo "
     "internamente, salvo anuência do terceiro. [Exercício Q03-I, Rodada 02 "
     "Abr/2024]"),

    ("03-II – O Estatuto de Roma de 1998 prevê a competência do Tribunal "
     "Penal Internacional para julgar o crime de genocídio; os crimes "
     "contra a humanidade; os crimes de guerra e o crime de agressão, "
     "todos imprescritíveis e devidamente tipificados na redação do "
     "referido tratado que adquiriu vigência internacional em 2002. "
     "(C/E?)",
     "<b>ERRADO.</b> Genocídio, crimes contra a humanidade e de guerra "
     "estão tipificados nos arts. 6º, 7º e 8º; o <b>crime de agressão</b> "
     "não foi tipificado no texto original (art. 5º, §2º) e só foi definido "
     "nas Emendas de Kampala (2010), aplicáveis a partir de 2017 e apenas "
     "aos Estados que as ratificaram. O Brasil não ratificou. [Exercício "
     "Q03-II, Rodada 02 Abr/2024]"),

    ("03-IV – Sobre a pena de morte, pode-se afirmar que, no atual estágio "
     "de desenvolvimento do Direito Internacional dos Direitos Humanos, tem "
     "sido regularmente adotada por tribunais internacionais, desde o "
     "Tribunal Militar Internacional de Nuremberg e o Tribunal Militar "
     "internacional de Tóquio. (C/E?)",
     "<b>ERRADO.</b> O Estatuto de Roma, ápice do direito penal "
     "internacional, não prevê pena de morte. Pelo art. 77, o TPI aplica "
     "como principais a prisão de até <b>30 anos</b> ou a <b>perpétua</b>, "
     "e como acessórias a multa e o perdimento de bens oriundos do crime. "
     "[Exercício Q03-IV, Rodada 02 Abr/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Tribunal Penal Internacional",
        "Direito Internacional - Tribunal Penal Internacional.apkg",
        TPI,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
