---
layout: post
lang: hi
title: "Tableau में पैकेजिंग-लाइन OEE को विज़ुअलाइज़ करना"
image: /assets/og/tableau-packaging-line-oee-dashboard.png
description: "Tableau में पैकेजिंग-लाइन का OEE डैशबोर्ड बनाएँ — Availability, Performance और Quality को कैलकुलेटेड फ़ील्ड के रूप में, एक डाउनटाइम Pareto और लाइन फ़िल्टर के साथ।"
date: 2023-02-21
updated: 2023-02-21
permalink: /hi/2023/tableau-packaging-line-oee-dashboard/
tags: [brewing-science, tableau, packaging]
faq:
  - q: "OEE को Tableau कैलकुलेटेड फ़ील्ड के रूप में कैसे निकाला जाता है?"
    a: "OEE, Availability गुणा Performance गुणा Quality है, और इनमें से हर एक एक अनुपात है जिसे आप कैलकुलेटेड फ़ील्ड के रूप में बनाते हैं: Availability यानी रन टाइम बँटा नियोजित समय, Performance यानी वास्तविक उत्पादन बँटा सैद्धांतिक उत्पादन, और Quality यानी अच्छी इकाइयाँ बँटा कुल इकाइयाँ। इन तीनों का गुणनफल आपका OEE प्रतिशत है।"
  - q: "OEE डैशबोर्ड पर सबसे उपयोगी चार्ट कौन-सा है?"
    a: "डाउनटाइम के कारणों का एक Pareto। यह उपलब्धता की हानि के कारणों को क्रम में रखता है, ताकि आप उन कुछ अहम रुकावटों को देख सकें जो अधिकांश हानि के लिए ज़िम्मेदार हैं — और आमतौर पर यहीं सबसे तेज़ सुधार मिलता है।"
  - q: "मेरा OEE गलत क्यों दिखता है?"
    a: "लगभग हमेशा इसलिए कि लाइन पर डाउनटाइम को किस तरह कोड किया जाता है। अगर ऑपरेटर रुकावटों को असंगत ढंग से दर्ज करते हैं या सब कुछ ‘other’ में डाल देते हैं, तो Availability घटक — और इसलिए OEE — अविश्वसनीय हो जाता है। गणित उतना ही अच्छा है जितना डाउनटाइम डेटा।"
---

**संक्षिप्त उत्तर: Tableau में OEE तीन ईमानदार अनुपातों का गुणनफल है, और एक Pareto जो आपको बताता है कि कहाँ देखना है।** बनाना सीधा है; मूल्य पूरी तरह इस पर निर्भर करता है कि लाइन अपना डाउनटाइम कितनी साफ़-सुथरी तरह दर्ज करती है।

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Tableau में पैकेजिंग-लाइन OEE को विज़ुअलाइज़ करने का सामान्य डैशबोर्ड लेआउट"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">डैशबोर्ड लेआउट</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Tableau में पैकेजिंग-लाइन OEE को विज़ुअलाइज़ करना</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">फ़िल्टर:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">रुझान</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">विभाजन</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">इस डैशबोर्ड का एक सामान्य लेआउट: ऊपर मुख्य मीट्रिक, नीचे एक रुझान और एक विभाजन, और इसे काटने के लिए फ़िल्टर।</figcaption>
</figure>

## चार्ट बनाने से पहले OEE को परिभाषित करना
Overall Equipment Effectiveness एक पैकेजिंग लाइन की उत्पादकता को एक संख्या में समेट देता है: Availability × Performance × Quality. अनुशासन यह है कि कुछ भी बनाने से पहले हर घटक को एक कैलकुलेटेड फ़ील्ड के रूप में सटीकता से परिभाषित किया जाए।

- **Availability** = वास्तविक रन टाइम ÷ नियोजित उत्पादन समय (ब्रेकडाउन और चेंजओवर से हुई हानि)।
- **Performance** = वास्तविक उत्पादन ÷ रेटेड गति पर सैद्धांतिक उत्पादन (छोटी रुकावटों और धीमी चाल से हुई हानि)।
- **Quality** = अच्छी इकाइयाँ ÷ कुल उत्पादित इकाइयाँ (रिजेक्ट और दोबारा काम से हुई हानि)।

