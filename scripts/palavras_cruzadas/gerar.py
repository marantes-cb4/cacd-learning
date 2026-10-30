#!/usr/bin/env python3
"""Gera as palavras cruzadas (jogar e imprimir), o índice e a seção do README.

Uso:
  python3 scripts/palavras_cruzadas/gerar.py                 # gera só as que ainda não têm grade
  python3 scripts/palavras_cruzadas/gerar.py CHAVE [CHAVE..] # (re)gera as chaves indicadas
  python3 scripts/palavras_cruzadas/gerar.py --todas         # (re)gera todas
  python3 scripts/palavras_cruzadas/gerar.py --so-paginas [CHAVE ..]  # só reescreve HTMLs/índice/README (use quando só mudou a redação de dicas)

Cada palavra cruzada vem de pools/<chave>.json (resposta, dica, fonte). A dica só pode vir das
anotações em /anotações/<materia>/ ou do material do professor — nunca de conteúdo externo.
"""
import json, glob, os, re, sys, random, multiprocessing as mp
from html import escape

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
POOLS = os.path.join(AQUI, 'pools')
GRADES = os.path.join(AQUI, 'grades')
JOGOS = os.path.join(RAIZ, 'jogos')
BASE = "https://htmlpreview.github.io/?https://github.com/marantes-cb4/cacd-learning/blob/main/jogos/"
SEMENTES = 30
TAMANHO_MAX = 19
PASTAS = {'Direito Interno': 'direito-interno', 'Direito Internacional': 'direito-internacional', 'Economia': 'economia'}

# ---------- geração da grade ----------
def colocar_todas(palavras, rng, maxd):
    grade, dirs, colocadas = {}, {}, []
    def cabe(a, r, c, d):
        dr, dc = (0, 1) if d == 'A' else (1, 0)
        if (r - dr, c - dc) in grade or (r + dr * len(a), c + dc * len(a)) in grade: return -1
        cruz = 0
        for i, ch in enumerate(a):
            rr, cc = r + dr * i, c + dc * i
            if (rr, cc) in grade:
                if grade[(rr, cc)] != ch or d in dirs[(rr, cc)]: return -1
                cruz += 1
            elif d == 'A':
                if (rr - 1, cc) in grade or (rr + 1, cc) in grade: return -1
            else:
                if (rr, cc - 1) in grade or (rr, cc + 1) in grade: return -1
        return cruz
    def caixa(a, r, c, d):
        rs = [p[0] for p in grade] + [r, r + (len(a) - 1 if d == 'D' else 0)]
        cs = [p[1] for p in grade] + [c, c + (len(a) - 1 if d == 'A' else 0)]
        return max(rs) - min(rs) + 1, max(cs) - min(cs) + 1
    primeira = palavras[0]
    for i, ch in enumerate(primeira[0]):
        grade[(0, i)] = ch; dirs[(0, i)] = {'A'}
    colocadas.append((primeira, 0, 0, 'A'))
    while True:
        melhor = None
        for w in palavras[1:]:
            if any(p[0] == w for p in colocadas): continue
            a = w[0]
            for i, ch in enumerate(a):
                for (rr, cc), g in list(grade.items()):
                    if g != ch: continue
                    for d in ('A', 'D'):
                        r, c = (rr, cc - i) if d == 'A' else (rr - i, cc)
                        n = cabe(a, r, c, d)
                        if n < 1: continue
                        h, wd = caixa(a, r, c, d)
                        if h > maxd or wd > maxd: continue
                        sc = n * 10 - (h * wd) / 40 + rng.random() * 3 + len(a) * 0.3
                        if melhor is None or sc > melhor[0]: melhor = (sc, w, r, c, d)
        if not melhor: break
        _, w, r, c, d = melhor
        dr, dc = (0, 1) if d == 'A' else (1, 0)
        for i, ch in enumerate(w[0]):
            grade.setdefault((r + dr * i, c + dc * i), ch)
            dirs.setdefault((r + dr * i, c + dc * i), set()).add(d)
        colocadas.append((w, r, c, d))
    return colocadas, grade

def melhor_grade(chave):
    pool = json.load(open(os.path.join(POOLS, chave + '.json')))
    palavras = [tuple(p) for p in pool['palavras'] if p[0].isalpha() and 3 <= len(p[0]) <= TAMANHO_MAX - 2]
    if len(palavras) < len(pool['palavras']):
        print('aviso: %s tem resposta fora do tamanho 3..%d e foi ignorada' % (chave, TAMANHO_MAX - 2))
    melhor = None
    for semente in range(SEMENTES):
        rng = random.Random(semente)
        ws = palavras[:]; rng.shuffle(ws); ws.sort(key=lambda x: -len(x[0]) + rng.random() * 4)
        col, grade = colocar_todas(ws, rng, TAMANHO_MAX)
        rs = [p[0] for p in grade]; cs = [p[1] for p in grade]
        area = (max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1)
        k = (len(col), -area)
        if melhor is None or k > melhor[0]: melhor = (k, col, grade)
    _, col, grade = melhor
    mr = min(p[0] for p in grade); mc = min(p[1] for p in grade)
    pal = [dict(a=w[0], q=w[1], f=w[2], r=r - mr, c=c - mc, d=d) for (w, r, c, d) in col]
    H = max(p[0] for p in grade) - mr + 1; W = max(p[1] for p in grade) - mc + 1
    inicios = sorted({(o['r'], o['c']) for o in pal}); num = {s: i + 1 for i, s in enumerate(inicios)}
    for o in pal: o['n'] = num[(o['r'], o['c'])]
    g = dict(chave=chave, h=H, w=W, palavras=pal)
    json.dump(g, open(os.path.join(GRADES, chave + '.json'), 'w'), ensure_ascii=False)
    return chave, len(pal), len(palavras)

