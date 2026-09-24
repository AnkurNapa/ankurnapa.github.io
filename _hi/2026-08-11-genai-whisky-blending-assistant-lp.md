---
layout: post
lang: hi
title: "ऐसा GenAI blending असिस्टेंट जिसका गणित कोड में होता है: vatting के लिए LP, पानी के लिए density टेबल"
image: /assets/og/genai-whisky-blending-assistant-lp.png
description: "The Still and the Model का भाग 5। language model किसी blender को vatting समझा सकता है, पर उसे कभी जोड़-घटाव नहीं करना चाहिए। cask चयन एक linear programme है, bottling strength तक reduction के लिए एथेनॉल-पानी के सिकुड़न का गणित चाहिए, और age statement एक नियम है, औसत नहीं। LLM टूल बुलाता है और जवाब समझाता है।"
date: 2026-08-11 09:00:00 -0700
updated: 2026-08-11
permalink: /hi/2026/genai-whisky-blending-assistant-lp/
tags: [distilling-maturation, still-and-model, generative-ai, optimisation, blending]
faq:
  - q: "व्हिस्की में कितना पानी मिलाना है, यह निकालने के लिए सिर्फ़ वॉल्यूम घटाना क्यों काफ़ी नहीं?"
    a: "क्योंकि एथेनॉल और पानी मिलने पर सिकुड़ते हैं। 63.5% पर 1,000 लीटर को 40% तक लाने के लिए लगभग 605 लीटर पानी चाहिए, वे 587.5 लीटर नहीं जो सीधा वॉल्यूम गणित बताता है, और सिर्फ़ 587.5 लीटर मिलाने से spirit लगभग 40.4% पर रह जाती है। सही तरीका 20 डिग्री C पर density टेबल का इस्तेमाल करके द्रव्यमान में काम करता है, फिर माप से पुष्टि करता है।"
  - q: "क्या एक LLM व्हिस्की blend के लिए casks चुन सकता है?"
    a: "उसे सीधे नहीं चुनना चाहिए। cask चयन एक optimisation समस्या है जिसमें पक्की शर्तें होती हैं, जैसे वॉल्यूम, sensory लक्ष्य और सबसे युवा व्हिस्की की उम्र, और एक linear programming solver इसे ठीक-ठीक हल करता है। LLM का काम है blender के अनुरोध को solver के इनपुट में बदलना, solver बुलाना और नतीजा समझाना।"
  - q: "व्हिस्की blend में age statement कैसे काम करता है?"
    a: "Scotch whisky में और EU नियमों के तहत, लेबल पर उम्र बोतल में मौजूद सबसे युवा व्हिस्की की उम्र है। यह औसत नहीं है। blending टूल को दावे से कम उम्र के हर cask को बाहर रखना होगा, चाहे उसकी कीमत या flavour कितना भी आकर्षक हो, और optimiser को इसे पक्के नियम के रूप में लागू करना चाहिए।"
---

