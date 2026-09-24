---
layout: post
lang: mr
title: "Cellar चे event-sourcing: वायनरीतील volumes साठवू नयेत, ते नेहमी काढले जावेत"
image: /assets/og/event-sourced-cellar-records-winery.png
description: "The Cellar Ledger चा भाग 2. tank volume हा editable field असतो तेव्हा losses कोणत्याही कारणाशिवाय गायब होतात. lakehouse मधील append-only movement ledger प्रत्येक balance ला गणित बनवतो, AI agent ला समजावून सांगण्यासाठी खरी provenance देतो, आणि agent ला सत्य कधीही overwrite करू देत नाही."
date: 2026-06-27 09:00:00 -0700
updated: 2026-06-27
permalink: /mr/2026/event-sourced-cellar-records-winery/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, data-modeling]
faq:
  - q: "वायनरीच्या data model मध्ये event sourcing म्हणजे काय?"
    a: "प्रत्येक tank चे volume लोक edit करतात असा field म्हणून साठवण्याऐवजी, तुम्ही प्रत्येक हालचाल बदलता न येणारा event म्हणून साठवता: receipt, transfer, topping, racking, blend, filtration, bottling, sample, loss. कोणत्याही क्षणी कोणत्याही vessel मधील volume म्हणजे त्या क्षणापर्यंतच्या events ची बेरीज. काहीही overwrite होत नाही, म्हणून प्रत्येक litre ला इतिहास असतो."
  - q: "book volume शी न जुळणारे dip reading कसे हाताळावे?"
    a: "dip ला नवे volume म्हणून नव्हे तर observation म्हणून नोंदवा. ते काढलेल्या balance पेक्षा वेगळे असेल, तर तो फरक स्वतःचा adjustment event बनतो, ज्याला evaporation, न नोंदवलेले topping किंवा meter error असे कारण देणे बंधनकारक असते. book ची दुरुस्ती event ने होते, edit ने कधीच नाही, त्यामुळे तफावत दिसत राहते आणि तिचे स्पष्टीकरण देता येते."
  - q: "AI agent ला वायनरीची inventory update करू द्यावी का?"
    a: "त्याला प्रस्ताव देऊ द्यावा, लिहू देऊ नये. agent ला movement ledger वाचू द्या आणि त्याच्या तर्कासह movement किंवा adjustment चा मसुदा तयार करू द्या, मग तो append होण्याआधी एखाद्या व्यक्तीकडून मंजूर करून घ्या. ledger append-only असल्यामुळे मंजूर झालेली चूकसुद्धा reversing event ने दुरुस्त होते आणि कधीच नाहीशी होत नाही."
---

**थोडक्यात उत्तर: बहुतेक वायनरी systems मध्ये tank चे volume लोक edit करू शकतात असा आकडा म्हणून साठवले जाते. dip आणि book जुळले नाहीत की कोणीतरी नवा आकडा टाइप करतो, आणि फरक कोणत्याही कारणाशिवाय नाहीसा होतो. cellar चे event-sourcing म्हणजे प्रत्येक हालचाल append-only event म्हणून साठवणे आणि प्रत्येक balance त्यांच्यावरून काढणे. मग book स्वतःच स्वतःचे स्पष्टीकरण देते, GenAI agent ला अंदाज बांधण्याऐवजी तर्क करण्यासाठी खरा इतिहास मिळतो, आणि "agents प्रस्ताव देतात, माणसे मंजूर करतात" हा नियम लागू करणे सोपे होते कारण काहीही overwrite होऊ शकत नाही.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="tank 12 नोंदवण्याच्या दोन पद्धती. डावीकडे state table मध्ये एकच volume field आहे, जे कोणीतरी 4,980 वरून 4,920 litres केले, आणि 60 litres कोणत्याही कारणाशिवाय गेले. उजवीकडे movement ledger मध्ये events आहेत: 5,000 litres receive, barrel मधून 40 litres top, 2 litres sample, 58 litres lees rack out, dip observation 4,920 litres, आणि मग नोंदवलेल्या कारणासह उणे 60 litres चे gauge adjustment. balance म्हणजे events ची बेरीज.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TANK 12: साठवलेली STATE विरुद्ध काढलेली STATE</text>
<g font-family="sans-serif">
<text x="210" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">EDITABLE FIELD</text>
<rect x="40" y="72" width="340" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="210" y="106" text-anchor="middle" font-size="12" fill="#06483f">tank_12.volume_l</text>
<text x="210" y="140" text-anchor="middle" font-size="22" font-weight="700" fill="#06483f">4,980 &#8594; 4,920</text>
<text x="210" y="172" text-anchor="middle" font-size="11" fill="#ff4081">60 L गेले, कारण नाही, इतिहास नाही</text>
<text x="700" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">APPEND-ONLY MOVEMENT LEDGER</text>
<rect x="440" y="72" width="520" height="190" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<g font-size="11.5" fill="#06483f">
<text x="460" y="98">receive &#183; press 3 मधून</text><text x="940" y="98" text-anchor="end">+5,000</text>
<text x="460" y="122">top &#183; barrel B-17 मधून</text><text x="940" y="122" text-anchor="end">+40</text>
<text x="460" y="146">sample &#183; lab</text><text x="940" y="146" text-anchor="end">&#8722;2</text>
<text x="460" y="170">rack &#183; lees, lees tank मध्ये</text><text x="940" y="170" text-anchor="end">&#8722;58</text>
<text x="460" y="194" fill="#4a6b64">observe &#183; dip 4,920 दाखवतो (book 4,980)</text><text x="940" y="194" text-anchor="end" fill="#4a6b64">0</text>
<text x="460" y="218" fill="#00695c" font-weight="700">adjust &#183; कारण: tank 12 मधून barrel topping नोंदले नाही</text><text x="940" y="218" text-anchor="end" fill="#00695c" font-weight="700">&#8722;60</text>
</g>
<line x1="460" y1="232" x2="940" y2="232" stroke="#4db6a2" stroke-width="1"/>
<text x="460" y="252" font-size="12" font-weight="700" fill="#06483f">balance = events ची बेरीज</text><text x="940" y="252" text-anchor="end" font-size="12" font-weight="700" fill="#06483f">4,920</text>
<rect x="40" y="276" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="301" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">शेवटचा आकडा तोच &#183; का, हे त्यांपैकी एकच सांगू शकतो</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">दोन्ही books 4,920 litres वर संपतात. auditor ला, किंवा agent ला, उत्तर देऊ शकतो तो फक्त ledger.</figcaption>
</figure>

