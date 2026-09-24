---
layout: post
lang: mr
title: "चॅटबॉटला alcohol विचारले, तीन उत्तरे मिळाली: GenAI ला semantic layer लागतो"
image: /assets/og/genai-winery-semantic-layer-potential-alcohol.png
description: "The Cellar Ledger चा भाग 1. वायनरीत potential alcohol विचारल्यावर chat-with-your-data assistant तीन वेगवेगळे आकडे देतो, कारण हे रूपांतर तीन spreadsheets मध्ये राहते. text-to-SQL agents अव्याख्यित metrics ची गडबड का वाढवतात, आणि governed semantic layer, instrument ओळखणाऱ्या pipelines आणि एक छोटा eval set ती कशी दूर करतात."
date: 2026-06-22 09:00:00 -0700
updated: 2026-06-22
permalink: /mr/2026/genai-winery-semantic-layer-potential-alcohol/
tags: [winemaking, cellar-ledger, generative-ai, data-engineering, semantic-layer]
faq:
  - q: "chat-with-your-data assistant एकाच प्रश्नाला वेगवेगळी उत्तरे का देतो?"
    a: "सहसा कारण असे की ते metric assistant ला दिसेल अशा कुठल्याही ठिकाणी व्याख्यित केलेले नसते. text-to-SQL agent जे columns पटण्यासारखे दिसतात त्यांच्यावर query लिहितो. potential alcohol तीन workbooks मध्ये तीन वेगवेगळ्या factors ने काढले जात असेल, तर agent एक निवडतो, आणि थोडा वेगळा prompt दुसरा निवडतो. उपाय म्हणजे metric एकदाच governed semantic layer मध्ये व्याख्यित करणे आणि assistant ला raw tables कडे नव्हे तर त्याकडे वळवणे."
  - q: "वायनरीने semantic layer मध्ये सर्वात आधी काय ठेवावे?"
    a: "ज्या आकड्यांवर लोक वाद घालतात ते: potential alcohol, residual sugar, हातातील volume, loss, आणि प्रति टन yield. प्रत्येकाला एक व्याख्या, sugar-to-alcohol yield figure सारखे स्पष्ट लिहिलेले parameters, आणि एक नावाने ठरलेला मालक. GenAI assistant ला हेच प्रश्न सर्वाधिक विचारले जाणार, म्हणून चुकीचे उत्तर इथेच सर्वात जास्त नुकसान करते."
  - q: "winemaker वापरण्याआधी GenAI data assistant ची चाचणी कशी घ्यावी?"
    a: "cellar प्रत्यक्ष विचारते असे साधारण वीस खरे प्रश्न लिहा, ज्यांची उत्तरे एखाद्या व्यक्तीने हाताने तपासली आहेत, आणि model, prompt किंवा semantic model बदलेल तेव्हा प्रत्येक वेळी ते चालवा. आकड्यांवर exact match ने गुण द्या. हा छोटा evaluation set आहे, आणि बहुतेक regressions winemaker च्या आधी तोच पकडतो."
---

