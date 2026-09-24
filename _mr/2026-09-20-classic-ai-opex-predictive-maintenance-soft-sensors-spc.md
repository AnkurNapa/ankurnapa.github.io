---
layout: post
lang: mr
title: "OpEx साठी क्लासिक AI: SPC च्या वर predictive maintenance, soft sensors आणि anomaly detection"
image: /assets/og/classic-ai-opex-predictive-maintenance-soft-sensors-spc.png
description: "बेव्हरेज प्लांटमधील ऑपरेशनल एक्सलन्ससाठी AI, भाग 5. बेव्हरेज प्लांटमध्ये आधीच पैसा वाचवणारे machine learning: fillers आणि pasteurisers वर predictive maintenance, लाइनमध्ये मोजता न येणाऱ्या गोष्टींसाठी soft sensors, SPC वर बसवलेले multivariate anomaly detection, आणि योग्य baseline विरुद्ध प्रति hectolitre ऊर्जा व पाणी."
date: 2026-09-20 09:00:00 -0700
updated: 2026-09-20
permalink: /mr/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/
tags: [brewing-science, ai-opex, machine-learning, predictive-maintenance, operational-excellence]
faq:
  - q: "filler किंवा pasteuriser वर predictive maintenance साठी कोणता डेटा लागतो?"
    a: "मशीनचा condition डेटा, जसे की vibration, motor current, तापमान आणि दाब, historian मध्ये उपयुक्त वारंवारतेने साठवलेला, आणि CMMS मधील maintenance इतिहास ज्यात काय बिघडले आणि केव्हा हे नोंदलेले असते. बिघाडाच्या नोंदी नसतानाही असामान्य वर्तन ओळखता येते, पण बिघाड किती आधी येत आहे हे शिकता येत नाही."
  - q: "machine learning मुळे statistical process control ची गरज संपते का?"
    a: "नाही. fill volume किंवा PU सारख्या एकेका variable साठी SPC हाच सोपा, तपासता येणारा baseline राहतो. machine learning एक थर जोडते, अनेक signals मध्ये एकाच वेळी दिसणाऱ्या अशा patterns साठी जे कोणताही एक control chart दाखवत नाही. एखाद्या प्रश्नावर model SPC पेक्षा चांगले करू शकत नसेल, तर SPC च वापरा."
  - q: "प्रति hectolitre ऊर्जा आणि पाणी न्याय्य पद्धतीने कसे मोजायचे?"
    a: "प्रत्यक्ष वापराची तुलना अशा baseline शी करा जो वापर ठरवणारे घटक लक्षात घेतो: उत्पादित volume, product आणि pack mix, आणि बाहेरचे तापमान. energy management standards मध्ये वापरला जातो तसा साधा regression baseline दाखवतो की एखादा आठवडा खरोखर चांगला होता की फक्त गर्दीचा होता. प्रत्यक्ष आणि baseline यांमधील फरक हाच कृतीसाठीचा आकडा आहे."
---

**थोडक्यात उत्तर: generative AI येण्याआधीही बेव्हरेज प्लांटमध्ये स्वतःचा खर्च वसूल करणारे भरपूर machine learning होते, आणि ते आजही करते. Predictive maintenance fillers, pasteuriser pumps आणि conveyors वरचे vibration आणि current पाहते आणि बिघाडाच्या काही दिवस आधी इशारा देते. Soft sensors लाइनमध्ये मोजता न येणारी मूल्ये, मोजता येणाऱ्या मूल्यांवरून अंदाजतात. Multivariate anomaly detection डझनभर signals मधले असे patterns पकडते जे कोणताही एक control chart दाखवत नाही, आणि खाली baseline म्हणून SPC कायम राहतो. आणि प्रति hectolitre ऊर्जा व पाणी यांना अर्थ तेव्हाच येतो जेव्हा baseline ला माहीत असते की तुम्ही किती कामात होता. यातले काहीच नवीन नाही. हे सगळे मागच्या लेखातील डेटाच्या पायावर उभे आहे.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="बेव्हरेज प्लांटमधील क्लासिक AI चा थरांचा stack. तळाशी डेटाचे स्रोत: historian, MES stop log, CMMS आणि LIMS. त्यावर rules आणि SPC चा baseline थर: interlocks, PU गणना, fill volume वरचे control charts. त्यावर machine learning चा थर, चार उपयोगांसह: filler आणि pasteuriser वर predictive maintenance, soft sensors, multivariate anomaly detection, आणि ऊर्जा व पाण्याचे baselines. सर्वात वर माणसे कृती करतात: planners, operators आणि engineers. एक टीप सांगते की machine learning baseline थरात भर घालते, त्याची जागा कधीच घेत नाही.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">बेव्हरेज प्लांटमधील क्लासिक AI: BASELINE च्या वर ML</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="920" height="44" rx="9" fill="#06483f"/>
<text x="500" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">माणसे कृती करतात: planners, operators, engineers</text>
<rect x="40" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="150" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">predictive maintenance</text>
<text x="150" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">filler, pasteuriser, conveyors</text>
<rect x="273" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="383" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">soft sensors</text>
<text x="383" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">न मोजलेल्याचा अंदाज</text>
<rect x="506" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="616" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">multivariate anomalies</text>
<text x="616" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">एकाच वेळी अनेक signals</text>
<rect x="740" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="850" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">ऊर्जा &amp; पाणी</text>
<text x="850" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">प्रति hl, baseline विरुद्ध</text>
<rect x="40" y="188" width="920" height="50" rx="9" fill="#4db6a2"/>
<text x="500" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">BASELINE: rules आणि SPC</text>
<text x="500" y="228" text-anchor="middle" font-size="10.5" fill="#06483f">interlocks &#183; PU गणना &#183; fill volume आणि CO2 वरचे control charts</text>
<rect x="40" y="250" width="920" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="500" y="277" text-anchor="middle" font-size="11.5" fill="#06483f">डेटा: historian &#183; MES stop log &#183; CMMS &#183; LIMS</text>
<text x="500" y="318" text-anchor="middle" font-size="11" fill="#4a6b64">machine learning baseline च्या वर एक थर जोडते &#183; त्याची जागा कधीच घेत नाही</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">क्लासिक machine learning चे चार उपयोग, प्रत्येक rules, SPC आणि जोडलेल्या डेटावर उभा.</figcaption>
</figure>