**संक्षिप्त उत्तर: GenAI blender के लिए अच्छा इंटरफ़ेस और खराब कैलकुलेटर है। cask चयन एक linear programme है: इस्तेमाल हुए स्टॉक के सबसे कम मूल्य पर वॉल्यूम और sensory लक्ष्य पूरे करना, जिसमें age statement एक पक्का नियम है क्योंकि लेबल सबसे युवा व्हिस्की बताता है, औसत नहीं। bottling strength तक reduction के लिए एथेनॉल-पानी के सिकुड़न का गणित चाहिए: 63.5% पर 1,000 लीटर को 40% तक लाने के लिए लगभग 605 लीटर पानी चाहिए, 587.5 नहीं। दोनों गणनाएँ परखे हुए कोड में रखिए, उन्हें टूल के रूप में खोलिए, और language model को वह करने दीजिए जिसमें वह अच्छा है: अनुरोध समझना, टूल बुलाना और जवाब सादे शब्दों में समझाना।**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="blending असिस्टेंट का आर्किटेक्चर। एक blender 300 लीटर absolute alcohol की 12 साल पुरानी vatting माँगता है जिसका sherry character score कम से कम 6 हो। LLM दो टूल बुलाता है। cask चयन solver cask A से 94, cask B से 130 और cask C से 76 लीटर absolute alcohol लौटाता है, और cask D को बाहर रखता है क्योंकि वह 10 साल पुराना है। reduction टूल बताता है कि 63.5 प्रतिशत पर 1,000 लीटर को 40 प्रतिशत तक लाने के लिए 604.9 लीटर पानी चाहिए, और सीधे-सादे 587.5 लीटर उसे 40.4 प्रतिशत पर छोड़ेंगे। फिर LLM नतीजा समझाता है।">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">LLM पूछता है, टूल गणना करते हैं (उदाहरण)</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="250" height="100" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="155" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">blender पूछता है</text>
<text x="155" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">12 साल पुरानी vatting,</text>
<text x="155" y="125" text-anchor="middle" font-size="10.5" fill="#4a6b64">300 LAA, sherry score &#8805; 6,</text>
<text x="155" y="142" text-anchor="middle" font-size="10.5" fill="#4a6b64">इस्तेमाल स्टॉक का सबसे कम मूल्य</text>
<line x1="280" y1="110" x2="340" y2="110" stroke="#4db6a2" stroke-width="2"/>
<rect x="340" y="75" width="160" height="70" rx="12" fill="#06483f"/>
<text x="420" y="106" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="126" text-anchor="middle" font-size="10.5" fill="#cfe6df">टूल बुलाता है, समझाता है</text>
<line x1="500" y1="100" x2="560" y2="80" stroke="#4db6a2" stroke-width="2"/>
<line x1="500" y1="125" x2="560" y2="200" stroke="#4db6a2" stroke-width="2"/>
<rect x="560" y="50" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="74" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">select_casks() &#183; linear programme</text>
<text x="765" y="96" text-anchor="middle" font-size="11" fill="#06483f">A 94 LAA &#183; B 130 LAA &#183; C 76 LAA</text>
<text x="765" y="116" text-anchor="middle" font-size="11" fill="#06483f">sherry score 6.0, मूल्य 415</text>
<text x="765" y="136" text-anchor="middle" font-size="11" fill="#ff4081">D बाहर: 10 साल पुराना</text>
<rect x="560" y="165" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="189" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">reduction_water() &#183; density टेबल</text>
<text x="765" y="211" text-anchor="middle" font-size="11" fill="#06483f">1,000 L, 63.5% से 40%: 604.9 L पानी</text>
<text x="765" y="231" text-anchor="middle" font-size="11" fill="#06483f">अंतिम 1,587.5 L, 635 LAA</text>
<text x="765" y="251" text-anchor="middle" font-size="11" fill="#ff4081">सीधे-सादे 587.5 L से 40.4% रह जाता है</text>
<rect x="30" y="286" width="940" height="40" rx="10" fill="#06483f"/>
<text x="500" y="311" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">हर संख्या टूल से आती है &#183; मॉडल कभी जोड़-घटाव नहीं करता</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरण के स्टॉक और मूल्य। दोनों टूल साधारण, परखा हुआ कोड हैं। language model इंटरफ़ेस है।</figcaption>
</figure>

एक blender GenAI असिस्टेंट से पूछता है कि 63.5% पर 1,000 लीटर cask-strength spirit को 40% तक लाने के लिए कितना पानी मिलाना है। असिस्टेंट तुरंत जवाब देता है: 587.5 लीटर। वह अपना हिसाब दिखाता है, और हिसाब साफ़-सुथरा है। पर वह गलत भी है, और गलती rounding की नहीं है। यह रसायन है जिसके बारे में किसी ने मॉडल को बताया नहीं।

