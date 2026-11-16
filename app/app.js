// CACD Games — app estático (PWA). Todo o progresso fica no navegador de cada pessoa (localStorage).
(function () {
'use strict';
const KEY = 'cacd-games-v1';
const $app = document.getElementById('app'), $toast = document.getElementById('toast');
let JOGOS = [], CONEXOES = [], QDECKS = [], LDECKS = [], GERADO = '';

/* ---------- utilidades ---------- */
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const norm = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toUpperCase();
const pad = n => String(n).padStart(2, '0');
const hoje = () => { const d = new Date(); return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); };
const diaNum = k => { const [y, m, d] = k.split('-').map(Number); return Math.round(Date.UTC(y, m - 1, d) / 864e5); };
const keyDeNum = n => { const d = new Date(n * 864e5); return d.getUTCFullYear() + '-' + pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate()); };
const fmtT = s => pad(Math.floor(s / 60)) + ':' + pad(s % 60);
let tt; function toast(t, ms) { $toast.textContent = t; $toast.style.display = 'block'; clearTimeout(tt); tt = setTimeout(() => $toast.style.display = 'none', ms || 2500); }

/* ---------- armazenamento ---------- */
let mem = null;
function carrega() {
  if (mem) return mem;
  try { mem = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { mem = null; }
  if (!mem || typeof mem !== 'object') mem = {};
  mem.cw = mem.cw || {}; mem.cx = mem.cx || {}; mem.qd = mem.qd || {}; mem.lt = mem.lt || {}; mem.dias = mem.dias || {};
  return mem;
}
function salva() { try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) { } }
const prog = id => carrega().cw[id] || null;
function concluidoEm(id) { const p = prog(id); return !!(p && p.ok); }
function pct(j) { const p = prog(j.id); if (!p) return 0; if (p.ok) return 100; const t = totalCels(j); return Math.min(99, Math.round(100 * Object.keys(p.v || {}).length / t)); }
const _tc = {}; function totalCels(j) { if (_tc[j.id]) return _tc[j.id]; const s = new Set(); j.palavras.forEach(w => { for (let k = 0; k < w.a.length; k++) s.add((w.d === 'A' ? w.r : w.r + k) + ',' + (w.d === 'A' ? w.c + k : w.c)); }); return _tc[j.id] = s.size; }

/* ---------- sequência (streak) ---------- */
function streaks() {
  const dias = Object.keys(carrega().dias).filter(k => carrega().dias[k].length).map(diaNum).sort((a, b) => a - b);
  const set = new Set(dias); let best = 0, run = 0, prev = null;
  dias.forEach(n => { run = (prev !== null && n === prev + 1) ? run + 1 : 1; best = Math.max(best, run); prev = n; });
  const t = diaNum(hoje()); let cur = 0, n = set.has(t) ? t : t - 1;
  while (set.has(n)) { cur++; n--; }
  return { cur, best, hojeFeito: set.has(t) };
}

/* ---------- jogo do dia ---------- */
function hashStr(s) { let h = 5381; for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0; return h; }
const TIPOS = [
  { k: 'cruzada', nome: 'Palavras cruzadas', ic: '▦', desc: 'Preencha a grade com as dicas' },
  { k: 'conexoes', nome: 'Conexões', ic: '◫', desc: 'Agrupe 16 termos em 4 grupos' },
  { k: 'quem', nome: 'Quem disse?', ic: '❝', desc: 'Descubra o autor ou a figura' },
  { k: 'tempo', nome: 'Linha do tempo', ic: '⌛', desc: 'Ordene os eventos do mais antigo ao mais recente' }
];
function itensDe(k) {
  const m = carrega();
  if (k === 'cruzada') return JOGOS.map(j => ({ id: j.id, titulo: j.titulo, materia: j.materia, sub: 'Item ' + j.item + ' · ' + j.palavras.length + ' palavras' + (j.status === 'parcial' ? ' · matéria parcial' : ''), hash: '#/cruzada/' + j.id, ok: concluidoEm(j.id), pct: pct(j) }));
  if (k === 'conexoes') return CONEXOES.map(j => { const c = m.cx[j.id] || {}; return { id: j.id, titulo: j.titulo, materia: j.materia, sub: 'Item ' + j.item + ' · 4 grupos', hash: '#/conexoes/' + j.id, ok: !!c.ok, pct: c.ok ? 100 : 25 * (c.solved || []).length, lost: !!c.lost }; });
  if (k === 'quem') return QDECKS.map(d => { const q = m.qd[d.id]; return { id: d.id, titulo: d.titulo, materia: d.materia, sub: (d.cartas.length > 12 ? '10 de ' + d.cartas.length : d.cartas.length) + ' perguntas por rodada', hash: '#/quem/' + d.id, ok: !!q && q.melhor === (q.n || d.cartas.length), nota: q ? 'melhor ' + q.melhor + '/' + (q.n || d.cartas.length) : '' }; });
  if (k === 'tempo') return LDECKS.map(d => { const q = m.lt[d.id] || {}; return { id: d.id, titulo: d.titulo, materia: d.materia, sub: d.eventos.length + ' eventos', hash: '#/tempo/' + d.id, ok: !!q.ok, nota: !q.ok && q.tent ? q.tent + (q.tent === 1 ? ' tentativa' : ' tentativas') : '' }; });
  return [];
}
function jogoDoDia() {
  const ativos = TIPOS.filter(t => !t.soon && itensDe(t.k).length), dn = diaNum(hoje());
  const t = ativos[dn % ativos.length], its = itensDe(t.k).sort((a, b) => hashStr(a.id) - hashStr(b.id));
  const it = its[Math.floor(dn / ativos.length) % its.length];
  const feito = it.ok || (carrega().dias[hoje()] || []).includes(it.id);
  return { tipo: t, item: it, feito };
}

