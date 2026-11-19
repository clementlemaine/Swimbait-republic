"""Génère toutes les pages HTML du site Swimbait Republic.

Le contenu (textes, specs, coloris, revendeurs) est dans les blocs DATA ci-dessous,
repris du site actuel swimbaitrepublic.com. On modifie ici, puis :  python3 build.py
"""
import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
V = "20261119-1144"  # numéro de version des fichiers css/js (mis à jour par maj.sh)

# ---------------------------------------------------------------- DATA

SOCIAL = [
    ("Instagram", "https://www.instagram.com/swimbait_republic/", "ig"),
    ("TikTok", "https://www.tiktok.com/@swimbait_republic", "tt"),
    ("Facebook", "https://www.facebook.com/swimbaitrepublic", "fb"),
    ("Spotify", "https://open.spotify.com/user/31b65vdjs4ejuoiwymn5zjxxtdke", "sp"),
]

C176 = [("14", "After Party"), ("46", "Aurora Shad"), ("47", "Bl8nkt OG"), ("1", "Bone Soldier"), ("52", "Caribe"), ("50", "EO Carp"), ("51", "EO Trout"), ("2", "Galaxy Mirror"), ("15", "Gold Rush"), ("68", "Gold Ship"), ("67", "Green Back"), ("44", "Green Glass"), ("16", "Greenade"), ("17", "Halley"), ("66", "JDM Sardine"), ("3", "Lavender Syrup"), ("69", "Matte White"), ("53", "Matte Yellow"), ("4", "Moon Walker"), ("48", "OG Red Head"), ("5", "Offspring"), ("49", "Pinky"), ("19", "Purple Shiner"), ("20", "Radioactive"), ("43", "SWCM"), ("45", "Sunset"), ("54", "Supernatural"), ("21", "Supernatural V2"), ("22", "UV Tiger")]
C126 = [("29", "After Party"), ("38", "Aurora Shad"), ("75", "Bl8nkt OG"), ("76", "Bl8nkt Shad"), ("26", "Bone Soldier"), ("41", "EO Carp"), ("42", "EO Trout"), ("71", "Galaxy Mirror"), ("34", "Gold Rush"), ("74", "Gold Ship"), ("39", "Green Back"), ("36", "Green Glass"), ("30", "Greenade"), ("31", "Halley"), ("37", "JDM Sardine"), ("27", "Lavender Syrup"), ("77", "Matte White"), ("70", "Moon Walker"), ("40", "OG Red Head"), ("28", "Offspring"), ("32", "Purple Shiner"), ("33", "Radioactive"), ("73", "Sunset"), ("55", "Supernatural"), ("35", "Supernatural V2"), ("72", "UV Tiger")]
C236 = [("59", "After Party"), ("56", "Bone Soldier"), ("65", "EO Trout"), ("60", "Greenade"), ("61", "Halley"), ("57", "Lavender Syrup"), ("58", "Moon Walker"), ("64", "Offspring"), ("62", "Radioactive"), ("63", "Supernatural V2")]
TAILS = [("8", "Brown"), ("23", "Chartreuse"), ("25", "Green Honey"), ("10", "Gunsmoke"), ("11", "Purple"), ("9", "Red Wine"), ("7", "Transparent"), ("12", "Transparent Brown"), ("24", "Transparent Purple"), ("6", "Transparent Red"), ("13", "Turquoise")]

GLIDEWAYS = {
    "126": dict(
        pid="5", colors=C126, hero="26", film="glideway-126",
        kicker="The little freestyler",
        lede="If you believe that tiny glides should also have action (besides being cute), the Glideway 126 is your bait.",
        body=[
            "This small piece of art is a total freestyler like his big brother, but with an even more electric and reactive rhythm while still being very stable.",
            "It has been perfectly balanced to adopt a natural position on the stop, but also to perform perfectly under any speed or any type of retrieve.",
        ],
        quote="Even more electric and reactive rhythm — still very stable.",
        specs=[("Weight", "29.5 g"), ("Version", "Floating"), ("Treble hooks", "BKK Super Strong 4X #5"), ("Lead Stickers", "Floating to sinking · 1 g")],
        stats=[("29.5", "g", "Weight"), ("26", "", "Colours"), ("10–12", "ft", "Max depth")],
        depth=["Slow floating", "Suspending", "Slow sinking"],
        depth_text="From surface to 10–12 ft, the depth of the Glideway 126 depends on the number of Lead Stickers you stick on the lure cavities. The lure is slow floating by itself; fill the first cavity and it turns into suspending. Fill the second cavity as well and it turns into slow sinking.",
        depth_note="",
        rig="Tie your line straight to the solid ring. For a better performance, don't add any snap or extra ring between the line and the solid ring. Finally, cast and enjoy!",
        gear=[("Line", "10 lb braid + 12 lb fluorocarbon leader"), ("Reel", "Size 201, any ratio"), ("Rod", "Moderate, 1 oz")],
        photos=[("photos/glideway-126-branch.webp", "Glideway 126 resting on a branch"), ("photos/glideway-126-hand.webp", "Glideway 126 in hand at sunset")],
    ),
    "176": dict(
        pid="1", colors=C176, hero="1", film="glideway-176",
        kicker="The original tank slayer",
        lede="The ultimate multi-species glide bait — an authentic tank slayer that will help you increase the quantity, and especially the quality, of the bites in your swimbait journeys.",
        body=[
            "The Glideway 176 has been designed to trigger the bite of those smart big fish, thanks to its realistic slow-moving action.",
            "It has been perfectly balanced to adopt a natural position on the stop, but also to perform perfectly under any speed or type of retrieve.",
        ],
        retrieves=["Fast steady", "Super slow steady", "Side walk", "Twitching", "Heavy sweeps"],
        quote="It's a true freestyler!",
        specs=[("Length", "176 mm"), ("Weight", "80 g"), ("Type", "Floating"), ("Hooks", "3X BKK trebles")],
        stats=[("176", "mm", "Length"), ("80", "g", "Weight"), ("29", "", "Colours")],
        depth=["Slow floating", "Suspending", "Slow sinking"],
        depth_text="From surface to 10–12 ft, the depth of the Glideway depends on the number of Lead Stickers you stick on the lure cavities. The lure is slow floating by itself; fill the first cavity and it turns into suspending. Fill the second cavity as well and it turns into slow sinking.",
        depth_note="The weights have been adjusted very accurately, so buoyancy also depends on water temperature: the warmer the water, the faster it sinks. The length and diameter of your fluorocarbon leader affect the sinking rate too — the longer and thicker the leader, the more it pushes the lure towards the bottom.",
        rig="Tie your line straight to its solid ring. For a better performance, make sure you don't add any snap or extra ring between the line and the solid ring.",
        gear=[],
        photos=[("photos/bass-176.webp", "Angler holding a big black bass caught on a Glideway 176"), ("photos/glideway-sunset.webp", "Three Glideway 176 at sunset")],
    ),
    "236": dict(
        pid="8", colors=C236, hero="56", film="glideway-236",
        kicker="The big guy has arrived",
        lede="The wait is finally over… The big guy has arrived! This oversized creation is a true freestyler, just like the 176 — the same smooth and natural action, with a much larger profile.",
        body=[
            "Exceptionally stable and perfectly balanced, it settles naturally on the pause and performs flawlessly at any speed or retrieve style.",
            "The key difference between the Glideway 236 and its smaller brothers is its impressive side slide. With the right input, the lure can glide sideways up to around 4 ft, creating a wide and irresistible presentation.",
        ],
        quote="Up to ~4 ft of side slide on a single input.",
        specs=[("Length", "236 mm"), ("Weight", "150 g"), ("Treble hooks", "BKK Fangs 3X 1/0"), ("Lead Stickers", "3.75 g")],
        stats=[("236", "mm", "Length"), ("150", "g", "Weight"), ("4", "ft", "Side slide")],
        depth=["Floating", "Slow floating / suspending", "Slow sinking"],
        depth_text="Running depth ranges from the surface down to approximately 10–12 ft and can be adjusted using the Lead Stickers placed inside the lure's cavities. Out of the box, the Glideway 236 is floating. Filling the first cavity makes it slow floating or suspending; filling the second turns it into a slow sinking bait.",
        depth_note="Buoyancy may vary slightly depending on water temperature and the material or thickness of your fishing line.",
        rig="For optimal performance, tie your line directly to the solid ring. Avoid snaps or additional split rings between the line and the solid ring. Finally, cast and enjoy!",
        gear=[],
        photos=[("photos/glideway-236-top.webp", "Glideway 236 held over dark water"), ("photos/glideway-236-hand.webp", "Glideway 236 hanging from the rod tip")],
    ),
}
ORDER = ["126", "176", "236"]

