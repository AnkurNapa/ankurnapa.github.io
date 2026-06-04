---
layout: page
lang: mr
title: "संग्रह"
permalink: /mr/archive/
description: "बिअर, वाइन, व्हिस्की आणि AI ची प्रत्येक पोस्ट, नवीनतम आधी — संपूर्ण कालरेषा."
---

संपूर्ण कालरेषा — नवीनतम आधी.

{% assign mr_sorted = site.mr | sort: 'date' | reverse %}
{% assign postsByYear = mr_sorted | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<section class="archive-year">
  <h2>{{ year.name }}</h2>
  <ul class="posts">
  {% for post in year.items %}
    <li class="post-item">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %b" }}</time> —
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
