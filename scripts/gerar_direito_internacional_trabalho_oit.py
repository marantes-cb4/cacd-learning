#!/usr/bin/env python3
"""Gera deck Anki — Direito Internacional Rodada 01 (Outubro/2024).

Tema: Direito Internacional do Trabalho / OIT (Item 33 do Edital CACD).

Fontes:
  - Anotações: Direito Internacional do Trabalho - OIT.md
  - Material do professor: Direito Internacional_Rodada 01_Outubro_2024_Anotada.pdf
  - Exercícios: Exercícios objetivo_Direito Internacional_Rodada 01_Outubro_2024.pdf
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


OIT = [

    ('No que diz respeito à Organização Internacional do Trabalho (OIT), julgue certo ou errado: A configuração institucional da OIT apresenta uma somatória de organismos com personalidade jurídica própria, abarcando Conferência Internacional do Trabalho, o Conselho de Administração e a Repartição Internacional do Trabalho.',
     '<b>ERRADO.</b> Quem tem personalidade jurídica própria é a <b>OIT como organização</b> (agência especializada da ONU). Seus três órgãos permanentes (Conferência, Conselho de Administração e Repartição/Bureau) são órgãos internos e não têm personalidade própria — raciocínio idêntico ao dos órgãos da ONU (AGNU, CSNU, CIJ). [Anotações da aula; Rodada 01 Out/2024]'),

    ('No que diz respeito à OIT, julgue certo ou errado: Não obstante a Organização Internacional do Trabalho (OIT) seja uma das agências especializadas da Organização das Nações Unidas, um Estado recém-criado pode pleitear ser parte da OIT, ainda que seu pedido para ingressar na condição de membro na ONU tenha sido rejeitado.',
     '<b>CERTO.</b> A OIT é agência especializada, e não órgão da ONU: tem personalidade jurídica própria e é independente. O ingresso de novos membros é decidido pela <b>Conferência Internacional do Trabalho</b>, sem depender da condição de membro da ONU. A pegadinha é supor vinculação automática entre as duas adesões. [Anotações da aula; Rodada 01 Out/2024]'),

    ('No que diz respeito à OIT, julgue certo ou errado: Conselho de Administração é a principal instância deliberativa da OIT e responsável pela origem das principais normas internacionais sobre as questões trabalhistas. Totalizando centenas de delegados, o Conselho é composto por quatro representantes de cada Estado-membro.',
     '<b>ERRADO.</b> A descrição é da <b>Conferência Internacional do Trabalho</b> (órgão de cúpula, 4 delegados por Estado). O Conselho de Administração é órgão <b>executivo</b>, com apenas <b>56 conselheiros</b> (28 governos, 14 trabalhadores, 14 empregadores), eleitos pela Conferência para mandato de 3 anos. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Considerando-se as características institucionais da OIT e sua produção normativa, julgue: A delegação de cada Estado-membro, no órgão máximo de deliberação da OIT, seguindo os preceitos democráticos igualitários, segue o padrão tripartite, sendo composta mediante a participação de três representantes, um do governo, um dos empregadores e um dos trabalhadores.',
     '<b>ERRADO.</b> A composição é tripartite, mas cada Estado envia <b>4 delegados</b>, cada um com 1 voto: <b>2 do governo</b>, 1 dos empregados e 1 dos empregadores (art. 3º do Acordo Constitutivo). O governo tem, portanto, metade da delegação. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Considerando-se as características institucionais da OIT e sua produção normativa, julgue: Tanto convenções quanto recomendações, para serem adotadas, exigem o voto favorável de dois terços dos presentes na Conferência Internacional do Trabalho.',
     '<b>CERTO.</b> O quórum é o mesmo para os dois tipos de norma: <b>2/3 dos presentes</b>. A diferença está nos efeitos: convenções são tratados (hard law); recomendações são soft law e não exigem ratificação. Mesmo se os 4 delegados do Brasil votarem contra, o Brasil terá de cumprir os procedimentos do art. 19. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Considerando-se as características institucionais da OIT e sua produção normativa, julgue: Caso a Conferência Internacional do Trabalho delibere pela edição de recomendação, será dado conhecimento do seu teor aos Estados-membros, a fim de que estes a considerem, atendendo à sua efetivação por meio de lei nacional ou por qualquer outra forma.',
     '<b>CERTO.</b> A recomendação não vincula, mas gera 2 obrigações procedimentais (art. 19, 6º): submetê-la ao órgão nacional competente (no Brasil, o Congresso) em 1 ano ou, excepcionalmente, 18 meses, para eventuais medidas internas; e comunicar ao Diretor-Geral as medidas adotadas. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Acerca do Direito Internacional do Trabalho e da atuação da OIT, julgue: Como regra geral, os Estados-membros têm o prazo de 01 (um) ano para ratificarem a convenção aprovada pela Conferência Internacional do Trabalho. Excepcionalmente, esse prazo poderá ser de 18 (dezoito) meses, conforme disposto no Acordo Constitutivo da OIT de 1946.',
     '<b>ERRADO.</b> O prazo de 1 ano (ou 18 meses, excepcionalmente) é para o Estado <b>submeter</b> a convenção ao órgão nacional competente — no Brasil, o Executivo envia ao Congresso. Não é prazo para ratificar, e o Congresso sequer tem prazo para deliberar. Se aprovar, aí sim o Presidente é obrigado a ratificar. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Acerca do Direito Internacional do Trabalho e da atuação da OIT, julgue: Consoante a jurisprudência do STF, as convenções e recomendações da OIT ingressam no ordenamento jurídico brasileiro com status de supralegalidade.',
     '<b>ERRADO.</b> O status supralegal vale para as <b>convenções</b>, que são tratados de direitos humanos (2ª geração). As <b>recomendações</b> são soft law: não são tratados, não são ratificadas e não ingressam no ordenamento com hierarquia normativa. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Acerca do Direito Internacional do Trabalho e da atuação da OIT, julgue: Reclamação é o procedimento constitucional mediante o qual um Estado-membro submete à OIT denúncia contra outro Estado-membro que não tenha adotado medidas satisfatórias para o cumprimento de uma convenção que ambos hajam ratificado.',
     '<b>ERRADO.</b> A descrição é de <b>queixa</b> (art. 26), apresentada por Estado-membro contra outro. A <b>reclamação</b> (art. 24) é apresentada por organizações de empregados ou de empregadores — e não por governos —, dirigida ao Bureau. Ambas são endereçadas à Repartição Internacional do Trabalho. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Após a aprovação de uma convenção da OIT pelo Congresso Nacional, o Presidente da República mantém a discricionariedade de ratificá-la ou não, como ocorre com os tratados em geral, e o Congresso deve deliberar sobre ela dentro do prazo de um ano contado do encerramento da sessão da Conferência.',
     '<b>ERRADO.</b> Duas particularidades das convenções da OIT: (i) o Executivo tem 1 ano (ou 18 meses) para <b>enviar</b> ao Congresso, que <b>não tem prazo</b> para votar; (ii) aprovada pelo CN, o Presidente é <b>obrigado a ratificar</b> (art. 19, 5º, "d"). Além disso, a adoção da convenção dispensa a vontade do Presidente: decorre do voto de 2/3 da Conferência. [Anotações da aula; Rodada 01 Out/2024]'),

    ('As recomendações da OIT, por serem soft law, dispensam qualquer providência dos Estados-membros; por isso a Conferência só as utiliza para temas já consolidados, que não encontrariam resistência para serem aprovados como convenção.',
     '<b>ERRADO.</b> Recomendações geram obrigações procedimentais (submissão ao órgão nacional e comunicação ao Diretor-Geral) e são usadas justamente em temas <b>delicados</b>, sujeitos a rejeição como convenção. Dão flexibilidade e preparam os ordenamentos internos: no médio/longo prazo, tendem a virar convenções (hard law). [Anotações da aula; Rodada 01 Out/2024]'),

    ('A Conferência Internacional do Trabalho pode ser equiparada à Assembleia Geral da ONU quanto às funções e à forma de votação, pois ambas são o órgão de cúpula de suas organizações e reúnem delegações dos Estados-membros.',
     '<b>ERRADO.</b> A Conferência é órgão de cúpula, mas tem composição <b>tripartite</b> e cada Estado tem <b>4 votos</b> (governo, empregados e empregadores). Na AGNU cada Estado tem <b>1 voto</b> (art. 18 da Carta) e só há representantes do governo. Daí a impossibilidade de equiparar as funções. [Anotações da aula; Rodada 01 Out/2024]'),

    ('Em sua origem, em 1919, a OIT foi criada como organização internacional dotada de personalidade jurídica própria, e foi o fim da 2ª Guerra Mundial que a vinculou à ONU como agência especializada, sem alterar sua natureza jurídica.',
     '<b>ERRADO.</b> Em 1919 (Tratado de Versalhes) a OIT nasceu como <b>órgão da Liga das Nações</b>, sem personalidade própria. Só em <b>1946</b>, com a ONU, tornou-se OI com personalidade jurídica e agência especializada. Sua criação é um dos 3 movimentos que antecedem 1945 como gênese da proteção dos direitos humanos (DIH, normas contra a escravidão e OIT). [Anotações da aula; Rodada 01 Out/2024]'),

    ('A fragmentação do Direito Internacional, de que o Direito Internacional do Trabalho é exemplo, tende a reduzir a eficácia das normas internacionais, pois cada microssistema cria órgãos e regimes de execução próprios, o que impede a transferência automática de institutos de um ramo a outro.',
     '<b>ERRADO.</b> A fragmentação (microssistemas como OIT e OMC) <b>aumenta a eficácia</b>: produção normativa e execução seguem regras ajustadas ao tema, com órgãos políticos ou jurisdicionais especializados. É verdade que, por isso, não se transferem automaticamente conceitos entre microssistemas — mas essa é consequência, não prejuízo. [Anotações da aula; Rodada 01 Out/2024]'),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Internacional::Direito Internacional do Trabalho - OIT",
        "Direito Internacional - Direito Internacional do Trabalho - OIT.apkg",
        OIT,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
