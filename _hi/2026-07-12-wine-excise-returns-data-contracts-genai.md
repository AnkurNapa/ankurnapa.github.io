---
layout: post
lang: hi
title: "Data contracts के रूप में excise returns: टेस्ट मिलान करते हैं, LLM ड्राफ़्ट बनाता है, व्यक्ति हस्ताक्षर करता है"
image: /assets/og/wine-excise-returns-data-contracts-genai.png
description: "The Cellar Ledger का भाग 5। वाइनरी का excise return हर tax class के लिए एक बैलेंस समीकरण है। इसके इनपुट को data contract मानिए, समीकरण को हर रात पाइपलाइन में टेस्ट कीजिए, और GenAI का इस्तेमाल वहाँ कीजिए जहाँ वह यहाँ अच्छा है: गड़बड़ removal नोट्स को वर्गों में बाँटना, स्पष्टीकरण का ड्राफ़्ट बनाना और मार्गदर्शन का सही पैराग्राफ़ ढूँढना।"
date: 2026-07-12 09:00:00 -0700
updated: 2026-07-12
permalink: /hi/2026/wine-excise-returns-data-contracts-genai/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, compliance]
faq:
  - q: "वाइनरी के संदर्भ में data contract क्या है?"
    a: "यह एक लिखित और लागू किया गया समझौता है कि किसी dataset में क्या होना ज़रूरी है। excise के लिए movement ledger पर contract कह सकता है कि हर removal की एक tax class, एक गंतव्य प्रकार और एक मापा गया अल्कोहल हो, और हर महीने का opening balance पिछले महीने के closing के बराबर हो। पाइपलाइन इन नियमों को टेस्ट करती है और खराब रिकॉर्ड को return तक पहुँचने से पहले रोक देती है।"
  - q: "क्या एक LLM वाइन excise return भर सकता है?"
    a: "उसे संख्याएँ नहीं भरनी चाहिए। आँकड़े ledger पर चलने वाली परखी हुई क्वेरी से आते हैं। LLM return के आसपास काम का है: free-text removal नोट्स को श्रेणियों में बाँटना, किसी असामान्य नुकसान के स्पष्टीकरण का ड्राफ़्ट बनाना, और किसी व्यक्ति के पढ़ने के लिए संबंधित मार्गदर्शन पैराग्राफ़ ढूँढना। हर return की समीक्षा और हस्ताक्षर एक नामित व्यक्ति करता है।"
  - q: "वाइन की tax classes मिलान में समस्या क्यों पैदा करती हैं?"
    a: "क्योंकि एक लॉट इमारत छोड़े बिना अपनी class बदल सकता है। उदाहरण के लिए US में still wine पर अल्कोहल के हिसाब से बैंड में टैक्स लगता है, और 16 प्रतिशत पर एक रेखा है। blending, fortification या सुधारा गया लैब नतीजा किसी लॉट को उस रेखा के पार ले जा सकता है, और अगर बदलाव event के रूप में दर्ज न हो, तो प्रति-class बैलेंस का जोड़ मिलना बंद हो जाता है।"
---

