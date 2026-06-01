---
layout: page
lang: de
title: "Suche"
permalink: /de/search/
description: "Durchsuche jeden Artikel von Bier, Wein, Whisky & KI — Produktionswissenschaft, KI, Datenplattformen, generative KI, IoT, Nachhaltigkeit, Vertrieb und Finanzen."
---

Durchsuche jeden Artikel — nach Titel, Themen-Tag, Zusammenfassung oder Text.

<input type="search" id="search-input" class="search-box" placeholder="Artikel suchen… z. B. Gärung, Power BI, Fass, Microsoft Fabric" autocomplete="off" autofocus aria-label="Artikel suchen">
<p id="search-status" class="search-status" role="status" aria-live="polite"></p>

<p class="search-chips" style="margin:.4rem 0 1rem">Versuche:
  <a class="tag" href="?q=Gärung">Gärung</a>
  <a class="tag" href="?q=Power BI">Power BI</a>
  <a class="tag" href="?q=Microsoft Fabric">Microsoft Fabric</a>
  <a class="tag" href="?q=Claude">Claude</a>
  <a class="tag" href="?q=Databricks">Databricks</a>
  <a class="tag" href="?q=Snowflake">Snowflake</a>
  <a class="tag" href="?q=IoT">IoT</a>
  <a class="tag" href="?q=Nachhaltigkeit">Nachhaltigkeit</a>
  <a class="tag" href="?q=Wasser">Wasser</a>
  <a class="tag" href="?q=CO2">CO₂</a>
  <a class="tag" href="?q=Fass">Fass</a>
  <a class="tag" href="?q=ABV">ABV</a>
  <a class="tag" href="?q=IBU">IBU</a>
  <a class="tag" href="?q=Excel">Excel</a>
  <a class="tag" href="?q=Prognose">Prognose</a>
  <a class="tag" href="?q=Vertrieb">Vertrieb</a>
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
    if (!items.length) { status.textContent = 'Keine Artikel passen zu „' + q + '“.'; return; }
    status.textContent = items.length + (items.length > 1 ? ' Ergebnisse' : ' Ergebnis') + ' für „' + q + '“';
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
  fetch('{{ "/de/search.json" | relative_url }}')
    .then(function (r) { return r.json(); })
    .then(function (j) {
      data = j;
      var q = new URLSearchParams(location.search).get('q');
      if (q) { input.value = q; run(q); }
    })
    .catch(function () { status.textContent = 'Suchindex konnte nicht geladen werden.'; });
  input.addEventListener('input', function () { run(input.value); });
})();
</script>
