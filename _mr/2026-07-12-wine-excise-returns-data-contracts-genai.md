---
layout: post
lang: mr
title: "data contracts म्हणून excise returns: tests हिशेब जुळवतात, LLM मसुदा लिहिते, माणूस सही करतो"
image: /assets/og/wine-excise-returns-data-contracts-genai.png
description: "The Cellar Ledger चा भाग 5. वायनरीचा excise return म्हणजे प्रत्येक tax class साठी एक balance equation. त्याच्या inputs ला data contract माना, pipeline मध्ये दर रात्री equation तपासा, आणि GenAI चा वापर त्याला इथे जे जमते त्यासाठी करा: गोंधळलेल्या removal notes चे वर्गीकरण, स्पष्टीकरणांचे मसुदे, आणि मार्गदर्शनातील योग्य परिच्छेद शोधणे."
date: 2026-07-12 09:00:00 -0700
updated: 2026-07-12
permalink: /mr/2026/wine-excise-returns-data-contracts-genai/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, compliance]
faq:
  - q: "वायनरीच्या संदर्भात data contract म्हणजे काय?"
    a: "dataset मध्ये काय असलेच पाहिजे याबद्दलचा लेखी, लागू केलेला करार. excise साठी movement ledger वरील contract असे म्हणू शकतो की प्रत्येक removal ला tax class, destination type आणि measured alcohol असावे, आणि प्रत्येक महिन्याचा opening balance मागील महिन्याच्या closing इतका असावा. pipeline हे नियम तपासतो आणि वाईट नोंदी return पर्यंत पोहोचण्याआधीच थांबवतो."
  - q: "LLM wine excise return भरू शकते का?"
    a: "त्याने आकडे भरू नयेत. आकडे ledger वरील तपासलेल्या queries मधून येतात. LLM return च्या आजूबाजूला उपयोगी आहे: मुक्त मजकुरातील removal notes चे categories मध्ये वर्गीकरण, असामान्य loss च्या स्पष्टीकरणाचा मसुदा, आणि एखाद्या व्यक्तीने वाचावा असा संबंधित मार्गदर्शन परिच्छेद शोधणे. प्रत्येक return चा आढावा घेऊन त्यावर नावाने ठरलेली व्यक्ती सही करते."
  - q: "wine tax classes मुळे reconciliation च्या समस्या का येतात?"
    a: "कारण एखादा lot इमारत न सोडताही class बदलू शकतो. उदाहरणार्थ US मध्ये still wine वर alcohol नुसार टप्प्यांत कर लागतो, आणि 16 टक्क्यांवर एक रेषा आहे. blending, fortification किंवा दुरुस्त केलेला lab result lot ला ती रेषा ओलांडायला लावू शकतो, आणि तो बदल event म्हणून नोंदवला नाही तर प्रत्येक class चा balance जुळणे थांबते."
---

**थोडक्यात उत्तर: excise return म्हणजे प्रत्येक tax class साठी balance equation: opening, अधिक produced आणि received, वजा removals आणि losses, बरोबर closing. महिनाअखेरीस हे equation हाताने form मध्ये उतरवले, तर प्रत्येक चूक सर्वात वाईट क्षणी समोर येते. return च्या inputs ना movement ledger वरील data contract माना, pipeline मध्ये दर रात्री equation तपासा, आणि return अशी query बनते जिने आधीच आपल्या तपासण्या पार केल्या आहेत. GenAI कडेकडेने मदत करतो: गोंधळलेल्या removal notes ची वर्गवारी, विचित्र loss च्या स्पष्टीकरणाचा मसुदा, आणि मार्गदर्शनातील योग्य परिच्छेद शोधणे. तो आकडे तयार करत नाही, आणि सही करत नाही.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एका tax class साठी excise balance equation: opening balance, अधिक produced आणि received, वजा tax-paid removed, वजा in bond transferred किंवा exported, वजा losses, बरोबर closing balance. खाली data contract मधील तीन रात्रीच्या tests: opening बरोबर मागील महिन्याचे closing, प्रत्येक class साठी equation शून्यावर जुळते, आणि प्रत्येक class बदल event म्हणून नोंदवलेला. एक banner सांगतो की return म्हणजे आधीच tests पार केलेली query आहे.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एक TAX CLASS, एक EQUATION, दर रात्री तपासलेले</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="95" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">opening</text>
<text x="95" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="177" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">+</text>
<rect x="195" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">produced</text>
<text x="260" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; received</text>
<text x="342" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="360" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="425" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">removed</text>
<text x="425" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">tax-paid</text>
<text x="507" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="525" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="590" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">in bond</text>
<text x="590" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; export</text>
<text x="672" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="690" y="60" width="110" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="745" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">losses</text>
<text x="817" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">=</text>
<rect x="835" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="900" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">closing</text>
<text x="900" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="500" y="160" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">DATA CONTRACT TESTS</text>
<rect x="30" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="180" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; opening = मागील closing</text>
<text x="180" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">महिन्यांदरम्यान गुपचूप edits नाहीत</text>
<rect x="350" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; equation 0 वर जुळते</text>
<text x="500" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">प्रत्येक tax class, प्रत्येक महिना</text>
<rect x="670" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="820" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; class बदल म्हणजे events</text>
<text x="820" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">16% ओलांडणारा blend नोंदवला जातो</text>
<rect x="30" y="262" width="940" height="42" rx="10" fill="#06483f"/>
<text x="500" y="288" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">RETURN म्हणजे आधीच TESTS पार केलेली QUERY</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">excise अधिकारी जे equation तपासतो तेच, पण महिनाअखेरीस माणसाऐवजी दर रात्री pipeline ने तपासलेले.</figcaption>
</figure>

