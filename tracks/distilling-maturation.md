---
layout: page
title: "Distilling & Maturation"
permalink: /tracks/distilling-maturation/
description: "AI applied to distilling and cask maturation — distillation cut points, new-make spirit flavour, the angel's share, cask selection, congener evolution, blending, and bottling maturity for whiskey and spirits."
---

The spirits track: machine learning across distillation and the long, slow business of maturation — cut-point selection, new-make spirit character, the angel's share, cask inventory, congener development, blending consistency, and bottling maturity. Written for distillers, with the same honest line on what data can and cannot tell you across years in the warehouse. The full track, in order:

{% assign track_posts = site.tags['distilling-maturation'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