यह पोस्ट ऐसा blending असिस्टेंट बनाने के बारे में है जो यह गलती कर ही न सके, क्योंकि वह कभी गणित करता ही नहीं। पिछली पोस्ट की [cask इन्वेंटरी]({{ '/hi/2026/cask-inventory-data-engineering-scd2/' | relative_url }}) स्टॉक देती है। गणित टूल्स में रहता है। मॉडल बात करता है।

## पानी की समस्या: वॉल्यूम क्यों नहीं जुड़ते

63.5% ABV पर 1,000 लीटर लीजिए। इसमें 635 लीटर absolute alcohol है। 40% पर वे 635 लीटर अल्कोहल 635 / 0.40 = 1,587.5 लीटर spirit बनाते हैं। तो सीधा जवाब है 587.5 लीटर पानी मिलाना।

दिक्कत यह है कि एथेनॉल और पानी मिलने पर सिकुड़ते हैं। अणु किसी भी तरल के अकेले होने से ज़्यादा कसकर जुड़ते हैं, इसलिए 1,000 लीटर spirit जोड़ 587.5 लीटर पानी 1,587.5 लीटर से कम देता है। strength लक्ष्य से ऊपर रह जाती है, इस मामले में लगभग 40.4%।

सही तरीका द्रव्यमान में काम करता है, जो संरक्षित रहता है, और 20 डिग्री C पर एथेनॉल-पानी मिश्रण के घनत्व का इस्तेमाल करता है:

```python
def reduction_water(vol_l, abv_in, abv_out, rho20):
    # rho20(abv) -> density in kg/L at 20 C, from the official alcoholometric tables
    laa = vol_l * abv_in / 100
    vol_out = laa / (abv_out / 100)
    mass_in = vol_l * rho20(abv_in)
    mass_out = vol_out * rho20(abv_out)
    return (mass_out - mass_in) / rho20(0)   # litres of water at 20 C
```

63.5% पर लगभग 0.901 kg/L और 40% पर 0.948 kg/L घनत्व के साथ, जवाब लगभग 605 लीटर पानी है, 587.5 नहीं। गायब 17 लीटर सिकुड़न है।

क्या 0.4% से फ़र्क पड़ता है? EU नियमों के तहत spirit strength के लिए लेबल की छूट 0.3% vol है, और duty अल्कोहल पर लगती है। ज़्यादा strength मतलब spirit मुफ़्त में दे देना। दूसरी ओर चूकना और बुरा है: UK और EU में 40% से नीचे की व्हिस्की व्हिस्की के रूप में बेची ही नहीं जा सकती। इसीलिए असली reductions चरणों में, demineralised पानी से किए जाते हैं, और किसी भी गणना पर, चाहे कितनी भी अच्छी हो, भरोसा करने की बजाय density meter से strength मापकर पूरे किए जाते हैं।

## cask चयन एक linear programme है

vatting के लिए casks चुनना सादे कपड़ों में एक optimisation समस्या है। एक सरल संस्करण:

- **फ़ैसला:** हर योग्य cask से absolute alcohol के कितने लीटर निकालने हैं।
- **उद्देश्य:** स्टॉक का सबसे कम कुल मूल्य इस्तेमाल करना, ताकि सबसे कीमती पुराने casks वहाँ के लिए बचें जहाँ वे मायने रखते हैं।
- **शर्तें:** कुल अल्कोहल लक्ष्य; हर cask में उपलब्ध अल्कोहल; भारित औसत के रूप में sensory लक्ष्य (उदाहरण के लिए, पूरी vatting में कम से कम 6 का sherry character score); और उम्र का नियम।

एक linear programming solver (SciPy, OR-Tools, या आपके planning टूल वाला) इसे मिलीसेकंडों में ठीक-ठीक हल करता है। उदाहरण में, 12 साल पुराने cask A (मूल्य 1.0 प्रति LAA, sherry 3), 14 साल पुराने B (1.3, sherry 7) और 18 साल पुराने C (2.0, sherry 8) के साथ, 6 के sherry score वाली 300 LAA की सबसे सस्ती vatting A से 94 LAA, B से पूरे 130 और C से 76 लेती है, और स्टॉक मूल्य 415 आता है।

