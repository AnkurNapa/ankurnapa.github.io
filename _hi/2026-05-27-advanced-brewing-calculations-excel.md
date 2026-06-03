---
layout: post
lang: hi
title: "20 उन्नत ब्रुइंग गणनाएँ जो आप Excel में कर सकते हैं (फ़ॉर्मूले शामिल)"
image: /assets/og/advanced-brewing-calculations-excel.png
description: "स्ट्राइक तापमान, IBU, ABV, पिचिंग रेट, कार्बोनेशन, रंग, दक्षता और बहुत कुछ — 20 उन्नत ब्रुइंग गणनाएँ काम किए गए उदाहरणों के साथ तैयार-पेस्ट Excel फ़ॉर्मूलों के रूप में।"
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /hi/2026/advanced-brewing-calculations-excel/
tags: [brewing-science, excel, brewing-calculations, recipe-formulation, quality-control]
faq:
  - q: "क्या आप Excel में ABV की गणना कर सकते हैं?"
    a: "हाँ। मानक फ़ॉर्मूला है =(OG-FG)*131.25, जहाँ OG और FG आपकी ओरिजिनल और फ़ाइनल स्पेसिफ़िक ग्रेविटी हैं। उच्च-शक्ति बीयर के लिए एक अधिक सटीक संस्करण है =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794)। दोनों Excel के किसी भी संस्करण में बिना ऐड-इन के काम करते हैं।"
  - q: "मैश स्ट्राइक वॉटर तापमान के लिए Excel फ़ॉर्मूला क्या है?"
    a: "स्ट्राइक टेम्प Tw = (0.2/R)(T2-T1)+T2, जहाँ R क्वार्ट प्रति पाउंड में वॉटर-टू-ग्रेन अनुपात है, T1 ग्रेन तापमान है और T2 आपका लक्ष्य मैश तापमान °F में है। Excel में: =(0.2/B2)*(B4-B3)+B4 जहाँ R, B2 में, ग्रेन टेम्प B3 में और लक्ष्य B4 में हो। मेट्रिक (L/kg, °C) के लिए 0.2 को 0.41 से बदलें।"
  - q: "क्या इन गणनाओं को करने के लिए मुझे विशेष ब्रुइंग सॉफ़्टवेयर चाहिए?"
    a: "नहीं। यहाँ हर गणना — ग्रेविटी, दक्षता, IBU, रंग, पिचिंग रेट, कार्बोनेशन, ABV — बस अंकगणित है जिसे ब्रुइंग सॉफ़्टवेयर अंदर ही अंदर चलाता है। इन फ़ॉर्मूलों वाली एक अकेली Excel शीट इसे पुनरुत्पादित करती है, और चूँकि आप हर सेल देख सकते हैं, आप परिणाम को समझते और उस पर भरोसा करते हैं।"
---

**संक्षिप्त उत्तर: कोई भी संख्या जो एक ब्रुइंग ऐप आपको देता है — स्ट्राइक तापमान, IBU, ABV, पिचिंग रेट, प्राइमिंग शुगर, रंग, दक्षता — वह सादा अंकगणित है जिसे आप बिना ऐड-इन के एक Excel शीट में बना सकते हैं। नीचे काम किए गए उदाहरणों के साथ तैयार-पेस्ट फ़ॉर्मूलों के रूप में 20 उन्नत ब्रुइंग गणनाएँ हैं, जो ब्रू डे भर में व्यवस्थित हैं। सेल एक बार सेट करें और आपके पास एक ब्रूहाउस कैलकुलेटर है जिसे आप पूरी तरह समझते हैं।**

ब्रुइंग सॉफ़्टवेयर गणित को छिपाता है। यह तब तक ठीक है जब तक आपको सुबह 6 बजे एक रेसिपी ट्वीक करनी न हो, एक दक्षता-चूक का मिलान न करना हो, या एक नए ब्रुअर को कार्बोनेशन सेट-पॉइंट समझाना न हो। आपके द्वारा बनाई गई एक स्प्रेडशीट यह सब करती है और अपना काम दिखाती है। यदि आप अब भी ख़ुद को मना रहे हैं, तो [पहले डेटा एकत्र करना]({{ '/hi/2026/collect-your-data-before-ai/' | relative_url }}) सही अंतर्ज्ञान है — ये फ़ॉर्मूले वही हैं जो उन संख्याओं को निर्णयों में बदलते हैं।

