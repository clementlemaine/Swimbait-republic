# Swimbait Republic — nouveau site

## Le projet

Refonte de **https://www.swimbaitrepublic.com** (marque espagnole de swimbaits : leurres Glideway, accessoires, canne, casquette). Site actuel : PHP/Bootstrap, en anglais, une page d'accueil avec 4 vignettes de catégories, sans mise en avant des produits.
Clément mène ce projet **seul**.

Objectif de la refonte : donner une vraie personnalité (registre « République » militaire / carnet de terrain), un vrai parcours au scroll, une page par produit, plus visuel.

## Charte (reprise du site actuel, vérifiée par capture)

- Vert olive `#3e4939`, vert sauge `#77916b`, kaki `#c8c8b1`, fond camo (`img/brand/camo.webp`)
- Rouge du logo `#ff0129`, rouge bordeaux des titres `#a51632`
- Polices : Barlow Condensed (titres), Barlow (texte), **Black Ops One** (noms produits, déjà utilisée sur leurs fiches). Ajout : JetBrains Mono pour les petites étiquettes « fiche technique ».

## Structure

```
build.py            TOUT le contenu (textes, specs, coloris, revendeurs) + gabarits → génère les .html
                    Ne pas éditer les .html à la main : modifier build.py puis  python3 build.py
index.html          accueil (vidéo plein écran, manifeste, famille à l'échelle, scène « glide », profondeur, film, coloris, gear, processus horizontal, pays)
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
