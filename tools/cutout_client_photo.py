"""Détoure une photo envoyée par le client (fond gris clair ou blanc) et la place comme vue d'une fiche.

Usage : python3 tools/cutout_client_photo.py <photo> <taille> <vue>
   ex : python3 tools/cutout_client_photo.py _scrape/client/glideway-176-dessus.png 176 dessus
Le fond = pixels clairs et quasi sans couleur, reliés au bord de l'image.
"""
import os
import sys
from collections import deque
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, size, view = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
w, h = im.size
px = im.load()


def is_bg(x, y):
    r, g, b = px[x, y]
    if min(r, g, b) > 249:                      # coins blancs de la capture
        return True
    # gris du fond (~220) et son ombre douce ; les reflets du leurre, plus clairs ou teintés, restent
    return 150 < min(r, g, b) and max(r, g, b) < 236 and max(r, g, b) - min(r, g, b) < 11


# remplissage depuis tous les bords : seul le fond relié au bord devient transparent
bg = [[False] * w for _ in range(h)]
q = deque([(x, y) for x in range(w) for y in (0, h - 1)] + [(x, y) for y in range(h) for x in (0, w - 1)])
while q:
    x, y = q.popleft()
    if not (0 <= x < w and 0 <= y < h) or bg[y][x] or not is_bg(x, y):
        continue
    bg[y][x] = True
    q.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

mask = Image.new("L", (w, h), 255)
m = mask.load()
for y in range(h):
    for x in range(w):
        if bg[y][x]:
            m[x, y] = 0
mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
out = im.convert("RGBA")
out.putalpha(mask)
box = mask.point(lambda v: 255 if v > 30 else 0).getbbox()
if box:
    out = out.crop((max(0, box[0] - 8), max(0, box[1] - 8), min(w, box[2] + 8), min(h, box[3] + 8)))
dst = os.path.join(ROOT, "img", "views", size, f"{view}.webp")
os.makedirs(os.path.dirname(dst), exist_ok=True)
out.save(dst, "WEBP", quality=90, method=6)
print("ok", dst, out.size)