पूरे लेख के लिए एक परिपाटी: `B2` जैसे सेल संदर्भ उदाहरण हैं — अपना इनपुट उस सेल में डालें और फ़ॉर्मूला उसके बग़ल में पेस्ट करें। ग्रेविटी स्पेसिफ़िक ग्रेविटी हैं (जैसे 1.050) जब तक न कहा गया हो; "points" का मतलब है अंतिम तीन अंक ((SG − 1) × 1000), इसलिए 1.050 = 50 points। वर्तनी ब्रिटिश है (colour, litres); इम्पीरियल और मेट्रिक नोट वहाँ दिए गए हैं जहाँ स्थिरांक बदलता है।

<aside style="margin:1.6rem 0;padding:1rem 1.25rem;border:1px solid #b45309;border-left:5px solid #b45309;border-radius:8px;background:#f7ece0">
<strong style="color:#b45309">📊 ‘ब्रुअर के लिए Excel’ शृंखला</strong>
<p style="margin:.5rem 0 .35rem">यह पोस्ट हब है। नीचे की छह गणनाओं की एक पूरी गहरी-डुबकी है — एक पूर्ण शीट बिल्ड, अतिरिक्त फ़ॉर्मूले, काम किए गए उदाहरण और एक डायग्राम:</p>
<ul style="margin:0;padding-left:1.2rem;line-height:1.5">
<li><a href="{{ '/hi/2026/build-brewing-water-chemistry-calculator-excel/' | relative_url }}">वॉटर केमिस्ट्री कैलकुलेटर</a> — साल्ट, आयन, रेज़िडुअल एल्कलिनिटी, sulfate:chloride <em>(उपयोग-मामला 9)</em></li>
<li><a href="{{ '/hi/2026/mash-water-temperature-calculator-excel/' | relative_url }}">मैश वॉटर और तापमान कैलकुलेटर</a> — स्ट्राइक, स्टेप, अवशोषण, स्पार्ज <em>(5, 7, 8)</em></li>
<li><a href="{{ '/hi/2026/ibu-recipe-builder-excel/' | relative_url }}">IBU रेसिपी बिल्डर</a> — मल्टी-एडिशन Tinseth, BU:GU, स्केलिंग <em>(10, 11)</em></li>
<li><a href="{{ '/hi/2026/yeast-pitching-rates-starters-excel/' | relative_url }}">यीस्ट पिचिंग रेट और स्टार्टर</a> — वायबिलिटी क्षय, स्टार्टर वृद्धि <em>(13)</em></li>
<li><a href="{{ '/hi/2026/carbonation-calculator-excel/' | relative_url }}">कार्बोनेशन कैलकुलेटर</a> — प्राइमिंग शुगर, केग PSI, लाइन बैलेंसिंग <em>(17)</em></li>
<li><a href="{{ '/hi/2026/brewhouse-efficiency-yield-excel/' | relative_url }}">ब्रूहाउस दक्षता और यील्ड मिलान</a> — कन्वर्ज़न बनाम लॉटर लॉस <em>(2, 3)</em></li>
</ul>
</aside>

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1046 280" width="100%" style="max-width:1046px;height:auto" role="img" aria-label="ब्रू-डे प्रक्रिया प्रवाह जो दिखाता है कि 20 में से कौन-सी गणनाएँ हर चरण पर लागू होती हैं">
<rect x="0" y="0" width="1046" height="280" fill="#fdfbf7"/>
<text x="523" y="34" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="700" fill="#1c1a17">ब्रू डे, संख्याओं के अनुसार — हर गणना कहाँ बैठती है</text>
<g font-family="sans-serif">
<rect x="4" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="83" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">रेसिपी</text>
<text x="83" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">1 · SG ↔ °Plato</text>
<text x="83" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">2 · ग्रिस्ट से OG</text>
<text x="83" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">3 · दक्षता</text>
<text x="83" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">12 · रंग SRM</text>
<rect x="180" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="259" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">मैश</text>
<text x="259" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">5 · स्ट्राइक टेम्प</text>
<text x="259" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">6 · स्टेप इन्फ़्यूज़न</text>
<text x="259" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">7 · लिकर:ग्रिस्ट</text>
<text x="259" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">9 · वॉटर साल्ट</text>
<rect x="356" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="435" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">उबाल</text>
<text x="435" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">8 · बॉइल-ऑफ़</text>
<text x="435" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">10 · IBU (Tinseth)</text>
<text x="435" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">11 · हॉप सब</text>
<rect x="532" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="611" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">फ़र्मेंट</text>
<text x="611" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">13 · पिच रेट</text>
<text x="611" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">14 · एटेन्युएशन</text>
<text x="611" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">4 · टेम्प सुधार</text>
<text x="611" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">15 · रिफ़्रैक्टोमीटर</text>
<rect x="708" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="787" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">पैकेज</text>
<text x="787" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">16 · ABV</text>
<text x="787" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">17 · कार्बोनेशन</text>
<text x="787" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">18 · ब्लेंड/डाइल्यूट</text>
<text x="787" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">19 · कैलोरी</text>
<rect x="884" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#7a1f3d" stroke-width="1.5"/>
<text x="963" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#7a1f3d">लागत</text>
<text x="963" y="118" text-anchor="middle" font-size="12.5" fill="#1c1a17">20 · COGS / hL</text>
<text x="963" y="142" text-anchor="middle" font-size="12.5" fill="#1c1a17">और प्रति पिंट लागत</text>
</g>
<g fill="#b45309" stroke="#b45309" stroke-width="2">
<line x1="162" y1="155" x2="174" y2="155"/><polygon points="174,150 181,155 174,160" stroke="none"/>
<line x1="338" y1="155" x2="350" y2="155"/><polygon points="350,150 357,155 350,160" stroke="none"/>
<line x1="514" y1="155" x2="526" y2="155"/><polygon points="526,150 533,155 526,160" stroke="none"/>
<line x1="690" y1="155" x2="702" y2="155"/><polygon points="702,150 709,155 702,160" stroke="none"/>
<line x1="866" y1="155" x2="878" y2="155"/><polygon points="878,150 885,155 878,160" stroke="none"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">20 गणनाएँ, उस चरण से मैप की गईं जहाँ आप उनका उपयोग करते हैं। नीचे की संख्याएँ इस मानचित्र से मेल खाती हैं।</figcaption>
</figure>

