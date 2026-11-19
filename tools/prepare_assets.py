"""Prépare les images du site à partir de la copie brute dans _scrape/site.

- convertit les photos en webp (plus légères)
- détoure les photos de coloris (fond blanc -> transparent) pour que les leurres
  « flottent » sur les fonds sombres du nouveau site

Usage : python3 tools/prepare_assets.py   (nécessite Pillow)
"""
import json
import os
import shutil
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_scrape", "site")
OUT = os.path.join(ROOT, "img")


def out(*p):
    path = os.path.join(OUT, *p)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def photo(src, dst, width=1600, q=80):
    im = Image.open(os.path.join(SRC, src))
    im = im.convert("RGBA" if im.mode in ("RGBA", "P", "LA") else "RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(out(dst), "WEBP", quality=q, method=6)


def cutout(src, dst, width=900, thresh=16):
    """Fond blanc -> transparent, par remplissage depuis les bords (le blanc
    à l'intérieur du leurre n'est pas touché), puis recadrage serré."""
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    w, h = im.size
    key = (255, 0, 255)
    work = im.copy()
    seeds = [(x, y) for x in range(0, w, 25) for y in (0, h - 1)] + \
            [(x, y) for y in range(0, h, 25) for x in (0, w - 1)]
    for s in seeds:
        if min(work.getpixel(s)) > 255 - thresh * 2:
            ImageDraw.floodfill(work, s, key, thresh=thresh)
    mask = Image.new("L", (w, h), 255)
    mpx, wpx = mask.load(), work.load()
    for y in range(h):
        for x in range(w):
            if wpx[x, y] == key:
                mpx[x, y] = 0
    mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = im.convert("RGBA")
    rgba.putalpha(mask)
    bbox = mask.point(lambda v: 255 if v > 20 else 0).getbbox()
    if bbox:
        pad = 12
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        rgba = rgba.crop(bbox)
    if rgba.width > width:
        rgba = rgba.resize((width, round(rgba.height * width / rgba.width)), Image.LANCZOS)
    rgba.save(out(dst), "WEBP", quality=82, method=6)


def main():
    # --- photos d'ambiance / produits
    jobs = {
        "img/about/pbls.jpg": "photos/bass-reeds.webp",
        "img/about/gw-stages.jpg": "photos/prototypes.webp",
        "img/about/testing.jpg": "photos/testing.webp",
        "img/about/production.jpg": "photos/production.webp",
        "img/products/1/glideway3.jpg": "photos/bass-176.webp",
        "img/products/5/glideway4.jpg": "photos/glideway-126-hand.webp",
        "img/products/8/glideway4.jpg": "photos/glideway-236-hand.webp",
        "img/products/5/top126.jpg": "photos/glideway-126-branch.webp",
        "img/products/8/top236.jpg": "photos/glideway-236-top.webp",
        "img/products/top/1.jpg": "photos/glideway-sunset.webp",
        "img/products/top/2.jpg": "photos/glideway-glow.webp",
        "img/products/top/3.jpg": "photos/banner-3.webp",
        "img/products/top/4.jpg": "photos/banner-4.webp",
        "img/products/3/sparetail1.jpg": "photos/spare-tail-1.webp",
        "img/products/3/sparetail2.jpg": "photos/spare-tail-2.webp",
        "img/products/4/leadstickers1.jpg": "photos/lead-stickers-1.webp",
        "img/products/4/leadstickers2.jpg": "photos/lead-stickers-2.webp",
        "img/products/6/sneak711-0.jpg": "photos/sneak-attack-0.webp",
        "img/products/6/sneak711-1.png": "photos/sneak-attack-1.webp",
        "img/products/6/barra.jpg": "photos/barramundi.webp",
        "img/products/7/flatcap1.jpg": "photos/flat-cap.webp",
        "video/glideway-126.jpg": "posters/glideway-126.webp",
        "video/glideway-176.jpg": "posters/glideway-176.webp",
        "video/glideway-236.jpg": "posters/glideway-236.webp",
        "video/sneakattack.jpg": "posters/sneakattack.webp",
        "img/camobg.png": "brand/camo.webp",
        "img/products/1/glideway1.png": "products/glideway-176-hero.webp",
    }
    for src, dst in jobs.items():
        photo(src, dst)
    shutil.copy(os.path.join(SRC, "img/logo.png"), out("brand/logo.png"))
    shutil.copy(os.path.join(SRC, "img/wm.png"), out("brand/sr-mark.png"))
    shutil.copy(os.path.join(SRC, "favicon-32x32.png"), out("brand/favicon.png"))

    # --- coloris détourés
    colors = json.load(open(os.path.join(ROOT, "_scrape", "colors.json")))
    for src, name in colors.items():
        pid, cid = src.split("/")[3], src.split("/")[-1].split(".")[0]
        cutout(src.lstrip("/"), f"colors/{pid}/{cid}.webp", width=900 if pid != "3" else 600)
    # la photo produit de la 126 et de la 236 : on prend le premier coloris comme visuel détouré
    print("ok", len(colors), "coloris")


if __name__ == "__main__":
    main()
