---
layout: page
title: "Search"
permalink: /search/
description: "Search every article on Beer, Wine, Whiskey & AI — beer, wine, whiskey, AI, data science, and the production process."
---

Search across every article — by title, topic tag, or summary.

<input type="search" id="search-input" class="search-box" placeholder="Search articles… e.g. fermentation, Power BI, cask" autocomplete="off" autofocus aria-label="Search articles">
<p id="search-status" class="search-status" role="status" aria-live="polite"></p>
<ul id="search-results" class="posts"></ul>

<script>
(function () {
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var status = document.getElementById('search-status');
  var data = [];
  function esc(s){ return (s||'').replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function render(items, q) {
    results.innerHTML = '';
    if (!q) { status.textContent = ''; return; }
    if (!items.length) { status.textContent = 'No articles match “' + q + '”.'; return; }
    status.textContent = items.length + ' result' + (items.length > 1 ? 's' : '') + ' for “' + q + '”';
    items.forEach(function (p) {
      var li = document.createElement('li');
      li.className = 'post-item';
      li.innerHTML = '<a class="post-link" href="' + p.url + '">' + esc(p.title) + '</a>' +
        '<time>' + esc(p.date) + '</time>' +
        (p.description ? '<p class="post-excerpt">' + esc(p.description) + '</p>' : '');
      results.appendChild(li);
    });
  }
  function run(q) {
    q = (q || '').trim().toLowerCase();
    if (!q) { render([], ''); return; }
    var hits = data.filter(function (p) {
      return ((p.title || '') + ' ' + (p.tags || '') + ' ' + (p.description || '')).toLowerCase().indexOf(q) > -1;
    });
    render(hits, q);
  }
  fetch('{{ "/search.json" | relative_url }}')
    .then(function (r) { return r.json(); })
    .then(function (j) {
      data = j;
      var q = new URLSearchParams(location.search).get('q');
      if (q) { input.value = q; run(q); }
    })
    .catch(function () { status.textContent = 'Search index could not load.'; });
  input.addEventListener('input', function () { run(input.value); });
})();
</script>
