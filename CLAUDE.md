# Swimbait Republic — nouveau site

## Le projet

Refonte de **https://www.swimbaitrepublic.com** (marque espagnole de swimbaits : leurres Glideway, accessoires, canne, casquette). Site actuel : PHP/Bootstrap, en anglais, une page d'accueil avec 4 vignettes de catégories, sans mise en avant des produits.
Clément mène ce projet **seul**.

Objectif de la refonte : donner une vraie personnalité (registre « République » militaire / carnet de terrain), un vrai parcours au scroll, une page par produit, plus visuel.

## Charte = celle du site actuel (demande de Clément, 2026-11-19)

Relevée dans leur CSS : fond clair `#f8f8f8` / blanc, vert olive `#3e4939` (en-tête avec leur image camo `img/brand/header.webp`, pied de page, boutons, bandeaux specs), kaki `#c8c8b1` / `#cdd5c6`, rouge `#c10e2f` / `#a51632` en petite touche. Polices : Barlow Condensed, Barlow, Black Ops One (noms produits). Tableaux de specs au format de leurs fiches (en-tête olive, cellules grises). Les dessins de catégories de l'accueil sont les leurs (`img/brand/cat-*.webp`).

Retours de Clément sur la V1 (sombre, très longue) : trop long, couleurs pas les leurs, trop de grosses phrases. V2 : pages environ deux fois plus courtes, titres sobres, plus de bandeaux défilants ni de slogans géants. **À garder absolument** : les animations qui expliquent le leurre (gamme à l'échelle, nage en S au scroll, module de profondeur Lead Stickers, nuancier cliquable, leurre animé en tête de fiche).

## Structure

```
build.py            TOUT le contenu (textes, specs, coloris, revendeurs) + gabarits → génère les .html
                    Ne pas éditer les .html à la main : modifier build.py puis  python3 build.py
index.html          accueil (vidéo, 4 catégories, gamme à l'échelle, nage en S, profondeur, film, coloris, revendeurs)
swimbaits.html      les 3 Glideway + tableau comparatif
glideway-126/176/236.html   fiche produit (hero, specs, module profondeur interactif, film, nuancier cliquable)
accessories.html    Spare Tail (11 coloris) + Lead Stickers (« quand les ajouter »)
sneak-attack-711.html   canne
apparel.html        casquette
about.html, dealers.html, contact.html
css/style.css       tout le design ; couleurs dans :root
js/app.js           défilement fluide (Lenis), animations au scroll (GSAP ScrollTrigger, CDN), nuanciers, films, menu
img/colors/<id>/    photos de coloris DÉTOURÉES (fond blanc retiré) — générées par tools/prepare_assets.py
img/photos, img/posters, img/brand   photos du client converties en webp
media/              vidéos ré-encodées (720p, 8–12 Mo) + hero-loop.mp4 (20 s de la vidéo 236, sans son)
tools/prepare_assets.py   reconvertit/détoure les images depuis _scrape/
_scrape/            copie brute du site actuel (ignoré par git)
```

Les animations dépendent de GSAP/Lenis (cdnjs / unpkg). Si les CDN ne chargent pas, le site reste lisible (repli sans animations).

## Règles

- **Ne rien inventer.** Tous les textes, specs, coloris et revendeurs viennent du site actuel. Seules des fautes d'anglais évidentes ont été corrigées (« it's » → « is », « addind », etc.). Les titres d'accroche (« Pick your poison », « Big baits. Bigger bites. », « Dial in your depth ») sont du ton éditorial, pas des affirmations.
- Distinguer : fait vérifié / hypothèse / proposition.
- Clément n'a pas de background technique : expliquer simplement.
- Avant de pousser : vérifier qu'aucune page n'a d'erreur JS ni d'image manquante.

## À confirmer avec le client

- **Longueur de la Glideway 126** : non indiquée sur leur fiche (affichée « — » dans le comparatif ; le nom suggère 126 mm).
- **Formulaire de contact** : sur leur site il poste vers leur serveur PHP. Ici c'est une maquette (message « à brancher »). Il faudra soit l'envoyer vers leur backend, soit un service type Formspree, avec leur adresse email.
- **Newsletter** : présente sur l'ancien site (lien pied de page), pas reprise faute de backend.
- **Pages légales** : les liens pointent vers celles de l'ancien site.
- **Langues** : site actuel en anglais uniquement (variable `lang` prévue chez eux). FR/ES possibles plus tard.
- **Vente en ligne** : il n'y en a pas sur le site actuel (renvoi vers les revendeurs) — conservé ainsi.

## Mise en ligne

`./maj.sh "message"` met à jour le numéro de version CSS/JS, régénère les pages, commit et push.
Dépôt GitHub : **à relier** (aucun dépôt Swimbait trouvé sur le compte au 2026-11-19).
