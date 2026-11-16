#!/usr/bin/env python3
"""Gera app/data/jogos.json a partir dos pools e grades das palavras cruzadas.
Rodado automaticamente por scripts/palavras_cruzadas/gerar.py; pode ser rodado sozinho."""
import glob, json, os, time
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
POOLS = os.path.join(RAIZ, 'scripts', 'palavras_cruzadas', 'pools')
GRADES = os.path.join(RAIZ, 'scripts', 'palavras_cruzadas', 'grades')
SAIDA = os.path.join(RAIZ, 'app', 'data', 'jogos.json')

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

if __name__ == '__main__':
    main()
