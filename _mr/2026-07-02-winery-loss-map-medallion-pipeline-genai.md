---
layout: post
lang: mr
title: "Loss Map: medallion pipeline, anomaly flags आणि variance note चा मसुदा लिहिणारे LLM"
image: /assets/og/winery-loss-map-medallion-pipeline-genai.png
description: "The Cellar Ledger चा भाग 3. प्रत्येक वायनरी crush आणि bottle दरम्यान wine गमावते. movement ledger वर bronze, silver आणि gold pipeline म्हणून loss map बांधा, robust statistics ने असामान्य टप्पे flag करा, आणि LLM ला एकही गणित न करता मासिक variance note चा मसुदा लिहू द्या."
date: 2026-07-02 09:00:00 -0700
updated: 2026-07-02
permalink: /mr/2026/winery-loss-map-medallion-pipeline-genai/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, anomaly-detection]
faq:
  - q: "crush आणि bottle दरम्यान वायनरी किती wine गमावते?"
    a: "हे style, press पद्धत, barrel मधील वेळ आणि cellar मधील आर्द्रता यानुसार खूप बदलते, म्हणून कोणताही एक आकडा सावधपणे घ्या. अधिक उपयुक्त आकडा तुमचा स्वतःचा आहे: नोंदवलेल्या movements वरून काढलेला प्रत्येक lot चा प्रत्येक टप्प्यावरील loss, आणि त्यानंतर उरणारा unexplained residual. पाठलाग करण्यासारखा भाग तो residual आहे."
  - q: "वायनरीच्या loss डेटासाठी कोणते anomaly detection चालते?"
    a: "इथे साध्या, robust statistics सहसा गुंतागुंतीच्या models पेक्षा सरस ठरतात. प्रत्येक lot चा एखाद्या टप्प्यावरील loss rate त्याच टप्प्याच्या आणि त्याच vessel प्रकाराच्या median शी, median absolute deviation ने scale करून तुलना करा, आणि outliers flag करा. deep model साठी पुरेसा डेटा क्वचितच असतो, आणि robust z-score cellar master हाताने सहज तपासू शकतो."
  - q: "LLM मासिक loss variance report लिहू शकते का?"
    a: "ते मसुदा लिहू शकते, पण एकच अट: ते कधीच गणित करत नाही. आकडे SQL मध्ये काढा, निकाल आणि नोंदवलेली adjustment कारणे model ला द्या, आणि त्या ठरलेल्या आकड्यांभोवती त्याला टिप्पणी लिहू द्या. एखादी व्यक्ती आढावा घेऊन सही करते. table आणि वीस reason codes वाचनीय परिच्छेदांत बदलण्यात model चांगले आहे, आणि गणितात वाईट."
---

