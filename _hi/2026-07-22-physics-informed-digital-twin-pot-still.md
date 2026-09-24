---
layout: post
lang: hi
title: "Pot still का physics-informed digital twin: सिर्फ़ ML वाले twin क्यों भटकते हैं"
image: /assets/og/physics-informed-digital-twin-pot-still.png
description: "The Still and the Model का भाग 1। बैच pot still Rayleigh समीकरण का पालन करता है, और अंदर गया अल्कोहल बाहर आए अल्कोहल के बराबर होना चाहिए। सिर्फ़ डेटा पर बना twin चुपचाप यह नियम क्यों तोड़ता है, और एक hybrid मॉडल, जिसमें ढाँचा भौतिकी से और कुछ fitted पैरामीटर रन डेटा से आते हैं, कैसे ईमानदार रहता है।"
date: 2026-07-22 09:00:00 -0700
updated: 2026-07-22
permalink: /hi/2026/physics-informed-digital-twin-pot-still/
tags: [distilling-maturation, still-and-model, digital-twin, machine-learning, data-engineering]
faq:
  - q: "still का physics-informed digital twin क्या है?"
    a: "यह ऐसा मॉडल है जिसका ढाँचा आसवन की भौतिकी से आता है, जैसे Rayleigh समीकरण और vapour-liquid equilibrium, और जिसके कुछ पैरामीटर डिस्टिलरी के अपने रन डेटा से fit किए जाते हैं। भौतिकी अल्कोहल संरक्षण जैसी चीज़ों की गारंटी देती है। डेटा मॉडल को इस खास still, इसकी heat input और इसके condenser के हिसाब से ढालता है।"
  - q: "सिर्फ़ डेटा पर बना still twin क्यों भटकता है?"
    a: "सिर्फ़ पिछले रनों पर train हुआ machine learning मॉडल सहसंबंध सीखता है, नियम नहीं। वह heads, hearts और feints के ऐसे वॉल्यूम बता सकता है जिनका जोड़ charge से ज़्यादा अल्कोहल बनता है, और जब charge की strength या heat input उसके training दायरे से बाहर जाए, तो उसे कुछ पता नहीं होता कि क्या करे। उसके ढाँचे में ऐसा कुछ नहीं जो उसे संरक्षण तोड़ने से रोके।"
  - q: "hybrid pot still मॉडल fit करने के लिए कौन सा डेटा चाहिए?"
    a: "हर रन के लिए: charge का वॉल्यूम और strength, समय के साथ heat input या steam flow, spirit safe पर distillate का flow और strength, और cut के समय। hybrid मॉडल के मुट्ठी भर पैरामीटर fit करने के लिए आमतौर पर कुछ दर्जन अच्छी तरह दर्ज रन काफ़ी होते हैं, क्योंकि ज़्यादातर काम भौतिकी करती है।"
---