# ---------- páginas ----------
def nome_arquivo(chave): return 'item-' + re.sub(r'^(di|ec)', '', chave)

def pasta(pool): return PASTAS[pool['materia']]

def grade_html(g, preenchida, cel, nums):
    linhas = []
    for r in range(g['h']):
        tds = []
        for c in range(g['w']):
            if (r, c) in cel:
                n = nums.get((r, c)); dentro = ('<i>%d</i>' % n if n else '') + (cel[(r, c)] if preenchida else '')
                tds.append('<td class="c">%s</td>' % dentro)
            else: tds.append('<td class="b"></td>')
        linhas.append('<tr>%s</tr>' % ''.join(tds))
    return '<table class="grid">%s</table>' % ''.join(linhas)

def escreve_paginas(chave):
    pool = json.load(open(os.path.join(POOLS, chave + '.json')))
    g = json.load(open(os.path.join(GRADES, chave + '.json')))
    # as dicas vêm sempre do pool (assim, editar uma dica não exige refazer a grade)
    dicas = {p[0]: p for p in pool['palavras']}
    for w in g['palavras']:
        if w['a'] in dicas: w['q'], w['f'] = dicas[w['a']][1], dicas[w['a']][2]
    titulo = 'Palavras Cruzadas — ' + pool['titulo']
    pdir = os.path.join(JOGOS, pasta(pool)); os.makedirs(pdir, exist_ok=True)
    modelo = open(os.path.join(AQUI, 'modelo_jogo.html')).read()
    dados = json.dumps({'h': g['h'], 'w': g['w'], 'words': [dict(w, t=0) for w in g['palavras']]}, ensure_ascii=False)
    h = (modelo.replace('__TITLE__', escape(titulo)).replace('__SUB__', escape(pool['descricao']))
         .replace('__KEY__', chave).replace('/*__DATA__*/', dados))
    open(os.path.join(pdir, nome_arquivo(chave) + '.html'), 'w').write(h)
    cel, nums = {}, {}
    for w in g['palavras']:
        for i, ch in enumerate(w['a']):
            r, c = (w['r'], w['c'] + i) if w['d'] == 'A' else (w['r'] + i, w['c']); cel[(r, c)] = ch
        nums[(w['r'], w['c'])] = w['n']
    def dicas_li(d):
        return ''.join('<li><b>%d</b> %s <span>(%d)</span></li>' % (w['n'], escape(w['q']), len(w['a']))
                       for w in sorted([w for w in g['palavras'] if w['d'] == d], key=lambda w: w['n']))
    css = open(os.path.join(AQUI, 'modelo_impressao.css')).read()
    pag = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(t)s — versão para imprimir</title>
