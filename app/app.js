// CACD Games — app estático (PWA). Todo o progresso fica no navegador de cada pessoa (localStorage).
(function () {
'use strict';
const KEY = 'cacd-games-v1';
const $app = document.getElementById('app'), $toast = document.getElementById('toast');
let JOGOS = [], GERADO = '';

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
  mem.cw = mem.cw || {}; mem.dias = mem.dias || {};
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
function jogoDoDia() {
  const ord = JOGOS.slice().sort((a, b) => hashStr(a.id) - hashStr(b.id));
  return ord[diaNum(hoje()) % ord.length];
}

/* ---------- roteamento ---------- */
function rota() {
  const h = location.hash.replace(/^#\/?/, '');
  if (h.startsWith('cruzada/')) return jogoTela(h.slice(8));
  if (h === 'stats') return statsTela();
  homeTela();
}

/* ---------- navegação inferior ---------- */
const tabs = on => '<nav class="tabs"><a href="#/" class="' + (on === 'home' ? 'on' : '') + '"><b>▦</b>Jogos</a><a href="#/stats" class="' + (on === 'stats' ? 'on' : '') + '"><b>▤</b>Progresso</a></nav>';

/* ---------- home ---------- */
function homeTela() {
  document.title = 'CACD Games';
  const st = streaks(), d = jogoDoDia(), dp = prog(d.id);
  const mats = [...new Set(JOGOS.map(j => j.materia))];
  const aberto = new Set(); try { JSON.parse(sessionStorage.getItem('abertas') || '[]').forEach(m => aberto.add(m)); } catch (e) { }
  let h = '<div class="screen"><div class="top"><h1>CACD Games</h1><div class="streak ' + (st.cur ? 'on' : '') + '" title="Dias seguidos com pelo menos uma palavra cruzada concluída">🔥 ' + st.cur + '</div></div>' +
    '<p class="lead">Jogos de estudo feitos só com as suas anotações e os materiais do professor.</p>' +
    '<button class="daily" data-go="' + d.id + '"><small>Jogo do dia' + (dp && dp.ok ? ' · concluído ✓' : '') + '</small><strong>' + esc(d.titulo) + '</strong><span>' + esc(d.materia) + ' · ' + d.palavras.length + ' palavras' + (dp && !dp.ok && pct(d) ? ' · ' + pct(d) + '% feito' : '') + '</span></button>' +
    '<h2 class="sec">Palavras cruzadas</h2>';
  mats.forEach(m => {
    const js = JOGOS.filter(j => j.materia === m), ok = js.filter(j => concluidoEm(j.id)).length;
    h += '<details class="mat" data-m="' + esc(m) + '"' + (aberto.has(m) ? ' open' : '') + '><summary>' + esc(m) + ' <span class="cnt">' + ok + ' de ' + js.length + '</span></summary>';
    js.forEach(j => {
      const p = pct(j), done = concluidoEm(j.id);
      h += '<button class="row" data-go="' + j.id + '"><div class="t"><b>' + esc(j.titulo) + '</b><span>Item ' + esc(j.item) + ' · ' + j.palavras.length + ' palavras' + (j.status === 'parcial' ? ' · matéria parcial' : '') + '</span></div>' +
        (done ? '<span class="tag ok">✓ completo</span>' : p ? '<span class="tag part">' + p + '%</span>' : '') + '</button>';
    });
    h += '</details>';
  });
  h += '<h2 class="sec">Em breve</h2><div class="soon"><div><b>Conexões</b>agrupe termos por tema</div><div><b>Quem disse?</b>autor, teoria e artigo</div><div><b>Linha do tempo</b>ordene eventos</div></div></div>' + tabs('home');
  $app.innerHTML = h;
  $app.querySelectorAll('[data-go]').forEach(b => b.onclick = () => { location.hash = '#/cruzada/' + b.dataset.go; });
  $app.querySelectorAll('details.mat').forEach(el => el.addEventListener('toggle', () => {
    const ab = [...$app.querySelectorAll('details.mat[open]')].map(x => x.dataset.m);
    try { sessionStorage.setItem('abertas', JSON.stringify(ab)); } catch (e) { }
  }));
}

/* ---------- estatísticas e backup ---------- */
function statsTela() {
  document.title = 'Progresso · CACD Games';
  const m = carrega(), st = streaks();
  const feitos = JOGOS.filter(j => concluidoEm(j.id)), semAjuda = feitos.filter(j => !prog(j.id).assist);
  let h = '<div class="screen"><div class="top"><h1>Progresso</h1></div><div class="cards">' +
    '<div class="card"><b>' + st.cur + '</b><span>' + (st.cur === 1 ? 'dia seguido' : 'dias seguidos') + '</span></div><div class="card"><b>' + st.best + '</b><span>melhor sequência</span></div>' +
    '<div class="card"><b>' + feitos.length + '<small style="font-size:14px;color:var(--muted)"> / ' + JOGOS.length + '</small></b><span>cruzadas concluídas</span></div>' +
    '<div class="card"><b>' + semAjuda.length + '</b><span>sem ajuda</span></div></div>';
  const t = diaNum(hoje()); let cal = '';
  for (let i = 27; i >= 0; i--) { const k = keyDeNum(t - i); cal += '<i class="' + ((m.dias[k] || []).length ? 'on' : '') + '" title="' + k + '"></i>'; }
  h += '<h2 class="sec">Últimos 28 dias</h2><div class="cal">' + cal + '</div><h2 class="sec">Por matéria</h2>';
  [...new Set(JOGOS.map(j => j.materia))].forEach(mt => {
    const js = JOGOS.filter(j => j.materia === mt), ok = js.filter(j => concluidoEm(j.id)).length;
    h += '<div><b>' + esc(mt) + '</b> <span class="cnt">' + ok + ' de ' + js.length + '</span><div class="bar"><i style="width:' + Math.round(100 * ok / js.length) + '%"></i></div></div>';
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
      try { const o = JSON.parse(decodeURIComponent(escape(atob(ta.value.trim())))); if (!o || typeof o.cw !== 'object' || typeof o.dias !== 'object') throw 0; mem = o; salva(); toast('Progresso importado.'); statsTela(); } catch (e) { toast('Código inválido.'); }
    };
  };
  document.getElementById('bZero').onclick = e => {
    if (e.target.dataset.s) { mem = { cw: {}, dias: {} }; salva(); toast('Progresso apagado.'); statsTela(); return; }
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
    '<button class="opt" data-a="rst" style="color:var(--bad)">Recomeçar<small>Apaga as letras e o tempo desta grade</small></button>',
    (s, fechar) => s.querySelectorAll('.opt').forEach(b => b.onclick = () => {
      const a = b.dataset.a;
      if (a === 'chk') { wrong = new Set(); let n = 0; cells.forEach(o => { if (o.val && o.val !== o.ans) { wrong.add(o); n++; } }); render(); toast(n ? n + (n > 1 ? ' letras erradas marcadas.' : ' letra errada marcada.') : 'Nenhuma letra errada até agora.'); }
      else if (a === 'let') { if (!cur) cur = firstEmpty(act); if (!fim) { cur.val = cur.ans; P.assist = true; wrong.delete(cur); save(); render(); } }
      else if (a === 'wrd') { if (!fim) { cellsOf(act).forEach(o => { o.val = o.ans; wrong.delete(o); }); P.assist = true; save(); render(); } }
      else if (a === 'rst') { cells.forEach(o => o.val = ''); wrong = new Set(); fim = false; segs = 0; last = Date.now(); P.ok = false; P.assist = false; P.t = 0; const m = carrega(); Object.keys(m.dias).forEach(d => { m.dias[d] = m.dias[d].filter(x => x !== id); }); save(); act = order.find(i => words[i].d === 'A') ?? order[0]; cur = firstEmpty(act); render(); toast('Grade limpa.'); }
      fechar();
    }));

  dimensiona();
  act = order.find(i => words[i].d === 'A') ?? order[0]; cur = firstEmpty(act); render();
}

/* ---------- início ---------- */
function iniciar() {
  window.addEventListener('hashchange', () => { if (stopGame) stopGame(); rota(); });
  fetch('data/jogos.json', { cache: 'no-cache' }).then(r => r.json()).then(d => { JOGOS = d.jogos; GERADO = d.gerado; rota(); })
    .catch(() => { $app.innerHTML = '<div class="screen"><p style="padding:40px 0">Não consegui carregar os jogos. Abra o app uma vez com internet.</p></div>'; });
  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('sw.js').catch(() => { });
}
iniciar();
})();
