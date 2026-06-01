---
layout: page
lang: de
title: "EHS-Analytik für Getränke"
permalink: /de/tracks/ehs/
description: "Eine EHS-Führungsstrecke für Brauereien — vorausschauende Sicherheit, Gefahrenkartierung, Rückverfolgbarkeit der Lebensmittelsicherheit, Compliance und Sicherheitskultur für Bier- und alkoholfreie Werke."
---

Prävention statt Papierkram — Umwelt-, Gesundheits- und Sicherheitsanalytik für Bier- und alkoholfreie Produktion. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'ehs'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
