---
layout: post
lang: hi
title: "Tableau में वाइन किण्वन निगरानी डैशबोर्ड"
image: /assets/og/tableau-wine-fermentation-dashboard.png
description: "Explain Data डायग्नोस्टिक्स के साथ प्रति-टैंक Brix और तापमान वक्र, अटके-किण्वन फ़्लैग और YAN को ट्रैक करने वाला एक Tableau किण्वन डैशबोर्ड बनाएँ।"
date: 2023-02-14
updated: 2023-02-14
permalink: /hi/2023/tableau-wine-fermentation-dashboard/
tags: [winemaking, tableau, fermentation]
faq:
  - q: "Tableau में किण्वन डैशबोर्ड को वास्तव में क्या दिखाना चाहिए?"
    a: "एक लक्ष्य बैंड के विरुद्ध प्रति-टैंक Brix अवरोहण और तापमान, साथ ही एक अटके-किण्वन फ़्लैग और शुरुआती YAN रीडिंग। ये चारों मिलकर बताते हैं कि प्रत्येक टैंक सही राह पर है या उसे हस्तक्षेप की ज़रूरत है।"
  - q: "क्या Tableau अटके हुए किण्वन का पता लगा सकता है?"
    a: "यह लक्षण को चिह्नित कर सकता है — एक Brix वक्र जो सूखेपन से ऊपर समतल हो गया है — एक परिकलित फ़ील्ड का उपयोग करके जो नवीनतम रीडिंग की तुलना पिछले दिनों से करता है। यह कारण का निदान नहीं कर सकता; उसके लिए अब भी एक सेलर हैंड और एक लैब की ज़रूरत होती है।"
  - q: "क्या Explain Data किण्वन टैंकों पर काम करता है?"
    a: "Explain Data यह उभार सकता है कि आपके डेटा में कौन-से फ़ील्ड किसी धीमे टैंक से सहसंबद्ध हैं, जैसे कम YAN या तापमान में गिरावट। इसके परिणाम को जाँच का संकेत मानें, फ़ैसला नहीं।"
---

**संक्षिप्त उत्तर: एक किण्वन डैशबोर्ड तभी अपनी जगह सार्थक करता है जब वह हर टैंक के Brix अवरोहण को एक ही स्क्रीन पर तापमान बैंड के विरुद्ध दिखाए, ताकि एक सुस्त किण्वन रुकने से पहले ही स्पष्ट दिख जाए।** पहले लक्ष्य बैंड तय करें; चार्ट उसके बाद आते हैं।

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Tableau में वाइन किण्वन निगरानी डैशबोर्ड के लिए सामान्य डैशबोर्ड लेआउट"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">डैशबोर्ड लेआउट</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Tableau में वाइन किण्वन निगरानी डैशबोर्ड</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">फ़िल्टर:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">रुझान</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">विभाजन</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">इस डैशबोर्ड के लिए एक सामान्य लेआउट: ऊपर मुख्य मेट्रिक्स, नीचे एक रुझान और एक विभाजन, और इसे काटने के लिए फ़िल्टर।</figcaption>
</figure>

## बनाने से पहले बैंड तय करें
डेटा साइंस की आदत — पहले मापो — सेलर में बगीचे से भी अधिक मायने रखती है, क्योंकि किण्वन घंटों में आगे बढ़ता है। अपनी लक्ष्य खिड़कियाँ पहले ही तय करें: सफ़ेद वाइन लगभग 12 से 18 °C पर ठंडी किण्वित होती हैं, लाल 25 से 30 °C पर गर्म, और शुरुआती YAN आदर्श रूप से कहीं लगभग 150 से 250 mg/L के आसपास उतरता है। ये संख्याएँ पैरामीटर और संदर्भ बैंड बनती हैं, हार्ड-कोडेड निशान नहीं, ताकि एक वाइनमेकर वर्कबुक संपादित किए बिना सफ़ेद-किण्वन की सीमा को बदल सके।

आपका स्रोत आमतौर पर एक टैंक-लॉगिंग सिस्टम होता है या एक शीट में निर्यात किया गया मैनुअल लॉग। चरम किण्वन के दौरान एक लाइव कनेक्शन आदर्श है; अन्यथा एक बार-बार ताज़ा किया गया .hyper एक्सट्रैक्ट ठीक है। Tableau Prep वर्ष के बीच टैंक नाम बदलने की अनिवार्य गड़बड़ी को साफ़ करता है और लैब के YAN परिणामों को सेलर के तापमान लॉग के साथ मिलाता है।

## प्रति-टैंक स्मॉल मल्टीपल
सबसे काम का दृश्य एक स्मॉल-मल्टीपल ग्रिड है: प्रति टैंक एक मिनी-चार्ट, अक्ष पर समय, अवरोही रेखा पर Brix, और लक्ष्य तापमान बैंड एक छायांकित संदर्भ के रूप में खींचा गया। Brix रेखा को इस आधार पर रंग दें कि नवीनतम तापमान बैंड के भीतर बैठता है या बाहर, और सेलर सेकंडों में पढ़ लेता है।

