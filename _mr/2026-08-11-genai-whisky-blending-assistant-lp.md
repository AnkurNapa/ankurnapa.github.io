---
layout: post
lang: mr
title: "गणित code मध्ये करणारा GenAI blending assistant: vatting साठी LP, पाण्यासाठी density tables"
image: /assets/og/genai-whisky-blending-assistant-lp.png
description: "The Still and the Model चा भाग 5. language model blender ला vatting मधून मार्गदर्शन करू शकते, पण त्याने कधीच बेरजा करू नयेत. cask selection हा linear programme आहे, bottling strength पर्यंत reduction ला ethanol-पाणी contraction चे गणित लागते, आणि age statement हा नियम आहे, सरासरी नाही. LLM tools call करते आणि उत्तर समजावते."
date: 2026-08-11 09:00:00 -0700
updated: 2026-08-11
permalink: /mr/2026/genai-whisky-blending-assistant-lp/
tags: [distilling-maturation, still-and-model, generative-ai, optimisation, blending]
faq:
  - q: "whisky मध्ये किती पाणी घालायचे हे फक्त volumes वजा करून का काढता येत नाही?"
    a: "कारण ethanol आणि पाणी मिसळल्यावर आकुंचन पावतात. 63.5% वरील 1,000 litres 40% पर्यंत आणायला साधारण 605 litres पाणी लागते, साध्या volume गणिताने सुचवलेले 587.5 litres नव्हे, आणि फक्त 587.5 litres घातल्यास spirit साधारण 40.4% वर राहते. योग्य पद्धत 20 degrees C वरील density tables वापरून mass मध्ये काम करते, आणि मग मोजमापाने खात्री करते."
  - q: "LLM whisky blend साठी casks निवडू शकते का?"
    a: "त्याने ते थेट निवडू नयेत. cask selection ही volume, sensory targets आणि सर्वात तरुण whisky चे वय यासारख्या कठोर constraints असलेली optimisation समस्या आहे, आणि linear programming solver ती तंतोतंत हाताळतो. LLM चे काम म्हणजे blender ची मागणी solver inputs मध्ये बदलणे, solver call करणे आणि निकाल समजावणे."
  - q: "whisky blend मध्ये age statement कसे काम करते?"
    a: "Scotch whisky मध्ये आणि EU नियमांनुसार label वरील वय म्हणजे bottle मधील सर्वात तरुण whisky चे वय. ती सरासरी नाही. blending tool ने दाव्यापेक्षा तरुण प्रत्येक cask वगळलाच पाहिजे, त्याची किंमत किंवा flavour कितीही आकर्षक असो, आणि optimiser ने तो कठोर नियम म्हणून लागू करायला हवा."
---

**थोडक्यात उत्तर: GenAI blender साठी चांगला interface आहे आणि वाईट calculator. cask selection हा linear programme आहे: volume आणि sensory targets वापरलेल्या stock च्या सर्वात कमी मूल्यात गाठणे, आणि age statement कठोर नियम म्हणून, कारण label सरासरी नव्हे तर सर्वात तरुण whisky सांगते. bottling strength पर्यंत reduction ला ethanol-पाणी contraction चे गणित लागते: 63.5% वरील 1,000 litres ना 40% गाठायला साधारण 605 litres पाणी लागते, 587.5 नव्हे. दोन्ही गणिते तपासलेल्या code मध्ये ठेवा, त्यांना tools म्हणून उपलब्ध करा, आणि language model ला जे जमते ते करू द्या: मागणी समजून घेणे, tools call करणे आणि उत्तर साध्या शब्दांत समजावणे.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="blending assistant ची रचना. blender किमान 6 sherry character score असलेले 300 litres absolute alcohol चे 12 वर्षे जुने vatting मागतो. LLM दोन tools call करते. cask selection solver cask A मधून 94, cask B मधून 130 आणि cask C मधून 76 litres absolute alcohol देतो, आणि cask D 10 वर्षांचा असल्याने वगळतो. reduction tool सांगते की 63.5 टक्क्यांवरील 1,000 litres ना 40 टक्के गाठायला 604.9 litres पाणी लागते, आणि भोळे 587.5 litres ते 40.4 टक्क्यांवर ठेवतील. मग LLM निकाल समजावते.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">LLM विचारते, TOOLS गणित करतात (उदाहरणादाखल)</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="250" height="100" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="155" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">blender विचारतो</text>
<text x="155" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">12 वर्षे जुने vatting,</text>
<text x="155" y="125" text-anchor="middle" font-size="10.5" fill="#4a6b64">300 LAA, sherry score &#8805; 6,</text>
<text x="155" y="142" text-anchor="middle" font-size="10.5" fill="#4a6b64">वापरलेल्या stock चे किमान मूल्य</text>
<line x1="280" y1="110" x2="340" y2="110" stroke="#4db6a2" stroke-width="2"/>
<rect x="340" y="75" width="160" height="70" rx="12" fill="#06483f"/>
<text x="420" y="106" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="126" text-anchor="middle" font-size="10.5" fill="#cfe6df">tools call करते, समजावते</text>
<line x1="500" y1="100" x2="560" y2="80" stroke="#4db6a2" stroke-width="2"/>
<line x1="500" y1="125" x2="560" y2="200" stroke="#4db6a2" stroke-width="2"/>
<rect x="560" y="50" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="74" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">select_casks() &#183; linear programme</text>
<text x="765" y="96" text-anchor="middle" font-size="11" fill="#06483f">A 94 LAA &#183; B 130 LAA &#183; C 76 LAA</text>
<text x="765" y="116" text-anchor="middle" font-size="11" fill="#06483f">sherry score 6.0, मूल्य 415</text>
<text x="765" y="136" text-anchor="middle" font-size="11" fill="#ff4081">D वगळला: 10 वर्षे जुना</text>
<rect x="560" y="165" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="189" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">reduction_water() &#183; density tables</text>
<text x="765" y="211" text-anchor="middle" font-size="11" fill="#06483f">63.5% वरील 1,000 L ते 40%: 604.9 L पाणी</text>
<text x="765" y="231" text-anchor="middle" font-size="11" fill="#06483f">अंतिम 1,587.5 L, 635 LAA</text>
<text x="765" y="251" text-anchor="middle" font-size="11" fill="#ff4081">भोळे 587.5 L ते 40.4% वर ठेवतात</text>
<rect x="30" y="286" width="940" height="40" rx="10" fill="#06483f"/>
<text x="500" y="311" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">प्रत्येक आकडा TOOL कडून येतो &#183; MODEL कधीच बेरजा करत नाही</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरणादाखल stock आणि मूल्ये. दोन्ही tools साधे, तपासलेले code आहेत. language model हा interface आहे.</figcaption>
</figure>

