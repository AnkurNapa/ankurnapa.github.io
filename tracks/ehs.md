---
layout: page
title: "EHS Analytics for Beverage"
permalink: /tracks/ehs/
description: "An executive EHS track for breweries — predictive safety, hazard mapping, food safety traceability, compliance, and safety culture, for beer and non-alcoholic beer plants."
---

Prevention over paperwork — environment, health, and safety analytics for beer and non-alcoholic production. The full track, in order:

{% assign track_posts = site.tags['ehs'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