एक FIXED स्तर-विस्तार परिकलन प्रत्येक टैंक के शुरुआती Brix को स्थिर करता है — `{FIXED [Tank] : MIN([Brix])}` — ताकि आप यह गणना कर सकें कि कितने प्रतिशत शर्करा खपत हुई, चाहे टैंक में कितनी भी रीडिंग हों। एक अटके-किण्वन फ़्लैग एक टेबल कैल्कुलेशन है जो नवीनतम Brix की तुलना दो या तीन दिन पहले की रीडिंग से करता है: यदि यह मुश्किल से हिला है और सूखेपन से ऊपर बैठा है, तो टैंक लाल हो जाता है। एक पैरामीटर एक्शन जोड़ें ताकि किसी टैंक पर क्लिक करने से उसका पूरा विवरण दृश्य YAN और मैलोलैक्टिक स्थिति के साथ लोड हो जाए।

## Explain Data को धीमे टैंक से पूछताछ करने दें
जब एक टैंक पिछड़ जाए, तो मार्क पर राइट-क्लिक करें और Explain Data चलाएँ। Einstein का Explain Data अन्य फ़ील्ड्स को स्कैन करता है और रिपोर्ट करता है कि सांख्यिकीय रूप से उस टैंक को क्या अलग करता है — शायद यह कम YAN के साथ शुरू हुआ, या इसका तापमान रात भर में गिर गया। यह एक तेज़, उपयोगी संकेत है। Tableau Pulse, सेलर-व्यापी "लक्ष्य से बाहर टैंक" मेट्रिक पर सेट, एक सुबह का सारांश भेजता है ताकि टीम जान सके कि पहले किसके पास चलकर जाना है।

## यह कहाँ टूटता है
ईमानदार सीमाएँ कैडेंस और जीवविज्ञान के बारे में हैं। यदि आपके सेंसर हर छह घंटे में लॉग करते हैं, तो डैशबोर्ड एक ऐसे तापमान शिखर को नहीं पकड़ सकता जो बीच में चरम पर पहुँचकर गुज़र जाए। प्राकृतिक और जंगली किण्वन स्वभाव से अनियमित होते हैं — एक समतल Brix वक्र शायद एक स्वस्थ लैग फ़ेज़ हो, रुकावट नहीं — इसलिए एक भोला अटके-किण्वन फ़्लैग एक धीमे-पर-ठीक टैंक पर झूठा अलार्म बजाएगा। Explain Data केवल वही कॉलम जानता है जो आपने उसे दिए; यह कभी सुझाव नहीं देगा कि असली दोषी एक पोषक तत्व जोड़ था जिसे किसी ने लॉग नहीं किया। और कोई डैशबोर्ड SO2 का प्रबंधन नहीं करता या रेंगती हुई वोलेटाइल अम्लता को सूँघता नहीं; वह एक मानवीय काम बना रहता है।

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="एक बंद नियंत्रण लूप: मापें, गणना करें, क्रियान्वित करें — फिर परिणाम को वापस फ़ीड करें।"><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">नियंत्रण लूप</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Tableau में वाइन किण्वन निगरानी डैशबोर्ड</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">सेंसर</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">नियंत्रक</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">एक्चुएटर</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">प्रक्रिया</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">फ़ीडबैक</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">एक बंद नियंत्रण लूप: मापें, गणना करें, क्रियान्वित करें — फिर परिणाम को वापस फ़ीड करें।</figcaption>
</figure>

## निचोड़
एक Tableau किण्वन डैशबोर्ड एक पूर्व-चेतावनी ग्रिड है: एक तापमान बैंड के विरुद्ध प्रति-टैंक Brix, एक अटके-किण्वन फ़्लैग, और YAN संदर्भ, जिसमें Explain Data और Pulse आपको उस टैंक की ओर इशारा करते हैं जिसे ध्यान चाहिए। लक्ष्य बैंड को पैरामीटर के रूप में सेट करें, अपने सेंसर कैडेंस का सम्मान करें, और याद रखें कि डैशबोर्ड लक्षण चिह्नित करता है जबकि सेलर कारणों का निदान करता है।

*[Winemaking & AI]({{ '/hi/tracks/winemaking-ai/' | relative_url }}) ट्रैक का हिस्सा।* संबंधित: [AI वाइन किण्वन नियंत्रण]({{ '/hi/2024/ai-wine-fermentation-control/' | relative_url }})।

## अक्सर पूछे जाने वाले प्रश्न

**Tableau में किण्वन डैशबोर्ड को वास्तव में क्या दिखाना चाहिए?**
एक लक्ष्य बैंड के विरुद्ध प्रति-टैंक Brix अवरोहण और तापमान, साथ ही एक अटके-किण्वन फ़्लैग और शुरुआती YAN रीडिंग। ये चारों मिलकर बताते हैं कि प्रत्येक टैंक सही राह पर है या उसे हस्तक्षेप की ज़रूरत है।

**क्या Tableau अटके हुए किण्वन का पता लगा सकता है?**
यह लक्षण को चिह्नित कर सकता है — एक Brix वक्र जो सूखेपन से ऊपर समतल हो गया है — एक परिकलित फ़ील्ड का उपयोग करके जो नवीनतम रीडिंग की तुलना पिछले दिनों से करता है। यह कारण का निदान नहीं कर सकता; उसके लिए अब भी एक सेलर हैंड और एक लैब की ज़रूरत होती है।

**क्या Explain Data किण्वन टैंकों पर काम करता है?**
Explain Data यह उभार सकता है कि आपके डेटा में कौन-से फ़ील्ड किसी धीमे टैंक से सहसंबद्ध हैं, जैसे कम YAN या तापमान में गिरावट। इसके परिणाम को जाँच का संकेत मानें, फ़ैसला नहीं।