## रेसिपी और ग्रेविटी

**1. स्पेसिफ़िक ग्रेविटी को °Plato में बदलें।** ब्रुअर और इंस्ट्रूमेंट स्केल पर असहमत होते हैं; बिना लुकअप टेबल के बदलें।
फ़ॉर्मूला: °P ≈ 259 − (259 ÷ SG)।
Excel (SG `B2` में): `=259-(259/B2)`। उलटा (Plato → SG): `=259/(259-B2)`।
उदाहरण: SG 1.048 → `=259-(259/1.048)` = **11.9 °P**।

**2. ग्रेन बिल से ओरिजिनल ग्रेविटी का पूर्वानुमान।** ब्रू करने से पहले अपनी OG जानें।
फ़ॉर्मूला: points = Σ(weight × PPG) × efficiency ÷ volume; OG = 1 + points ÷ 1000। PPG, points-per-pound-per-gallon है (पेल मॉल्ट के लिए ≈ 37)।
Excel (वज़न `B2:B6` में, PPG `C2:C6` में, दक्षता `F2` में, पोस्ट-बॉइल गैलन `G2` में): `=1+(SUMPRODUCT(B2:B6,C2:C6)*F2)/(G2*1000)`।
उदाहरण: 10 lb पेल मॉल्ट (PPG 37) 75% पर 5.5 gal में → **1.050**।

**3. ब्रूहाउस और मैश दक्षता।** वह एकल संख्या जो समझाती है कि आपकी OG क्यों चूकी।
फ़ॉर्मूला: efficiency = (measured points × volume) ÷ maximum possible points।
Excel (OG `B2` में, एकत्र किए गैलन `B3` में, कुल संभावित points Σ(lb × PPG) `B4` में): `=((B2-1)*1000*B3)/B4*100`।
उदाहरण: OG 1.050, 5.5 gal, 370 संभावित points → **74%**।

