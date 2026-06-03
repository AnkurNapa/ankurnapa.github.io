---
layout: page
lang: hi
title: "बेवरेज के लिए वित्तीय नियोजन और विश्लेषण"
permalink: /hi/tracks/financial-planning-analytics/
description: "ब्रुअरीज़ के लिए एक कार्यकारी FP&A ट्रैक — वस्तुओं की लागत, ड्राइवर-आधारित पूर्वानुमान, मार्जिन ब्रिज, कॉस्ट-टू-सर्व, परिदृश्य नियोजन और वर्किंग कैपिटल, बीयर तथा नॉन-अल्कोहलिक बीयर के लिए।"
---

अस्थिर लागत वाले उद्योग के लिए ड्राइवर-आधारित वित्त — बीयर और नॉन-अल्कोहलिक लाइनों के लिए FP&A। पूरा ट्रैक, क्रम में:

{% assign track_posts = site.hi | where_exp: "p", "p.tags contains 'fpna'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