**थोडक्यात उत्तर: governed metric layer शिवाय तुम्ही वायनरीच्या डेटावर GenAI assistant बसवलात, तर "Shiraz lots वर potential alcohol किती?" या प्रश्नाचे उत्तर तो तुमच्या तीन लपलेल्या conversion factors पैकी जो त्याला आधी सापडेल त्याने देईल. 24 Brix ला हे factors alcohol च्या 1.7 points ने वेगळे पडतात, जे label tolerance पेक्षा जास्त आहे. समस्या model ची नाही. समस्या अव्याख्यित metric ची आहे. potential alcohol एकदाच, त्याचे parameters उघडपणे मांडून व्याख्यित करा, pipeline असा बांधा की प्रत्येक reading सोबत त्याचे instrument राहील, assistant ला raw tables ऐवजी semantic layer कडे वळवा, आणि cellar प्रत्यक्ष विचारते अशा वीस प्रश्नांवर त्याची चाचणी घ्या.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एकाच प्रश्नाचे दोन मार्ग. वरच्या मार्गावर GenAI assistant थेट तीन spreadsheets ना query करतो आणि 13.2, 14.2 आणि 14.9 टक्के potential alcohol देतो. खालच्या मार्गावर raw readings bronze table मध्ये जातात, मग instrument आणि fermentation phase जोडणाऱ्या silver table मध्ये, मग semantic layer मधील एकाच governed potential alcohol metric मध्ये, आणि assistant पद्धत नमूद करून 14.2 टक्के हे एकच उत्तर देतो.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एकच प्रश्न, दोन architectures</text>
<g font-family="sans-serif">
<text x="40" y="60" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">SEMANTIC LAYER शिवाय</text>
<rect x="40" y="72" width="170" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">GenAI assistant</text>
<text x="125" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">text-to-SQL</text>
<line x1="210" y1="102" x2="290" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="290" y="72" width="380" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="480" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">harvest.xlsx &#183; lab.xlsx &#183; labels.xlsx</text>
<text x="480" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">&#215;0.55, &#215;0.59, &#215;0.62 cells मध्ये दडलेले</text>
<line x1="670" y1="102" x2="740" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="72" width="220" height="60" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="850" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">13.2 / 14.2 / 14.9%</text>
<text x="850" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">prompt वर अवलंबून</text>
<text x="40" y="170" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">SEMANTIC LAYER सह</text>
<rect x="40" y="182" width="170" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">bronze</text>
<text x="125" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">raw readings, जशी घेतली तशी</text>
<line x1="210" y1="215" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="182" width="190" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">silver</text>
<text x="335" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">+ instrument, + ferment phase</text>
<line x1="430" y1="215" x2="460" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="460" y="182" width="220" height="66" rx="9" fill="#06483f"/>
<text x="570" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">semantic layer</text>
<text x="570" y="226" text-anchor="middle" font-size="10.5" fill="#cfe6df">एकच potential_alcohol, एकच मालक</text>
<line x1="680" y1="215" x2="740" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="182" width="220" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="850" y="208" text-anchor="middle" font-size="14" font-weight="700" fill="#2e9e7c">14.2%</text>
<text x="850" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">पद्धत आणि parameters नमूद</text>
<rect x="40" y="276" width="920" height="44" rx="10" fill="#06483f"/>
<text x="500" y="303" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">समस्या MODEL ची नाही &#183; अव्याख्यित METRIC ची आहे</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">spreadsheets कडे वळवलेल्या assistant ला जो factor आधी सापडतो तोच तो वापरतो. governed metric कडे वळवल्यावर त्याला एकच सापडू शकतो.</figcaption>
</figure>

एक winemaker नव्या data assistant मध्ये टाइप करतो: "Shiraz lots वर potential alcohol किती आहे?" दोन सेकंदांत नीटनेटक्या table सह उत्तर येते. assistant बरोबर आहे, या अर्थाने की तो आकडा कुठेतरी अस्तित्वात आहे. तो चूकही आहे, कारण lab च्या workbook ने वेगळे काही सांगितले असते, आणि label artwork च्या फाईलने आणखी वेगळे.

त्या इमारतीत कोणीही चूक केली नाही. कोणीतरी वर्षांपूर्वी एका cell मध्ये conversion factor टाइप केला, तो cell पुढच्या vintage च्या workbook मध्ये copy झाला, आणि आता एकाच metric च्या तीन आवृत्त्या तीन फाईल्समध्ये राहतात. कोणत्या फाईलवर विश्वास ठेवायचा हे माणसाला माहीत असते. text-to-SQL agent ला नाही. **The Cellar Ledger** मधील ही पहिली पोस्ट आहे. ही मालिका वायनरीच्या आकड्यांखाली असलेल्या data engineering आणि GenAI कामावर आहे, आणि तिची सुरुवात अशा आकड्याने होते जो सगळे वापरतात पण कोणीही व्याख्यित केलेला नाही.

## GenAI जुनी समस्या अधिक मोठ्याने का मांडतो

2026 मध्ये बाजारातील प्रत्येक chat-with-your-data product साधारण एकाच पद्धतीने काम करते. तुम्ही इंग्रजीत प्रश्न विचारता. assistant तुमच्या डेटाचे काहीतरी वर्णन वाचतो, query लिहितो, ती चालवतो आणि निकालाचा सारांश देतो. Power BI Copilot, Databricks AI/BI Genie आणि Snowflake Cortex Analyst तिघेही हाच नमुना पाळतात, आणि तुम्ही semantic model किंवा निवडक सूचनांचा संच दिलात तर तिघेही आधी तो वाचतात.

तुम्ही तो दिला नाहीत, तर ते tables वाचतात. आणि `pot_alc` नावाचा column model ला हे अजिबात सांगत नाही की तो कोणत्या factor ने तयार झाला.

मग एकाच वेळी दोन गोष्टी बिघडतात:

