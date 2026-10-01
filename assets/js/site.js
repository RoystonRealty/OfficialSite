(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');

  function onScroll() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.classList.toggle('menu-open', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { toggle.click(); toggle.focus(); }
    });
  }

  // Enquiry form: opens WhatsApp with the details filled in. Nothing is stored.
  var form = document.getElementById('enquiry');
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('service');
    if (pre) {
      var sel = form.querySelector('#f-service');
      for (var i = 0; i < sel.options.length; i++) if (sel.options[i].value === pre) sel.selectedIndex = i;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('#f-name').value.trim();
      var phone = form.querySelector('#f-phone').value.trim();
      var service = form.querySelector('#f-service').value;
      var role = form.querySelector('#f-role').value;
      var brief = form.querySelector('#f-brief').value.trim();
      var err = form.querySelector('.form-error');
      if (!name) { err.textContent = 'Add your name so we know who we are speaking with.'; form.querySelector('#f-name').focus(); return; }
      if (!brief) { err.textContent = 'Add a line or two about your requirement.'; form.querySelector('#f-brief').focus(); return; }
      err.textContent = '';
      var lines = ['Hello Royston Realty,', '', 'Name: ' + name];
      if (phone) lines.push('Phone: ' + phone);
      lines.push('Service: ' + service, 'I am: ' + role, '', brief);
      window.open('https://wa.me/918123125757?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();

// Listings: rendered from assets/data/listings.js
(function () {
  var data = (window.LISTINGS || []).filter(function (l) { return l && l.title; });
  var lists = document.querySelectorAll('[data-listings]');
  if (!lists.length) return;
  var WA = 'https://wa.me/918123125757?text=';
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function card(l, base) {
    var msg = 'Hello Royston Realty, I\'m interested in: ' + l.title + (l.project ? ', ' + l.project : '') + (l.area ? ', ' + l.area : '') + '.';
    var img = l.photo
      ? '<img src="' + esc(base + l.photo) + '" alt="' + esc(l.title) + '" loading="lazy">'
      : '<div class="ph"><img src="' + esc(base) + 'assets/lion-cream.png" alt=""></div>';
    var specs = (l.specs || []).map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('');
    return '<li class="listing" data-type="' + esc(l.type) + '">' +
      '<div class="l-media">' + img + '<span class="l-type">' + esc(l.type) + '</span></div>' +
      '<div class="l-body"><p class="l-where">' + esc([l.project, l.area].filter(Boolean).join(', ')) + '</p>' +
      '<h3>' + esc(l.title) + '</h3><ul class="l-specs">' + specs + '</ul>' +
      '<div class="l-foot"><span class="l-price">' + esc(l.price) + '</span>' +
      (l.status ? '<span class="l-status">' + esc(l.status) + '</span>' : '') + '</div>' +
      '<a class="btn btn--ghost" href="' + WA + encodeURIComponent(msg) + '" target="_blank" rel="noopener">Enquire about this home</a></div></li>';
  }
  lists.forEach(function (ul) {
    var limit = parseInt(ul.getAttribute('data-limit') || '0', 10);
    var items = limit ? data.slice(0, limit) : data;
    ul.innerHTML = items.map(function (l) { return card(l, ul.getAttribute('data-base') || ''); }).join('');
  });
  var section = document.querySelector('[data-listings-section]');
  if (section && data.length) section.hidden = false;
  var empty = document.querySelector('[data-listings-empty]');
  if (empty && data.length) empty.classList.add('is-after');
  var filters = document.querySelector('[data-filters]');
  if (filters && data.length > 3) {
    filters.hidden = false;
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      filters.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var f = b.getAttribute('data-filter');
      document.querySelectorAll('.listing').forEach(function (li) { li.hidden = f !== 'all' && li.getAttribute('data-type') !== f; });
    });
  }
})();
