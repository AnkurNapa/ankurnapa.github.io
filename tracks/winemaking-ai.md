---
layout: page
title: "Winemaking & AI"
permalink: /tracks/winemaking-ai/
description: "Where winemaking meets machine learning — grape ripeness and harvest timing, vineyard yield, fermentation, wine faults, blending, and precision viticulture, with honest takes on what AI can and cannot predict from vine to bottle."
---

The wine track: applied AI from vineyard to cellar — predicting ripeness and harvest date, forecasting yield, steering fermentation, catching faults early, optimising blends, and reading the vineyard with computer vision. Grounded in real oenology and viticulture, and honest about where the models help and where the winemaker's judgement still rules. The full track, in order:

{% assign track_posts = site.tags['winemaking'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