**संक्षिप्त उत्तर: excise return हर tax class के लिए एक बैलेंस समीकरण है: opening, जोड़ उत्पादित और प्राप्त, घटा removals और नुकसान, बराबर closing। अगर यह समीकरण महीने के अंत में हाथ से फ़ॉर्म में कॉपी किया जाता है, तो हर गलती सबसे बुरे समय पर सामने आती है। return के इनपुट को movement ledger पर एक data contract मानिए, समीकरण को हर रात पाइपलाइन में टेस्ट कीजिए, और return एक ऐसी क्वेरी बन जाता है जो अपनी जाँचें पहले ही पास कर चुकी है। GenAI किनारों पर मदद करता है: गड़बड़ removal नोट्स छाँटना, किसी अजीब नुकसान के स्पष्टीकरण का ड्राफ़्ट बनाना, और मार्गदर्शन का सही पैराग्राफ़ ढूँढना। वह आँकड़े नहीं बनाता, और हस्ताक्षर नहीं करता।**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एक tax class के लिए excise बैलेंस समीकरण: opening balance, जोड़ उत्पादित और प्राप्त, घटा tax-paid removals, घटा in bond ट्रांसफ़र या निर्यात, घटा नुकसान, बराबर closing balance। नीचे data contract के तीन रात्रिकालीन टेस्ट: opening पिछले महीने के closing के बराबर, समीकरण हर class के लिए शून्य पर संतुलित, और हर class बदलाव event के रूप में दर्ज। एक बैनर कहता है कि return एक ऐसी क्वेरी है जो अपने टेस्ट पहले ही पास कर चुकी है।">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एक TAX CLASS, एक समीकरण, हर रात टेस्ट</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="95" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">opening</text>
<text x="95" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="177" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">+</text>
<rect x="195" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">उत्पादित</text>
<text x="260" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; प्राप्त</text>
<text x="342" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="360" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="425" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">removed</text>
<text x="425" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">tax-paid</text>
<text x="507" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="525" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="590" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">in bond</text>
<text x="590" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; निर्यात</text>
<text x="672" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="690" y="60" width="110" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="745" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">नुकसान</text>
<text x="817" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">=</text>
<rect x="835" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="900" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">closing</text>
<text x="900" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="500" y="160" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">DATA CONTRACT टेस्ट</text>
<rect x="30" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="180" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; opening = पिछला closing</text>
<text x="180" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">महीनों के बीच कोई चुपचाप एडिट नहीं</text>
<rect x="350" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; समीकरण 0 पर संतुलित</text>
<text x="500" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">हर tax class, हर महीने</text>
<rect x="670" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="820" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; class बदलाव events हैं</text>
<text x="820" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">16% के पार blend दर्ज होता है</text>
<rect x="30" y="262" width="940" height="42" rx="10" fill="#06483f"/>
<text x="500" y="288" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">RETURN एक ऐसी क्वेरी है जो अपने टेस्ट पहले ही पास कर चुकी है</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">वही समीकरण जो excise अधिकारी जाँचता है, महीने के अंत में किसी व्यक्ति की बजाय हर रात पाइपलाइन द्वारा टेस्ट किया गया।</figcaption>
</figure>

महीने का दूसरा कामकाजी दिन है और excise return जमा होना है। कोई पिछले महीने का return खोलता है, सेलर सिस्टम खोलता है, और फ़ॉर्म में संख्याएँ कॉपी करना शुरू करता है। opening balance पिछले महीने के closing से मेल नहीं खाता। बीच में किसी ने एक टैंक का वॉल्यूम एडिट कर दिया। अगले तीन घंटे यह ढूँढने में जाते हैं कि कौन सा, और इस बीच deadline नज़दीक आती जाती है।

