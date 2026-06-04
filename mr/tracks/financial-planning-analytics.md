---
layout: page
lang: mr
title: "पेयांसाठी आर्थिक नियोजन आणि अॅनालिटिक्स"
permalink: /mr/tracks/financial-planning-analytics/
description: "ब्रूअरीजसाठी एक कार्यकारी FP&A ट्रॅक — वस्तूंची किंमत, ड्रायव्हर-आधारित पूर्वानुमान, मार्जिन ब्रिज, कॉस्ट-टू-सर्व्ह, परिस्थिती नियोजन आणि वर्किंग कॅपिटल, बिअर व नॉन-अल्कोहोलिक बिअरसाठी."
---

अस्थिर खर्च असलेल्या उद्योगासाठी ड्रायव्हर-आधारित वित्त — बिअर आणि नॉन-अल्कोहोलिक लाइन्ससाठी FP&A. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'fpna'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
