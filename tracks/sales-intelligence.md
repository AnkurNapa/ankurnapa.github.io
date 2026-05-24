---
layout: page
title: "Sales Intelligence for Beverage"
permalink: /tracks/sales-intelligence/
description: "An executive track on sales intelligence for breweries — depletion data, account scoring, distributor scorecards, perfect-store execution, and churn for beer and non-alcoholic beer."
---

From distributor black boxes to outlet-level decisions — sharper sales intelligence for beer and non-alcoholic lines. The full track, in order:

{% assign track_posts = site.tags['sales-intelligence'] | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
