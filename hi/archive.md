---
layout: page
lang: hi
title: "संग्रह"
permalink: /hi/archive/
description: "बीयर, वाइन, व्हिस्की और AI की हर पोस्ट, नवीनतम पहले — पूरी समयरेखा।"
---

पूरी समयरेखा — नवीनतम पहले।

{% assign hi_sorted = site.hi | sort: 'date' | reverse %}
{% assign postsByYear = hi_sorted | group_by_exp: "post", "post.date | date: '%Y'" %}
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