## age statement एक नियम है, औसत नहीं

अब cask D जोड़िए: 10 साल पुराना, बढ़िया sherry character (score 9), 0.8 प्रति LAA पर सस्ता। solver को इसे इस्तेमाल करने दीजिए और लागत 302.5 पर गिर जाती है, एक चौथाई कम। वह D को पूरा लेता है और पुराने स्टॉक से बहुत कम।

और 12 साल वाले लेबल के लिए यह गैरकानूनी भी है। Scotch Whisky Regulations और EU नियमों के तहत age statement बोतल में सबसे युवा व्हिस्की की उम्र है। यह उम्रों का औसत नहीं है, चाहे कैसे भी भारित किया जाए। जो टूल औसत उम्र निकालकर उसे 12 के सामने जाँचता है, वह इस vatting को खुशी-खुशी मंज़ूर कर देगा।

यह ठीक उस तरह का डोमेन नियम है जिसे language model बातचीत में गलत कर देता है, और solver सिर्फ़ तभी सही करता है जब कोई उसे encode करे। इसलिए उम्र का नियम गणित में कोई शर्त नहीं है। यह एक filter है कि कौन से casks समस्या में आ भी सकते हैं, जो solver के चलने से पहले कोड में लगाया जाता है।

## LLM कहाँ बैठता है

गणनाएँ टूल्स में होने से language model के पास एक उपयोगी और सुरक्षित काम है:

1. **अनुरोध को इनपुट में बदलना।** "पिछले साल के 12 जैसा कुछ, थोड़ा ज़्यादा sherry, 300 LAA, 25 साल वालों को मत छूना" एक लक्ष्य, शर्तों और बाहर रखने की सूची बन जाता है। कुछ भी चलाने से पहले असिस्टेंट पुष्टि के लिए इनपुट वापस दिखाता है।
2. **टूल बुलाना।** vatting के लिए `select_casks`, reduction के लिए `reduction_water`, और blender किसी खास cask के बारे में जो भी पूछे उसके लिए इन्वेंटरी से `cask_history`।
3. **नतीजा समझाना।** cask B पूरा क्यों इस्तेमाल हुआ (sherry score बढ़ाने का यह सबसे सस्ता तरीका है), D बाहर क्यों रहा (उम्र), और अगर sherry लक्ष्य 5 पर आ जाए तो क्या बदलेगा।
4. **खुद कभी कोई संख्या न बनाना।** समझाने में हर आँकड़ा किसी टूल के आउटपुट से आता है। अगर blender कोई मात्रात्मक सवाल पूछे जिसका जवाब टूल नहीं दे सकते, तो असिस्टेंट यही कहता है।

फ़ैसला blender करता है, और आखिरी परीक्षा नाक की है। [blending consistency पोस्ट]({{ '/hi/2024/ai-whiskey-blending-consistency/' | relative_url }}) sensory और रासायनिक डेटा से house style मिलाने के बारे में है। यह पोस्ट यह पक्का करने के बारे में है कि उसके आसपास का गणित कभी कमज़ोर कड़ी न बने।

## यह कहाँ टूटता है

**sensory scores रैखिक नहीं हैं।** solver vatting के sherry score को उसके casks का भारित औसत मानता है। flavour हमेशा इतनी शालीनता से नहीं मिलता: एक दबंग cask अपने हिस्से से कहीं ज़्यादा हावी हो सकता है। optimum को सैंपल vatting की शुरुआती रेसिपी मानिए, अंतिम blend नहीं।

**density टेबल आधिकारिक ही होनी चाहिए।** ऊपर का खाका उतना ही अच्छा है जितना `rho20`। duty और लेबलिंग के लिए आधिकारिक alcoholometric टेबल (OIML R22 या आपके प्राधिकरण का समकक्ष) और calibrated उपकरण इस्तेमाल कीजिए, किसी का टाइप किया हुआ अनुमान नहीं।