महिन्याचा दुसरा कामकाजाचा दिवस आहे आणि excise return भरायचा आहे. कोणीतरी मागील महिन्याचा return उघडतो, cellar system उघडतो, आणि आकडे form मध्ये उतरवू लागतो. opening balance मागील महिन्याच्या closing शी जुळत नाही. मधल्या काळात कोणीतरी tank volume edit केले. पुढचे तीन तास ते कोणते हे शोधण्यात जातात, आणि deadline जवळ येत राहते.

ही मालिकेतील सर्वात कमी आकर्षक पोस्ट आहे, आणि कदाचित सर्वात उपयुक्त. duty भरणारी प्रत्येक वायनरी याच्यासोबत जगते, आणि बहुतेक जण हे एक माणूस आणि calculator घेऊन सोडवतात. [movement ledger]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) आणि [loss map]({{ '/mr/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) ने बहुतेक काम आधीच केले आहे. ही पोस्ट असे नियम जोडते जे कोणी form उघडण्याआधीच return विश्वासार्ह बनवतात.

## return म्हणजे balance equation

देश कोणताही असो, वायनरीचा excise return प्रत्येक tax class साठी एकाच समीकरणावर येतो:

> opening + produced आणि received - tax-paid removed - in bond transferred किंवा exported - losses = closing

US मध्ये हा tax class नुसार विभागलेला मासिक Report of Wine Premises Operations असतो. EU मध्ये duty-suspended movements EMCS मधून जातात. भारतात प्रत्येक राज्याच्या excise विभागाचे स्वतःचे registers आणि formats असतात. forms वेगळे असतात. गणित तेच असते.

data team साठी ही चांगली बातमी आहे, कारण समीकरण ही अशी गोष्ट आहे जी pipeline तपासू शकतो.

## tax class चा सापळा

सूक्ष्म भाग म्हणजे "प्रत्येक tax class साठी". wine वर टप्प्यांत कर लागतो. US मध्ये 16% किंवा त्याखालील alcohol ची still wine एक class, 16 पेक्षा जास्त ते 21% दुसरा, 21 पेक्षा जास्त ते 24% तिसरा, आणि sparkling व carbonated wines वेगळ्या. इतर बाजार आपापल्या रेषा ओढतात.

एखादा lot इमारत न सोडताही class बदलू शकतो. 15.8% lot 16.6% lot सोबत blend करा, आणि volumes नुसार निकाल 16% च्या कोणत्याही बाजूला येऊ शकतो. fortify करा, आणि lot class ओलांडतो. lab result दुरुस्त करा, आणि गेल्या महिन्यात 16% खाली नोंदवलेला lot प्रत्यक्षात त्यावर निघतो.

हे बदल नोंदवले नाहीत, तर प्रत्येक class चे equation जुळणे थांबते, आणि का हे कोणालाच कळत नाही. म्हणून class बदल स्वतःच ledger मध्ये event बनतो: lot 24-SH-03 या तारखेला, या volume सह, या blend मुळे class A मधून class B मध्ये जातो. [या मालिकेतील पहिल्या पोस्ट]({{ '/mr/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) ने predicted alcohol ऐवजी measured alcohol वर आग्रह धरला तो याच कारणासाठी. ढोबळ नियमाच्या रूपांतरावर आधारित tax class म्हणजे auditor ची वाट पाहणारी समस्या.

## data contract लिहिणे

data contract म्हणजे dataset मध्ये काय असलेच पाहिजे याबद्दलचा लेखी करार, जो चांगल्या हेतूंनी नव्हे तर pipeline कडून लागू केला जातो. excise साठी movement ledger वरील contract छोटा आहे:

1. **प्रत्येक removal ला tax class, destination type आणि measured alcohol असते.** tax-paid, in bond, export, sample, destroyed. destination नसलेले removal नाकारले जाते.
2. **प्रत्येक class बदल हा event आहे.** एखाद्या lot चे measured alcohol class ची सीमा ओलांडत असेल, तर pipeline class change event ची अपेक्षा करतो आणि तो नसल्यास flag करतो.
3. **opening बरोबर मागील closing.** प्रत्येक class साठी, प्रत्येक महिन्याला. ही एकच test प्रत्येक गुपचूप edit पकडते.
4. **समीकरण शून्यावर जुळते.** प्रत्येक class, प्रत्येक महिना, तुमच्या accountant सोबत ठरवलेल्या tolerance आत. शून्य नसलेला residual कोणीतरी त्याचे स्पष्टीकरण देईपर्यंत return अडवतो.
5. **negative balances नाहीत.** negative closing volume असलेला class म्हणजे एखादा event गहाळ आहे किंवा चुकीच्या वर्गात आहे.

व्यवहारात या तुम्ही आधीच वापरत असलेल्या कशातही मोजक्या tests असतात: dbt tests, Great Expectations, Fabric data quality rules, किंवा रात्रीचा job fail करणाऱ्या साध्या SQL assertions. महत्त्वाचा निर्णय म्हणजे त्या महिनाअखेरीस नव्हे तर **दर रात्री** चालवणे. 14 तारखेला fail होणारी test तुम्हाला नोंद दुरुस्त करायला दोन आठवडे देते, जेव्हा काय घडले ते लोकांना अजून आठवत असते. 2 तारखेला fail होणारी test तुम्हाला एक वाईट सकाळ देते.

fail होणाऱ्या नोंदी शून्यात नव्हे तर fail झालेल्या नियमासह quarantine table मध्ये जातात. cellar team ला दुरुस्त करायच्या गोष्टींची छोटी यादी दिसते. त्या दुरुस्त होईपर्यंत return त्यांना कधीच पाहत नाही.

## GenAI प्रत्यक्षात कुठे मदत करतो

आकडे तपासलेल्या queries हाताळत असल्याने, language model साठी उपयुक्त कामे म्हणजे ज्यात गोंधळलेला मजकूर असतो ती.

**removal notes चे वर्गीकरण.** operators "2 cs to Sunday tasting", "breakage, dropped pallet" किंवा "sample for show" असे काहीतरी लिहितात. त्यांचे categories व्हायला हवेत: sample, tasting room, breakage, destroyed. model हे confidence score सह चांगले वर्गीकरण करते, आणि जे अनिश्चित आहे ते माणसाकडे पाठवते. हे छोटे काम दर महिन्याला तास वाचवते.

**स्पष्टीकरणांचे मसुदे.** loss नेहमीपेक्षा मोठा असतो तेव्हा return ला किंवा अंतर्गत फाईलला का, हे सांगणारी note लागते. model ती loss map च्या आकड्यांवरून आणि adjustment कारणांवरून, [variance note]({{ '/mr/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) च्याच pattern ने तयार करते: प्रत्येक आकडा SQL पुरवते, model त्याभोवती शब्द लिहिते.

**योग्य परिच्छेद शोधणे.** excise मार्गदर्शन लांबलचक असते आणि वारंवार update होते. regulator च्या प्रकाशित मार्गदर्शनावरचा retrieval assistant, जो परिच्छेद उद्धृत करतो आणि त्याची link देतो, प्रश्न उभा राहतो तेव्हा खरा वेळ वाचवतो: "दुसऱ्या bonded premises च्या topping साठी वापरलेली wine आपण कशी हाताळायची?". तो ग्रंथपाल आहे. परिच्छेद वाचून निर्णय माणूसच घेतो.

**अधिकाऱ्याला उत्तर देणे.** एखाद्या class चा balance का हलला असे excise अधिकारी विचारतो तेव्हा ledger वाचण्याची परवानगी असलेला agent नेमके events, तारखा आणि operators काढू शकतो, आणि rows जोडून उत्तराचा मसुदा तयार करू शकतो. माणसाने तपासल्यानंतर उत्तर जाते.

त्याने जे करू नये ते म्हणजे return भरणे, कायद्याचा अर्थ लावणे, किंवा धूसर क्षेत्रातील movement कशी हाताळायची ते ठरवणे. हे कायदेशीर वजन असलेले निर्णय आहेत, आणि ते नावाने ठरलेल्या व्यक्तीचे आहेत.

## हे कुठे मोडते

**नियम वेगळे असतात आणि बदलतात.** tax classes, मान्य losses आणि reporting formats देशानुसार, आणि भारतात राज्यानुसार, बदलतात. contract मध्ये तुमचे नियम असायला हवेत, ते जाणणाऱ्याने तपासलेले, आणि ते बदलल्यावर update केलेले.

**महिनाअखेर अडवणाऱ्या contracts ना बगल दिली जाते.** fail होणारी test कोणताही मार्ग न ठेवता 2 तारखेला return थांबवत असेल, तर कोणीतरी त्याभोवती मार्ग शोधेल. tests दर रात्री चालवा आणि quarantine चा मार्ग असा रचा की pipeline ला बगल देण्यापेक्षा नोंद दुरुस्त करणे सोपे असेल.

**मान्य loss हा नियामक प्रश्न आहे, सांख्यिकीय नाही.** loss map सांगू शकतो की एखादा loss असामान्य आहे. तो regulator च्या मर्यादेत आहे का, आणि त्यावर कर लागतो का, हे नियम आणि सही करणारी व्यक्ती ठरवतात.

**retrieval चुकीचा परिच्छेद समोर आणू शकतो.** index मधील जुने मार्गदर्शन, किंवा जवळचा पण पूर्णपणे संबंधित नसलेला परिच्छेद, आत्मविश्वासाने परत येईल. index अद्ययावत ठेवा आणि नेहमी मूळ स्रोत वाचा.

## निष्कर्ष

excise return हा असा एकमेव report आहे ज्यातील प्रत्येक आकडा व्यवसायाबाहेरचा कोणीतरी तपासतो. म्हणूनच हाताने आकडे उतरवणे थांबवण्यासाठी हीच सर्वोत्तम जागा आहे. return चे नियम data contract म्हणून लिहा, ते दर रात्री तपासा, आणि महिनाअखेर शोधाशोध न राहता आढावा बनतो. जिथे गोंधळ मजकुराचा आहे तिथे GenAI वापरा, notes ची वर्गवारी आणि स्पष्टीकरणांचे मसुदे, आणि आकडे व सही माणसांकडे आणि तपासलेल्या code कडेच ठेवा.

मालिकेतील पुढील आणि शेवटचा भाग: [वायनरी AI कुठे मोडते]({{ '/mr/2026/where-winery-ai-breaks-ten-vintages-ten-rows/' | relative_url }}), आणि दहा vintages म्हणजे फक्त दहा rows का. संपूर्ण यादी [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**वायनरीच्या संदर्भात data contract म्हणजे काय?**
dataset मध्ये काय असलेच पाहिजे याबद्दलचा लेखी, लागू केलेला करार. excise साठी movement ledger वरील contract असे म्हणू शकतो की प्रत्येक removal ला tax class, destination type आणि measured alcohol असावे, आणि प्रत्येक महिन्याचा opening balance मागील महिन्याच्या closing इतका असावा. pipeline हे नियम तपासतो आणि वाईट नोंदी return पर्यंत पोहोचण्याआधीच थांबवतो.

**LLM wine excise return भरू शकते का?**
त्याने आकडे भरू नयेत. आकडे ledger वरील तपासलेल्या queries मधून येतात. LLM return च्या आजूबाजूला उपयोगी आहे: मुक्त मजकुरातील removal notes चे categories मध्ये वर्गीकरण, असामान्य loss च्या स्पष्टीकरणाचा मसुदा, आणि एखाद्या व्यक्तीने वाचावा असा संबंधित मार्गदर्शन परिच्छेद शोधणे. प्रत्येक return चा आढावा घेऊन त्यावर नावाने ठरलेली व्यक्ती सही करते.

**wine tax classes मुळे reconciliation च्या समस्या का येतात?**
कारण एखादा lot इमारत न सोडताही class बदलू शकतो. उदाहरणार्थ US मध्ये still wine वर alcohol नुसार टप्प्यांत कर लागतो, आणि 16 टक्क्यांवर एक रेषा आहे. blending, fortification किंवा दुरुस्त केलेला lab result lot ला ती रेषा ओलांडायला लावू शकतो, आणि तो बदल event म्हणून नोंदवला नाही तर प्रत्येक class चा balance जुळणे थांबते.
