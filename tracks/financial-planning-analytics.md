---
layout: page
title: "Financial Planning & Analytics for Beverage"
permalink: /tracks/financial-planning-analytics/
description: "An executive FP&A track for breweries — cost of goods, driver-based forecasting, margin bridges, cost-to-serve, scenario planning, and working capital for beer and non-alcoholic beer."
---

Driver-based finance for a volatile-cost industry — FP&A for beer and non-alcoholic lines. The full track, in order:

{% assign track_posts = site.tags['fpna'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