DEALERS = [
    ("United States", "US", "Optimum Baits", "info@optimumbaits.com", "https://www.optimumbaits.com/"),
    ("France", "FR", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("Switzerland", "CH", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("Belgium", "BE", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("Spain", "ES", "Bocarde S.L.", "info@bocarde.com", "http://www.bocarde.com/"),
    ("Portugal", "PT", "Bocarde S.L.", "info@bocarde.com", "http://www.bocarde.com/"),
]
DIRECT = [("Japan", "JP"), ("China", "CN"), ("Germany", "DE"), ("Italy", "IT"), ("Mexico", "MX"), ("Singapore", "SG")]

# ---------------------------------------------------------------- HELPERS

e = html.escape


def color_img(pid, cid):
    return f"img/colors/{pid}/{cid}.webp"


ICONS = {
    "ig": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>',
    "tt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M14 3c.4 2.6 2.3 4.6 5 4.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 21v-7.5h2.6l.4-3h-3V8.7c0-.9.3-1.5 1.6-1.5h1.5V4.5c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.3H9.2v3h2.5V21" fill="currentColor"/></svg>',
    "sp": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.5 9.5c3-1 6.5-.7 9 .8M8 12.6c2.5-.7 5.2-.4 7.3.8M8.6 15.4c2-.5 4-.3 5.6.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg>',
    "play": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',
}


def btn(href, label, cls="btn"):
    return f'<a class="{cls}" href="{href}"><span>{label}</span>{ICONS["arrow"]}</a>'


def socials(cls="social"):
    return f'<ul class="{cls}">' + "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{ICONS[k]}</a></li>' for n, u, k in SOCIAL
    ) + "</ul>"


NAV = [
    ("swimbaits.html", "Swimbaits", "swimbaits"),
    ("accessories.html", "Accessories", "accessories"),
    ("sneak-attack-711.html", "Rods", "rods"),
    ("apparel.html", "Apparel", "apparel"),
    ("about.html", "About", "about"),
    ("dealers.html", "Dealers", "dealers"),
]


def layout(slug, title, desc, body, section="", hero_dark=True):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if section == s else ""}>{l}</a></li>' for h, l, s in NAV
    )
    mobile_nav = "".join(
        f'<li><a href="{h}"><small>0{i+1}</small>{l}</a></li>' for i, (h, l, s) in enumerate(NAV + [("contact.html", "Contact", "contact")])
    )
    t = e(title)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Swimbait Republic">
<meta property="og:image" content="img/posters/hero.webp">
<meta name="theme-color" content="#0e110c">
<link rel="icon" type="image/png" href="img/brand/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=Barlow:wght@400;500;600;700&family=Black+Ops+One&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="css/style.css?v={V}">
<script>document.documentElement.classList.add('js');setTimeout(function(){{var c=document.querySelector('.curtain');if(c&&!c.classList.contains('is-in'))c.classList.add('is-out')}},2500);</script>
</head>
<body class="page-{slug}{' hero-light' if not hero_dark else ''}">
<a class="skip" href="#main">Skip to content</a>
<div class="grain" aria-hidden="true"></div>
<div class="progress" aria-hidden="true"><span></span></div>
<div class="curtain" aria-hidden="true"><img src="img/brand/logo.png" alt=""></div>