**संक्षिप्त उत्तर: बैच pot still दो ऐसे नियम मानता है जिन पर कोई data scientist मोलभाव नहीं कर सकता। Rayleigh समीकरण बताता है कि रन आगे बढ़ने के साथ pot और vapour कैसे बदलते हैं, और जितना अल्कोहल आप charge करते हैं वह heads, hearts, feints और residue में इकट्ठे अल्कोहल के बराबर होना चाहिए। पिछले रनों पर सिर्फ़ machine learning से बना digital twin इनमें से कोई नियम नहीं जानता, इसलिए परिस्थितियाँ बदलते ही वह भटक जाता है और ऐसे fractions बता सकता है जिनमें अंदर गए से ज़्यादा अल्कोहल हो। twin को उल्टी तरह बनाइए: ढाँचा भौतिकी से, कुछ fitted पैरामीटर रन डेटा से। इसे कम डेटा चाहिए, यह समझदारी से extrapolate करता है, और यह spirit पैदा नहीं कर सकता।**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एक उदाहरण spirit still रन। 22 प्रतिशत पर 10,000 लीटर low wines के charge में 2,200 लीटर absolute alcohol है। hybrid twin इसे heads 60, hearts 1,050, feints 1,070 और residue 20 में बाँटता है, जिनका जोड़ 2,200 है। सिर्फ़ machine learning वाला twin heads 60, hearts 1,120, feints 1,110 और residue 20 बताता है, जिनका जोड़ 2,310 है, यानी charge से ज़्यादा अल्कोहल।">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">अंदर गया अल्कोहल = बाहर आया अल्कोहल (उदाहरण रन, absolute alcohol के लीटर)</text>
<g font-family="sans-serif">
<rect x="40" y="110" width="200" height="90" rx="10" fill="#06483f"/>
<text x="140" y="140" text-anchor="middle" font-size="12" fill="#cfe6df">charge</text>
<text x="140" y="166" text-anchor="middle" font-size="20" font-weight="700" fill="#ffffff">2,200 LAA</text>
<text x="140" y="187" text-anchor="middle" font-size="10.5" fill="#cfe6df">10,000 L, 22% पर</text>
<line x1="240" y1="155" x2="300" y2="100" stroke="#4db6a2" stroke-width="2"/>
<line x1="240" y1="155" x2="300" y2="220" stroke="#4db6a2" stroke-width="2"/>
<text x="310" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#2e9e7c">HYBRID TWIN</text>
<rect x="300" y="72" width="660" height="56" rx="9" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="330" y="106" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,050 &#183; feints 1,070 &#183; residue 20</text>
<text x="940" y="106" text-anchor="end" font-size="15" font-weight="700" fill="#2e9e7c">= 2,200 &#10003;</text>
<text x="310" y="172" font-size="11" font-weight="700" letter-spacing="1" fill="#ff4081">सिर्फ़ ML वाला TWIN</text>
<rect x="300" y="182" width="660" height="56" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="330" y="216" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,120 &#183; feints 1,110 &#183; residue 20</text>
<text x="940" y="216" text-anchor="end" font-size="15" font-weight="700" fill="#ff4081">= 2,310 &#10007;</text>
<rect x="40" y="272" width="920" height="42" rx="10" fill="#06483f"/>
<text x="500" y="298" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">जो TWIN 110 लीटर अल्कोहल गढ़ सकता है, वह TWIN नहीं है</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरण के आँकड़े। हर fraction अकेले देखने पर ठीक लगता है। सिर्फ़ जोड़ सिर्फ़-ML twin की पोल खोलता है।</figcaption>
</figure>

digital twin प्रोजेक्ट शुरू करने वाली हर डिस्टिलरी को एक ही पिच मिलती है: मॉडल को कुछ साल का रन डेटा खिलाइए, और वह रन की भविष्यवाणी करेगा। heads वॉल्यूम, hearts वॉल्यूम, cut के समय, सब सीखा हुआ। पिछले साल के रनों पर डेमो बेहतरीन दिखता है। फिर charge सामान्य से डेढ़ पॉइंट ज़्यादा strong आता है, या boiler की मरम्मत के बाद steam supply बदल जाती है, और twin ऐसी बातें कहने लगता है जिन्हें stillman बकवास जानता है।

यह **The Still and the Model** की पहली पोस्ट है, एक सीरीज़ जो डिस्टिलरी की संख्याओं के नीचे के डेटा इंजीनियरिंग और GenAI के बारे में है। यह twin से शुरू होती है, क्योंकि डेटा पर फ़िट होने वाले मॉडल और भौतिकी का सम्मान करने वाले मॉडल के बीच का फ़र्क सबसे पहले twin में ही दिखता है।

## pot still असल में क्या करता है

बैच pot still एक पाठ्यपुस्तक वाला उदाहरण है, और पाठ्यपुस्तक के पास सौ साल से ज़्यादा से इसका जवाब है। जैसे-जैसे charge उबलता है, vapour उस तरल से ज़्यादा अल्कोहल-समृद्ध होता है जिसे वह पीछे छोड़ता है, इसलिए pot लगातार कमज़ोर होता जाता है और रन के दौरान distillate की strength गिरती है। Lord Rayleigh ने 1902 में यह संबंध लिखा: रन के हर छोटे हिस्से में, vapour में जाने वाला अल्कोहल pot से घटे अल्कोहल के बराबर है।

