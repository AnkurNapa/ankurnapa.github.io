---
layout: page
lang: mr
title: "ब्रूइंग विज्ञान आणि AI"
permalink: /mr/tracks/brewing-science-ai/
description: "जिथे ब्रूइंग विज्ञान मशीन लर्निंगला भेटते — माल्ट, पाणी, हॉप्स, वोर्ट, यीस्ट, फर्मेंटेशन, फिल्ट्रेशन, पॅकेजिंग, स्वच्छता आणि गुणवत्ता नियंत्रण, उत्पादन फ्लोअरवर AI काय अंदाज लावू शकते आणि काय नाही याच्या प्रामाणिक मूल्यमापनासह."
---

तांत्रिक ट्रॅक: धान्य मिळवण्यापासून पॅक केलेल्या बिअरपर्यंत, संपूर्ण ब्रूइंग प्रक्रियेत लागू केलेले AI. ब्रूइंगच्या मूलभूत गोष्टींवर आधारित — माल्टिंग, मॅशिंग, वोर्ट उत्पादन, यीस्ट आणि फर्मेंटेशन, परिपक्वन, फिल्ट्रेशन, पॅकेजिंग, स्वच्छता आणि गुणवत्ता नियंत्रण — आणि मॉडेल कुठे आपली किंमत वसूल करतात आणि कुठे नाही याबद्दल प्रामाणिक. संपूर्ण ट्रॅक, क्रमाने:

{% assign track_posts = site.mr | where_exp: "p", "p.tags contains 'brewing-science'" | sort: 'date' %}
<ul class="posts">
{% for post in track_posts %}
  <li class="post-item">
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    {% if post.description %}<p class="post-excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
