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
                if x['fonte'] not in ns: erros.append('%s: fonte inexistente: %s' % (tag, x['fonte'])); continue
                for t in x['termos']:
                    if norm(t) not in ' '.join(ns.values()):
                        avisos.append('%s: "%s" não aparece nas anotações de %s (conferir material do professor)' % (tag, t, j['materia']))
            jogos.append(j)
    ordem = {'Direito Interno': 0, 'Direito Internacional': 1, 'Economia': 2}
    jogos.sort(key=lambda j: (ordem.get(j['materia'], 9), [int(x) for x in j['item'].split('.')], j['id']))
    for a in avisos: print('AVISO', a)
    for e in erros: print('ERRO', e)
    if erros: sys.exit(1)
    json.dump(dict(gerado=time.strftime('%Y-%m-%d'), jogos=jogos), open(SAIDA_CX, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('app: %d conexões em %s' % (len(jogos), os.path.relpath(SAIDA_CX, RAIZ)))

if __name__ == '__main__':
    main()
    conexoes()
