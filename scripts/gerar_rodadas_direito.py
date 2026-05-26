#!/usr/bin/env python3
"""Gera decks Anki para Direito Interno — Rodadas do professor.

Rodada 02 (Set/2023): Normas Jurídicas (Item 1 do Edital)
Rodada 01 (Jan/2024): Personalidade Jurídica (Item 2 do Edital)
"""
import genanki
import random
import os

DECK_DIR = "/Users/isabelamarantes/Desktop/cacd-learning/anki/decks/direito"
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


# ══════════════════════════════════════════════════════════════════════════════
# RODADA 02 — NORMAS JURÍDICAS (Item 1 do Edital CACD)
# Fonte: Direito Interno_Rodada 02_Setembro_2023.pdf
# ══════════════════════════════════════════════════════════════════════════════

NORMAS_JURIDICAS = [

    # ── DOUTRINA ──────────────────────────────────────────────────────────────

    ("Quem teorizou o poder constituinte originário e em qual obra?",
     "Abade Sièyes, em <i>Que é o Terceiro Estado?</i> (1789) — manifesto da Revolução Francesa. "
     "[Mendes/Coelho/Branco, Curso Dir. Const., 5ª ed., p. 273]"),

    ("Qual a relação entre Constituição e poder constituinte originário segundo Sièyes?",
     "A Constituição é produto do PCO, que gera e organiza os poderes constituídos, sendo superior a eles. "
     "O povo é soberano para ordenar seu destino por meio da Constituição. "
     "[Mendes/Coelho/Branco, p. 273]"),

    ("Como a Constituição pode ser modificada por via formal?",
     "Por reforma constitucional (emenda), procedimento previsto na própria Carta, mais complexo que a legislação "
     "ordinária — o que caracteriza a rigidez constitucional. "
     "[Barroso, Curso Dir. Const. Contemporâneo, 11ª ed., p. 258]"),

    ("O que é mutação constitucional?",
     "Alteração por via informal: transformação do sentido e do alcance de normas constitucionais sem modificação "
     "do texto, decorrente da plasticidade das normas constitucionais. "
     "[Barroso, p. 258]"),

    ("O que é o poder constituinte difuso?",
     "Terceira modalidade de poder constituinte: exerce-se permanentemente por mecanismos informais "
     "(interpretação das normas e costumes constitucionais), não expressamente previsto na CF mas por ela admitido. "
     "Titularidade remanesce no povo. [Barroso, p. 265]"),

    # ── LEGISLAÇÃO ────────────────────────────────────────────────────────────

    ("Quem tem legitimidade para propor emenda à Constituição? (art. 60, I-III CF)",
     "1/3 dos membros da Câmara ou do Senado; Presidente da República; mais da metade das Assembleias "
     "Legislativas, manifestando-se cada uma por maioria relativa de seus membros."),

    ("Qual o quórum e o rito de aprovação de emenda constitucional? (art. 60, §2º CF)",
     "Discussão e votação em cada Casa do Congresso em <b>dois turnos</b>; aprovação por "
     "<b>3/5 dos respectivos membros</b> em ambos os turnos de ambas as Casas."),

    ("Quais são as cláusulas pétreas? (art. 60, §4º CF)",
     "São insuscetíveis de deliberação por proposta de emenda: (I) forma federativa de Estado; "
     "(II) voto direto, secreto, universal e periódico; (III) separação dos Poderes; "
     "(IV) direitos e garantias individuais."),

    ("Em que situações a CF não pode ser emendada? (art. 60, §1º CF)",
     "Na vigência de <b>intervenção federal</b>, de <b>estado de defesa</b> ou de <b>estado de sítio</b> "
     "(limitações circunstanciais ao poder constituinte derivado reformador)."),

    ("Após rejeição de proposta de emenda, quando pode ser reapresentada? (art. 60, §5º CF)",
     "Não pode ser reapresentada na mesma <b>sessão legislativa</b> (ano). "
     "Porém <b>pode</b> ser reapresentada em outra sessão legislativa dentro da mesma legislatura (quadriênio). "
     "Atenção: sessão legislativa ≠ legislatura."),

    ("O que previa o art. 3º do ADCT sobre revisão constitucional?",
     "Revisão a realizar após 5 anos da promulgação da CF, por <b>maioria absoluta</b> dos membros do CN "
     "em <b>sessão unicameral</b>. Poder revisor exaurido em 1993-1994 — não pode ser convocado novamente."),

    # ── JURISPRUDÊNCIA ────────────────────────────────────────────────────────

    ("Normas do poder constituinte originário estão sujeitas a controle de constitucionalidade pelo STF?",
     "<b>Não.</b> A eficácia das regras do PCO não está sujeita a limitações normativas (material ou formal), "
     "pois provém de poder de fato ou suprapositivo. Apenas normas do poder reformador (emendas) submetem-se "
     "ao controle. (STF, ADI 2.356 e ADI 2.362, rel. min. Ayres Britto)"),

    ("Cabe ADI contra emenda constitucional?",
     "<b>Sim</b> — quando se alega que a emenda contraria princípios imutáveis ou cláusulas pétreas "
     "do art. 60, §4º CF. O STF pode conhecer da ação e declarar a emenda inconstitucional. "
     "(STF, ADI 1.946 MC, rel. min. Sydney Sanches; precedente: ADI 939)"),

    ("As cláusulas pétreas tornam intangível todo o texto original da CF?",
     "<b>Não</b> — protegem apenas o <b>núcleo essencial</b> dos princípios e institutos, "
     "não a intangibilidade literal de sua disciplina na Constituição originária. "
     "Ex.: a forma federativa é pétrea, mas a distribuição exata de competências pode ser alterada. "
     "(STF, ADI 2.024, rel. min. Sepúlveda Pertence)"),

    ("A interpretação judicial é forma legítima de mutação constitucional?",
     "<b>Sim</b> — o STF reconhece a interpretação judicial como instrumento juridicamente idôneo de mudança "
     "informal da Constituição, compatibilizando-a com novas exigências, necessidades e transformações sociais, "
     "econômicas e políticas. (STF, HC 91.361, rel. min. Celso de Mello)"),

    # ── EXERCÍCIOS DO PROFESSOR (frente: enunciado paráfrase; verso: resposta + fundamentação) ──

    ("EXERCÍCIO — O poder constituinte derivado está juridicamente no mesmo nível do poder constituinte "
     "originário, pois ambos têm a capacidade de gerar e alterar a Constituição. (C/E?)",
     "<b>ERRADO.</b> O PCO é superior ao PCD: cria a Constituição sem se vincular a normas anteriores, "
     "enquanto o derivado atua nos termos e limites estabelecidos pelo PCO — inclusive submetendo-se "
     "às cláusulas pétreas. São poderes de natureza e hierarquia distintas."),

    ("EXERCÍCIO — As limitações admitidas em face do poder constituinte originário permitem que o STF "
     "aprecie, em controle de constitucionalidade, as normas por ele produzidas. (C/E?)",
     "<b>ERRADO.</b> Normas do PCO são suprapositivas e não se submetem a controle de constitucionalidade. "
     "O STF controla apenas emendas (poder derivado reformador), nunca a Constituição originária. "
     "(STF, ADI 2.356 e 2.362)"),

    ("EXERCÍCIO — O poder constituinte originário esgota-se quando é editada uma Constituição, "
     "caracterizando-se pela temporariedade. (C/E?)",
     "<b>ERRADO.</b> O PCO é <b>permanente</b> (latente): não se esgota com a promulgação da CF. "
     "Pode ressurgir a qualquer momento em que o povo exerça novamente o poder constituinte. "
     "Suas características são: inicial, incondicionado, ilimitado e permanente — não temporário."),

    ("EXERCÍCIO — Para a doutrina majoritária, não existem limites implícitos ao poder constituinte "
     "derivado reformador; é possível adotar a teoria da dupla revisão. (C/E?)",
     "<b>ERRADO.</b> A doutrina majoritária reconhece limites implícitos ao PCD reformador e rejeita "
     "a teoria da dupla revisão (que usaria emendas para eliminar cláusulas pétreas e, na sequência, "
     "suprimir as matérias protegidas — manobra vedada pelo sistema)."),

    ("EXERCÍCIO — A Constituição não poderá ser emendada na vigência de intervenção federal, "
     "de estado de defesa ou de estado de sítio. (C/E?)",
     "<b>CORRETO.</b> Art. 60, §1º CF — limitação circunstancial ao poder constituinte derivado reformador. "
     "O objetivo é impedir que situações de crise sejam aproveitadas para alterar a Constituição."),

    ("EXERCÍCIO — O poder reformador e o revisor podem ser manifestados a qualquer tempo, "
     "mediante o voto de 3/5 de cada Casa em dois turnos. (C/E?)",
     "<b>ERRADO.</b> O poder <b>revisor</b> (ADCT, art. 3º) foi exaurido em 1994 e não pode ser "
     "manifestado novamente — é poder constituinte de segundo grau com prazo e condições específicas "
     "(maioria absoluta em sessão unicameral). Apenas o poder <b>reformador</b> persiste (3/5, dois turnos)."),

    ("EXERCÍCIO — Matéria de proposta de emenda rejeitada pode ser objeto de nova proposição "
     "na mesma legislatura. (C/E?)",
     "<b>CORRETO.</b> Art. 60, §5º CF veda nova proposta na mesma <b>sessão legislativa</b> (1 ano), "
     "mas não na mesma <b>legislatura</b> (4 anos). A distinção entre sessão legislativa e legislatura "
     "é ponto clássico de prova do CACD."),

    ("EXERCÍCIO — A modificação da Constituição por emendas impossibilita o fenômeno da "
     "mutação constitucional. (C/E?)",
     "<b>ERRADO.</b> São mecanismos distintos e coexistentes: a emenda altera formalmente o texto; "
     "a mutação ocorre informalmente via interpretação e prática constitucional, sem alterar o texto. "
     "A existência de um não exclui o outro."),

    ("EXERCÍCIO — Direitos adquiridos sob a égide de Constituição anterior, ainda que incompatíveis "
     "com a CF atual, devem ser respeitados, pois a própria CF prevê o respeito ao direito adquirido. (C/E?)",
     "<b>ERRADO.</b> O PCO é suprapositivo; a nova CF não se sujeita ao direito anterior. "
     "Não há direito adquirido em face do poder constituinte originário — ele pode revogar "
     "toda e qualquer situação jurídica anterior incompatível com a nova ordem constitucional."),

    ("EXERCÍCIO — Os estados estão obrigados a seguir as regras do processo legislativo federal, "
     "sendo vedado ao constituinte estadual adotar normas sem simetria com o modelo básico da CF. (C/E?)",
     "<b>CORRETO.</b> Princípio da simetria: os estados devem observar o modelo básico da CF/88 quanto "
     "ao processo legislativo, não podendo criar procedimentos mais ou menos rígidos que o federal "
     "sem amparo constitucional. (STF, ADI 486, rel. min. Celso de Mello)"),

    ("EXERCÍCIO — O poder constituinte originário, embora não absoluto, não se subordina hierarquicamente "
     "a normas jurídicas anteriores na acepção jurídico-formal. (C/E?)",
     "<b>CORRETO.</b> O PCO pode ter condicionamentos políticos, morais ou metajurídicos, mas no plano "
     "jurídico-formal não se vincula a nenhuma norma preexistente. É expressão da soberania popular "
     "sem filtro normativo anterior."),

    ("EXERCÍCIO — O poder constituinte derivado decorrente é secundário; por isso, "
     "trata-se de um poder de fato. (C/E?)",
     "<b>ERRADO.</b> Por ter origem na Constituição (secundário), o PCD decorrente é poder <b>jurídico</b> "
     "— condicionado e limitado pela CF. O poder de fato é o poder constituinte <b>originário</b>, "
     "que atua fora e acima da ordem jurídica preexistente."),
]


