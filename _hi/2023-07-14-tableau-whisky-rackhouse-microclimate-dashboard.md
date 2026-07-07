---
layout: post
lang: hi
title: "Tableau में एक रैकहाउस माइक्रोक्लाइमेट डैशबोर्ड"
image: /assets/og/tableau-whisky-rackhouse-microclimate-dashboard.png
description: "एक Tableau रैकहाउस माइक्रोक्लाइमेट डैशबोर्ड बनाएँ जो स्थिति के अनुसार वेयरहाउस तापमान व आर्द्रता को परिपक्वता-हानि से मैप करे, AI बाहरी-मान व्याख्याओं के साथ।"
date: 2023-07-14
updated: 2023-07-14
permalink: /hi/2023/tableau-whisky-rackhouse-microclimate-dashboard/
tags: [distilling-maturation, tableau, whiskey]
faq:
  - q: "मैं Tableau में वेयरहाउस स्थिति कैसे मैप करूँ?"
    a: "बे, रो और ऊँचाई को निर्देशांक मानें और उन्हें रो व कॉलम के रूप में उपयोग करके एक हीटमैप बनाएँ, हर सेल को तापमान, आर्द्रता या मापी गई हानि के अनुसार रंग दें ताकि रैकहाउस का ऊर्ध्वाधर ढाल दिखाई दे।"
  - q: "क्या Tableau मुझे बता सकता है कि किन कास्क को घुमाना है?"
    a: "यह गर्म या शुष्क ज़ोनों के संपर्क के अनुसार उम्मीदवारों को क्रम दे सकता है और उन्हें चिह्नित कर सकता है, पर घुमाव के निर्णय स्पिरिट की लक्ष्य शैली पर भी निर्भर करते हैं, इसलिए डैशबोर्ड आदेश देने के बजाय सूचित करता है।"
  - q: "Explain Data यहाँ क्या जोड़ता है?"
    a: "Explain Data किसी बाहरी मान के लिए सांख्यिकीय कारण प्रस्तावित करता है — जैसे किसी गर्म बे में ऊँचा रखा कास्क अधिक खोना — आपको सेंसर और वज़न रिकॉर्ड के विरुद्ध जाँचने के लिए एक तेज़ परिकल्पना देता है।"
---

**संक्षिप्त उत्तर: एक Tableau रैकहाउस डैशबोर्ड वेयरहाउस सेंसर रीडिंग को एक हीटमैप में बदल देता है जो ठीक-ठीक दिखाता है कि गर्मी और सूखापन कहाँ तेज़ हानि और बड़ी कास्क-दर-कास्क भिन्नता चला रहे हैं।** यह एक अदृश्य माइक्रोक्लाइमेट को दृश्य बना देता है — बशर्ते आपके पास उसे मैप करने के लिए पर्याप्त सेंसर हों।

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Tableau में एक रैकहाउस माइक्रोक्लाइमेट डैशबोर्ड के लिए विशिष्ट डैशबोर्ड लेआउट"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">डैशबोर्ड लेआउट</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Tableau में एक रैकहाउस माइक्रोक्लाइमेट डैशबोर्ड</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">फ़िल्टर:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">रुझान</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">विभाजन</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">इस डैशबोर्ड के लिए एक विशिष्ट लेआउट: ऊपर शीर्ष मीट्रिक, नीचे एक रुझान और एक विभाजन, इसे काटने के लिए फ़िल्टर।</figcaption>
</figure>

## माइक्रोक्लाइमेट ड्राम का फ़ैसला क्यों करता है
एक पारंपरिक डनेज वेयरहाउस और एक ऊँचा रैक्ड रैकहाउस स्पिरिट को बहुत अलग ढंग से परिपक्व करते हैं, और किसी भी एक इमारत के भीतर ऊपरी शेल्फ़ फ़र्श की तुलना में अधिक गर्म और शुष्क रहते हैं। यही ऊर्ध्वाधर ढाल इसका कारण है कि एक ही दिन एक ही स्पिरिट से भरे गए दो कास्क एक दशक में अलग हो सकते हैं — अलग एंजल्स शेयर, वैनिलिन, लैक्टोन और टैनिन का अलग लकड़ी-निष्कर्षण। अगर आप माइक्रोक्लाइमेट को देख नहीं सकते, तो आप भिन्नता की व्याख्या नहीं कर सकते, और निश्चित रूप से इसे प्रबंधित नहीं कर सकते।

इस डैशबोर्ड का काम स्थिति को आपके डेटा का एक प्रथम-श्रेणी आयाम बनाना है, कास्क और समय के साथ-साथ।

## हीटमैप बनाना
ग्रेन को परिभाषित करने से शुरू करें: हर सेंसर के हर टाइमस्टैम्प पर एक रीडिंग, एक कास्क-पोज़िशन टेबल से जुड़ी जो हर कास्क की बे, रो और ऊँचाई दर्ज करती है। Tableau Prep में, सेंसर फ़ीड को पिवट और साफ़ करें, फिर एक .hyper एक्सट्रैक्ट प्रकाशित करें। मुख्य व्यू को एक हीटमैप के रूप में बनाएँ जिसमें अक्षों पर बे और रो हों और ऊँचाई एक स्मॉल-मल्टीपल या एक पैरामीटर हो जिसे उपयोगकर्ता टॉगल करे, सेलों को औसत तापमान, सापेक्ष आर्द्रता, या मापी गई हानि के अनुसार रंग दें।

