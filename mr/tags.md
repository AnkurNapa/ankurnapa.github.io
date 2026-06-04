---
layout: page
lang: mr
title: "विषय"
permalink: /mr/tags/
description: "बिअर, वाइन, व्हिस्की आणि AI विषयानुसार ब्राउझ करा — उत्पादन विज्ञान, AI आणि मशीन लर्निंग, जनरेटिव्ह AI, डेटा प्लॅटफॉर्म (Microsoft Fabric, Databricks, Snowflake), IoT, शाश्वतता, विक्री आणि वित्त. प्रत्येक पोस्ट टॅगनुसार रचलेली."
---

प्रत्येक पोस्ट विषयानुसार ब्राउझ करा — फर्मेंटेशन, एंजेल्स' शेअर आणि ब्रूइंग गणितांपासून Microsoft Fabric, Claude, IoT, शाश्वतता आणि ESG पर्यंत.

किंवा कोणत्याही कीवर्डवर जा:

{% assign all_tags = "" | split: "" %}
{% for post in site.mr %}
  {% for tag in post.tags %}
    {% assign one = tag | split: "~~NOSPLIT~~" %}
    {% assign all_tags = all_tags | concat: one %}
  {% endfor %}
{% endfor %}
{% assign all_tags = all_tags | uniq | sort %}

<div class="tag-cloud">
{% for tag in all_tags %}<a class="tag" href="#{{ tag | slugify }}">#{{ tag }}</a>
{% endfor %}
</div>

{% for tag in all_tags %}
<section class="tag-section" id="{{ tag | slugify }}">
  <h2>#{{ tag }}</h2>
  <ul class="posts">
  {% assign tagged = site.mr | where_exp: "post", "post.tags contains tag" | sort: 'date' | reverse %}
  {% for post in tagged %}
    <li class="post-item">
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %b %Y" }}</time>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
