---
layout: page
lang: mr
title: "पेयांसाठी ESG अॅनालिटिक्स"
permalink: /mr/tracks/esg/
description: "ब्रूअरीजसाठी एक कार्यकारी ESG ट्रॅक — जल व्यवस्थापन, कार्बन लेखांकन, पॅकेजिंगचा पर्यावरणीय परिणाम, रिपोर्टिंग ऑटोमेशन आणि बिझनेस केस, बिअर व नॉन-अल्कोहोलिक बिअरमध्ये."
---

मार्जिनशी जोडलेली मोजता येणारी शाश्वतता — बिअर आणि नॉन-अल्कोहोलिक उत्पादनासाठी ESG अॅनालिटिक्स. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'esg'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
