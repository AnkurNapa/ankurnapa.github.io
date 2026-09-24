---
layout: post
lang: mr
title: "data engineering म्हणून cask inventory: SCD2 positions, regauge events आणि काढलेला आकडा म्हणून angel's share"
image: /assets/og/cask-inventory-data-engineering-scd2.png
description: "The Still and the Model चा भाग 4. cask warehouse मध्ये बारा किंवा अधिक वर्षे राहतो, हलवला जातो, sample केला जातो, regauge होतो, आणि दर वर्षी spirit गमावतो. त्याचे attributes slowly changing dimensions म्हणून, त्याचे आयुष्य events म्हणून, आणि angel's share गणित म्हणून model करा, म्हणजे कोणत्याही तारखेला कोणत्याही cask बद्दलच्या कोणत्याही प्रश्नाला एकच उत्तर असेल."
date: 2026-08-06 09:00:00 -0700
updated: 2026-08-06
permalink: /mr/2026/cask-inventory-data-engineering-scd2/
tags: [distilling-maturation, still-and-model, data-engineering, data-modeling, generative-ai]
faq:
  - q: "SCD2 table म्हणजे काय आणि casks साठी ते का वापरावे?"
    a: "type 2 slowly changing dimension नोंद overwrite करण्याऐवजी तिची प्रत्येक आवृत्ती ती ज्या तारखांना वैध होती त्यांसह ठेवते. casks साठी याचा अर्थ cask ची आजवरची प्रत्येक warehouse position, मालक आणि status त्यांच्या तारखांसह table मध्ये राहतात. March 2019 मध्ये cask कुठे होता असे विचारून तुम्हाला उत्तर मिळू शकते, आणि microclimate analysis, audits आणि ग्राहकांच्या प्रश्नांसाठी हे महत्त्वाचे आहे."
  - q: "cask inventory मध्ये angel's share कसा काढावा?"
    a: "काढलेला आकडा म्हणून, साठवलेला कधीच नाही. भरतानाचे litres of absolute alcohol घ्या, त्यातून शेवटच्या regauge मधील alcohol आणि नोंदवलेले samples किंवा withdrawals वजा करा, आणि जे उरते तो loss. field म्हणून साठवलेला angel's share शिळा होतो आणि sampling लपवतो. events वरून काढलेला तो नेहमी अद्ययावत आणि स्पष्टीकरण देता येण्याजोगा असतो."
  - q: "GenAI assistant maturing stock बद्दलच्या प्रश्नांची उत्तरे देऊ शकतो का?"
    a: "हो, जर तो raw tables ऐवजी governed queries मार्फत उत्तर देत असेल. त्याला event आणि SCD2 tables वर आधारित cask_history, position_on आणि alcohol_balance सारखे tools द्या, आणि दिलेल्या fill मधील कोणत्या casks नी नेहमीपेक्षा जास्त गमावले यासारख्या प्रश्नांची तो उत्तरे देऊ शकतो, प्रत्येक आकडा query मधून येत."
---

