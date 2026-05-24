---
layout: page
title: "Sales Forecasting for Beverage"
permalink: /tracks/sales-forecasting/
description: "An executive sales forecasting track for breweries — maturity model, new-product and seasonal forecasting, promo lift, hierarchical reconciliation, accuracy metrics, and honest limits."
---

A maturity ladder from spreadsheet to ML — and an honest account of its limits — for beer and non-alcoholic demand. The full track, in order:

{% assign track_posts = site.tags['forecasting'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
