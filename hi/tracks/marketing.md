---
layout: page
lang: hi
title: "बेवरेज के लिए मार्केटिंग विश्लेषण"
permalink: /hi/tracks/marketing/
description: "ब्रुअरीज़ के लिए मार्केटिंग विश्लेषण पर एक कार्यकारी ट्रैक — सेगमेंटेशन, मार्केटिंग मिक्स मॉडलिंग, ब्रांड इक्विटी, एट्रिब्यूशन और सोबर-क्यूरियस नॉन-अल्कोहलिक बीयर उपभोक्ता।"
---

ख़र्च की जवाबदेही और सोबर-क्यूरियस उपभोक्ता — बीयर और नॉन-अल्कोहलिक ब्रांडों के लिए मार्केटिंग विश्लेषण। पूरा ट्रैक, क्रम में:

{% assign track_posts = site.hi | where_exp: "p", "p.tags contains 'marketing'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
