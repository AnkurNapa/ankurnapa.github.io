---
layout: page
title: "Topics"
permalink: /tags/
description: "Browse Beer, Wine, Whiskey & AI by topic and keyword — every post organized by tag."
---

Browse every post by topic. Jump to a keyword:

<div class="tag-cloud">
{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}<a class="tag" href="#{{ tag[0] | slugify }}">#{{ tag[0] }} <span class="count">{{ tag[1] | size }}</span></a>
{% endfor %}
</div>

{% for tag in sorted_tags %}
<section class="tag-section" id="{{ tag[0] | slugify }}">
  <h2>#{{ tag[0] }}</h2>
  <ul class="posts">
  {% for post in tag[1] %}
    <li class="post-item">
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