एक blender GenAI assistant ला विचारतो की 63.5% वरील 1,000 litres cask-strength spirit 40% पर्यंत आणायला किती पाणी घालायचे. assistant क्षणात उत्तर देतो: 587.5 litres. तो गणित दाखवतो, आणि गणित नीटनेटके आहे. पण ते चुकीचे आहे, आणि ही चूक rounding ची नाही. हे असे रसायनशास्त्र आहे ज्याबद्दल model ला कोणी सांगितलेच नाही.

ही पोस्ट अशा blending assistant बद्दल आहे जो ती चूक करूच शकत नाही, कारण तो कधीच गणित करत नाही. मागील पोस्टमधील [cask inventory]({{ '/mr/2026/cask-inventory-data-engineering-scd2/' | relative_url }}) stock पुरवते. गणित tools मध्ये राहते. model बोलते.

## पाण्याची समस्या: volumes ची बेरीज का होत नाही

63.5% ABV वरील 1,000 litres घ्या. त्यात 635 litres absolute alcohol आहे. 40% वर ते 635 litres alcohol 635 / 0.40 = 1,587.5 litres spirit बनवतात. म्हणून स्पष्ट उत्तर म्हणजे 587.5 litres पाणी घालणे.

अडचण अशी की ethanol आणि पाणी मिसळल्यावर आकुंचन पावतात. रेणू दोन्हीपैकी कोणत्याही द्रवापेक्षा एकमेकांत अधिक घट्ट बसतात, म्हणून 1,000 litres spirit अधिक 587.5 litres पाणी 1,587.5 litres पेक्षा कमी होते. strength लक्ष्यापेक्षा वर राहते, या उदाहरणात साधारण 40.4%.

योग्य पद्धत 20 degrees C वरील ethanol-पाणी मिश्रणांची density वापरून mass मध्ये काम करते, कारण mass conserve होते:

```python
def reduction_water(vol_l, abv_in, abv_out, rho20):
    # rho20(abv) -> density in kg/L at 20 C, from the official alcoholometric tables
    laa = vol_l * abv_in / 100
    vol_out = laa / (abv_out / 100)
    mass_in = vol_l * rho20(abv_in)
    mass_out = vol_out * rho20(abv_out)
    return (mass_out - mass_in) / rho20(0)   # litres of water at 20 C
```

63.5% वर साधारण 0.901 kg/L आणि 40% वर 0.948 kg/L density असताना उत्तर साधारण 605 litres पाणी येते, 587.5 नव्हे. हरवलेले 17 litres म्हणजे contraction.