**4. हाइड्रोमीटर तापमान सुधार।** एक गरम नमूना कम पढ़ता है; अनुमान के बजाय इसे ठीक करें।
फ़ॉर्मूला: हाइड्रोमीटर के कैलिब्रेशन तापमान (°F) के सापेक्ष नमूना तापमान में एक क्यूबिक।
Excel (मापी गई SG `B2`, नमूना टेम्प °F `B3`, कैलिब्रेशन टेम्प °F `B4`): `=B2*((1.00130346-0.000134722124*B3+0.00000204052596*B3^2-0.00000000232820948*B3^3)/(1.00130346-0.000134722124*B4+0.00000204052596*B4^2-0.00000000232820948*B4^3))`।
उदाहरण: 1.050, 100 °F पर पढ़ा गया, 60 °F पर कैलिब्रेटेड → **1.056**।

## मैश और वॉटर

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 230" width="100%" style="max-width:760px;height:auto" role="img" aria-label="स्ट्राइक वॉटर ऊष्मा संतुलन: गरम लिकर प्लस ठंडा ग्रेन बराबर लक्ष्य तापमान पर मैश">
<rect x="0" y="0" width="760" height="230" fill="#fdfbf7"/>
<rect x="20" y="60" width="180" height="110" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="110" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#1c1a17">गरम लिकर</text>
<text x="110" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#b45309">Tw ≈ 164 °F</text>
<text x="110" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">(जिस तक आप गरम करते हैं)</text>
<text x="230" y="122" text-anchor="middle" font-family="sans-serif" font-size="30" font-weight="700" fill="#6b6258">+</text>
<rect x="260" y="60" width="180" height="110" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="350" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#1c1a17">ग्रेन</text>
<text x="350" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#b45309">T1 = 65 °F</text>
<text x="350" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">(विशिष्ट ऊष्मा ≈ 0.2)</text>
<g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="450" y1="115" x2="490" y2="115"/><polygon points="490,108 502,115 490,122" stroke="none"/></g>
<rect x="510" y="60" width="220" height="110" rx="8" fill="#b45309"/>
<text x="620" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#fdfbf7">मैश टन</text>
<text x="620" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#fdfbf7">T2 = 152 °F लक्ष्य</text>
<text x="620" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#f7ece0">(जो आप चाहते हैं)</text>
<text x="380" y="205" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#1c1a17">Tw = (0.2 ÷ R)(T2 − T1) + T2  →  पानी को इतना गरम करें कि वह ग्रेन के ठंडे द्रव्यमान को सोख ले</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">स्ट्राइक-वॉटर ऊष्मा संतुलन (उपयोग-मामला 5): पानी इतना गरम चलना चाहिए कि ठंडा ग्रेन मिश्रण को लक्ष्य तक नीचे खींच ले।</figcaption>
</figure>

**5. स्ट्राइक (मैश-इन) वॉटर तापमान।** लिकर को इतना गरम करें कि ठंडा ग्रेन आपको लक्ष्य पर लाए।
फ़ॉर्मूला: Tw = (0.2 ÷ R)(T2 − T1) + T2 — R = water:grain in qt/lb, T1 = ग्रेन टेम्प, T2 = लक्ष्य मैश टेम्प (°F)।
Excel (R `B2` में, ग्रेन टेम्प `B3` में, लक्ष्य `B4` में): `=(0.2/B2)*(B4-B3)+B4`।
उदाहरण: R = 1.5 qt/lb, ग्रेन 65 °F, लक्ष्य 152 °F → **163.6 °F**। मेट्रिक (L/kg, °C): `0.2` को `0.41` से बदलें।

**6. स्टेप-मैश इन्फ़्यूज़न (उबलते पानी का जोड़)।** कितना उबलता पानी मैश को अगले रेस्ट तक बढ़ाता है।
फ़ॉर्मूला: Wa = (T2 − T1)(0.2·G + Wm) ÷ (Tw − T2) — G = ग्रेन (lb), Wm = मैश में पहले से पानी (qt), Tw = 212 °F।
Excel (G `B2`, वर्तमान टेम्प `B3`, लक्ष्य `B4`, मैश वॉटर `B5`, इन्फ़्यूज़न टेम्प `B6`): `=(B4-B3)*(0.2*B2+B5)/(B6-B4)`।
उदाहरण: 10 lb, 152→168 °F, मैश में 15 qt, 212 °F पानी → **6.2 qt**।

