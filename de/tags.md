---
layout: page
lang: de
title: "Themen"
permalink: /de/tags/
description: "Durchstöbere Bier, Wein, Whisky & KI nach Thema — Produktionswissenschaft, KI und maschinelles Lernen, generative KI, Datenplattformen (Microsoft Fabric, Databricks, Snowflake), IoT, Nachhaltigkeit, Vertrieb und Finanzen. Jeder Beitrag nach Tag geordnet."
---

Durchstöbere jeden Beitrag nach Thema — von Gärung, dem Angels' Share und Brauberechnungen bis zu Microsoft Fabric, Claude, IoT, Nachhaltigkeit und ESG.

Oder springe zu einem beliebigen Stichwort:

{% assign all_tags = "" | split: "" %}
{% for post in site.de %}
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
  {% assign tagged = site.de | where_exp: "post", "post.tags contains tag" | sort: 'date' | reverse %}
  {% for post in tagged %}
    <li class="post-item">
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d. %b %Y" }}</time>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