**थोडक्यात उत्तर: 100 टन red फळ crush करणारी वायनरी कदाचित 72,000 litres press करेल आणि 63,500 bottle करेल. मधले 8,500 litres बहुतेक ज्ञात losses असतात: lees, racking, evaporation, filtration, bottling. महत्त्वाचा भाग म्हणजे यांचा हिशेब लावल्यानंतर जे उरते ते, म्हणजे unexplained residual. movement ledger वर medallion pipeline म्हणून loss map बांधा, भारी model ऐवजी robust statistics ने असामान्य टप्पे flag करा, आणि query results वरून LLM ला variance note चा मसुदा लिहू द्या. शब्द model लिहिते. बेरजा SQL करते.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="100 टन red vintage साठी उदाहरणादाखल waterfall chart. सुरुवात 72,000 litres pressed पासून, मग gross lees 2,900 litres, racking 1,100, barrel evaporation 2,000, topping आणि samples 400, filtration 700, bottling 500 अशी घट, आणि गुलाबी रंगात ठळक केलेला 900 litres चा unexplained residual, शेवट 63,500 litres bottled. उभा अक्ष 60,000 litres पासून सुरू होतो.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">LOSS MAP: 100 टन RED, CRUSH ते BOTTLE (उदाहरणादाखल)</text>
<g font-family="sans-serif">
<line x1="60" y1="260" x2="960" y2="260" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">अक्ष 60,000 L पासून सुरू</text>
<rect x="70" y="70" width="64" height="190" fill="#06483f"/>
<text x="102" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">72,000</text>
<rect x="170" y="70" width="64" height="45.9" fill="#4db6a2"/>
<text x="202" y="130" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2,900</text>
<rect x="270" y="115.9" width="64" height="17.4" fill="#4db6a2"/>
<text x="302" y="148" text-anchor="middle" font-size="11" fill="#06483f">&#8722;1,100</text>
<rect x="370" y="133.3" width="64" height="31.7" fill="#4db6a2"/>
<text x="402" y="180" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2,000</text>
<rect x="470" y="165" width="64" height="6.3" fill="#4db6a2"/>
<text x="502" y="186" text-anchor="middle" font-size="11" fill="#06483f">&#8722;400</text>
<rect x="570" y="171.3" width="64" height="11.1" fill="#4db6a2"/>
<text x="602" y="197" text-anchor="middle" font-size="11" fill="#06483f">&#8722;700</text>
<rect x="670" y="182.4" width="64" height="7.9" fill="#4db6a2"/>
<text x="702" y="205" text-anchor="middle" font-size="11" fill="#06483f">&#8722;500</text>
<rect x="770" y="190.3" width="64" height="14.3" fill="#ff4081"/>
<text x="802" y="220" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">&#8722;900</text>
<rect x="870" y="204.6" width="64" height="55.4" fill="#06483f"/>
<text x="902" y="198" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">63,500</text>
<g font-size="10" fill="#4a6b64" text-anchor="middle">
<text x="102" y="278">pressed</text>
<text x="202" y="278">gross lees</text>
<text x="302" y="278">racking</text>
<text x="402" y="278">barrel</text><text x="402" y="291">evaporation</text>
<text x="502" y="278">topping</text><text x="502" y="291">&amp; samples</text>
<text x="602" y="278">filtration</text>
<text x="702" y="278">bottling</text>
<text x="802" y="278" fill="#ff4081" font-weight="700">अस्पष्ट</text>
<text x="902" y="278">bottled</text>
</g>
<rect x="40" y="304" width="920" height="30" rx="8" fill="#06483f"/>
<text x="500" y="324" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">7,600 L ज्ञात LOSS &#183; 900 L ज्याचे कोणीही स्पष्टीकरण देऊ शकत नाही &#183; गुलाबी BAR चा पाठलाग करा</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">हे उदाहरणादाखल आकडे आहेत, benchmarks नाहीत. तुमच्या स्वतःच्या ledger मधील तुमचे स्वतःचे टप्पे, एवढेच आकडे महत्त्वाचे.</figcaption>
</figure>

प्रत्येक vintage च्या शेवटी कोणीतरी तोच प्रश्न विचारतो: आपण इतके press केले, तितके bottle केले, बाकीचे कुठे गेले? प्रामाणिक उत्तर सहसा खांदे उडवत दिले जाते: "lees, evaporation आणि बऱ्याच छोट्या गोष्टी". त्या खांदे उडवण्यामागे दोन अगदी वेगळ्या प्रकारचे loss लपलेले असतात. बहुतेक भाग wine बनवण्याचा सामान्य खर्च असतो. एक छोटा तुकडा अशी wine असते जिचा वायनरी हिशेब देऊ शकत नाही, आणि पैसा, excise चे प्रश्न आणि प्रक्रियेतील समस्या नेमक्या त्याच तुकड्यात राहतात.

[मागील पोस्ट]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) ने movement ledger बांधला. ही पोस्ट त्याचे loss map करते, anomaly detection चा हलका थर जोडते, आणि मासिक लेखन आखूड दोरीवर LLM च्या हाती देते.

## ज्ञात loss विरुद्ध अस्पष्ट loss

