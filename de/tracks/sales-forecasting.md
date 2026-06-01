---
layout: page
lang: de
title: "Absatzprognose für Getränke"
permalink: /de/tracks/sales-forecasting/
description: "Eine Führungsstrecke zur Absatzprognose für Brauereien — Reifegradmodell, Neuprodukt- und saisonale Prognose, Promotion-Lift, hierarchische Abstimmung, Genauigkeitskennzahlen und ehrliche Grenzen."
---

Eine Reifegrad-Leiter vom Tabellenblatt zum ML — und eine ehrliche Darstellung ihrer Grenzen — für Bier- und alkoholfreie Nachfrage. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'forecasting'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
