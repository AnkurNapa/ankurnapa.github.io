---
layout: page
lang: hi
title: "बेवरेज के लिए सेल्स इंटेलिजेंस"
permalink: /hi/tracks/sales-intelligence/
description: "ब्रुअरीज़ के लिए सेल्स इंटेलिजेंस पर एक कार्यकारी ट्रैक — डिप्लीशन डेटा, अकाउंट स्कोरिंग, डिस्ट्रीब्यूटर स्कोरकार्ड, परफ़ेक्ट-स्टोर एग्ज़ीक्यूशन और चर्न, बीयर तथा नॉन-अल्कोहलिक बीयर के लिए।"
---

डिस्ट्रीब्यूटर ब्लैक बॉक्सेज़ से लेकर आउटलेट-स्तर के निर्णयों तक — बीयर और नॉन-अल्कोहलिक लाइनों के लिए तेज़ सेल्स इंटेलिजेंस। पूरा ट्रैक, क्रम में:

{% assign track_posts = site.hi | where_exp: "p", "p.tags contains 'sales-intelligence'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
