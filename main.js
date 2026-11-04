(function(){
  var D = window.TA_DATA; D.awards = 8;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function fmt(el,v){var dec=el.dataset.dec?+el.dataset.dec:2; el.textContent = (el.dataset.dec ? Math.round(v).toLocaleString('en-US') : D.peso(v,dec));}
  function count(el){var target=D[el.dataset.count]; if(reduce){fmt(el,target);return;}
    var t0=performance.now(),dur=1600;(function step(t){var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);fmt(el,p<1?target*e:target);if(p<1)requestAnimationFrame(step);})(t0);}
  var max=Math.max(D.main2025,D.main2026ytd);
  function bar(el){el.style.width=(D[el.dataset.w]/max*100).toFixed(1)+'%';}
  document.querySelectorAll('[data-count]').forEach(function(el){el.dataset.done='';});
  function show(el){el.classList.add('in');
    el.querySelectorAll('[data-count]').forEach(function(c){if(!c.dataset.done){c.dataset.done=1;count(c);}});
    if(el.matches('[data-count]')&&!el.dataset.done){el.dataset.done=1;count(el);}
    el.querySelectorAll('[data-w]').forEach(bar);}
  var els=document.querySelectorAll('.rv, .stat');
  if(!('IntersectionObserver' in window)||reduce){els.forEach(show);}
  else{var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){show(e.target);io.unobserve(e.target);}});},{threshold:.15,rootMargin:'0px 0px -5% 0px'});els.forEach(function(el){io.observe(el);});}
  window.__revealAll=function(){els.forEach(show);};
  var f=document.getElementById('inq'); f.addEventListener('submit',function(ev){ev.preventDefault();
    document.getElementById('formmsg').textContent='Nothing was sent: the online form is not connected yet. Please use the owner contact above.';});
})();
