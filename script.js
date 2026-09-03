// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Count-up numbers, triggered when they scroll into view.
  // Respects reduced-motion: shows the final value immediately.
  var nums = document.querySelectorAll('[data-count]');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!nums.length) return;

  if (reduce || !('IntersectionObserver' in window)) {
    nums.forEach(function (el) { el.textContent = fmt(el.dataset.count) + (el.dataset.suffix || ''); });
    return;
  }

  function fmt(n) { return Number(n).toLocaleString('en-US'); }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      io.unobserve(el);
      var target = parseInt(el.dataset.count, 10);
      var suffix = el.dataset.suffix || '';
      var start = performance.now();
      var dur = 1200;
      function step(now) {
        var p = Math.min((now - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(Math.round(target * eased)) + suffix;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }, { threshold: 0.4 });

  nums.forEach(function (el) { el.textContent = '0' + (el.dataset.suffix || ''); io.observe(el); });
});
