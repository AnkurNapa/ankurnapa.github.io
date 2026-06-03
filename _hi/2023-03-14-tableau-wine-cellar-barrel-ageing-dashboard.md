---
layout: post
lang: hi
title: "Tableau में सेलर और बैरल-एजिंग इन्वेंटरी डैशबोर्ड"
image: /assets/og/tableau-wine-cellar-barrel-ageing-dashboard.png
description: "LOD के ज़रिए बैरलों को प्रकार और उम्र के अनुसार ट्रैक करने वाला Tableau सेलर डैशबोर्ड बनाएं — टॉप-अप और वाष्पीकरण, SO2 स्थिति और Pulse अलर्ट के साथ एजिंग टाइमलाइन।"
date: 2023-03-14
updated: 2023-03-14
permalink: /hi/2023/tableau-wine-cellar-barrel-ageing-dashboard/
tags: [winemaking, tableau, inventory]
faq:
  - q: "Tableau में बैरलों को लॉट के अनुसार कैसे एकत्र करूँ?"
    a: "लॉट पर आधारित एक FIXED level-of-detail गणना का उपयोग करें, जैसे प्रति लॉट कुल वॉल्यूम या औसत फ्री SO2। इससे आपको प्रति-लॉट का साफ रोलअप मिलता है, भले ही हर पंक्ति एक अकेला बैरल हो।"
  - q: "क्या Tableau बैरल वाष्पीकरण को ट्रैक कर सकता है?"
    a: "हाँ, अगर आप टॉप-अप लॉग करते हैं। समय के साथ प्रति बैरल जोड़े गए वॉल्यूम की गणना करें और डैशबोर्ड वाष्पीकरण को एक रनिंग टॉप-अप कुल के रूप में दिखाता है, जो अपेक्षा से अधिक नुकसान वाले बैरलों को भी चिह्नित करता है।"
  - q: "क्या Tableau Pulse मुझे बताएगा कि कौन-से बैरल देय हैं?"
    a: "Pulse आपके परिभाषित मीट्रिक पर नज़र रखता है, जैसे अंतिम SO2 जाँच के बाद के दिन या बैरल में बीते महीने, और एक डाइजेस्ट भेजता है जो आपकी सीमा पार करने वाले बैरलों के नाम बताता है। यह सूची सामने लाता है; काम अब भी सेलर ही करता है।"
---

**संक्षिप्त उत्तर: एक सेलर डैशबोर्ड तब बनाने लायक होता है जब वह इस सवाल का जवाब दे कि बैरल में क्या है, कितना पुराना है, और किन बैरलों पर ध्यान चाहिए — बिना किसी के दिमाग में सेलर का नक्शा खोले।** कुछ भी बनाने से पहले रोलअप ग्रेन — बैरल, लॉट, प्रकार — तय करें।

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Tableau में सेलर और बैरल-एजिंग इन्वेंटरी डैशबोर्ड के लिए सामान्य डैशबोर्ड लेआउट"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">डैशबोर्ड लेआउट</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Tableau में सेलर और बैरल-एजिंग इन्वेंटरी डैशबोर्ड</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">फ़िल्टर:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">ट्रेंड</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">विभाजन</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">इस डैशबोर्ड का एक सामान्य लेआउट: ऊपर मुख्य मीट्रिक, नीचे एक ट्रेंड और एक विभाजन, इसे काटने के लिए फ़िल्टर।</figcaption>
</figure>

## पहले सेलर ग्रेन का मॉडल बनाएं
बैरल डेटा पदानुक्रमिक होता है, इसलिए बनाने से पहले अपने स्तर तय करें: अलग-अलग बैरल, लॉट, बैरल प्रकार (नया बनाम इस्तेमाल किया हुआ ओक), और विंटेज। आपके स्रोत में हर पंक्ति आमतौर पर एक बैरल होती है जिसमें विशेषताएं होती हैं — भरने की तारीख, ओक प्रकार, लॉट, अंतिम टॉप-अप, फ्री और कुल SO2। मेज़र-फर्स्ट अनुशासन का मतलब है कि उसे दृश्य रूप देने से पहले यह तय करना कि टॉप-अप के लिए देय बैरल या SO2 पर जोखिम वाला बैरल का वास्तव में क्या अर्थ है।

सेलर डेटा अक्सर हाथ से लॉग किया जाता है, इसलिए लाइव फ़ीड के पीछे भागने के बजाय एक रिफ्रेश किया गया एक्सट्रैक्ट कनेक्ट करें, और स्प्रेडशीटों के बीच खिसकने वाले बैरल आईडी को मिलाने के लिए Tableau Prep का उपयोग करें। Level-of-detail गणनाएं भारी काम संभालती हैं: `{FIXED [Lot] : SUM([Volume])}` प्रति लॉट लीटर देता है, और एक INCLUDE एक्सप्रेशन आपको बैरल ग्रेन पर फ्री SO2 का औसत निकालने देता है जबकि उसे लॉट के अनुसार दिखाता है।

## इन्वेंटरी और एजिंग व्यू
ओक प्रकार से रंगे और वॉल्यूम से आकार दिए बैरलों का एक मैट्रिक्स बनाएं, जो लॉट और विंटेज से फ़िल्टर हो — एक नज़र में सेलर। उसके बगल में, एक एजिंग टाइमलाइन हर लॉट के बैरल में बीते महीनों को एक पैरामीटर में रखे लक्ष्य एजिंग विंडो के सामने प्लॉट करती है, ताकि अपनी योजना से आगे खिसकता कोई लॉट स्पष्ट हो जाए।

