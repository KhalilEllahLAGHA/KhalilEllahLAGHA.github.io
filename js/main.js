/* Khalil LAGHA — Portfolio · vanilla JS
   i18n FR/EN · theme toggle · mobile nav · scroll reveal · scrollspy */
(function () {
  'use strict';

  var d = document;
  var root = d.documentElement;

  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { } }
  };

  /* ==================== i18n ==================== */

  var TITLES = {
    fr: 'Khalil LAGHA — Étudiant M2 CSEE | Électronique de puissance & énergie',
    en: 'Khalil LAGHA — M2 Electrical Energy Systems Design | Power electronics'
  };

  var EN = {
    'skip': 'Skip to content',
    'nav.home': 'Home', 'nav.about': 'About', 'nav.edu': 'Education', 'nav.exp': 'Experience',
    'nav.proj': 'Projects', 'nav.skills': 'Skills', 'nav.docs': 'Documents', 'nav.contact': 'Contact',
    'hero.kicker': 'Work-study from September 2026 · Final-year internship 2027',
    'hero.tagline': 'M2 student in Electrical Energy Systems Design — power electronics & energy conversion',
    'hero.subline': 'Looking for a work-study contract (alternance) starting September 2026 (2–3 weeks company / university rotation) or a final-year internship in spring–summer 2027.',
    'chip1': 'Power electronics', 'chip2': 'EV / powertrain', 'chip3': 'Electrical grids', 'chip4': 'AI applied to power systems',
    'cta.contact': 'Contact me',
    'cta.cv': 'Download my CV',
    'cta.cvshort': 'My CV',
    'cta.cvats': 'Also available:',
    'cta.cvats2': 'ATS version of my CV (plain single-column layout, for online applications)',
    'hero.work': 'Authorized to work in France',
    'about.title': 'About',
    'about.p1': 'M2 student in CSEE (Electrical Energy Systems Design) at Université Grenoble Alpes, passionate about power electronics and energy conversion. Trained in the Electrical Engineering programme of École Nationale Polytechnique d\'Alger, ranked 2nd of the M1 EEA cohort at UGA (annual average 15,43/20). My experience covers PEMFC fuel-cell modelling (GIPSA-lab), industrial converters and automation (EURL Lagha) and power grids (Sonelgaz).',
    'about.p2': 'I am looking for a work-study contract from September 2026 or a final-year internship (spring–summer 2027) in power electronics, EV / powertrain, electrical grids or AI applied to power systems.',
    'stat1v': '2nd', 'stat1l': 'of the M1 EEA cohort (UGA)', 'stat2l': 'M1 annual average', 'stat3l': 'English',
    'edu.title': 'Education',
    'e1.h': 'M2 CSEE — Electrical Energy Systems Design', 'e1.badge': 'Admitted',
    'e2.p': 'Ranked 2nd of the cohort · annual average 15,43/20.',
    'e3.h': 'Engineering programme in Electrical Engineering',
    'e3.p': '4 of 5 years completed (left to pursue a master\'s in France) · preparatory classes: among the top-ranked students.',
    'e4.h': 'Baccalauréat in Mathematics', 'e4.p': 'Highest honours (mention Très Bien) — 16,93/20.',
    'exp.title': 'Experience',
    'x1.date': '04 → 07/2026 · 3.5 months', 'x1.role': 'Research Intern',
    'x1.p1': 'Matlab/Simulink model of a PEMFC fuel cell — 6 % error (dynamic) / 1 % (static).',
    'x1.p2': 'Voltage regulation with a DC-DC boost converter + PI controller, in simulation then on real hardware.',
    'x2.date': '2025 · 1 month', 'x2.role': 'Intern',
    'x2.p1': 'International industrial immersion · technical summaries (directional drilling) · NEST & SIPP Level 2 HSE certifications.',
    'x2.t2': 'International',
    'x2.cert': 'NEST & SIPP HSE certificate',
    'x3.date': '2024 · 15 days + 1 month', 'x3.role': 'Power Electronics & Automation Intern',
    'x3.p1': 'Industrial DC-DC buck converter, 50 V → 0–48 V, 25 A.',
    'x3.p2': '4 transformer-rectifiers for pipelines (electrolysis) — 400 V three-phase → 100 V, rectification + filtering, 100 V DC / 80 A output (≈ 8 kW), ripple < 5 %.',
    'x3.p3': 'Supervision HMI in Siemens TIA Portal · EPLAN schematics.',
    'x3.cert1': 'Internship certificate — 01/2024',
    'x3.cert2': 'Internship certificate — 09/2024',
    'x4.date': '2024 · 15 days · observation', 'x4.role': 'Power Grid Intern',
    'x4.p1': 'Substation structure and the full generation → distribution chain (400/220 kV → 60 kV → 30/10 kV → 400/230 V) · visit of an MV/LV substation.',
    'x4.report': 'Internship report — power grids',
    'x4.cert': 'Internship certificate',
    'proj.title': 'Projects', 'proj.flag': 'Flagship project',
    'p1.meta': 'Matlab · solo', 'p1.h': 'Power grid analysis',
    'p1.p': 'Load flow from 3 to 118 buses (PQ/PV/slack) · comparison of 3 methods (accuracy vs computation time) · transient stability.',
    'p1.t3': 'Transient stability',
    'p1.r2': 'Project report',
    'repo.soon': '· soon',
    'repo.soon2': 'soon',
    'files.label': 'View the files',
    'p2.meta': 'Python · PyQt', 'p2.h': 'Winding and flux analysis program',
    'p2.p': 'PyQt app: three-phase winding, tooth-based MMF profiles, reluctance-network flux density, FEMM validation.',
    'p2.t2': 'Reluctance networks',
    'p3.h': 'Field-oriented control (FOC) — induction motor',
    'p3.p': 'Park transforms, PID controllers, observers.',
    'p6.h': 'Cascade control of a DC motor',
    'p6.p': 'Voltage control through a three-phase thyristor bridge · outer speed loop, inner current loop.',
    'p6.t1': 'DC motor',
    'p4.h': 'Siemens Step7 automation', 'p4.p': 'HMI + Ladder program for a machine cycle (simulation).',
    'p5.h': 'Line-follower robot',
    'p5.p': 'Design and programming · Poly Maze competition (4th edition, VIC — ENP, 07/2024), team OPTIMUM.',
    'p5.t3': 'Competition',
    'p5.cert': 'Participation certificate',
    'p7.meta': 'ENP · Lab reports',
    'p7.h': 'Power electronics lab work',
    'p7.p': 'Three-phase diode rectification, single-phase semi-controlled bridge, smoothing and commutation overlap — bench measurements, theoretical analysis and Matlab/Simulink simulations.',
    'p7.t1': 'Rectification',
    'p7.r1': 'Three-phase diode rectifier',
    'p7.r2': 'Single-phase semi-controlled bridge',
    'p7.r3': 'Smoothing and commutation',
    'p8.h': 'Neural network from scratch (MLP)',
    'p8.p': 'Multilayer perceptron and gradient backpropagation hand-coded in Matlab, no toolbox — two implementations: didactic loops and vectorised matrix computation.',
    'p8.t1': 'Backpropagation',
    'p8.t2': 'Neural networks',
    'skills.title': 'Skills',
    'sk.d1': 'Power conversion (all types)',
    'sk.d2': 'Power conversion for the electrical grid',
    'sk.d3': 'Power electronics for machine control',
    'sk.d4': 'Electrical machines & transformers',
    'sk.d5': 'Power system analysis, transient stability',
    'sk.d6': 'Control engineering',
    'sk.d7': 'Industrial automation (PLC, HMI/SCADA)',
    'sk.d8': 'AI (neural networks, genetic algorithms, fuzzy logic)',
    'sk.sw': 'Software', 'sk.lc': 'Languages & certification',
    'sk.fr': 'French', 'sk.en': 'English', 'sk.ar': 'Arabic', 'sk.arlvl': 'native',
    'sk.cert': 'Certification: SLB NEST & SIPP Level 2 — 07/2025, HSE.',
    'sk.assoc': 'Student involvement',
    'docs.title': 'Documents',
    'docs.intro': 'Academic transcript and recommendation letters.',
    'docs.transcript.h': 'Academic transcript',
    'docs.transcript.p': 'Baccalauréat, preparatory classes and engineering programme — École Nationale Polytechnique d\'Alger.',
    'docs.rec1.h': 'Recommendation letter — Dr Y. Benmahamed',
    'docs.rec1.p': 'Electrical Engineering Research Laboratory, ENP Algiers.',
    'docs.rec2.h': 'Recommendation letter — I. Saadaoui',
    'docs.rec2.p': 'Head of department, preparatory classes, ENP Algiers.',
    'contact.title': 'Contact',
    'contact.pitch': 'A work-study or internship opportunity in power electronics, EV / powertrain, electrical grids or AI applied to energy? Get in touch.',
    'contact.mail': 'Email me'
  };

  var EN_ARIA = { 'aria.nav': 'Main navigation', 'aria.menu': 'Menu', 'aria.chips': 'Areas of interest', 'aria.scroll': 'Scroll to About', 'aria.top': 'Back to top' };

  /* Capture French strings from the DOM so we can switch back. */
  var FR = {}, FR_ARIA = {};
  var i18nEls = d.querySelectorAll('[data-i18n]');
  var ariaEls = d.querySelectorAll('[data-i18n-aria]');
  i18nEls.forEach(function (el) {
    var k = el.getAttribute('data-i18n');
    if (!(k in FR)) { FR[k] = el.textContent; }
  });
  ariaEls.forEach(function (el) {
    var k = el.getAttribute('data-i18n-aria');
    if (!(k in FR_ARIA)) { FR_ARIA[k] = el.getAttribute('aria-label'); }
  });

  var DICT = { fr: FR, en: EN };
  var DICT_ARIA = { fr: FR_ARIA, en: EN_ARIA };

  function setLang(lang) {
    var dict = DICT[lang], aria = DICT_ARIA[lang];
    i18nEls.forEach(function (el) {
      var s = dict[el.getAttribute('data-i18n')];
      if (s != null) { el.textContent = s; }
    });
    ariaEls.forEach(function (el) {
      var s = aria[el.getAttribute('data-i18n-aria')];
      if (s != null) { el.setAttribute('aria-label', s); }
    });
    root.lang = lang;
    d.title = TITLES[lang];
    /* Both CV types download in the language currently displayed. */
    d.querySelectorAll('.js-cv-design').forEach(function (a) {
      a.setAttribute('href', lang === 'fr' ? 'cv/CV_Khalil_LAGHA_FR.pdf' : 'cv/CV_Khalil_LAGHA_EN.pdf');
    });
    d.querySelectorAll('.js-cv-ats').forEach(function (a) {
      a.setAttribute('href', lang === 'fr' ? 'cv/CV_Khalil_LAGHA_ATS_FR.pdf' : 'cv/CV_Khalil_LAGHA_ATS_EN.pdf');
    });
    d.querySelectorAll('.lang-toggle').forEach(function (b) {
      b.textContent = lang === 'fr' ? 'EN' : 'FR';
      b.setAttribute('aria-label', lang === 'fr' ? 'Switch to English' : 'Passer en français');
    });
    store.set('kl-lang', lang);
    applyThemeLabels();
  }

  d.querySelectorAll('.lang-toggle').forEach(function (b) {
    b.addEventListener('click', function () {
      setLang(root.lang === 'fr' ? 'en' : 'fr');
    });
  });

  /* ==================== Theme ==================== */

  var THEME_LABELS = {
    fr: { toLight: 'Basculer en thème clair', toDark: 'Basculer en thème sombre' },
    en: { toLight: 'Switch to light theme', toDark: 'Switch to dark theme' }
  };

  function applyThemeLabels() {
    var t = root.dataset.theme || 'dark';
    var L = THEME_LABELS[root.lang === 'en' ? 'en' : 'fr'];
    d.querySelectorAll('.theme-toggle').forEach(function (b) {
      b.setAttribute('aria-label', t === 'dark' ? L.toLight : L.toDark);
      b.setAttribute('aria-pressed', String(t === 'dark'));
    });
  }

  function setTheme(t) {
    root.dataset.theme = t;
    store.set('kl-theme', t);
    applyThemeLabels();
  }

  d.querySelectorAll('.theme-toggle').forEach(function (b) {
    b.addEventListener('click', function () {
      setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    });
  });

  /* ==================== Mobile nav ==================== */

  var burger = d.querySelector('.burger');
  var nav = d.getElementById('site-nav');

  function closeNav() {
    nav.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
  }

  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { closeNav(); }
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeNav(); }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 768) { closeNav(); }
    });
  }

  /* ==================== Scroll reveal ==================== */

  var reduced = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revealEls = d.querySelectorAll('.reveal');

  if (reduced || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ==================== Scrollspy ==================== */

  var navLinks = {};
  d.querySelectorAll('.nav a[href^="#"]').forEach(function (a) {
    navLinks[a.getAttribute('href').slice(1)] = a;
  });
  var sections = d.querySelectorAll('main section[id]');

  if ('IntersectionObserver' in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          Object.keys(navLinks).forEach(function (id) {
            navLinks[id].removeAttribute('aria-current');
          });
          var link = navLinks[entry.target.id];
          if (link) { link.setAttribute('aria-current', 'true'); }
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ==================== Scroll progress + back to top ==================== */

  var progress = d.querySelector('.scroll-progress span');
  var toTop = d.querySelector('.to-top');
  var ticking = false;

  function onScroll() {
    if (ticking) { return; }
    ticking = true;
    requestAnimationFrame(function () {
      var doc = d.documentElement;
      var max = doc.scrollHeight - doc.clientHeight;
      var y = window.scrollY || doc.scrollTop || 0;
      if (progress) { progress.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')'; }
      if (toTop) { toTop.classList.toggle('show', y > 600); }
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ==================== Card spotlight ==================== */

  if (!reduced && window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    d.querySelectorAll('.card').forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  /* ==================== Staggered reveals ==================== */

  ['.cards', '.stat-cards', '.skill-grid', '.timeline'].forEach(function (sel) {
    d.querySelectorAll(sel).forEach(function (group) {
      for (var i = 0; i < group.children.length; i++) {
        group.children[i].style.setProperty('--rd', Math.min(i, 7) * 70 + 'ms');
      }
    });
  });

  /* ==================== Misc ==================== */

  var yearEl = d.getElementById('year');
  if (yearEl) { yearEl.textContent = String(new Date().getFullYear()); }

  /* ==================== Init ==================== */

  var savedLang = store.get('kl-lang');
  if (savedLang === 'en') { setLang('en'); } else { applyThemeLabels(); }
})();