%(css)s
</head><body>
<button class="print-btn" onclick="window.print()">Imprimir</button>
<div class="page"><h1>%(t)s</h1><p class="sub">%(sub)s Dicas tiradas das anotações e do material do professor. Respostas sem acento e sem espaço.</p>
<div class="bar"><div>Nome: <span></span></div><div>Data: <span style="min-width:30mm"></span></div></div>%(b)s</div>
<div class="page pb"><h1>Dicas</h1><div class="clues"><div class="col"><h2>Horizontais</h2><ol>%(ca)s</ol></div><div class="col"><h2>Verticais</h2><ol>%(cd)s</ol></div></div><p class="foot">Cada dica traz entre parênteses o número de letras. Gabarito na próxima página.</p></div>
<div class="page pb"><h1>Gabarito</h1><p class="sub">Confira só depois de tentar.</p>%(p)s</div>
</body></html>''' % dict(t=escape(titulo), css=css, sub=escape(pool['descricao']), b=grade_html(g, False, cel, nums),
                         p=grade_html(g, True, cel, nums), ca=dicas_li('A'), cd=dicas_li('D'))
    open(os.path.join(pdir, nome_arquivo(chave) + '-impressao.html'), 'w').write(pag)

def chave_ordem(pool):
    return [int(x) for x in pool['item'].split('.')]

def indice_e_readme():
    pools = [json.load(open(f)) for f in glob.glob(os.path.join(POOLS, '*.json'))]
    n_pal = {os.path.basename(f)[:-5]: len(json.load(open(f))['palavras']) for f in glob.glob(os.path.join(GRADES, '*.json'))}
    por_mat = {m: sorted([p for p in pools if p['materia'] == m and p['chave'] in n_pal], key=chave_ordem) for m in PASTAS}
    # índice
    corpo = ''
    for m, lista in por_mat.items():
        corpo += '<h2>%s</h2><ul>' % m
        for p in lista:
            cam = PASTAS[m] + '/' + nome_arquivo(p['chave'])
            corpo += '<li><span>%s <em>(%d palavras)</em></span> <a href="%s%s.html">jogar</a> <a href="%s%s-impressao.html">imprimir</a></li>' % (
                escape(p['titulo']), n_pal[p['chave']], BASE, cam.replace(' ', '%20'), BASE, cam.replace(' ', '%20'))
        corpo += '</ul>'
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Palavras Cruzadas do CACD</title>'
            '<style>:root{--bg:#f3f4f1;--ink:#1d2327;--muted:#5b666c;--line:#c9cfcf;--accent:#1f5f6b;--panel:#fff}@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14181a;--ink:#e6e9ea;--muted:#9aa5aa;--line:#3a4448;--accent:#6fb7c4;--panel:#1b2023;color-scheme:dark}}'
            'body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}main{max-width:760px;margin:0 auto;padding:24px 16px 60px}h1{font-size:22px;margin:0 0 4px}p{color:var(--muted);margin:0 0 18px}h2{font-size:13px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:26px 0 8px}ul{list-style:none;margin:0;padding:0;background:var(--panel);border:1px solid var(--line);border-radius:10px}li{display:flex;gap:12px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line)}li:last-child{border:0}li span{flex:1}em{color:var(--muted);font-style:normal;font-size:13px}a{color:var(--accent);font-weight:600;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:5px 10px}a:hover{border-color:var(--accent)}@media (max-width:560px){li{flex-wrap:wrap}}</style></head>'
            '<body><main><h1>Palavras Cruzadas do CACD</h1><p>Uma por item do edital com anotações de aula (completo ou parcial). Dicas só das anotações e do material do professor.</p>%s</main></body></html>') % corpo
    open(os.path.join(JOGOS, 'index.html'), 'w').write(html)
    # README
    md = '<!-- palavras-cruzadas:inicio (gerado por scripts/palavras_cruzadas/gerar.py — não editar à mão) -->\n'
    md += '## Palavras cruzadas\n\nUma palavra cruzada por item do edital com anotações de aula, nos dois formatos (jogar no navegador e imprimir em A4 com gabarito). Dicas só das anotações de aula e do material do professor.\n\n'
    md += '- [Abrir a lista completa](%sindex.html)\n' % BASE
    for m, lista in por_mat.items():
        md += '\n### %s\n\n| Item | Status | Palavras | Jogar | Imprimir |\n|---|---|---|---|---|\n' % m
        for p in lista:
            cam = (PASTAS[m] + '/' + nome_arquivo(p['chave'])).replace(' ', '%20')
            status = '✅ completo' if p['status'] == 'completo' else '🟡 parcial'
            md += '| %s | %s | %d | [jogar](%s%s.html) | [imprimir](%s%s-impressao.html) |\n' % (
                p['titulo'].replace(' (parcial)', ''), status, n_pal[p['chave']], BASE, cam, BASE, cam)
    md += '<!-- palavras-cruzadas:fim -->\n'
    caminho = os.path.join(RAIZ, 'README.md')
    texto = open(caminho).read()
    padrao = re.compile(r'<!-- palavras-cruzadas:inicio.*?<!-- palavras-cruzadas:fim -->\n', re.S)
    if padrao.search(texto): texto = padrao.sub(lambda _: md, texto)
    else: texto = texto.rstrip('\n') + '\n\n' + md
    open(caminho, 'w').write(texto)

def main(args):
    os.makedirs(GRADES, exist_ok=True)
    if '--so-paginas' in args:
        chaves = [a for a in args if not a.startswith('--')] or [os.path.basename(f)[:-5] for f in glob.glob(os.path.join(GRADES, '*.json'))]
        for c in chaves: escreve_paginas(c)
        indice_e_readme(); print('ok'); return
    todas = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(POOLS, '*.json')))
    if '--todas' in args: alvo = todas
    elif args: alvo = [a for a in args if a in todas]; faltam = [a for a in args if a not in todas]; \
        print('chaves desconhecidas:', faltam) if faltam else None
    else: alvo = [k for k in todas if not os.path.exists(os.path.join(GRADES, k + '.json'))]
    if alvo:
        with mp.Pool(min(8, len(alvo))) as pool:
            for chave, n, total in pool.imap_unordered(melhor_grade, alvo): print('grade', chave, '-', n, 'de', total, 'palavras')
    # páginas: as geradas agora e todas as que já têm grade (as dicas vêm do pool)
    for chave in (todas if '--todas' in args or not args else alvo):
        if os.path.exists(os.path.join(GRADES, chave + '.json')): escreve_paginas(chave)
    indice_e_readme()
    print('ok')

if __name__ == '__main__':
    main(sys.argv[1:])