<header class="nav" id="nav">
  <a class="nav-logo" href="index.html" aria-label="Swimbait Republic — home"><img src="img/brand/logo.png" alt="Swimbait Republic" width="166" height="41"></a>
  <nav aria-label="Main"><ul class="nav-links">{nav}</ul></nav>
  <a class="nav-cta" href="contact.html">Contact</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
</header>
<div class="menu" id="menu" hidden>
  <ul>{mobile_nav}</ul>
  {socials("social menu-social")}
</div>

<main id="main">
{body}
</main>

<footer class="footer">
  <div class="footer-top">
    <div class="footer-cta">
      <p class="eyebrow">Join the Republic</p>
      <p class="footer-title">Big baits.<br>Bigger bites.</p>
      {socials()}
      <p class="footer-handle">@swimbait_republic</p>
    </div>
    <div class="footer-cols">
      <div><p class="footer-h">Products</p>
        <a href="glideway-126.html">Glideway 126</a><a href="glideway-176.html">Glideway 176</a><a href="glideway-236.html">Glideway 236</a>
        <a href="accessories.html">Spare Tails &amp; Lead Stickers</a><a href="sneak-attack-711.html">Sneak Attack 711</a><a href="apparel.html">Flat Cap</a></div>
      <div><p class="footer-h">Republic</p>
        <a href="about.html">About us</a><a href="dealers.html">Locate a dealer</a><a href="contact.html">Contact us</a></div>
      <div><p class="footer-h">Legal</p>
        <a href="https://www.swimbaitrepublic.com/privacy-policy">Privacy policy</a><a href="https://www.swimbaitrepublic.com/cookie-policy">Cookie policy</a><a href="https://www.swimbaitrepublic.com/terms-and-conditions">Legal notice</a></div>
    </div>
  </div>
  <div class="footer-word" aria-hidden="true">SWIMBAIT REPUBLIC</div>
  <div class="footer-bottom"><span>© Swimbait Republic</span><span>Garage designed &amp; worldwide tested</span><span class="ver" id="ver">{V}</span></div>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="js/app.js?v={V}" defer></script>
</body>
</html>
"""


def page_hero(kicker, title, lede, img, extra=""):
    return f"""
<section class="phero">
  <div class="phero-media" data-parallax><img src="{img}" alt="" fetchpriority="high"></div>
  <div class="phero-inner wrap">
    <p class="eyebrow" data-reveal>{kicker}</p>
    <h1 class="display" data-split>{title}</h1>
    <p class="lede" data-reveal>{lede}</p>
    {extra}
  </div>
</section>"""


def marquee(items, cls=""):
    row = "".join(f"<span>{i}</span><b aria-hidden='true'>✕</b>" for i in items)
    return f'<div class="marquee {cls}" aria-hidden="true"><div class="marquee-track">{row}{row}{row}</div></div>'


def depth_module(g, name, interactive=True):
    states = "".join(
        f'<button class="depth-btn{" is-on" if i == 0 else ""}" data-depth="{i}" aria-pressed="{"true" if i == 0 else "false"}"><span class="depth-n">{i}</span><span>{"No sticker" if i == 0 else ("1st cavity" if i == 1 else "2nd cavity")}</span><strong>{s}</strong></button>'
        for i, s in enumerate(g["depth"])
    )
    lure = color_img(g["pid"], g["hero"])
    return f"""
<section class="depth" data-depth-module>
  <div class="wrap depth-grid">
    <div class="depth-copy">
      <p class="eyebrow" data-reveal>Lead Stickers · buoyancy</p>
      <h2 class="h2" data-split>Dial in your depth.</h2>
      <p data-reveal>{g["depth_text"]}</p>
      {f'<p class="note" data-reveal>{g["depth_note"]}</p>' if g["depth_note"] else ""}
      <div class="depth-btns" role="group" aria-label="Lead Stickers">{states}</div>
    </div>
    <div class="depth-tank" aria-hidden="true">
      <div class="depth-surface"></div>
      <ol class="depth-ruler"><li>0 ft</li><li>3</li><li>6</li><li>9</li><li>12 ft</li></ol>
      <div class="depth-lure" data-state="0"><img src="{lure}" alt=""><span class="depth-tag">{g["depth"][0]}</span></div>
      <div class="depth-bubbles"><i></i><i></i><i></i><i></i><i></i></div>
    </div>
  </div>
</section>"""


def color_chart(pid, colors, name, start=None):
    start = start or colors[0][0]
    sname = dict(colors)[start]
    items = "".join(
        f'<li><button class="swatch{" is-on" if cid == start else ""}" data-src="{color_img(pid, cid)}" data-name="{e(n)}" aria-pressed="{"true" if cid == start else "false"}">'
        f'<img src="{color_img(pid, cid)}" alt="" loading="lazy"><span>{e(n)}</span></button></li>'
        for cid, n in colors
    )
    return f"""
<section class="chart" id="colours">
  <div class="wrap">
    <div class="chart-head">
      <div><p class="eyebrow" data-reveal>Colour chart · {len(colors)} finishes</p>
      <h2 class="h2" data-split>Pick your poison.</h2></div>
      <p class="chart-hint" data-reveal>Tap a colour to inspect it.</p>
    </div>
    <div class="viewer" data-reveal>
      <div class="viewer-stage"><img class="viewer-img" src="{color_img(pid, start)}" alt="{e(name)} — {e(sname)}"></div>
      <div class="viewer-meta"><span class="mono">{e(name)}</span><strong class="viewer-name">{e(sname)}</strong></div>
    </div>
    <ul class="swatches">{items}</ul>
  </div>
</section>"""


def film(src, poster, title):
    return f"""
<section class="film" data-reveal>
  <div class="film-frame">
    <video class="film-video" preload="none" playsinline poster="img/posters/{poster}.webp" src="media/{src}.mp4"></video>
    <button class="film-play" aria-label="Play the film: {e(title)}"><span class="film-btn">{ICONS["play"]}</span><span class="film-label"><small>Watch the film</small>{e(title)}</span></button>
  </div>
