---
layout: page
title: "Marketing Analytics for Beverage"
permalink: /tracks/marketing/
description: "An executive track on marketing analytics for breweries — segmentation, marketing mix modeling, brand equity, attribution, and the sober-curious non-alcoholic beer consumer."
---

Spend accountability and the sober-curious consumer — marketing analytics for beer and non-alcoholic brands. The full track, in order:

{% assign track_posts = site.tags['marketing'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