काही loss म्हणजे वायनरीने नोंदवलेल्या कारणासह स्वतःहून सोडलेली wine:

- fermentation आणि पहिल्या racking नंतरचे **gross lees**, बहुतेकदा volume च्या काही टक्के.
- wine गाळावरून हलवली जाते तेव्हा प्रत्येक वेळी होणारे **racking losses**.
- **barrel evaporation**, जे cellar मधील आर्द्रता आणि तापमानावर मोठ्या प्रमाणात अवलंबून असते, आणि वर्षाला काही टक्के असते.
- **topping आणि samples**, छोटे पण सततचे.
- **filtration आणि bottling**, म्हणजे hoses, filters आणि filler bowl मधील dead volume.

बाकी सर्व म्हणजे residual: inputs, वजा outputs, वजा प्रत्येक नोंदवलेला loss. वरील उदाहरणादाखल vintage मध्ये 7,600 litres loss ला कारण आहे आणि 900 litres ला नाही. नऊशे litres तयार red म्हणजे हजारपेक्षा जास्त bottles. त्यासाठी एक दुपार खर्च करणे योग्य आहे.

residual कधीच शून्य नसतो. meters जुळत नाहीत, dips मध्ये त्रुटी असते, तापमान volumes इकडेतिकडे हलवते. ध्येय शून्य नाही. ध्येय असा residual आहे जो इतका छोटा आणि स्थिर असेल की तो उसळी घेतो तेव्हा तुमच्या लक्षात येईल.

## pipeline: bronze, silver, gold

loss map ही analytics समस्या होण्याआधी data engineering समस्या आहे. medallion pattern तिला चांगला बसतो.

**Bronze** म्हणजे movement ledger स्वतः, जसा आहे तसा: प्रत्येक receive, transfer, rack, top, filter, bottle, observe आणि adjust event, volumes 20 degrees C वर दुरुस्त केलेले.

**Silver** प्रत्येक movement चे टप्पा आणि loss category मध्ये वर्गीकरण करते. 58 litres lees tank मध्ये पाठवणारा rack event "loss: gross lees, stage: post-ferment, lot 24-SH-03" बनतो. नंतर filter करून परत मिळवलेले lees recovery event म्हणून परत येतात, म्हणजे ते दोनदा loss म्हणून मोजले जात नाहीत. बहुतेक domain logic इथे राहते, आणि cellar master ने इथले नियम तपासावेत, कारण event type पासून loss category पर्यंतचे mapping म्हणजे प्रक्रियेबद्दलच्या मतांचा संच आहे.

**Gold** म्हणजे प्रत्येक lot, प्रत्येक टप्पा, प्रत्येक vintage साठी एक row: आत आलेले volume, बाहेर गेलेले volume, category नुसार ज्ञात loss, आणि residual. तोच waterfall, dashboard आणि, आपण पाहणार आहोत तसे, language model ला पुरवतो.

```sql
SELECT lot_id, stage,
       SUM(volume_in_l)  AS vol_in,
       SUM(volume_out_l) AS vol_out,
       SUM(known_loss_l) AS known_loss,
       SUM(volume_in_l) - SUM(volume_out_l) - SUM(known_loss_l) AS residual_l
FROM   silver_lot_stage_movements
GROUP  BY lot_id, stage;
```

ही एक query आहे. खरे कष्ट silver मध्ये आहेत, categories बरोबर करण्यात.

## anomaly flags: हेतुपुरस्सर कंटाळवाणी statistics

gold table तयार झाले की पुढची स्वाभाविक मागणी असते "समस्या शोधायला AI वापरा". deep model कडे धाव घेण्याचा मोह टाळा. वायनरीकडे वर्षाला कदाचित काही शे lots आणि स्वच्छ इतिहासाच्या मोजक्या vintages असतात. काहीही गुंतागुंतीचे train करायला एवढा डेटा पुरेसा नाही, आणि cellar master ला flag हाताने तपासता आला पाहिजे.

robust z-score हे काम करतो:

