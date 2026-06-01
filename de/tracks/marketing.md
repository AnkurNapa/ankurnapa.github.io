---
layout: page
lang: de
title: "Marketing-Analytik für Getränke"
permalink: /de/tracks/marketing/
description: "Eine Führungsstrecke zur Marketing-Analytik für Brauereien — Segmentierung, Marketing-Mix-Modellierung, Markenwert, Attribution und der sober-curious Konsument von alkoholfreiem Bier."
---

Ausgabenverantwortung und der sober-curious Konsument — Marketing-Analytik für Bier- und alkoholfreie Marken. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'marketing'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
