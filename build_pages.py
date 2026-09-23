"""Generate the standalone pages that share the Farah Plast site chrome."""

from pathlib import Path

ROOT = Path(__file__).parent
NAV = [
    ("index.html", "Accueil"),
    ("apropos.html", "À propos"),
    ("services.html", "Nos services"),
    ("demarche.html", "Notre démarche"),
    ("galerie.html", "Galerie"),
    ("contact.html", "Contact"),
]


def button(label, url, tone="light"):
    return f'<a class="button button-{tone}" href="{url}">{label} <span aria-hidden="true">↗</span></a>'


def hero(kicker, title, copy, image, action, tone="light"):
    return f'''<section class="page-hero" style="--page-image:url('assets/{image}')">
      <div class="container page-hero-inner">
        <div class="eyebrow eyebrow-light"><span class="eyebrow-line"></span>{kicker}</div>
        <h1>{title}</h1>
        <p>{copy}</p>
        {button(*action, tone=tone)}
      </div>
    </section>'''


def shell(filename, title, description, content):
    links = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == filename else ""
        cls = ' class="nav-contact"' if href == "contact.html" else ""
        arrow = ' <span aria-hidden="true">↗</span>' if href == "contact.html" else ""
        links.append(f'<a{cls} href="{href}"{current}>{label}{arrow}</a>')
    html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#10253b" />
  <meta name="description" content="{description}" />
  <title>{title} — Farah Plast Merrouche</title>
  <link rel="icon" type="image/png" href="assets/logo-mark.png" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <div class="topbar"><div class="container topbar-inner"><span>Bordj Ghedir, Bordj Bou Arréridj · Algérie</span><a href="tel:+21335206729">Service commercial : 035 20 67 29</a></div></div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Farah Plast Merrouche, retour à l'accueil"><img src="assets/logo-mark.png" alt="" width="66" height="62" /><span class="brand-copy"><strong>FARAH PLAST</strong><span>MERROUCHE</span></span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
      <nav class="main-nav" id="main-nav" aria-label="Navigation principale">{''.join(links)}</nav>
    </div>
  </header>
  <main id="contenu">{content}</main>
  <footer class="footer">
    <div class="container footer-main"><div class="footer-brand"><img src="assets/logo-mark.png" alt="" width="80" height="76" /><div><strong>FARAH PLAST<br />MERROUCHE</strong><span>Fabrication · Broyage · Recyclage</span></div></div><div class="footer-right"><p>Des sacs pour un avenir plus propre.</p><a href="index.html">Accueil ↑</a></div></div>
    <div class="container footer-bottom"><span>© <span id="year">2026</span> Farah Plast Merrouche. Tous droits réservés.</span><span>Bordj Ghedir · Algérie</span></div>
  </footer>
  <script src="script.js" defer></script>
</body>
</html>
'''
    (ROOT / filename).write_text(html, encoding="utf-8")


about = hero(
    "NOTRE ENTREPRISE", "Une industrie locale.<br /><em>Une vision durable.</em>",
    "Depuis Bordj Ghedir, nous fabriquons et valorisons la matière plastique avec un savoir-faire ancré dans notre territoire.",
    "exterieur.webp", ("Nous contacter", "contact.html"),
) + '''<section class="section"><div class="container feature-split">
  <div class="feature-media"><img src="assets/fabrication-et-recyclage.webp" alt="Fabrication et recyclage plastique dans les ateliers Farah Plast Merrouche" /></div>
  <div class="feature-copy"><div class="eyebrow"><span class="eyebrow-line"></span>QUI NOUS SOMMES</div><h2>Transformer avec <em>exigence.</em></h2>
    <p class="lead">Farah Plast Merrouche est implantée à Bordj Ghedir, dans la wilaya de Bordj Bou Arréridj.</p>
    <p>Depuis 2011, nous développons deux activités complémentaires : la fabrication de sacs plastiques et la préparation de matières issues du broyage. Cette proximité entre production et valorisation guide notre travail au quotidien.</p>
    <p>Nous échangeons avec chaque client pour comprendre son besoin, ses contraintes d’utilisation et les caractéristiques de la matière attendue.</p>
    <div class="check-list"><span>Production locale</span><span>Atelier de transformation</span><span>Relation directe</span></div>
  </div>
