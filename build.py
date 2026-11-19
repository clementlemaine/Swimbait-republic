"""Génère toutes les pages HTML du site Swimbait Republic, en 3 langues.

- espagnol (langue par défaut) : index.html, swimbaits.html, glideway-176.html …
- anglais : index-en.html, swimbaits-en.html, glideway-176-en.html …
- français : index-fr.html, swimbaits-fr.html, glideway-176-fr.html …

Tout le texte est ici, sous la forme L("anglais", "français", "espagnol").
Le contenu vient du site actuel swimbaitrepublic.com (anglais) ; le français et
l'espagnol sont des traductions. On modifie ici, puis :  python3 build.py
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
V = "20261119-1249"  # numéro de version des fichiers css/js (mis à jour par maj.sh)
LANGS = ["es", "en", "fr"]          # l'espagnol est la langue par défaut (pages sans suffixe)
DEFAULT = "es"
CUR = {"lang": DEFAULT}


def L(en, fr, es):
    return {"en": en, "fr": fr, "es": es}


def _(x):
    """Texte dans la langue en cours."""
    if isinstance(x, dict) and set(x) == {"en", "fr", "es"}:
        return x[CUR["lang"]]
    return x


def url(slug, lang=None):
    lang = lang or CUR["lang"]
    return f"{slug}.html" if lang == DEFAULT else f"{slug}-{lang}.html"


e = html.escape

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

SLOW_FLOAT = L("Slow floating", "Flottant lent", "Flotante lento")
SUSP = L("Suspending", "Suspending", "Suspending")
SLOW_SINK = L("Slow sinking", "Coulant lent", "Hundimiento lento")
FLOATING = L("Floating", "Flottant", "Flotante")
W_WEIGHT = L("Weight", "Poids", "Peso")
W_LENGTH = L("Length", "Longueur", "Longitud")
W_COLOURS = L("Colours", "Coloris", "Colores")
W_HOOKS = L("Hooks", "Hameçons", "Anzuelos")
W_TREBLES = L("Treble hooks", "Hameçons triples", "Anzuelos triples")

RIG_SHORT = L(
    "Tie your line straight to its solid ring. For a better performance, make sure you don't add any snap or extra ring between the line and the solid ring.",
    "Attachez votre ligne directement sur l'anneau soudé. Pour de meilleures performances, n'ajoutez ni agrafe ni anneau supplémentaire entre la ligne et l'anneau soudé.",
    "Ata el hilo directamente a la anilla sólida. Para un mejor rendimiento, no añadas grapa ni anilla extra entre el hilo y la anilla sólida.")
BALANCED = L(
    "It has been perfectly balanced to adopt a natural position on the stop, but also to perform perfectly under any speed or type of retrieve.",
    "Il a été parfaitement équilibré pour adopter une position naturelle à l'arrêt, tout en nageant parfaitement à toutes les vitesses et avec tous les types de récupération.",
    "Está perfectamente equilibrado para adoptar una posición natural en la parada y nadar a la perfección a cualquier velocidad y con cualquier tipo de recogida.")

GLIDEWAYS = {
    "126": dict(
        pid="5", colors=C126, hero="26", film="glideway-126",
        kicker=L("The little freestyler", "Le petit freestyler", "El pequeño freestyler"),
        lede=L("If you believe that tiny glides should also have action (besides being cute), the Glideway 126 is your bait.",
               "Si vous pensez que les petits glides doivent aussi avoir de l'action (en plus d'être mignons), le Glideway 126 est fait pour vous.",
               "Si crees que los glides pequeños también deben tener acción (además de ser bonitos), el Glideway 126 es tu señuelo."),
        body=[
            L("This small piece of art is a total freestyler like his big brother, but with an even more electric and reactive rhythm while still being very stable.",
              "Ce petit bijou est un vrai freestyler comme son grand frère, avec un rythme encore plus électrique et réactif, tout en restant très stable.",
              "Esta pequeña obra de arte es un freestyler total como su hermano mayor, con un ritmo aún más eléctrico y reactivo sin perder estabilidad."),
            BALANCED,
        ],
        specs=[(W_WEIGHT, "29.5 g"), (L("Version", "Version", "Versión"), FLOATING), (W_TREBLES, "BKK Super Strong 4X #5"),
               ("Lead Stickers", L("Floating to sinking · 1 g", "De flottant à coulant · 1 g", "De flotante a hundimiento · 1 g"))],
        stats=[("29.5", "g", W_WEIGHT), ("26", "", W_COLOURS), ("10–12", "ft", L("Max depth", "Profondeur max", "Profundidad máx."))],
        depth=[SLOW_FLOAT, SUSP, SLOW_SINK],
        depth_text=L(
            "From surface to 10–12 ft, the depth of the Glideway 126 depends on the number of Lead Stickers you stick on the lure cavities. The lure is slow floating by itself; fill the first cavity and it turns into suspending. Fill the second cavity as well and it turns into slow sinking.",
            "De la surface jusqu'à 10–12 ft (environ 3 à 3,5 m), la profondeur du Glideway 126 dépend du nombre de Lead Stickers collés dans les cavités du leurre. Seul, il est flottant lent ; remplissez la première cavité et il devient suspending. Remplissez aussi la seconde et il devient coulant lent.",
            "Desde la superficie hasta 10–12 ft (unos 3–3,5 m), la profundidad del Glideway 126 depende del número de Lead Stickers que pegues en las cavidades. Por sí solo es flotante lento; llena la primera cavidad y pasa a ser suspending. Llena también la segunda y pasa a hundimiento lento."),
        depth_note=None,
        rig=L("Tie your line straight to the solid ring. For a better performance, don't add any snap or extra ring between the line and the solid ring. Finally, cast and enjoy!",
              "Attachez votre ligne directement sur l'anneau soudé. Pour de meilleures performances, n'ajoutez ni agrafe ni anneau supplémentaire entre la ligne et l'anneau soudé. Ensuite, lancez et profitez !",
              "Ata el hilo directamente a la anilla sólida. Para un mejor rendimiento, no añadas grapa ni anilla extra entre el hilo y la anilla sólida. ¡Después, lanza y disfruta!"),
        gear=[(L("Line", "Ligne", "Línea"), L("10 lb braid + 12 lb fluorocarbon leader", "Tresse 10 lb + bas de ligne fluorocarbone 12 lb", "Trenzado 10 lb + bajo de fluorocarbono 12 lb")),
              (L("Reel", "Moulinet", "Carrete"), L("Size 201, any ratio", "Taille 201, tout ratio", "Tamaño 201, cualquier ratio")),
              (L("Rod", "Canne", "Caña"), L("Moderate, 1 oz", "Action moderate, 1 oz", "Acción moderada, 1 oz"))],
        photos=[("photos/glideway-126-branch.webp", "Glideway 126"), ("photos/glideway-126-hand.webp", "Glideway 126")],
    ),
    "176": dict(
        pid="1", colors=C176, hero="1", film="glideway-176",
        kicker=L("The original tank slayer", "Le tank slayer original", "El tank slayer original"),
        lede=L("The ultimate multi-species glide bait — an authentic tank slayer that will help you increase the quantity, and especially the quality, of the bites in your swimbait journeys.",
               "Le glide bait multi-espèces ultime — un vrai tank slayer qui vous aidera à augmenter la quantité, et surtout la qualité, de vos touches en swimbait.",
               "El glide bait multiespecie definitivo: un auténtico tank slayer que te ayudará a aumentar la cantidad, y sobre todo la calidad, de las picadas en tus jornadas de swimbait."),
        body=[
            L("The Glideway 176 has been designed to trigger the bite of those smart big fish, thanks to its realistic slow-moving action.",
              "Le Glideway 176 a été conçu pour déclencher l'attaque des gros poissons méfiants, grâce à son action lente et réaliste.",
              "El Glideway 176 está diseñado para provocar la picada de los peces grandes y desconfiados, gracias a su acción lenta y realista."),
            BALANCED,
        ],
        retrieves=[L("Fast steady", "Rapide régulier", "Rápido constante"), L("Super slow steady", "Ultra lent régulier", "Muy lento constante"),
                   "Side walk", "Twitching", L("Heavy sweeps", "Grands sweeps", "Barridos fuertes")],
        specs=[(W_LENGTH, "176 mm"), (W_WEIGHT, "80 g"), (L("Type", "Type", "Tipo"), FLOATING), (W_HOOKS, L("3X BKK trebles", "Triples BKK 3X", "Triples BKK 3X"))],
        stats=[("176", "mm", W_LENGTH), ("80", "g", W_WEIGHT), ("29", "", W_COLOURS)],
        depth=[SLOW_FLOAT, SUSP, SLOW_SINK],
        depth_text=L(
            "From surface to 10–12 ft, the depth of the Glideway depends on the number of Lead Stickers you stick on the lure cavities. The lure is slow floating by itself; fill the first cavity and it turns into suspending. Fill the second cavity as well and it turns into slow sinking.",
            "De la surface jusqu'à 10–12 ft (environ 3 à 3,5 m), la profondeur du Glideway dépend du nombre de Lead Stickers collés dans les cavités. Seul, il est flottant lent ; remplissez la première cavité et il devient suspending. Remplissez aussi la seconde et il devient coulant lent.",
            "Desde la superficie hasta 10–12 ft (unos 3–3,5 m), la profundidad del Glideway depende del número de Lead Stickers que pegues en las cavidades. Por sí solo es flotante lento; llena la primera cavidad y pasa a ser suspending. Llena también la segunda y pasa a hundimiento lento."),
        depth_note=L(
            "The weights have been adjusted very accurately, so buoyancy also depends on water temperature: the warmer the water, the faster it sinks. The length and diameter of your fluorocarbon leader affect the sinking rate too — the longer and thicker the leader, the more it pushes the lure towards the bottom.",
            "Les poids ont été ajustés très précisément : la flottabilité dépend aussi de la température de l'eau. Plus l'eau est chaude, plus il coule vite. La longueur et le diamètre du bas de ligne fluorocarbone jouent aussi : plus il est long et épais, plus il entraîne le leurre vers le fond.",
            "Los pesos se han ajustado con mucha precisión, así que la flotabilidad depende también de la temperatura del agua: cuanto más caliente, más rápido se hunde. La longitud y el diámetro del bajo de fluorocarbono también influyen: cuanto más largo y grueso, más empuja el señuelo hacia el fondo."),
        rig=RIG_SHORT,
        gear=[],
        photos=[("photos/bass-176.webp", "Black bass caught on a Glideway 176"), ("photos/glideway-sunset.webp", "Glideway 176")],
    ),
    "236": dict(
        pid="8", colors=C236, hero="56", film="glideway-236",
        kicker=L("The big guy has arrived", "Le grand frère est arrivé", "Ha llegado el grande"),
        lede=L("The wait is finally over… The big guy has arrived! This oversized creation is a true freestyler, just like the 176 — the same smooth and natural action, with a much larger profile.",
               "L'attente est enfin terminée… Le grand est arrivé ! Cette création XXL est un vrai freestyler, comme le 176 : la même action douce et naturelle, avec un profil bien plus imposant.",
               "La espera ha terminado… ¡Ha llegado el grande! Esta creación XXL es un auténtico freestyler, como el 176: la misma acción suave y natural, con un perfil mucho más grande."),
        body=[
            L("Exceptionally stable and perfectly balanced, it settles naturally on the pause and performs flawlessly at any speed or retrieve style.",
              "Exceptionnellement stable et parfaitement équilibré, il se pose naturellement à l'arrêt et nage parfaitement à toutes les vitesses et avec tous les styles de récupération.",
              "Excepcionalmente estable y perfectamente equilibrado, se queda natural en la pausa y nada sin fallos a cualquier velocidad y estilo de recogida."),
            L("The key difference between the Glideway 236 and its smaller brothers is its impressive side slide. With the right input, the lure can glide sideways up to around 4 ft, creating a wide and irresistible presentation.",
              "La grande différence avec ses petits frères, c'est son impressionnant glissé latéral : avec la bonne impulsion, il peut glisser sur le côté jusqu'à environ 4 ft (1,2 m), pour une présentation large et irrésistible.",
              "La gran diferencia con sus hermanos pequeños es su impresionante deslizamiento lateral: con el toque adecuado, puede deslizarse de lado hasta unos 4 ft (1,2 m), creando una presentación amplia e irresistible."),
        ],
        specs=[(W_LENGTH, "236 mm"), (W_WEIGHT, "150 g"), (W_TREBLES, "BKK Fangs 3X 1/0"), ("Lead Stickers", "3.75 g")],
        stats=[("236", "mm", W_LENGTH), ("150", "g", W_WEIGHT), ("4", "ft", L("Side slide", "Glissé latéral", "Deslizamiento lateral"))],
        depth=[FLOATING, L("Slow floating / suspending", "Flottant lent / suspending", "Flotante lento / suspending"), SLOW_SINK],
        depth_text=L(
            "Running depth ranges from the surface down to approximately 10–12 ft and can be adjusted using the Lead Stickers placed inside the lure's cavities. Out of the box, the Glideway 236 is floating. Filling the first cavity makes it slow floating or suspending; filling the second turns it into a slow sinking bait.",
            "La profondeur de nage va de la surface à environ 10–12 ft (3 à 3,5 m) et se règle avec les Lead Stickers placés dans les cavités du leurre. Sorti de la boîte, le Glideway 236 est flottant. Remplir la première cavité le rend flottant lent ou suspending ; remplir la seconde en fait un leurre coulant lent.",
            "La profundidad de nado va desde la superficie hasta unos 10–12 ft (3–3,5 m) y se ajusta con los Lead Stickers colocados en las cavidades del señuelo. De serie, el Glideway 236 es flotante. Llenar la primera cavidad lo vuelve flotante lento o suspending; llenar la segunda lo convierte en un señuelo de hundimiento lento."),
        depth_note=L(
            "Buoyancy may vary slightly depending on water temperature and the material or thickness of your fishing line.",
            "La flottabilité peut légèrement varier selon la température de l'eau et la matière ou l'épaisseur de votre ligne.",
            "La flotabilidad puede variar ligeramente según la temperatura del agua y el material o grosor de tu línea."),
        rig=L("For optimal performance, tie your line directly to the solid ring. Avoid snaps or additional split rings between the line and the solid ring. Finally, cast and enjoy!",
              "Pour des performances optimales, attachez la ligne directement sur l'anneau soudé. Évitez agrafes et anneaux brisés supplémentaires entre la ligne et l'anneau. Ensuite, lancez et profitez !",
              "Para un rendimiento óptimo, ata el hilo directamente a la anilla sólida. Evita grapas o anillas abiertas adicionales entre el hilo y la anilla sólida. ¡Después, lanza y disfruta!"),
        gear=[],
        photos=[("photos/glideway-236-top.webp", "Glideway 236"), ("photos/glideway-236-hand.webp", "Glideway 236")],
    ),
}
ORDER = ["126", "176", "236"]

COUNTRY = {
    "US": L("United States", "États-Unis", "Estados Unidos"), "FR": L("France", "France", "Francia"),
    "CH": L("Switzerland", "Suisse", "Suiza"), "BE": L("Belgium", "Belgique", "Bélgica"),
    "ES": L("Spain", "Espagne", "España"), "PT": L("Portugal", "Portugal", "Portugal"),
    "JP": L("Japan", "Japon", "Japón"), "CN": L("China", "Chine", "China"), "DE": L("Germany", "Allemagne", "Alemania"),
    "IT": L("Italy", "Italie", "Italia"), "MX": L("Mexico", "Mexique", "México"), "SG": L("Singapore", "Singapour", "Singapur"),
}
DEALERS = [
    ("US", "Optimum Baits", "info@optimumbaits.com", "https://www.optimumbaits.com/"),
    ("FR", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("CH", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("BE", "Babylon Fishing", "info@babylon.fishing", "https://www.babylon.fishing/"),
    ("ES", "Bocarde S.L.", "info@bocarde.com", "http://www.bocarde.com/"),
    ("PT", "Bocarde S.L.", "info@bocarde.com", "http://www.bocarde.com/"),
]
DIRECT = ["JP", "CN", "DE", "IT", "MX", "SG"]

# textes d'interface communs
U = dict(
    swimbaits="Swimbaits",
    accessories=L("Accessories", "Accessoires", "Accesorios"),
    rods=L("Rods", "Cannes", "Cañas"),
    apparel=L("Apparel", "Textile", "Ropa"),
    about=L("About", "À propos", "Nosotros"),
    dealers=L("Dealers", "Revendeurs", "Distribuidores"),
    contact=L("Contact", "Contact", "Contacto"),
    tagline=L("Garage designed & worldwide tested", "Conçu au garage, testé dans le monde entier", "Diseñado en el garaje, probado en todo el mundo"),
    discover=L("Discover", "Découvrir", "Descubrir"),
    colours_n=L("{n} colours", "{n} coloris", "{n} colores"),
    watch=L("Watch the film", "Voir le film", "Ver el vídeo"),
    find_dealer=L("Find a dealer", "Trouver un revendeur", "Encontrar distribuidor"),
    where_buy=L("Where to buy", "Où acheter", "Dónde comprar"),
    specs=L("Specifications", "Caractéristiques", "Especificaciones"),
    chart=L("Colour chart", "Nuancier", "Carta de colores"),
    chart_hint=L("Click a colour to see it in large.", "Cliquez sur un coloris pour l'agrandir.", "Haz clic en un color para verlo en grande."),
    depth_eyebrow=L("Lead Stickers · buoyancy", "Lead Stickers · flottabilité", "Lead Stickers · flotabilidad"),
    depth_h=L("Depth control", "Réglage de la profondeur", "Control de profundidad"),
    cav=[L("No sticker", "Sans sticker", "Sin sticker"), L("1st cavity", "1re cavité", "1.ª cavidad"), L("2nd cavity", "2e cavité", "2.ª cavidad")],
    rig=L("Rigging tip", "Conseil de montage", "Consejo de montaje"),
    gear=L("Recommended gear", "Matériel conseillé", "Equipo recomendado"),
    menu_open=L("Open menu", "Ouvrir le menu", "Abrir menú"),
    skip=L("Skip to content", "Aller au contenu", "Ir al contenido"),
    products=L("Products", "Produits", "Productos"),
    legal=L("Legal", "Légal", "Legal"),
    privacy=L("Privacy policy", "Confidentialité", "Privacidad"),
    cookies=L("Cookie policy", "Cookies", "Cookies"),
    notice=L("Legal notice", "Mentions légales", "Aviso legal"),
    about_us=L("About us", "À propos", "Sobre nosotros"),
    locate=L("Locate a dealer", "Trouver un revendeur", "Encontrar distribuidor"),
    contact_us=L("Contact us", "Nous contacter", "Contáctanos"),
    no_lure=L("If you're looking for jerkbaits, jigs, worms, crankbaits… you're in the wrong place. This is all about swimbaits.",
              "Si vous cherchez des jerkbaits, des jigs, des vers ou des crankbaits… vous n'êtes pas au bon endroit. Ici, tout tourne autour du swimbait.",
              "Si buscas jerkbaits, jigs, vinilos o crankbaits… estás en el sitio equivocado. Aquí todo va de swimbaits."),
)

CATS = [
    ("swimbaits", U["swimbaits"], "Glideway 126 · 176 · 236", "img/photos/glideway-sunset.webp", "img/brand/cat-glideway.webp"),
    ("accessories", U["accessories"], "Spare Tails · Lead Stickers", "img/photos/spare-tail-2.webp", "img/brand/cat-sinkers.webp"),
    ("sneak-attack-711", U["rods"], "Sneak Attack 711", "img/photos/rod-hero.webp", "img/brand/cat-rods.webp"),
    ("apparel", U["apparel"], "Flat Cap", "img/photos/flat-cap.webp", "img/brand/cat-apparel.webp"),
]

# ---------------------------------------------------------------- HELPERS


def color_img(pid, cid):
    return f"img/colors/{pid}/{cid}.webp"


ICONS = {
    "ig": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>',
    "tt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M14 3c.4 2.6 2.3 4.6 5 4.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 21v-7.5h2.6l.4-3h-3V8.7c0-.9.3-1.5 1.6-1.5h1.5V4.5c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.3H9.2v3h2.5V21" fill="currentColor"/></svg>',
    "sp": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.5 9.5c3-1 6.5-.7 9 .8M8 12.6c2.5-.7 5.2-.4 7.3.8M8.6 15.4c2-.5 4-.3 5.6.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg>',
    "left": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
    "right": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
    "play": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',
}


def btn(href, label, cls="btn"):
    return f'<a class="{cls}" href="{href}"><span>{_(label)}</span>{ICONS["arrow"]}</a>'


def socials(cls="social"):
    return f'<ul class="{cls}">' + "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{ICONS[k]}</a></li>' for n, u, k in SOCIAL
    ) + "</ul>"


def NAV():
    return [("swimbaits", U["swimbaits"], "swimbaits"), ("accessories", U["accessories"], "accessories"),
            ("sneak-attack-711", U["rods"], "rods"), ("apparel", U["apparel"], "apparel"),
            ("about", U["about"], "about"), ("dealers", U["dealers"], "dealers")]


def layout(slug, title, desc, body, section=""):
    lang = CUR["lang"]
    nav = "".join(f'<li><a href="{url(h)}"{" aria-current=page" if section == s else ""}>{_(l)}</a></li>' for h, l, s in NAV())
    mobile_nav = "".join(f'<li><a href="{url(h)}"><small>0{i+1}</small>{_(l)}</a></li>'
                         for i, (h, l, s) in enumerate(NAV() + [("contact", U["contact"], "contact")]))
    langs = "".join(
        f'<a href="{url(slug, l)}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(slug, l)}">' for l in LANGS)
    t = e(_(title))
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{e(_(desc))}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{e(_(desc))}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Swimbait Republic">
<meta property="og:image" content="img/posters/hero.webp">
<meta name="theme-color" content="#3e4939">
{alt}
<link rel="icon" type="image/png" href="img/brand/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=Barlow:wght@400;500;600;700&family=Black+Ops+One&display=swap">
<link rel="stylesheet" href="css/style.css?v={V}">
<script>if('scrollRestoration' in history)history.scrollRestoration='manual';if(location.hash)history.replaceState(null,'',location.pathname+location.search);window.scrollTo(0,0);document.documentElement.classList.add('js');setTimeout(function(){{var c=document.querySelector('.curtain');if(c&&!c.classList.contains('is-in'))c.classList.add('is-out')}},2500);</script>
</head>
<body class="page-{slug}">
<a class="skip" href="#main">{_(U['skip'])}</a>
<div class="progress" aria-hidden="true"><span></span></div>
<div class="curtain" aria-hidden="true"><img src="img/brand/logo.png" alt=""></div>

<header class="nav" id="nav">
  <a class="nav-logo" href="{url('index')}" aria-label="Swimbait Republic"><img src="img/brand/logo.png" alt="Swimbait Republic" width="166" height="41"></a>
  <nav aria-label="Main"><ul class="nav-links">{nav}</ul></nav>
  <div class="lang" aria-label="Language">{langs}</div>
  <a class="nav-cta" href="{url('contact')}">{_(U['contact'])}</a>
  <button class="burger" aria-label="{_(U['menu_open'])}" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
</header>
<div class="menu" id="menu" hidden>
  <ul>{mobile_nav}</ul>
  <div class="lang lang-menu">{langs}</div>
  {socials("social menu-social")}
</div>

<main id="main">
{body}
</main>

<footer class="footer">
  <div class="footer-top">
    <div class="footer-cta">
      <img class="footer-logo" src="img/brand/logo.png" alt="Swimbait Republic" width="166" height="41" loading="lazy">
      {socials()}
      <p class="footer-handle">@swimbait_republic</p>
    </div>
    <div class="footer-cols">
      <div><p class="footer-h">{_(U['products'])}</p>
        <a href="{url('glideway-126')}">Glideway 126</a><a href="{url('glideway-176')}">Glideway 176</a><a href="{url('glideway-236')}">Glideway 236</a>
        <a href="{url('accessories')}">Spare Tails &amp; Lead Stickers</a><a href="{url('sneak-attack-711')}">Sneak Attack 711</a><a href="{url('apparel')}">Flat Cap</a></div>
      <div><p class="footer-h">Republic</p>
        <a href="{url('about')}">{_(U['about_us'])}</a><a href="{url('dealers')}">{_(U['locate'])}</a><a href="{url('contact')}">{_(U['contact_us'])}</a></div>
      <div><p class="footer-h">{_(U['legal'])}</p>
        <a href="https://www.swimbaitrepublic.com/privacy-policy">{_(U['privacy'])}</a><a href="https://www.swimbaitrepublic.com/cookie-policy">{_(U['cookies'])}</a><a href="https://www.swimbaitrepublic.com/terms-and-conditions">{_(U['notice'])}</a></div>
    </div>
  </div>
  <div class="footer-bottom"><span>© Swimbait Republic</span><span>{_(U['tagline'])}</span><span class="ver" id="ver">{V}</span></div>
</footer>

<div class="mprev" data-mprev hidden>
  <button class="mprev-btn" type="button" aria-expanded="false" aria-controls="mprev-panel" data-tip="{_(L('Mobile view', 'Vue mobile', 'Vista móvil'))}">
    <svg class="mprev-ico-phone" viewBox="0 0 24 24" aria-hidden="true"><rect x="6.5" y="2.5" width="11" height="19" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10.5 18.5h3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
    <svg class="mprev-ico-x" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="mprev-open">{_(L('Mobile view', 'Vue mobile', 'Vista móvil'))}</span><span class="mprev-close">{_(L('Close', 'Fermer', 'Cerrar'))}</span>
  </button>
  <div class="mprev-panel" id="mprev-panel" role="dialog" aria-label="{_(L('Mobile view', 'Vue mobile', 'Vista móvil'))}">
    <div class="mprev-phone"><div class="mprev-notch"></div><iframe title="{_(L('Mobile view', 'Vue mobile', 'Vista móvil'))}" loading="lazy"></iframe></div>
    <p class="mprev-hint">{_(L('Scroll inside the phone', 'Faites défiler dans le téléphone', 'Desliza dentro del móvil'))}</p>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="js/app.js?v={V}" defer></script>
</body>
</html>
"""


