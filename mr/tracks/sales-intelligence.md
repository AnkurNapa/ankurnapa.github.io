---
layout: page
lang: mr
title: "पेयांसाठी सेल्स इंटेलिजन्स"
permalink: /mr/tracks/sales-intelligence/
description: "ब्रूअरीजसाठी सेल्स इंटेलिजन्सवरील एक कार्यकारी ट्रॅक — डिप्लीशन डेटा, अकाउंट स्कोअरिंग, डिस्ट्रिब्युटर स्कोअरकार्ड, परफेक्ट-स्टोअर एक्झिक्युशन आणि चर्न, बिअर व नॉन-अल्कोहोलिक बिअरसाठी."
---

डिस्ट्रिब्युटर ब्लॅक बॉक्सेसपासून आउटलेट-स्तरीय निर्णयांपर्यंत — बिअर आणि नॉन-अल्कोहोलिक लाइन्ससाठी जलद सेल्स इंटेलिजन्स. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'sales-intelligence'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