0.4% ला महत्त्व आहे का? EU नियमांनुसार spirit strength साठी label tolerance 0.3% vol आहे, आणि duty alcohol वर भरली जाते. जास्त strength म्हणजे spirit फुकट देणे. दुसऱ्या बाजूने चुकणे त्याहून वाईट: UK आणि EU मध्ये 40% खालील whisky whisky म्हणून विकताच येत नाही. म्हणूनच खरी reductions टप्प्याटप्प्याने, demineralised पाण्याने केली जातात, आणि कोणत्याही गणितावर, ते कितीही चांगले असो, विश्वास न ठेवता density meter ने strength मोजून पूर्ण केली जातात.

## cask selection हा linear programme आहे

vatting साठी casks निवडणे म्हणजे साध्या वेशातील optimisation समस्या. एक सोपी आवृत्ती:

- **निर्णय:** प्रत्येक पात्र cask मधून किती litres absolute alcohol काढायचे.
- **उद्दिष्ट:** stock चे एकूण मूल्य सर्वात कमी वापरणे, म्हणजे सर्वात मौल्यवान जुने casks जिथे त्यांचे महत्त्व आहे तिथे राखून ठेवता येतात.
- **constraints:** एकूण alcohol लक्ष्य; प्रत्येक cask मधील उपलब्ध alcohol; weighted averages म्हणून sensory targets (उदाहरणार्थ, vatting भर किमान 6 चा sherry character score); आणि वयाचा नियम.

linear programming solver (SciPy, OR-Tools, किंवा तुमच्या planning tool मधील) हे milliseconds मध्ये तंतोतंत सोडवतो. उदाहरणादाखल, 12 वर्षांचा A cask (प्रति LAA मूल्य 1.0, sherry 3), 14 वर्षांचा B (1.3, sherry 7) आणि 18 वर्षांचा C (2.0, sherry 8) असताना, 6 sherry score सह 300 LAA चे सर्वात स्वस्त vatting A मधून 94 LAA, B मधून सगळे 130 आणि C मधून 76 घेते, आणि stock मूल्य 415 येते.

## age statement हा नियम आहे, सरासरी नाही

आता cask D जोडा: 10 वर्षांचा, सुंदर sherry character (score 9), प्रति LAA 0.8 ला स्वस्त. solver ला तो वापरू द्या आणि खर्च 302.5 वर येतो, म्हणजे एक-चतुर्थांश कमी. तो D पूर्ण घेतो आणि जुन्या stock मधून खूपच कमी.

पण 12 वर्षांच्या label साठी हे बेकायदेशीरही आहे. Scotch Whisky Regulations आणि EU नियमांनुसार age statement म्हणजे bottle मधील सर्वात तरुण whisky चे वय. ती वयांची सरासरी नाही, ती कशीही weighted असो. सरासरी वय काढून ते 12 शी तपासणारे tool हे vatting आनंदाने मंजूर करेल.

संभाषणात language model नेमका असाच domain नियम चुकवते, आणि solver तो तेव्हाच बरोबर करतो जेव्हा कोणीतरी तो encode करतो. म्हणून वयाचा नियम गणितातील constraint नाही. तो कोणत्या casks ना समस्येत प्रवेशच मिळतो यावरील filter आहे, solver चालण्याआधीच code मध्ये लावलेला.

## LLM कुठे बसते

गणिते tools मध्ये असताना language model ला उपयुक्त आणि सुरक्षित काम मिळते:

1. **मागणीचे inputs मध्ये रूपांतर.** "गेल्या वर्षीच्या 12 सारखे काहीतरी, थोडे जास्त sherry, 300 LAA, 25 वर्षांच्या casks ना हात लावू नका" हे लक्ष्य, constraints आणि वगळायच्या यादीत बदलते. काहीही चालवण्याआधी assistant inputs पुष्टीसाठी परत दाखवतो.
2. **tools call करणे.** vatting साठी `select_casks`, reduction साठी `reduction_water`, आणि blender एखाद्या विशिष्ट cask बद्दल विचारेल त्यासाठी inventory मधून `cask_history`.
3. **निकाल समजावणे.** cask B पूर्ण का वापरला (sherry score वाढवण्याचा तो सर्वात स्वस्त मार्ग आहे), D का वगळला (वय), आणि sherry लक्ष्य 5 वर आले तर काय बदलेल.
4. **स्वतः कधीच आकडा तयार न करणे.** स्पष्टीकरणातील प्रत्येक आकडा tool output मधून येतो. blender ने tools उत्तर देऊ शकत नाहीत असा संख्यात्मक प्रश्न विचारला, तर assistant तसे सांगतो.

निर्णय घेणारा blender च राहतो, आणि अंतिम चाचणी नाकाचीच राहते. sensory आणि chemical डेटावरून house style जुळवणे [blending consistency पोस्ट]({{ '/2024/ai-whiskey-blending-consistency/' | relative_url }}) मध्ये आहे. ही पोस्ट याची खात्री करण्याबद्दल आहे की त्याभोवतीचे गणित कधीच कमकुवत दुवा ठरत नाही.

