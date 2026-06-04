---
layout: page
lang: mr
title: "पेयांसाठी विक्री पूर्वानुमान"
permalink: /mr/tracks/sales-forecasting/
description: "ब्रूअरीजसाठी एक कार्यकारी विक्री पूर्वानुमान ट्रॅक — परिपक्वता मॉडेल, नवीन-उत्पादन आणि मोसमी पूर्वानुमान, प्रमोशन लिफ्ट, श्रेणीबद्ध समाधान, अचूकता मेट्रिक्स आणि प्रामाणिक मर्यादा."
---

स्प्रेडशीटपासून ML पर्यंत एक परिपक्वता शिडी — आणि तिच्या मर्यादांचा एक प्रामाणिक हिशेब — बिअर आणि नॉन-अल्कोहोलिक मागणीसाठी. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'forecasting'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
