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
      if ((m = q.match(/^P(\d{6})\.(\d+)$/i)) && D.notebook && D.pages[+m[1]] != null)
        return base + 'notebook/' + D.pages[+m[1]][1] + '/#P' + m[1] + '.' + m[2];
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
      /* not a reference: search for it */
      location.href = u || (BASE + LANG + '/search/?q=' + encodeURIComponent(q));
    }, function () { if (msg) msg.textContent = msg.dataset.nf; });
  });

  /* typeset formulas in content added after load */
  function typeset(el) {
    if (window.MathJax && MathJax.typesetPromise) return MathJax.typesetPromise([el]).catch(function () {});
    return Promise.resolve();
  }
  var SHARDS = {};
  function shard(L, p) {
    var k = L + '/' + p;
    if (!SHARDS[k]) SHARDS[k] = fetch(BASE + 'data/pages/' + k + '.json').then(function (r) {
      if (!r.ok) throw new Error(r.status); return r.json(); });
    return SHARDS[k];
  }
  /* talk pages: the text of a notebook page, loaded when its box is opened */
  document.querySelectorAll('details.nbload').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open || d.dataset.done) return;
      d.dataset.done = '1';
      var box = d.querySelector('.nbtext'), m = d.dataset.src.match(/pages\/(ru|en)\/(P\d{6})\.json$/);
      shard(m[1], m[2]).then(function (j) { box.innerHTML = j.html; typeset(box); },
        function () { delete d.dataset.done; });
    });
  });
  /* notebook pages: this language, the other language, or both side by side aligned passage by passage */
  var modes = document.querySelector('.nbmodes');
  function segs(el) {
    var out = [], cur = [];
    Array.prototype.forEach.call(el.childNodes, function (ch) {
      if (ch.nodeType === 1 && ch.classList.contains('passage')) {
        if (cur.length) out.push({p: false, nodes: cur});
        out.push({p: true, key: ch.dataset.n + (ch.classList.contains('cont') ? 'c' : ''), nodes: [ch]});
        cur = [];
      } else if (ch.nodeType === 1 || (ch.nodeType === 3 && ch.textContent.trim())) cur.push(ch);
    });
    if (cur.length) out.push({p: false, nodes: cur});
    return out;
  }
  function rows(a, b) {
    var pos = {}, out = [], ia = 0, ib = 0;
    b.forEach(function (s, i) { if (s.p && pos[s.key] == null) pos[s.key] = i; });
    for (var i = 0; i < a.length; i++) {
      if (!a[i].p || pos[a[i].key] == null || pos[a[i].key] < ib) continue;
      var j = pos[a[i].key];
      out.push([a.slice(ia, i + 1), b.slice(ib, j + 1)]);
      ia = i + 1; ib = j + 1;
    }
    out.push([a.slice(ia), b.slice(ib)]);
    return out;
  }
  function cell(list, L, clone) {
    var c = document.createElement('div'); c.className = 'nbcell'; c.lang = L;
    list.forEach(function (s) { s.nodes.forEach(function (n) { c.appendChild(clone ? n.cloneNode(true) : n); }); });
    return c;
  }
  if (modes) {
    var OTHER = modes.dataset.other, secs = document.querySelectorAll('section.nbp');
    var otherBox = function (sec) {
      var o = sec.querySelector('.nbother');
      if (!o) { o = document.createElement('div'); o.className = 'nbtext nbother'; o.lang = OTHER; o.hidden = true;
        o.textContent = modes.dataset.loading; sec.appendChild(o); }
      return o;
    };
    var loadOther = function (sec) {
      var o = otherBox(sec);
      if (o.dataset.done) return Promise.resolve(o);
      return shard(OTHER, sec.dataset.p).then(function (j) {
        o.innerHTML = j.html; o.dataset.done = '1';
        /* the anchors stay with this language's text */
        o.querySelectorAll('[id]').forEach(function (e) { e.dataset.id = e.id; e.removeAttribute('id'); });
        return o;
      });
    };
    /* the side-by-side view moves this language's blocks into its rows; they go back for the other views */
    var restore = function (sec, mine) {
      var b = sec.querySelector('.nbboth');
      if (b) b.remove();
      if (sec._orig) sec._orig.forEach(function (n) { mine.appendChild(n); });
    };
    var show = function (sec, mode) {
      var mine = sec.querySelector('.nbtext:not(.nbother)');
      if (mode === 'this') { restore(sec, mine); mine.hidden = false; otherBox(sec).hidden = true; return; }
      loadOther(sec).then(function (o) {
        if (document.body.dataset.nbmode !== mode) return;
        restore(sec, mine);
        mine.hidden = true;
        if (mode === 'other') { o.hidden = false; typeset(o); return; }
        o.hidden = true;
        sec._orig = sec._orig || Array.prototype.slice.call(mine.childNodes);
        var both = document.createElement('div'); both.className = 'nbboth';
        rows(segs(mine), segs(o)).forEach(function (r) {
          if (!r[0].length && !r[1].length) return;
          var row = document.createElement('div'); row.className = 'nbrow';
          row.appendChild(cell(r[0], document.body.dataset.lang, false)); row.appendChild(cell(r[1], OTHER, true));
          both.appendChild(row);
        });
        sec.appendChild(both);
        typeset(both);
      }, function () { otherBox(sec).textContent = modes.dataset.loading + ' ✗'; });
    };
    var setMode = function (mode) {
      document.body.dataset.nbmode = mode;
      modes.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.mode === mode); });
      try { localStorage.setItem('nbmode', mode); } catch (e) {}
      if (mode === 'this') { secs.forEach(function (s) { show(s, mode); }); return; }
      /* the pages near the view first, then the rest */
      var near = [], far = [];
      secs.forEach(function (s) { var r = s.getBoundingClientRect();
        (r.bottom > -2 * innerHeight && r.top < 3 * innerHeight ? near : far).push(s); });
      near.forEach(function (s) { show(s, mode); });
      setTimeout(function () { far.forEach(function (s) { show(s, mode); }); }, 400);
    };
    modes.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-mode]'); if (b) setMode(b.dataset.mode);
    });
    var saved = null; try { saved = localStorage.getItem('nbmode'); } catch (e) {}
    if (saved === 'other' || saved === 'both') setMode(saved);
  }
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
