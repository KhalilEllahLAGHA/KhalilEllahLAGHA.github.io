(() => {
  'use strict';
  const root = document.documentElement;
  const viewers = document.querySelectorAll('[data-project-views]');

  function localiseImage(panel, loadImage) {
    const img = panel.querySelector('img');
    if (!img) return;
    const lang = root.lang === 'en' ? 'en' : 'fr';
    const file = img.getAttribute('data-source-' + lang) || img.dataset.file;
    img.alt = img.getAttribute('data-figure-alt-' + lang);
    if (file && loadImage && img.getAttribute('src') !== file) img.src = file;
    const link = panel.querySelector('.view-image');
    if (file && link.dataset.figureLink !== 'card') link.href = file;
  }

  function updateLanguage() {
    viewers.forEach(viewer => {
      viewer.querySelector('[data-views-group]').setAttribute('aria-label',
        root.lang === 'en' ? 'Project views' : 'Vues du projet');
      viewer.querySelectorAll('.view-panel').forEach(panel => localiseImage(panel, !panel.hidden));
    });
  }

  viewers.forEach(viewer => {
    const group = viewer.querySelector('[data-views-group]');
    const buttons = Array.from(group.querySelectorAll('button'));
    for (const button of buttons) {
      button.addEventListener('click', () => {
        if (button.getAttribute('aria-pressed') === 'true') return;
        for (const choice of buttons) {
          const active = choice === button;
          const panel = document.getElementById(choice.getAttribute('aria-controls'));
          if (active) localiseImage(panel, true);
          const video = panel.querySelector('video');
          if (video && active && !video.hasAttribute('src')) {
            video.poster = video.dataset.poster;
            video.src = video.dataset.movie;
          }
          if (video && !active) video.pause();
          panel.hidden = !active;
          panel.classList.toggle('is-entering', active);
          choice.setAttribute('aria-pressed', String(active));
        }
      });
    }
    group.hidden = false;
  });
  updateLanguage();
  new MutationObserver(updateLanguage).observe(root, { attributes: true, attributeFilter: ['lang'] });
  // Filtering out a playing project also hides its native pause control.
  document.querySelectorAll('.project-card .view-movie').forEach(video => {
    const card = video.closest('.project-card');
    new MutationObserver(() => {
      if (card.hidden) video.pause();
    }).observe(card, { attributes: true, attributeFilter: ['hidden'] });
  });
})();