/* ---------- roteamento ---------- */
function rota() {
  const h = location.hash.replace(/^#\/?/, '');
  if (h.startsWith('cruzada/')) return jogoTela(h.slice(8));
  if (h.startsWith('conexoes/')) return conexoesTela(h.slice(9));
  if (h.startsWith('quem/')) return quemTela(h.slice(5));
  if (h.startsWith('tempo/')) return tempoTela(h.slice(6));
  if (h.startsWith('checagem')) { const m = h.match(/[?&]q=([^&]*)/); return checagemTela(m ? decodeURIComponent(m[1]) : ''); }
  if (h.startsWith('nota')) { const p = new URLSearchParams(h.split('?')[1] || ''); return notaTela(p.get('m') || '', p.get('a') || '', p.get('q') || '', +(p.get('s') || -1)); }
  if (h === 'stats') return statsTela();
  homeTela();
}

/* ---------- navegação inferior ---------- */
const tabs = on => '<nav class="tabs"><a href="#/" class="' + (on === 'home' ? 'on' : '') + '"><b>▦</b>Jogos</a><a href="#/checagem" class="' + (on === 'check' ? 'on' : '') + '"><b>⌕</b>Checagem</a><a href="#/stats" class="' + (on === 'stats' ? 'on' : '') + '"><b>▤</b>Progresso</a></nav>';

/* ---------- home ---------- */
function homeTela() {
  document.title = 'CACD Games';
  const st = streaks(), d = jogoDoDia();
  let sel = ''; try { sel = sessionStorage.getItem('tipo') || ''; } catch (e) { }
  const aberto = new Set(); try { JSON.parse(sessionStorage.getItem('abertas') || '[]').forEach(m => aberto.add(m)); } catch (e) { }
  let h = '<div class="screen"><div class="top"><h1>CACD Games</h1><div class="streak ' + (st.cur ? 'on' : '') + '" title="Dias seguidos com pelo menos um jogo concluído">🔥 ' + st.cur + '</div></div>' +
    '<button class="daily" data-go="' + esc(d.item.hash) + '"><small>Jogo do dia · ' + esc(d.tipo.nome) + (d.feito ? ' · concluído ✓' : '') + '</small><strong>' + esc(d.item.titulo) + '</strong><span>' + esc(d.item.materia) + ' · ' + esc(d.item.sub) + '</span></button>' +
    '<h2 class="sec">Outros jogos</h2><div class="chips">';
  TIPOS.forEach(t => { h += '<button class="chip' + (sel === t.k ? ' on' : '') + '" data-tipo="' + t.k + '"' + (t.soon ? ' disabled' : '') + '><b>' + t.ic + '</b>' + esc(t.nome) + (t.soon ? '<small>em breve</small>' : '') + '</button>'; });
  h += '</div>';
  const tp = TIPOS.find(t => t.k === sel && !t.soon);
  if (tp) {
    const its = itensDe(tp.k);
    h += '<div class="gamehead"><b>' + esc(tp.nome) + '</b><span>' + esc(tp.desc) + '</span></div>';
    [...new Set(its.map(i => i.materia))].forEach(mt => {
      const ls = its.filter(i => i.materia === mt), ok = ls.filter(i => i.ok).length, key = tp.k + '-' + mt;
      h += '<details class="mat" data-m="' + esc(key) + '"' + (aberto.has(key) ? ' open' : '') + '><summary>' + esc(mt) + ' <span class="cnt">' + ok + ' de ' + ls.length + '</span></summary>';
      ls.forEach(i => {
        h += '<button class="row" data-go="' + esc(i.hash) + '"><div class="t"><b>' + esc(i.titulo) + '</b><span>' + esc(i.sub) + '</span></div>' +
          (i.ok ? '<span class="tag ok">✓ completo</span>' : i.lost ? '<span class="tag">tente de novo</span>' : i.nota ? '<span class="tag part">' + esc(i.nota) + '</span>' : i.pct ? '<span class="tag part">' + i.pct + '%</span>' : '') + '</button>';
      });
      h += '</details>';
    });
  }
  h += '</div>' + tabs('home');
  $app.innerHTML = h;
  $app.querySelectorAll('[data-go]').forEach(b => b.onclick = () => { location.hash = b.dataset.go; });
  $app.querySelectorAll('.chip').forEach(b => b.onclick = () => { try { sessionStorage.setItem('tipo', sel === b.dataset.tipo ? '' : b.dataset.tipo); } catch (e) { } homeTela(); });
  $app.querySelectorAll('details.mat').forEach(el => el.addEventListener('toggle', () => {
    const ab = [...$app.querySelectorAll('details.mat[open]')].map(x => x.dataset.m);
    try { sessionStorage.setItem('abertas', JSON.stringify(ab)); } catch (e) { }
  }));
}

/* ---------- checagem: busca nas anotações ---------- */
let ANOT = null, ANOT_PROMISE = null;
const nn = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
function carregaAnotacoes() {
  if (ANOT) return Promise.resolve(ANOT);
  if (!ANOT_PROMISE) ANOT_PROMISE = fetch('data/anotacoes.json').then(r => r.json()).then(d => { d.docs.forEach(x => { x._n = nn(x.t + ' \n' + x.x); x._t = nn(x.t); }); ANOT = d.docs; return ANOT; });
  return ANOT_PROMISE;
}
function marca(raw, toks) {
  const n = nn(raw), rg = [];
  toks.forEach(t => { let i = n.indexOf(t); while (i >= 0) { rg.push([i, i + t.length]); i = n.indexOf(t, i + t.length); } });
  rg.sort((a, b) => a[0] - b[0]);
  const m = []; rg.forEach(r => { if (m.length && r[0] <= m[m.length - 1][1]) m[m.length - 1][1] = Math.max(m[m.length - 1][1], r[1]); else m.push(r.slice()); });
  let o = '', p = 0; m.forEach(([a, b]) => { o += esc(raw.slice(p, a)) + '<mark>' + esc(raw.slice(a, b)) + '</mark>'; p = b; });
  return o + esc(raw.slice(p));
}
const md = h => h.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/\*(.+?)\*/g, '<em>$1</em>');
function secaoHtml(x, toks, semRodape) {
  let o = '';
  x.x.split('\n').forEach(l => {
    if (!l.trim() || /^\s*-{3,}\s*$/.test(l)) return;
    const ind = l.match(/^[ \t]*/)[0].replace(/\t/g, '  ').length, bul = /^\s*[-*]\s+/.test(l), txt = l.replace(/^\s*[-*]\s+/, '');
    if (/^\s*\|/.test(l)) { o += '<div class="tab">' + md(marca(l.trim(), toks)) + '</div>'; return; }
    o += '<div style="padding-left:' + Math.min(ind, 16) * 6 + 'px">' + (bul ? '• ' : '') + md(marca(txt, toks)) + '</div>';
  });
  if (semRodape) return o;
  return o + '<div class="dim">' + esc(x.m) + ' · ' + esc(x.a) + '</div>';
}
function snippet(x, toks) {
  const plain = x.x.replace(/\*\*|\*|^\s*[-|]\s*/gm, '').replace(/\s+/g, ' ');
  const n = nn(plain); let pos = -1;
  toks.forEach(t => { const i = n.indexOf(t); if (i >= 0 && (pos < 0 || i < pos)) pos = i; });
  const a = Math.max(0, (pos < 0 ? 0 : pos) - 70), seg = plain.slice(a, a + 240);
  return (a > 0 ? '… ' : '') + marca(seg, toks) + (a + 240 < plain.length ? ' …' : '');
}
function checagemTela(q0) {
  document.title = 'Checagem · CACD Games';
  let filtro = 'Todas', q = q0 || '', abertos = new Set();
  $app.innerHTML = '<div class="screen"><div class="top"><h1>Checagem</h1></div><p class="lead">Busque uma palavra nas suas anotações e releia o trecho. Ex.: garantias fundamentais, funding scheme, legítima defesa.</p>' +
    '<input id="q" class="search" type="search" placeholder="Digite uma palavra ou tema…" autocomplete="off" autocapitalize="off" spellcheck="false" value="' + esc(q) + '"><div class="fchips" id="fc"></div><div id="out"><div class="empty">Carregando anotações…</div></div></div>' + tabs('check');
  const inp = document.getElementById('q'), out = document.getElementById('out'), fc = document.getElementById('fc');
  let timer;
  function lista(docs) {
    const mats = ['Todas', ...new Set(docs.map(d => d.m))];
    fc.innerHTML = mats.map(m => '<button class="fc' + (m === filtro ? ' on' : '') + '" data-m="' + esc(m) + '">' + esc(m) + '</button>').join('');
    fc.querySelectorAll('.fc').forEach(b => b.onclick = () => { filtro = b.dataset.m; busca(); });
  }
  function busca() {
    carregaAnotacoes().then(docs => {
      lista(docs); fc.querySelectorAll('.fc').forEach(b => b.classList.toggle('on', b.dataset.m === filtro));
      q = inp.value; const toks = nn(q).split(/\s+/).filter(t => t.length >= 2);
      if (!toks.length) { out.innerHTML = '<div class="empty">Digite ao menos 2 letras para buscar.<br>A busca ignora acentos e maiúsculas e exige todas as palavras.</div>'; return; }
      const rs = [];
      docs.forEach((d, i) => {
        if (filtro !== 'Todas' && d.m !== filtro) return;
        let sc = 0; for (const t of toks) { if (!d._n.includes(t)) return; sc += (d._t.includes(t) ? 8 : 0) + Math.min(5, d._n.split(t).length - 1); }
        rs.push([sc, i]);
      });
      rs.sort((a, b) => b[0] - a[0]);
      if (!rs.length) { out.innerHTML = '<div class="empty">Nada encontrado nas anotações para “' + esc(q) + '”.<br>Tente menos palavras, ou outra grafia.</div>'; return; }
      const top = rs.slice(0, 40);
      out.innerHTML = '<p class="lead">' + rs.length + (rs.length === 1 ? ' trecho encontrado' : ' trechos encontrados') + (rs.length > 40 ? ' (mostrando os 40 mais relevantes)' : '') + '</p>' +
        top.map(([s, i]) => { const d = docs[i]; return '<div class="res" data-i="' + i + '"><button><div class="meta">' + esc(d.m) + ' · ' + esc(d.a) + '</div><div class="tt">' + marca(d.t, toks) + '</div><div class="sn">' + snippet(d, toks) + '</div></button><div class="full" hidden></div><div class="acts"><button class="btn nota">Ver anotação completa de ' + esc(d.a) + ' →</button></div></div>'; }).join('');
      out.querySelectorAll('.res').forEach(r => {
        const d = docs[+r.dataset.i], full = r.querySelector('.full');
        r.querySelector('.nota').onclick = () => { const sec = docs.filter(x => x.m === d.m && x.a === d.a).indexOf(d); location.hash = '#/nota?m=' + encodeURIComponent(d.m) + '&a=' + encodeURIComponent(d.a) + '&q=' + encodeURIComponent(q) + '&s=' + sec; };
        const abre = () => { full.innerHTML = secaoHtml(d, toks); full.hidden = false; r.querySelector('.sn').style.display = 'none'; };
        r.querySelector('button').onclick = () => { if (full.hidden) { abre(); abertos.add(r.dataset.i); } else { full.hidden = true; r.querySelector('.sn').style.display = ''; abertos.delete(r.dataset.i); } };
        if (abertos.has(r.dataset.i)) abre();
      });
    }).catch(() => { out.innerHTML = '<div class="empty">Não consegui carregar as anotações. Abra o app com internet uma vez.</div>'; });
  }
  inp.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => { abertos = new Set(); busca(); }, 180); });
  busca();
  if (!q0) setTimeout(() => { try { inp.focus(); } catch (e) { } }, 50);
}