# ══════════════════════════════════════════════════════════════════════════════
# RODADA 01 — PERSONALIDADE JURÍDICA (Item 2 do Edital CACD)
# Fonte: Direito Interno_Rodada 01_Janeiro_2024.pdf
# ══════════════════════════════════════════════════════════════════════════════

PERSONALIDADE_JURIDICA = [

    # ── DOUTRINA ──────────────────────────────────────────────────────────────

    ("O que é personalidade jurídica?",
     "Aptidão genérica para adquirir direitos e contrair obrigações; toda pessoa tem personalidade "
     "(art. 1º CC). O art. 1º entrosou o conceito de capacidade com o de personalidade. "
     "[Gonçalves, Dir. Civil: Parte Geral, 18ª ed., p. 49]"),

    ("O que é capacidade de direito (de gozo)?",
     "Aptidão para adquirir ou gozar direitos — todos a possuem (art. 1º CC). "
     "É a medida mínima da personalidade; ninguém pode ser privado dela. "
     "[Gonçalves, p. 49]"),

    ("O que é capacidade de fato (de exercício ou de ação)?",
     "Aptidão para exercer <b>pessoalmente</b> os atos da vida civil. Nem todos a possuem: "
     "ex., menores de 16 anos têm capacidade de direito (podem herdar), mas não de fato "
     "(precisam ser representados). [Gonçalves, p. 49]"),

    # ── LEGISLAÇÃO ────────────────────────────────────────────────────────────

    ("Quando começa e quando termina a personalidade civil da pessoa natural? (arts. 2º e 6º CC)",
     "<b>Começa:</b> nascimento com vida (art. 2º CC) — a lei protege os direitos do nascituro desde "
     "a concepção. <b>Termina:</b> com a morte (art. 6º); presume-se a morte dos ausentes nos casos "
     "em que a lei autoriza a abertura de sucessão definitiva."),

    ("Quem é absolutamente incapaz após o Estatuto da Pessoa com Deficiência (Lei 13.146/2015)?",
     "Apenas os <b>menores de 16 anos</b> (art. 3º CC). O critério passou a ser exclusivamente etário: "
     "eliminadas as hipóteses de deficiência mental ou intelectual anteriormente previstas no CC. "
     "(Lei 13.146/2015 — ratifica Convenção da ONU sobre Direitos das Pessoas com Deficiência)"),

    ("Quais são os relativamente incapazes? (art. 4º CC)",
     "I — maiores de 16 e menores de 18 anos; "
     "II — ébrios habituais e viciados em tóxico; "
     "III — quem, por causa transitória ou permanente, não puder exprimir vontade; "
     "IV — pródigos. Parágrafo único: capacidade dos indígenas regulada por legislação especial."),

    ("Em quais situações cabe morte presumida sem decretação de ausência? (art. 7º CC)",
     "I — morte extremamente provável de quem estava em perigo de vida; "
     "II — desaparecido em campanha ou feito prisioneiro, não encontrado até <b>2 anos</b> após o fim da guerra. "
     "A declaração só pode ser requerida após esgotadas buscas; a sentença fixa a data provável do falecimento."),

    ("Quais são as pessoas jurídicas de direito público interno? (art. 41 CC)",
     "I — União; II — Estados, DF e Territórios; III — Municípios; "
     "IV — autarquias, inclusive associações públicas; V — demais entidades de caráter público criadas por lei."),

    ("Quais são as pessoas jurídicas de direito público externo? (art. 42 CC)",
     "Estados estrangeiros e <b>todas as pessoas</b> regidas pelo direito internacional público "
     "(ex.: organismos internacionais com personalidade jurídica própria)."),

    ("Quais são as pessoas jurídicas de direito privado? (art. 44 CC)",
     "I — associações; II — sociedades; III — fundações; "
     "IV — organizações religiosas; V — partidos políticos. "
     "<b>Atenção:</b> partidos políticos são PJ de direito PRIVADO — adquirem personalidade pela lei civil "
     "e registram estatutos no TSE (art. 17, §2º CF)."),

    ("Quando começa a existência legal de pessoa jurídica de direito privado? (art. 45 CC)",
     "Com a <b>inscrição do ato constitutivo no respectivo registro</b>, precedida, quando necessário, "
     "de autorização ou aprovação do Poder Executivo. "
     "Decai em 3 anos o direito de anular a constituição por defeito do ato (contado da publicação)."),

    ("Quais são os requisitos para desconsideração da personalidade jurídica? (art. 50 CC)",
     "Abuso da personalidade jurídica caracterizado por: "
     "(a) <b>desvio de finalidade</b> (uso da PJ para lesar credores ou praticar atos ilícitos) OU "
     "(b) <b>confusão patrimonial</b>. "
     "A mera existência de grupo econômico <b>não autoriza</b> a desconsideração (art. 50, §4º)."),

    # ── JURISPRUDÊNCIA ────────────────────────────────────────────────────────

    ("A União pode celebrar tratados que isentem tributos estaduais/municipais?",
     "<b>Sim</b> — a vedação do art. 151, III CF aplica-se às relações domésticas entre PJ de direito "
     "público interno. Ao celebrar tratados, atua a <b>República Federativa do Brasil</b> (PJ de DI público), "
     "que detém o treaty making power e o monopólio da soberania e personalidade internacional. "
     "(STF, RE 543.943 AgR, rel. min. Celso de Mello)"),

    ("O nascituro tem direito a danos morais pela morte do pai?",
     "<b>Sim</b> — o STJ reconhece o direito do nascituro a danos morais pela morte do pai; "
     "a circunstância de não tê-lo conhecido em vida influencia na fixação do <i>quantum</i>. "
     "(STJ, AREsp 150.297, rel. min. Sidnei Beneti; REsp 399.028/SP)"),

    ("Após o Estatuto da PcD, portador de Alzheimer sem discernimento é absolutamente incapaz?",
     "<b>Não</b> — após a Lei 13.146/2015, somente menores de 16 anos são absolutamente incapazes. "
     "Portadores de Alzheimer são <b>relativamente incapazes</b> (art. 4º, III CC). "
     "O objetivo do estatuto é promover inclusão social e autonomia, não reduzir proteção. "
     "(STJ, rel. min. Marco Aurélio Bellizze)"),

    # ── EXERCÍCIOS DO PROFESSOR ───────────────────────────────────────────────

    ("EXERCÍCIO — A personalidade civil da pessoa natural tem início a partir do nascimento com vida, "
     "independentemente do preenchimento de qualquer requisito psíquico. (C/E?)",
     "<b>CORRETO.</b> Art. 2º CC: basta o nascimento com vida. Não há exigência de consciência, "
     "discernimento ou qualquer requisito psíquico. Mesmo um recém-nascido em estado vegetativo "
     "adquire plena personalidade."),

    ("EXERCÍCIO — Conforme a teoria natalista, o nascituro é pessoa humana titular de direitos, "
     "de modo que mesmo o natimorto possui proteção quanto aos direitos da personalidade. (C/E?)",
     "<b>ERRADO.</b> A teoria <b>natalista</b> não considera o nascituro pessoa: a personalidade "
     "só existe a partir do nascimento com vida. É a teoria <b>concepcionista</b> que trata o nascituro "
     "como pessoa desde a concepção. O CC adota posição intermediária (personalidade condicional)."),

    ("EXERCÍCIO — Com exceção dos absolutamente incapazes, toda pessoa é capaz de direitos e "
     "deveres na ordem civil. (C/E?)",
     "<b>ERRADO.</b> Art. 1º CC: toda pessoa, <b>sem exceção</b>, é capaz de direitos e deveres. "
     "A incapacidade absoluta limita apenas a capacidade de <b>fato</b> (exercício pessoal dos atos), "
     "nunca a capacidade de <b>direito</b> (titularidade de direitos)."),

    ("EXERCÍCIO — Pessoa com paralisia cerebral que não consiga exprimir sua vontade não é "
     "considerada absolutamente incapaz. (C/E?)",
     "<b>CORRETO.</b> Após a Lei 13.146/2015, somente menores de 16 anos são absolutamente incapazes. "
     "Quem não pode exprimir vontade por causa permanente é <b>relativamente incapaz</b> (art. 4º, III CC), "
     "sujeito a curatela — com maior autonomia preservada."),

    ("EXERCÍCIO — A forma prevista na legislação civil de declarar o fim da existência da pessoa "
     "natural é somente pela morte, que será sempre natural ou física. (C/E?)",
     "<b>ERRADO.</b> Além da morte real (natural/física), existe a <b>morte presumida</b>: "
     "sem decretação de ausência (art. 7º CC) e com decretação de ausência (abertura de sucessão "
     "definitiva — art. 6º CC). A morte presumida não é natural nem física."),

    ("EXERCÍCIO — A pessoa passa, a partir do nascimento com vida, a ser sujeito de direitos e "
     "deveres, com exceção de aspectos sucessórios. (C/E?)",
     "<b>ERRADO.</b> Não há exceção para aspectos sucessórios — o nascimento com vida é determinante "
     "também para a sucessão. O nascituro pode ser beneficiado por herança e doação, mas a consolidação "
     "definitiva de seus direitos patrimoniais ocorre com o nascimento com vida."),

    ("EXERCÍCIO — De acordo com o STF, a União, por não ser pessoa jurídica de direito público "
     "interno, não é parte das convenções internacionais adotadas pela RFB. (C/E?)",
     "<b>ERRADO</b> em dois pontos: (1) a União SIM é PJ de direito público interno (art. 41, I CC); "
     "(2) o STF distingue: os tratados são celebrados pela <b>República Federativa do Brasil</b> "
     "(PJ de DI público), não pela União como ente federado doméstico. "
     "(STF, RE 543.943, rel. min. Celso de Mello)"),

    ("EXERCÍCIO — O Senado Federal não tem competência para aprovar previamente a celebração de "
     "tratados relativos a operações financeiras de interesse da União, Estados, DF e Municípios. (C/E?)",
     "<b>CORRETO.</b> A aprovação de tratados cabe ao <b>Congresso Nacional</b> (ambas as casas, via "
     "decreto legislativo — art. 49, I CF). O art. 52, V CF atribui ao Senado competência para "
     "<b>autorizar operações externas</b> de natureza financeira — distinto de aprovar os tratados."),

    ("EXERCÍCIO — A existência legal das pessoas jurídicas de direito privado começa com a inscrição "
     "do ato constitutivo no registro, precedida, quando necessário, de autorização do Poder Executivo. (C/E?)",
     "<b>CORRETO.</b> Art. 45 CC. O registro é ato constitutivo da PJ de direito privado; "
     "a autorização prévia do Poder Executivo é necessária em casos específicos "
     "(ex.: partidos políticos, entidades financeiras)."),

    ("EXERCÍCIO — Os partidos políticos, assim como os Municípios e a União, são pessoas jurídicas "
     "de direito público interno. (C/E?)",
     "<b>ERRADO.</b> Partidos políticos são PJ de <b>direito privado</b> (art. 44, V CC). "
     "Adquirem personalidade pela lei civil e registram estatutos no TSE (art. 17, §2º CF). "
     "Municípios e União são PJ de direito público interno (art. 41 CC)."),

    ("EXERCÍCIO — A personalidade jurídica de uma empresa pode ser desconsiderada sempre que "
     "estiver dificultando o recebimento de quantias líquidas e exigíveis por algum credor. (C/E?)",
     "<b>ERRADO.</b> O inadimplemento isolado não autoriza a desconsideração. "
     "Exige-se abuso da personalidade caracterizado por <b>desvio de finalidade</b> ou "
     "<b>confusão patrimonial</b> (art. 50 CC). A mera dificuldade de recebimento não basta."),

    ("EXERCÍCIO — O registro competente é ato necessário para constituir as pessoas jurídicas de "
     "direito privado, mas não para as de direito público. (C/E?)",
     "<b>CORRETO.</b> As PJ de direito público existem por determinação legal (criadas pela CF ou por lei), "
     "independentemente de registro. As de direito privado requerem inscrição do ato constitutivo "
     "no registro competente (art. 45 CC)."),
]


if __name__ == "__main__":
    make_deck(
        "CACD :: Direito Interno :: Normas Jurídicas",
        "Direito Interno - Normas Juridicas.apkg",
        NORMAS_JURIDICAS,
    )
    make_deck(
        "CACD :: Direito Interno :: Personalidade Jurídica",
        "Direito Interno - Personalidade Juridica.apkg",
        PERSONALIDADE_JURIDICA,
    )
    print(f"\n🎉 2 decks gerados em {DECK_DIR}")