कोड में, इसका एक कदम लगभग शर्मिंदगी की हद तक छोटा है:

```python
def rayleigh_step(W, x, dW, vle, eff):
    # W: moles in pot, x: alcohol mole fraction in pot, dW: moles boiled off
    y = x + eff * (vle(x) - x)        # vapour composition, eff fitted from runs
    x_new = (W * x - y * dW) / (W - dW)
    return W - dW, x_new, y
```

`vle(x)` एथेनॉल और पानी का vapour-liquid equilibrium है, जो प्रकाशित डेटा से आता है, आपके रनों से नहीं। `eff` बताता है कि आपका खास still, अपनी गर्दन से होने वाले reflux, lyne arm के कोण और condenser के साथ, उस equilibrium के कितना करीब पहुँचता है। और इसमें बना संरक्षण देखिए: कदम से पहले pot में अल्कोहल बराबर कदम के बाद pot में अल्कोहल जोड़ vapour में अल्कोहल। मॉडल इसे तोड़ नहीं सकता, क्योंकि गणित इसकी इजाज़त नहीं देता।

असली still में reflux, heat input के बदलाव और flavour के लिए अहम तांबे की सतह जुड़ जाती है, इसलिए production twin में कुछ और पद होते हैं। आकार वही रहता है: ज्ञात भौतिकी, और मुट्ठी भर पैरामीटर जो आपके still का वर्णन करते हैं।

## सिर्फ़ ML वाला twin क्यों भटकता है

पिछले रनों पर train हुआ machine learning मॉडल कुछ बिल्कुल अलग करता है। वह सीखता है कि उसने जो रन देखे, उनमें इस तरह का charge उस तरह का hearts cut देता था। यह एक सहसंबंध है, और still पर सहसंबंधों की दो कमज़ोरियाँ हैं।

**वे कुछ भी संरक्षित नहीं करते।** heads, hearts और feints की भविष्यवाणी तीन अलग मॉडलों से कीजिए, या तीन आउटपुट वाले एक मॉडल से, और कुछ भी उन्हें जुड़कर मेल खाने पर मजबूर नहीं करता। ऊपर के उदाहरण रन में हर अनुमानित fraction अपने ऐतिहासिक दायरे के भीतर है। साथ मिलाकर उनमें 110 लीटर absolute alcohol है जो charge में कभी था ही नहीं। डैशबोर्ड पर कोई उन्हें नहीं जोड़ता। excise मिलान में कोई ज़रूर जोड़ेगा।

**वे extrapolate नहीं करते।** training set के रन उन्हीं charge strengths, heat inputs और fill levels को कवर करते हैं जो डिस्टिलरी ने संयोग से इस्तेमाल किए। इनमें से एक बदलिए और मॉडल अंदाज़ा लगा रहा है। भौतिकी वाला मॉडल नहीं: Rayleigh समीकरण को फ़र्क नहीं पड़ता कि charge 21% है या 24%, वह बस चलता है।

गहरी समस्या यह है कि सिर्फ़-डेटा twin ठीक तब कम भरोसेमंद होता है जब उसकी सबसे ज़्यादा ज़रूरत होती है, यानी असामान्य रन पर।

## hybrid: ढाँचे के लिए भौतिकी, पैरामीटर के लिए डेटा

जो तरीका काम करता है वह hybrid है, जिसे कभी-कभी grey-box modelling कहा जाता है। भौतिकी ढाँचा तय करती है: mass और अल्कोहल balances, Rayleigh, vapour-liquid equilibrium, एक सरल heat balance। रन डेटा वे कुछ संख्याएँ fit करता है जो भौतिकी नहीं जान सकती:

- इस still की **enrichment efficiency** (ऊपर का `eff`),
- किसी steam valve position या burner setting के लिए **प्रभावी heat input**,
- **condenser और safe का lag**, यानी pot से vapour निकलने और hydrometer तक spirit पहुँचने के बीच की देरी।

