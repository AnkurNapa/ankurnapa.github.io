---
layout: page
lang: de
title: "ESG-Analytik für Getränke"
permalink: /de/tracks/esg/
description: "Eine ESG-Führungsstrecke für Brauereien — Wasser-Stewardship, CO₂-Bilanzierung, Verpackungs-Fußabdruck, Reporting-Automatisierung und der Business Case, über Bier und alkoholfreies Bier hinweg."
---

Messbare Nachhaltigkeit, an die Marge gekoppelt — ESG-Analytik für Bier- und alkoholfreie Produktion. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'esg'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