/* ---------- jogo: linha do tempo ---------- */
function tempoTela(id) {
  const d = LDECKS.find(x => x.id === id);
  if (!d) { location.hash = '#/'; return; }
  document.title = d.titulo + ' · CACD Games';
  const m = carrega(), P = m.lt[id] || (m.lt[id] = { ok: false, tent: 0 });
  const rnd = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const k = Math.floor(Math.random() * (i + 1)); [a[i], a[k]] = [a[k], a[i]]; } return a; };
  const certa = d.eventos.map((_, i) => i);
  let ordem, marcas = null, fim = false;
  do { ordem = rnd(certa); } while (ordem.every((v, i) => v === i));
  function draw() {
    let h = '<div class="game"><header class="gbar"><button class="icon" id="tBack" aria-label="Voltar">‹</button><div class="gt"><strong>' + esc(d.titulo) + '</strong><span>Linha do tempo · ' + d.eventos.length + ' eventos · ' + P.tent + (P.tent === 1 ? ' tentativa' : ' tentativas') + '</span></div><button class="icon" id="tMenu" aria-label="Menu">⋯</button></header>' +
      '<div class="cxmain"><p class="cxhint">' + (fim ? 'Ordem correta, do mais antigo ao mais recente.' : 'Do <b>mais antigo</b> (em cima) ao <b>mais recente</b> (embaixo). Use as setas para mover.') + '</p><div class="tl">';
    ordem.forEach((ix, pos) => {
      const e = d.eventos[ix], cls = fim ? ' ok' : marcas ? (marcas[pos] ? ' ok' : ' bad') : '';
      h += '<div class="tev' + cls + '"><div class="tn">' + (pos + 1) + '</div><div class="tt2">' + (fim ? '<b class="td">' + esc(e.d) + '</b> ' : '') + esc(e.t) + (fim ? '<small>Fonte: ' + esc(e.fonte) + '</small>' : '') + '</div>' +
        (fim ? '' : '<div class="tb"><button data-m="' + pos + ',-1" aria-label="Subir"' + (pos === 0 ? ' disabled' : '') + '>▲</button><button data-m="' + pos + ',1" aria-label="Descer"' + (pos === ordem.length - 1 ? ' disabled' : '') + '>▼</button></div>') + '</div>';
    });
    h += '</div>';
    if (!fim) h += '<p class="cxerr" id="tInfo">' + (marcas ? marcas.filter(Boolean).length + ' de ' + marcas.length + ' na posição certa' : '') + '</p><div class="btns" style="justify-content:center"><button class="btn primary" id="tChk">Verificar</button></div>';
    else h += '<div class="btns" style="justify-content:center;margin-top:14px"><button class="btn primary" id="tHome">Voltar aos jogos</button><button class="btn" id="tAgain">Jogar de novo</button></div>';
    h += '</div></div>';
    $app.innerHTML = h;
    document.getElementById('tBack').onclick = () => { location.hash = '#/'; };
    document.getElementById('tMenu').onclick = menu;
    $app.querySelectorAll('.tb button').forEach(b => b.onclick = () => { const [p, dl] = b.dataset.m.split(',').map(Number); const q = p + dl; [ordem[p], ordem[q]] = [ordem[q], ordem[p]]; marcas = null; draw(); });
    const c = document.getElementById('tChk'); if (c) c.onclick = verifica;
    const hh = document.getElementById('tHome'); if (hh) hh.onclick = () => { location.hash = '#/'; };
    const ag = document.getElementById('tAgain'); if (ag) ag.onclick = () => { P.ok = false; tempoTela(id); };
  }
  function verifica() {
    P.tent++; marcas = ordem.map((ix, pos) => ix === pos);
    if (marcas.every(Boolean)) { fim = true; P.ok = true; const dk = hoje(), mm = carrega(); (mm.dias[dk] = mm.dias[dk] || []); if (!mm.dias[dk].includes(id)) mm.dias[dk].push(id); salva(); draw(); const st = streaks(); toast('Ordem correta em ' + P.tent + (P.tent === 1 ? ' tentativa' : ' tentativas') + ' · 🔥 ' + st.cur, 4000); return; }
    salva(); draw(); toast(marcas.filter(Boolean).length + ' de ' + marcas.length + ' na posição certa. Ajuste as que estão em vermelho.');
  }
  function menu() {
    const s = document.createElement('div'); s.className = 'scrim'; s.innerHTML = '<div class="sheet"><h3>Opções</h3><button class="opt" id="oCh">Consultar anotações<small>Abre a Checagem para rever o tema</small></button><button class="opt" id="oRev">Mostrar a ordem correta<small>Encerra a rodada sem concluir</small></button></div>'; document.body.appendChild(s);
    const f = () => s.remove(); s.addEventListener('click', e => { if (e.target === s) f(); });
    s.querySelector('#oCh').onclick = () => { f(); location.hash = '#/checagem?q=' + encodeURIComponent(d.titulo); };
    s.querySelector('#oRev').onclick = () => { f(); fim = true; draw(); ordem = certa.slice(); marcas = null; draw(); };
  }
  draw();
}

