---
layout: page
lang: de
title: "Destillation & Reifung"
permalink: /de/tracks/distilling-maturation/
description: "KI angewendet auf Destillation und Fassreifung — Schnittpunkte der Destillation, New-Make-Spirit-Aroma, der Angels' Share, Fassauswahl, Congener-Entwicklung, Verschnitt und Abfüllreife für Whisky und Spirituosen."
---

Die Spirituosen-Strecke: maschinelles Lernen über die Destillation und das lange, langsame Geschäft der Reifung hinweg — Schnittpunktwahl, New-Make-Spirit-Charakter, der Angels' Share, Fassinventar, Congener-Entwicklung, Verschnittkonsistenz und Abfüllreife. Geschrieben für Brenner, mit derselben ehrlichen Linie dazu, was Daten über Jahre im Lagerhaus sagen können und was nicht. Die vollständige Strecke, der Reihe nach:

{% assign track_posts = site.de | where_exp: "p", "p.tags contains 'distilling-maturation'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