कुछ दर्जन अच्छी तरह दर्ज रनों पर fit किए गए तीन-चार पैरामीटर आमतौर पर असली still को करीब से ट्रैक कर लेते हैं। training दायरे के भीतर उतनी ही सटीकता तक पहुँचने के लिए सिर्फ़-ML twin को कहीं ज़्यादा रन चाहिए, और उसके बाहर वह फिर भी भटका हुआ है।

hybrid में machine learning की भी जगह है: residual को मॉडल करना, यानी भौतिकी के अनुमान और still ने जो किया उसके बीच का अंतर। अगर residual में कोई पैटर्न है (वह परिवेश के तापमान के साथ खिसकता है, या हर CIP के बाद), तो एक छोटा मॉडल उसे सीख सकता है। फ़र्क यह है कि ML एक ठोस मॉडल को सुधार रहा है, उसकी जगह नहीं ले रहा।

## नीचे का डेटा इंजीनियरिंग

twin उतना ही अच्छा है जितने उसके रन रिकॉर्ड, और यहीं ज़्यादातर डिस्टिलरियों को पता चलता है कि वे क्या दर्ज करती रही हैं:

1. **charge का वॉल्यूम और strength, मापे हुए।** योजना वाला charge नहीं। 20 डिग्री C पर strength, hydrometer या density meter से, उपकरण के साथ दर्ज।
2. **time series के रूप में heat input।** हर कुछ सेकंड का steam flow या valve position, historian से, रन शीट पर लिखी कोई setting नहीं।
3. **spirit safe पर distillate का flow और strength।** strength कर्व खींचने लायक रीडिंग, cut के समय और उन्हें किसने किया, समेत।
4. **हर fraction, मापा हुआ।** रन के अंत में heads, hearts और feints के वॉल्यूम और strength, ताकि हर रन का अल्कोहल balance जाँचा जा सके।

वह आखिरी चीज़ आपको मुफ़्त में एक डेटा quality टेस्ट देती है। हर रन के लिए charge अल्कोहल घटा fractions का जोड़ शून्य के करीब होना चाहिए। 5% से चूकने वाला रन मॉडलिंग की समस्या नहीं है। यह मीटर, hydrometer या दर्ज करने की समस्या है, और उस रन से कुछ भी fit करने से पहले इसे ठीक किया जाना चाहिए। [वाइन सीरीज़ का cellar ledger]({{ '/hi/2026/event-sourced-cellar-records-winery/' | relative_url }}) वॉल्यूम के लिए यही तर्क देता है: movements दर्ज कीजिए, और balances को खुद अपनी जाँच करने दीजिए।

## twin किसलिए है

भरोसेमंद twin के साथ काम की चीज़ें काफ़ी विनम्र हैं:

- charge से **रन का पूर्वानुमान**: अपेक्षित cut के समय और fraction वॉल्यूम, ताकि stillman और planner एक ही संख्याएँ देखें।
- **किसी बदलाव को पहले मॉडल पर परखिए।** अलग charge strength या heat profile को still पर चलाने से पहले twin पर चलाया जा सकता है।
- **ऐसे रन को पकड़िए जो भौतिकी के हिसाब से व्यवहार नहीं कर रहा।** यह [अगली पोस्ट]({{ '/hi/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}) का विषय है।

जो यह नहीं करता वह है cut चुनना। cut एक sensory और व्यावसायिक फ़ैसला है जिसे [cut points पोस्ट]({{ '/hi/2024/predicting-distillation-cut-points-ai/' | relative_url }}) विस्तार से बताती है। twin बताता है कि रन किस ओर जा रहा है। वह कहाँ रुकेगा, यह अब भी stillman तय करता है।

## यह कहाँ टूटता है

**congeners एथेनॉल नहीं हैं।** एथेनॉल-पानी equilibrium वाला Rayleigh अल्कोहल को अच्छी तरह ट्रैक करता है। esters, higher alcohols और तांबे से हटने वाले sulphur यौगिक अलग तरह व्यवहार करते हैं, और flavour यही यौगिक तय करते हैं। strength ट्रैक करने वाला twin flavour का twin नहीं है।

**equilibrium डेटा की सीमाएँ हैं।** प्रकाशित vapour-liquid डेटा साफ़ एथेनॉल और पानी का है। low wines में दूसरे volatiles भी होते हैं, और रन के बिल्कुल शुरू और अंत में सरल मॉडल सबसे कम सटीक होता है। twin को रन के बीच वाले हिस्से पर fit कीजिए और परखिए।

**fitted पैरामीटर खिसकते हैं।** तांबा पतला होता है, heating surfaces पर मैल जमता है, condenser बदल दिया जाता है। पैरामीटर तय समय पर दोबारा fit कीजिए और समय के साथ उन पर नज़र रखिए। जो पैरामीटर लगातार खिसकता है, वह still के बारे में बता रहा है, मॉडल के बारे में नहीं।

**खराब रिकॉर्ड एक आत्मविश्वासी खराब twin बनाते हैं।** अगर charge strengths मापी हुई नहीं बल्कि योजना वाली हैं, तो twin कल्पना पर fit होता है और उसे दो दशमलव तक रिपोर्ट करता है।

## निचोड़

still पेय व्यवसाय की उन गिनी-चुनी जगहों में है जहाँ भौतिकी पूरी तरह ज्ञात है और डेटा अधूरा। यह ठीक उसका उल्टा है जो सिर्फ़ machine learning चाहता है। ढाँचे के लिए भौतिकी इस्तेमाल कीजिए, ताकि अल्कोहल संरक्षित रहे और मॉडल उन रनों पर भी ठीक व्यवहार करे जो उसने नहीं देखे। डेटा उन कुछ पैरामीटर के लिए इस्तेमाल कीजिए जो इसे आपका still बनाते हैं। मॉडल रन लॉग देखता है। stillman तांबा, steam और अजीब charge देखता है। hybrid twin वह संस्करण है जो दोनों का सम्मान करता है।

twin को भरने वाले सेंसर के लिए देखें [डिस्टिलरी में IoT]({{ '/hi/2026/iot-in-the-distillery-sensors-process/' | relative_url }})। पूरी सूची [The Still and the Model सीरीज़ पेज]({{ '/series/still-and-model/' | relative_url }}) पर है।

## अक्सर पूछे जाने वाले सवाल

**still का physics-informed digital twin क्या है?**
यह ऐसा मॉडल है जिसका ढाँचा आसवन की भौतिकी से आता है, जैसे Rayleigh समीकरण और vapour-liquid equilibrium, और जिसके कुछ पैरामीटर डिस्टिलरी के अपने रन डेटा से fit किए जाते हैं। भौतिकी अल्कोहल संरक्षण जैसी चीज़ों की गारंटी देती है। डेटा मॉडल को इस खास still, इसकी heat input और इसके condenser के हिसाब से ढालता है।

**सिर्फ़ डेटा पर बना still twin क्यों भटकता है?**
सिर्फ़ पिछले रनों पर train हुआ machine learning मॉडल सहसंबंध सीखता है, नियम नहीं। वह heads, hearts और feints के ऐसे वॉल्यूम बता सकता है जिनका जोड़ charge से ज़्यादा अल्कोहल बनता है, और जब charge की strength या heat input उसके training दायरे से बाहर जाए, तो उसे कुछ पता नहीं होता कि क्या करे। उसके ढाँचे में ऐसा कुछ नहीं जो उसे संरक्षण तोड़ने से रोके।

**hybrid pot still मॉडल fit करने के लिए कौन सा डेटा चाहिए?**
हर रन के लिए: charge का वॉल्यूम और strength, समय के साथ heat input या steam flow, spirit safe पर distillate का flow और strength, और cut के समय। hybrid मॉडल के मुट्ठी भर पैरामीटर fit करने के लिए आमतौर पर कुछ दर्जन अच्छी तरह दर्ज रन काफ़ी होते हैं, क्योंकि ज़्यादातर काम भौतिकी करती है।