**7. लिकर-टू-ग्रिस्ट अनुपात (मैश गाढ़ापन)।** पतले मैश फ़र्मेंटेबिलिटी का पक्ष लेते हैं; गाढ़े मैश एंज़ाइम की रक्षा करते हैं।
फ़ॉर्मूला: ratio = water ÷ grain।
Excel (water `B2`, grain `B3`): `=B2/B3`। qt/lb → L/kg बदलें `=B2/B3*2.086` से।
उदाहरण: 15 qt ÷ 10 lb = **1.5 qt/lb** (≈ 3.13 L/kg)।

**8. प्री-बॉइल वॉल्यूम और बॉइल-ऑफ़।** सही प्री-बॉइल से शुरू करके अपना पोस्ट-बॉइल वॉल्यूम पाएँ।
फ़ॉर्मूला: pre-boil = target post-boil + (evaporation rate × boil hours); कूलिंग सिकुड़न के लिए ~4% जोड़ें।
Excel (लक्ष्य पोस्ट-बॉइल litres `B2`, evap L/hr `B3`, hours `B4`): `=(B2/0.96)+B3*B4`।
उदाहरण: 23 L लक्ष्य, 4 L/hr, 1 hr → **≈ 28 L** प्री-बॉइल।

**9. वॉटर केमिस्ट्री — रेज़िडुअल एल्कलिनिटी और sulfate:chloride.** दो संख्याएँ जो मैश pH और हॉप कैरेक्टर तय करती हैं।
फ़ॉर्मूले: RA = alkalinity − (Ca ÷ 3.5 + Mg ÷ 7), सभी ppm में; SO₄:Cl = sulfate ÷ chloride।
Excel (alkalinity as CaCO₃ `B2`, Ca `B3`, Mg `B4`, sulfate `B5`, chloride `B6`): RA `=B2-(B3/3.5+B4/7)`, अनुपात `=B5/B6`।
साल्ट जोड़ (प्रति ग्राम प्रति गैलन): जिप्सम 61.5 ppm Ca + 147.4 ppm SO₄ जोड़ता है; कैल्शियम क्लोराइड 72 ppm Ca + 127.4 ppm Cl जोड़ता है। नया स्तर: `=base_ppm + grams_per_gal*61.5`।
उदाहरण: alkalinity 100, Ca 50, Mg 10 → RA **84 ppm**; SO₄ 150, Cl 50 → **3.0** (हॉप-फ़ॉरवर्ड)।

## उबाल और हॉप्स

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 350" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Tinseth हॉप उपयोगिता वक्र जो तेज़ी से चढ़ता फिर उबाल के 60 मिनट तक समतल हो जाता है">
<rect x="0" y="0" width="620" height="350" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">हॉप उपयोगिता बनाम उबाल समय (Tinseth)</text>
<g stroke="#e0d8cc" stroke-width="1">
<line x1="60" y1="40" x2="580" y2="40"/><line x1="60" y1="170" x2="580" y2="170"/>
</g>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="580" y2="300"/></g>
<polyline points="60,300 117.8,217.3 175.6,161.9 233.3,124.9 291.1,100.1 406.7,72.1 493.3,61.9 580,56.2" fill="none" stroke="#b45309" stroke-width="3"/>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle">
<text x="60" y="318">0</text><text x="233" y="318">30</text><text x="406" y="318">60</text><text x="580" y="318">90</text>
<text x="320" y="340">उबाल समय (मिनट)</text>
</g>
<text x="20" y="170" font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle" transform="rotate(-90 20 170)">उपयोगिता</text>
<line x1="406" y1="72" x2="470" y2="120" stroke="#7a1f3d" stroke-width="1"/>
<text x="475" y="124" font-family="sans-serif" font-size="12" fill="#7a1f3d">अधिकांश कड़वाहट</text>
<text x="475" y="140" font-family="sans-serif" font-size="12" fill="#7a1f3d">~60 मिनट तक तय</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">क्यों एक 90-मिनट का जोड़ एक 60-मिनट के जोड़ से ज़्यादा कड़वा नहीं होता (उपयोग-मामला 10)।</figcaption>
</figure>