## हे कुठे मोडते

**sensory scores रेषीय नसतात.** solver vatting च्या sherry score ला त्याच्या casks ची weighted average मानतो. flavour नेहमी इतक्या सभ्यपणे मिसळत नाही: एक आक्रमक cask त्याच्या वाट्याच्या कितीतरी पलीकडे वर्चस्व गाजवू शकतो. optimum ला अंतिम blend नव्हे तर sample vatting साठीची सुरुवातीची रेसिपी माना.

**density tables अधिकृतच असाव्यात.** वरील रेखाटन `rho20` इतकेच चांगले आहे. duty आणि labelling साठी अधिकृत alcoholometric tables (OIML R22 किंवा तुमच्या प्राधिकरणाचे समतुल्य) आणि calibrated instrument वापरा, कोणीतरी टाइप केलेला अंदाज नव्हे.

**वेगवेगळ्या strengths मिसळतानाही थोडे आकुंचन होते.** वेगवेगळ्या strength च्या दोन spirits मिसळल्यावरही थोडे आकुंचन होते, म्हणून vatting चे volume casks च्या बेरजेइतके तंतोतंत नसते. सारख्या strength च्या casks साठी परिणाम छोटा असतो, पण alcohol मध्ये काम करा आणि निकाल मोजा.

**stock मूल्ये हा धोरणात्मक निर्णय आहे.** stock मूल्य कमीत कमी ठेवणे म्हणजे कोणते casks सर्वात महत्त्वाचे याबद्दलचा दृष्टिकोन encode करणे. तो दृष्टिकोन maturing inventory ज्यांच्या मालकीची आहे त्यांच्याकडून घ्या, आणि त्यांना तो बदलू द्या.

## निष्कर्ष

language model blending च्या प्रश्नाचे उत्तर अस्खलित, आत्मविश्वासू वाक्यांत देईल, रसायनशास्त्र किंवा कायदा मोडणाऱ्या वाक्यांसकट. त्याला बेरजांपासून दूर ठेवा. cask selection solver मध्ये ठेवा, age statement कठोर filter म्हणून. reduction density tables वापरणाऱ्या आणि mass conserve करणाऱ्या code मध्ये ठेवा. मग model ला ते करू द्या ज्यात ते खरोखर चांगले आहे: blender ला काय म्हणायचे होते ते समजणे, योग्य tools call करणे आणि उत्तर समजावणे. model आकडे पाहते. blender vatting चाखतो.

मालिकेतील पुढील आणि शेवटचा भाग: [distillery AI कुठे मोडते]({{ '/mr/2026/where-distillery-ai-breaks/' | relative_url }}). dashboard मधील blending च्या sensory बाजूसाठी पाहा [whisky blending आणि sensory dashboard]({{ '/2023/tableau-whisky-blending-sensory-dashboard/' | relative_url }}). संपूर्ण यादी [The Still and the Model मालिकेच्या पानावर]({{ '/series/still-and-model/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**whisky मध्ये किती पाणी घालायचे हे फक्त volumes वजा करून का काढता येत नाही?**
कारण ethanol आणि पाणी मिसळल्यावर आकुंचन पावतात. 63.5% वरील 1,000 litres 40% पर्यंत आणायला साधारण 605 litres पाणी लागते, साध्या volume गणिताने सुचवलेले 587.5 litres नव्हे, आणि फक्त 587.5 litres घातल्यास spirit साधारण 40.4% वर राहते. योग्य पद्धत 20 degrees C वरील density tables वापरून mass मध्ये काम करते, आणि मग मोजमापाने खात्री करते.

**LLM whisky blend साठी casks निवडू शकते का?**
त्याने ते थेट निवडू नयेत. cask selection ही volume, sensory targets आणि सर्वात तरुण whisky चे वय यासारख्या कठोर constraints असलेली optimisation समस्या आहे, आणि linear programming solver ती तंतोतंत हाताळतो. LLM चे काम म्हणजे blender ची मागणी solver inputs मध्ये बदलणे, solver call करणे आणि निकाल समजावणे.

**whisky blend मध्ये age statement कसे काम करते?**
Scotch whisky मध्ये आणि EU नियमांनुसार label वरील वय म्हणजे bottle मधील सर्वात तरुण whisky चे वय. ती सरासरी नाही. blending tool ने दाव्यापेक्षा तरुण प्रत्येक cask वगळलाच पाहिजे, त्याची किंमत किंवा flavour कितीही आकर्षक असो, आणि optimiser ने तो कठोर नियम म्हणून लागू करायला हवा.
