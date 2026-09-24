---
layout: post
lang: mr
title: "spirit safe वर alarms ऐवजी soft sensors आणि proactive bands"
image: /assets/og/soft-sensors-proactive-bands-spirit-safe.png
description: "The Still and the Model चा भाग 2. hydrometer readings दरम्यानची distillate strength तापमाने आणि flow वरून अंदाजे काढा, प्रत्येक run ची चांगल्या runs वरून बांधलेल्या band शी तुलना करा, आणि कृती करायला अजून वेळ असतानाच drift flag करा. operator ने दुर्लक्ष करायला शिकलेल्या panel वर आणखी एक fixed alarm लावण्यापेक्षा हे सरस का ठरते."
date: 2026-07-27 09:00:00 -0700
updated: 2026-07-27
permalink: /mr/2026/soft-sensors-proactive-bands-spirit-safe/
tags: [distilling-maturation, still-and-model, soft-sensors, machine-learning, data-engineering]
faq:
  - q: "distillery मध्ये soft sensor म्हणजे काय?"
    a: "soft sensor अशी गोष्ट अंदाजे काढतो जी तुम्ही सतत मोजू शकत नाही, जसे distillate strength, आणि तेही अशा गोष्टींवरून ज्या तुम्ही मोजू शकता, जसे vapour तापमान, pot तापमान, pressure आणि flow. spirit safe hydrometer सारखे खरे मोजमाप घेतले जाते तेव्हा प्रत्येक वेळी त्याच्याशी तो पुन्हा calibrate होतो. तो readings मधील पोकळी भरतो; reference ची जागा घेत नाही."
  - q: "still run वरील proactive band म्हणजे काय?"
    a: "distillery च्या स्वतःच्या चांगल्या runs वरून बांधलेले आवरण, जे run च्या प्रत्येक टप्प्यावर strength, तापमान किंवा flow साधारणपणे कुठे असतात ते दाखवते. नव्या run ची band शी सतत तुलना होते. तो band सोडू लागला की operator ला लवकर कळवले जाते, बहुतेकदा कोणताही fixed alarm threshold ओलांडला जाण्याच्या खूप आधी."
  - q: "distillery operators alarms कडे दुर्लक्ष का करतात?"
    a: "कारण ते खूप जास्त असतात आणि बहुतेकांना कृतीची गरज नसते. EEMUA 191 आणि ISA-18.2 सारखे alarm management मार्गदर्शन alarms च्या पुराला स्वतःच एक safety समस्या मानते. प्रत्येक त्रासदायक alarm operator ला शिकवतो की alarms acknowledge करून विसरता येतात, आणि खरा alarm येतो तेव्हा हाच धडा नेमका चुकीचा ठरतो."
---