/* ---------- anotação completa ---------- */
function notaTela(m, a, q, alvo) {
  document.title = a + ' · CACD Games';
  $app.innerHTML = '<div class="screen"><div class="top"><button class="icon" id="nBack" aria-label="Voltar">‹</button><h1 style="font-size:18px">' + esc(a) + '</h1></div><p class="lead">' + esc(m) + ' · anotação completa' + (q ? ' · destacando “' + esc(q) + '”' : '') + '</p><div id="nbody"><div class="empty">Carregando…</div></div></div>' + tabs('check');
  document.getElementById('nBack').onclick = () => { if (history.length > 1) history.back(); else location.hash = '#/checagem' + (q ? '?q=' + encodeURIComponent(q) : ''); };
  carregaAnotacoes().then(docs => {
    const secs = docs.filter(x => x.m === m && x.a === a), body = document.getElementById('nbody');
    if (!secs.length) { body.innerHTML = '<div class="empty">Anotação não encontrada.</div>'; return; }
    const toks = nn(q).split(/\s+/).filter(t => t.length >= 2);
    body.innerHTML = secs.map((x, i) => '<section class="nsec' + (i === alvo ? ' alvo' : '') + '" id="sec-' + i + '"><h3>' + marca(x.t, toks) + '</h3><div class="full" style="border:0;padding:0">' + secaoHtml(x, toks, true) + '</div></section>').join('');
    const el = document.getElementById('sec-' + alvo); if (el) setTimeout(() => el.scrollIntoView({ block: 'start' }), 60);
  });
}

/* ---------- estatísticas e backup ---------- */
function statsTela() {
  document.title = 'Progresso · CACD Games';
  const m = carrega(), st = streaks();
  const feitos = JOGOS.filter(j => concluidoEm(j.id)), semAjuda = feitos.filter(j => !prog(j.id).assist), cxFeitos = CONEXOES.filter(j => (carrega().cx[j.id] || {}).ok), qdFeitos = QDECKS.filter(d => carrega().qd[d.id]), ltFeitos = LDECKS.filter(d => (carrega().lt[d.id] || {}).ok);
  let h = '<div class="screen"><div class="top"><h1>Progresso</h1></div><div class="cards">' +
    '<div class="card"><b>' + st.cur + '</b><span>' + (st.cur === 1 ? 'dia seguido' : 'dias seguidos') + '</span></div><div class="card"><b>' + st.best + '</b><span>melhor sequência</span></div>' +
    '<div class="card"><b>' + feitos.length + '<small style="font-size:14px;color:var(--muted)"> / ' + JOGOS.length + '</small></b><span>cruzadas concluídas</span></div>' +
    '<div class="card"><b>' + semAjuda.length + '</b><span>cruzadas sem ajuda</span></div>' +
    '<div class="card"><b>' + cxFeitos.length + '<small style="font-size:14px;color:var(--muted)"> / ' + CONEXOES.length + '</small></b><span>conexões concluídas</span></div>' +
    '<div class="card"><b>' + qdFeitos.length + '<small style="font-size:14px;color:var(--muted)"> / ' + QDECKS.length + '</small></b><span>baralhos de Quem disse</span></div>' +
    '<div class="card"><b>' + ltFeitos.length + '<small style="font-size:14px;color:var(--muted)"> / ' + LDECKS.length + '</small></b><span>linhas do tempo</span></div></div>';
  const t = diaNum(hoje()); let cal = '';
  for (let i = 27; i >= 0; i--) { const k = keyDeNum(t - i); cal += '<i class="' + ((m.dias[k] || []).length ? 'on' : '') + '" title="' + k + '"></i>'; }
  h += '<h2 class="sec">Últimos 28 dias</h2><div class="cal">' + cal + '</div><h2 class="sec">Por matéria</h2>';
  [...new Set(JOGOS.map(j => j.materia))].forEach(mt => {
    const js = JOGOS.filter(j => j.materia === mt), cs = CONEXOES.filter(j => j.materia === mt), qs = QDECKS.filter(d => d.materia === mt), ls = LDECKS.filter(d => d.materia === mt), ok = js.filter(j => concluidoEm(j.id)).length + cs.filter(j => (carrega().cx[j.id] || {}).ok).length + qs.filter(d => carrega().qd[d.id]).length + ls.filter(d => (carrega().lt[d.id] || {}).ok).length, tot = js.length + cs.length + qs.length + ls.length;
    h += '<div><b>' + esc(mt) + '</b> <span class="cnt">' + ok + ' de ' + tot + ' jogos</span><div class="bar"><i style="width:' + Math.round(100 * ok / tot) + '%"></i></div></div>';
  });
  h += '<h2 class="sec">Backup do progresso</h2><div class="box"><p>Seu progresso fica só neste aparelho e neste navegador. Para levar para outro celular (ou guardar antes de limpar os dados do navegador), exporte o código e importe lá.</p>' +
    '<div class="btns"><button class="btn" id="bExp">Exportar código</button><button class="btn" id="bImp">Importar código</button></div><textarea id="code" hidden spellcheck="false" aria-label="Código do progresso"></textarea><div class="btns" id="codeBtns" hidden></div></div>' +
    '<div class="box"><p>Dados desta versão: ' + esc(GERADO) + '. O app atualiza sozinho quando você abre com internet.</p><div class="btns"><button class="btn danger" id="bZero">Apagar todo o meu progresso</button></div></div></div>' + tabs('stats');
  $app.innerHTML = h;
  const ta = document.getElementById('code'), cb = document.getElementById('codeBtns');
  document.getElementById('bExp').onclick = () => {
    const c = btoa(unescape(encodeURIComponent(JSON.stringify(carrega()))));
    ta.hidden = false; cb.hidden = false; ta.value = c; ta.readOnly = true;
    cb.innerHTML = '<button class="btn primary" id="bCopy">Copiar código</button>';
    document.getElementById('bCopy').onclick = () => { ta.select(); (navigator.clipboard ? navigator.clipboard.writeText(c) : Promise.reject()).then(() => toast('Código copiado.'), () => { document.execCommand('copy'); toast('Código copiado.'); }); };
  };
  document.getElementById('bImp').onclick = () => {
    ta.hidden = false; cb.hidden = false; ta.value = ''; ta.readOnly = false; ta.placeholder = 'Cole aqui o código exportado';
    cb.innerHTML = '<button class="btn primary" id="bGo">Importar (substitui o progresso atual)</button>';
    document.getElementById('bGo').onclick = () => {
      try { const o = JSON.parse(decodeURIComponent(escape(atob(ta.value.trim())))); if (!o || typeof o.cw !== 'object' || typeof o.dias !== 'object') throw 0; o.cx = o.cx || {}; o.qd = o.qd || {}; o.lt = o.lt || {}; mem = o; salva(); toast('Progresso importado.'); statsTela(); } catch (e) { toast('Código inválido.'); }
    };
  };
  document.getElementById('bZero').onclick = e => {
    if (e.target.dataset.s) { mem = { cw: {}, cx: {}, qd: {}, lt: {}, dias: {} }; salva(); toast('Progresso apagado.'); statsTela(); return; }
    e.target.dataset.s = 1; e.target.textContent = 'Toque de novo para confirmar'; setTimeout(() => { e.target.dataset.s = ''; e.target.textContent = 'Apagar todo o meu progresso'; }, 3500);
  };
}

