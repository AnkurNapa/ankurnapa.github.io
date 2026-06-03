---
layout: page
lang: hi
title: "आसवन और परिपक्वन"
permalink: /hi/tracks/distilling-maturation/
description: "आसवन और कास्क परिपक्वन पर लागू AI — आसवन के कट-पॉइंट, न्यू-मेक स्पिरिट की सुगंध, एंजेल्स शेयर, कास्क चयन, कंजेनर विकास, ब्लेंडिंग और व्हिस्की तथा स्पिरिट्स के लिए बॉटलिंग परिपक्वता।"
---

स्पिरिट्स ट्रैक: आसवन और परिपक्वन के लंबे, धीमे कारोबार में मशीन लर्निंग — कट-पॉइंट चयन, न्यू-मेक स्पिरिट का चरित्र, एंजेल्स शेयर, कास्क इन्वेंटरी, कंजेनर विकास, ब्लेंडिंग की निरंतरता, और बॉटलिंग परिपक्वता। डिस्टिलर्स के लिए लिखा गया, उसी ईमानदार रुख के साथ कि वेयरहाउस में बीते वर्षों के बारे में डेटा आपको क्या बता सकता है और क्या नहीं। पूरा ट्रैक, क्रम में:

{% assign track_posts = site.hi | where_exp: "p", "p.tags contains 'distilling-maturation'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