</div></section>
<section class="section section-tint"><div class="container"><div class="center-heading"><div class="eyebrow"><span class="eyebrow-line"></span>CE QUI NOUS ANIME</div><h2>Une entreprise tournée vers <em>l’action.</em></h2></div>
  <div class="info-grid"><article class="info-card"><span>01</span><h3>Fabriquer</h3><p>Produire des sacs et des emballages plastiques adaptés aux usages de nos clients.</p></article><article class="info-card"><span>02</span><h3>Valoriser</h3><p>Collecter, broyer et préparer des matières plastiques pour leur donner une nouvelle utilité.</p></article><article class="info-card"><span>03</span><h3>Accompagner</h3><p>Rester disponibles pour discuter des formats, des quantités et des besoins de chaque projet.</p></article></div>
</div></section>
<section class="cta-band"><div class="container cta-band-inner"><div><div class="eyebrow eyebrow-light"><span class="eyebrow-line"></span>TRAVAILLONS ENSEMBLE</div><h2>Parlons de votre <em>projet.</em></h2></div>''' + button("Prendre contact", "contact.html", "on-dark") + '</div></section>'

services = hero(
    "NOS SERVICES", "La matière au cœur<br /><em>de notre métier.</em>",
    "Fabrication de sacs plastiques, broyage et recyclage : découvrez les activités de notre atelier et nos perspectives de développement.",
    "films-colores.webp", ("Demander un renseignement", "contact.html"),
) + '''<section class="section"><div class="container"><div class="center-heading"><div class="eyebrow"><span class="eyebrow-line"></span>NOTRE SAVOIR-FAIRE</div><h2>Trois domaines, <em>une même exigence.</em></h2><p>Chaque projet commence par un échange sur les besoins, les usages et la matière.</p></div>
  <div class="service-detail" id="fabrication"><img src="assets/ligne-sacs.webp" alt="Ligne de fabrication de sacs plastiques" /><div><span class="detail-number">01 · PRODUCTION</span><h2>Fabrication de sacs <em>plastiques</em></h2><p>Notre atelier réalise des sacs et emballages plastiques destinés à différents usages. Nous étudions les besoins de format, de couleur et d’utilisation afin de proposer une solution adaptée.</p><ul><li>Sacs plastiques selon les besoins du client</li><li>Échanges sur les formats et l’utilisation</li><li>Production dans notre atelier à Bordj Ghedir</li></ul>''' + button("Discuter de votre besoin", "contact.html") + '''</div></div>
  <div class="service-detail reverse" id="recyclage"><img src="assets/broyeur.webp" alt="Équipement de broyage de matières plastiques" /><div><span class="detail-number">02 · VALORISATION</span><h2>Broyage & <em>recyclage</em></h2><p>Nous récupérons et broyons des déchets plastiques pour préparer une matière pouvant rejoindre de nouveaux cycles d’utilisation. La préparation est pensée selon la nature de la matière et les besoins exprimés.</p><ul><li>Collecte de matières plastiques à valoriser</li><li>Broyage et préparation</li><li>Échange sur les caractéristiques de la matière</li></ul>''' + button("Échanger sur la matière", "contact.html") + '''</div></div>
  <div class="service-detail" id="injection"><img src="assets/paillettes-plastique.webp" alt="Fragments de plastique préparés pour la transformation" /><div><span class="detail-number">03 · PROJET À VENIR</span><h2>Injection <em>plastique</em></h2><p>L’injection plastique est une perspective de développement pour l’entreprise. Cette activité n’est pas encore proposée comme service. Elle reflète notre volonté d’élargir progressivement nos possibilités de transformation.</p>''' + button("Suivre notre évolution", "contact.html") + '''</div></div>
