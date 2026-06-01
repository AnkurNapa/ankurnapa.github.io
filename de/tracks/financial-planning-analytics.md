---
layout: page
lang: de
title: "Finanzplanung & Analytik für Getränke"
permalink: /de/tracks/financial-planning-analytics/
description: "Eine FP&A-Führungsstrecke für Brauereien — Herstellkosten, treiberbasierte Prognose, Margenbrücken, Cost-to-Serve, Szenarioplanung und Working Capital für Bier und alkoholfreies Bier."
---

Treiberbasierte Finanzsteuerung für eine Branche mit volatilen Kosten — FP&A für Bier und alkoholfreie Linien. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'fpna'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
