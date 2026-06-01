---
layout: page
lang: de
title: "Archiv"
permalink: /de/archive/
description: "Jeder Beitrag von Bier, Wein, Whisky & KI, neueste zuerst — die vollständige Zeitleiste."
---

Die vollständige Zeitleiste — neueste zuerst.

{% assign de_sorted = site.de | sort: 'date' | reverse %}
{% assign postsByYear = de_sorted | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<section class="archive-year">
  <h2>{{ year.name }}</h2>
  <ul class="posts">
  {% for post in year.items %}
    <li class="post-item">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d. %b" }}</time> —
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