def page_hero(kicker, title, lede, img):
    return f"""
<section class="phero">
  <div class="phero-media" data-parallax><img src="{img}" alt="" fetchpriority="high"></div>
  <div class="phero-inner wrap">
    <p class="eyebrow" data-reveal>{_(kicker)}</p>
    <h1 class="display" data-split>{_(title)}</h1>
    <p class="lede" data-reveal>{_(lede)}</p>
  </div>
</section>"""


def depth_box(g):
    """Le bac d'eau + les 3 boutons Lead Stickers (vraies photos du leurre)."""
    btns = "".join(
        f'<button class="depth-btn{" is-on" if i == 0 else ""}" data-depth="{i}" aria-pressed="{"true" if i == 0 else "false"}">'
        f'<span class="depth-n">{i}</span><span>{_(U["cav"][i])}</span><strong>{_(s)}</strong></button>'
        for i, s in enumerate(g["depth"]))
    return f"""
      <div class="depth-box" data-depth-module>
        <div class="depth-tank" aria-hidden="true">
          <div class="depth-surface"></div>
          <ol class="depth-ruler"><li>0 ft</li><li>3</li><li>6</li><li>9</li><li>12 ft</li></ol>
          <div class="depth-lure" data-state="0"><img src="{color_img(g['pid'], g['hero'])}" alt=""><span class="depth-tag">{_(g['depth'][0])}</span></div>
          <div class="depth-bubbles"><i></i><i></i><i></i><i></i><i></i></div>
        </div>
        <div class="depth-btns" role="group" aria-label="Lead Stickers">{btns}</div>
      </div>"""


