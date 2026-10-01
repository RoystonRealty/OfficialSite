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
