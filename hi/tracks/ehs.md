---
layout: page
lang: hi
title: "बेवरेज के लिए EHS विश्लेषण"
permalink: /hi/tracks/ehs/
description: "ब्रुअरीज़ के लिए एक कार्यकारी EHS ट्रैक — पूर्वानुमानात्मक सुरक्षा, ख़तरा मानचित्रण, खाद्य सुरक्षा अनुरेखणीयता, अनुपालन और सुरक्षा संस्कृति, बीयर तथा नॉन-अल्कोहलिक संयंत्रों के लिए।"
---

कागज़ी कार्रवाई से ऊपर रोकथाम — बीयर और नॉन-अल्कोहलिक उत्पादन के लिए पर्यावरण, स्वास्थ्य और सुरक्षा विश्लेषण। पूरा ट्रैक, क्रम में:

{% assign track_posts = site.hi | where_exp: "p", "p.tags contains 'ehs'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