यह सीरीज़ की सबसे कम चमकदार और शायद सबसे काम की पोस्ट है। duty भरने वाली हर वाइनरी इसके साथ जीती है, और उनमें से ज़्यादातर इसे एक व्यक्ति और एक कैलकुलेटर से हल करती हैं। [movement ledger]({{ '/hi/2026/event-sourced-cellar-records-winery/' | relative_url }}) और [loss map]({{ '/hi/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) ज़्यादातर काम पहले ही कर चुके हैं। यह पोस्ट वे नियम जोड़ती है जो किसी के फ़ॉर्म खोलने से पहले ही return को भरोसेमंद बना देते हैं।

## return एक बैलेंस समीकरण है

देश कोई भी हो, वाइनरी का excise return हर tax class के लिए एक ही समीकरण पर आता है:

> opening + उत्पादित और प्राप्त - tax-paid removals - in bond ट्रांसफ़र या निर्यात - नुकसान = closing

US में यह मासिक Report of Wine Premises Operations है, tax class के हिसाब से बँटा हुआ। EU में duty-suspended movements EMCS के ज़रिए चलते हैं। भारत में हर राज्य के excise विभाग के अपने रजिस्टर और फ़ॉर्मेट हैं। फ़ॉर्म अलग हैं। गणित नहीं।

डेटा टीम के लिए यह अच्छी खबर है, क्योंकि समीकरण एक ऐसी चीज़ है जिसे पाइपलाइन टेस्ट कर सकती है।

## tax class का जाल

बारीक हिस्सा है "हर tax class के लिए"। वाइन पर बैंड में टैक्स लगता है। US में 16% या उससे कम अल्कोहल वाली still wine एक class है, 16 से ऊपर 21% तक दूसरी, 21 से ऊपर 24% तक तीसरी, और sparkling व carbonated वाइन अलग। दूसरे बाज़ार अपनी रेखाएँ खींचते हैं।

एक लॉट इमारत छोड़े बिना class बदल सकता है। 15.8% वाले लॉट को 16.6% वाले लॉट के साथ blend कीजिए, और वॉल्यूम के हिसाब से नतीजा 16% के किसी भी तरफ़ बैठ सकता है। fortify कीजिए, और लॉट class कूद जाता है। कोई लैब नतीजा सुधारिए, और जो लॉट पिछले महीने 16% से नीचे बताया गया था, वह उसके ऊपर निकलता है।

अगर ये बदलाव दर्ज न हों, तो प्रति-class समीकरण संतुलित होना बंद हो जाता है, और किसी को नहीं पता कि क्यों। इसलिए class बदलाव खुद ledger में एक event बन जाता है: लॉट 24-SH-03 इस तारीख को, इस वॉल्यूम के साथ, इस blend की वजह से class A से class B में गया। यही कारण है कि इस सीरीज़ की [पहली पोस्ट]({{ '/hi/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) ने ज़ोर दिया था कि मापा गया अल्कोहल अनुमानित अल्कोहल की जगह ले। अंगूठे के नियम वाले रूपांतरण पर टिकी tax class एक ऐसी समस्या है जो बस किसी ऑडिटर का इंतज़ार कर रही है।

## data contract लिखना

data contract एक लिखित समझौता है कि किसी dataset में क्या होना ज़रूरी है, जिसे अच्छे इरादों की बजाय पाइपलाइन लागू करती है। excise के लिए movement ledger पर contract छोटा है:

1. **हर removal की एक tax class, एक गंतव्य प्रकार और एक मापा गया अल्कोहल हो।** tax-paid, in bond, निर्यात, सैंपल, नष्ट। बिना गंतव्य वाला removal अस्वीकार होता है।
2. **हर class बदलाव एक event है।** अगर किसी लॉट का मापा गया अल्कोहल class की सीमा पार करता है, तो पाइपलाइन class change event की अपेक्षा करती है और उसके न होने को फ़्लैग करती है।
3. **opening बराबर पिछला closing।** हर class के लिए, हर महीने। यह एक टेस्ट हर चुपचाप हुए एडिट को पकड़ लेता है।
4. **समीकरण शून्य पर संतुलित हो।** हर class, हर महीने, उस tolerance के भीतर जिस पर आप अपने अकाउंटेंट से सहमत हों। शून्य से अलग residual तब तक return को रोकता है जब तक कोई उसे समझा न दे।
5. **कोई नेगेटिव बैलेंस नहीं।** नेगेटिव closing वॉल्यूम वाली class का मतलब है कोई event गायब है या गलत वर्ग में है।

व्यवहार में ये जो भी आप पहले से इस्तेमाल करते हैं उसमें मुट्ठी भर टेस्ट हैं: dbt tests, Great Expectations, Fabric data quality rules, या सादे SQL assertions जो रात वाले job को फ़ेल कर दें। अहम फ़ैसला यह है कि इन्हें **हर रात** चलाया जाए, महीने के अंत में नहीं। 14 तारीख को फ़ेल होने वाला टेस्ट आपको रिकॉर्ड ठीक करने के लिए दो हफ़्ते देता है, जब लोगों को अभी याद है कि क्या हुआ था। 2 तारीख को फ़ेल होने वाला टेस्ट आपको एक खराब सुबह देता है।

फ़ेल होने वाले रिकॉर्ड शून्य में नहीं, बल्कि फ़ेल हुए नियम के साथ एक quarantine टेबल में जाते हैं। सेलर टीम को ठीक करने वाली चीज़ों की एक छोटी सूची दिखती है। ठीक होने तक return उन्हें कभी नहीं देखता।

## GenAI असल में कहाँ मदद करता है

जब संख्याएँ परखी हुई क्वेरी संभाल रही हों, तो language model के लिए काम के काम वे हैं जिनमें गड़बड़ टेक्स्ट हो।

**removal नोट्स को वर्गों में बाँटना।** ऑपरेटर कुछ ऐसा लिखते हैं: "Sunday tasting को 2 cs", "टूट-फूट, pallet गिरा" या "show के लिए सैंपल"। इन्हें श्रेणियों में बदलना होता है: सैंपल, tasting room, टूट-फूट, नष्ट। मॉडल इन्हें confidence score के साथ अच्छी तरह बाँटता है, और जिसमें भी संदेह हो उसे किसी व्यक्ति के पास भेज देता है। यह छोटा काम है जो हर महीने घंटों बचाता है।

**स्पष्टीकरण का ड्राफ़्ट बनाना।** जब कोई नुकसान सामान्य से बड़ा हो, तो return या आंतरिक फ़ाइल में कारण बताने वाला नोट चाहिए। मॉडल उसे loss map के आँकड़ों और adjustment कारणों से ड्राफ़्ट करता है, उसी पैटर्न में जैसे [variance नोट]({{ '/hi/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}): हर संख्या SQL देता है, मॉडल उनके इर्द-गिर्द शब्द लिखता है।

**सही पैराग्राफ़ ढूँढना।** excise मार्गदर्शन लंबा है और अक्सर अपडेट होता है। regulator के प्रकाशित मार्गदर्शन पर एक retrieval असिस्टेंट, जो पैराग्राफ़ उद्धृत करे और उसका लिंक दे, सवाल उठने पर असली समय बचाता है: "किसी दूसरे bonded premises को top करने में इस्तेमाल हुई वाइन को कैसे दिखाएँ?"। यह एक लाइब्रेरियन है। पैराग्राफ़ पढ़कर फ़ैसला व्यक्ति ही करता है।

**अधिकारी को जवाब देना।** जब कोई excise अधिकारी पूछता है कि किसी class का बैलेंस क्यों बदला, तो ledger पढ़ने की अनुमति वाला एजेंट ठीक-ठीक events, तारीखें और ऑपरेटर निकाल सकता है, और पंक्तियाँ संलग्न करके जवाब का ड्राफ़्ट बना सकता है। जवाब किसी व्यक्ति के जाँचने के बाद जाता है।

उसे जो नहीं करना चाहिए, वह है return भरना, कानून की व्याख्या करना, या यह तय करना कि किसी धुंधले मामले वाले movement को कैसे दिखाया जाए। ये कानूनी वज़न वाले फ़ैसले हैं, और ये एक नामित व्यक्ति के हैं।

## यह कहाँ टूटता है

**नियम अलग हैं और बदलते हैं।** tax classes, अनुमत नुकसान और रिपोर्टिंग फ़ॉर्मेट देश के हिसाब से बदलते हैं, और भारत में राज्य के हिसाब से। contract में आपके नियम होने चाहिए, जिनकी समीक्षा उन्हें जानने वाला कोई व्यक्ति करे, और बदलने पर उन्हें अपडेट किया जाए।

**जो contracts महीने का अंत रोकते हैं, उन्हें बायपास कर दिया जाता है।** अगर फ़ेल होता टेस्ट 2 तारीख को return रोक दे और आगे का कोई रास्ता न हो, तो कोई न कोई उसके इर्द-गिर्द रास्ता निकाल लेगा। टेस्ट हर रात चलाइए और quarantine का रास्ता ऐसा बनाइए कि रिकॉर्ड ठीक करना पाइपलाइन के इर्द-गिर्द काम करने से आसान हो।

**अनुमत नुकसान regulatory सवाल है, statistical नहीं।** loss map बता सकता है कि कोई नुकसान असामान्य है। वह regulator की अनुमति के भीतर है या नहीं, और उस पर टैक्स लगेगा या नहीं, यह नियमों और हस्ताक्षर करने वाले व्यक्ति का मामला है।

**retrieval गलत पैराग्राफ़ सामने ला सकता है।** index में पुराना मार्गदर्शन, या ऐसा पैराग्राफ़ जो करीब तो है पर पूरी तरह प्रासंगिक नहीं, पूरे आत्मविश्वास से लौटाया जाएगा। index को ताज़ा रखिए और हमेशा स्रोत पढ़िए।

## निचोड़

excise return वह एक रिपोर्ट है जिसकी हर संख्या व्यवसाय के बाहर का कोई व्यक्ति जाँचता है। इसलिए हाथ से आँकड़े कॉपी करना बंद करने की यह सबसे अच्छी जगह है। return के नियम data contract के रूप में लिखिए, उन्हें हर रात टेस्ट कीजिए, और महीने का अंत खोजबीन की बजाय एक समीक्षा बन जाता है। GenAI वहाँ इस्तेमाल कीजिए जहाँ गड़बड़ टेक्स्ट में है, नोट्स छाँटने और स्पष्टीकरण लिखने में, और आँकड़े व हस्ताक्षर लोगों और परखे हुए कोड के पास रखिए।

सीरीज़ में आगे, और आखिरी: [वाइनरी AI कहाँ टूटता है]({{ '/hi/2026/where-winery-ai-breaks-ten-vintages-ten-rows/' | relative_url }}), और दस विंटेज सिर्फ़ दस पंक्तियाँ क्यों हैं। पूरी सूची [Cellar Ledger सीरीज़ पेज]({{ '/series/cellar-ledger/' | relative_url }}) पर है।

## अक्सर पूछे जाने वाले सवाल

**वाइनरी के संदर्भ में data contract क्या है?**
यह एक लिखित और लागू किया गया समझौता है कि किसी dataset में क्या होना ज़रूरी है। excise के लिए movement ledger पर contract कह सकता है कि हर removal की एक tax class, एक गंतव्य प्रकार और एक मापा गया अल्कोहल हो, और हर महीने का opening balance पिछले महीने के closing के बराबर हो। पाइपलाइन इन नियमों को टेस्ट करती है और खराब रिकॉर्ड को return तक पहुँचने से पहले रोक देती है।

**क्या एक LLM वाइन excise return भर सकता है?**
उसे संख्याएँ नहीं भरनी चाहिए। आँकड़े ledger पर चलने वाली परखी हुई क्वेरी से आते हैं। LLM return के आसपास काम का है: free-text removal नोट्स को श्रेणियों में बाँटना, किसी असामान्य नुकसान के स्पष्टीकरण का ड्राफ़्ट बनाना, और किसी व्यक्ति के पढ़ने के लिए संबंधित मार्गदर्शन पैराग्राफ़ ढूँढना। हर return की समीक्षा और हस्ताक्षर एक नामित व्यक्ति करता है।

**वाइन की tax classes मिलान में समस्या क्यों पैदा करती हैं?**
क्योंकि एक लॉट इमारत छोड़े बिना अपनी class बदल सकता है। उदाहरण के लिए US में still wine पर अल्कोहल के हिसाब से बैंड में टैक्स लगता है, और 16 प्रतिशत पर एक रेखा है। blending, fortification या सुधारा गया लैब नतीजा किसी लॉट को उस रेखा के पार ले जा सकता है, और अगर बदलाव event के रूप में दर्ज न हो, तो प्रति-class बैलेंस का जोड़ मिलना बंद हो जाता है।
