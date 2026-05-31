#!/usr/bin/env python3
"""Gera deck Anki: Direito Internacional - Direito Internacional Privado"""

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


DIPRIVADO = [
    # ── CONCEITO ───────────────────────────────────────────────────────────────
    (
        "O que é o Direito Internacional Privado (DIPr) e como se diferencia do DIP?",
        "O DIPr <b>não</b> disciplina relações entre Estados no exercício da soberania (isso é DIP). "
        "Cuida de relações <b>particulares</b> em casos concretos com 3 fatores cumulativos: "
        "(1) envolve particulares, (2) matéria de direito privado, (3) fato jurídico multiconectado.<br>"
        "<i>Fonte: Anotações – DIPrivado</i>",
    ),
    (
        "Quais são os 3 fatores cumulativos que identificam um caso de DIPr?",
        "1. <b>Particulares</b>: interesses de pessoas físicas ou PJ de direito privado "
        "(Estados podem ser implicados quando praticam atos de gestão, não de soberania).<br>"
        "2. <b>Direito Privado</b>: conectado ao direito civil (contratos, casamento, sucessão).<br>"
        "3. <b>Fato jurídico multiconectado</b>: o caso pode envolver legislação brasileira <i>e</i> "
        "estrangeira.<br>"
        "<i>Fonte: Anotações – DIPrivado</i>",
    ),
    (
        "O que é o 'conflito de leis no espaço' e qual o papel do DIPr?",
        "Situação em que um caso concreto está conectado a dois ou mais ordenamentos jurídicos. "
        "O DIPr não julga o mérito — apenas <b>indica qual legislação deve ser aplicada</b> "
        "(soluciona o conflito de leis no espaço). A fonte primária no Brasil é a LINDB, "
        "não tratados internacionais.<br>"
        "<i>Fonte: Anotações – DIPrivado</i>",
    ),

    # ── APLICAÇÃO DA LEI ESTRANGEIRA ────────────────────────────────────────────
    (
        "O que prevê o art. 17 da LINDB sobre os limites à aplicação da lei estrangeira?",
        "A lei estrangeira <b>não</b> será aplicada no Brasil se ofender:<br>"
        "1. Ordem pública<br>2. Soberania nacional<br>3. Bons costumes<br>"
        "Nesses casos, aplica-se a lei brasileira. A verificação desses limites cabe ao juiz.<br>"
        "<i>Fonte: Art. 17 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "O que prevê o art. 13 da LINDB sobre provas de fatos ocorridos no exterior?",
        "A produção de provas de fatos ocorridos no exterior segue a <b>lei do Estado estrangeiro</b>. "
        "Contudo, os tribunais brasileiros <b>não admitem</b> provas que a lei brasileira desconheça — "
        "a prova é produzida no exterior e admitida no Brasil se reconhecida pelo ordenamento pátrio.<br>"
        "<i>Fonte: Art. 13 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "O que prevê o art. 14 da LINDB sobre a comprovação da lei estrangeira?",
        "Não conhecendo a lei estrangeira, o juiz pode exigir que a <b>parte que a invocou</b> "
        "prove seu texto e vigência.<br>"
        "<i>Fonte: Art. 14 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "O que é a homologação de sentença estrangeira e a quem compete?",
        "Quando o caso multiconectado foi ajuizado no exterior e obteve sentença por autoridade "
        "competente estrangeira, essa sentença precisa ser <b>homologada pelo STJ</b> para ser "
        "executada no Brasil.<br>"
        "<i>Fonte: Anotações – DIPrivado</i>",
    ),

    # ── ELEMENTOS DE CONEXÃO ────────────────────────────────────────────────────
    (
        "O que são os elementos de conexão no DIPr (LINDB arts. 7–11)?",
        "Critérios que indicam ao juiz brasileiro se deve aplicar a lei <b>brasileira ou estrangeira</b> "
        "para resolver o conflito de leis no espaço. Previstos na LINDB, confirmando que o direito "
        "interno é a fonte primária do DIPr no Brasil.<br>"
        "<i>Fonte: Anotações – DIPrivado</i>",
    ),
    (
        "Elemento de conexão: família, capacidade civil e personalidade jurídica (art. 7 LINDB). "
        "Qual a regra e as exceções?",
        "<b>Regra</b>: aplica-se a <b>lei do domicílio</b> da pessoa.<br>"
        "<b>Exceções</b>:<br>"
        "• §2: casamento de estrangeiros domiciliados no BR celebrado por autoridade consular → "
        "lei do país da embaixada/consulado.<br>"
        "• §3-4: noivos com domicílios diferentes → lei do <b>primeiro domicílio conjugal</b>.<br>"
        "<i>Fonte: Art. 7 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "Elemento de conexão: contratos e obrigações (art. 9 LINDB). Qual a regra?",
        "<b>Regra (lex loci contractus)</b>: aplica-se a lei do <b>local onde o contrato foi "
        "constituído/celebrado</b>. A LINDB não prevê autonomia da vontade para escolha da lei.<br>"
        "<b>§2 (contratos entre ausentes)</b>: aplica-se a lei do domicílio do <b>proponente</b> "
        "(quem oferece o bem/serviço).<br>"
        "<i>Fonte: Art. 9 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "Elemento de conexão: sucessão (art. 10 LINDB). Qual a regra geral e a exceção?",
        "<b>Regra</b>: lei do <b>domicílio do de cujus</b>, independentemente da natureza dos bens.<br>"
        "<b>Exceção (art. 10 §1 + art. 5, XXXI CF)</b> — aplica-se a lei brasileira se "
        "<i>cumulativamente</i>:<br>"
        "1. Bens situados no Brasil<br>"
        "2. Cônjuge ou filhos brasileiros<br>"
        "3. Lei brasileira mais favorável a esses herdeiros<br>"
        "<i>Fonte: Art. 10 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "Elementos de conexão: qualificação de bens (art. 8) e funcionamento de pessoas jurídicas "
        "(art. 11 LINDB).",
        "<b>Bens (art. 8)</b>: qualificação (principal, acessório etc.) pela lei do <b>local onde "
        "os bens estão situados</b>.<br>"
        "<b>Pessoas jurídicas (art. 11)</b>: funcionamento e organização regidos pela lei do "
        "<b>local de constituição/registro</b> da PJ.<br>"
        "<i>Fonte: Arts. 8 e 11 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "O que prevê o art. 11 §§2 e 3 da LINDB sobre aquisição de bens por Estados estrangeiros "
        "no Brasil?",
        "<b>Regra</b>: Estados estrangeiros (e suas estatais/fundações) estão <b>proibidos</b> de "
        "adquirir bens imóveis ou suscetíveis de desapropriação no Brasil.<br>"
        "<b>Exceção</b>: podem adquirir a propriedade dos prédios necessários para sediar "
        "<b>representantes diplomáticos ou consulares</b>.<br>"
        "<i>Fonte: Art. 11 §§2-3 LINDB / Anotações – DIPrivado</i>",
    ),
    (
        "O que é o reenvio e por que é proibido no Brasil (art. 16 LINDB)?",
        "<b>Reenvio</b>: quando a lei estrangeira indicada pelo elemento de conexão remete o caso "
        "a um <b>terceiro ordenamento</b>.<br>"
        "O art. 16 da LINDB <b>proíbe</b> o reenvio: se ocorrer, o juiz brasileiro aplica a "
        "<b>lei brasileira</b> em vez de seguir a cadeia de remissões.<br>"
        "<i>Fonte: Art. 16 LINDB / Anotações – DIPrivado</i>",
    ),

    # ── EXERCÍCIOS — Q01 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – O Direito Internacional Privado trata principalmente do conflito de leis "
        "originárias de Estados diferentes, estabelecendo regras para a opção entre as leis em "
        "conflito, sendo por isso um direito eminentemente nacional.",
        "<b>CERTO.</b> O DIPr é eminentemente nacional — sua fonte primária no Brasil é a LINDB, "
        "não tratados internacionais. Sua função é estabelecer qual lei (brasileira ou estrangeira) "
        "se aplica ao caso multiconectado.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q01-I</i>",
    ),
    (
        "[Exercício] II – Ao Direito Internacional Privado não cabe solucionar o conflito das "
        "normas materiais internas, mas tão somente indicar qual sistema jurídico deve ser aplicado "
        "dentre as várias legislações conectadas com a hipótese jurídica.",
        "<b>CERTO.</b> O DIPr não julga o mérito nem resolve o conflito material em si — apenas "
        "aponta qual ordenamento jurídico deve reger o caso concreto.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q01-II</i>",
    ),
    (
        "[Exercício] III – De acordo com a LINDB, a autonomia da vontade não prevalece sobre a "
        "'lex loci contractus', uma vez que as obrigações se regem e se qualificam no país em que "
        "se constituírem.",
        "<b>CERTO.</b> O art. 9 da LINDB adota a <i>lex loci contractus</i> (lei do local de "
        "constituição do contrato) sem prever autonomia da vontade das partes para escolha da lei "
        "aplicável.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q01-III</i>",
    ),
    (
        "[Exercício] IV – As regras sobre o começo e o fim da personalidade, o nome, a capacidade "
        "ou o direito de família de brasileiro que tenha outra nacionalidade são determinadas pela "
        "lei do país de nascimento do indivíduo.",
        "<b>ERRADO.</b> O art. 7 da LINDB adota como elemento de conexão a lei do <b>domicílio</b> "
        "da pessoa, não a lei do país de nascimento.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q01-IV</i>",
    ),

    # ── EXERCÍCIOS — Q02 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – Para resolver os conflitos de lei no espaço, o Brasil adota a prática do "
        "reenvio, mediante a qual se substitui a lei nacional pela estrangeira, desprezando-se o "
        "elemento de conexão apontado pela ordenação nacional, para dar preferência à indicada pelo "
        "ordenamento jurídico alienígena.",
        "<b>ERRADO.</b> O Brasil <b>proíbe</b> expressamente o reenvio (art. 16 LINDB). Quando a "
        "lei estrangeira indicada remete a um terceiro ordenamento, aplica-se a lei brasileira.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q02-I</i>",
    ),
    (
        "[Exercício] II – Na aplicação de lei estrangeira, o magistrado deve ater-se a ela, mas "
        "poderá, excepcionalmente, usar remissão ou indicação que a lei estrangeira faça a uma "
        "outra lei.",
        "<b>ERRADO.</b> Isso configuraria reenvio, expressamente vedado pelo art. 16 da LINDB. "
        "O magistrado não pode seguir a remissão da lei estrangeira a outro ordenamento.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q02-II</i>",
    ),
    (
        "[Exercício] III – A prova dos fatos ocorridos em país estrangeiro rege-se pela lei que "
        "nele vigorar, quanto ao ônus e aos meios de produzir-se, não admitindo, porém, os "
        "tribunais brasileiros provas que a lei brasileira desconheça.",
        "<b>CERTO.</b> Art. 13 da LINDB: provas de fatos no exterior seguem a lei estrangeira, "
        "mas os tribunais brasileiros não admitem provas que o ordenamento pátrio desconheça.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q02-III</i>",
    ),
    (
        "[Exercício] IV – Governos estrangeiros não podem adquirir no Brasil bens imóveis ou "
        "suscetíveis de desapropriação, exceto a propriedade dos prédios necessários à sede dos "
        "representantes diplomáticos ou dos agentes consulares.",
        "<b>CERTO.</b> Art. 11 §§2-3 da LINDB: proibição geral de aquisição de imóveis por "
        "Estados estrangeiros, com exceção expressa para os prédios destinados às sedes "
        "diplomáticas e consulares.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q02-IV</i>",
    ),

    # ── EXERCÍCIOS — Q03 ───────────────────────────────────────────────────────
    (
        "[Exercício] I – As partes têm liberdade para escolher a lei de regência em contratos "
        "internacionais em razão da regra geral da autonomia da vontade, em matéria contratual. "
        "Nesse sentido, as leis, atos e sentenças de outro país, bem como quaisquer declarações "
        "de vontade, terão plena eficácia no Brasil, independentemente de qualquer condição ou "
        "ressalva.",
        "<b>ERRADO.</b> Dois erros: (1) a LINDB não prevê autonomia da vontade — impõe a "
        "<i>lex loci contractus</i> (art. 9); (2) leis estrangeiras têm limites no Brasil: "
        "não podem ofender a ordem pública, a soberania nacional e os bons costumes (art. 17).<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q03-I</i>",
    ),
    (
        "[Exercício] II – A sucessão de bens de estrangeiro situados no Brasil é regulada pela "
        "lei brasileira em benefício do cônjuge e filhos brasileiros, ou de quem os represente, "
        "sempre que não lhes seja mais favorável a lei pessoal do 'de cujus'.",
        "<b>CERTO.</b> Art. 10 §1 da LINDB + art. 5, XXXI, CF/88: a lei brasileira prevalece na "
        "sucessão se houver bens no Brasil, cônjuge ou filhos brasileiros, e a lei brasileira for "
        "mais favorável a esses herdeiros.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q03-II</i>",
    ),
    (
        "[Exercício] III – A reserva da ordem pública não está expressa na Lei de Introdução às "
        "Normas do Direito Brasileiro.",
        "<b>ERRADO.</b> O art. 17 da LINDB prevê <b>expressamente</b> a ordem pública como um "
        "dos três limites à aplicação da lei estrangeira no Brasil.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q03-III</i>",
    ),
    (
        "[Exercício] IV – A regra geral, ante o conflito de leis no espaço, é a aplicação do "
        "direito estrangeiro, empregando-se o direito brasileiro, quando isso for expressamente "
        "determinado por tratado internacional do qual o Brasil figure como parte.",
        "<b>ERRADO.</b> É o oposto: os <b>elementos de conexão da LINDB</b> (direito interno) "
        "determinam quando se aplica o direito estrangeiro ou o brasileiro. O DIPr brasileiro é "
        "de fonte primariamente nacional, não convencional.<br>"
        "<i>Fonte: Exercícios objetivos – DIP Rodada 01 Mar/2024, Q03-IV</i>",
    ),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Direito Internacional :: Direito Internacional Privado (LINDB)",
        "Direito Internacional - DIPrivado.apkg",
        DIPRIVADO,
    )
