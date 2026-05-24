---
layout: page
title: "Commercial Planning Analytics for Beverage"
permalink: /tracks/commercial-planning/
description: "An executive track on commercial planning analytics for breweries — portfolio strategy, revenue growth management, trade promotion, route-to-market, and S&OP for beer and non-alcoholic beer."
---

Turning fragmented sales and supply plans into one margin-aware commercial engine — across beer and the non-alcoholic segment. The full track, in order:

{% assign track_posts = site.tags['commercial-planning'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
