---
layout: page
lang: mr
title: "शोध"
permalink: /mr/search/
description: "बिअर, वाइन, व्हिस्की आणि AI चा प्रत्येक लेख शोधा — उत्पादन विज्ञान, AI, डेटा प्लॅटफॉर्म, जनरेटिव्ह AI, IoT, शाश्वतता, विक्री आणि वित्त."
---

प्रत्येक लेख शोधा — शीर्षक, विषय टॅग, सारांश किंवा मूळ मजकुरानुसार.

<input type="search" id="search-input" class="search-box" placeholder="लेख शोधा… उदा. फर्मेंटेशन, Power BI, कास्क, Microsoft Fabric" autocomplete="off" autofocus aria-label="लेख शोधा">
<p id="search-status" class="search-status" role="status" aria-live="polite"></p>

<p class="search-chips" style="margin:.4rem 0 1rem">वापरून पाहा:
  <a class="tag" href="?q=फर्मेंटेशन">फर्मेंटेशन</a>
  <a class="tag" href="?q=Power BI">Power BI</a>
  <a class="tag" href="?q=Microsoft Fabric">Microsoft Fabric</a>
  <a class="tag" href="?q=Claude">Claude</a>
  <a class="tag" href="?q=Databricks">Databricks</a>
  <a class="tag" href="?q=Snowflake">Snowflake</a>
  <a class="tag" href="?q=IoT">IoT</a>
  <a class="tag" href="?q=शाश्वतता">शाश्वतता</a>
  <a class="tag" href="?q=पाणी">पाणी</a>
  <a class="tag" href="?q=CO2">CO₂</a>
  <a class="tag" href="?q=कास्क">कास्क</a>
  <a class="tag" href="?q=ABV">ABV</a>
  <a class="tag" href="?q=IBU">IBU</a>
  <a class="tag" href="?q=Excel">Excel</a>
  <a class="tag" href="?q=पूर्वानुमान">पूर्वानुमान</a>
  <a class="tag" href="?q=विक्री">विक्री</a>
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
    if (!items.length) { status.textContent = '„' + q + '“ शी जुळणारा कोणताही लेख नाही.'; return; }
    status.textContent = items.length + ' निकाल „' + q + '“ साठी';
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
  fetch('{{ "/mr/search.json" | relative_url }}')
    .then(function (r) { return r.json(); })
    .then(function (j) {
      data = j;
      var q = new URLSearchParams(location.search).get('q');
      if (q) { input.value = q; run(q); }
    })
    .catch(function () { status.textContent = 'शोध सूची लोड होऊ शकली नाही.'; });
  input.addEventListener('input', function () { run(input.value); });
})();
</script>