- **उत्तर अस्थिर असते.** प्रश्न थोडा वेगळ्या शब्दांत विचारा आणि agent वेगळे table join करू शकतो, वेगळा column निवडू शकतो आणि त्याच आत्मविश्वासाच्या सुरात वेगळा आकडा देऊ शकतो.
- **उत्तर अधिकृत वाटते.** चुकीचा आकडा असलेले spreadsheet spreadsheet सारखेच दिसते. चुकीचा आकडा देणारा chatbot म्हणजे system असे वाटते. लोक spreadsheets तपासतात. chatbot ला मात्र बहुतेक तपासत नाहीत.

जुनी समस्या अशी होती की तीन माणसे तीन आकड्यांवरून काम करत. नवी समस्या अशी आहे की prompt ज्या आकड्यापर्यंत योगायोगाने पोहोचतो तोच assistant प्रत्येक व्यक्तीला पाठवतो.

## खालचे metric: रूपांतर खरे काय आहे

potential alcohol एकदाच व्याख्यित करायचे तर ढोबळ नियम काय लपवतात हे माहीत असायला हवे. Brix गुणिले 0.55, 0.59 किंवा 0.62 हा चार टप्प्यांच्या गणिताचा शॉर्टकट आहे, आणि प्रत्येक टप्पा हा असा parameter आहे ज्याचा कोणीतरी मालक असायला हवा.

**1. Brix ते density.** Degrees Brix म्हणजे 100 grams द्रावणातील sucrose चे grams, वजन प्रति वजन. sucrose द्रावणांसाठीचे एक प्रमाणित polynomial 24 Brix ला साधारण 1.101 specific gravity देते.

**2. प्रति litre विरघळलेले घन पदार्थ.** Brix गुणिले SG गुणिले 10. आपल्या must साठी साधारण 264 g/L.

**3. जे साखर नाही ते वजा करा.** द्राक्षाचा must म्हणजे glucose आणि fructose, सोबत acids, minerals आणि phenolics. पिकलेल्या फळात साखर नसलेले घन पदार्थ साधारणपणे 20 ते 30 g/L च्या आसपास असतात. 25 धरा, म्हणजे साधारण 239 g/L fermentable sugar उरते.

**4. साखर ते alcohol.** सिद्धांतानुसार glucose चा एक रेणू ethanol चे दोन आणि CO2 चे दोन रेणू देतो, म्हणजे साधारण 15.4 g/L साखरेपासून 1% alcohol by volume होते. खरे yeast पेशी बांधते, glycerol तयार करते आणि वायूसोबत थोडे ethanol गमावते, म्हणून व्यवहारातील आकडे जास्त असतात. EU प्रति 1% vol साठी 16.83 g/L वापरतो. 239 भागिले 16.83 म्हणजे 14.2%.

function म्हणून लिहिले तर हे सगळे छोटेसे आहे:

```python
def potential_alcohol(brix, non_sugar_gl=25.0, yield_gl_per_pct=16.83):
    sg = 1 + brix / (258.6 - (brix / 258.2) * 227.1)
    sugar_gl = brix * sg * 10 - non_sugar_gl
    return sugar_gl / yield_gl_per_pct
```

मुद्दा code चा नाही. मुद्दा असा आहे की `non_sugar_gl` आणि `yield_gl_per_pct` यांना आता नाव आहे, ते दिसतात आणि त्यांचा मालक आहे. शॉर्टकट factors हे दोन्ही लपवतात, म्हणूनच ते एकमेकांशी जुळत नाहीत.

हे महत्त्वाचे आहे कारण tolerances एका-एका point मध्ये मोजल्या जातात. US मध्ये 14% किंवा त्याखालील wine सत्याच्या 1.5 points आत label करता येते, आणि 14% वरील wine 1 point आत, आणि label 14% ची रेषा ओलांडू शकत नाही कारण तिथे excise दर बदलतो. इमारतीभर 1.7 points चा फरक म्हणजे ज्या tolerance आत राहायचे आहे त्यापेक्षा मोठा.

## data engineering उपाय: instrument ओळखणारे layers

metric व्याख्यित करणे हा अर्धा भाग आहे. उरलेला अर्धा भाग म्हणजे inputs चा अर्थ तोच आहे याची खात्री करणे जो metric गृहीत धरते. बऱ्याच वायनरींचा डेटा कोणतेही AI जवळ येण्याआधीच इथे मोडतो.

vineyard मध्ये refractometer ठीक आहे. fermentation सुरू झाले की alcohol refractive index वाढवते, म्हणून refractometer उरलेली साखर जास्त दाखवतो, आणि wine जितकी कोरडी होते तितके हे जास्त. hydrometer density मोजतो, आणि ethanol पाण्यापेक्षा हलके असते, म्हणून कोरडी red wine साधारण उणे 1 ते उणे 2 Brix दाखवते. दोन्ही readings त्या instrument ने जे मोजले त्याचे बरोबर reading आहेत. pipeline त्यांना `brix` नावाच्या एकाच column मध्ये साठवतो त्या क्षणी दोन्ही चुकीची ठरतात.

