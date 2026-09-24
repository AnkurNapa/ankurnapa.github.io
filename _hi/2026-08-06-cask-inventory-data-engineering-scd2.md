---
layout: post
lang: hi
title: "डेटा इंजीनियरिंग के रूप में cask इन्वेंटरी: SCD2 positions, regauge events और निकाली गई संख्या के रूप में angel's share"
image: /assets/og/cask-inventory-data-engineering-scd2.png
description: "The Still and the Model का भाग 4। एक cask बारह साल या उससे ज़्यादा warehouse में रहता है, जगह बदलता है, उसका सैंपल लिया जाता है, regauge होता है, और हर साल spirit खोता है। उसकी विशेषताओं को slowly changing dimensions के रूप में, उसके जीवन को events के रूप में, और angel's share को एक गणना के रूप में मॉडल कीजिए, ताकि किसी भी तारीख पर किसी भी cask के बारे में हर सवाल का एक ही जवाब हो।"
date: 2026-08-06 09:00:00 -0700
updated: 2026-08-06
permalink: /hi/2026/cask-inventory-data-engineering-scd2/
tags: [distilling-maturation, still-and-model, data-engineering, data-modeling, generative-ai]
faq:
  - q: "SCD2 टेबल क्या है और casks के लिए इसे क्यों इस्तेमाल करें?"
    a: "type 2 slowly changing dimension किसी रिकॉर्ड को ओवरराइट करने की बजाय उसका हर संस्करण उन तारीखों के साथ रखता है जब वह मान्य था। casks के लिए इसका मतलब है कि किसी cask की हर warehouse position, मालिक और स्थिति अपनी तारीखों के साथ टेबल में बनी रहती है। आप पूछ सकते हैं कि मार्च 2019 में cask कहाँ था और जवाब पा सकते हैं, जो microclimate विश्लेषण, ऑडिट और ग्राहकों के सवालों के लिए मायने रखता है।"
  - q: "cask इन्वेंटरी में angel's share की गणना कैसे होनी चाहिए?"
    a: "एक निकाली गई संख्या के रूप में, कभी स्टोर की गई संख्या के रूप में नहीं। भरते समय के absolute alcohol के लीटर लीजिए, नवीनतम regauge पर अल्कोहल और दर्ज सैंपल या निकासी घटाइए, और जो बचा वह नुकसान है। फ़ील्ड के रूप में स्टोर किया गया angel's share बासी हो जाता है और सैंपलिंग को छिपा लेता है। events से निकाला गया, यह हमेशा ताज़ा और समझाने योग्य रहता है।"
  - q: "क्या एक GenAI असिस्टेंट पक रहे स्टॉक के बारे में सवालों के जवाब दे सकता है?"
    a: "हाँ, अगर वह कच्ची टेबल की बजाय नियंत्रित क्वेरी के ज़रिए जवाब दे। उसे event और SCD2 टेबल पर टिके cask_history, position_on और alcohol_balance जैसे टूल दीजिए, और वह ऐसे सवालों के जवाब दे सकता है कि किसी खास fill के कौन से casks ने सामान्य से ज़्यादा खोया, जिसमें हर आँकड़ा क्वेरी से आता है।"
---