**थोडक्यात उत्तर: spirit safe मधील hydrometer हेच सत्य आहे, पण ते डोळ्यांनी वाचले जाते आणि दर मिनिटाला नाही. readings दरम्यान soft sensor vapour आणि pot तापमाने, pressure आणि flow वरून strength अंदाजे काढू शकतो, आणि stillman प्रत्येक वेळी reading घेतो तेव्हा पुन्हा calibrate होऊ शकतो. हा अंदाज distillery च्या स्वतःच्या चांगल्या runs वरून बांधलेल्या band शी तुलना करा, घड्याळाच्या वेळेनुसार नव्हे तर run किती पुढे गेला आहे त्यानुसार index करून, आणि भरकटणारा run तुम्ही लवकर flag करता, समायोजन करायला अजून वेळ असतानाच. fixed low-strength alarm तीच गोष्ट वीस मिनिटांनी सांगतो, अशा panel वर जो operator ने आधीच गप्प करायला शिकलेला आहे.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="spirit run साठी band chart. आडवा अक्ष म्हणजे परत मिळालेल्या charge alcohol चा वाटा, उभा अक्ष म्हणजे distillate strength. चांगल्या runs वरून बांधलेला छायांकित band खाली उतरतो. सामान्य run त्याच्या आत राहतो. भरकटणारा run run च्या मध्याजवळ band ची खालची कड सोडतो, जिथे गुलाबी खूण सांगते की band त्याला flag करतो. तोच run fixed low-strength alarm रेषा खूप नंतर ओलांडतो, जिथे दुसरी खूण सांगते की alarm वाजतो.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ALARM च्या आधी BAND ला DRIFT दिसतो (उदाहरणादाखल)</text>
<g font-family="sans-serif">
<line x1="100" y1="280" x2="910" y2="280" stroke="#4a6b64" stroke-width="1"/>
<line x1="100" y1="60" x2="100" y2="280" stroke="#4a6b64" stroke-width="1"/>
<text x="505" y="302" text-anchor="middle" font-size="10.5" fill="#4a6b64">परत मिळालेल्या charge alcohol चा वाटा &#8594;</text>
<text x="88" y="170" text-anchor="middle" font-size="10.5" fill="#4a6b64" transform="rotate(-90 88 170)">safe वरील strength</text>
<polygon points="100,80 300,100 500,130 700,175 900,235 900,265 700,205 500,160 300,128 100,105" fill="#f0f6f5" stroke="#4db6a2" stroke-width="1"/>
<polyline points="100,92 300,114 500,145 700,190 900,250" fill="none" stroke="#06483f" stroke-width="2.5"/>
<polyline points="100,92 300,118 400,140 500,172 600,200 700,228" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<line x1="100" y1="225" x2="900" y2="225" stroke="#4a6b64" stroke-width="1.5" stroke-dasharray="6 5"/>
<text x="905" y="219" text-anchor="end" font-size="10.5" fill="#4a6b64">fixed low-strength alarm</text>
<circle cx="450" cy="156" r="7" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<text x="450" y="196" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">band इथे flag करतो</text>
<circle cx="690" cy="225" r="7" fill="none" stroke="#06483f" stroke-width="2.5"/>
<text x="690" y="252" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">alarm इथे वाजतो</text>
<text x="230" y="76" font-size="10.5" fill="#00695c">चांगल्या runs वरून band</text>
<text x="780" y="170" font-size="10.5" fill="#06483f">सामान्य run</text>
<rect x="40" y="312" width="920" height="24" rx="6" fill="#06483f"/>
<text x="500" y="329" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">तोच RUN, तोच DATA &#183; त्यांपैकी एकच कृतीसाठी वेळ ठेवतो</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरणादाखल आकार. band तुमच्या स्वतःच्या चांगल्या runs वरून बांधलेला असतो, आणि x अक्ष म्हणजे घड्याळ नव्हे तर run मधील प्रगती.</figcaption>
</figure>

spirit still वर इमारतीतील सर्वात महत्त्वाचा आकडा काचेतून वाचला जातो. stillman spirit safe मध्ये तरंगणाऱ्या hydrometer कडे पाहतो, तापमानासाठी दुरुस्ती करतो आणि तो लिहून ठेवतो. ते reading हेच reference आहे. पण ते ठरावीक अंतराने घेतले जाते, अशा व्यक्तीकडून जिच्याकडे आणखी चार कामे असतात, आणि धावपळीच्या shift मध्ये readings मधील अंतर वाढत जाते.

[मागील पोस्ट]({{ '/mr/2026/physics-informed-digital-twin-pot-still/' | relative_url }}) ने असा twin बांधला ज्याला run कुठे जायला हवा हे माहीत आहे. ही पोस्ट त्या अपेक्षेच्या तुलनेत चालू run वर लक्ष ठेवण्याबद्दल आहे, कोणीही न वाचणाऱ्या alarms च्या ढिगात भर न घालता.

## soft sensor: readings दरम्यानची strength

soft sensor अशी गोष्ट अंदाजे काढतो जी तुम्ही सतत मोजू शकत नाही, आणि तेही तुम्ही मोजू शकता अशा गोष्टींवरून. pot still वर उपयुक्त inputs बहुतेक historians वर आधीच असतात:

- **pot मधील द्रवाचे तापमान.** दिलेल्या pressure वर ethanol आणि पाण्याचे उत्कलन तापमान pot मधील द्रवाच्या composition नुसार बदलते.
- **lyne arm किंवा column head वरील vapour तापमान.** हे बाहेर पडणाऱ्या vapour च्या composition नुसार बदलते.
- **barometric pressure.** उत्कलन बिंदू हवामानासोबत सरकतात. जोरदार front त्यांना एका degree च्या काही दशांशांनी हलवू शकतो, आणि भोळ्या अंदाजाला फसवायला एवढे पुरेसे आहे.
- **distillate flow आणि cumulative volume**, run किती पुढे गेला हे कळण्यासाठी.