**थोडक्यात उत्तर: whisky cask warehouse मध्ये बारा किंवा अधिक वर्षे बसू शकतो, आणि त्या काळात तो हलतो, sample होतो, regauge होतो आणि शांतपणे spirit हवेत गमावतो. inventory फक्त cask ची सध्याची position आणि सध्याचे volume साठवत असेल, तर तो बहुतेक इतिहास नाहीसा होतो. हळूहळू बदलणारे attributes (position, मालक, status) type 2 slowly changing dimension म्हणून model करा, cask च्या बाबतीत जे काही घडते ते event म्हणून नोंदवा, आणि angel's share साठवण्याऐवजी events वरून काढा. मग "हा cask 2019 मध्ये कुठे होता?" आणि "त्याने प्रत्यक्षात किती गमावले?" या प्रत्येकाला एकच उत्तर असते, आणि GenAI assistant अंदाज न लावता ती देऊ शकतो.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एका cask ची उदाहरणादाखल बारा वर्षांची timeline. 2014 मध्ये warehouse 1 मध्ये 63.5 टक्क्यांवर 250 litres भरला, म्हणजे 158.75 litres absolute alcohol. 2016 मध्ये warehouse 3 मध्ये हलवला. 2019 मध्ये sample केला. 2020 मध्ये regauge केला. 2022 मध्ये पुन्हा हलवला. 2026 मध्ये 205 litres आणि 60.8 टक्क्यांवर regauge, म्हणजे 124.64 litres absolute alcohol. angel's share साधारण 34 litres absolute alcohol असा काढला जातो, म्हणजे वर्षाला साधारण 2 टक्के.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एक CASK, बारा वर्षांचे EVENTS (उदाहरणादाखल)</text>
<g font-family="sans-serif">
<line x1="70" y1="150" x2="930" y2="150" stroke="#4db6a2" stroke-width="3"/>
<circle cx="70" cy="150" r="9" fill="#06483f"/>
<text x="70" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2014 fill</text>
<text x="70" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">63.5% वर 250 L</text>
<text x="70" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">158.75 LAA</text>
<circle cx="213" cy="150" r="7" fill="#4db6a2"/>
<text x="213" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2016 move</text>
<text x="213" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W1 ते W3</text>
<circle cx="427" cy="150" r="7" fill="#4db6a2"/>
<text x="427" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2019 sample</text>
<text x="427" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">नोंदवलेला draw</text>
<circle cx="498" cy="150" r="7" fill="#4db6a2"/>
<text x="518" y="100" text-anchor="middle" font-size="11.5" fill="#06483f">2020 regauge</text>
<circle cx="643" cy="150" r="7" fill="#4db6a2"/>
<text x="643" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2022 move</text>
<text x="643" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W3 ते W5</text>
<circle cx="930" cy="150" r="9" fill="#06483f"/>
<text x="915" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2026 regauge</text>
<text x="915" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">60.8% वर 205 L</text>
<text x="915" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">124.64 LAA</text>
<rect x="250" y="222" width="500" height="44" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="500" y="249" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081">काढलेला loss साधारण 34 LAA, वर्षाला साधारण 2%</text>
<rect x="40" y="282" width="920" height="36" rx="10" fill="#06483f"/>
<text x="500" y="305" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">ANGEL'S SHARE म्हणजे EVENTS वरील QUERY, कोणी UPDATE करतो असा FIELD नव्हे</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरणादाखल cask. litres of absolute alcohol (LAA) म्हणजे bulk litres गुणिले strength. संपूर्ण balance मध्ये 2019 च्या draw सारखे samples कशालाही angel's share म्हणण्याआधी वजा केले जातात.</figcaption>
</figure>

warehouse manager ला cask 14-0387 कुठे आहे असे विचारा, आणि तो काही सेकंदांत सांगेल. 2019 च्या उन्हाळ्यात तो कुठे होता असे विचारा, जेव्हा त्या fill मधील काही casks मध्ये अनपेक्षित note आली होती, आणि उत्तरात सहसा कागदी ledger, निवृत्त सहकारी आणि भरपूर सद्भावना यांचा समावेश असतो.

[या मालिकेतील मागील पोस्ट्स]({{ '/mr/2026/llm-copilot-still-operator/' | relative_url }}) still house च्या floor वर होत्या. ही पोस्ट warehouse मध्ये जाते, जिथे कालमान तासांऐवजी वर्षांचे असते, आणि जिथे इतिहास टिकतो की नाही हे data model ठरवते.

## बदलाचे दोन प्रकार

cask दोन वेगळ्या प्रकारे बदलतो, आणि त्यांना दोन वेगळ्या रचना लागतात.

**कधीमधी बदलणारे attributes:** warehouse, bay आणि tier; मालक (ग्राहकांसाठी ठेवलेल्या casks साठी); status (maturing, earmarked, disgorged); re-rack नंतरचा cask प्रकार. ही cask बद्दलची तथ्ये आहेत जी काही काळ टिकतात, मग बदलतात.

**त्याच्या बाबतीत घडणाऱ्या गोष्टी:** भरणे, हलवणे, sampling, regauging, topping up, नव्या cask मध्ये re-rack, disgorging. हे तारीख, प्रमाण आणि व्यक्ती असलेले events आहेत.

बहुतेक cask systems पहिला प्रकार सध्याच्या values म्हणून साठवतात आणि दुसरा, फार तर, comments field म्हणून. दोन्हीमुळे इतिहास हरवतो.

## SCD2: प्रत्येक आवृत्ती, तिच्या तारखांसह

type 2 slowly changing dimension attribute ला overwrite करण्याऐवजी त्याची प्रत्येक आवृत्ती ठेवते. प्रत्येक row मध्ये ती कधी खरी झाली आणि कधी थांबली याची तारीख असते:

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

ती एक query 2019 च्या प्रश्नाचे उत्तर देते. ती microclimate analysis सुद्धा शक्य करते: कालानुरूप positions warehouse तापमान आणि आर्द्रतेच्या logs शी join करा, आणि प्रत्येक cask ला त्याने प्रत्यक्ष अनुभवलेल्या हवामानाचा स्वतःचा इतिहास मिळतो, आणि [rackhouse microclimate पोस्ट]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) ला input म्हणून नेमके हेच हवे असते. SCD2 शिवाय प्रत्येक cask ने बारा वर्षे जिथे तो आज आहे तिथेच घालवली असे दिसते.

