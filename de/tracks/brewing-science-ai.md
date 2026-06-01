---
layout: page
lang: de
title: "Brauwissenschaft & KI"
permalink: /de/tracks/brewing-science-ai/
description: "Wo Brauwissenschaft auf maschinelles Lernen trifft — Malz, Wasser, Hopfen, Würze, Hefe, Gärung, Filtration, Verpackung, Hygiene und QK, mit ehrlichen Einschätzungen, was KI auf dem Produktionsboden vorhersagen kann und was nicht."
---

Die technische Strecke: angewandte KI über den gesamten Brauprozess, von der Kornannahme bis zum verpackten Bier. Verankert in den Grundlagen des Brauens — Mälzen, Maischen, Würzebereitung, Hefe und Gärung, Reifung, Filtration, Verpackung, Hygiene und Qualitätskontrolle — und ehrlich darüber, wo sich die Modelle bezahlt machen und wo nicht. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'brewing-science'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