</div></section>'''

process = hero(
    "NOTRE DÉMARCHE", "Donner une nouvelle<br /><em>valeur à la matière.</em>",
    "De la récupération à la préparation, nous avançons étape par étape pour faire de la matière plastique usagée une ressource utile.",
    "operateur-recyclage.webp", ("Découvrir nos services", "services.html"),
) + '''<section class="section"><div class="container"><div class="center-heading"><div class="eyebrow"><span class="eyebrow-line"></span>UNE CHAÎNE DE VALORISATION</div><h2>Une démarche <em>concrète.</em></h2><p>La valorisation commence par une bonne compréhension de la matière, puis par sa préparation dans l’atelier.</p></div>
  <div class="steps-grid"><article><span>01</span><h3>Collecter</h3><p>Récupérer les déchets plastiques destinés à une nouvelle utilisation.</p></article><article><span>02</span><h3>Broyer</h3><p>Réduire la matière à l’aide des équipements de notre atelier.</p></article><article><span>03</span><h3>Préparer</h3><p>Organiser la matière broyée selon ses caractéristiques et les besoins visés.</p></article><article><span>04</span><h3>Valoriser</h3><p>Permettre à la matière préparée d’entrer dans de nouveaux usages de production.</p></article></div>
</div></section>
<section class="section section-tint"><div class="container feature-split"><div class="feature-media"><img src="assets/matiere-broyee.webp" alt="Matière plastique broyée dans l'atelier" /></div><div class="feature-copy"><div class="eyebrow"><span class="eyebrow-line"></span>NOTRE ATELIER</div><h2>La transformation se voit <em>sur le terrain.</em></h2><p class="lead">Nos équipes interviennent directement sur les matières et les équipements.</p><p>Nous cherchons à préparer la matière de façon cohérente avec sa nature et sa destination. Cette démarche accompagne notre activité de fabrication et notre projet de développement.</p>''' + button("Voir les ateliers", "galerie.html") + '''</div></div></section>'''

photos = [
    ("ligne-sacs.webp", "Ligne de fabrication de sacs", "Fabrication de sacs"),
    ("rouleaux-film.webp", "Rouleaux de film plastique", "Ligne de production"),
    ("atelier-recyclage.webp", "Atelier de recyclage plastique", "Atelier recyclage"),
    ("sacs-conditionnes.webp", "Sacs plastiques conditionnés", "Produits conditionnés"),
    ("matiere-broyee.webp", "Matière plastique broyée", "Matière broyée"),
    ("extrusion-film.webp", "Machine d'extrusion du film", "Extrusion du film"),
    ("stock-matieres.webp", "Stock de matières plastiques", "Stock de matières"),
    ("atelier-recyclage-2.webp", "Espace de recyclage", "Recyclage"),
    ("valorisation-plastique.webp", "Valorisation du plastique", "Valorisation"),
    ("films-colores.webp", "Films plastiques colorés", "Films plastiques"),
    ("broyeur.webp", "Broyeur de plastique", "Équipement de broyage"),
    ("camion.webp", "Camion sur le site", "Logistique"),
]
gallery = hero(
    "GALERIE", "Notre activité<br /><em>en images.</em>",
    "Parcourez notre site, nos équipements et les matières que nous travaillons à Bordj Ghedir.",
    "atelier-recyclage-2.webp", ("Nous contacter", "contact.html"),
) + '<section class="section"><div class="container"><div class="center-heading"><div class="eyebrow"><span class="eyebrow-line"></span>DANS NOS ATELIERS</div><h2>Au plus près de <em>la production.</em></h2><p>Un aperçu de notre environnement de travail et de nos activités.</p></div><div class="photo-grid">' + ''.join(f'<figure><img src="assets/{file}" alt="{alt}" loading="lazy" /><figcaption>{caption}</figcaption></figure>' for file, alt, caption in photos) + '</div></div></section>'

contact = hero(
    "CONTACT", "Un projet, une question ?<br /><em>Échangeons.</em>",
    "Notre équipe est à votre écoute pour la fabrication de sacs plastiques et les demandes liées à la matière recyclée.",
    "exterieur.webp", ("Écrire un message", "#formulaire"),
) + '''<section class="section section-tint" id="formulaire"><div class="container contact-page-grid">
  <div class="contact-form-wrap"><div class="eyebrow"><span class="eyebrow-line"></span>ÉCRIVEZ-NOUS</div><h2>Parlez-nous de <em>votre besoin.</em></h2><p>Décrivez votre demande et indiquez comment nous pouvons vous joindre. Les champs marqués * sont obligatoires.</p>
    <form class="contact-form" action="https://formsubmit.co/farahplastmerrouche@gmail.com" method="POST">
      <input type="hidden" name="_subject" value="Nouvelle demande depuis le site Farah Plast Merrouche" />
      <input type="hidden" name="_next" value="https://renolix.github.io/adel.github.io/merci.html" />
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" class="honeypot" aria-hidden="true" />
      <div class="form-row"><div class="form-field"><label for="nom">Nom *</label><input id="nom" name="nom" type="text" autocomplete="name" required maxlength="100" /></div><div class="form-field"><label for="entreprise">Entreprise</label><input id="entreprise" name="entreprise" type="text" autocomplete="organization" maxlength="120" /></div></div>
      <div class="form-row"><div class="form-field"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="180" /></div><div class="form-field"><label for="telephone">Téléphone</label><input id="telephone" name="telephone" type="tel" autocomplete="tel" maxlength="30" /></div></div>
      <div class="form-field"><label for="sujet">Votre demande *</label><select id="sujet" name="sujet" required><option value="" selected disabled>Choisir un sujet</option><option>Fabrication de sacs plastiques</option><option>Broyage et recyclage</option><option>Autre demande</option></select></div>
      <div class="form-field"><label for="message">Message *</label><textarea id="message" name="message" rows="6" required minlength="10" maxlength="3000" placeholder="Précisez votre projet, les quantités ou la matière concernée..."></textarea></div>
      <button class="button button-dark" type="submit">Envoyer mon message <span aria-hidden="true">↗</span></button>
    </form>
  </div>
  <aside class="contact-page-aside"><h3>Nos coordonnées</h3><div class="contact-fact"><span>ADRESSE</span><p>10 Rue Ben Badis, Bordj Ghedir 34004<br />Bordj Bou Arréridj, Algérie</p><a href="https://www.google.com/maps/search/?api=1&amp;query=Farah+Plast+Merrouche+Bordj+Ghedir" target="_blank" rel="noopener noreferrer">Voir sur la carte ↗</a></div><div class="contact-fact"><span>TÉLÉPHONE</span><p><a href="tel:+21335206729">035 20 67 29</a><br /><a href="tel:+213552439760">0552 43 97 60</a><br /><a href="tel:+213779384252">0779 38 42 52</a></p></div><div class="contact-fact"><span>E-MAIL</span><p><a href="mailto:farahplastmerrouche@gmail.com">farahplastmerrouche@gmail.com</a><br /><a href="mailto:merroucheadel22@gmail.com">merroucheadel22@gmail.com</a></p></div><div class="contact-fact"><span>HORAIRES</span><p>Samedi — jeudi · 6h à 18h</p></div></aside>
