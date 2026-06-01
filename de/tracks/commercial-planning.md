---
layout: page
lang: de
title: "Kommerzielle Planungsanalytik für Getränke"
permalink: /de/tracks/commercial-planning/
description: "Eine Führungsstrecke zur kommerziellen Planungsanalytik für Brauereien — Portfoliostrategie, Revenue Growth Management, Trade Promotion, Route-to-Market und S&OP für Bier und alkoholfreies Bier."
---

Fragmentierte Vertriebs- und Lieferpläne in eine einzige margenbewusste Vertriebsmaschine verwandeln — über Bier und das alkoholfreie Segment hinweg. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'commercial-planning'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