एक साधा medallion layout कोणत्याही धाडसाशिवाय हे हाताळतो:

- **Bronze** प्रत्येक reading जसे घेतले तसेच ठेवते: value, unit, instrument, कोणी, कधी, कोणती tank. काहीही रूपांतरित होत नाही आणि काहीही टाकून दिले जात नाही.
- **Silver** pipeline ला काढता येईल असा संदर्भ जोडते: tank च्या स्वतःच्या events वरून fermentation phase (pre-inoculation, active, dry), आणि inoculation नंतर घेतलेल्या प्रत्येक refractometer reading वर flag. fermentation मधील hydrometer readings ना त्यांचे खरे नाव, density, दिले जाते आणि ते negative जाऊ दिले जातात.
- **Gold आणि semantic layer** मध्ये governed metrics राहतात. `potential_alcohol` फक्त pre-inoculation sugar readings वाचते. तयार lot ला lab कडून मोजलेले alcohol मिळाले की वेगळे `alcohol_measured` ताबा घेते आणि त्या lot साठी prediction निवृत्त होते.

bronze table वर असा data contract ठेवा जो instrument नसलेले reading नाकारेल. ही validation ची एक ओळ आहे, आणि हीच ओळ पुढच्या vintage ची संदिग्धता board report मध्ये नव्हे तर दारातच थांबवते.

## assistant ला योग्य layer कडे वळवणे

metric व्याख्यित झाल्यावर GenAI भाग खूपच कमी रोमांचक होतो, आणि तुम्हाला तेच हवे आहे. तीन settings बहुतेक काम करतात:

1. **assistant ला semantic model पुरते मर्यादित ठेवा.** त्याला raw tables अजिबात देऊ नका. त्याला `potential_alcohol` फक्त measure म्हणून दिसत असेल, तर तो चौथी आवृत्ती शोधून काढू शकत नाही.
2. **सूचना cellar manual सारख्या लिहा.** यातील बहुतेक tools साध्या मजकुरातील सूचना स्वीकारतात. model ला अंदाज लावता येणार नाहीत अशा domain facts साठी त्या वापरा: "inoculation नंतरचे Brix म्हणजे density, साखर नाही", "तयार lot चे alcohol `alcohol_measured` मधून येते", "volumes 20 degrees C ला litres मध्ये आहेत".
3. **पद्धत नमूद करायला लावा.** प्रत्येक उत्तराखाली metric चे नाव आणि त्याचे parameters मागा. ज्या winemaker ला "potential alcohol, EU yield 16.83 g/L, non-sugar 25 g/L" दिसते तो आकड्याशी नव्हे तर गृहीतकाशी वाद घालू शकतो.

## वीस प्रश्नांचा eval set

शेवटचा टप्पा म्हणजे जो teams वगळतात. कोणीही assistant वर अवलंबून राहण्याआधी, cellar प्रत्यक्ष विचारते असे साधारण वीस प्रश्न लिहा, ज्यांची उत्तरे कोणीतरी हाताने तपासली आहेत. "lot 24-SH-03 वर potential alcohol." "कोणत्या tanks अजून 5 Brix वर आहेत?" "गेल्या वर्षीच्या Viognier चे मोजलेले alcohol." model, prompt किंवा semantic model बदलेल तेव्हा प्रत्येक वेळी हा संच चालवा आणि आकड्यांच्या exact match वर गुण द्या.

ही छोटी फाईल आहे. "आपण chatbot वर विश्वास ठेवू शकतो का?" या प्रश्नाचे हेच एकमेव प्रामाणिक उत्तर आहे. तुम्ही त्यावर विश्वास ठेवत नाही. तुम्ही त्याची चाचणी घेता, जसे lab नवे instrument वापरात आणण्याआधी reference शी तपासते.

आणि यातून मिळणारा बोनस असा. प्रत्येक तयार lot तुम्हाला एक जोडी देतो: सुरुवातीची साखर आणि मोजलेले alcohol. variety नुसार अशा जोड्यांच्या काही vintages मधून तुम्ही तुमच्या फळाला, तुमच्या yeast ला आणि तुमच्या cellar ला साजेसा स्वतःचा yield figure fit करू शकता. इमारतीतील पहिले खरोखर उपयुक्त model तेच आहे, आणि ते अस्तित्वात आहे कारण pipeline ने दोन्ही आकडे जपून ठेवले.