1. प्रत्येक टप्पा आणि vessel प्रकारासाठी (उदाहरणार्थ, 5,000 litre stainless मधून racking) सर्व lots मधील median loss rate घ्या.
2. rates किती पसरलेले आहेत ते median absolute deviation ने मोजा, जे एखाद्या टोकाच्या मूल्याने ओढले न जाता त्याकडे दुर्लक्ष करते.
3. ज्या lot चा loss rate median पासून साधारण तीन scaled deviations पेक्षा जास्त दूर आहे तो flag करा.

यामुळे racking मध्ये 4% गमावणारी ती एक tank flag होते जेव्हा तिच्या भावंडांनी 1.5% गमावले, आणि प्रत्येक tank ला लागू असलेल्या vintage-व्यापी बदलाकडे दुर्लक्ष होते. हे आकर्षक नाही. ते स्वतःचे स्पष्टीकरण एका वाक्यात देते, आणि ते जास्त महत्त्वाचे आहे.

barrel evaporation ला स्वतंत्र वागणूक हवी. ते barrel कुठे ठेवले आहे यावर अवलंबून असते, म्हणून तुम्ही नोंदवत असाल तर cellar zone आणि position नुसार गट करा. [rackhouse microclimate पोस्ट]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) हेच भौतिकशास्त्र whisky च्या बाजूने मांडते.

## LLM variance note चा मसुदा लिहिते

दर महिन्याला कोणीतरी operations review साठी एक-दोन परिच्छेद लिहितो: या महिन्याचा loss, तुलना कशी आहे, काय घडले. त्याला एक तास लागतो आणि ते कंटाळवाणे असते. language model साठी हे चांगले काम आहे, जोपर्यंत तुम्ही अशी रचना करता की त्याला आकडे चुकवताच येणार नाहीत.

चालणारा pattern:

1. **प्रत्येक गणित SQL करते.** gold table, महिन्या-दर-महिना बदल, flag झालेले lots, volume नुसार सर्वोच्च adjustment कारणे. model काहीही पाहण्याआधीच हे सगळे काढलेले असते.
2. **model ला निकाल structured input म्हणून मिळतात.** आकड्यांचा छोटा JSON block, flag झालेल्या lots ची यादी, आणि operators नी adjustment events वर टाइप केलेली मुक्त मजकुरातील कारणे.
3. **model ठरलेल्या आकड्यांभोवती गद्य लिहिते.** त्याला फक्त दिलेले आकडेच वापरायला आणि प्रत्येक दाव्यासाठी source row चे नाव द्यायला सांगा. त्याहूनही चांगले, त्याला placeholders सह note परत करायला लावा जे code JSON मधून भरतो, म्हणजे एकही आकडा model कधीच टाइप करत नाही.
4. **ते operators ची कारणे गटांत बांधते.** "topping not logged", "topped B-row, forgot", "topping, missed" असे म्हणणाऱ्या वीस adjustment notes एक ओळ बनतात: "residual चा बहुतेक भाग B row मधील न नोंदवलेल्या barrel topping कडे जातो". इथे model खरोखर आपली किंमत वसूल करते. ते गोंधळलेला मानवी मजकूर चांगला वाचते.
5. **एखादी व्यक्ती संपादन करून सही करते.** note winemaker च्या नावाने जाते, model च्या नाही.

तुम्ही जे करू नये ते म्हणजे model ला raw ledger देऊन या महिन्यात काय चुकले असे विचारणे. ते मनातल्या मनात columns ची बेरीज करेल, आणि आत्मविश्वासाने काही शे litres ने चुकेल.

## हे कुठे मोडते

**residual प्रत्येक मापन त्रुटी शोषून घेतो.** हळूहळू भरकटणारा flow meter अस्पष्ट loss म्हणून दिसतो. चुकीच्या तापमानाला वाचलेली dip stick सुद्धा. residual ला हरवलेली wine समजण्याआधी instruments तपासा.

