---
layout: page
lang: de
title: "Weinherstellung & KI"
permalink: /de/tracks/winemaking-ai/
description: "Wo Weinherstellung auf maschinelles Lernen trifft — Traubenreife und Erntezeitpunkt, Weinbergsertrag, Gärung, Weinfehler, Verschnitt und Präzisionsweinbau, mit ehrlichen Einschätzungen, was KI von der Rebe bis zur Flasche vorhersagen kann und was nicht."
---

Die Wein-Strecke: angewandte KI vom Weinberg bis in den Keller — Reife und Erntezeitpunkt vorhersagen, Ertrag prognostizieren, die Gärung steuern, Fehler früh erkennen, Verschnitte optimieren und den Weinberg mit Computer Vision lesen. Verankert in echter Önologie und Viticultur und ehrlich darüber, wo die Modelle helfen und wo das Urteil des Winzers weiterhin regiert. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'winemaking'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