def depth_section(g):
    note = f'<p class="note">{_(g["depth_note"])}</p>' if g["depth_note"] else ""
    return f"""
<section class="depth">
  <div class="wrap depth-grid">
    <div class="depth-copy">
      <p class="eyebrow">{_(U['depth_eyebrow'])}</p>
      <h2 class="h2">{_(U['depth_h'])}</h2>
      <p>{_(g['depth_text'])}</p>
      {note}
    </div>
    {depth_box(g)}
  </div>
</section>"""


def color_chart(pid, colors, name, start):
    sname = dict(colors)[start]
    items = "".join(
        f'<li><button class="swatch{" is-on" if cid == start else ""}" data-src="{color_img(pid, cid)}" data-name="{e(n)}" aria-pressed="{"true" if cid == start else "false"}">'
        f'<img src="{color_img(pid, cid)}" alt="" loading="lazy"><span>{e(n)}</span></button></li>'
        for cid, n in colors)
    return f"""
<section class="chart" id="colours">
  <div class="wrap">
    <div class="chart-head">
      <div><p class="eyebrow">{_(U['colours_n']).format(n=len(colors))}</p><h2 class="h2">{_(U['chart'])}</h2></div>
      <p class="chart-hint">{_(U['chart_hint'])}</p>
    </div>
    <div class="viewer">
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
    <button class="film-play" aria-label="{_(U['watch'])}: {e(title)}"><span class="film-btn">{ICONS["play"]}</span><span class="film-label"><small>{_(U['watch'])}</small>{e(title)}</span></button>
  </div>
</section>"""