/* ---------- jogo: palavras cruzadas ---------- */
let stopGame = null;
function jogoTela(id) {
  const j = JOGOS.find(x => x.id === id);
  if (!j) { location.hash = '#/'; return; }
  document.title = j.titulo + ' · CACD Games';
  const H = j.h, W = j.w, words = j.palavras.map(w => Object.assign({}, w));
  const key = (r, c) => r + ',' + c;
  const cells = new Map();
  words.forEach((w, i) => {
    for (let k = 0; k < w.a.length; k++) {
      const r = w.d === 'A' ? w.r : w.r + k, c = w.d === 'A' ? w.c + k : w.c;
      let o = cells.get(key(r, c)); if (!o) { o = { r, c, ans: w.a[k], words: [], num: 0, val: '', el: null }; cells.set(key(r, c), o); }
      o.words.push(i); if (k === 0) o.num = w.n;
    }
  });
  const P = carrega().cw[id] || (carrega().cw[id] = { v: {}, ok: false, assist: false, t: 0 });
  for (const k in P.v) { const o = cells.get(k); if (o) o.val = P.v[k]; }
  let wrong = new Set(), cur = null, act = 0, done = new Set(), fim = P.ok, segs = P.t || 0, last = Date.now();
  const cellsOf = i => { const w = words[i], a = []; for (let k = 0; k < w.a.length; k++) a.push(cells.get(key(w.d === 'A' ? w.r : w.r + k, w.d === 'A' ? w.c + k : w.c))); return a; };
  const order = words.map((w, i) => i).sort((a, b) => words[a].n - words[b].n || (words[a].d === 'A' ? -1 : 1));
  const firstEmpty = i => { const cs = cellsOf(i); return cs.find(o => !o.val) || cs[0]; };

  $app.innerHTML = '<div class="game"><header class="gbar"><button class="icon" id="gBack" aria-label="Voltar">‹</button><div class="gt"><strong>' + esc(j.titulo) + '</strong><span id="gMeta"></span></div><button class="icon" id="gMenu" aria-label="Menu">⋯</button></header>' +
    '<div class="clue"><button id="cPrev" aria-label="Dica anterior">‹</button><p id="cText"></p><button class="cl" id="cList" aria-label="Todas as dicas" style="font-size:16px">☰</button><button id="cNext" aria-label="Próxima dica">›</button></div>' +
    '<div class="gmain"><div class="gwrap" id="gwrap"><div id="grid" role="grid" aria-label="Grade"></div></div><aside class="cluepane" id="pane"></aside></div>' +
    '<div class="kbd" id="kbd"></div></div>';
  const grid = document.getElementById('grid'), gwrap = document.getElementById('gwrap');
  function dimensiona() {
    const av = Math.max(200, gwrap.clientWidth - 24);
    document.documentElement.style.setProperty('--cs', Math.max(26, Math.min(40, Math.floor((av - (W - 1) * 2) / W))) + 'px');
  }
  grid.style.gridTemplateColumns = 'repeat(' + W + ',var(--cs))';
  for (let r = 0; r < H; r++) for (let c = 0; c < W; c++) {
    const o = cells.get(key(r, c)), el = document.createElement('div');
    if (!o) { el.className = 'cell blank'; grid.appendChild(el); continue; }
    el.className = 'cell'; el.setAttribute('role', 'gridcell'); el.onclick = () => pick(o); o.el = el; grid.appendChild(el);
  }
  // painel de dicas (lateral no desktop; folha no celular)
  const pane = document.getElementById('pane');
  function cluesHtml(sheet) {
    let h = '';
    [['A', 'Horizontais'], ['D', 'Verticais']].forEach(([d, t]) => {
      h += '<h3>' + t + '</h3><ol>';
      order.filter(i => words[i].d === d).forEach(i => { h += '<li data-i="' + i + '" class="' + (i === act ? 'act ' : '') + (done.has(i) ? 'done' : '') + '"><b>' + words[i].n + '</b><span>' + esc(words[i].q) + ' (' + words[i].a.length + ')</span></li>'; });
      h += '</ol>';
    });
    return h;
  }
  function bindClues(root, after) { root.querySelectorAll('li').forEach(li => li.onclick = () => { act = +li.dataset.i; cur = firstEmpty(act); render(); if (after) after(); }); }
  // teclado na tela
  const kbd = document.getElementById('kbd');
  ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'].forEach((row, ri) => {
    const d = document.createElement('div');
    if (ri === 2) d.innerHTML = '<button class="wide" data-k="DIR" aria-label="Trocar direção">⇄</button>';
    [...row].forEach(ch => d.insertAdjacentHTML('beforeend', '<button data-k="' + ch + '">' + ch + '</button>'));
    if (ri === 2) d.insertAdjacentHTML('beforeend', '<button class="wide" data-k="BS" aria-label="Apagar">⌫</button>');
    kbd.appendChild(d);
  });
  kbd.addEventListener('pointerdown', e => { const b = e.target.closest('button'); if (!b) return; e.preventDefault(); tecla(b.dataset.k); });

  function pick(o) {
    if (!o) return; const aw = words[act];
    if (cur === o && o.words.length > 1) act = o.words.find(i => i !== act);
    else if (!o.words.includes(act)) act = o.words.find(i => words[i].d === aw.d) ?? o.words[0];
    cur = o; render();
  }
  const isDone = i => cellsOf(i).every(o => o.val === o.ans);
  function save() { P.v = {}; cells.forEach((o, k) => { if (o.val) P.v[k] = o.val; }); P.t = segs; salva(); }
  function render() {
    done = new Set(); words.forEach((w, i) => { if (isDone(i)) done.add(i); });
    const inw = new Set(cellsOf(act));
    cells.forEach(o => {
      o.el.className = 'cell' + (inw.has(o) ? ' inword' : '') + (o === cur ? ' cur' : '') + (wrong.has(o) ? ' bad' : '') + (o.words.some(i => done.has(i)) ? ' done' : '');
      o.el.innerHTML = (o.num ? '<i>' + o.num + '</i>' : '') + (o.val || '');
    });
    const w = words[act];
    document.getElementById('cText').innerHTML = '<b>' + w.n + (w.d === 'A' ? ' horizontal' : ' vertical') + '</b> · ' + esc(w.q) + ' (' + w.a.length + ')' + (done.has(act) ? '<small>✓ Fonte: ' + esc(w.f) + '</small>' : '');
    document.getElementById('gMeta').textContent = done.size + ' de ' + words.length + ' palavras · ' + fmtT(segs);
    pane.innerHTML = cluesHtml(); bindClues(pane);
    const ac = pane.querySelector('li.act'); if (ac && ac.scrollIntoView) ac.scrollIntoView({ block: 'nearest' });
    if (cur && cur.el && cur.el.scrollIntoView) cur.el.scrollIntoView({ block: 'nearest', inline: 'nearest' });
    if (!fim && done.size === words.length) vitoria();
  }
  function vitoria() {
    fim = true; P.ok = true; P.t = segs; const dk = hoje(), m = carrega(); (m.dias[dk] = m.dias[dk] || []); if (!m.dias[dk].includes(id)) m.dias[dk].push(id); salva();
    const st = streaks();
    setTimeout(() => sheet('<div class="win"><div class="big">🎉</div><h3>Grade completa!</h3><p style="color:var(--muted);margin:0">' + esc(j.titulo) + (P.assist ? ' · com ajuda' : ' · sem ajuda') + '</p><div class="stats"><div><b>' + fmtT(segs) + '</b><span>tempo</span></div><div><b>🔥 ' + st.cur + '</b><span>' + (st.cur === 1 ? 'dia seguido' : 'dias seguidos') + '</span></div></div><div class="btns" style="justify-content:center"><button class="btn primary" id="wHome">Voltar aos jogos</button><button class="btn" id="wStay">Ver grade</button></div></div>'), 350);
  }
  function sheet(html, bind) {
    const s = document.createElement('div'); s.className = 'scrim'; s.innerHTML = '<div class="sheet">' + html + '</div>'; document.body.appendChild(s);
    const fechar = () => s.remove(); s.addEventListener('click', e => { if (e.target === s) fechar(); });
    const wh = s.querySelector('#wHome'); if (wh) wh.onclick = () => { fechar(); location.hash = '#/'; };
    const ws = s.querySelector('#wStay'); if (ws) ws.onclick = fechar;
    if (bind) bind(s, fechar); return s;
  }
  function tecla(k) {
    if (k === 'DIR') { if (cur && cur.words.length > 1) { act = cur.words.find(i => i !== act); render(); } return; }
    if (k === 'BS') { if (!cur || fim) return; const cs = cellsOf(act), i = cs.indexOf(cur); if (cur.val) { cur.val = ''; } else if (i > 0) { cur = cs[i - 1]; cur.val = ''; } wrong.delete(cur); save(); render(); return; }
    if (!cur || fim || !/^[A-Z]$/.test(k)) return;
    cur.val = k; wrong.delete(cur); const cs = cellsOf(act), i = cs.indexOf(cur);
    if (i < cs.length - 1) cur = cs[i + 1]; else { const nx = cs.find(o => !o.val); if (nx) cur = nx; }
    save(); render();
  }
  function move(dr, dc) {
    if (!cur) return; let r = cur.r, c = cur.c;
    for (let n = 0; n < Math.max(H, W); n++) { r += dr; c += dc; if (r < 0 || c < 0 || r >= H || c >= W) return; const o = cells.get(key(r, c)); if (o) { cur = o; if (!o.words.includes(act)) act = o.words.find(i => words[i].d === (dc ? 'A' : 'D')) ?? o.words[0]; render(); return; } }
  }
  const passo = d => { const ix = order.indexOf(act), n = order.length; act = order[(ix + d + n) % n]; cur = firstEmpty(act); render(); };
  function onKey(e) {
    if (e.metaKey || e.ctrlKey || e.altKey || document.querySelector('.scrim')) return;
    const k = e.key;
    if (k === 'Backspace') { e.preventDefault(); tecla('BS'); }
    else if (k === 'ArrowRight') { e.preventDefault(); move(0, 1); } else if (k === 'ArrowLeft') { e.preventDefault(); move(0, -1); }
    else if (k === 'ArrowDown') { e.preventDefault(); move(1, 0); } else if (k === 'ArrowUp') { e.preventDefault(); move(-1, 0); }
    else if (k === 'Tab') { e.preventDefault(); passo(e.shiftKey ? -1 : 1); }
    else if (k === ' ' || k === 'Enter') { e.preventDefault(); tecla('DIR'); }
    else if (k.length === 1) { const u = norm(k); if (/^[A-Z]$/.test(u)) tecla(u); }
  }
  document.addEventListener('keydown', onKey);
  const tick = setInterval(() => { if (document.hidden || fim) { last = Date.now(); return; } const n = Date.now(); segs += Math.round((n - last) / 1000); last = n; document.getElementById('gMeta').textContent = done.size + ' de ' + words.length + ' palavras · ' + fmtT(segs); if (segs % 5 === 0) { P.t = segs; salva(); } }, 1000);
  const onResize = () => { dimensiona(); };
  window.addEventListener('resize', onResize);
  stopGame = () => { clearInterval(tick); document.removeEventListener('keydown', onKey); window.removeEventListener('resize', onResize); P.t = segs; salva(); stopGame = null; document.documentElement.style.removeProperty('--cs'); };

  document.getElementById('gBack').onclick = () => { location.hash = '#/'; };
  document.getElementById('cPrev').onclick = () => passo(-1);
  document.getElementById('cNext').onclick = () => passo(1);
  document.getElementById('cList').onclick = () => sheet('<h3>Dicas</h3><div class="cluepane" style="display:block;width:auto;padding:0">' + cluesHtml() + '</div>', (s, fechar) => bindClues(s, fechar));
  document.getElementById('gMenu').onclick = () => sheet(
    '<h3>Opções</h3><button class="opt" data-a="chk">Verificar<small>Marca em vermelho as letras erradas</small></button>' +
    '<button class="opt" data-a="let">Revelar letra<small>Conta como “com ajuda”</small></button>' +
    '<button class="opt" data-a="wrd">Revelar palavra<small>Conta como “com ajuda”</small></button>' +
    '<button class="opt" data-a="chk2">Consultar anotações<small>Abre a Checagem para rever o tema</small></button>' + '<button class="opt" data-a="rst" style="color:var(--bad)">Recomeçar<small>Apaga as letras e o tempo desta grade</small></button>',
    (s, fechar) => s.querySelectorAll('.opt').forEach(b => b.onclick = () => {
      const a = b.dataset.a;
      if (a === 'chk2') { location.hash = '#/checagem?q=' + encodeURIComponent(j.titulo); return; }
      if (a === 'chk') { wrong = new Set(); let n = 0; cells.forEach(o => { if (o.val && o.val !== o.ans) { wrong.add(o); n++; } }); render(); toast(n ? n + (n > 1 ? ' letras erradas marcadas.' : ' letra errada marcada.') : 'Nenhuma letra errada até agora.'); }
      else if (a === 'let') { if (!cur) cur = firstEmpty(act); if (!fim) { cur.val = cur.ans; P.assist = true; wrong.delete(cur); save(); render(); } }
      else if (a === 'wrd') { if (!fim) { cellsOf(act).forEach(o => { o.val = o.ans; wrong.delete(o); }); P.assist = true; save(); render(); } }
      else if (a === 'rst') { cells.forEach(o => o.val = ''); wrong = new Set(); fim = false; segs = 0; last = Date.now(); P.ok = false; P.assist = false; P.t = 0; const m = carrega(); Object.keys(m.dias).forEach(d => { m.dias[d] = m.dias[d].filter(x => x !== id); }); save(); act = order.find(i => words[i].d === 'A') ?? order[0]; cur = firstEmpty(act); render(); toast('Grade limpa.'); }
      fechar();
    }));

  dimensiona();
  act = order.find(i => words[i].d === 'A') ?? order[0]; cur = firstEmpty(act); render();
}

