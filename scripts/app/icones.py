#!/usr/bin/env python3
"""Gera os ícones PNG do app (sem dependências) em app/icons/."""
import os, struct, zlib
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(RAIZ, 'app', 'icons')
BG = (31, 95, 107); FG = (255, 255, 255); BLOCK = (23, 70, 79); ACC = (242, 199, 92)
# mini palavra cruzada 5x5 (1 = casa branca, 0 = bloco, 2 = casa destacada)
G = ["11111", "10101", "12221", "10101", "11111"]

def png(w, h, px):
    raw = b''.join(b'\x00' + bytes(sum((px(x, y) for x in range(w)), ())) for y in range(h))
    def ch(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) + ch(b'IDAT', zlib.compress(raw, 9)) + ch(b'IEND', b'')

def icone(n, margem):
    area = n * (1 - 2 * margem); x0 = n * margem; c = area / 5; gap = max(1, n // 100)
    def px(x, y):
        i = int((x - x0) // c); j = int((y - x0) // c)
        if 0 <= i < 5 and 0 <= j < 5:
            fx = (x - x0) - i * c; fy = (y - x0) - j * c
            if fx < gap or fy < gap or fx > c - gap or fy > c - gap: return BG
            k = G[j][i]
            return BLOCK if k == '0' else ACC if k == '2' else FG
        return BG
    return png(n, n, px)

os.makedirs(OUT, exist_ok=True)
for nome, n, m in (('icon-192.png', 192, 0.14), ('icon-512.png', 512, 0.14), ('maskable-512.png', 512, 0.22), ('apple-touch-icon.png', 180, 0.14)):
    open(os.path.join(OUT, nome), 'wb').write(icone(n, m)); print(nome)
