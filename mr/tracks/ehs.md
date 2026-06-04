---
layout: page
lang: mr
title: "पेयांसाठी EHS अॅनालिटिक्स"
permalink: /mr/tracks/ehs/
description: "ब्रूअरीजसाठी एक कार्यकारी EHS ट्रॅक — पूर्वानुमानात्मक सुरक्षा, धोका मॅपिंग, अन्न सुरक्षा ट्रेसेबिलिटी, अनुपालन आणि सुरक्षा संस्कृती, बिअर व नॉन-अल्कोहोलिक संयंत्रांसाठी."
---

कागदोपत्री कामापेक्षा प्रतिबंध — बिअर आणि नॉन-अल्कोहोलिक उत्पादनासाठी पर्यावरण, आरोग्य आणि सुरक्षा अॅनालिटिक्स. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'ehs'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