**10. Tinseth विधि से IBU।** उद्योग-मानक कड़वाहट अनुमान, दो सेल में।
फ़ॉर्मूले: utilisation = (1.65 × 0.000125^(OG−1)) × ((1 − e^(−0.04·t)) ÷ 4.15); IBU = utilisation × (AA% × grams × 1000 ÷ litres)।
Excel (AA% `B2`, grams `B3`, boil min `B4`, litres `B5`, OG `B6`): utilisation `B7` में = `=(1.65*0.000125^(B6-1))*((1-EXP(-0.04*B4))/4.15)`; IBU = `=B7*((B2/100)*B3*1000)/B5`।
उदाहरण: 28 g 6.4% AA पर, 60 min, 23 L, OG 1.050 → **≈ 18 IBU**।

**11. अल्फा एसिड से हॉप प्रतिस्थापन।** स्टॉक ख़त्म? वज़न नहीं, कड़वाहट मिलाएँ।
फ़ॉर्मूला: new weight = (original weight × original AA%) ÷ new AA%।
Excel (original grams `B2`, original AA% `B3`, substitute AA% `B4`): `=(B2*B3)/B4`।
उदाहरण: रेसिपी 28 g 6.4% पर चाहती है; आपके पास 9.2% AA हॉप्स हैं → **19.5 g**।

**12. बीयर रंग (SRM और EBC)।** मैश से पहले गिलास का अनुमान लगाएँ।
फ़ॉर्मूले: MCU = Σ(grain °L × weight lb) ÷ gallons; SRM = 1.4922 × MCU^0.6859 (Morey); EBC = SRM × 1.97।
Excel (°L `B2:B3`, weights `C2:C3`, gallons `D2`): MCU `E2` = `=SUMPRODUCT(B2:B3,C2:C3)/D2`; SRM `F2` = `=1.4922*E2^0.6859`; EBC = `=F2*1.97`।
उदाहरण: 9 lb पेल (3 °L) + 1 lb क्रिस्टल (60 °L) 5.5 gal में → MCU 15.8 → **≈ 10 SRM / 19 EBC** (एम्बर)।

## यीस्ट और फ़र्मेंटेशन

**13. यीस्ट पिचिंग रेट।** अंडर-पिचिंग सबसे आम टाली जाने योग्य दोष है; इसका आकार दें।
फ़ॉर्मूला: billion cells = pitch rate (M cells/mL/°P) × volume (L) × °Plato। दर ≈ एल के लिए 0.75, लेगर के लिए 1.5।
Excel (rate `B2`, litres `B3`, °P `B4`): cells `=B2*B3*B4`; प्रति 100 B के पैक `=B2*B3*B4/100`।
उदाहरण: एल 0.75 पर, 23 L, 12 °P → **207 billion cells** ≈ 2 ताज़ा पैक या एक स्टार्टर।

**14. अपैरेंट और रियल एटेन्युएशन।** यीस्ट वास्तव में कितना आगे गया।
फ़ॉर्मूले: apparent = (OG − FG) ÷ (OG − 1) × 100; real ≈ apparent × 0.81 (वास्तविक रियल डिग्री Plato से रियल एक्सट्रैक्ट इस्तेमाल करती है)।
Excel (OG `B2`, FG `B3`): apparent `=(B2-B3)/(B2-1)*100`; real `=(B2-B3)/(B2-1)*100*0.81`।
उदाहरण: 1.050 → 1.010 → **80% apparent / ≈ 65% real**।

**15. रिफ़्रैक्टोमीटर फ़ाइनल-ग्रेविटी सुधार।** एक बार अल्कोहल मौजूद होने पर रिफ़्रैक्टोमीटर झूठ बोलते हैं; यह उसे ठीक करता है।
फ़ॉर्मूला: इनिशियल और फ़ाइनल Brix में Terrill क्यूबिक (पहले हर रीडिंग को अपने वोर्ट करेक्शन फ़ैक्टर, ~1.04 से भाग दें)।
Excel (corrected initial Brix `B2`, corrected final Brix `B3`): `=1.0000-0.0044993*B2+0.011774*B3+0.00027581*B2^2-0.0012717*B3^2-0.00000728*B2^3+0.000063293*B3^3`।
उदाहरण: 12.5 → 6.0 Brix → FG **≈ 1.011**।