टॉप-अप और वाष्पीकरण को प्रति बैरल जोड़े गए लीटर के रनिंग टोटल के रूप में ट्रैक करें; अपने पड़ोसियों से कहीं अधिक टॉप-अप माँगता बैरल या तो प्यासा ओक है या कोई समस्या। एक SO2 स्थिति व्यू हर बैरल को आपके फ्री-SO2 फ्लोर के सामने लाल, एम्बर या हरा रंग देता है, एक फ़िल्टर एक्शन के साथ ताकि किसी लॉट पर क्लिक करने से उसके बैरल दिखें। पैरामीटर एक्शन आपको एजिंग लक्ष्य को लचीला बनाने और देखने देते हैं कि कौन-से लॉट योजना में आते या बाहर जाते हैं।

## जो देय है, उसे Pulse को चिह्नित करने दें
Tableau Pulse को SO2 जाँच से पिछड़े बैरल और एजिंग विंडो के अंत के निकट पहुँचते लॉट पर सेट करें। यह उन मीट्रिक पर नज़र रखता है और एक डाइजेस्ट भेजता है जो रेखा पार करने वाले बैरलों और लॉटों के नाम बताता है — सेलर की सुबह की टू-डू सूची, सादी भाषा में लिखी। जब किसी एक लॉट का SO2 बाकियों से तेज़ी से गिर रहा हो तब Einstein का Explain Data मदद कर सकता है, उन फ़ील्डों की ओर इशारा करते हुए जो अलग हैं।

## जहाँ यह टूटता है
स्पष्ट सीमाएं डेटा और जीवविज्ञान के बारे में हैं। सेलर डेटा काफी हद तक मैनुअल है, इसलिए डैशबोर्ड उतना ही ताज़ा है जितना लॉग में अंतिम बार लिखने वाला व्यक्ति; एक बैरल जिसे टॉप-अप किया गया पर कभी दर्ज नहीं किया गया, वह उपेक्षित दिखता है। बैरल-दर-बैरल भिन्नता वास्तविक है — एक ही ओक और उम्र के दो बैरल बहुत अलग तरह से उम्र पा सकते हैं — इसलिए प्रकार के अनुसार एक समुच्चय उन व्यक्तिगत आउटलायर्स को छिपा देता है जो ब्लेंडिंग में मायने रखते हैं। और डैशबोर्ड एजिंग को ट्रैक करता है; यह आपको नहीं बता सकता कि वाइन तैयार है। वह एक बेंच-ट्रायल और स्वाद का निर्णय है, और एक AI गुणवत्ता मॉडल भी एक चखने के बजाय एक अनुमान है।

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="बैरल एजिंग को क्या चलाता है, और यह आगे क्या बदलता है।"><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">इसे क्या चलाता है</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Tableau में सेलर और बैरल-एजिंग इन्वेंटरी डैशबोर्ड</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">बैरल एजिंग</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">गुणवत्ता</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">लागत / जोखिम</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">बैरल एजिंग को क्या चलाता है, और यह आगे क्या बदलता है।</figcaption>
</figure>

## निचोड़
एक Tableau सेलर डैशबोर्ड एक बिखरे हुए बैरल लॉग को एक प्रबंधित इन्वेंटरी में बदल देता है: लॉट और प्रकार के अनुसार LOD रोलअप, टॉप-अप और वाष्पीकरण ट्रैकिंग, SO2 स्थिति, और एक एजिंग टाइमलाइन, जिसमें Pulse देय बैरलों के नाम बताता है। डेटा को ताज़ा रखें और याद रखें कि यह एजिंग को ट्रैक करता है, तत्परता को नहीं।

*[Winemaking & AI]({{ '/hi/tracks/winemaking-ai/' | relative_url }}) ट्रैक का हिस्सा।* संबंधित: [क्या AI वाइन की गुणवत्ता का पूर्वानुमान लगा सकता है?]({{ '/hi/2026/can-ai-predict-wine-quality/' | relative_url }})।

## अक्सर पूछे जाने वाले सवाल

**Tableau में बैरलों को लॉट के अनुसार कैसे एकत्र करूँ?**
लॉट पर आधारित एक FIXED level-of-detail गणना का उपयोग करें, जैसे प्रति लॉट कुल वॉल्यूम या औसत फ्री SO2। इससे आपको प्रति-लॉट का साफ रोलअप मिलता है, भले ही हर पंक्ति एक अकेला बैरल हो।

**क्या Tableau बैरल वाष्पीकरण को ट्रैक कर सकता है?**
हाँ, अगर आप टॉप-अप लॉग करते हैं। समय के साथ प्रति बैरल जोड़े गए वॉल्यूम की गणना करें और डैशबोर्ड वाष्पीकरण को एक रनिंग टॉप-अप कुल के रूप में दिखाता है, जो अपेक्षा से अधिक नुकसान वाले बैरलों को भी चिह्नित करता है।

**क्या Tableau Pulse मुझे बताएगा कि कौन-से बैरल देय हैं?**
Pulse आपके परिभाषित मीट्रिक पर नज़र रखता है, जैसे अंतिम SO2 जाँच के बाद के दिन या बैरल में बीते महीने, और एक डाइजेस्ट भेजता है जो आपकी सीमा पार करने वाले बैरलों के नाम बताता है। यह सूची सामने लाता है; काम अब भी सेलर ही करता है।
