#!/usr/bin/env python3
"""Gera deck Anki — Direito Interno Rodada 01 (Maio/2024).

Tema: Processo Legislativo Brasileiro — LO, LC e EC (Item 7 do Edital CACD).

Fontes:
  - Anotações: Processo Legislativo - Parte 2.md
  - Material do professor: Direito Interno_Rodada 01_Maio_2024_Anotada.pdf
  - Exercícios: Exercícios objetivos_Direito Interno_Rodada 01_Maio_2024.pdf
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


PROCESSO_LEGISLATIVO_PARTE2 = [

    # ── CONTEÚDO (lacunas não cobertas pelos exercícios do professor) ──────────

    ("Como a lei complementar e a lei ordinária diferem apenas quanto à "
     "matéria e ao quórum de aprovação, a edição de lei complementar para "
     "disciplinar tema que admitiria lei ordinária configura "
     "inconstitucionalidade formal, assim como ocorre na hipótese inversa.",
     "<b>ERRADO.</b> Só a hipótese inversa é inconstitucional: lei "
     "<b>ordinária</b> sobre tema reservado à LC viola a cláusula de reserva "
     "de lei complementar (inconstitucionalidade formal). Já a LC sobre tema "
     "que admite LO <b>não</b> gera vício formal, pois o quórum da LO "
     "(maioria simples) está contido no da LC (maioria absoluta, art. 69). "
     "Não há hierarquia entre as espécies. [Anotações da aula; Rodada "
     "01/Mai.2024]"),

    ("O quórum para iniciar a votação de um projeto de lei complementar é "
     "de maioria absoluta dos membros da Casa, ao passo que, para um "
     "projeto de lei ordinária, basta a presença da maioria simples, "
     "aplicando-se a regra geral do art. 47 da CF/88.",
     "<b>ERRADO.</b> O quórum de <b>votação</b> (presença mínima para "
     "iniciar a deliberação) é <b>sempre maioria absoluta</b> dos membros, "
     "tanto para LO quanto para LC. A diferença está no quórum de "
     "<b>aprovação</b>: LO = maioria simples (dos presentes); LC = maioria "
     "absoluta (dos membros, art. 69). A banca troca os dois conceitos. "
     "[Anotações da aula; Rodada 01/Mai.2024]"),

    ("Projeto de lei sobre aumento da remuneração de servidores do "
     "Executivo, apresentado por parlamentar e posteriormente sancionado "
     "pelo Presidente da República, tem seu vício de iniciativa convalidado "
     "pela sanção, por expressar a concordância do titular da competência "
     "reservada.",
     "<b>ERRADO.</b> A sanção <b>não convalida</b> o vício formal de "
     "iniciativa (art. 61, §1º, CF/88): a lei continua inconstitucional. "
     "Para obter uma lei válida, o Presidente deve <b>vetar</b> o projeto "
     "viciado e <b>reapresentá-lo</b> ele mesmo. Pelo princípio da simetria, "
     "a regra vale para Governadores e Prefeitos nos entes subnacionais. "
     "[Anotações da aula; Rodada 01/Mai.2024]"),

    ("Derrubado o veto presidencial em sessão conjunta, o projeto é enviado "
     "ao Presidente da República para promulgação em quarenta e oito horas; "
     "se este não o fizer, a promulgação cabe ao Presidente da Câmara dos "
     "Deputados e, em caso de nova inércia, ao Presidente do Senado Federal.",
     "<b>ERRADO.</b> Art. 66, §§5º e 7º: a ordem é Presidente da República "
     "→ <b>Presidente do Senado</b> → <b>Vice-Presidente do Senado</b>, cada "
     "um com 48 horas. O Presidente da Câmara <b>não tem nenhuma "
     "participação</b> na promulgação de leis — pegadinha clássica. Já a EC "
     "é promulgada pelas Mesas das duas Casas. [Anotações da aula; Rodada "
     "01/Mai.2024]"),

    ("O veto parcial a projeto de lei pode alcançar palavras ou expressões "
     "isoladas do texto, desde que fundamentado em inconstitucionalidade ou "
     "contrariedade ao interesse público, e, uma vez apresentado, só pode "
     "ser afastado por maioria absoluta de deputados e senadores em sessão "
     "conjunta.",
     "<b>ERRADO.</b> A segunda parte está certa (art. 66, §4º: sessão "
     "conjunta, 30 dias, maioria absoluta — o veto não é definitivo). Mas o "
     "veto parcial só pode abranger o <b>texto integral</b> de artigo, "
     "parágrafo, inciso ou alínea (§2º), <b>nunca</b> palavras ou frases "
     "soltas. [Anotações da aula; Rodada 01/Mai.2024]"),

    ("Em projeto de lei de iniciativa de Senador, o Senado Federal atua "
     "como Casa iniciadora e, por força do princípio da prevalência da "
     "vontade da Casa iniciadora, as alterações feitas pela Câmara dos "
     "Deputados como Casa revisora só serão mantidas se o Senado "
     "concordar com elas.",
     "<b>CERTO.</b> Regra: Câmara inicia e Senado revisa (inclusive projetos "
     "do Presidente, do STF e de iniciativa popular). Exceção: projeto de "
     "<b>Senador ou Comissão do Senado</b> inverte os papéis. Pelo art. 65, "
     "parágrafo único, emenda da revisora <b>volta à iniciadora</b>, que "
     "define a versão final. Na EC não há iniciadora nem revisora. "
     "[Anotações da aula; Rodada 01/Mai.2024]"),

    ("Embora a CF/88 não preveja iniciativa popular para propostas de "
     "emenda à Constituição Federal, o STF admite que as Constituições "
     "Estaduais a estabeleçam para emendas à própria Constituição Estadual.",
     "<b>CERTO.</b> O art. 60 não inclui o eleitor entre os legitimados à "
     "PEC, e a iniciativa popular do art. 61, §2º vale apenas para projetos "
     "de lei. Mas, com base no art. 27, §4º, o STF entende que os Estados "
     "podem ampliar a iniciativa popular para emendas estaduais, desde que "
     "haja previsão na Constituição Estadual (ex.: SP). [Anotações da aula; "
     "Rodada 01/Mai.2024]"),

    # ── EXERCÍCIOS DO PROFESSOR (literal — Rodada 01, Mai/2024) ───────────────

    ("01-I – O prazo constitucional para o presidente da República "
     "sancionar ou vetar um projeto de lei, total ou parcialmente, é de "
     "trinta dias úteis contados da data do recebimento, após esse prazo, o "
     "silêncio do presidente da República importará sanção. (C/E?)",
     "<b>ERRADO.</b> O prazo do art. 66, §1º, CF/88 é de <b>15 dias "
     "úteis</b> contados do recebimento do projeto. Decorrido o prazo, o "
     "silêncio importa <b>sanção tácita</b> (§3º). O veto deve ser "
     "expresso e fundamentado, e o parcial só alcança texto integral de "
     "artigo, inciso, parágrafo ou alínea. [Exercício Q01-I, Rodada 01 "
     "Mai/2024]"),

    ("01-III – O presidente da República pode solicitar urgência "
     "constitucional na tramitação para a apreciação de proposições "
     "legislativas de qualquer parlamentar, desde que o autor do projeto "
     "esteja de acordo. (C/E?)",
     "<b>ERRADO.</b> O art. 64, §1º permite ao Presidente solicitar "
     "urgência apenas para projetos de <b>sua própria iniciativa</b>. "
     "Solicitada, cada Casa tem, sucessivamente, <b>45 dias</b>; esgotado o "
     "prazo, sobrestam-se as demais deliberações da Casa, exceto as de "
     "prazo constitucional determinado. [Exercício Q01-III, Rodada 01 "
     "Mai/2024]"),

    ("01-IV – De acordo com o disposto na CF/88, a lei deve dispor sobre a "
     "iniciativa popular através do processo legislativo federal. (C/E?)",
     "<b>ERRADO.</b> A iniciativa popular federal já está definida no "
     "próprio texto constitucional (art. 61, §2º): 1% do eleitorado "
     "nacional, em pelo menos 5 Estados, com mais de 3/10 de 1% dos "
     "eleitores de cada um. É no processo <b>estadual</b> que <b>a lei</b> "
     "disporá (art. 27, §4º); nos Municípios, 5% do eleitorado (art. 29, "
     "XIII). [Exercício Q01-IV, Rodada 01 Mai/2024]"),

    ("02-I – Considere-se que uma Proposta de Emenda à Constituição (PEC) "
     "visando extinguir o Supremo Tribunal Federal e contendo 3/5 de "
     "assinaturas de parlamentares tenha sido apresentada à Comissão de "
     "Constituição e Justiça. Nessa situação, a proposta não poderá ser "
     "objeto de deliberação do colegiado por violar a Constituição Federal "
     "de 1988. (C/E?)",
     "<b>CERTO.</b> O número de assinaturas é regular (basta 1/3 de uma "
     "das Casas, art. 60, I; 3/5 é o quórum de aprovação, não de "
     "apresentação). Mas extinguir o STF é tendente a abolir a separação "
     "dos Poderes (art. 60, §4º, III), cláusula pétrea, e por isso a "
     "proposta nem pode ser objeto de deliberação. [Exercício Q02-I, "
     "Rodada 01 Mai/2024]"),

    ("02-II – Considere que uma proposta de emenda constitucional tenha "
     "sido rejeitada em maio de 2024. Nesse caso, nova proposta de emenda "
     "versando sobre a mesma matéria pode ser proposta, ainda no ano de "
     "2024, se for de iniciativa da maioria absoluta dos membros do "
     "Senado Federal ou da Câmara dos Deputados. (C/E?)",
     "<b>ERRADO.</b> O art. 60, §5º é regra inflexível: a PEC rejeitada ou "
     "prejudicada só pode ser reapresentada na <b>próxima sessão "
     "legislativa</b> (a partir de 2 de fevereiro de 2025). A exceção da "
     "maioria absoluta de qualquer das Casas existe apenas para "
     "<b>projetos de lei</b> rejeitados (art. 67). [Exercício Q02-II, "
     "Rodada 01 Mai/2024]"),

    ("03-II – O projeto de lei aprovado por uma Casa será revisto pela "
     "outra, em dois turnos de discussão e votação, enviado para sanção ou "
     "promulgação, se a Casa revisora o aprovar, ou arquivado, se o "
     "rejeitar. (C/E?)",
     "<b>ERRADO.</b> Para LO e LC, o art. 65 exige discussão e votação em "
     "<b>turno único</b> em cada Casa (aprovação por maioria simples na LO "
     "e absoluta na LC). Os <b>dois turnos</b> e o quórum de 3/5 dos "
     "membros de cada Casa são exigências da <b>emenda constitucional</b> "
     "(art. 60, §2º), reflexo da rigidez constitucional. [Exercício "
     "Q03-II, Rodada 01 Mai/2024]"),

    ("03-III – Caso um deputado federal apresente projeto de lei versando "
     "sobre matéria tributária, ela será incompatível com a CF, pois a "
     "referida iniciativa, independentemente de seu conteúdo, é privativa "
     "do chefe do Poder Executivo. (C/E?)",
     "<b>ERRADO.</b> Segundo o STF (art. 61, §1º, II, \"b\"), só a matéria "
     "tributária dos <b>Territórios</b> é de iniciativa privativa do "
     "Presidente. O tributário da União é de iniciativa <b>concorrente</b>: "
     "parlamentar pode propor isenção, parcelamento de dívidas e alteração "
     "de alíquotas. [Exercício Q03-III, Rodada 01 Mai/2024]"),

    ("03-IV – A CF admite que se modifiquem, por meio de emendas "
     "parlamentares, projetos de lei elaborados pelo chefe do Poder "
     "Executivo no exercício de sua iniciativa reservada e não veda, por "
     "inteiro, as emendas que ensejem aumento de despesa pública. (C/E?)",
     "<b>CERTO.</b> A emenda parlamentar é admitida, mas o art. 63, I veda "
     "aumento de despesa em projetos de iniciativa exclusiva do Presidente. "
     "Exceção (art. 166, §§3º e 4º): emendas orçamentárias compatíveis com "
     "PPA e LDO e que indiquem recursos por anulação de outras despesas. "
     "Emendas também não podem desfigurar o projeto com matéria estranha. "
     "[Exercício Q03-IV, Rodada 01 Mai/2024]"),
]


if __name__ == "__main__":
    make_deck(
        "REVIEW::Direito Interno::Processo Legislativo - Parte 2",
        "Direito Interno - Processo Legislativo - Parte 2.apkg",
        PROCESSO_LEGISLATIVO_PARTE2,
    )
    print(f"\n🎉 Deck gerado em {DECK_DIR}")