2026 मध्ये लोक 'प्लांटमध्ये AI' ऐकतात, तेव्हा त्यांच्या डोळ्यासमोर chatbot येतो. गेल्या दशकभर बेव्हरेज प्लांटमध्ये पैसे वाचवणारे AI chatbot सारखे अजिबात दिसत नाही. ते म्हणजे pasteuriser pump वरचे vibration पाहणारे model, लॅबचे मूल्य वर्तवणारे regression, पहाटे 4 वाजता एखादा विचित्र pattern दाखवणारा chart. ते शांत, नेमके आणि मोजता येणारे आहे, आणि म्हणूनच ते काम करते.

या मालिकेतील हा पाचवा लेख आहे. [मागच्या लेखात]({{ '/mr/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}) OEE, सहा मोठे losses आणि डेटा कुठे राहतो हे मांडले. हा लेख [AI शिडीच्या]({{ '/mr/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}) machine learning पायरीवरील चार उपयोग पाहतो, जे नियमितपणे पैसा वसूल करतात.

## fillers आणि pasteurisers वर predictive maintenance

Breakdowns हा सहा मोठ्या losses पैकी पहिला आणि सहसा सर्वात त्रासदायक, कारण तो पूर्वसूचनेशिवाय आणि अनेकदा run च्या मध्येच येतो. Predictive maintenance ती पूर्वसूचना देण्याचा प्रयत्न करते.

डेटाच्या दोन बाजू आहेत:

- मशीनकडून **condition signals**: pump आणि motor bearings वरचे vibration, motor current, तापमान, दाब, cycle counts. tunnel pasteuriser वर circulation pumps, spray headers आणि heat exchangers हे नेहमीचे उमेदवार. filler वर main drive, vacuum pump आणि valves.
- CMMS मधून **बिघाडाचा इतिहास**: काय बिघडले, केव्हा, आणि काय केले.

दोन्ही असतील तर model शिकू शकते की मागच्या बिघाडांच्या आधीच्या दिवसांत signals कसे दिसत होते, आणि तोच pattern लवकर दाखवू शकते. बिघाडाचा इतिहास नसला तरी काहीतरी उपयुक्त करता येते: normal कसे दिसते ते शिका आणि त्यापासूनचा drift दाखवा. याला anomaly-based maintenance म्हणतात, आणि बहुतेक प्लांटनी इथूनच सुरुवात करावी, कारण स्वच्छ बिघाड-नोंदी दुर्मिळ असतात.

फायदा अंदाजात नाही. फायदा आहे अनियोजित breakdown ला नियोजित stop दरम्यानच्या नियोजित दुरुस्तीत बदलण्यात. packaging बाजूवर मी [Predictive Maintenance for Fillers and Seamers]({{ '/2024/predictive-maintenance-filler-seamer/' | relative_url }}) मध्ये अधिक खोलात लिहिले आहे.

## Soft sensors: लाइनमध्ये मोजता न येणाऱ्याचा अंदाज

Soft sensor थेट मोजायला अवघड किंवा सावकाश असलेल्या मूल्याचा अंदाज, सहज मोजता येणाऱ्या signals वरून करतो.

शिडी कुठून सुरू होते ते पाहणे उपयोगी आहे. Pasteurisation units ही गणना आहे, model नाही. नेहमीच्या पद्धतीनुसार 60 degrees C वर एक मिनिट म्हणजे 1 PU, आणि त्यावरचा प्रत्येक degree दर सुमारे 1.393 ने गुणतो. म्हणजे 62 degrees वर एक मिनिट सुमारे 1.94 PU देते, आणि तिथे दहा मिनिटे सुमारे 19.4. हे physics आणि एक rule आहे, सर्वात खालच्या पायरीवर, आणि ते तिथेच राहायला हवे.

machine learning ची आवृत्ती तिथे येते जिथे physics अपुरे पडते. महत्त्वाचा PU म्हणजे pack च्या आतल्या product ला मिळालेला PU. आपण मोजतो ते प्रत्येक zone मधील spray water चे तापमान. travelling temperature logger असलेल्या test runs च्या डेटावर प्रशिक्षित soft sensor आतल्या तापमानाचा, आणि म्हणून PU चा, अंदाज प्रत्येक pack साठी करू शकतो, फक्त test packs साठी नाही. अशाच कल्पना lab samples च्या दरम्यान dissolved CO2 किंवा oxygen pickup, किंवा gravity readings च्या दरम्यान fermentation मधील उरलेला extract अंदाजतात.

soft sensors चा नियम: ते अंदाज देतात, reference method खात्री करते. ते कुठे पाहायचे आणि केव्हा sample घ्यायचा हे सांगतात, काय release करायचे हे नाही.

## SPC च्या वर anomaly detection

मागच्या लेखातील SPC एका वेळी एक variable पाहण्यात उत्कृष्ट आहे: fill volume, crown crimp, PU. त्याचा आंधळा कोपरा म्हणजे असे patterns जे अनेक signals एकत्र पाहिल्यावरच दिसतात. थोडा जास्त filler bowl pressure, थोडे कमी product तापमान आणि थोडे वेगळे CO2 reading हे प्रत्येक आपापल्या control limits मध्ये असू शकतात, पण एकत्रितपणे बदललेली प्रक्रिया दाखवत असतात.

Multivariate anomaly detection ही पोकळी भरते. पद्धती जुन्या, प्रस्थापित पद्धतींपासून (Hotelling T squared chart सह principal component analysis, जी process industries मध्ये दशकानुदशके वापरली जाते) isolation forests किंवा autoencoders सारख्या नव्या पद्धतींपर्यंत आहेत. त्या अनेक signals मधील normal नाते शिकतात आणि ते तुटले की दाखवतात.

दोन व्यावहारिक नियम:

- **SPC ला baseline म्हणून ठेवा.** तो सोपा, तपासता येणारा आणि विश्वासाचा आहे. Anomaly detection हा दुसरा थर आहे, आणि तुमच्या प्रक्रियेवर SPC ला न दिसणारे काहीच त्याला सापडत नसेल, तर त्याची गरज नाही.
- **alarms चे बजेट ठरवा.** प्रत्येक anomaly flag कोणाचे तरी लक्ष खर्च करतो. shift मध्ये वीस गोष्टी दाखवणाऱ्या model कडे बुधवारपर्यंत कोणी लक्ष देणार नाही. त्याला मोजक्या, दर्जेदार flags पर्यंत tune करा, प्रत्येकासोबत ते कोणत्या signals मुळे आले ते दाखवा.

## प्रति hectolitre ऊर्जा आणि पाणी, न्याय्य baseline विरुद्ध

प्रत्येक बेव्हरेज प्लांट प्रति hectolitre ऊर्जा आणि पाणी मोजतो, आणि अनेकांना हे आकडे त्रासदायक वाटतात. चांगला आठवडा अनेकदा वाईट दिसतो आणि वाईट आठवडा चांगला, कारण हे गुणोत्तर volume, product mix, pack mix, cleaning वेळापत्रक आणि हवामानासोबत बदलते.

उपाय म्हणजे या घटकांची माहिती असलेला baseline. उदाहरणार्थ, आठवड्याच्या thermal energy चे packed volume, returnable glass चा वाटा (त्याच्या bottle washer सह) आणि बाहेरचे तापमान यांच्याविरुद्ध regression प्रत्येक आठवड्यासाठी अपेक्षित मूल्य देते. पाहायचा आकडा म्हणजे प्रत्यक्ष आणि अपेक्षित यांमधील फरक, कच्चे गुणोत्तर नाही. energy management standards नेमकी हीच पद्धत वापरतात, आणि हे अगदी साध्या प्रकारचे machine learning आहे.

baseline तयार झाला की वरच्या anomaly पद्धती लागू होतात: अपेक्षेपेक्षा खूप जास्त वापरणारा आठवडा, shift किंवा CIP cycle दाखवला जातो आणि त्याचे स्पष्टीकरण शोधले जाते. माझा आधीचा [CIP optimisation for water and chemicals]({{ '/2026/cip-optimisation-water-chemicals-ai/' | relative_url }}) हा लेख याची CIP बाजू पुढे नेतो, आणि [brewery energy and utilities]({{ '/2024/ai-brewery-energy-utilities-optimization/' | relative_url }}) utility बाजू पाहतो.

## हे कुठे मोडते

**बिघाडाचा डेटा तुटपुंजा असतो.** चांगली देखभाल केलेला pump काही वर्षांत एकदा बिघडू शकतो. प्लांटसाठी हे छान, पण model प्रशिक्षणासाठी भयंकर. सारख्या मशीनचा डेटा एकत्र करा, anomaly detection ने सुरुवात करा आणि हळूहळू prediction कडे जा.

**Sensors drift होतात आणि बदलले जातात.** दुरुस्तीदरम्यान बदललेला vibration sensor मशीनमध्ये अचानक बदल झाल्यासारखा दिसू शकतो. sensor बदल घटना म्हणून नोंदवा, नाहीतर model मशीनऐवजी maintenance calendar शिकेल.

**Soft sensors जुने होतात.** pasteuriser rebuild आधी प्रशिक्षित soft sensor नंतर चुकीचा ठरू शकतो. ठरलेल्या वेळापत्रकाने त्याची reference method शी तपासणी करा आणि drift झाला की पुन्हा प्रशिक्षित करा.

**Baselines खरी सुधारणा लपवू शकतात.** baseline दर महिन्याला पुन्हा प्रशिक्षित केला तर खरी बचत हळूहळू नवीन normal बनते आणि report मधून गायब होते. energy standards करतात तसे, ठरावीक कालावधीसाठी baseline गोठवा.

## सार

बेव्हरेज प्लांटमध्ये पैसा वसूल करणारे machine learning झगमगीत नाही. ते pumps पाहते, लाइनमध्ये मोजता न येणाऱ्याचा अंदाज बांधते, SPC ला एकट्याने न दिसणारे signals मधील patterns टिपते, आणि ऊर्जा व पाणी न्याय्य baseline विरुद्ध तोलते. प्रत्येक उपयोग खाली rules आणि SPC वर, आणि त्याखाली जोडलेल्या, स्वच्छ डेटावर उभा आहे. हे नीट जमले की पुढच्या दोन लेखांतील generative आणि agentic थरांना उभे राहायला भक्कम जमीन मिळते.

पुढे: [OpEx साठी generative AI]({{ '/mr/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}), जिथे प्लांटचा मजकूर उपयोगी ठरतो. विशेषतः packaging-line downtime साठी [Predicting Packaging Line Downtime and Lifting OEE]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}) पाहा. संपूर्ण यादी [मालिकेच्या पानावर]({{ '/series/ai-operational-excellence/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**filler किंवा pasteuriser वर predictive maintenance साठी कोणता डेटा लागतो?**
मशीनचा condition डेटा, जसे की vibration, motor current, तापमान आणि दाब, historian मध्ये उपयुक्त वारंवारतेने साठवलेला, आणि CMMS मधील maintenance इतिहास ज्यात काय बिघडले आणि केव्हा हे नोंदलेले असते. बिघाडाच्या नोंदी नसतानाही असामान्य वर्तन ओळखता येते, पण बिघाड किती आधी येत आहे हे शिकता येत नाही.

**machine learning मुळे statistical process control ची गरज संपते का?**
नाही. fill volume किंवा PU सारख्या एकेका variable साठी SPC हाच सोपा, तपासता येणारा baseline राहतो. machine learning एक थर जोडते, अनेक signals मध्ये एकाच वेळी दिसणाऱ्या अशा patterns साठी जे कोणताही एक control chart दाखवत नाही. एखाद्या प्रश्नावर model SPC पेक्षा चांगले करू शकत नसेल, तर SPC च वापरा.

**प्रति hectolitre ऊर्जा आणि पाणी न्याय्य पद्धतीने कसे मोजायचे?**
प्रत्यक्ष वापराची तुलना अशा baseline शी करा जो वापर ठरवणारे घटक लक्षात घेतो: उत्पादित volume, product आणि pack mix, आणि बाहेरचे तापमान. energy management standards मध्ये वापरला जातो तसा साधा regression baseline दाखवतो की एखादा आठवडा खरोखर चांगला होता की फक्त गर्दीचा होता. प्रत्यक्ष आणि baseline यांमधील फरक हाच कृतीसाठीचा आकडा आहे.