/* ---------- jogo: conexões ---------- */
function conexoesTela(id) {
  const j = CONEXOES.find(x => x.id === id);
  if (!j) { location.hash = '#/'; return; }
  document.title = j.titulo + ' · CACD Games';
  const CORES = ['c0', 'c1', 'c2', 'c3'], MAXERR = 4;
  const m = carrega(), P = m.cx[id] || (m.cx[id] = { solved: [], erros: 0, ok: false, lost: false, tent: [] });
  const gidx = {}; j.grupos.forEach((g, i) => g.termos.forEach(t => gidx[t] = i));
  let sel = [], tiles = null;
  const rnd = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const k = Math.floor(Math.random() * (i + 1)); [a[i], a[k]] = [a[k], a[i]]; } return a; };
  const restantes = () => Object.keys(gidx).filter(t => !P.solved.includes(gidx[t]));
  function embaralha() { tiles = rnd(restantes()); }
  embaralha();
  const fim = () => P.ok || P.lost;
  function draw() {
    const ordem = P.lost ? [...P.solved, ...[0, 1, 2, 3].filter(i => !P.solved.includes(i))] : P.solved;
    let h = '<div class="game"><header class="gbar"><button class="icon" id="xBack" aria-label="Voltar">‹</button><div class="gt"><strong>' + esc(j.titulo) + '</strong><span>Conexões · Item ' + esc(j.item) + '</span></div><button class="icon" id="xMenu" aria-label="Menu">⋯</button></header>' +
      '<div class="cxmain"><p class="cxhint">Agrupe os 16 termos em 4 grupos de 4 que tenham algo em comum.</p><div class="cxgroups">';
    ordem.forEach((gi, n) => { const g = j.grupos[gi]; const perdeu = P.lost && !P.solved.includes(gi); h += '<div class="cxg ' + CORES[gi] + (perdeu ? ' miss' : '') + '"><b>' + esc(g.tema) + '</b><span>' + g.termos.map(esc).join(' · ') + '</span><small>Fonte: ' + esc([].concat(g.fonte).join(', ')) + '</small></div>'; });
    h += '</div>';
    if (!fim()) {
      h += '<div class="cxtiles">' + tiles.map(t => '<button class="tile' + (sel.includes(t) ? ' on' : '') + '" data-t="' + esc(t) + '">' + esc(t) + '</button>').join('') + '</div>' +
        '<p class="cxerr" aria-live="polite">Erros restantes: ' + '●'.repeat(MAXERR - P.erros) + '<span style="opacity:.3">' + '●'.repeat(P.erros) + '</span></p>' +
        '<div class="btns" style="justify-content:center"><button class="btn" id="xShuf">Embaralhar</button><button class="btn" id="xClr"' + (sel.length ? '' : ' disabled') + '>Limpar</button><button class="btn primary" id="xGo"' + (sel.length === 4 ? '' : ' disabled') + '>Enviar</button></div>';
    } else if (P.ok) h += '<p class="cxerr">Completo com ' + P.erros + (P.erros === 1 ? ' erro' : ' erros') + '.</p>';
    else h += '<p class="cxerr">Acabaram as tentativas. Os grupos que faltavam estão marcados.</p><div class="btns" style="justify-content:center"><button class="btn primary" id="xRe">Tentar de novo</button></div>';
    h += '</div></div>';
    $app.innerHTML = h;
    document.getElementById('xBack').onclick = () => { location.hash = '#/'; };
    document.getElementById('xMenu').onclick = () => sheet('<h3>Opções</h3><button class="opt" id="oCh">Consultar anotações<small>Abre a Checagem para rever o tema</small></button><button class="opt" id="oRe" style="color:var(--bad)">Recomeçar<small>Apaga o progresso desta conexão</small></button>', (s, f) => { s.querySelector('#oRe').onclick = () => { reset(); f(); }; s.querySelector('#oCh').onclick = () => { f(); location.hash = '#/checagem?q=' + encodeURIComponent(j.titulo); }; });
    $app.querySelectorAll('.tile').forEach(b => b.onclick = () => { const t = b.dataset.t; sel = sel.includes(t) ? sel.filter(x => x !== t) : sel.length < 4 ? [...sel, t] : sel; draw(); });
    const q = id => document.getElementById(id);
    if (q('xShuf')) q('xShuf').onclick = () => { embaralha(); draw(); };
    if (q('xClr')) q('xClr').onclick = () => { sel = []; draw(); };
    if (q('xGo')) q('xGo').onclick = envia;
    if (q('xRe')) q('xRe').onclick = reset;
  }
  function reset() { Object.assign(P, { solved: [], erros: 0, ok: false, lost: false, tent: [] }); const mm = carrega(); Object.keys(mm.dias).forEach(d => { mm.dias[d] = mm.dias[d].filter(x => x !== id); }); sel = []; salva(); embaralha(); draw(); }
  function envia() {
    if (sel.length !== 4) return;
    const k = sel.slice().sort().join('|');
    if (P.tent.includes(k)) { toast('Você já tentou essa combinação.'); return; }
    P.tent.push(k);
    const cont = [0, 0, 0, 0]; sel.forEach(t => cont[gidx[t]]++);
    const gi = cont.indexOf(4);
    if (gi >= 0) { P.solved.push(gi); sel = []; embaralha(); if (P.solved.length === 4) { P.ok = true; vitoria(); } salva(); draw(); return; }
    P.erros++; toast(cont.some(c => c === 3) ? 'Falta só um!' : 'Esses termos não formam um grupo.');
    if (P.erros >= MAXERR) { P.lost = true; sel = []; salva(); draw(); $toast.style.display = 'none'; setTimeout(() => sheet('<div class="win"><div class="big">😕</div><h3>Acabaram as tentativas</h3><p style="color:var(--muted);margin:0 0 14px">Veja os grupos que faltavam e tente de novo, com calma.</p><div class="btns" style="justify-content:center"><button class="btn primary" id="wStay">Ver respostas</button></div></div>'), 300); return; }
    salva(); draw();
  }
  function vitoria() {
    const dk = hoje(), mm = carrega(); (mm.dias[dk] = mm.dias[dk] || []); if (!mm.dias[dk].includes(id)) mm.dias[dk].push(id); salva();
    const st = streaks();
    setTimeout(() => sheet('<div class="win"><div class="big">🎉</div><h3>Você achou os 4 grupos!</h3><p style="color:var(--muted);margin:0">' + esc(j.titulo) + ' · ' + P.erros + (P.erros === 1 ? ' erro' : ' erros') + '</p><div class="stats"><div><b>🔥 ' + st.cur + '</b><span>' + (st.cur === 1 ? 'dia seguido' : 'dias seguidos') + '</span></div></div><div class="btns" style="justify-content:center"><button class="btn primary" id="wHome">Voltar aos jogos</button><button class="btn" id="wStay">Ver grupos</button></div></div>'), 350);
  }
  function sheet(html, bind) {
    $toast.style.display = 'none';
    const s = document.createElement('div'); s.className = 'scrim'; s.innerHTML = '<div class="sheet">' + html + '</div>'; document.body.appendChild(s);
    const f = () => s.remove(); s.addEventListener('click', e => { if (e.target === s) f(); });
    const wh = s.querySelector('#wHome'); if (wh) wh.onclick = () => { f(); location.hash = '#/'; };
    const ws = s.querySelector('#wStay'); if (ws) ws.onclick = f;
    if (bind) bind(s, f);
  }
  draw();
}