</section>"""


def stats(items):
    return '<dl class="stats">' + "".join(
        f'<div data-reveal><dt>{l}</dt><dd><span data-count="{n}">{n}</span><em>{u}</em></dd></div>' for n, u, l in items
    ) + "</dl>"


# ---------------------------------------------------------------- PAGES


def home():
    fam = ""
    for k in ORDER:
        g = GLIDEWAYS[k]
        w = round(int(k) / 236 * 100, 1)
        weight = dict(g["specs"])["Weight"]
        fam += f"""
      <a class="fam-row" href="glideway-{k}.html" style="--w:{w}%">
        <span class="fam-name"><small>Glideway</small>{k}</span>
        <span class="fam-lure"><img src="{color_img(g['pid'], g['hero'])}" alt="Glideway {k}" loading="lazy"></span>
        <span class="fam-meta"><b>{weight}</b><em>{len(g['colors'])} colours</em>{ICONS['arrow']}</span>
      </a>"""
    row1 = "".join(f'<img src="{color_img("1", c)}" alt="" loading="lazy">' for c, _ in C176[:15])
    row2 = "".join(f'<img src="{color_img("1", c)}" alt="" loading="lazy">' for c, _ in C176[15:])
    steps = [
        ("01", "Concept", "First a concept or an idea clicks in our brain.", "photos/production.webp"),
        ("02", "The draw", "Then comes the drawing: the shape, the joint, the cavities.", "photos/glideway-sunset.webp"),
        ("03", "Wood & resin", "A wooden prototype, then a lot of resin prototypes to try every possible weight configuration and bait thickness.", "photos/prototypes.webp"),
        ("04", "Field testing", "Up to 2 years of field testing before releasing a product — it has to perform everywhere, and get love from fish.", "photos/testing.webp"),
        ("05", "Production", "We supervise the whole process personally, from shell injection to packing.", "photos/bass-reeds.webp"),
    ]
    st = "".join(
        f'<article class="step"><div class="step-img"><img src="img/{img}" alt="" loading="lazy"></div><p class="step-n">{n}</p><h3>{h}</h3><p>{p}</p></article>'
        for n, h, p, img in steps
    )
    countries = [d[0] for d in DEALERS] + [d[0] for d in DIRECT]
    body = f"""
<section class="hero" data-hero>
  <div class="hero-media">
    <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="img/posters/hero.webp"><source src="media/hero-loop.mp4" type="video/mp4"></video>
  </div>
  <div class="hero-inner wrap">
    <p class="eyebrow hero-eyebrow">Garage designed · worldwide tested</p>
    <h1 class="hero-title"><span class="hero-small" data-split>This is all about</span><span class="hero-big" data-split>Swimbaits.</span></h1>
    <div class="hero-foot">
      <p class="lede">Off-road swimbaits that will help you increase the quantity — and especially the quality — of the bites on your fishing journeys.</p>
      <div class="hero-ctas">{btn("swimbaits.html", "Meet the Glideway")}{btn("#film", "Watch the film", "btn btn-ghost")}</div>
    </div>
  </div>
  <div class="hero-scroll" aria-hidden="true"><span>Scroll</span><i></i></div>
</section>

{marquee(["No jerkbaits", "No jigs", "No worms", "No crankbaits", "Only swimbaits"], "marquee-red")}

<section class="manifesto">
  <div class="wrap">
    <p class="eyebrow" data-reveal>The Republic manifesto</p>
    <p class="manifesto-text" data-words>If you're looking for jerkbaits, jigs, worms, crankbaits… you're in the wrong place. We put over 10 years of swimbait fishing into every lure we make — to help anglers catch bigger fish, in an easier way.</p>
    {stats([("10", "+", "Years of swimbait fishing"), ("2", "yrs", "Of field testing, max"), ("3", "", "Glideway sizes"), ("12", "", "Countries")])}
  </div>
</section>

<section class="family" id="family">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow" data-reveal>The Glideway family · to scale</p>
      <h2 class="h2" data-split>Three sizes.<br>One freestyler.</h2>
      <p data-reveal>Slow floating out of the box, balanced to sit natural on the stop and swim at any speed. Pick the size that matches the fish you're after.</p>
    </div>
    <div class="fam-list">{fam}
    </div>
  </div>
</section>

<section class="glide" data-glide aria-label="Glide action">
  <div class="glide-sticky">
    <div class="glide-water" aria-hidden="true"></div>
    <p class="glide-word" aria-hidden="true">Freestyle</p>
    <div class="glide-lure" aria-hidden="true"><img src="{color_img('1', '16')}" alt=""></div>
    <div class="glide-copy wrap">
      <p class="eyebrow">The action</p>
      <p class="glide-list"><span>Fast steady</span><span>Super slow steady</span><span>Side walk</span><span>Twitching</span><span>Heavy sweeps</span></p>
    </div>
  </div>
</section>

{depth_module(GLIDEWAYS["176"], "Glideway 176")}

<div id="film">{film("glideway-236", "glideway-236", "Glideway 236 — the big guy")}</div>

<section class="parade">
  <div class="wrap parade-head">
    <div><p class="eyebrow" data-reveal>29 finishes on the 176</p><h2 class="h2" data-split>A colour for every mood of the water.</h2></div>
    {btn("glideway-176.html#colours", "See the colour chart", "btn btn-ghost")}
  </div>
  <div class="parade-row" data-dir="1"><div class="parade-track">{row1}{row1}</div></div>
  <div class="parade-row" data-dir="-1"><div class="parade-track">{row2}{row2}</div></div>
</section>

<section class="gear">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow" data-reveal>Beyond the bait</p><h2 class="h2" data-split>Gear up.</h2></div>
    <div class="gear-grid">
      <a class="gcard" href="accessories.html" data-reveal><div class="gcard-img"><img src="img/photos/spare-tail-2.webp" alt="" loading="lazy"></div><p class="gcard-n">01</p><h3>Accessories</h3><p>Spare Tails &amp; Lead Stickers — customise colour and buoyancy.</p>{ICONS['arrow']}</a>
      <a class="gcard" href="sneak-attack-711.html" data-reveal><div class="gcard-img"><img src="img/posters/sneakattack.webp" alt="" loading="lazy"></div><p class="gcard-n">02</p><h3>Sneak Attack 711</h3><p>Toray 11,000T carbon, 1–3 oz, 14 titanium guides.</p>{ICONS['arrow']}</a>
      <a class="gcard" href="apparel.html" data-reveal><div class="gcard-img"><img src="img/photos/flat-cap.webp" alt="" loading="lazy"></div><p class="gcard-n">03</p><h3>Apparel</h3><p>The Republic flat cap. Embroidered, breathable, one size.</p>{ICONS['arrow']}</a>
    </div>
  </div>