ते सांभाळणारा pipeline नेहमीचाच आहे: प्रत्येक वेळी move नोंदवली की सध्याची row बंद करा आणि नवी उघडा. dbt snapshots, Delta `MERGE` आणि Fabric pipelines हे सगळे काही ओळींच्या configuration ने करतात.

## events: cask चा स्वतःचा ledger

cask मधील सामग्री बदलणारी प्रत्येक गोष्ट event आहे, [wine cellar ledger]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) movements नोंदवतो त्याच पद्धतीने नोंदवलेली:

- **fill**: bulk litres, strength, LAA, spirit batch, cask प्रकार
- **sample**: काढलेले volume, हेतू
- **regauge**: bulk litres, strength, LAA, पद्धत (dip किंवा weight)
- **re-rack**: कोणत्या cask मधून, कोणत्या cask मध्ये, volume
- **disgorge**: vatting कडे बाहेर गेलेले volume आणि strength

regauges बद्दल एक टीप आवश्यक आहे. casks बहुतेकदा dip ऐवजी वजनाने gauge केले जातात: gross weight वजा cask चा tare, भागिले मोजलेल्या strength वरील density, म्हणजे bulk litres. हे गणित 20 degrees C वरील ethanol आणि पाण्याच्या density table वर, आणि भरताना नोंदवलेल्या tare weight वर अवलंबून असते. यापैकी एकही गहाळ किंवा चुकीचे असेल, तर त्या cask चे प्रत्येक regauge एकाच दिशेने चुकते. event वर फक्त निकालातील volume नव्हे तर gross weight, tare आणि strength साठवा, म्हणजे गणित तपासता आणि पुन्हा करता येईल.

## काढलेला आकडा म्हणून angel's share

events जागेवर आल्यावर angel's share कोणीतरी update करतो असा field राहत नाही आणि गणित बनतो:

> loss = भरतानाचे LAA - शेवटच्या regauge वरील LAA - samples आणि withdrawals मध्ये काढलेले LAA

वरील उदाहरणादाखल cask साठी: 63.5% वर 250 litres भरले, म्हणजे 158.75 LAA. बारा वर्षांनंतर तो 205 litres आणि 60.8% वर regauge होतो, म्हणजे 124.64 LAA. साधेपणासाठी 2019 चा छोटा sample बाजूला ठेवला, तर loss साधारण 34 LAA, म्हणजे बारा वर्षांत 21.5%, चक्रवाढीने वर्षाला साधारण 2%. थंड, दमट warehouse मधील Scotch साठी सहसा सांगितल्या जाणाऱ्या श्रेणीत हे आहे. उष्ण हवामानात कितीतरी जास्त loss होतो, आणि जिथे पाणी alcohol पेक्षा वेगाने उडते तिथे strength घसरण्याऐवजी वाढूही शकते.