इन तीनों को गुणा करें और आपको OEE मिल जाता है। इन्हें एक साफ़ डेटा मॉडल पर नामित कैलकुलेटेड फ़ील्ड के रूप में बनाएँ — प्रति उत्पादन रन या प्रति शिफ्ट प्रति लाइन एक पंक्ति, जिसमें नियोजित समय, रन टाइम, गिनती और रिजेक्ट गिनती हो — और बाक़ी डैशबोर्ड बस जोड़-तोड़ है। यह "पहले माप" वाली कठोरता मायने रखती है क्योंकि हर घटक अलग समस्या की ओर इशारा करता है; एक अकेली OEE संख्या यह छिपा लेती है कि आप रुकावटों, गति या स्क्रैप में हार रहे हैं।

## डैशबोर्ड बनाना
OEE प्रतिशत को एक BAN (बड़ी एग्रीगेट संख्या) और लक्ष्य के विरुद्ध एक गेज के साथ शीर्षक के रूप में दिखाएँ। इसके नीचे Availability, Performance और Quality को अलग-अलग दिखाएँ ताकि कहानी पठनीय रहे — कमज़ोर availability से बना 85% OEE, कमज़ोर quality से बने 85% OEE से बिल्कुल अलग समस्या है।

मुख्य रूप से काम करने वाला व्यू है **डाउनटाइम के कारणों का एक Pareto**: हर कारण के अनुसार खोए गए मिनटों की बार बनाएँ, अवरोही क्रम में, और एक रनिंग-टोटल टेबल कैलकुलेशन से संचयी रेखा खींचें। यहीं Tableau की टेबल कैलक अपनी जगह बनाती हैं। एक **parameter** उपयोगकर्ता को लाइन और शिफ्ट चुनने देता है, बिना नई शीट के संदर्भ बदलते हुए; parameter actions इसे क्लिक-आधारित बना देते हैं। OEE को समय के साथ ट्रेंड करें, लक्ष्य के लिए एक रेफरेंस रेखा डालें, और एक filter action जोड़ें ताकि किसी दिन पर क्लिक करने से उस शिफ्ट के रन और रुकावटों में ड्रिल हो सके।

भविष्यवाणी के लिए — दर्ज किए गए डाउनटाइम को *भविष्य* के डाउनटाइम के अनुमान में बदलने के लिए — Tableau अपने आप में ग़लत उपकरण है; वह एक मॉडलिंग का काम है। इसका स्वाभाविक साथी है [पैकेजिंग-लाइन OEE और डाउनटाइम भविष्यवाणी]({{ '/hi/2024/packaging-line-oee-downtime-prediction/' | relative_url }}), जहाँ एक बाहरी मॉडल पूर्वानुमान करता है और Tableau नतीजे को विज़ुअलाइज़ करता है। एक जनरेटिव-AI सारांश सप्ताह के Pareto को उत्पादन बैठक के लिए एक छोटी कथा में भी बदल सकता है, जिसे एक मैनेजर परखता है।

## जहाँ यह टूटता है
यहाँ असहज सच्चाई है: कचरा डाउनटाइम कोडिंग अंदर, तो कचरा OEE बाहर। Availability और Performance घटक पूरी तरह इस पर निर्भर करते हैं कि ऑपरेटर रुकावटों को सटीक और संगत ढंग से दर्ज करें। अगर आधी माइक्रो-स्टॉप कभी दर्ज ही नहीं होतीं, तो Performance ठीक दिखता है जबकि लाइन रेंगती रहती है। अगर हर अस्पष्ट रुकावट "other" के नीचे दर्ज होती है, तो आपका Pareto एक अकेली बेकार बार बन जाता है। Tableau की कोई चमक-दमक इसे ठीक नहीं करती — डैशबोर्ड ईमानदारी से वही दिखाता है जो लाइन क्लर्क ने टाइप किया।

