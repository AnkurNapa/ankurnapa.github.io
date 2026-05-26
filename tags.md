---
layout: page
title: "Topics"
permalink: /tags/
description: "Browse Beer, Wine, Whiskey & AI by topic — production science, AI and machine learning, generative AI, data platforms (Microsoft Fabric, Databricks, Snowflake), IoT, sustainability, sales and finance. Every post organized by tag."
---

Browse every post by topic — from fermentation, the angel's share and brewing calculations to Microsoft Fabric, Claude, IoT, sustainability and ESG.

**Popular topics:** [#machine-learning](#machine-learning) · [#generative-ai](#generative-ai) · [#data-platform](#data-platform) · [#sustainability](#sustainability) · [#iot](#iot) · [#excel](#excel) · [#power-bi](#power-bi) · [#forecasting](#forecasting)

Or jump to any keyword:

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
