"""Prépare les vues 6 angles des fiches Glideway (img/views/<taille>/<vue>.webp).

- autre-cote : la vraie photo de profil retournée en miroir (aucune IA)
- face / dessus / dessous / arriere : images générées par Nano Banana Pro à partir de la vraie
  photo (_scrape/gen/<vue>.png), détourées ici comme les coloris (fond blanc -> transparent)

Usage : python3 tools/prepare_views.py   (nécessite Pillow)
"""
import os
import sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from prepare_assets import cutout  # noqa: E402  (même détourage que les coloris)

SIZE = "176"
OUT = os.path.join(ROOT, "img", "views", SIZE)
os.makedirs(OUT, exist_ok=True)

# autre côté : miroir de la vraie photo détourée du Bone Soldier
side = Image.open(os.path.join(ROOT, "img", "colors", "1", "1.webp"))
ImageOps.mirror(side).save(os.path.join(OUT, "autre-cote.webp"), "WEBP", quality=85, method=6)
print("autre-cote ok")

# vues générées : détourage depuis _scrape/gen (chemin relatif à _scrape/site attendu par cutout)
for name in ("face", "dessus", "dessous", "arriere"):
    src = os.path.join(ROOT, "_scrape", "gen", f"{name}.png")
    if not os.path.exists(src):
        print(name, "absente")
        continue
    cutout(os.path.join("..", "gen", f"{name}.png"), os.path.join("views", SIZE, f"{name}.webp"), width=1100, thresh=14)
    print(name, "ok")