/* ---------- jogo: quem disse? ---------- */
function quemTela(id) {
  const d = QDECKS.find(x => x.id === id);
  if (!d) { location.hash = '#/'; return; }
  document.title = d.titulo + ' · CACD Games';
  const rnd = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const k = Math.floor(Math.random() * (i + 1)); [a[i], a[k]] = [a[k], a[i]]; } return a; };
  const cartas = rnd(d.cartas).slice(0, d.cartas.length > 12 ? 10 : d.cartas.length).map(c => ({ c, opts: rnd([c.r, ...rnd(d.cartas.filter(x => x.r !== c.r).map(x => x.r)).slice(0, 3)]) }));
  let i = 0, acertos = 0, resp = null;
  function sair() { location.hash = '#/'; }
  function draw() {
    if (i >= cartas.length) return fim();
    const { c, opts } = cartas[i];
    let h = '<div class="game"><header class="gbar"><button class="icon" id="qBack" aria-label="Voltar">‹</button><div class="gt"><strong>' + esc(d.titulo) + '</strong><span>Quem disse? · ' + (i + 1) + ' de ' + cartas.length + ' · ' + acertos + ' certas</span></div></header>' +
      '<div class="cxmain"><div class="qcard"><small>' + esc(d.rotulo || 'QUEM DISSE, FEZ OU FORMULOU?') + '</small><p>' + esc(c.q) + '</p></div><div class="qopts">';
    opts.forEach(o => { const cls = resp === null ? '' : o === c.r ? ' certo' : o === resp ? ' errado' : ' apagado'; h += '<button class="qopt' + cls + '" data-o="' + esc(o) + '"' + (resp !== null ? ' disabled' : '') + '>' + esc(o) + '</button>'; });
    h += '</div>';
    if (resp !== null) h += '<div class="qexp"><b>' + (resp === c.r ? 'Certo!' : 'Era ' + esc(c.r) + '.') + '</b> ' + esc(c.exp) + '<small>Fonte: ' + esc(c.fonte) + '</small></div><div class="btns" style="justify-content:center"><button class="btn" id="qCheck">Rever nas anotações</button><button class="btn primary" id="qNext">' + (i + 1 === cartas.length ? 'Ver resultado' : 'Próxima') + '</button></div>';
    h += '</div></div>';
    $app.innerHTML = h;
    document.getElementById('qBack').onclick = sair;
    $app.querySelectorAll('.qopt').forEach(b => b.onclick = () => { resp = b.dataset.o; if (resp === c.r) acertos++; draw(); });
    const n = document.getElementById('qNext'); if (n) n.onclick = () => { i++; resp = null; draw(); };
    const ck = document.getElementById('qCheck'); if (ck) ck.onclick = () => { location.hash = '#/checagem?q=' + encodeURIComponent(c.chave); };
  }
  function fim() {
    const m = carrega(), q = m.qd[id] || (m.qd[id] = { melhor: 0, vezes: 0 });
    q.vezes++; q.melhor = Math.max(q.melhor, acertos); q.n = cartas.length;
    const dk = hoje(); (m.dias[dk] = m.dias[dk] || []); if (!m.dias[dk].includes(id)) m.dias[dk].push(id); salva();
    const st = streaks();
    $app.innerHTML = '<div class="game"><header class="gbar"><button class="icon" id="qBack" aria-label="Voltar">‹</button><div class="gt"><strong>' + esc(d.titulo) + '</strong><span>Quem disse? · resultado</span></div></header><div class="cxmain win"><div class="big">' + (acertos === cartas.length ? '🏆' : '🎯') + '</div><h3>' + acertos + ' de ' + cartas.length + ' certas</h3><p style="color:var(--muted)">Melhor resultado: ' + q.melhor + '/' + cartas.length + ' · 🔥 ' + st.cur + (st.cur === 1 ? ' dia seguido' : ' dias seguidos') + '</p><div class="btns" style="justify-content:center"><button class="btn primary" id="qAgain">Jogar de novo</button><button class="btn" id="qHome">Voltar aos jogos</button></div></div></div>';
    document.getElementById('qBack').onclick = sair; document.getElementById('qHome').onclick = sair;
    document.getElementById('qAgain').onclick = () => quemTela(id);
  }
  draw();
}

/* ---------- início ---------- */
function iniciar() {
  window.addEventListener('hashchange', () => { if (stopGame) stopGame(); rota(); });
  Promise.all([fetch('data/jogos.json', { cache: 'no-cache' }).then(r => r.json()), fetch('data/conexoes.json', { cache: 'no-cache' }).then(r => r.json()).catch(() => ({ jogos: [] })), fetch('data/quem-disse.json', { cache: 'no-cache' }).then(r => r.json()).catch(() => ({ decks: [] })), fetch('data/linha-do-tempo.json', { cache: 'no-cache' }).then(r => r.json()).catch(() => ({ decks: [] }))]).then(([d, c, q, l]) => { JOGOS = d.jogos; CONEXOES = c.jogos; QDECKS = q.decks; LDECKS = l.decks; GERADO = d.gerado; rota(); })
    .catch(() => { $app.innerHTML = '<div class="screen"><p style="padding:40px 0">Não consegui carregar os jogos. Abra o app uma vez com internet.</p></div>'; });
  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('sw.js').catch(() => { });
}
iniciar();
})();
