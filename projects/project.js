(function(){'use strict';
  var root=document.documentElement;
  function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function set(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function applyLanguage(lang){
    root.lang=lang;
    document.querySelectorAll('.lang-toggle').forEach(function(b){b.textContent=lang==='fr'?'EN':'FR';b.setAttribute('aria-label',lang==='fr'?'Switch to English':'Passer en français')});
    document.querySelectorAll('[data-alt-fr]').forEach(function(img){img.alt=img.getAttribute(lang==='fr'?'data-alt-fr':'data-alt-en')||img.alt});
    document.querySelectorAll('.report-link').forEach(function(a){var url=a.getAttribute(lang==='fr'?'data-fr':'data-en');if(url)a.href=url});
    var title=document.querySelector('h1');if(title)document.title=(title.querySelector('[lang='+lang+']')||title).textContent+' — '+(lang==='fr'?'Lagha Khalil':'Khalil Lagha');
    document.querySelectorAll('[data-label-fr]').forEach(function(el){el.setAttribute('aria-label',el.getAttribute(lang==='fr'?'data-label-fr':'data-label-en'))});
    set('kl-lang',lang);updateThemeLabel();
  }
  function updateThemeLabel(){var b=document.querySelector('.theme-toggle');if(!b)return;var light=root.dataset.theme==='light',fr=root.lang!=='en';b.setAttribute('aria-label',fr?(light?'Passer au thème sombre':'Passer au thème clair'):(light?'Switch to dark theme':'Switch to light theme'));b.setAttribute('aria-pressed',String(!light));}
  var theme=get('kl-theme')||(window.matchMedia&&matchMedia('(prefers-color-scheme: light)').matches?'light':'dark');root.dataset.theme=theme;
  document.querySelectorAll('.lang-toggle').forEach(function(b){b.addEventListener('click',function(){applyLanguage(root.lang==='fr'?'en':'fr')})});
  document.querySelectorAll('.theme-toggle').forEach(function(b){b.addEventListener('click',function(){root.dataset.theme=root.dataset.theme==='light'?'dark':'light';set('kl-theme',root.dataset.theme);updateThemeLabel()})});
  applyLanguage(get('kl-lang')==='en'?'en':'fr');
  var progress=document.querySelector('.progress');
  function onScroll(){if(!progress)return;var span=document.documentElement.scrollHeight-innerHeight;progress.style.transform='scaleX('+Math.max(0,Math.min(1,span>0?scrollY/span:0))+')'}
  addEventListener('scroll',onScroll,{passive:true});addEventListener('resize',onScroll);onScroll();
  if('IntersectionObserver'in window){
    var nav=new Map();document.querySelectorAll('.chapter-nav a').forEach(function(a){nav.set(a.getAttribute('href').slice(1),a)});
    var obs=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting){nav.forEach(function(a){a.removeAttribute('aria-current')});var a=nav.get(entry.target.id);if(a)a.setAttribute('aria-current','true')}})},{rootMargin:'-25% 0px -65% 0px'});
    document.querySelectorAll('.chapter[id]').forEach(function(el){obs.observe(el)});
  }
})();