**संक्षिप्त उत्तर: व्हिस्की का एक cask बारह साल या उससे ज़्यादा warehouse में रह सकता है, और उस दौरान वह जगह बदलता है, उसका सैंपल लिया जाता है, उसे regauge किया जाता है और वह चुपचाप हवा को spirit खोता रहता है। अगर इन्वेंटरी सिर्फ़ cask की मौजूदा जगह और मौजूदा वॉल्यूम रखती है, तो उस इतिहास का ज़्यादातर हिस्सा चला गया। धीरे-धीरे बदलने वाली विशेषताओं (जगह, मालिक, स्थिति) को type 2 slowly changing dimension के रूप में मॉडल कीजिए, cask के साथ जो भी होता है उसे event के रूप में दर्ज कीजिए, और angel's share को स्टोर करने की बजाय events से निकालिए। तब "यह cask 2019 में कहाँ था?" और "इसने असल में कितना खोया?" दोनों का एक-एक जवाब होता है, और एक GenAI असिस्टेंट बिना अंदाज़ा लगाए उनका जवाब दे सकता है।**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एक cask की बारह साल की उदाहरण timeline। 2014 में warehouse 1 में 63.5 प्रतिशत पर 250 लीटर से भरा गया, 158.75 लीटर absolute alcohol। 2016 में warehouse 3 में ले जाया गया। 2019 में सैंपल लिया गया। 2020 में regauge हुआ। 2022 में फिर जगह बदली। 2026 में 205 लीटर और 60.8 प्रतिशत पर regauge, 124.64 लीटर absolute alcohol। angel's share लगभग 34 लीटर absolute alcohol निकलता है, मोटे तौर पर 2 प्रतिशत प्रति वर्ष।">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एक CASK, बारह साल के EVENTS (उदाहरण)</text>
<g font-family="sans-serif">
<line x1="70" y1="150" x2="930" y2="150" stroke="#4db6a2" stroke-width="3"/>
<circle cx="70" cy="150" r="9" fill="#06483f"/>
<text x="70" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2014 fill</text>
<text x="70" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">250 L, 63.5% पर</text>
<text x="70" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">158.75 LAA</text>
<circle cx="213" cy="150" r="7" fill="#4db6a2"/>
<text x="213" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2016 move</text>
<text x="213" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W1 से W3</text>
<circle cx="427" cy="150" r="7" fill="#4db6a2"/>
<text x="427" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2019 सैंपल</text>
<text x="427" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">दर्ज निकासी</text>
<circle cx="498" cy="150" r="7" fill="#4db6a2"/>
<text x="518" y="100" text-anchor="middle" font-size="11.5" fill="#06483f">2020 regauge</text>
<circle cx="643" cy="150" r="7" fill="#4db6a2"/>
<text x="643" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2022 move</text>
<text x="643" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W3 से W5</text>
<circle cx="930" cy="150" r="9" fill="#06483f"/>
<text x="915" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2026 regauge</text>
<text x="915" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">205 L, 60.8% पर</text>
<text x="915" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">124.64 LAA</text>
<rect x="250" y="222" width="500" height="44" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="500" y="249" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081">निकाला गया नुकसान लगभग 34 LAA, मोटे तौर पर 2% प्रति वर्ष</text>
<rect x="40" y="282" width="920" height="36" rx="10" fill="#06483f"/>
<text x="500" y="305" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">ANGEL'S SHARE EVENTS पर एक क्वेरी है, कोई फ़ील्ड नहीं जिसे कोई अपडेट करे</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरण cask। absolute alcohol के लीटर (LAA) बल्क लीटर गुणा strength हैं। पूरे balance में, किसी भी चीज़ को angel's share कहने से पहले 2019 जैसे सैंपल घटाए जाते हैं।</figcaption>
</figure>

किसी warehouse मैनेजर से पूछिए कि cask 14-0387 कहाँ है, और वह सेकंडों में बता देगा। पूछिए कि 2019 की गर्मियों में वह कहाँ था, जब उस fill के casks के एक समूह में एक अनपेक्षित note आ गया था, और जवाब में आमतौर पर एक कागज़ी बही, एक रिटायर हो चुका सहकर्मी और ढेर सारी सद्भावना शामिल होती है।

इस सीरीज़ की [पिछली पोस्ट]({{ '/hi/2026/llm-copilot-still-operator/' | relative_url }}) still house के फ़र्श पर थीं। यह पोस्ट warehouse में जाती है, जहाँ समय का पैमाना घंटों की बजाय साल है, और जहाँ डेटा मॉडल तय करता है कि इतिहास बचेगा या नहीं।

## दो तरह के बदलाव

एक cask दो अलग तरह से बदलता है, और उन्हें दो अलग ढाँचे चाहिए।

