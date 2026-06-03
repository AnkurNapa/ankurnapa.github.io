---
layout: page
lang: hi
title: "विषय"
permalink: /hi/tags/
description: "बीयर, वाइन, व्हिस्की और AI को विषय के अनुसार ब्राउज़ करें — उत्पादन विज्ञान, AI और मशीन लर्निंग, जेनरेटिव AI, डेटा प्लेटफ़ॉर्म (Microsoft Fabric, Databricks, Snowflake), IoT, स्थिरता, बिक्री और वित्त। हर पोस्ट टैग के अनुसार व्यवस्थित।"
---

हर पोस्ट को विषय के अनुसार ब्राउज़ करें — फर्मेंटेशन, एंजेल्स' शेयर और ब्रूइंग गणनाओं से लेकर Microsoft Fabric, Claude, IoT, स्थिरता और ESG तक।

या किसी भी कीवर्ड पर जाएँ:

{% assign all_tags = "" | split: "" %}
{% for post in site.hi %}
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
  {% assign tagged = site.hi | where_exp: "post", "post.tags contains tag" | sort: 'date' | reverse %}
  {% for post in tagged %}
    <li class="post-item">
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %b %Y" }}</time>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