AI परत की भी यही निर्भरता है। Tableau Pulse OEE पर नज़र रख सकता है और गिरावट को चिह्नित कर सकता है, और Explain Data सुझा सकता है कि कौन-सा कारक बदला, पर दोनों दर्ज किए गए डेटा पर ही तर्क करते हैं। वे ऐसी रुकावट को वापस नहीं ला सकते जिसे किसी ने दर्ज ही नहीं किया। समाधान ऊपर की धारा में है: एक कसा हुआ, अच्छी तरह प्रशिक्षित डाउनटाइम-कारण वर्गीकरण और अनुशासित कैप्चर, आदर्श रूप से लाइन के अपने काउंटर से अर्ध-स्वचालित। इसे सही करें और OEE ब्रूअरी की सबसे क्रियाशील संख्याओं में से एक बन जाता है; इसे ग़लत करें और यह महज़ नाटक है।

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="प्रक्रिया को क्या चलाता है, और यह आगे की धारा में क्या बदलता है।"><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">इसे क्या चलाता है</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Tableau में पैकेजिंग-लाइन OEE को विज़ुअलाइज़ करना</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">इनपुट 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">इनपुट 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">इनपुट 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">प्रक्रिया</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">गुणवत्ता</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">लागत / जोखिम</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">प्रक्रिया को क्या चलाता है, और यह आगे की धारा में क्या बदलता है।</figcaption>
</figure>

## निचोड़
एक Tableau OEE डैशबोर्ड तीन स्पष्ट कैलकुलेटेड फ़ील्ड, डाउनटाइम का एक Pareto, और लाइन व शिफ्ट के अनुसार काटने के लिए parameter है। यह आपको ठीक-ठीक बता देगा कि आपकी पैकेजिंग हानि कहाँ बसती है — पर तभी जब डाउनटाइम डेटा ईमानदारी से दर्ज हुआ हो। पहले कैप्चर ठीक करें, फिर Tableau को हानियों को नज़रअंदाज़ करना असंभव बना देने दें।

*[Brewing Science & AI]({{ '/hi/tracks/brewing-science-ai/' | relative_url }}) ट्रैक का हिस्सा।* संबंधित: [पैकेजिंग-लाइन OEE और डाउनटाइम भविष्यवाणी]({{ '/hi/2024/packaging-line-oee-downtime-prediction/' | relative_url }})।

## अक्सर पूछे जाने वाले प्रश्न

**OEE को Tableau कैलकुलेटेड फ़ील्ड के रूप में कैसे निकाला जाता है?**
OEE, Availability गुणा Performance गुणा Quality है, और इनमें से हर एक एक अनुपात है जिसे आप कैलकुलेटेड फ़ील्ड के रूप में बनाते हैं: Availability यानी रन टाइम बँटा नियोजित समय, Performance यानी वास्तविक उत्पादन बँटा सैद्धांतिक उत्पादन, और Quality यानी अच्छी इकाइयाँ बँटा कुल इकाइयाँ। इन तीनों का गुणनफल आपका OEE प्रतिशत है।

**OEE डैशबोर्ड पर सबसे उपयोगी चार्ट कौन-सा है?**
डाउनटाइम के कारणों का एक Pareto। यह उपलब्धता की हानि के कारणों को क्रम में रखता है, ताकि आप उन कुछ अहम रुकावटों को देख सकें जो अधिकांश हानि के लिए ज़िम्मेदार हैं — और आमतौर पर यहीं सबसे तेज़ सुधार मिलता है।

**मेरा OEE गलत क्यों दिखता है?**
लगभग हमेशा इसलिए कि लाइन पर डाउनटाइम को किस तरह कोड किया जाता है। अगर ऑपरेटर रुकावटों को असंगत ढंग से दर्ज करते हैं या सब कुछ ‘other’ में डाल देते हैं, तो Availability घटक — और इसलिए OEE — अविश्वसनीय हो जाता है। गणित उतना ही अच्छा है जितना डाउनटाइम डेटा।