**कभी-कभार बदलने वाली विशेषताएँ:** warehouse, bay और tier; मालिक (ग्राहकों के लिए रखे casks के लिए); स्थिति (पक रहा, निर्धारित, disgorged); re-rack के बाद cask का प्रकार। ये cask के बारे में ऐसे तथ्य हैं जो एक अवधि तक सही रहते हैं, फिर बदलते हैं।

**उसके साथ होने वाली चीज़ें:** भरना, जगह बदलना, सैंपल, regauge, top up, नए cask में re-rack, disgorge। ये तारीख, मात्रा और व्यक्ति वाले events हैं।

ज़्यादातर cask सिस्टम पहली तरह को मौजूदा मानों के रूप में रखते हैं और दूसरी को, बहुत हुआ तो, एक comments फ़ील्ड में। दोनों इतिहास खो देते हैं।

## SCD2: हर संस्करण, अपनी तारीखों के साथ

type 2 slowly changing dimension किसी विशेषता को ओवरराइट करने की बजाय उसका हर संस्करण रखता है। हर पंक्ति में वह तारीख होती है जब वह सच हुई और जब वह सच नहीं रही:

```sql
-- cask_position_scd2: one row per period the cask sat in one place
-- cask_id | warehouse | bay | tier | valid_from | valid_to   | is_current
-- 14-0387 | W1        | A   | 2    | 2014-05-12 | 2016-09-03 | false
-- 14-0387 | W3        | C   | 1    | 2016-09-03 | 2022-04-18 | false
-- 14-0387 | W5        | B   | 3    | 2022-04-18 | 9999-12-31 | true

SELECT warehouse, bay, tier
FROM   cask_position_scd2
WHERE  cask_id = '14-0387'
  AND  DATE '2019-07-01' >= valid_from
  AND  DATE '2019-07-01' <  valid_to;
```