tank 12 मध्ये 4,980 litres असायला हवेत. cellar hand dip घेतो आणि 4,920 वाचतो. system मध्ये volume field आहे, म्हणून तो 4,920 टाइप करतो आणि सकाळचे काम पुढे चालू ठेवतो. धावपळीच्या दिवशी हे अगदी वाजवी आहे. पण याचा अर्थ असाही आहे की आता 60 litres wine वायनरीच्या नोंदींमधून कोणत्याही कारणाशिवाय, loss च्या तारखेशिवाय आणि नंतर शोधण्याच्या कोणत्याही मार्गाशिवाय बाहेर पडली.

हे शंभर vessels आणि एका harvest भरातील topping, racking आणि blending ने गुणा, आणि वर्षअखेरीस हरवलेल्या wine चा परिचित शोध सुरू होतो. [या मालिकेतील पहिली पोस्ट]({{ '/mr/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) कधीच व्याख्यित न झालेल्या metric बद्दल होती. ही पोस्ट अशा प्रमाणाबद्दल आहे ज्याला कधी इतिहास असूच दिला गेला नाही.

## साठवलेली state विरुद्ध काढलेली state

बहुतेक cellar software, आणि जवळजवळ प्रत्येक cellar spreadsheet, **state** साठवते: प्रत्येक vessel मधील सध्याचे volume. हालचाली होतात, आणि कोणीतरी त्यानुसार state update करतो. हालचाल स्वतः एकतर दुसरीकडे नोंदवली जाते किंवा अजिबात नाही.

event sourcing हे उलटे करते. तुम्ही **हालचाली** साठवता, आणि volume कधीच साठवत नाही. cellar मधील प्रत्येक बदल हा event असतो:

- receive (press, truck किंवा दुसऱ्या site वरून)
- transfer आणि blend (vessel ते vessel, lot composition सह)
- top, rack, filter, fine
- sample आणि lab वापर
- bottle (finished goods कडे बाहेर)
- observe (dip किंवा gauge reading, जे स्वतःहून काहीच बदलत नाही)
- adjust (observed आणि काढलेल्या आकड्यातील फरक, बंधनकारक कारणासह)

कोणत्याही क्षणी कोणत्याही vessel मधील volume ही एक query आहे: त्या वेळेपर्यंतच्या प्रत्येक event ची बेरीज. कोणी ते edit करत नाही कारण edit करण्यासारखे काही उरतच नाही.

```sql
SELECT vessel_id,
       SUM(signed_volume_l_20c) AS volume_l
FROM   cellar_movements
WHERE  event_ts <= :as_of
GROUP  BY vessel_id;
```

`:as_of` बदला आणि गेल्या पाच वर्षांतील कोणत्याही दिवसाच्या शेवटची cellar तुमच्या हातात. प्रत्येक excise return, प्रत्येक audit आणि प्रत्येक "Grenache कुठे गेली" संभाषणाला खरे तर हीच query हवी असते.

## सर्वांना अडकवणारा तपशील: litres, पण कोणत्या तापमानाला?

वरच्या column चे नाव पाहा: 20 degrees C ला litres. wine गरम झाल्यावर प्रसरण पावते, साधारण प्रति degree 0.02 ते 0.03 टक्के. 10 degrees ला आणि पुन्हा 20 degrees ला वाचलेल्या 5,000 litre tank मध्ये कोणतीही wine कुठेही न जाता साधारण 10 ते 15 litres चा फरक पडतो.

साठवलेल्या state च्या system मध्ये हा फरक वसंताच्या पहिल्या उबदार आठवड्यात गूढ loss किंवा gain म्हणून समोर येतो. event model मध्ये प्रत्येक observation सोबत त्याचे तापमान असते, pipeline book शी तुलना करण्याआधी ते reference तापमानावर दुरुस्त करतो, आणि तापमानामुळे होणारी हलचाल कधीच adjustment बनत नाही. ही छोटी गोष्ट आहे. पण अशाच गोष्टीमुळे cellar master पहिल्याच महिन्यात system वरचा विश्वास गमावतो.

## lakehouse मध्ये हे बांधणे

यासाठी कोणत्याही विलक्षण tooling ची गरज नाही. तुम्ही आधीच चालवत असलेल्या कोणत्याही lakehouse मधील append-only table (Fabric किंवा Databricks मध्ये Delta, Snowflake मध्ये Iceberg) हे काम करते. काही नियम त्याला प्रामाणिक ठेवतात:

1. **फक्त append, आणि ते लागू केलेले.** movement table वर insert ची परवानगी द्या, पण update किंवा delete ची नाही. दुरुस्त्या म्हणजे reversing events: चुकीचा plus 500 रद्द करण्यासाठी minus 500, मग बरोबर event. चूक दिसत राहते, आणि मुद्दा तोच आहे.
2. **adjustments वर कारण बंधनकारक.** data contract रिकाम्या कारणाचा adjust event नाकारतो. "Unknown" चालते. रिकामे नाही.
3. **शक्य असल्यास source वरच capture करा.** वायनरी system आधीच अस्तित्वात असेल, तर change data capture (Debezium, Fabric mirroring किंवा vendor चा स्वतःचा feed) त्याच्या updates चे events करू शकतो, त्यामुळे harvest च्या काळात cellar ला नवे app शिकायला सांगावे लागत नाही.
4. **snapshot वेगासाठी, सत्यासाठी कधीच नाही.** dashboards साठी रात्रीचे balance table ठीक आहे. ते events वरून पुन्हा बांधले जाते आणि कधीच edit होत नाही.

lakehouse time travel कधी कधी शॉर्टकट म्हणून सुचवले जाते. ते तेच नाही. time travel table कसे दिसत होते ते दाखवते. event ledger cellar मध्ये काय घडले ते सांगतो. का, याचे उत्तर फक्त दुसरा देतो.

## GenAI साठी हे का महत्त्वाचे आहे

इथे जुन्या पद्धतीचे data model नव्या पद्धतीच्या tools ची किंमत चुकवते.

**agent फक्त जे नोंदवले गेले त्याचेच स्पष्टीकरण देऊ शकतो.** GenAI assistant ला विचारा "tank 12 मध्ये 60 litres कमी का आहेत?" साठवलेल्या state च्या system मध्ये त्याच्याकडे दोन volume snapshots असतात आणि मधे काहीच नाही, म्हणून तो एकतर माहीत नाही असे म्हणतो किंवा, त्याहून वाईट, evaporation बद्दल पटण्यासारखी कहाणी रचतो. movement ledger वर तो events वाचतो, adjustment शोधतो आणि operator व timestamp सह कारण उद्धृत करतो. तेच model, तोच prompt. फरक पूर्णपणे डेटामध्ये आहे.

**agents नी प्रस्ताव द्यावा, कधीच लिहू नये.** पुढचे स्पष्ट पाऊल म्हणजे agent ला data entry करू देणे: cellar work order वाचून movements नोंदवणे. हे उपयुक्त आहे आणि थोडे भीतीदायकही. append-only रचनेमुळे हे करून पाहणे सुरक्षित होते. agent त्याच्या तर्कासह ("work order 4417 म्हणतो tank 12 मधून B-17 top करा, 40 L") events चा मसुदा pending table मध्ये ठेवतो. एखादी व्यक्ती ते मंजूर करते, आणि तेव्हाच ते append होतात. मंजूर event चुकीचा निघाला तर तो इतर कोणत्याही event सारखा reverse होतो. agent जे काही करतो त्याने book शांतपणे overwrite होऊ शकत नाही.

**tool calls सोपे होतात.** तुम्ही cellar छोट्या tools च्या संचातून agent समोर ठेवलात, तर event model तुम्हाला ते नेमके कोणते हे सांगते: `balance(vessel, as_of)`, `history(vessel, from, to)`, `propose_movement(...)`. `set_volume` नाही. नसलेले tool हेच safety feature आहे.

## हे कुठे मोडते

**नोंद जितकी पूर्ण तितकाच तो पूर्ण.** धावपळीच्या आठवड्यातील topping whiteboard वर गेले आणि system मध्ये कधीच आले नाही, तर ledger प्रत्येक वेळी adjustment दाखवेल. तरीही ते शांततेपेक्षा चांगले, कारण adjustment ची कारणे नोंद करण्याची सवय कुठे कमकुवत आहे ते सांगतात, पण ती हरवलेले events तयार करत नाहीत.

**flow meters आणि dips जुळत नाहीत.** flow meter ने मोजलेला transfer आणि दोन्ही vessels dip करून मोजलेला तोच transfer अगदी तंतोतंत जुळणार नाहीत. कोणत्या प्रकारच्या movement साठी कोणते reference आहे ते ठरवा आणि दुसरे observation म्हणून नोंदवा.

**harvest म्हणजे गोंधळ.** crush च्या काळात events उशिरा आणि क्रमाबाहेर येतात. model ला event time सोबतच नोंदवलेल्या entry time सह मागच्या तारखेचे events स्वीकारावे लागतात, नाहीतर cellar November पर्यंत तो वापरणेच बंद करेल.

**migration फुकट नाही.** साठवलेल्या state च्या system मधून बाहेर पडणे म्हणजे प्रत्येक vessel साठी opening balance event पासून सुरुवात. त्या तारखेपूर्वीचा इतिहास नेहमीसारखाच अस्पष्ट राहतो.

## निष्कर्ष

तुम्ही edit करू शकता असे volume आपली कहाणी गमावू शकते. हालचालींवरून काढलेले volume ती जपते. event ledger ही जुनी कल्पना आहे (accountants शतकानुशतके असेच हिशेब ठेवत आले आहेत), आणि GenAI agent ला नेमके हेच हवे असते: स्पष्टीकरणासाठी खरी provenance, आणि भूतकाळ पुन्हा लिहिण्याविरुद्ध भक्कम भिंत. wine नेहमीच हलत होती. data model ने फक्त ते मान्य करायचे आहे.

मालिकेतील पुढील भाग: [loss map]({{ '/mr/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}), जिथे हे events crush ते bottle असा waterfall बनतात आणि LLM variance note चा मसुदा लिहिते. हे events पुरवणाऱ्या sensors साठी पाहा [IoT in the Winery]({{ '/2026/iot-in-the-winery-sensors-process/' | relative_url }}). संपूर्ण यादी [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**वायनरीच्या data model मध्ये event sourcing म्हणजे काय?**
प्रत्येक tank चे volume लोक edit करतात असा field म्हणून साठवण्याऐवजी, तुम्ही प्रत्येक हालचाल बदलता न येणारा event म्हणून साठवता: receipt, transfer, topping, racking, blend, filtration, bottling, sample, loss. कोणत्याही क्षणी कोणत्याही vessel मधील volume म्हणजे त्या क्षणापर्यंतच्या events ची बेरीज. काहीही overwrite होत नाही, म्हणून प्रत्येक litre ला इतिहास असतो.

**book volume शी न जुळणारे dip reading कसे हाताळावे?**
dip ला नवे volume म्हणून नव्हे तर observation म्हणून नोंदवा. ते काढलेल्या balance पेक्षा वेगळे असेल, तर तो फरक स्वतःचा adjustment event बनतो, ज्याला evaporation, न नोंदवलेले topping किंवा meter error असे कारण देणे बंधनकारक असते. book ची दुरुस्ती event ने होते, edit ने कधीच नाही, त्यामुळे तफावत दिसत राहते आणि तिचे स्पष्टीकरण देता येते.

**AI agent ला वायनरीची inventory update करू द्यावी का?**
त्याला प्रस्ताव देऊ द्यावा, लिहू देऊ नये. agent ला movement ledger वाचू द्या आणि त्याच्या तर्कासह movement किंवा adjustment चा मसुदा तयार करू द्या, मग तो append होण्याआधी एखाद्या व्यक्तीकडून मंजूर करून घ्या. ledger append-only असल्यामुळे मंजूर झालेली चूकसुद्धा reversing event ने दुरुस्त होते आणि कधीच नाहीशी होत नाही.
