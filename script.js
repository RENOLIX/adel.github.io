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

const roadmaps = document.querySelectorAll('[data-roadmap]');
if (roadmaps.length) {
  let framePending = false;
  const updateRoadmaps = () => {
    roadmaps.forEach((roadmap) => {
      const path = roadmap.querySelector('.roadmap-path');
      const ball = roadmap.querySelector('.roadmap-ball');
      if (!path) return;
      const length = path.getTotalLength();
      const bounds = roadmap.getBoundingClientRect();
      const start = window.innerHeight / 2;
      const distance = Math.max(1, bounds.height - start);
      const progress = Math.max(0, Math.min(1, (start - bounds.top) / distance));
      path.style.strokeDasharray = String(length);
      path.style.strokeDashoffset = String(length * (1 - progress));
      if (ball) ball.style.opacity = progress > 0 && progress < 1 ? '0' : '1';
    });
    framePending = false;
  };
  const scheduleRoadmapUpdate = () => {
    if (framePending) return;
    framePending = true;
    window.requestAnimationFrame(updateRoadmaps);
  };
  updateRoadmaps();
  window.addEventListener('scroll', scheduleRoadmapUpdate, { passive: true });
  window.addEventListener('resize', scheduleRoadmapUpdate);
}
