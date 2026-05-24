---
layout: page
title: "Brewing Science & AI"
permalink: /tracks/brewing-science-ai/
description: "Where brewing science meets machine learning — malt, water, hops, wort, yeast, fermentation, filtration, packaging, hygiene, and QC, with honest takes on what AI can and cannot predict on the production floor."
---

The technical track: applied AI across the brewing process, from grain intake to packaged beer. Grounded in brewing fundamentals — malting, mashing, wort production, yeast and fermentation, maturation, filtration, packaging, hygiene, and quality control — and honest about where the models earn their keep and where they don't. The full track, in order:

{% assign track_posts = site.tags['brewing-science'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
