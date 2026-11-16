#!/usr/bin/env python3
"""Gera app/data/jogos.json a partir dos pools e grades das palavras cruzadas.
Rodado automaticamente por scripts/palavras_cruzadas/gerar.py; pode ser rodado sozinho."""
import glob, json, os, re, sys, time, unicodedata
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
POOLS = os.path.join(RAIZ, 'scripts', 'palavras_cruzadas', 'pools')
GRADES = os.path.join(RAIZ, 'scripts', 'palavras_cruzadas', 'grades')
SAIDA = os.path.join(RAIZ, 'app', 'data', 'jogos.json')
CONEXOES = os.path.join(RAIZ, 'scripts', 'app', 'conexoes')
SAIDA_CX = os.path.join(RAIZ, 'app', 'data', 'conexoes.json')
QUEM = os.path.join(RAIZ, 'scripts', 'app', 'quem-disse')
SAIDA_QD = os.path.join(RAIZ, 'app', 'data', 'quem-disse.json')
NOTAS = os.path.join(RAIZ, 'anotações')

def chave_ordem(p):
    return [int(x) for x in p['item'].split('.')]

def main():
    jogos = []
    for f in sorted(glob.glob(os.path.join(POOLS, '*.json'))):
        pool = json.load(open(f))
        gf = os.path.join(GRADES, pool['chave'] + '.json')
        if not os.path.exists(gf): continue
        g = json.load(open(gf))
        pal = [{k: w[k] for k in ('a', 'q', 'f', 'r', 'c', 'd', 'n')} for w in g['palavras']]
        jogos.append(dict(id=pool['chave'], tipo='cruzada', materia=pool['materia'], item=pool['item'],
                          status=pool['status'], titulo=pool['titulo'].replace(' (parcial)', ''),
                          descricao=pool['descricao'], h=g['h'], w=g['w'], palavras=pal))
    ordem = {'Direito Interno': 0, 'Direito Internacional': 1, 'Economia': 2}
    jogos.sort(key=lambda j: (ordem.get(j['materia'], 9), [int(x) for x in j['item'].split('.')]))
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    json.dump(dict(gerado=time.strftime('%Y-%m-%d'), jogos=jogos), open(SAIDA, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('app: %d jogos em %s' % (len(jogos), os.path.relpath(SAIDA, RAIZ)))

def norm(t):
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', unicodedata.normalize('NFD', t.lower()).encode('ascii', 'ignore').decode()).split())

def conexoes():
    """Valida e junta os jogos Conexões (scripts/app/conexoes/*.json) em app/data/conexoes.json.
    Cada jogo: 4 grupos x 4 termos únicos; fonte = arquivo de anotação existente; termo deve aparecer nas anotações da matéria."""
    jogos, erros, avisos = [], [], []
    cache = {}
    def notas_de(mat):
        if mat not in cache:
            cache[mat] = {os.path.basename(f): norm(open(f).read()) for f in glob.glob(os.path.join(NOTAS, mat, '*.md'))}
        return cache[mat]
    ids = set()
    for f in sorted(glob.glob(os.path.join(CONEXOES, '*.json'))):
        for j in json.load(open(f)):
            tag = j.get('id', '?')
            if tag in ids: erros.append('%s: id repetido' % tag)
            ids.add(tag)
            g = j.get('grupos', [])
            if len(g) != 4 or any(len(x['termos']) != 4 for x in g): erros.append('%s: precisa de 4 grupos com 4 termos' % tag); continue
            todos = [norm(t) for x in g for t in x['termos']]
            if len(set(todos)) != 16: erros.append('%s: termo repetido entre grupos' % tag)
            ns = notas_de(j['materia'])
            for x in g:
                fs = x['fonte'] if isinstance(x['fonte'], list) else [x['fonte']]
                if any(f not in ns for f in fs): erros.append('%s: fonte inexistente: %s' % (tag, fs)); continue
                for t in x['termos']:
                    if norm(t) not in ' '.join(ns.values()):
                        avisos.append('%s: "%s" não aparece nas anotações de %s (conferir material do professor)' % (tag, t, j['materia']))
                    elif not any(norm(t) in ns[f] for f in fs):
                        avisos.append('%s: "%s" existe nas anotações, mas não na(s) fonte(s) citada(s): %s' % (tag, t, ', '.join(fs)))
            jogos.append(j)
    ordem = {'Direito Interno': 0, 'Direito Internacional': 1, 'Economia': 2}
    jogos.sort(key=lambda j: (ordem.get(j['materia'], 9), [int(x) for x in j['item'].split('.')], j['id']))
    for a in avisos: print('AVISO', a)
    for e in erros: print('ERRO', e)
    if erros: sys.exit(1)
    json.dump(dict(gerado=time.strftime('%Y-%m-%d'), jogos=jogos), open(SAIDA_CX, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('app: %d conexões em %s' % (len(jogos), os.path.relpath(SAIDA_CX, RAIZ)))

def quem_disse():
    """Valida e junta os decks Quem disse? (scripts/app/quem-disse/*.json) em app/data/quem-disse.json.
    Cada deck: >= 5 cartas {q, r, chave, fonte, exp}; respostas distintas; `chave` deve aparecer na anotação `fonte`."""
    decks, erros, avisos, ids = [], [], [], set()
    for f in sorted(glob.glob(os.path.join(QUEM, '*.json'))):
        for d in json.load(open(f)):
            tag = d.get('id', '?')
            if tag in ids: erros.append('%s: id repetido' % tag)
            ids.add(tag)
            cs = d.get('cartas', [])
            if len(cs) < 5: erros.append('%s: precisa de pelo menos 5 cartas' % tag)
            if len({c['r'] for c in cs}) != len(cs): erros.append('%s: resposta repetida' % tag)
            for c in cs:
                for k in ('q', 'r', 'chave', 'fonte', 'exp'):
                    if not c.get(k): erros.append('%s: carta sem %s (%s)' % (tag, k, c.get('r', '?')))
                arq = os.path.join(NOTAS, d['materia'], c['fonte'])
                if not os.path.exists(arq): erros.append('%s: fonte inexistente: %s' % (tag, c['fonte'])); continue
                if norm(c['chave']) not in norm(open(arq).read()):
                    avisos.append('%s: "%s" não aparece em "%s" (conferir material do professor)' % (tag, c['chave'], c['fonte']))
                if norm(c['chave']).split()[-1] in norm(c['q']): erros.append('%s: enunciado entrega a resposta (%s)' % (tag, c['r']))
            decks.append(d)
    ordem = {'Direito Interno': 0, 'Direito Internacional': 1, 'Economia': 2}
    decks.sort(key=lambda d: (ordem.get(d['materia'], 9), d['id']))
    for a in avisos: print('AVISO', a)
    for e in erros: print('ERRO', e)
    if erros: sys.exit(1)
    json.dump(dict(gerado=time.strftime('%Y-%m-%d'), decks=decks), open(SAIDA_QD, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('app: %d decks Quem disse em %s' % (len(decks), os.path.relpath(SAIDA_QD, RAIZ)))

if __name__ == '__main__':
    main()
    conexoes()
    quem_disse()
