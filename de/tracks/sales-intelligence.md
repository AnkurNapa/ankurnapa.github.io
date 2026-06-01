---
layout: page
lang: de
title: "Vertriebsintelligenz für Getränke"
permalink: /de/tracks/sales-intelligence/
description: "Eine Führungsstrecke zur Vertriebsintelligenz für Brauereien — Depletion-Daten, Account-Scoring, Distributoren-Scorecards, Perfect-Store-Execution und Churn für Bier und alkoholfreies Bier."
---

Von Distributoren-Blackboxes zu Entscheidungen auf Outlet-Ebene — schärfere Vertriebsintelligenz für Bier und alkoholfreie Linien. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'sales-intelligence'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