</section>

<section class="process" data-hscroll>
  <div class="process-pin">
    <div class="process-intro">
      <p class="eyebrow">How our lures are born</p>
      <h2 class="h2">From the garage<br>to the water.</h2>
      <p>A mix of creativity and artisan skills.</p>
      {btn("about.html", "Our story", "btn btn-ghost")}
    </div>
    <div class="process-view"><div class="process-track">{st}</div></div>
  </div>
</section>

<section class="dealers-band">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Worldwide</p>
    <h2 class="h2" data-split>Fishing in 12 countries.</h2>
    <ul class="country-cloud">{''.join(f'<li data-reveal>{c}</li>' for c in countries)}</ul>
    {btn("dealers.html", "Find a dealer")}
  </div>
</section>
"""
    return layout("home", "Swimbait Republic — This is all about swimbaits",
                  "Off-road swimbaits that will help you increase the quantity and especially the quality of the bites on your fishing journeys. Glideway 126, 176 and 236.", body)


def swimbaits():
    rows = ""
    for i, k in enumerate(ORDER):
        g = GLIDEWAYS[k]
        dots = "".join(f'<img src="{color_img(g["pid"], c)}" alt="" loading="lazy">' for c, _ in g["colors"][:6])
        specs = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in g["specs"])
        rows += f"""
  <article class="prow{' prow-rev' if i % 2 else ''}">
    <a class="prow-visual" href="glideway-{k}.html" aria-label="Glideway {k}">
      <span class="prow-num" aria-hidden="true">{k}</span>
      <img src="{color_img(g['pid'], g['hero'])}" alt="Glideway {k}" data-float>
    </a>
    <div class="prow-copy">
      <p class="eyebrow" data-reveal>{g['kicker']}</p>
      <h2 class="stencil" data-split>Glideway {k}</h2>
      <p data-reveal>{g['lede']}</p>
      <dl class="mini-specs" data-reveal>{specs}</dl>
      <div class="prow-colors" data-reveal><span class="mono">{len(g['colors'])} colours</span><div>{dots}</div></div>
      {btn(f"glideway-{k}.html", f"Discover the {k}")}
    </div>
  </article>"""
    comp_rows = [
        ("Length", ["—", "176 mm", "236 mm"]),
        ("Weight", ["29.5 g", "80 g", "150 g"]),
        ("Hooks", ["BKK Super Strong 4X #5", "3X BKK trebles", "BKK Fangs 3X 1/0"]),
        ("Out of the box", ["Slow floating", "Slow floating", "Floating"]),
        ("Depth range", ["Surface – 10/12 ft"] * 3),
        ("Colours", [str(len(GLIDEWAYS[k]["colors"])) for k in ORDER]),
    ]
    table = "".join(f"<tr><th scope='row'>{a}</th>{''.join(f'<td>{x}</td>' for x in v)}</tr>" for a, v in comp_rows)
    body = page_hero("Category 01 · Swimbaits", "Swimbaits", "If you're looking for jerkbaits, jigs, worms, crankbaits… you're in the wrong place. This is all about swimbaits.",
                     "img/photos/glideway-sunset.webp") + f"""
<section class="products wrap">{rows}
</section>
<section class="compare wrap">
  <p class="eyebrow" data-reveal>Side by side</p>
  <h2 class="h2" data-split>Compare the family.</h2>
  <div class="table-scroll" data-reveal><table>
    <thead><tr><th></th>{''.join(f'<th scope="col"><a href="glideway-{k}.html">Glideway {k}</a></th>' for k in ORDER)}</tr></thead>
    <tbody>{table}</tbody></table></div>
</section>
{marquee(["Garage designed", "Worldwide tested", "Slow floating", "Suspending", "Slow sinking"], "marquee-olive")}
"""
    return layout("swimbaits", "Swimbaits — Glideway 126, 176 & 236 | Swimbait Republic",
                  "The Glideway family: multi-species glide baits in 126, 176 and 236 sizes. Garage designed and worldwide tested.", body, "swimbaits")


def glideway(k):
    g = GLIDEWAYS[k]
    name = f"Glideway {k}"
    i = ORDER.index(k)
    prev_k, next_k = ORDER[i - 1] if i > 0 else None, ORDER[i + 1] if i < 2 else None
    specs = "".join(f'<div data-reveal><dt>{a}</dt><dd>{b}</dd></div>' for a, b in g["specs"])
    body_p = "".join(f"<p data-reveal>{p}</p>" for p in g["body"])
    retr = ""
    if g.get("retrieves"):
        retr = '<ul class="chips" data-reveal>' + "".join(f"<li>{r}</li>" for r in g["retrieves"]) + "</ul>"
    gear = ""
    if g["gear"]:
        gear = '<div class="gear-rec" data-reveal><p class="eyebrow">Recommended gear</p><dl>' + "".join(
            f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in g["gear"]) + "</dl></div>"
    p1, p2 = g["photos"]
    nav = ""
    for kk, lab in ((prev_k, "Smaller brother"), (next_k, "Bigger brother")):
        if kk:
            gg = GLIDEWAYS[kk]
            nav += f'<a class="pnav-item" href="glideway-{kk}.html"><small>{lab}</small><strong>Glideway {kk}</strong><img src="{color_img(gg["pid"], gg["hero"])}" alt="" loading="lazy"></a>'
    body = f"""
