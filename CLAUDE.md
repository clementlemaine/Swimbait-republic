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
build.py            TOUT le contenu en 3 langues, sous la forme L("anglais", "français", "espagnol") + gabarits.
                    Ne pas éditer les .html à la main : modifier build.py puis  python3 build.py  (33 pages)
Langues             ESPAGNOL PAR DÉFAUT (demande de Clément, 2026-11-19) = index.html, glideway-176.html … ;
                    anglais = index-en.html … ; français = index-fr.html … (fichiers à la racine : Safari bloque les chemins ../ en local)
                    Sélecteur EN / FR / ES dans l'en-tête, qui renvoie vers la même page dans l'autre langue.
Accueil             vidéo (reste en place) + barre des 4 catégories → le panneau « gamme » glisse par-dessus avec un vrai
                    Glideway 176 (Galaxy Mirror, « GLIDEWAY 176 » imprimé) qui traverse → onglets 126/176/236 + bac de
                    profondeur Lead Stickers → carrousel des coloris par modèle → grandes cartes produits → film → revendeurs
glideway-126/176/236   fiche produit (hero, specs, profondeur, film, nuancier cliquable)
css/style.css, js/app.js, img/, media/, tools/prepare_assets.py, _scrape/ (ignoré par git)
```

Abandonné à la demande de Clément (2026-11-19) : la vue du dessus dessinée du leurre (forme pas fidèle). **Ne jamais dessiner le leurre** : uniquement les vraies photos détourées.
Le français et l'espagnol sont des traductions faites par Claude : à faire relire par le client (vocabulaire pêche : flottant lent / coulant lent, flotante lento / hundimiento lento).


## Vues 6 angles des fiches Glideway (2026-11-19)

Sous le titre de chaque fiche, il y a 6 boutons : Profil · Face · Autre côté · Dessus · Dessous · Arrière.
Seul le profil a une vraie photo (le coloris détouré). Les 5 autres affichent « Photo à venir », car le client n'a pas ces photos.
**Pour les ajouter :** déposer `img/views/<126|176|236>/<face|autre-cote|dessus|dessous|arriere>.webp` (fond blanc ou détouré), puis `python3 build.py`. La photo remplace automatiquement « Photo à venir ». **Ne pas générer ni dessiner ces vues.**

**État des vues (2026-11-19) :** Glideway 176 = profil (vraie photo), autre côté (vraie photo en miroir), face (générée par Nano Banana Pro, à faire valider par le client), dessus = **vraie photo envoyée par Clément** (2026-11-19, coloris vert pailleté avec « GLIDEWAY 176 » imprimé, original dans `_scrape/client/`, détourée par `tools/cutout_client_photo.py`), dessous / arrière = « photo à venir ». Dessus et dessous générés ont été **refusés par Clément (« le leurre n'est pas comme ça »)**, mis de côté dans `_scrape/gen/rejet/`. Ne plus générer de vues du produit : seulement de vraies photos du client. 126 et 236 : seulement le profil. Script : `tools/prepare_views.py`. Coût Gemini engagé : 4 images 2K, environ 0,55 $.

**Retour arrière :** sur les fiches, bouton rouge « ← Volver » ; le bouton retour du navigateur ramène aussi au même endroit, avec la même taille choisie (position gardée en sessionStorage). Le rechargement repart en haut.

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