**16. ग्रेविटी से ABV।** हेडलाइन संख्या, दो तरह से।
फ़ॉर्मूले: simple = (OG − FG) × 131.25; अधिक सटीक (मज़बूत बीयर) = (76.08 × (OG − FG) ÷ (1.775 − OG)) × (FG ÷ 0.794)।
Excel (OG `B2`, FG `B3`): simple `=(B2-B3)*131.25`; accurate `=(76.08*(B2-B3)/(1.775-B2))*(B3/0.794)`।
उदाहरण: 1.050 → 1.011 → **5.1% (simple) / 5.2% (accurate)**।

## पैकेजिंग और फ़िनिशिंग

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 560 300" width="100%" style="max-width:560px;height:auto" role="img" aria-label="दो बीयर को एक लक्ष्य ABV में ब्लेंड करने के लिए Pearson का स्क्वायर">
<rect x="0" y="0" width="560" height="300" fill="#fdfbf7"/>
<text x="280" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Pearson का स्क्वायर — एक लक्ष्य पर ब्लेंड करें</text>
<rect x="170" y="60" width="220" height="180" fill="none" stroke="#b45309" stroke-width="1.5"/>
<line x1="170" y1="60" x2="390" y2="240" stroke="#e0d8cc" stroke-width="1.5"/>
<line x1="170" y1="240" x2="390" y2="60" stroke="#e0d8cc" stroke-width="1.5"/>
<rect x="232" y="128" width="96" height="44" rx="6" fill="#b45309"/>
<text x="280" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#fdfbf7">लक्ष्य</text>
<text x="280" y="164" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fdfbf7">5.0%</text>
<text x="178" y="84" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">A: 6.5%</text>
<text x="178" y="232" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">B: 3.0%</text>
<text x="382" y="84" text-anchor="end" font-family="sans-serif" font-size="13" fill="#7a1f3d">parts A = 5.0−3.0 = 2.0</text>
<text x="382" y="232" text-anchor="end" font-family="sans-serif" font-size="13" fill="#7a1f3d">parts B = 6.5−5.0 = 1.5</text>
<text x="280" y="278" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1c1a17">ब्लेंड 2.0 : 1.5 (A : B) → 5.0% ✓</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Pearson का स्क्वायर (उपयोग-मामला 18): हर कोना ब्लेंड अनुपात देने के लिए तिरछे घटाता है।</figcaption>
</figure>

**17. बॉटल कार्बोनेशन के लिए प्राइमिंग शुगर।** बिना बॉटल बम के एक लक्ष्य CO₂ पाएँ।
फ़ॉर्मूले: residual CO₂ (vols) = 3.0378 − 0.050062·T + 0.00026555·T² (T = सबसे ऊँचा तापमान जो बीयर ने देखा, °F); corn sugar (g) = (target vols − residual) × litres × 4.0।
Excel (max temp °F `B2`, target vols `B3`, litres `B4`): residual `B5` = `=3.0378-0.050062*B2+0.00026555*B2^2`; sugar = `=(B3-B5)*B4*4.0`।
उदाहरण: 68 °F, लक्ष्य 2.4 vols, 23 L → residual 0.86 → **≈ 141 g corn sugar**। (टेबल शुगर: × 0.91.)

**18. एक लक्ष्य पर ब्लेंड या डाइल्यूट करें।** एक हाई-ग्रेविटी वोर्ट को पानी से ट्रिम करें, या दो बीयर को एक संख्या से मिलाएँ।
डाइल्यूशन फ़ॉर्मूला: water to add = volume × (current points − target points) ÷ target points।
Excel (volume `B2`, current points `B3`, target points `B4`): `=B2*(B3-B4)/B4`।
उदाहरण: 25 L 1.060 (60 pts) पर 1.050 (50 pts) तक → **5 L पानी जोड़ें**। दो तैयार बीयर को एक लक्ष्य ABV में ब्लेंड करने के लिए, ऊपर का Pearson का स्क्वायर इस्तेमाल करें: parts = तिरछे अंतर।

**19. प्रति सर्विंग कैलोरी।** एक लेबल संख्या जो मार्केटिंग हमेशा माँगती है।
फ़ॉर्मूले (प्रति 12 oz / 355 mL): alcohol cal = 1881.22 × FG × (OG − FG) ÷ (1.775 − OG); carbohydrate cal = 3550 × FG × ((0.1808 × OG) + (0.8192 × FG) − 1.0004); total = sum।
Excel (OG `B2`, FG `B3`): alcohol `=1881.22*B3*(B2-B3)/(1.775-B2)`; carbs `=3550*B3*((0.1808*B2)+(0.8192*B3)-1.0004)`; 355 mL से सर्विंग साइज़ अनुसार स्केल करें।
उदाहरण: 1.050 → 1.011 → ≈ 102 (alcohol) + 64 (carbs) = **≈ 166 cal** प्रति 12 oz।