<section class="pd-hero">
  <div class="pd-camo" aria-hidden="true"></div>
  <p class="pd-ghost" aria-hidden="true">{k}</p>
  <div class="wrap pd-hero-inner">
    <a class="crumb" href="swimbaits.html">← Swimbaits</a>
    <p class="eyebrow">{g['kicker']}</p>
    <h1 class="stencil pd-title" data-split>{name}</h1>
    <div class="pd-lure"><img src="{color_img(g['pid'], g['hero'])}" alt="{name}" fetchpriority="high"></div>
    <div class="pd-hero-foot">
      <p class="pd-tag">Garage designed &amp; worldwide tested</p>
      <div class="hero-ctas">{btn('#colours', 'Colour chart')}{btn('dealers.html', 'Where to buy', 'btn btn-ghost')}</div>
    </div>
  </div>
</section>

<section class="pd-intro">
  <div class="wrap pd-intro-grid">
    <div>
      <p class="pd-lede" data-words>{g['lede']}</p>
    </div>
    <div class="pd-body">{body_p}{retr}<blockquote data-reveal>“{g['quote']}”</blockquote></div>
  </div>
  <div class="wrap">{stats(g['stats'])}</div>
</section>

<section class="pd-photos wrap">
  <figure class="ph-big" data-reveal><div class="ph-clip"><img src="img/{p1[0]}" alt="{e(p1[1])}" loading="lazy" data-parallax-img></div></figure>
  <figure class="ph-small" data-reveal><div class="ph-clip"><img src="img/{p2[0]}" alt="{e(p2[1])}" loading="lazy" data-parallax-img></div></figure>
</section>

{depth_module(g, name)}

<section class="specs wrap">
  <div class="specs-head"><p class="eyebrow" data-reveal>Technical file</p><h2 class="h2" data-split>Specifications.</h2></div>
  <dl class="spec-sheet">{specs}</dl>
  <div class="rig" data-reveal><p class="eyebrow">Rigging tip</p><p>{g['rig']}</p></div>
  {gear}
</section>

{film(g['film'], g['film'], name)}

{color_chart(g['pid'], g['colors'], name, g['hero'])}

<section class="upsell wrap">
  <a class="upsell-card" href="accessories.html" data-reveal>
    <img src="img/photos/lead-stickers-2.webp" alt="" loading="lazy">
    <div><p class="eyebrow">Make it yours</p><h3>Spare Tails &amp; Lead Stickers</h3><p>Change the colour of the tail, change the depth of the dive.</p>{ICONS['arrow']}</div>
  </a>
</section>

<nav class="pnav wrap" aria-label="Other Glideway sizes">{nav}</nav>
"""
    return layout(f"glideway-{k}", f"{name} — {g['kicker']} | Swimbait Republic", g["lede"], body, "swimbaits")


def accessories():
    tails = "".join(
        f'<li><button class="swatch swatch-tail" data-src="{color_img("3", c)}" data-name="{e(n)}" aria-pressed="false"><img src="{color_img("3", c)}" alt="" loading="lazy"><span>{e(n)}</span></button></li>'
        for c, n in TAILS
    )
    whens = [
        ("Suspend or sink", "When you want the Glideway to suspend or to sink — it's a floating bait by itself."),
        ("Heavy wind", "When it's very windy: the wind pushes the line and tends to bring the lure up."),
        ("High banks", "When fishing from a cliff or any structure high above the water, because you're pulling the bait towards the surface."),
        ("Cold water", "When the water gets cold, to compensate the extra buoyancy — any lure floats more in cold water, which is denser than warm water."),
        ("Max distance", "When you need maximum casting distance. Yes, even 3 extra grams will help you cast longer!"),
    ]
    wl = "".join(f'<li data-reveal><span class="when-n">0{i+1}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(whens))
    body = page_hero("Category 02 · Accessories", "Accessories", "As the nerd anglers we are, we love to customise our swimbaits! Sinkers, Spare Tails and many others coming.",
                     "img/photos/glideway-glow.webp") + f"""
<section class="acc wrap">
  <div class="acc-grid">
    <div class="acc-copy">
      <p class="eyebrow" data-reveal>Accessory 01</p>
      <h2 class="stencil" data-split>Spare Tail</h2>
      <p data-reveal>One more accessory to customise the look of your Glideway with a special colour touch. Some days, little details really make the difference — and this can be one of them.</p>
      <p data-reveal>Our tails are made of tough silicone: hard to deform and highly resistant to toothy fish.</p>
      <p class="note" data-reveal>Tip: remove the tail from the Glideway before storing it back in your tackle box, to avoid any possible deformation.</p>
    </div>
    <div class="tail-viewer viewer" data-reveal>
      <div class="viewer-stage"><img class="viewer-img" src="{color_img('3', TAILS[1][0])}" alt="Spare Tail — {TAILS[1][1]}"></div>
      <div class="viewer-meta"><span class="mono">Spare Tail · {len(TAILS)} colours</span><strong class="viewer-name">{TAILS[1][1]}</strong></div>
    </div>
  </div>
  <ul class="swatches swatches-tails">{tails}</ul>
  <div class="duo">
    <figure data-reveal><div class="ph-clip"><img src="img/photos/spare-tail-1.webp" alt="Spare Tail on a Glideway" loading="lazy"></div></figure>
    <figure data-reveal><div class="ph-clip"><img src="img/photos/spare-tail-2.webp" alt="Purple Spare Tail" loading="lazy"></div></figure>
  </div>
</section>

{marquee(["Tune the colour", "Tune the depth", "Tune the cast"], "marquee-red")}

<section class="acc wrap">
  <div class="acc-grid acc-grid-rev">
    <div class="acc-copy">
      <p class="eyebrow" data-reveal>Accessory 02</p>
      <h2 class="stencil" data-split>Lead Stickers</h2>
      <p data-reveal>Designed to adjust the buoyancy of your Glideway, so you can fish different layers of the water column — or simply compensate for the elements, like low water temperature or heavy wind.</p>
      <p class="note" data-reveal>To remove them, use the gap in the Glideway cavities to slide in the treble and pull the sticker out. Lead Stickers can also be used to fine-tune the weight of any other lure.</p>
    </div>
    <figure class="acc-photo" data-reveal><div class="ph-clip"><img src="img/photos/lead-stickers-2.webp" alt="Lead Sticker being removed with a treble hook" loading="lazy"></div></figure>
  </div>
  <h3 class="when-title" data-reveal>When should you add them?</h3>
  <ol class="whens">{wl}</ol>
