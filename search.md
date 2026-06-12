---
layout: page
title: "Search"
permalink: /search/
description: "Search every article on Beer, Wine, Whiskey & AI — production science, AI, data platforms, generative AI, IoT, sustainability, sales and finance."
---

Search across every article — by title, topic tag, summary or text.

<input type="search" id="search-input" class="search-box" placeholder="Search articles… e.g. fermentation, Power BI, cask, Microsoft Fabric" autocomplete="off" autofocus aria-label="Search articles">
<p id="search-status" class="search-status" role="status" aria-live="polite"></p>

<p class="search-chips" style="margin:.4rem 0 1rem">Try:
  <a class="tag" href="?q=fermentation">fermentation</a>
  <a class="tag" href="?q=machine learning">machine learning</a>
  <a class="tag" href="?q=generative AI">generative AI</a>
  <a class="tag" href="?q=vibe coding">vibe coding</a>
  <a class="tag" href="?q=Fable 5">Fable 5</a>
  <a class="tag" href="?q=Claude">Claude</a>
  <a class="tag" href="?q=Power BI">Power BI</a>
  <a class="tag" href="?q=process intelligence">process intelligence</a>
  <a class="tag" href="?q=Microsoft Fabric">Microsoft Fabric</a>
  <a class="tag" href="?q=Databricks">Databricks</a>
  <a class="tag" href="?q=Snowflake">Snowflake</a>
  <a class="tag" href="?q=learning AI">learning AI</a>
  <a class="tag" href="?q=IoT">IoT</a>
  <a class="tag" href="?q=sustainability">sustainability</a>
  <a class="tag" href="?q=angel's share">angel's share</a>
  <a class="tag" href="?q=cask">cask</a>
  <a class="tag" href="?q=ABV">ABV</a>
  <a class="tag" href="?q=IBU">IBU</a>
  <a class="tag" href="?q=Excel">Excel</a>
  <a class="tag" href="?q=forecasting">forecasting</a>
  <a class="tag" href="?q=ESG">ESG</a>
</p>

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
      return ((p.title || '') + ' ' + (p.tags || '') + ' ' + (p.description || '') + ' ' + (p.body || '')).toLowerCase().indexOf(q) > -1;
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