def stats(items):
    return '<dl class="stats">' + "".join(
        f'<div data-reveal><dt>{_(l)}</dt><dd><span data-count="{n}">{n}</span><em>{u}</em></dd></div>' for n, u, l in items) + "</dl>"


def spec_list(specs, cls, reveal=False):
    r = " data-reveal" if reveal else ""
    return f'<dl class="{cls}">' + "".join(f"<div{r}><dt>{_(a)}</dt><dd>{_(b)}</dd></div>" for a, b in specs) + "</dl>"


# ---------------------------------------------------------------- PAGES


def home():
    # products bar on the video
    hero_cats = "".join(
        f'<a class="hcat" href="{url(slug)}"><img src="{draw}" alt="" loading="lazy"><span><b>{_(name)}</b><small>{sub}</small></span>{ICONS["arrow"]}</a>'
        for slug, name, sub, photo, draw in CATS)

    # range: tabs (lures to scale) + one panel per size with the depth tank
    tabs, panels = "", ""
    for i, k in enumerate(ORDER):
        g = GLIDEWAYS[k]
        on = k == "176"
        weight = _(dict((_(a), b) for a, b in g["specs"])[_(W_WEIGHT)])
        tabs += f"""
        <button class="rtab{' is-on' if on else ''}" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{'true' if on else 'false'}" data-k="{k}" style="--k:{int(k)/236:.3f}">
          <span class="rtab-img"><img src="{color_img(g['pid'], g['hero'])}" alt=""></span>
          <span class="rtab-radio" aria-hidden="true"></span>
          <b>Glideway {k}</b><small>{weight} · {_(U['colours_n']).format(n=len(g['colors']))}</small>
          <span class="rtab-pick" aria-hidden="true"><span class="rtab-choose">{_(L('Choose', 'Choisir', 'Elegir'))} →</span><span class="rtab-chosen">✓ {_(L('Selected', 'Sélectionné', 'Seleccionado'))}</span></span>
        </button>"""
        panels += f"""
      <div class="rpanel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}" data-k="{k}"{'' if on else ' hidden'}>
        <div class="rpanel-info">
          <p class="eyebrow">{_(g['kicker'])}</p>
          <h3 class="stencil">Glideway {k}</h3>
          <p>{_(g['lede'])}</p>
          {spec_list(g['specs'], 'mini-specs')}
          {btn(url(f'glideway-{k}'), L(f'Discover the Glideway {k}', f'Voir le Glideway {k}', f'Ver el Glideway {k}'))}
        </div>
        <div class="rpanel-depth">
          <p class="rstep"><span>2</span>{_(L('Add Lead Stickers and watch it sink', 'Ajoutez des Lead Stickers et regardez-le couler', 'Añade Lead Stickers y mira cómo se hunde'))}</p>
          {depth_box(g)}
        </div>
      </div>"""

    # colours carousel data (all models)
    cdata = {k: [[color_img(GLIDEWAYS[k]["pid"], c), n] for c, n in GLIDEWAYS[k]["colors"]] for k in ORDER}
    ctabs = "".join(f'<button class="ctab{" is-on" if k == "176" else ""}" data-model="{k}" aria-pressed="{"true" if k == "176" else "false"}">Glideway {k}</button>' for k in ORDER)

    cards = "".join(f"""
      <a class="pcard" href="{url(slug)}" data-reveal>
        <img src="{photo}" alt="" loading="lazy">
        <span class="pcard-in"><small>0{i+1}</small><b>{_(name)}</b><em>{sub}</em><span class="pcard-go">{_(U['discover'])} {ICONS['arrow']}</span></span>
      </a>""" for i, (slug, name, sub, photo, draw) in enumerate(CATS))

    countries = ", ".join(_(COUNTRY[c]) for c, *_x in DEALERS)
    body = f"""
<section class="hero" data-hero>
  <div class="hero-media">
    <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="img/posters/hero.webp"><source src="media/hero-loop.mp4" type="video/mp4"></video>
  </div>
  <div class="hero-shade" aria-hidden="true"></div>
  <div class="hero-inner wrap">
    <p class="eyebrow hero-eyebrow">{_(U['tagline'])}</p>
    <h1 class="hero-title" data-split>{_(L('Swimbait Republic official website', 'Site officiel Swimbait Republic', 'Web oficial de Swimbait Republic'))}</h1>
    <p class="lede">{_(L('Glide baits made to increase the quantity — and especially the quality — of your bites.', 'Des glide baits pensés pour augmenter la quantité — et surtout la qualité — de vos touches.', 'Glide baits creados para aumentar la cantidad — y sobre todo la calidad — de tus picadas.'))}</p>
    <div class="hero-ctas">{btn('#range', L('Discover the Glideway', 'Découvrir le Glideway', 'Descubrir el Glideway'))}{btn('#film', U['watch'], 'btn btn-ghost')}</div>
    <nav class="hero-cats" aria-label="{_(U['products'])}">{hero_cats}</nav>
  </div>
</section>

<section class="range" id="range" data-range>
  <div class="rider" aria-hidden="true"><img src="{color_img('1', '2')}" alt=""></div>
  <div class="wrap">
    <div class="sec-head sec-head-row">
      <h2 class="h2">{_(L('The Glideway range', 'La gamme Glideway', 'La gama Glideway'))}</h2>
      <p>{_(L('Choose a size, then add Lead Stickers to see how it sits in the water.', 'Choisissez une taille, puis ajoutez des Lead Stickers pour voir comment il se place dans l’eau.', 'Elige un tamaño y añade Lead Stickers para ver cómo se coloca en el agua.'))}</p>
    </div>
    <p class="rstep"><span>1</span>{_(L('Choose your size — click a Glideway', 'Choisissez votre taille — cliquez sur un Glideway', 'Elige tu tamaño — haz clic en un Glideway'))}</p>
    <div class="rtabs" role="tablist" aria-label="Glideway">{tabs}
    </div>
    {panels}
  </div>
</section>

<section class="colours" data-colours>
  <script type="application/json" class="colours-data">{json.dumps(cdata)}</script>
  <div class="wrap">
    <div class="sec-head sec-head-row">
      <h2 class="h2">{_(W_COLOURS)}</h2>
      <div class="ctabs">{ctabs}</div>
    </div>
    <div class="cv-stage">
      <span class="cv-ghost" aria-hidden="true"></span>
      <img class="cv-img" src="{color_img('1', '1')}" alt="">
      <div class="cv-meta"><span class="cv-model">Glideway 176</span><strong class="cv-name">Bone Soldier</strong><span class="cv-count"></span></div>
      <a class="cv-link" href="{url('glideway-176')}#colours">{_(U['chart'])} {ICONS['arrow']}</a>
    </div>
    <div class="cv-rail">
      <button class="cv-arrow cv-prev" aria-label="Previous">{ICONS['left']}</button>
      <div class="cv-strip" tabindex="0"></div>
      <button class="cv-arrow cv-next" aria-label="Next">{ICONS['right']}</button>
    </div>
  </div>
</section>

<section class="pcards-sec">
  <div class="wrap">
    <div class="sec-head sec-head-row">
      <h2 class="h2">{_(L('Our products', 'Nos produits', 'Nuestros productos'))}</h2>
      <p>{_(U['no_lure'])}</p>
    </div>
    <div class="pcards">{cards}
    </div>
  </div>
</section>

<div id="film">{film("glideway-236", "glideway-236", "Glideway 236")}</div>

<section class="dealers-band">
  <div class="wrap dealers-band-in">
    <p><strong>{_(L('Dealers in 6 countries', 'Revendeurs dans 6 pays', 'Distribuidores en 6 países'))}</strong> — {countries} — {_(L('and direct to tackle shops in 6 more.', 'et en direct avec les magasins dans 6 autres.', 'y directo a tiendas en otros 6.'))}</p>
    {btn(url('dealers'), U['find_dealer'])}
  </div>
</section>
"""
    return layout("index", L("Swimbait Republic official website", "Site officiel Swimbait Republic", "Web oficial de Swimbait Republic"),
                  L("Glideway 126, 176 and 236: glide baits garage designed and worldwide tested.", "Glideway 126, 176 et 236 : des glide baits conçus au garage et testés dans le monde entier.", "Glideway 126, 176 y 236: glide baits diseñados en el garaje y probados en todo el mundo."), body)