**silver नियम म्हणजे मते आहेत.** lees wine loss मानायची की परत मिळवता येणारे उपउत्पादन, यामुळे map बदलतो. नियम लिहून ठेवा आणि cellar master कडून मंजूर करून घ्या, नाहीतर दोन माणसे तोच waterfall दोन प्रकारे वाचतील.

**loss targets वर्तन बदलतात.** लोकांचे मूल्यमापन गुलाबी bar वर झाले, तर गुलाबी bar इतर काहीतरी म्हणून नोंदवला जाऊन लहान होईल. map प्रक्रियेतील समस्या शोधण्यासाठी वापरा, cellar crew ला गुण देण्यासाठी नाही.

**LLM शब्दांतून अजूनही दिशाभूल करू शकते.** आकडे ठरलेले असले तरी model सामान्य महिन्याला समस्या म्हणून मांडू शकते किंवा खऱ्या समस्येकडे दुर्लक्ष करू शकते. म्हणूनच flags statistics मधून येतात आणि model फक्त त्यांचे वर्णन करते.

## निष्कर्ष

प्रत्येक वायनरी wine गमावते. प्रश्न असा आहे की त्यातील किती loss कारणासह येतो. movement ledger वरचा pipeline ज्ञात loss आणि residual वेगळे करतो. robust statistics बदललेल्या टप्प्याकडे आणि lot कडे बोट दाखवतात. language model आकडे आणि cellar च्या स्वतःच्या notes वरून असा परिच्छेद तयार करते ज्यावर कोणीतरी आनंदाने सही करेल. या तीनपैकी एकही टप्पा विलक्षण नाही, आणि एकत्रितपणे ते vintage अखेरच्या खांदे उडवण्याला तपासायच्या tanks च्या छोट्या यादीत बदलतात.

मालिकेतील पुढील भाग: [graph म्हणून lot genealogy]({{ '/mr/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }}), जिथे तोच ledger "कोणत्या bottles मध्ये block 7 आहे?" याचे उत्तर देतो. Tableau मधील cellar आणि barrel view साठी पाहा [barrel-ageing dashboard]({{ '/2023/tableau-wine-cellar-barrel-ageing-dashboard/' | relative_url }}). संपूर्ण यादी [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**crush आणि bottle दरम्यान वायनरी किती wine गमावते?**
हे style, press पद्धत, barrel मधील वेळ आणि cellar मधील आर्द्रता यानुसार खूप बदलते, म्हणून कोणताही एक आकडा सावधपणे घ्या. अधिक उपयुक्त आकडा तुमचा स्वतःचा आहे: नोंदवलेल्या movements वरून काढलेला प्रत्येक lot चा प्रत्येक टप्प्यावरील loss, आणि त्यानंतर उरणारा unexplained residual. पाठलाग करण्यासारखा भाग तो residual आहे.

**वायनरीच्या loss डेटासाठी कोणते anomaly detection चालते?**
इथे साध्या, robust statistics सहसा गुंतागुंतीच्या models पेक्षा सरस ठरतात. प्रत्येक lot चा एखाद्या टप्प्यावरील loss rate त्याच टप्प्याच्या आणि त्याच vessel प्रकाराच्या median शी, median absolute deviation ने scale करून तुलना करा, आणि outliers flag करा. deep model साठी पुरेसा डेटा क्वचितच असतो, आणि robust z-score cellar master हाताने सहज तपासू शकतो.

**LLM मासिक loss variance report लिहू शकते का?**
ते मसुदा लिहू शकते, पण एकच अट: ते कधीच गणित करत नाही. आकडे SQL मध्ये काढा, निकाल आणि नोंदवलेली adjustment कारणे model ला द्या, आणि त्या ठरलेल्या आकड्यांभोवती त्याला टिप्पणी लिहू द्या. एखादी व्यक्ती आढावा घेऊन सही करते. table आणि वीस reason codes वाचनीय परिच्छेदांत बदलण्यात model चांगले आहे, आणि गणितात वाईट.
