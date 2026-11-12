/* The Gelfand seminar site: theme toggle, reference box, opening the views of an item named in the address. */
(function () {
  var B = document.body, BASE = B.dataset.base, LANG = B.dataset.lang || 'en';
  try { var t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
  var tb = document.getElementById('theme-toggle');
  if (tb) tb.addEventListener('click', function () {
    var cur = document.documentElement.dataset.theme ||
      (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var nx = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = nx;
    try { localStorage.setItem('theme', nx); } catch (e) {}
  });
  try { if (LANG === 'ru' || LANG === 'en') localStorage.setItem('lang', LANG); } catch (e) {}

  var RES = null;
  function data() {
    if (RES) return Promise.resolve(RES);
    return fetch(BASE + 'data/resolve.json').then(function (r) { return r.json(); }).then(function (d) { RES = d; return d; });
  }
  /* Resolve a reference string to a page address in language L: record 398, item 1976-398.5, problem GP-1976-01,
     notebook page P000659, academic year 1976-77, date 1976-09-06. */
  function resolve(q, L) {
    q = (q || '').trim().replace(/^GELFAND-/i, '');
    return data().then(function (D) {
      var m, base = BASE + L + '/';
      if (/^\d{1,3}$/.test(q) && D.records.indexOf(+q) >= 0) return base + 'talks/' + (+q) + '/';
      if ((m = q.match(/^(\d{4})-(\d+)\.(\d+)$/)) && D.items[q] != null) return base + 'talks/' + D.items[q] + '/#' + q;
      if ((m = q.match(/^GP-\d{4}-\d+$/i)) && D.problems.indexOf(q.toUpperCase()) >= 0) return base + 'problems/' + q.toUpperCase() + '/';
      if ((m = q.match(/^P?(\d{1,6})$/i)) && /^P/i.test(q) || /^\d{6}$/.test(q)) {
        var n = +(q.replace(/^P/i, ''));
        if (D.pages[n] != null) return (D.notebook ? base + 'notebook/' + D.pages[n][1] + '/' : base + 'talks/' + D.pages[n][0] + '/') + '#P' + ('00000' + n).slice(-6);
      }
      if ((m = q.match(/^(\d{4})[-–](\d{2})$/)) && D.years.indexOf(m[1] + '-' + m[2]) >= 0) return base + 'years/' + m[1] + '-' + m[2] + '/';
      if ((m = q.match(/^(\d{4}-\d{2}-\d{2})$/)) && D.dates[q]) return base + 'talks/' + D.dates[q][0] + '/';
      if (q.length > 2) {
        var k = q.toLowerCase().replace(/[^a-zа-яё]/g, '');
        for (var s in D.speakers) if (s.indexOf(k) >= 0) return base + 'speakers/#' + D.speakers[s];
      }
      return null;
    });
  }
  window.GelfandResolve = resolve;
  var f = document.getElementById('refbox');
  if (f) f.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var q = f.querySelector('input').value, msg = f.querySelector('.refmsg');
    resolve(q, LANG).then(function (u) {
      if (u) location.href = u; else if (msg) msg.textContent = msg.dataset.nf;
    }, function () { if (msg) msg.textContent = msg.dataset.nf; });
  });
  /* open the views of the item named in the hash */
  function openHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var el = document.getElementById(id);
    if (el && el.classList.contains('item')) {
      var d = el.querySelectorAll('details.view');
      for (var i = 0; i < d.length; i++) d[i].open = true;
    }
    if (el && el.tagName === 'DETAILS') el.open = true;
  }
  window.addEventListener('hashchange', openHash);
  openHash();
})();