def swimbaits():
    rows = ""
    for i, k in enumerate(ORDER):
        g = GLIDEWAYS[k]
        dots = "".join(f'<img src="{color_img(g["pid"], c)}" alt="" loading="lazy">' for c, _x in g["colors"][:6])
        rows += f"""
  <article class="prow{' prow-rev' if i % 2 else ''}">
    <a class="prow-visual" href="{url(f'glideway-{k}')}" aria-label="Glideway {k}"><img src="{color_img(g['pid'], g['hero'])}" alt="Glideway {k}" data-float></a>
    <div class="prow-copy">
      <p class="eyebrow">{_(g['kicker'])}</p>
      <h2 class="stencil" data-split>Glideway {k}</h2>
      <p>{_(g['lede'])}</p>
      {spec_list(g['specs'], 'mini-specs')}
      <div class="prow-colors"><span class="mono">{_(U['colours_n']).format(n=len(g['colors']))}</span><div>{dots}</div></div>
      {btn(url(f'glideway-{k}'), L(f'Discover the {k}', f'Découvrir le {k}', f'Descubrir el {k}'))}
    </div>
  </article>"""
    comp = [
        (W_LENGTH, ["—", "176 mm", "236 mm"]),
        (W_WEIGHT, ["29.5 g", "80 g", "150 g"]),
        (W_HOOKS, ["BKK Super Strong 4X #5", "3X BKK", "BKK Fangs 3X 1/0"]),
        (L("Out of the box", "Sorti de la boîte", "De serie"), [SLOW_FLOAT, SLOW_FLOAT, FLOATING]),
        (L("Depth range", "Profondeur", "Profundidad"), ["0 – 10/12 ft"] * 3),
        (W_COLOURS, [str(len(GLIDEWAYS[k]["colors"])) for k in ORDER]),
    ]
    table = "".join(f"<tr><th scope='row'>{_(a)}</th>{''.join(f'<td>{_(x)}</td>' for x in v)}</tr>" for a, v in comp)
    body = page_hero(L("Category 01 · Swimbaits", "Catégorie 01 · Swimbaits", "Categoría 01 · Swimbaits"), "Swimbaits", U["no_lure"], "img/photos/glideway-sunset.webp") + f"""
<section class="products wrap">{rows}
</section>
<section class="compare wrap">
  <h2 class="h2">{_(L('Compare', 'Comparer', 'Comparar'))}</h2>
  <div class="table-scroll"><table>
    <thead><tr><th></th>{''.join(f'<th scope="col"><a href="{url(f"glideway-{k}")}">Glideway {k}</a></th>' for k in ORDER)}</tr></thead>
    <tbody>{table}</tbody></table></div>
</section>
"""
    return layout("swimbaits", L("Swimbaits — Glideway 126, 176 & 236 | Swimbait Republic", "Swimbaits — Glideway 126, 176 et 236 | Swimbait Republic", "Swimbaits — Glideway 126, 176 y 236 | Swimbait Republic"),
                  L("The Glideway family: glide baits in 126, 176 and 236 sizes.", "La gamme Glideway : des glide baits en 126, 176 et 236.", "La gama Glideway: glide baits en 126, 176 y 236."), body, "swimbaits")


# vues du leurre sous 6 angles : une photo déposée dans img/views/<taille>/<vue>.webp apparaît toute seule
VIEWS = [
    ("profil", L("Side", "Profil", "Perfil")),
    ("face", L("Front", "Face", "Frente")),
    ("autre-cote", L("Other side", "Autre côté", "Otro lado")),
    ("dessus", L("Top", "Dessus", "Arriba")),
    ("dessous", L("Bottom", "Dessous", "Abajo")),
    ("arriere", L("Back", "Arrière", "Atrás")),
]
CAMERA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h3l1.5-2h7L17 8h3v11H4z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="13" r="3.4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'


def views_block(k, g, name):
    stages, tabs = "", ""
    for i, (key, label) in enumerate(VIEWS):
        own = f"img/views/{k}/{key}.webp"
        if key == "profil":
            src = color_img(g["pid"], g["hero"])
        elif os.path.exists(os.path.join(ROOT, own)):
            src = own
        else:
            src = None
        if key == "profil":
            inner = f'<div class="pd-lure"><img src="{src}" alt="{name} — {_(label)}" fetchpriority="high"></div>'
        elif src:
            inner = f'<img class="view-img" src="{src}" alt="{name} — {_(label)}" loading="lazy">'
        else:
            inner = (f'<div class="view-empty">{CAMERA}<b>{_(label)}</b>'
                     f'<span>{_(L("Photo coming soon", "Photo à venir", "Foto próximamente"))}</span></div>')
        stages += f'<div class="view" role="tabpanel" id="view-{key}" data-view="{key}"{"" if i == 0 else " hidden"}>{inner}</div>'
        thumb = f'<img src="{src}" alt="">' if src else CAMERA
        tabs += (f'<button class="vtab{" is-on" if i == 0 else ""}{"" if src else " vtab-empty"}" role="tab" aria-controls="view-{key}" '
                 f'aria-selected="{"true" if i == 0 else "false"}" data-view="{key}"><span class="vtab-thumb">{thumb}</span>{_(label)}</button>')
    return f"""
    <div class="views" data-views>
      <div class="views-stage">{stages}</div>
      <div class="views-tabs" role="tablist" aria-label="{_(L('Views', 'Vues', 'Vistas'))}">{tabs}</div>
    </div>"""


def glideway(k):
    g = GLIDEWAYS[k]
    name = f"Glideway {k}"
    i = ORDER.index(k)
    prev_k, next_k = ORDER[i - 1] if i > 0 else None, ORDER[i + 1] if i < 2 else None
    body_p = "".join(f"<p>{_(p)}</p>" for p in g["body"])
    retr = ""
    if g.get("retrieves"):
        retr = '<ul class="chips">' + "".join(f"<li>{_(r)}</li>" for r in g["retrieves"]) + "</ul>"
    gear = ""
    if g["gear"]:
        gear = f'<div class="gear-rec"><p class="eyebrow">{_(U["gear"])}</p>{spec_list(g["gear"], "")}</div>'
    p1, p2 = g["photos"]
    nav = ""
    for kk, lab in ((prev_k, L("Smaller brother", "Petit frère", "Hermano pequeño")), (next_k, L("Bigger brother", "Grand frère", "Hermano mayor"))):
        if kk:
            gg = GLIDEWAYS[kk]
            nav += f'<a class="pnav-item" href="{url(f"glideway-{kk}")}"><small>{_(lab)}</small><strong>Glideway {kk}</strong><img src="{color_img(gg["pid"], gg["hero"])}" alt="" loading="lazy"></a>'
    body = f"""
<section class="pd-hero">
  <div class="wrap pd-hero-inner">
    <a class="crumb" href="{url('swimbaits')}">← Swimbaits</a>
    <p class="eyebrow">{_(g['kicker'])}</p>
    <h1 class="stencil pd-title" data-split>{name}</h1>
    {views_block(k, g, name)}
    <div class="pd-hero-foot">
      <p class="pd-tag">{_(U['tagline'])}</p>
      <div class="hero-ctas">{btn('#colours', U['chart'])}{btn(url('dealers'), U['where_buy'], 'btn btn-ghost')}</div>
    </div>
  </div>
</section>

<section class="pd-intro">
  <div class="wrap pd-intro-grid">
    <p class="pd-lede">{_(g['lede'])}</p>
    <div class="pd-body">{body_p}{retr}</div>
  </div>
  <div class="wrap">{stats(g['stats'])}</div>
</section>

<section class="pd-photos wrap">
  <figure class="ph-big"><div class="ph-clip"><img src="img/{p1[0]}" alt="{e(p1[1])}" loading="lazy" data-parallax-img></div></figure>
  <figure class="ph-small"><div class="ph-clip"><img src="img/{p2[0]}" alt="{e(p2[1])}" loading="lazy" data-parallax-img></div></figure>
</section>

{depth_section(g)}

<section class="specs wrap">
  <h2 class="h2">{_(U['specs'])}</h2>
  {spec_list(g['specs'], 'spec-sheet')}
  <div class="rig"><p class="eyebrow">{_(U['rig'])}</p><p>{_(g['rig'])}</p></div>
  {gear}
</section>

{film(g['film'], g['film'], name)}

{color_chart(g['pid'], g['colors'], name, g['hero'])}

<section class="upsell wrap">
  <a class="upsell-card" href="{url('accessories')}">
    <img src="img/photos/lead-stickers-2.webp" alt="" loading="lazy">
    <div><p class="eyebrow">{_(L('Make it yours', 'Personnalisez-le', 'Hazlo tuyo'))}</p><h3>Spare Tails &amp; Lead Stickers</h3><p>{_(L('Change the colour of the tail, change the depth of the dive.', 'Changez la couleur de la queue, changez la profondeur de nage.', 'Cambia el color de la cola, cambia la profundidad de nado.'))}</p>{ICONS['arrow']}</div>
  </a>
</section>

<nav class="pnav wrap" aria-label="Glideway">{nav}</nav>
"""
    return layout(f"glideway-{k}", f"{name} — {_(g['kicker'])} | Swimbait Republic", g["lede"], body, "swimbaits")


