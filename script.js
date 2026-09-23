const menuButton = document.querySelector('.menu-toggle');
const mainNav = document.querySelector('.main-nav');

if (menuButton && mainNav) {
  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Ouvrir le menu' : 'Fermer le menu');
    mainNav.classList.toggle('is-open', !isOpen);
  });

  mainNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Ouvrir le menu');
      mainNav.classList.remove('is-open');
    });
  });
}

const galleryButton = document.querySelector('.gallery-more');
const extraPhotos = document.querySelectorAll('.gallery-extra');
if (galleryButton) {
  galleryButton.addEventListener('click', () => {
    const expanded = galleryButton.getAttribute('aria-expanded') === 'true';
    extraPhotos.forEach((photo) => { photo.hidden = expanded; });
    galleryButton.setAttribute('aria-expanded', String(!expanded));
    galleryButton.innerHTML = expanded
      ? 'Voir toutes les photos <span aria-hidden="true">↓</span>'
      : 'Réduire la galerie <span aria-hidden="true">↑</span>';
  });
}

const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();
