---
layout: page
title: "Archive"
permalink: /archive/
description: "Every post from Beer, Wine, Whiskey & AI, newest first — the full timeline."
---

The full timeline — newest first.

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<section class="archive-year">
  <h2>{{ year.name }}</h2>
  <ul class="posts">
  {% for post in year.items %}
    <li class="post-item">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d" }}</time> —
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
