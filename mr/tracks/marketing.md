---
layout: page
lang: mr
title: "पेयांसाठी मार्केटिंग अॅनालिटिक्स"
permalink: /mr/tracks/marketing/
description: "ब्रूअरीजसाठी मार्केटिंग अॅनालिटिक्सवरील एक कार्यकारी ट्रॅक — सेगमेंटेशन, मार्केटिंग मिक्स मॉडेलिंग, ब्रँड इक्विटी, अॅट्रिब्युशन आणि सोबर-क्युरिअस नॉन-अल्कोहोलिक बिअर ग्राहक."
---

खर्चाची उत्तरदायित्व आणि सोबर-क्युरिअस ग्राहक — बिअर आणि नॉन-अल्कोहोलिक ब्रँडसाठी मार्केटिंग अॅनालिटिक्स. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'marketing'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
