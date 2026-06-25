#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Nacionalidade"""

import genanki
import os
import random

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "anki", "decks", "direito")

STYLE = """
.card { font-family: Arial, sans-serif; font-size: 16px; text-align: left; padding: 12px; }
.front { font-weight: bold; }
"""

def make_deck(title, filename, cards):
    model_id = random.randrange(1_000_000_000, 2_000_000_000)
    deck_id = random.randrange(1_000_000_000, 2_000_000_000)

    model = genanki.Model(
        model_id,
        "CACD Basic",
        fields=[{"name": "Frente"}, {"name": "Verso"}],
        templates=[{
            "name": "Card",
            "qfmt": '<div class="front">{{Frente}}</div>',
            "afmt": '{{FrontSide}}<hr>{{Verso}}',
        }],
        css=STYLE,
    )

    deck = genanki.Deck(deck_id, title)
    for front, back in cards:
        deck.add_note(genanki.Note(model=model, fields=[front, back]))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename)
    genanki.Package(deck).write_to_file(out_path)
    print(f"✅ {filename} — {len(cards)} cards")
    print(f"🎉 Deck gerado em {OUTPUT_DIR}")


CARDS = [
    # ── CONCEITO E PRINCÍPIOS ─────────────────────────────────────────────────
    (
        "O que é nacionalidade no Direito Internacional e que tipo de direito humano representa?",
        "<b>Vínculo jurídico-político</b> entre um indivíduo e um Estado soberano.<br>"
        "É <b>direito humano de 1ª geração/dimensão</b> (direito civil e político): impõe ao "
        "Estado a proibição de privar arbitrariamente o indivíduo da nacionalidade obtida e "
        "de impedir a mudança de nacionalidade.<br>"
        "<i>Fonte: Anotações – Nacionalidade</i>",
    ),
    (
        "Quais são os dois princípios que regem a nacionalidade no Direito Internacional?",
        "1. <b>Prevalência do direito interno</b>: cada Estado fixa suas próprias regras de "
        "aquisição e perda de nacionalidade (decorre da personalidade jurídica internacional "
        "dos Estados)<br>"
        "2. <b>Efetividade do vínculo</b> (Caso Nottebohm, CIJ, 1945): para fins de proteção "
        "diplomática, exige-se vínculo efetivo entre o nacional e o Estado patrial; sem esse "
        "vínculo, a nacionalidade não é reconhecida para fins de proteção diplomática<br>"
        "<i>Fonte: Anotações – Nacionalidade</i>",
    ),
    (
        "O que decidiu o Caso Barcelona Traction (CIJ, 1970)?",
        "A CIJ reconheceu que <b>pessoas jurídicas podem ter personalidade e nacionalidade</b> "
        "para fins de Direito Internacional, possibilitando a proteção diplomática do Estado "
        "patrial em favor de PJs que tenham seus direitos violados por um Estado estrangeiro.<br>"
        "<i>Fonte: Anotações – Nacionalidade</i>",
    ),
    (
        "O que preveem a DUDH/1948 e o Pacto de San José/1969 sobre nacionalidade?",
        "<b>DUDH/1948, Art. 15</b>: toda pessoa tem direito a <i>uma</i> nacionalidade e "
        "de mudar sua nacionalidade.<br>"
        "<b>Pacto de San José da Costa Rica/1969, Art. 20</b>: toda pessoa tem direito à "
        "nacionalidade; combate a apatridia — assegura o direito à nacionalidade do lugar "
        "onde nasceu se não tiver outra.<br>"
        "<i>Fonte: Anotações – Nacionalidade</i>",
    ),

    # ── PERDA DA NACIONALIDADE ────────────────────────────────────────────────
    (
        "Quais são as hipóteses de perda da nacionalidade brasileira após a EC 131/2023?",
        "Art. 12, §4 CF/88 (EC 131/2023) — duas hipóteses:<br>"
        "1. <b>Sentença judicial</b>: cancelamento por fraude na naturalização ou atentado "
        "contra a ordem constitucional e o Estado democrático → <i>só naturalizados</i><br>"
        "2. <b>Processo administrativo</b>: pedido expresso ao Ministro da Justiça → "
        "<i>natos e naturalizados</i>, salvo risco de apatridia<br>"
        "⚠️ Atividade nociva ao interesse nacional deixou de ser hipótese autônoma com a EC 131/2023.<br>"
        "<i>Fonte: Anotações – Nacionalidade / Art. 12, §4 CF/88</i>",
    ),
    (
        "Quem readquire a nacionalidade brasileira mantém o status de nato ou de naturalizado?",
        "Mantém a <b>condição originária</b>: brasileiro nato que readquire a nacionalidade "
        "retorna como <b>nato</b> (não como naturalizado). A reaquisição não rebaixa o "
        "status da nacionalidade prévia.<br>"
        "<i>Fonte: Anotações – Nacionalidade / Art. 76, Lei 13.445/2017</i>",
    ),

    # ── BRASILEIRO NATO ───────────────────────────────────────────────────────
    (
        "Quais são os critérios para aquisição da nacionalidade brasileira originária (nato)?",
        "<b>1. Jus Soli</b> (critério primário): nascimento em território brasileiro, "
        "mesmo que pais sejam estrangeiros.<br>"
        "→ Exceção: pais estrangeiros a serviço do próprio país → filho <i>não</i> é nato.<br><br>"
        "<b>2. Jus Sanguinis</b>: nascido no exterior, filho de pai ou mãe brasileiro(a). "
        "Três sub-critérios (basta um): aquisição automática (genitor a serviço do Brasil), "
        "registro consular, ou nacionalidade potestativa (após 18 anos + residência + opção).<br>"
        "<i>Fonte: Anotações – Nacionalidade / Art. 12, I CF/88</i>",
    ),
    (
        "O que é a nacionalidade potestativa e quais são seus 3 requisitos cumulativos?",
        "Modalidade do <b>jus sanguinis</b> para filho nascido no exterior cujos pais "
        "brasileiros não estavam a serviço do Brasil e não realizaram registro consular.<br>"
        "Requisitos cumulativos:<br>"
        "1. <b>Ter 18 anos</b> (maioridade civil)<br>"
        "2. <b>Residir no Brasil</b><br>"
        "3. <b>Optar pela nacionalidade brasileira</b> — a qualquer tempo (não há prazo)<br>"
        "<i>Fonte: Anotações – Nacionalidade / Art. 12, I, c CF/88</i>",
    ),

    # ── NATURALIZAÇÃO ─────────────────────────────────────────────────────────
    (
        "Quais são as 3 formas de naturalização previstas na CF/88 e seus requisitos principais?",
        "1. <b>Extraordinária</b>: 15 anos de residência ininterrupta + ausência de condenação "
        "penal → ato vinculado (não pode ser negada se preenchidos os requisitos; STF exige pedido)<br>"
        "2. <b>Países de língua portuguesa</b>: 1 ano de residência ininterrupta + idoneidade "
        "moral → discricionária<br>"
        "3. <b>Na forma da lei</b>: hipóteses definidas em legislação infraconstitucional "
        "(Lei 13.445/2017)<br>"
        "<i>Fonte: Anotações – Nacionalidade / Art. 12, II CF/88</i>",
    ),
    (
        "Quais são as 3 hipóteses de naturalização da Lei de Migração (Lei 13.445/2017)?",
        "1. <b>Ordinária</b> (Art. 65-66): 4 anos residência (reduzível a 1 ano: filho br, "
        "cônjuge br ou serviço relevante); comunicação em português; capacidade civil; sem "
        "condenação penal<br>"
        "2. <b>Especial</b> (Art. 68-69): sem exigência de residência — para cônjuge de "
        "integrante do serviço exterior por 5+ anos OU quem trabalhou 10+ anos para missão "
        "diplomática do Brasil<br>"
        "3. <b>Provisória</b> (Art. 70): criança migrante (&lt;10 anos); requerida pelo "
        "representante legal; após a maioridade tem 2 anos para converter em definitiva<br>"
        "<i>Fonte: Anotações – Nacionalidade / Lei 13.445/2017</i>",
    ),

    # ── EXERCÍCIOS — Q01 (Rodada 02 – Nov/2023) ──────────────────────────────
    (
        "[Exercício] I – Consoante a DUDH/1948, toda pessoa tem direito à nacionalidade do "
        "Estado em cujo território houver nascido, se não tiver direito a outra.",
        "<b>ERRADO.</b> O Art. 15 da DUDH garante o direito a <b>uma</b> nacionalidade e o "
        "direito de mudá-la. Não estabelece que a pessoa tem direito à nacionalidade do Estado "
        "de nascimento — esse é o conteúdo do Art. 20 do Pacto de San José, que trata de "
        "apatridia de forma diferente.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q01-I</i>",
    ),
    (
        "[Exercício] II – Peter, filho de pais norte-americanos em férias no Brasil, nasceu "
        "em Alagoas, foi para os EUA e jamais retornou. Peter é brasileiro nato, sendo "
        "prescindível requerer a nacionalidade brasileira originária.",
        "<b>CERTO.</b> Pelo <b>jus soli</b> (Art. 12, I, a CF/88): nasceu em território "
        "brasileiro e seus pais estrangeiros não estavam a serviço do próprio país (estavam "
        "de férias). A aquisição do jus soli é automática — não requer pedido do interessado.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q01-II</i>",
    ),
    (
        "[Exercício] III – Aos portugueses com residência permanente no País, se houver "
        "reciprocidade, serão atribuídos os direitos inerentes ao brasileiro nato.",
        "<b>ERRADO.</b> O Art. 12, §1º CF/88 prevê que portugueses com residência permanente "
        "e reciprocidade adquirem os direitos inerentes ao <b>brasileiro naturalizado</b>, "
        "não ao nato — salvo exceções expressas na Constituição.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q01-III</i>",
    ),
    (
        "[Exercício] IV – Há vedação constitucional à nomeação de brasileiro naturalizado "
        "para o cargo de Procurador-Geral da República.",
        "<b>ERRADO.</b> O Art. 12, §3º CF/88 lista os cargos privativos de <b>brasileiro nato</b>: "
        "Presidente/VP, Presidentes de Câmara e Senado, Ministro do STF, carreira diplomática, "
        "oficial das Forças Armadas e Ministro da Defesa. PGR <b>não está nessa lista</b> — "
        "brasileiros naturalizados podem exercer o cargo.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – Entende-se por nacionalidade potestativa aquela em que o filho, "
        "nascido no exterior de pai ou mãe brasileira não a serviço do Brasil, venha a residir "
        "no Brasil e opte, a qualquer tempo após a maioridade, pela nacionalidade brasileira.",
        "<b>CERTO.</b> Definição correta da <b>nacionalidade potestativa</b> (Art. 12, I, c "
        "CF/88): filho de genitor brasileiro, nascido no exterior sem que o pai/mãe estivesse "
        "a serviço do Brasil e sem registro consular, pode optar pela nacionalidade brasileira "
        "a qualquer tempo após os 18 anos, desde que resida no Brasil.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q02-I</i>",
    ),
    (
        "[Exercício] II – Catarina é russa e há 16 anos ininterruptos reside no Brasil. "
        "Ela precisa comprovar idoneidade moral para ser naturalizada.",
        "<b>ERRADO.</b> Com 15+ anos de residência ininterrupta e sem condenação penal, "
        "Catarina se enquadra na <b>naturalização extraordinária</b> (Art. 12, II, b CF/88). "
        "Essa modalidade <b>não exige idoneidade moral</b> — esse requisito é exclusivo da "
        "naturalização de originários de países de língua portuguesa.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q02-II</i>",
    ),
    (
        "[Exercício] III – A aquisição de outra nacionalidade não acarreta perda da "
        "nacionalidade brasileira apenas se a norma estrangeira impuser a naturalização como "
        "condição para permanência no país.",
        "<b>ERRADO.</b> As exceções à perda são mais amplas (Art. 12, §4 CF/88): <br>"
        "(a) reconhecimento de <i>nacionalidade originária</i> pela lei estrangeira; e<br>"
        "(b) imposição de naturalização como condição para permanência <i>ou</i> para o "
        "exercício de direitos civis. O item omite a alínea (a) e restringe indevidamente a (b).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q02-III</i>",
    ),
    (
        "[Exercício] IV – Não constitui causa de perda da nacionalidade brasileira derivada "
        "a prática de atividade nociva ao interesse nacional.",
        "<b>CERTO.</b> Após a <b>EC 131/2023</b>, o Art. 12, §4 CF/88 passou a prever apenas "
        "duas causas de perda por sentença judicial: fraude no processo de naturalização e "
        "atentado contra a ordem constitucional e o Estado democrático. <i>Atividade nociva "
        "ao interesse nacional</i> foi removida como hipótese autônoma pela EC 131/2023.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ──────────────────────────────────────────────────────
    (
        "[Exercício] I – O prazo de residência na naturalização ordinária é reduzido para "
        "1 ano se o naturalizando tiver filho brasileiro ou cônjuge/companheiro brasileiro "
        "com quem não esteja separado.",
        "<b>CERTO.</b> Art. 65, §1º da Lei 13.445/2017: o prazo mínimo de 4 anos é reduzido "
        "para <b>1 ano</b> nos casos de filho brasileiro nato ou naturalizado, cônjuge ou "
        "companheiro brasileiro não separado legalmente ou de fato, entre outros.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q03-I</i>",
    ),
    (
        "[Exercício] II – A naturalização provisória pode ser concedida ao migrante criança "
        "que fixou residência no Brasil antes dos 10 anos, requerida pelo representante legal.",
        "<b>CERTO.</b> Art. 70 da Lei 13.445/2017: a naturalização provisória exige fixação "
        "de residência antes dos 10 anos e deve ser requerida pelo representante legal. "
        "Após atingir a maioridade, o naturalizado tem <b>2 anos</b> para requerer a "
        "conversão para naturalização definitiva.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q03-II</i>",
    ),
    (
        "[Exercício] III – A naturalização especial será concedida a pessoa fixada no Brasil "
        "há mais de 15 anos ininterruptos e sem condenação penal.",
        "<b>ERRADO.</b> 15 anos de residência ininterrupta + ausência de condenação penal é "
        "requisito da <b>naturalização extraordinária</b> (Art. 12, II, b CF/88). A "
        "<b>naturalização especial</b> (Art. 68-69 da Lei 13.445/2017) não exige residência "
        "no Brasil — aplica-se a cônjuge de integrante do serviço exterior ou a quem "
        "trabalhou 10+ anos para missão diplomática do Brasil.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q03-III</i>",
    ),
    (
        "[Exercício] IV – Brasileiro nato que perdeu a nacionalidade por adquirir outra "
        "poderá readquiri-la, mas terá o status de brasileiro naturalizado.",
        "<b>ERRADO.</b> A reaquisição da nacionalidade brasileira preserva a <b>condição "
        "originária</b> do requerente: brasileiro nato que readquire a nacionalidade retorna "
        "como <b>nato</b>, não como naturalizado. O Art. 76 da Lei 13.445/2017 e a "
        "jurisprudência confirmam essa interpretação.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 02, Nov/2023, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD::OWN::Direito Internacional::Nacionalidade",
        "Direito Internacional - Nacionalidade.apkg",
        CARDS,
    )