def accessories():
    tails = "".join(
        f'<li><button class="swatch swatch-tail" data-src="{color_img("3", c)}" data-name="{e(n)}" aria-pressed="false"><img src="{color_img("3", c)}" alt="" loading="lazy"><span>{e(n)}</span></button></li>'
        for c, n in TAILS)
    whens = [
        (L("Suspend or sink", "Suspendre ou couler", "Suspender o hundir"),
         L("When you want the Glideway to suspend or to sink — it's a floating bait by itself.", "Quand vous voulez que le Glideway soit suspending ou coulant : seul, c'est un leurre flottant.", "Cuando quieres que el Glideway quede suspendido o se hunda: por sí solo es un señuelo flotante.")),
        (L("Heavy wind", "Vent fort", "Viento fuerte"),
         L("When it's very windy: the wind pushes the line and tends to bring the lure up.", "Quand il y a beaucoup de vent : le vent pousse la ligne et a tendance à faire remonter le leurre.", "Cuando hace mucho viento: el viento empuja el hilo y tiende a subir el señuelo.")),
        (L("High banks", "Postes en hauteur", "Orillas altas"),
         L("When fishing from a cliff or any structure high above the water, because you're pulling the bait towards the surface.", "Quand vous pêchez depuis une falaise ou un poste en hauteur, car vous tirez le leurre vers la surface.", "Cuando pescas desde un acantilado o una estructura alta, porque tiras del señuelo hacia la superficie.")),
        (L("Cold water", "Eau froide", "Agua fría"),
         L("When the water gets cold, to compensate the extra buoyancy — any lure floats more in cold water, which is denser than warm water.", "Quand l'eau se refroidit, pour compenser la flottabilité en plus : tout leurre flotte davantage en eau froide, plus dense que l'eau chaude.", "Cuando el agua se enfría, para compensar la flotabilidad extra: cualquier señuelo flota más en agua fría, que es más densa que la caliente.")),
        (L("Max distance", "Distance max", "Máxima distancia"),
         L("When you need maximum casting distance. Yes, even 3 extra grams will help you cast longer!", "Quand vous avez besoin de lancer le plus loin possible. Oui, même 3 grammes de plus vous aideront à lancer plus loin !", "Cuando necesitas la máxima distancia de lance. Sí, ¡incluso 3 gramos extra te ayudarán a lanzar más lejos!")),
    ]
    wl = "".join(f'<li data-reveal><span class="when-n">0{i+1}</span><h3>{_(h)}</h3><p>{_(p)}</p></li>' for i, (h, p) in enumerate(whens))
    body = page_hero(L("Category 02 · Accessories", "Catégorie 02 · Accessoires", "Categoría 02 · Accesorios"), U["accessories"],
                     L("As the nerd anglers we are, we love to customise our swimbaits! Sinkers, Spare Tails and many others coming.",
                       "Pêcheurs passionnés jusqu'au bout, on adore personnaliser nos swimbaits ! Plombs, queues de rechange et bien d'autres à venir.",
                       "Como buenos frikis de la pesca, ¡nos encanta personalizar nuestros swimbaits! Plomos, colas de repuesto y muchos más en camino."),
                     "img/photos/glideway-glow.webp") + f"""
<section class="acc wrap">
  <div class="acc-grid">
    <div class="acc-copy">
      <p class="eyebrow">{_(L('Accessory 01', 'Accessoire 01', 'Accesorio 01'))}</p>
      <h2 class="stencil" data-split>Spare Tail</h2>
      <p>{_(L("One more accessory to customise the look of your Glideway with a special colour touch. Some days, little details really make the difference — and this can be one of them.", "Un accessoire de plus pour personnaliser le look de votre Glideway avec une touche de couleur. Certains jours, les petits détails font vraiment la différence — et celui-ci peut en faire partie.", "Un accesorio más para personalizar el aspecto de tu Glideway con un toque de color. Algunos días los pequeños detalles marcan la diferencia, y este puede ser uno de ellos."))}</p>
      <p>{_(L("Our tails are made of tough silicone: hard to deform and highly resistant to toothy fish.", "Nos queues sont en silicone résistant : difficiles à déformer et très résistantes aux poissons à dents.", "Nuestras colas son de silicona resistente: difíciles de deformar y muy resistentes a los peces con dientes."))}</p>
      <p class="note">{_(L("Tip: remove the tail from the Glideway before storing it back in your tackle box, to avoid any possible deformation.", "Conseil : retirez la queue du Glideway avant de le ranger dans votre boîte, pour éviter toute déformation.", "Consejo: quita la cola del Glideway antes de guardarlo en la caja para evitar cualquier deformación."))}</p>
    </div>
    <div class="tail-viewer viewer">
      <div class="viewer-stage"><img class="viewer-img" src="{color_img('3', TAILS[1][0])}" alt="Spare Tail — {TAILS[1][1]}"></div>
      <div class="viewer-meta"><span class="mono">Spare Tail · {_(U['colours_n']).format(n=len(TAILS))}</span><strong class="viewer-name">{TAILS[1][1]}</strong></div>
    </div>
  </div>
  <ul class="swatches swatches-tails">{tails}</ul>
  <div class="duo">
    <figure><div class="ph-clip"><img src="img/photos/spare-tail-1.webp" alt="Spare Tail" loading="lazy"></div></figure>
    <figure><div class="ph-clip"><img src="img/photos/spare-tail-2.webp" alt="Spare Tail" loading="lazy"></div></figure>
  </div>
</section>

<section class="acc wrap">
  <div class="acc-grid acc-grid-rev">
    <div class="acc-copy">
      <p class="eyebrow">{_(L('Accessory 02', 'Accessoire 02', 'Accesorio 02'))}</p>
      <h2 class="stencil" data-split>Lead Stickers</h2>
      <p>{_(L("Designed to adjust the buoyancy of your Glideway, so you can fish different layers of the water column — or simply compensate for the elements, like low water temperature or heavy wind.", "Conçus pour ajuster la flottabilité de votre Glideway : vous pouvez pêcher différentes couches d'eau, ou compenser les éléments, comme une eau froide ou un vent fort.", "Diseñados para ajustar la flotabilidad de tu Glideway: puedes pescar distintas capas de agua o compensar los elementos, como el agua fría o el viento fuerte."))}</p>
      <p class="note">{_(L("To remove them, use the gap in the Glideway cavities to slide in the treble and pull the sticker out. Lead Stickers can also be used to fine-tune the weight of any other lure.", "Pour les retirer, glissez l'hameçon triple dans l'encoche de la cavité et tirez. Les Lead Stickers peuvent aussi servir à ajuster le poids de n'importe quel autre leurre.", "Para quitarlos, mete el anzuelo triple en la ranura de la cavidad y tira. Los Lead Stickers también sirven para ajustar el peso de cualquier otro señuelo."))}</p>
    </div>
    <figure class="acc-photo"><div class="ph-clip"><img src="img/photos/lead-stickers-2.webp" alt="Lead Sticker" loading="lazy"></div></figure>
  </div>
  <h3 class="when-title">{_(L('When should you add them?', 'Quand les ajouter ?', '¿Cuándo añadirlos?'))}</h3>
  <ol class="whens">{wl}</ol>
</section>
"""
    return layout("accessories", L("Accessories — Spare Tails & Lead Stickers | Swimbait Republic", "Accessoires — Spare Tails et Lead Stickers | Swimbait Republic", "Accesorios — Spare Tails y Lead Stickers | Swimbait Republic"),
                  L("Spare Tails in 11 colours and Lead Stickers to tune the buoyancy of your Glideway.", "Des Spare Tails en 11 coloris et des Lead Stickers pour régler la flottabilité de votre Glideway.", "Spare Tails en 11 colores y Lead Stickers para ajustar la flotabilidad de tu Glideway."), body, "accessories")


ROD_SPECS = [(W_LENGTH, "7'11\""), (L("Lure range", "Poids de leurre", "Rango de señuelo"), "1–3 oz"),
             (L("Braid", "Tresse", "Trenzado"), "15–30 lb"), (L("Reel size", "Taille moulinet", "Tamaño de carrete"), "200")]