वह एक क्वेरी 2019 वाले सवाल का जवाब देती है। यह microclimate विश्लेषण भी संभव बनाती है: समय के साथ positions को warehouse के तापमान और नमी के लॉग से जोड़िए, और हर cask को अपना जिया हुआ जलवायु इतिहास मिल जाता है, जो [rackhouse microclimate पोस्ट]({{ '/hi/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) को इनपुट के रूप में चाहिए। SCD2 के बिना हर cask ऐसा दिखता है जैसे उसने बारह साल वहीं बिताए जहाँ वह आज संयोग से है।

इसे बनाए रखने की पाइपलाइन मानक है: हर बार जब कोई move दर्ज हो, मौजूदा पंक्ति बंद कीजिए और नई खोलिए। dbt snapshots, Delta `MERGE` और Fabric pipelines, सब कुछ पंक्तियों के configuration से यह कर देते हैं।

## Events: cask का अपना ledger

cask की सामग्री बदलने वाली हर चीज़ एक event है, उसी तरह दर्ज जैसे [वाइन cellar ledger]({{ '/hi/2026/event-sourced-cellar-records-winery/' | relative_url }}) movements दर्ज करता है:

- **fill**: बल्क लीटर, strength, LAA, spirit बैच, cask का प्रकार
- **sample**: निकाला गया वॉल्यूम, उद्देश्य
- **regauge**: बल्क लीटर, strength, LAA, तरीका (dip या वज़न)
- **re-rack**: किस cask से, किस cask में, वॉल्यूम
- **disgorge**: vatting के लिए बाहर गया वॉल्यूम और strength

regauges पर एक टिप्पणी बनती है। casks को अक्सर dip की बजाय वज़न से gauge किया जाता है: कुल वज़न घटा cask का tare, मापी गई strength पर घनत्व से भाग, बल्क लीटर देता है। यह गणना 20 डिग्री C पर एथेनॉल और पानी की density टेबल पर, और भरते समय दर्ज tare वज़न पर निर्भर करती है। अगर इनमें से कोई गायब या गलत है, तो उस cask का हर regauge एक ही दिशा में गलत होता है। event पर सिर्फ़ नतीजे वाला वॉल्यूम नहीं, बल्कि कुल वज़न, tare और strength रखिए, ताकि गणना जाँची और दोबारा की जा सके।

## निकाली गई संख्या के रूप में angel's share

events होने के बाद angel's share कोई फ़ील्ड नहीं रहता जिसे कोई अपडेट करे, बल्कि एक गणना बन जाता है:

> नुकसान = भरते समय LAA - नवीनतम regauge पर LAA - सैंपल और निकासी में गया LAA

ऊपर के उदाहरण cask के लिए: 63.5% पर 250 लीटर से भरा गया, यानी 158.75 LAA। बारह साल बाद यह 205 लीटर और 60.8% पर regauge होता है, यानी 124.64 LAA। सरलता के लिए 2019 के छोटे सैंपल को छोड़ दें, तो नुकसान लगभग 34 LAA है, यानी बारह साल में 21.5%, चक्रवृद्धि से मोटे तौर पर 2% प्रति वर्ष। यह ठंडे, नम warehouse में Scotch के लिए अक्सर बताए जाने वाले दायरे में है। गरम जलवायु कहीं ज़्यादा खोती है, और जहाँ पानी अल्कोहल से तेज़ी से उड़ता है वहाँ strength गिरने की बजाय बढ़ भी सकती है।

दो चीज़ें निकाले गए संस्करण को स्टोर किए गए से बेहतर बनाती हैं। यह हमेशा ताज़ा है: नया regauge इसे किसी के याद रखे बिना अपडेट कर देता है। और यह सैंपल के बारे में ईमानदार है: जो cask इसलिए प्यासा दिखता है कि blending टीम उससे बार-बार निकालती रही, वह अपने सैंपल को सैंपल के रूप में दिखाता है, वाष्पीकरण के रूप में नहीं। [angel's share पूर्वानुमान पोस्ट]({{ '/hi/2024/forecasting-whiskey-angels-share/' | relative_url }}) नुकसान को मॉडल करना बताती है। यह वह डेटा है जिससे उसे मॉडल किया जाना चाहिए।

## ऊपर एक GenAI असिस्टेंट रखना

SCD2 positions और cask event ledger के साथ, लोग जो सवाल सच में पूछते हैं वे क्वेरी बन जाते हैं, और क्वेरी GenAI असिस्टेंट के टूल बन सकती हैं:

- `cask_history(cask_id)`: क्रम में हर event और position
- `position_on(cask_id, date)`: ऊपर वाला SCD2 lookup
- `alcohol_balance(fill_batch)`: fill LAA, मौजूदा LAA, सैंपल, प्रति cask निकाला गया नुकसान

"मई 2014 के fill के कौन से casks ने अपने पड़ोसियों से ज़्यादा खोया?" पूछे जाने पर असिस्टेंट `alcohol_balance` बुलाता है, हर cask की तुलना उसके fill और warehouse के median से करता है, और outliers को समय के साथ उनकी positions समेत सूचीबद्ध करता है। हर संख्या क्वेरी से आती है। मॉडल का काम है सवाल समझना, सही टूल बुलाना और जवाब सादे शब्दों में समझाना। वाइन सीरीज़ की [semantic layer पोस्ट]({{ '/hi/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) बताती है कि उसे कच्ची टेबल क्यों नहीं देखनी चाहिए।

## यह कहाँ टूटता है

**बारह साल का इतिहास शायद ही कभी साफ़ शुरू होता है।** ज़्यादातर cask इन्वेंटरी का पहला दशक कागज़, पुराने सिस्टम और स्प्रेडशीट का मिश्रण है। जो हो सके उसे स्पष्ट स्रोत वाले events के रूप में माइग्रेट कीजिए, हर cask की opening position से SCD2 शुरू कीजिए, और माइग्रेट किए गए इतिहास को नए जितना अच्छा होने का दिखावा करने की बजाय कम भरोसे वाला चिह्नित कीजिए।

**regauges कम होते हैं और उनमें शोर होता है।** बारह साल में दो बार regauge हुआ cask अपने नुकसान के दो डेटा बिंदु देता है। casks के बीच कुछ प्रतिशत का अंतर maturation नहीं, माप हो सकता है।

**tare वज़न गायब हो जाते हैं।** बिना दर्ज tare वाले cask को वज़न से किसी भी सटीकता के साथ regauge नहीं किया जा सकता। गायब tare को डेटा quality दोष मानिए और उसे दसवें साल नहीं, पहले दिन फ़्लैग कीजिए।

**duty रिकॉर्ड अलग हैं।** bonded warehouse रिकॉर्ड excise प्राधिकरण को जवाबदेह हैं और उनके अपने नियम हैं। एनालिटिक इन्वेंटरी को उनसे मिलान करना चाहिए, उनकी जगह नहीं लेनी चाहिए।

## निचोड़

cask बारह साल का रिकॉर्ड है, और ज़्यादातर इन्वेंटरी उसका सिर्फ़ आखिरी पन्ना रखती हैं। हर position उसकी तारीखों के साथ रखिए, हर event उसकी मात्राओं के साथ दर्ज कीजिए, और angel's share को स्टोर करने की बजाय निकालिए। तब जलवायु, नुकसान, सैंपलिंग और ऑडिट के बारे में जो सवाल मायने रखते हैं, उनका एक-एक जवाब होता है, और GenAI असिस्टेंट गढ़ने की बजाय नियंत्रित टूल्स के ज़रिए उसे ढूँढ सकता है। spirit धैर्यवान है। डेटा मॉडल को भी होना चाहिए।

सीरीज़ में आगे: [ऐसा GenAI blending असिस्टेंट जिसका गणित कोड में होता है]({{ '/hi/2026/genai-whisky-blending-assistant-lp/' | relative_url }})। कौन से casks इस्तेमाल करें, यह चुनने के लिए देखें [cask चयन और पक रहे स्टॉक की इन्वेंटरी के लिए AI]({{ '/hi/2024/ai-cask-selection-inventory/' | relative_url }})। पूरी सूची [The Still and the Model सीरीज़ पेज]({{ '/series/still-and-model/' | relative_url }}) पर है।

## अक्सर पूछे जाने वाले सवाल

**SCD2 टेबल क्या है और casks के लिए इसे क्यों इस्तेमाल करें?**
type 2 slowly changing dimension किसी रिकॉर्ड को ओवरराइट करने की बजाय उसका हर संस्करण उन तारीखों के साथ रखता है जब वह मान्य था। casks के लिए इसका मतलब है कि किसी cask की हर warehouse position, मालिक और स्थिति अपनी तारीखों के साथ टेबल में बनी रहती है। आप पूछ सकते हैं कि मार्च 2019 में cask कहाँ था और जवाब पा सकते हैं, जो microclimate विश्लेषण, ऑडिट और ग्राहकों के सवालों के लिए मायने रखता है।

**cask इन्वेंटरी में angel's share की गणना कैसे होनी चाहिए?**
एक निकाली गई संख्या के रूप में, कभी स्टोर की गई संख्या के रूप में नहीं। भरते समय के absolute alcohol के लीटर लीजिए, नवीनतम regauge पर अल्कोहल और दर्ज सैंपल या निकासी घटाइए, और जो बचा वह नुकसान है। फ़ील्ड के रूप में स्टोर किया गया angel's share बासी हो जाता है और सैंपलिंग को छिपा लेता है। events से निकाला गया, यह हमेशा ताज़ा और समझाने योग्य रहता है।

**क्या एक GenAI असिस्टेंट पक रहे स्टॉक के बारे में सवालों के जवाब दे सकता है?**
हाँ, अगर वह कच्ची टेबल की बजाय नियंत्रित क्वेरी के ज़रिए जवाब दे। उसे event और SCD2 टेबल पर टिके cask_history, position_on और alcohol_balance जैसे टूल दीजिए, और वह ऐसे सवालों के जवाब दे सकता है कि किसी खास fill के कौन से casks ने सामान्य से ज़्यादा खोया, जिसमें हर आँकड़ा क्वेरी से आता है।