</div></section>'''

thanks = '''<section class="thankyou"><div class="container"><div class="eyebrow"><span class="eyebrow-line"></span>CONTACT</div><h1>Merci pour votre <em>message.</em></h1><p>Votre demande a été transmise. Nous vous répondrons dès que possible.</p>''' + button("Retour à l'accueil", "index.html") + '</div></section>'

shell("apropos.html", "À propos", "Découvrez Farah Plast Merrouche, entreprise de fabrication et de valorisation plastique à Bordj Ghedir depuis 2011.", about)
shell("services.html", "Nos services", "Fabrication de sacs plastiques, broyage et recyclage à Bordj Ghedir. Découvrez les activités de Farah Plast Merrouche.", services)
shell("demarche.html", "Notre démarche", "De la collecte à la valorisation : découvrez la démarche de Farah Plast Merrouche autour des matières plastiques.", process)
shell("galerie.html", "Galerie", "Découvrez en images les ateliers, équipements et matières de Farah Plast Merrouche à Bordj Ghedir.", gallery)
shell("contact.html", "Contact", "Contactez Farah Plast Merrouche pour la fabrication de sacs plastiques ou la valorisation de matières plastiques.", contact)
shell("merci.html", "Merci", "Confirmation de votre message à Farah Plast Merrouche.", thanks)