## लागत

**20. प्रति हेक्टोलीटर और प्रति पिंट लागत।** जहाँ रेसिपी गणित P&L से मिलता है।
फ़ॉर्मूले: COGS/hL = total batch cost ÷ batch volume (hL); cost/pint = COGS/hL × 0.00568 (एक UK पिंट 0.568 L है; 1 hL = 100 L)।
Excel (total batch cost `B2`, batch hL `B3`): COGS/hL `B4` = `=B2/B3`; cost/pint = `=B4*0.00568`।
उदाहरण: £450 बैच, 10 hL → **£45/hL ≈ £0.26 प्रति पिंट**। इसे [प्रति हेक्टोलीटर COGS]({{ '/hi/2025/cost-of-goods-per-hectoliter/' | relative_url }}) में दी गई विधि से ठीक से बनाएँ।

## निचोड़

ये 20 फ़ॉर्मूले ब्रू डे को आद्योपांत कवर करते हैं: रेसिपी डिज़ाइन, मैश और वॉटर, उबाल और हॉप्स, फ़र्मेंटेशन, पैकेजिंग और लागत। किसी को ऐड-इन की ज़रूरत नहीं — उन्हें एक शीट में पेस्ट करें, अपने इनपुट सेल को लेबल करें, और आपके पास एक ब्रूहाउस कैलकुलेटर है जो अपना काम दिखाता है और जिसे आप लाइन-दर-लाइन ऑडिट कर सकते हैं। इनपुट ईमानदार रखें (तौलें, मापें, रिकॉर्ड करें) और गणित हर बार सही होगा; वही अनुशासन ठीक वही है जो [ब्रुअर से डेटा साइंटिस्ट तक]({{ '/hi/2026/from-brewer-to-data-scientist/' | relative_url }}) की छलाँग को एक छोटी छलाँग बनाता है जब आप उसके लिए तैयार हों।

## अक्सर पूछे जाने वाले प्रश्न

**क्या आप Excel में ABV की गणना कर सकते हैं?**
हाँ। मानक फ़ॉर्मूला है =(OG-FG)*131.25, जहाँ OG और FG आपकी ओरिजिनल और फ़ाइनल स्पेसिफ़िक ग्रेविटी हैं। उच्च-शक्ति बीयर के लिए एक अधिक सटीक संस्करण है =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794)। दोनों Excel के किसी भी संस्करण में बिना ऐड-इन के काम करते हैं।

**मैश स्ट्राइक वॉटर तापमान के लिए Excel फ़ॉर्मूला क्या है?**
स्ट्राइक टेम्प Tw = (0.2/R)(T2-T1)+T2, जहाँ R क्वार्ट प्रति पाउंड में वॉटर-टू-ग्रेन अनुपात है, T1 ग्रेन तापमान है और T2 आपका लक्ष्य मैश तापमान °F में है। Excel में: =(0.2/B2)*(B4-B3)+B4 जहाँ R, B2 में, ग्रेन टेम्प B3 में और लक्ष्य B4 में हो। मेट्रिक (L/kg, °C) के लिए 0.2 को 0.41 से बदलें।

**क्या इन गणनाओं को करने के लिए मुझे विशेष ब्रुइंग सॉफ़्टवेयर चाहिए?**
नहीं। यहाँ हर गणना — ग्रेविटी, दक्षता, IBU, रंग, पिचिंग रेट, कार्बोनेशन, ABV — बस अंकगणित है जिसे ब्रुइंग सॉफ़्टवेयर अंदर ही अंदर चलाता है। इन फ़ॉर्मूलों वाली एक अकेली Excel शीट इसे पुनरुत्पादित करती है, और चूँकि आप हर सेल देख सकते हैं, आप परिणाम को समझते और उस पर भरोसा करते हैं।

*[ब्रुइंग साइंस और AI]({{ '/hi/tracks/brewing-science-ai/' | relative_url }}) ट्रैक का हिस्सा।*