LOD एक्सप्रेशन भारी काम करते हैं: `{ FIXED [Bay], [Height] : AVG([Temperature]) }` एक स्थिर प्रति-ज़ोन औसत देता है जो उपयोगकर्ता के महीने के अनुसार फ़िल्टर करने पर नहीं खिसकता। उस माइक्रोक्लाइमेट फ़ील्ड को कास्क परिणामों से जोड़ें और आप घुमाव के उम्मीदवारों को क्रम दे सकते हैं — वे कास्क जो सबसे गर्म, सबसे शुष्क सेलों में बैठे हैं। एक हाइलाइट एक्शन किसी उपयोगकर्ता को एक गर्म ज़ोन पर क्लिक करने और उसमें हर कास्क देखने देता है। जब कुछ ग़लत लगे, बाहरी मान पर Explain Data चलाएँ और Tableau आपके सत्यापन के लिए उम्मीदवार कारण प्रस्तावित करेगा।

## यह कहाँ टूटता है
ईमानदार सीमा सेंसर कवरेज है। एक बड़े रैकहाउस में मुट्ठी भर प्रोब मापने से अधिक प्रक्षेपित करते हैं, इसलिए आपका हीटमैप एक मॉडल है, एक नक्शा नहीं। सेल-स्तर के विवरण पर भरोसा करने से पहले सेंसरों पर खर्च करें। दूसरी सीमा नियंत्रण है: पारंपरिक वेयरहाउस जानबूझकर निष्क्रिय होते हैं, और आप व्हिस्की के चरित्र को बदले बिना एक डनेज शेड को एयर-कंडीशन नहीं कर सकते। डैशबोर्ड ज़्यादातर आपको बताता है कि कास्क कहाँ ले जाएँ, यह नहीं कि जलवायु कैसे बदलें — और घुमाव भी श्रम और स्पिरिट की इच्छित शैली से बँधा होता है। ऑप्टिमाइज़ेशन पक्ष के लिए, देखें [AI रैकहाउस माइक्रोक्लाइमेट ऑप्टिमाइज़ेशन]({{ '/hi/2024/ai-rackhouse-microclimate-optimization/' | relative_url }})।

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="परिपक्वता को क्या चलाता है, और यह आगे क्या बदलता है।"><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">इसे क्या चलाता है</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Tableau में एक रैकहाउस माइक्रोक्लाइमेट डैशबोर्ड</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">आगत 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">आगत 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">आगत 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">परिपक्वता</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">गुणवत्ता</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">लागत / जोखिम</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">परिपक्वता को क्या चलाता है, और यह आगे क्या बदलता है।</figcaption>
</figure>

## निचोड़
Tableau में माइक्रोक्लाइमेट मैप करना यह समझने का सबसे स्पष्ट तरीका है कि आपके कास्क क्यों अलग होते हैं और कौन-से सबसे कठोर परिस्थितियों के संपर्क में हैं। यह सेंसरों और एक साफ़ पोज़िशन टेबल में निवेश को पुरस्कृत करता है, और यह स्वाभाविक रूप से उन AI फ़ीचरों के साथ जुड़ता है जो बाहरी मानों की व्याख्या करते हैं। घुमाव और फ़िल रणनीति को सूचित करने के लिए इसका उपयोग करें, पर याद रखें कि वेयरहाउस एक धीमा, निष्क्रिय उपकरण है — डैशबोर्ड आपको इसे पढ़ने में मदद करता है, इसे रद्द करने में नहीं।

*[डिस्टिलिंग व मैच्योरेशन]({{ '/hi/tracks/distilling-maturation/' | relative_url }}) ट्रैक का हिस्सा।* संबंधित: [AI रैकहाउस माइक्रोक्लाइमेट ऑप्टिमाइज़ेशन]({{ '/hi/2024/ai-rackhouse-microclimate-optimization/' | relative_url }})।

## अक्सर पूछे जाने वाले सवाल

**मैं Tableau में वेयरहाउस स्थिति कैसे मैप करूँ?**
बे, रो और ऊँचाई को निर्देशांक मानें और उन्हें रो व कॉलम के रूप में उपयोग करके एक हीटमैप बनाएँ, हर सेल को तापमान, आर्द्रता या मापी गई हानि के अनुसार रंग दें ताकि रैकहाउस का ऊर्ध्वाधर ढाल दिखाई दे।

**क्या Tableau मुझे बता सकता है कि किन कास्क को घुमाना है?**
यह गर्म या शुष्क ज़ोनों के संपर्क के अनुसार उम्मीदवारों को क्रम दे सकता है और उन्हें चिह्नित कर सकता है, पर घुमाव के निर्णय स्पिरिट की लक्ष्य शैली पर भी निर्भर करते हैं, इसलिए डैशबोर्ड आदेश देने के बजाय सूचित करता है।

**Explain Data यहाँ क्या जोड़ता है?**
Explain Data किसी बाहरी मान के लिए सांख्यिकीय कारण प्रस्तावित करता है — जैसे किसी गर्म बे में ऊँचा रखा कास्क अधिक खोना — आपको सेंसर और वज़न रिकॉर्ड के विरुद्ध जाँचने के लिए एक तेज़ परिकल्पना देता है।