def rod():
    body = f"""
<section class="phero phero-rod">
  <div class="phero-media" data-parallax><img src="img/photos/rod-hero.webp" alt="" fetchpriority="high"></div>
  <div class="phero-inner wrap">
    <p class="eyebrow">{_(L('Category 03 · Rods', 'Catégorie 03 · Cannes', 'Categoría 03 · Cañas'))}</p>
    <h1 class="stencil display-stencil" data-split>Sneak Attack 711</h1>
    <p class="lede">{_(L('Designed to adapt to multiple scenarios and techniques, with outstanding versatility across a 1 to 3 oz lure range.', 'Conçue pour s’adapter à de multiples situations et techniques, avec une polyvalence remarquable sur une plage de leurres de 1 à 3 oz.', 'Diseñada para adaptarse a múltiples escenarios y técnicas, con una versatilidad excepcional en un rango de señuelos de 1 a 3 oz.'))}</p>
  </div>
</section>
<section class="pd-intro">
  <div class="wrap">{stats([("7'11", '"', W_LENGTH), ("1–3", "oz", L("Lure range", "Poids de leurre", "Rango de señuelo")), ("14", "", L("Titanium guides", "Anneaux titane", "Anillas de titanio")), ("200", "", L("Reel size", "Taille moulinet", "Tamaño de carrete"))])}</div>
  <div class="wrap pd-intro-grid">
    <p class="pd-lede">{_(L("Built with a Toray 11,000T carbon blank — extreme lightness, exceptional strength, and a weight-to-power ratio that's hard to match.", "Construite sur un blank carbone Toray 11 000T : extrême légèreté, résistance exceptionnelle et un rapport poids/puissance difficile à égaler.", "Construida con un blank de carbono Toray 11.000T: ligereza extrema, resistencia excepcional y una relación peso/potencia difícil de igualar."))}</p>
    <div class="pd-body">
      <p>{_(L("Pair it with a size 200 reel for perfect balance and handling comfort. Its smooth, progressive action allows precise control of lighter lures while keeping the power to snap cast a 3 oz lure over long distances with complete confidence.", "Associez-la à un moulinet taille 200 pour un équilibre et un confort parfaits. Son action progressive et douce permet de contrôler précisément les leurres légers, tout en gardant la puissance pour lancer un leurre de 3 oz très loin, en toute confiance.", "Combínala con un carrete tamaño 200 para un equilibrio y una comodidad perfectos. Su acción progresiva y suave permite controlar con precisión los señuelos ligeros, manteniendo la potencia para lanzar un señuelo de 3 oz muy lejos con total confianza."))}</p>
      <p>{_(L("Unlike typical swimbait rods, it absorbs the excess energy of the cast instead of sending it to your elbow and shoulder — so you can keep bombing big baits all day long without pain or fatigue.", "Contrairement aux cannes swimbait classiques, elle absorbe l'excès d'énergie du lancer au lieu de l'envoyer dans le coude et l'épaule : vous pouvez lancer de gros leurres toute la journée sans douleur ni fatigue.", "A diferencia de las cañas de swimbait típicas, absorbe el exceso de energía del lance en lugar de transmitirlo al codo y al hombro: puedes lanzar señuelos grandes todo el día sin dolor ni fatiga."))}</p>
      <p>{_(L("The progressive action also absorbs the head shakes during the fight, significantly reducing the chances of losing the fish.", "L'action progressive amortit aussi les coups de tête pendant le combat, ce qui réduit nettement les risques de décrocher le poisson.", "La acción progresiva también absorbe los cabezazos durante la pelea, reduciendo mucho las posibilidades de perder el pez."))}</p>
      <p class="note">{_(L("Designed to perform at 100% with braided line. Not recommended with fluorocarbon as the main line.", "Conçue pour donner 100 % de ses performances avec de la tresse. Déconseillée avec du fluorocarbone en corps de ligne.", "Diseñada para rendir al 100 % con trenzado. No recomendada con fluorocarbono como línea principal."))}</p>
    </div>
  </div>
</section>
<section class="rod-strip" aria-hidden="true"><img src="img/photos/sneak-attack-0.webp" alt="" data-rod></section>
<section class="guides">
  <div class="wrap guides-grid">
    <div class="guides-big" aria-hidden="true"><span data-count="14">14</span><small>{_(L('titanium guides', 'anneaux titane', 'anillas de titanio'))}</small></div>
    <div>
      <h2 class="h2">{_(L('Guide system', 'Les anneaux', 'Sistema de anillas'))}</h2>
      <p>{_(L("A guide layout engineered to channel line flow with maximum efficiency. The 14 titanium guides control every contact point and keep the line perfectly aligned, reducing friction and turbulence.", "Une disposition des anneaux étudiée pour guider la ligne le plus efficacement possible. Les 14 anneaux en titane contrôlent chaque point de contact et gardent la ligne parfaitement alignée, en réduisant frottements et turbulences.", "Una distribución de anillas diseñada para canalizar el hilo con la máxima eficacia. Las 14 anillas de titanio controlan cada punto de contacto y mantienen el hilo perfectamente alineado, reduciendo fricción y turbulencias."))}</p>
      <p>{_(L("The short spacing between guides stops the line from forming loops or tangles during the cast or the retrieve, so wind knots are virtually eliminated. And the generous inner diameter lets leader knots pass with minimal friction, even with thick leaders.", "Leur faible espacement empêche la ligne de former des boucles ou des nœuds au lancer comme à la récupération : les perruques en tresse sont quasiment éliminées. Et leur grand diamètre intérieur laisse passer les nœuds de bas de ligne sans frottement, même avec un bas de ligne épais.", "Su poca separación evita que el hilo forme bucles o enredos al lanzar o recoger: los nudos de viento prácticamente desaparecen. Y su amplio diámetro interior deja pasar los nudos del bajo con mínima fricción, incluso con bajos gruesos."))}</p>
    </div>
  </div>
</section>
<section class="pd-photos wrap">
  <figure class="ph-big"><div class="ph-clip"><img src="img/photos/banner-3.webp" alt="Sneak Attack 711" loading="lazy" data-parallax-img></div></figure>
  <figure class="ph-small"><div class="ph-clip"><img src="img/photos/barramundi.webp" alt="Sneak Attack 711" loading="lazy" data-parallax-img></div></figure>
</section>
<section class="specs wrap">
  <h2 class="h2">{_(U['specs'])}</h2>
  {spec_list(ROD_SPECS, 'spec-sheet')}
</section>
{film("sneakattack", "sneakattack", "Sneak Attack 711")}
<section class="upsell wrap">
  <a class="upsell-card" href="{url('swimbaits')}">
    <img src="img/photos/glideway-sunset.webp" alt="" loading="lazy">
    <div><p class="eyebrow">{_(L('Load it up', 'À associer', 'Para combinar'))}</p><h3>{_(L('The Glideway range', 'La gamme Glideway', 'La gama Glideway'))}</h3><p>{_(L('126, 176 and 236 — three sizes, one freestyle action.', '126, 176 et 236 : trois tailles, la même nage freestyle.', '126, 176 y 236: tres tamaños, la misma natación freestyle.'))}</p>{ICONS['arrow']}</div>
  </a>
</section>
"""
    return layout("sneak-attack-711", L("Sneak Attack 711 — swimbait rod 1–3 oz | Swimbait Republic", "Sneak Attack 711 — canne swimbait 1–3 oz | Swimbait Republic", "Sneak Attack 711 — caña de swimbait 1–3 oz | Swimbait Republic"),
                  L("Toray 11,000T carbon swimbait rod, 7'11\", 1–3 oz, 14 titanium guides.", "Canne swimbait carbone Toray 11 000T, 7'11\", 1–3 oz, 14 anneaux titane.", "Caña de swimbait de carbono Toray 11.000T, 7'11\", 1–3 oz, 14 anillas de titanio."), body, "rods")


def apparel():
    feats = [(L("Embroidered logo", "Logo brodé", "Logo bordado"), L("on the central panel", "sur le panneau central", "en el panel central")),
             (L("Printed visor", "Visière imprimée", "Visera estampada"), L("Republic pattern underneath", "motif Republic dessous", "estampado Republic debajo")),
             (L("Breathable mesh", "Filet respirant", "Malla transpirable"), L("keeps you cool", "garde au frais", "te mantiene fresco")),
             ("Snapback", L("adjustable, anti-rust closure", "réglable, fermeture antirouille", "ajustable, cierre antióxido")),
             (L("One size", "Taille unique", "Talla única"), L("fits most", "convient à la plupart", "sirve a casi todos"))]
    fl = "".join(f'<li><strong>{_(a)}</strong><span>{_(b)}</span></li>' for a, b in feats)
    body = page_hero(L("Category 04 · Apparel", "Catégorie 04 · Textile", "Categoría 04 · Ropa"), U["apparel"],
                     L("The Swimbait Republic flat cap.", "La casquette Swimbait Republic.", "La gorra Swimbait Republic."), "img/photos/banner-4.webp") + f"""
<section class="acc wrap">
  <div class="acc-grid">
    <figure class="acc-photo"><div class="ph-clip"><img src="img/photos/flat-cap.webp" alt="Flat Cap" loading="lazy"></div></figure>
    <div class="acc-copy">
      <p class="eyebrow">{_(L('Apparel 01', 'Textile 01', 'Ropa 01'))}</p>
      <h2 class="stencil" data-split>Flat Cap</h2>
      <p>{_(L("The Swimbait Republic Flat Cap features an embroidered logo on the central panel and a printed visor. Breathable mesh keeps you cool, and the adjustable snapback includes an anti-rust closure. One size fits most.", "La Flat Cap Swimbait Republic porte un logo brodé sur le panneau central et une visière imprimée. Le filet respirant vous garde au frais, et le snapback réglable a une fermeture antirouille. Taille unique.", "La Flat Cap de Swimbait Republic lleva el logo bordado en el panel central y una visera estampada. La malla transpirable te mantiene fresco y el cierre snapback ajustable es antióxido. Talla única."))}</p>
      <ul class="feats">{fl}</ul>
      {btn(url('dealers'), U['find_dealer'])}
    </div>
  </div>
</section>
"""
    return layout("apparel", L("Apparel — Flat Cap | Swimbait Republic", "Textile — Flat Cap | Swimbait Republic", "Ropa — Flat Cap | Swimbait Republic"),
                  L("The Swimbait Republic Flat Cap.", "La casquette Swimbait Republic.", "La gorra Swimbait Republic."), body, "apparel")


