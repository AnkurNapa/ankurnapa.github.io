---
layout: page
title: "ESG Analytics for Beverage"
permalink: /tracks/esg/
description: "An executive ESG track for breweries — water stewardship, carbon accounting, packaging footprint, reporting automation, and the business case, across beer and non-alcoholic beer."
---

Measurable sustainability tied to margin — ESG analytics for beer and non-alcoholic production. The full track, in order:

{% assign track_posts = site.tags['esg'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