दोन गोष्टी काढलेल्या आवृत्तीला साठवलेल्यापेक्षा चांगले बनवतात. ती नेहमी अद्ययावत असते: नवा regauge कोणालाही लक्षात ठेवावे न लागता ती update करतो. आणि ती samples बद्दल प्रामाणिक असते: blending team सतत ज्यातून काढत राहिली म्हणून तहानलेला वाटणारा cask त्याचे samples samples म्हणूनच दाखवतो, evaporation म्हणून नाही. [angel's share forecasting पोस्ट]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}) loss चे modelling मांडते. ज्या डेटावरून ते model करायला हवे तो हा आहे.

## वर GenAI assistant ठेवणे

SCD2 positions आणि cask event ledger असताना लोक प्रत्यक्ष विचारतात ते प्रश्न queries बनतात, आणि queries GenAI assistant साठी tools बनू शकतात:

- `cask_history(cask_id)`: प्रत्येक event आणि position, क्रमाने
- `position_on(cask_id, date)`: वरील SCD2 lookup
- `alcohol_balance(fill_batch)`: fill LAA, सध्याचे LAA, samples, प्रत्येक cask चा काढलेला loss

"May 2014 च्या fill मधील कोणत्या casks नी त्यांच्या शेजाऱ्यांपेक्षा जास्त गमावले?" असे विचारल्यावर assistant `alcohol_balance` call करतो, प्रत्येक cask ची त्याच्या fill आणि warehouse च्या median शी तुलना करतो, आणि outliers त्यांच्या कालानुरूप positions सह यादीत मांडतो. प्रत्येक आकडा query मधून येतो. model चे काम म्हणजे प्रश्न समजून घेणे, योग्य tools call करणे आणि उत्तर साध्या शब्दांत समजावणे. त्याने raw tables का पाहू नयेत याची मांडणी wine मालिकेतील [semantic layer पोस्ट]({{ '/mr/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) करते.

## हे कुठे मोडते

**बारा वर्षांचा इतिहास क्वचितच स्वच्छ सुरू होतो.** बहुतेक cask inventories चे पहिले दशक म्हणजे कागद, जुन्या systems आणि spreadsheets यांचे मिश्रण. जे शक्य आहे ते स्पष्ट स्रोतासह events म्हणून migrate करा, प्रत्येक cask च्या opening position पासून SCD2 सुरू करा, आणि migrate केलेला इतिहास नव्याइतकाच चांगला आहे असे भासवण्याऐवजी त्याला कमी confidence चा म्हणून खूण करा.

**regauges क्वचित आणि गोंगाटी असतात.** बारा वर्षांत दोनदा regauge झालेला cask त्याच्या loss साठी दोनच data points देतो. casks मधील काही टक्क्यांचे फरक maturation नव्हे तर मोजमापामुळे असू शकतात.

**tare weights हरवतात.** नोंदवलेला tare नसलेल्या cask चे वजनाने कोणत्याही अचूकतेने regauge करता येत नाही. गहाळ tare ला data quality दोष माना आणि दहाव्या वर्षी नव्हे तर पहिल्याच दिवशी flag करा.

**duty नोंदी वेगळ्या असतात.** bonded warehouse च्या नोंदी excise प्राधिकरणाला उत्तरदायी असतात आणि त्यांचे स्वतःचे नियम असतात. analytic inventory ने त्यांच्याशी जुळायला हवे, त्यांची जागा घ्यायला नको.

## निष्कर्ष

cask म्हणजे बारा वर्षांची नोंद, आणि बहुतेक inventories फक्त तिचे शेवटचे पान ठेवतात. प्रत्येक position तिच्या तारखांसह ठेवा, प्रत्येक event त्याच्या प्रमाणांसह नोंदवा, आणि angel's share साठवण्याऐवजी काढा. मग हवामान, loss, sampling आणि audits बद्दलच्या महत्त्वाच्या प्रश्नांना प्रत्येकी एकच उत्तर असते, आणि GenAI assistant मनाने रचण्याऐवजी governed tools मार्फत ते शोधू शकतो. spirit धीर धरते. data model नेही धरायला हवा.

मालिकेतील पुढील भाग: [गणित code मध्ये करणारा GenAI blending assistant]({{ '/mr/2026/genai-whisky-blending-assistant-lp/' | relative_url }}). कोणते casks वापरायचे हे निवडण्यासाठी पाहा [AI for Cask Selection and Maturing-Stock Inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}). संपूर्ण यादी [The Still and the Model मालिकेच्या पानावर]({{ '/series/still-and-model/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**SCD2 table म्हणजे काय आणि casks साठी ते का वापरावे?**
type 2 slowly changing dimension नोंद overwrite करण्याऐवजी तिची प्रत्येक आवृत्ती ती ज्या तारखांना वैध होती त्यांसह ठेवते. casks साठी याचा अर्थ cask ची आजवरची प्रत्येक warehouse position, मालक आणि status त्यांच्या तारखांसह table मध्ये राहतात. March 2019 मध्ये cask कुठे होता असे विचारून तुम्हाला उत्तर मिळू शकते, आणि microclimate analysis, audits आणि ग्राहकांच्या प्रश्नांसाठी हे महत्त्वाचे आहे.

**cask inventory मध्ये angel's share कसा काढावा?**
काढलेला आकडा म्हणून, साठवलेला कधीच नाही. भरतानाचे litres of absolute alcohol घ्या, त्यातून शेवटच्या regauge मधील alcohol आणि नोंदवलेले samples किंवा withdrawals वजा करा, आणि जे उरते तो loss. field म्हणून साठवलेला angel's share शिळा होतो आणि sampling लपवतो. events वरून काढलेला तो नेहमी अद्ययावत आणि स्पष्टीकरण देता येण्याजोगा असतो.

**GenAI assistant maturing stock बद्दलच्या प्रश्नांची उत्तरे देऊ शकतो का?**
हो, जर तो raw tables ऐवजी governed queries मार्फत उत्तर देत असेल. त्याला event आणि SCD2 tables वर आधारित cask_history, position_on आणि alcohol_balance सारखे tools द्या, आणि दिलेल्या fill मधील कोणत्या casks नी नेहमीपेक्षा जास्त गमावले यासारख्या प्रश्नांची तो उत्तरे देऊ शकतो, प्रत्येक आकडा query मधून येत.