def about():
    body = page_hero(U["about"], U["about_us"],
                     L("Over 10 years of swimbait fishing, and a whole life dedicated to many other lure techniques.", "Plus de 10 ans de pêche au swimbait, et toute une vie consacrée à bien d'autres techniques aux leurres.", "Más de 10 años pescando a swimbait y toda una vida dedicada a muchas otras técnicas de señuelo."),
                     "img/photos/production.webp") + f"""
<section class="manifesto">
  <div class="wrap"><p class="manifesto-text">{_(L("We put all our experience into our lures to help anglers catch bigger fish in an easier way — with the highest quality raw materials and handcraft work, for the best possible price, while ensuring good margins for all our business partners.", "Nous mettons toute notre expérience dans nos leurres pour aider les pêcheurs à prendre de plus gros poissons plus facilement — avec des matériaux de la meilleure qualité et un vrai travail artisanal, au meilleur prix possible, tout en garantissant de bonnes marges à tous nos partenaires.", "Ponemos toda nuestra experiencia en nuestros señuelos para ayudar a los pescadores a capturar peces más grandes de forma más fácil, con materiales de la máxima calidad y trabajo artesanal, al mejor precio posible y garantizando buenos márgenes a todos nuestros socios."))}</p></div>
</section>
<section class="story wrap">
  <article class="story-row">
    <figure><div class="ph-clip"><img src="img/photos/prototypes.webp" alt="Glideway prototypes" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">01</p><h2 class="h2">{_(L('How are our lures born?', 'Comment naissent nos leurres ?', '¿Cómo nacen nuestros señuelos?'))}</h2><p>{_(L("First a concept or an idea clicks in our brain. Then comes the draw, after that a wooden prototype, and finally a lot of resin prototypes to try every possible weight configuration, bait thickness… This process is a mix of creativity and artisan skills.", "D'abord, une idée nous traverse l'esprit. Puis vient le dessin, ensuite un prototype en bois, et enfin beaucoup de prototypes en résine pour tester toutes les configurations de poids et d'épaisseur possibles… Un mélange de créativité et de savoir-faire artisanal.", "Primero una idea nos hace clic en la cabeza. Luego llega el dibujo, después un prototipo de madera y, por último, muchos prototipos de resina para probar todas las configuraciones de peso y grosor posibles… Una mezcla de creatividad y oficio artesano."))}</p></div>
  </article>
  <article class="story-row story-rev">
    <figure><div class="ph-clip"><img src="img/photos/testing.webp" alt="Field testing" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">02</p><h2 class="h2">{_(L('Testing', 'Les tests', 'Pruebas'))}</h2><p>{_(L("One of the most important parts of the process: even if the lure swims great in the tank, we have to make sure it performs in different conditions and scenarios — and that fish love it!", "L'une des étapes les plus importantes : même si le leurre nage parfaitement en bassin, il doit performer dans toutes les conditions et situations — et plaire aux poissons !", "Una de las partes más importantes del proceso: aunque el señuelo nade genial en el tanque, tiene que rendir en distintas condiciones y escenarios, ¡y gustar a los peces!"))}</p>
    <p class="big-fact"><span data-count="2">2</span> {_(L('years', 'ans', 'años'))}<small>{_(L('of field testing, at most, before a release', 'de tests sur le terrain, au maximum, avant une sortie', 'de pruebas en el agua, como máximo, antes de un lanzamiento'))}</small></p></div>
  </article>
  <article class="story-row">
    <figure><div class="ph-clip"><img src="img/photos/bass-reeds.webp" alt="Black bass" loading="lazy" data-parallax-img></div></figure>
    <div><p class="step-n">03</p><h2 class="h2">{_(L('Production', 'La production', 'Producción'))}</h2><p>{_(L("Having an amazing bait means nothing to us if we can't make it available for everybody. We travel the world to find high quality factories to produce our creations, and we personally supervise the whole process — from shell injection to packing — to make sure everything reaches the quality level we aim for.", "Avoir un leurre incroyable ne sert à rien s'il n'est pas accessible à tous. Nous parcourons le monde pour trouver des usines de grande qualité, et nous supervisons nous-mêmes tout le processus — de l'injection des coques à l'emballage — pour atteindre le niveau de qualité que nous visons.", "Tener un señuelo increíble no significa nada si no podemos hacerlo llegar a todo el mundo. Recorremos el mundo buscando fábricas de alta calidad y supervisamos personalmente todo el proceso, desde la inyección de las carcasas hasta el embalaje, para alcanzar el nivel de calidad que buscamos."))}</p></div>
  </article>
</section>
<section class="upsell wrap">
  <a class="upsell-card" href="{url('swimbaits')}">
    <img src="img/photos/glideway-sunset.webp" alt="" loading="lazy">
    <div><p class="eyebrow">{_(L('The result', 'Le résultat', 'El resultado'))}</p><h3>{_(L('Meet the Glideway', 'Découvrez le Glideway', 'Descubre el Glideway'))}</h3><p>{_(L('Three sizes, one freestyle action.', 'Trois tailles, une seule nage freestyle.', 'Tres tamaños, una sola natación freestyle.'))}</p>{ICONS['arrow']}</div>
  </a>
</section>
"""
    return layout("about", L("About us | Swimbait Republic", "À propos | Swimbait Republic", "Sobre nosotros | Swimbait Republic"),
                  L("Over 10 years of swimbait fishing put into every lure.", "Plus de 10 ans de pêche au swimbait dans chaque leurre.", "Más de 10 años de pesca a swimbait en cada señuelo."), body, "about")


def dealers():
    cards = "".join(
        f'<article class="dcard"><span class="dcode">{code}</span><h3>{_(COUNTRY[code])}</h3><p class="dname">{n}</p>'
        f'<a href="mailto:{m}">{m}</a><a href="{w}" target="_blank" rel="noopener">{w.split("//")[1].strip("/")} ↗</a></article>'
        for code, n, m, w in DEALERS)
    direct = "".join(f'<li><span class="dcode">{c}</span>{_(COUNTRY[c])}</li>' for c in DIRECT)
    body = page_hero(L("Worldwide", "Dans le monde", "En el mundo"), L("Our dealers", "Nos revendeurs", "Nuestros distribuidores"),
                     L("Find the Republic near you — or talk to us directly.", "Trouvez la Republic près de chez vous, ou contactez-nous directement.", "Encuentra la Republic cerca de ti o habla directamente con nosotros."),
                     "img/photos/glideway-236-top.webp") + f"""
<section class="dealers wrap">
  <p class="eyebrow">{_(L('Official distributors', 'Distributeurs officiels', 'Distribuidores oficiales'))}</p>
  <div class="dgrid">{cards}</div>
  <div class="direct">
    <div><h2 class="h2">{_(L('Direct to tackle shops', 'En direct avec les magasins', 'Directo a tiendas'))}</h2>
    <p>{_(L('In these countries we work directly with tackle shops. Shop owner or angler, get in touch.', 'Dans ces pays, nous travaillons directement avec les magasins de pêche. Magasin ou pêcheur, contactez-nous.', 'En estos países trabajamos directamente con las tiendas de pesca. Seas tienda o pescador, contáctanos.'))}</p>{btn(url('contact'), U['contact_us'])}</div>
    <ul class="direct-list">{direct}</ul>
  </div>
</section>
"""
    return layout("dealers", L("Dealers worldwide | Swimbait Republic", "Revendeurs dans le monde | Swimbait Republic", "Distribuidores en el mundo | Swimbait Republic"),
                  L("Swimbait Republic dealers in 6 countries, and direct to tackle shops in 6 more.", "Revendeurs Swimbait Republic dans 6 pays, et en direct avec les magasins dans 6 autres.", "Distribuidores de Swimbait Republic en 6 países y directo a tiendas en otros 6."), body, "dealers")


def contact():
    bad = L("Please fill in your name, a valid email and your message.", "Merci d'indiquer votre nom, un email valide et votre message.", "Indica tu nombre, un email válido y tu mensaje.")
    ok = L("Thanks! (Prototype: the form still has to be connected.)", "Merci ! (Maquette : le formulaire reste à brancher.)", "¡Gracias! (Prototipo: el formulario aún no está conectado.)")
    body = page_hero(U["contact"], U["contact_us"],
                     L("Have a question or a comment for our team? We'd love to hear from you.", "Une question ou un commentaire pour notre équipe ? On sera ravis de vous lire.", "¿Tienes alguna pregunta o comentario para nuestro equipo? Nos encantará leerte."),
                     "img/photos/glideway-126-branch.webp") + f"""
<section class="contact wrap">
  <form class="cform" novalidate data-msg-bad="{e(_(bad))}" data-msg-ok="{e(_(ok))}">
    <label><span>{_(L('Name', 'Nom', 'Nombre'))}</span><input name="name" required autocomplete="name"></label>
    <label><span>Email</span><input name="email" type="email" required autocomplete="email"></label>
    <label class="full"><span>{_(L('Message', 'Message', 'Mensaje'))}</span><textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit"><span>{_(L('Send message', 'Envoyer', 'Enviar mensaje'))}</span>{ICONS['arrow']}</button>
    <p class="form-msg" role="status" aria-live="polite"></p>
  </form>
  <aside class="contact-side">
    <p class="eyebrow">{_(L('Or slide into our DMs', 'Ou écrivez-nous en DM', 'O escríbenos por DM'))}</p>
    <p>{_(L('Send us a message through our social media profiles.', 'Envoyez-nous un message sur nos réseaux sociaux.', 'Mándanos un mensaje por nuestras redes sociales.'))}</p>
    {socials("social social-big")}
    <p class="eyebrow" style="margin-top:2.5rem">{_(L('Looking for a shop?', 'Vous cherchez un magasin ?', '¿Buscas una tienda?'))}</p>
    {btn(url('dealers'), U['locate'], 'btn btn-ghost')}
  </aside>
</section>
"""
    return layout("contact", L("Contact us | Swimbait Republic", "Contact | Swimbait Republic", "Contacto | Swimbait Republic"),
                  L("Get in touch with Swimbait Republic.", "Contactez Swimbait Republic.", "Contacta con Swimbait Republic."), body)


# ---------------------------------------------------------------- BUILD

def main():
    pages = {"index": home, "swimbaits": swimbaits, "accessories": accessories, "sneak-attack-711": rod,
             "apparel": apparel, "about": about, "dealers": dealers, "contact": contact}
    for k in ORDER:
        pages[f"glideway-{k}"] = (lambda kk: (lambda: glideway(kk)))(k)
    n = 0
    for lang in LANGS:
        CUR["lang"] = lang
        for slug, fn in pages.items():
            with open(os.path.join(ROOT, url(slug, lang)), "w", encoding="utf-8") as f:
                f.write(fn())
            n += 1
    print(n, "pages générées (EN / FR / ES)")


if __name__ == "__main__":
    main()