</section>
"""
    return layout("accessories", "Accessories — Spare Tails & Lead Stickers | Swimbait Republic",
                  "Spare Tails in 11 colours and Lead Stickers to tune the buoyancy of your Glideway.", body, "accessories")


def rod():
    body = f"""
<section class="phero phero-rod">
  <div class="phero-media" data-parallax><img src="img/photos/rod-hero.webp" alt="" fetchpriority="high"></div>
  <div class="phero-inner wrap">
    <p class="eyebrow" data-reveal>Category 03 · Rods</p>
    <h1 class="stencil display-stencil" data-split>Sneak Attack 711</h1>
    <p class="lede" data-reveal>Designed to adapt to multiple scenarios and techniques, with outstanding versatility across a 1 to 3 oz lure range.</p>
  </div>
</section>
<section class="pd-intro">
  <div class="wrap">{stats([("7'11", '"', "Length"), ("1–3", "oz", "Lure range"), ("14", "", "Titanium guides"), ("200", "", "Reel size")])}</div>
  <div class="wrap pd-intro-grid">
    <p class="pd-lede" data-words>Built with a Toray 11,000T carbon blank — extreme lightness, exceptional strength, and a weight-to-power ratio that's hard to match.</p>
    <div class="pd-body">
      <p data-reveal>Pair it with a size 200 reel for perfect balance and handling comfort. Its smooth, progressive action allows precise control of lighter lures while keeping the power to snap cast a 3 oz lure over long distances with complete confidence.</p>
      <p data-reveal>Unlike typical swimbait rods, it absorbs the excess energy of the cast instead of sending it to your elbow and shoulder — so you can keep bombing big baits all day long without pain or fatigue.</p>
      <p data-reveal>The progressive action also absorbs the head shakes during the fight, significantly reducing the chances of losing the fish.</p>
      <p class="note" data-reveal>Designed to perform at 100% with braided line. Not recommended with fluorocarbon as the main line.</p>
    </div>
  </div>
</section>
<section class="rod-strip" aria-hidden="true"><img src="img/photos/sneak-attack-0.webp" alt="" data-rod></section>
<section class="guides">
  <div class="wrap guides-grid">
    <div class="guides-big" aria-hidden="true"><span data-count="14">14</span><small>titanium guides</small></div>
    <div>
      <p class="eyebrow" data-reveal>Guide system</p>
      <h2 class="h2" data-split>Wind knots, virtually eliminated.</h2>
      <p data-reveal>A guide layout engineered to channel line flow with maximum efficiency. The 14 titanium guides control every contact point and keep the line perfectly aligned, reducing friction and turbulence.</p>
      <p data-reveal>The short spacing between guides stops the line from forming loops or tangles during the cast or the retrieve. And the generous inner diameter lets leader knots pass with minimal friction, even with thick leaders.</p>
    </div>
  </div>
</section>
<section class="pd-photos wrap">
  <figure class="ph-big" data-reveal><div class="ph-clip"><img src="img/photos/banner-3.webp" alt="Sneak Attack 711 rod" loading="lazy" data-parallax-img></div></figure>
  <figure class="ph-small" data-reveal><div class="ph-clip"><img src="img/photos/barramundi.webp" alt="Angler with a large fish caught with the Sneak Attack 711" loading="lazy" data-parallax-img></div></figure>
</section>
<section class="specs wrap">
  <div class="specs-head"><p class="eyebrow" data-reveal>Technical file</p><h2 class="h2" data-split>Specifications.</h2></div>
  <dl class="spec-sheet"><div data-reveal><dt>Length</dt><dd>7'11"</dd></div><div data-reveal><dt>Lure range</dt><dd>1–3 oz</dd></div><div data-reveal><dt>Braid</dt><dd>15–30 lb</dd></div><div data-reveal><dt>Reel size</dt><dd>200</dd></div></dl>
</section>
{film("sneakattack", "sneakattack", "Sneak Attack 711")}
<section class="upsell wrap">
  <a class="upsell-card" href="swimbaits.html" data-reveal>
    <img src="img/photos/glideway-sunset.webp" alt="" loading="lazy">
    <div><p class="eyebrow">Load it up</p><h3>The Glideway family</h3><p>126, 176 and 236 — three sizes of freestyle glide.</p>{ICONS['arrow']}</div>
  </a>
</section>
"""
    return layout("rods", "Sneak Attack 711 — swimbait rod 1–3 oz | Swimbait Republic",
                  "Sneak Attack 711: Toray 11,000T carbon swimbait rod, 7'11\", 1–3 oz, 14 titanium guides.", body, "rods")


def apparel():
    feats = [("Embroidered logo", "on the central panel"), ("Printed visor", "Republic pattern underneath"), ("Breathable mesh", "keeps you cool"), ("Snapback", "adjustable, anti-rust closure"), ("One size", "fits most")]
    fl = "".join(f'<li data-reveal><strong>{a}</strong><span>{b}</span></li>' for a, b in feats)
    body = page_hero("Category 04 · Apparel", "Apparel", "Wear the flag.", "img/photos/banner-4.webp") + f"""
<section class="acc wrap">
  <div class="acc-grid">
    <figure class="acc-photo" data-reveal><div class="ph-clip"><img src="img/photos/flat-cap.webp" alt="Swimbait Republic flat cap surrounded by Glideway lures" loading="lazy"></div></figure>
    <div class="acc-copy">
      <p class="eyebrow" data-reveal>Apparel 01</p>
      <h2 class="stencil" data-split>Flat Cap</h2>
      <p data-reveal>The Swimbait Republic Flat Cap features an embroidered logo on the central panel and a printed visor. Breathable mesh keeps you cool, and the adjustable snapback includes an anti-rust closure. One size fits most.</p>
      <ul class="feats">{fl}</ul>
      {btn("dealers.html", "Find a dealer")}
    </div>
  </div>