equilibrium डेटावरून काढलेला physics-आधारित अंदाज, twin मधील fitted parameters ने दुरुस्त केलेला, दर काही सेकंदांनी strength देतो. मग येतो तो भाग जो त्याला विश्वासार्ह बनवतो: stillman प्रत्येक वेळी hydrometer reading घेतो तेव्हा soft sensor आपल्या अंदाजाची reading शी तुलना करतो आणि आपला bias दुरुस्त करतो. reading हेच reference राहते. soft sensor readings मधील पोकळी भरतो, आणि शेवटच्या reading विरुद्धची त्याची त्रुटी त्याच्या शेजारी दाखवली जाते, म्हणजे कोणता आकडा मोजलेला आणि कोणता अंदाजे हे कोणी विसरत नाही.

data engineering छोटे आहे पण महत्त्वाचे. hydrometer readings त्यांच्या timestamp, तापमान आणि ती घेणाऱ्या व्यक्तीसह, historian tags च्याच timeline मध्ये साठवा. जो soft sensor आपला अंदाज reading शी मिनिटाला मिनिट जुळवू शकत नाही, तो पुन्हा calibrate होऊ शकत नाही.

## band: threshold शी नव्हे, चांगल्या runs शी तुलना

fixed alarm एकच प्रश्न विचारतो: strength X च्या खाली गेली का? ती जाईपर्यंत run बराच वेळ भरकटत असतो.

band अधिक चांगला प्रश्न विचारतो: या टप्प्यावर हा run आपल्या चांगल्या runs सारखा वागत आहे का? तो बांधण्यासाठी:

1. **चांगले runs निवडा.** त्याच still वरील आणि त्याच charge प्रकाराचे शेवटचे तीस किंवा पन्नास runs, जे नीट झाले यावर team सहमत आहे.
2. **त्यांना वेळेनुसार नव्हे, प्रगतीनुसार index करा.** heat input आणि charge आकारानुसार runs ची लांबी बदलते. twin च्या balance वरून आधीच गोळा झालेल्या charge alcohol च्या वाट्याविरुद्ध प्रत्येक run मांडा, म्हणजे प्रत्येक run एकाच मोजपट्टीवर येतो.
3. **प्रत्येक पायरीवर median आणि robust spread घ्या** (standard deviation ऐवजी median absolute deviation, म्हणजे एका विचित्र run मुळे सर्वांसाठी band रुंदावत नाही).
4. **चालू run ची सतत तुलना करा** आणि तो band सोडतो तेव्हा, किंवा कोणत्याही चांगल्या run पेक्षा वेगाने त्याबाहेर चालला असेल तेव्हा, flag करा.

उदाहरणादाखल chart मध्ये भरकटणारा run fixed alarm वाजण्याच्या एक-तृतीयांश आधीच band सोडतो. ती पोकळीच उपयुक्त भाग आहे. steam तपासण्याची, condenser च्या पाण्याकडे पाहण्याची किंवा लवकर hydrometer reading घेण्याची ती वेळ आहे.

bands फक्त strength साठी नाहीत. condenser outlet तापमान, steam flow आणि distillate flow यांना प्रत्येकी स्वतःचा band मिळतो. एकाच वेळी दोघांवर भरकटणारा run एकाच्या कडेला स्पर्श करणाऱ्या run पेक्षा कितीतरी जास्त लक्ष देण्यासारखा असतो.

## कमी alarms हेच ध्येय का

alarm management वर एक संपूर्ण साहित्य आहे, आणि त्याचा मध्यवर्ती निष्कर्ष अस्वस्थ करणारा आहे: जास्त alarms मुळे plants कमी सुरक्षित होतात. EEMUA 191 आणि ISA-18.2 सारखे मार्गदर्शन स्थिर operation मध्ये प्रति operator दर दहा मिनिटांत साधारण एक alarm असे लक्ष्य ठेवते, आणि त्यावरील पुराला स्वतंत्र समस्या मानते. वाजणारा आणि कृतीची गरज नसलेला प्रत्येक alarm operator ला शिकवतो की alarms acknowledge करून विसरता येतात.

म्हणून band ने alarms ची जागा घ्यायला हवी, त्यांच्यात सामील व्हायला नको. हे लागू करणाऱ्या distillery साठी चांगला नियम:

- **safety alarms आणि interlocks जसे आहेत तसेच ठेवा.** high pressure, high temperature आणि vapour detection या analytics समस्या नाहीत.
- **band ज्या त्रासदायक process alarms ना व्यापतो ते निवृत्त करा**, एकावेळी एक, band ने तेच events आधी पकडतो हे दाखवल्यानंतर.
- **band flags सल्ल्यासारखे आणि शांत ठेवा.** operator screen वर रंगबदल आणि एक note, horn नाही.
- **पहिले काही महिने प्रत्येक flag चा साप्ताहिक आढावा घ्या.** खूप वेळा flag करणारा band खूप अरुंद आहे. कधीच flag न करणारा खूप रुंद.