**अलग strengths को blend करने पर भी थोड़ा सिकुड़न होता है।** अलग strengths वाली दो spirits मिलाने पर भी थोड़ा सिकुड़न होता है, इसलिए vatting का वॉल्यूम casks का ठीक-ठीक जोड़ नहीं होता। मिलती-जुलती strength वाले casks के लिए असर छोटा है, पर अल्कोहल में काम कीजिए और नतीजा मापिए।

**स्टॉक मूल्य एक नीतिगत फ़ैसला है।** स्टॉक मूल्य कम से कम करना इस नज़रिए को encode करता है कि कौन से casks सबसे ज़्यादा मायने रखते हैं। यह नज़रिया पक रही इन्वेंटरी के मालिकों से लीजिए, और उन्हें इसे बदलने दीजिए।

## निचोड़

language model blending के सवाल का जवाब धाराप्रवाह, आत्मविश्वास भरे वाक्यों में देगा, उनमें भी जो रसायन या कानून तोड़ते हैं। उसे जोड़-घटाव से दूर रखिए। cask चयन solver में रखिए, age statement को पक्के filter के रूप में। reduction को ऐसे कोड में रखिए जो density टेबल इस्तेमाल करे और द्रव्यमान संरक्षित रखे। फिर मॉडल को वह हिस्सा करने दीजिए जिसमें वह सचमुच अच्छा है: blender का मतलब समझना, सही टूल बुलाना और जवाब समझाना। मॉडल संख्याएँ देखता है। blender vatting चखता है।

सीरीज़ में आगे, और आखिरी: [डिस्टिलरी AI कहाँ टूटता है]({{ '/hi/2026/where-distillery-ai-breaks/' | relative_url }})। डैशबोर्ड में blending के sensory पक्ष के लिए देखें [व्हिस्की blending और sensory डैशबोर्ड]({{ '/hi/2023/tableau-whisky-blending-sensory-dashboard/' | relative_url }})। पूरी सूची [The Still and the Model सीरीज़ पेज]({{ '/series/still-and-model/' | relative_url }}) पर है।

## अक्सर पूछे जाने वाले सवाल

**व्हिस्की में कितना पानी मिलाना है, यह निकालने के लिए सिर्फ़ वॉल्यूम घटाना क्यों काफ़ी नहीं?**
क्योंकि एथेनॉल और पानी मिलने पर सिकुड़ते हैं। 63.5% पर 1,000 लीटर को 40% तक लाने के लिए लगभग 605 लीटर पानी चाहिए, वे 587.5 लीटर नहीं जो सीधा वॉल्यूम गणित बताता है, और सिर्फ़ 587.5 लीटर मिलाने से spirit लगभग 40.4% पर रह जाती है। सही तरीका 20 डिग्री C पर density टेबल का इस्तेमाल करके द्रव्यमान में काम करता है, फिर माप से पुष्टि करता है।

**क्या एक LLM व्हिस्की blend के लिए casks चुन सकता है?**
उसे सीधे नहीं चुनना चाहिए। cask चयन एक optimisation समस्या है जिसमें पक्की शर्तें होती हैं, जैसे वॉल्यूम, sensory लक्ष्य और सबसे युवा व्हिस्की की उम्र, और एक linear programming solver इसे ठीक-ठीक हल करता है। LLM का काम है blender के अनुरोध को solver के इनपुट में बदलना, solver बुलाना और नतीजा समझाना।

**व्हिस्की blend में age statement कैसे काम करता है?**
Scotch whisky में और EU नियमों के तहत, लेबल पर उम्र बोतल में मौजूद सबसे युवा व्हिस्की की उम्र है। यह औसत नहीं है। blending टूल को दावे से कम उम्र के हर cask को बाहर रखना होगा, चाहे उसकी कीमत या flavour कितना भी आकर्षक हो, और optimiser को इसे पक्के नियम के रूप में लागू करना चाहिए।