## हे कुठे मोडते

**non-sugar अंदाज अजूनही अंदाजच आहे.** तो variety, पिकण्याचे प्रमाण, सड आणि press fraction सोबत बदलतो. लपवलेल्या default पेक्षा स्पष्ट लिहिलेला default चांगला, पण दर वर्षी काही musts वर तो मोजा आणि तात्पुरता समजा.

**semantic layer वाईट sampling दुरुस्त करत नाही.** एका ओळीच्या उन्हाळ्या टोकाचा रस संपूर्ण block चे वर्णन करत नाही. कोणतीही metric व्याख्या ती बादली दुरुस्त करत नाही.

**सूचना हळूहळू बदलतात.** assistant ला दिलेले साध्या मजकुरातील मार्गदर्शन हे configuration आहे. त्याचे version ठेवा, बदलांचा आढावा घ्या, आणि ते बदलल्यावर eval set पुन्हा चालवा, नाहीतर ते शांतपणे चौथे spreadsheet बनते.

**नियम बाजारानुसार बदलतात.** वरील US tolerance आकडे मला सर्वाधिक माहीत आहेत. त्यांच्यावर labelling check बांधण्याआधी तुम्ही ज्या बाजारात विकता तिथले नियम तपासा.

## निष्कर्ष

chatbot ने तीन उत्तरे दिली कारण वायनरीकडे तीन उत्तरे होती. GenAI ने ती समस्या निर्माण केली नाही. त्याने फक्त ती लपवणे थांबवले. metric एकदाच, त्याचे parameters उघडपणे मांडून व्याख्यित करा, प्रत्येक reading त्याच्या instrument सह ठेवा, assistant ला फक्त governed layer दिसू द्या, आणि त्याला तपासलेल्या प्रश्नांच्या छोट्या संचावर जोखा. मग दोन सेकंदांचे उत्तर घेण्यासारखे ठरते.

वायनरी dashboards cellar चा विश्वास का गमावतात याच्या व्यापक मांडणीसाठी पाहा [Why Power BI Dashboards Die in Wineries]({{ '/2026/why-power-bi-dashboards-fail-wineries/' | relative_url }}). स्वच्छ fermentation curve वरून model काय करू शकते ते [AI for Wine Fermentation Control]({{ '/2024/ai-wine-fermentation-control/' | relative_url }}) मध्ये आहे. या मालिकेतील पुढील भाग: [cellar चे event-sourcing]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}), म्हणजे volumes जुळवून आणणारे data model. संपूर्ण यादी [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**chat-with-your-data assistant एकाच प्रश्नाला वेगवेगळी उत्तरे का देतो?**
सहसा कारण असे की ते metric assistant ला दिसेल अशा कुठल्याही ठिकाणी व्याख्यित केलेले नसते. text-to-SQL agent जे columns पटण्यासारखे दिसतात त्यांच्यावर query लिहितो. potential alcohol तीन workbooks मध्ये तीन वेगवेगळ्या factors ने काढले जात असेल, तर agent एक निवडतो, आणि थोडा वेगळा prompt दुसरा निवडतो. उपाय म्हणजे metric एकदाच governed semantic layer मध्ये व्याख्यित करणे आणि assistant ला raw tables कडे नव्हे तर त्याकडे वळवणे.

**वायनरीने semantic layer मध्ये सर्वात आधी काय ठेवावे?**
ज्या आकड्यांवर लोक वाद घालतात ते: potential alcohol, residual sugar, हातातील volume, loss, आणि प्रति टन yield. प्रत्येकाला एक व्याख्या, sugar-to-alcohol yield figure सारखे स्पष्ट लिहिलेले parameters, आणि एक नावाने ठरलेला मालक. GenAI assistant ला हेच प्रश्न सर्वाधिक विचारले जाणार, म्हणून चुकीचे उत्तर इथेच सर्वात जास्त नुकसान करते.

**winemaker वापरण्याआधी GenAI data assistant ची चाचणी कशी घ्यावी?**
cellar प्रत्यक्ष विचारते असे साधारण वीस खरे प्रश्न लिहा, ज्यांची उत्तरे एखाद्या व्यक्तीने हाताने तपासली आहेत, आणि model, prompt किंवा semantic model बदलेल तेव्हा प्रत्येक वेळी ते चालवा. आकड्यांवर exact match ने गुण द्या. हा छोटा evaluation set आहे, आणि बहुतेक regressions winemaker च्या आधी तोच पकडतो.