</section>
"""
    return layout("apparel", "Apparel — Flat Cap | Swimbait Republic", "The Swimbait Republic Flat Cap: embroidered logo, printed visor, breathable mesh, adjustable snapback.", body, "apparel")


def about():
    body = page_hero("About us", "About the Republic", "Over 10 years of swimbait fishing, and a whole life dedicated to many other lure techniques.",
                     "img/photos/production.webp") + f"""
<section class="manifesto manifesto-light">
  <div class="wrap">
    <p class="manifesto-text" data-words>We put all our experience into our lures to help anglers catch bigger fish in an easier way — with the highest quality raw materials and handcraft work, for the best possible price, while ensuring good margins for all our business partners.</p>
  </div>
</section>
<section class="story wrap">
  <article class="story-row">
    <figure data-reveal><div class="ph-clip"><img src="img/photos/prototypes.webp" alt="Glideway prototypes at different stages" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">01</p><h2 class="h2" data-split>How are our lures born?</h2><p data-reveal>First a concept or an idea clicks in our brain. Then comes the draw, after that a wooden prototype, and finally a lot of resin prototypes to try every possible weight configuration, bait thickness… This process is a mix of creativity and artisan skills.</p></div>
  </article>
  <article class="story-row story-rev">
    <figure data-reveal><div class="ph-clip"><img src="img/photos/testing.webp" alt="Angler with a large bass during field testing" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">02</p><h2 class="h2" data-split>Testing.</h2><p data-reveal>One of the most important parts of the process: even if the lure swims great in the tank, we have to make sure it performs in different conditions and scenarios — and that fish love it!</p>
    <p class="big-fact" data-reveal><span data-count="2">2</span> years<small>of field testing, at most, before a release</small></p></div>
  </article>
  <article class="story-row">
    <figure data-reveal><div class="ph-clip"><img src="img/photos/bass-reeds.webp" alt="Big black bass caught on a Glideway" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">03</p><h2 class="h2" data-split>Production.</h2><p data-reveal>Having an amazing bait means nothing to us if we can't make it available for everybody. We travel the world to find high quality factories to produce our creations, and we personally supervise the whole process — from shell injection to packing — to make sure everything reaches the quality level we aim for.</p></div>
  </article>
</section>
{marquee(["Concept", "Draw", "Wood", "Resin", "Test", "Produce"], "marquee-olive")}
<section class="upsell wrap">
  <a class="upsell-card" href="swimbaits.html" data-reveal>
    <img src="img/photos/glideway-sunset.webp" alt="" loading="lazy">
    <div><p class="eyebrow">The result</p><h3>Meet the Glideway</h3><p>Three sizes, one freestyle action.</p>{ICONS['arrow']}</div>
  </a>
</section>
"""
    return layout("about", "About us | Swimbait Republic", "Over 10 years of swimbait fishing put into every lure: concept, prototypes, up to 2 years of field testing, supervised production.", body, "about")


def dealers():
    cards = "".join(
        f'<article class="dcard" data-reveal><span class="dcode">{code}</span><h3>{c}</h3><p class="dname">{n}</p>'
        f'<a href="mailto:{m}">{m}</a><a href="{w}" target="_blank" rel="noopener">{w.split("//")[1].strip("/")} ↗</a></article>'
        for c, code, n, m, w in DEALERS
    )
    direct = "".join(f'<li data-reveal><span class="dcode">{code}</span>{c}</li>' for c, code in DIRECT)
    body = page_hero("Worldwide", "Our dealers", "Find the Republic near you — or talk to us directly.", "img/photos/glideway-236-top.webp") + f"""
<section class="dealers wrap">
  <p class="eyebrow" data-reveal>Official distributors</p>
  <div class="dgrid">{cards}</div>
  <div class="direct">
    <div><p class="eyebrow" data-reveal>Direct to tackle shops</p><h2 class="h2" data-split>No dealer in your country yet?</h2>
    <p data-reveal>In these countries we work directly with tackle shops. Shop owner or angler, get in touch.</p>{btn("contact.html", "Contact us")}</div>
    <ul class="direct-list">{direct}</ul>
  </div>
</section>
"""
    return layout("dealers", "Dealers worldwide | Swimbait Republic", "Swimbait Republic dealers in the United States, France, Switzerland, Belgium, Spain and Portugal — and direct to tackle shops in 6 more countries.", body, "dealers")


def contact():
    body = page_hero("Contact", "Talk to us", "Have a question or a comment for our team? We'd love to hear from you.", "img/photos/glideway-126-branch.webp") + f"""
<section class="contact wrap">
  <form class="cform" data-reveal novalidate>
    <label><span>Name</span><input name="name" required autocomplete="name"></label>
    <label><span>Email</span><input name="email" type="email" required autocomplete="email"></label>
    <label class="full"><span>Message</span><textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit"><span>Send message</span>{ICONS['arrow']}</button>
    <p class="form-msg" role="status" aria-live="polite"></p>
  </form>
  <aside class="contact-side" data-reveal>
    <p class="eyebrow">Or slide into our DMs</p>
    <p>Send us a message through our social media profiles.</p>
    {socials("social social-big")}
    <p class="eyebrow" style="margin-top:2.5rem">Looking for a shop?</p>
    {btn("dealers.html", "Locate a dealer", "btn btn-ghost")}
  </aside>
</section>
"""
    return layout("contact", "Contact us | Swimbait Republic", "Get in touch with Swimbait Republic.", body)


# ---------------------------------------------------------------- BUILD

def main():
    pages = {
        "index.html": home(),
        "swimbaits.html": swimbaits(),
        "accessories.html": accessories(),
        "sneak-attack-711.html": rod(),
        "apparel.html": apparel(),
        "about.html": about(),
        "dealers.html": dealers(),
        "contact.html": contact(),
    }
    for k in ORDER:
        pages[f"glideway-{k}.html"] = glideway(k)
    for name, content in pages.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(len(pages), "pages générées")


if __name__ == "__main__":
    main()