## हे कुठे मोडते

**band तुमच्या सवयी शिकतो, चांगल्या आणि वाईट.** चांगले runs सगळे थोडे जास्त वेगवान असतील, तर band जास्त वेग सामान्य ठरवतो. reference runs जाणीवपूर्वक निवडा, आणि process हेतुपुरस्सर बदलल्यावर band पुन्हा बांधा.

**soft sensors readings दरम्यान सरकतात.** मळलेला temperature probe किंवा बदललेला steam पुरवठा अंदाज हलवतो, आणि band ला खरा drift आणि वाईट probe यांतील फरक कळत नाही. म्हणूनच hydrometer reading reference राहते आणि त्याविरुद्धची soft sensor ची त्रुटी नेहमी screen वर असते.

**run ची सुरुवात आणि शेवट सर्वात कठीण.** foreshots आणि run ची शेपटी म्हणजे जिथे equilibrium model सर्वात कमकुवत असते आणि operators नाक आणि अनुभवावर सर्वाधिक अवलंबून असतात. bands run च्या मधल्या भागासाठी वापरा, जिथे physics नीट वागते.

**तो cut करत नाही.** band सांगतो की run असामान्य आहे. flavour साठी कुठे cut करायचा हे तो सांगत नाही. [cut points पोस्ट]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}) मांडते तसे ते stillman कडेच राहते.

## निष्कर्ष

spirit safe hydrometer हेच सत्य आहे, आणि ते एखादी व्यक्ती ठरावीक अंतराने वाचते. soft sensor पोकळी भरतो आणि प्रत्येक reading शी पुन्हा calibrate होऊन प्रामाणिक राहतो. तुमच्या स्वतःच्या चांगल्या runs वरून बांधलेला band कृतीसाठी वेळ असतानाच drift दाखवतो, आणि alarms वाढवण्याऐवजी निवृत्त करू देतो. ध्येय हुशार horn नाही. ध्येय शांत panel आहे जिथे उरलेले मोजके signals पाहण्यासारखे असतात.

मालिकेतील पुढील भाग: [still operator साठी LLM copilot]({{ '/mr/2026/llm-copilot-still-operator/' | relative_url }}), जो तोच डेटा वाचतो आणि setpoint ला कधीच हात लावत नाही. sensors साठी पाहा [IoT in the Distillery]({{ '/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). संपूर्ण यादी [The Still and the Model मालिकेच्या पानावर]({{ '/series/still-and-model/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**distillery मध्ये soft sensor म्हणजे काय?**
soft sensor अशी गोष्ट अंदाजे काढतो जी तुम्ही सतत मोजू शकत नाही, जसे distillate strength, आणि तेही अशा गोष्टींवरून ज्या तुम्ही मोजू शकता, जसे vapour तापमान, pot तापमान, pressure आणि flow. spirit safe hydrometer सारखे खरे मोजमाप घेतले जाते तेव्हा प्रत्येक वेळी त्याच्याशी तो पुन्हा calibrate होतो. तो readings मधील पोकळी भरतो; reference ची जागा घेत नाही.

**still run वरील proactive band म्हणजे काय?**
distillery च्या स्वतःच्या चांगल्या runs वरून बांधलेले आवरण, जे run च्या प्रत्येक टप्प्यावर strength, तापमान किंवा flow साधारणपणे कुठे असतात ते दाखवते. नव्या run ची band शी सतत तुलना होते. तो band सोडू लागला की operator ला लवकर कळवले जाते, बहुतेकदा कोणताही fixed alarm threshold ओलांडला जाण्याच्या खूप आधी.

**distillery operators alarms कडे दुर्लक्ष का करतात?**
कारण ते खूप जास्त असतात आणि बहुतेकांना कृतीची गरज नसते. EEMUA 191 आणि ISA-18.2 सारखे alarm management मार्गदर्शन alarms च्या पुराला स्वतःच एक safety समस्या मानते. प्रत्येक त्रासदायक alarm operator ला शिकवतो की alarms acknowledge करून विसरता येतात, आणि खरा alarm येतो तेव्हा हाच धडा नेमका चुकीचा ठरतो.
