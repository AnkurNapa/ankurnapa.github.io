---
layout: post
lang: mr
title: "वायनरी AI कुठे मोडते: दहा vintages म्हणजे दहा rows"
image: /assets/og/where-winery-ai-breaks-ten-vintages-ten-rows.png
description: "The Cellar Ledger चा भाग 6. brewery वर्षाला शेकडो batches बनवते. वायनरीला एकच vintage मिळते. vintage चे परिणाम भाकीत करणारी models overfit का होतात, वायनरीचा डेटा प्रत्यक्षात कुठे समृद्ध असतो, आणि time-series foundation models, synthetic data आणि LLMs छोट्या डेटाच्या समस्येबद्दल काय करू शकतात आणि काय नाही."
date: 2026-07-17 09:00:00 -0700
updated: 2026-07-17
permalink: /mr/2026/where-winery-ai-breaks-ten-vintages-ten-rows/
tags: [winemaking, cellar-ledger, machine-learning, generative-ai, data-strategy]
faq:
  - q: "brewery पेक्षा वायनरीत machine learning कठीण का आहे?"
    a: "कारण शिकण्याचे एकक बहुतेकदा vintage असते, आणि वायनरीला वर्षाला एकच मिळते. harvest date, yield किंवा quality score सारख्या प्रश्नांसाठी दहा वर्षांचा इतिहास प्रत्येक block साठी दहा rows देतो, तर वर्षाला शेकडो batches बनवणाऱ्या brewery कडे हजारो असतात. दहा rows वर train झालेली models भूतकाळातून शिकण्याऐवजी बहुतेक तो पाठ करतात."
  - q: "synthetic data किंवा foundation model छोटा वायनरी dataset दुरुस्त करू शकतो का?"
    a: "स्वतःहून नाही. तुमच्या दहा vintages वरून बनवलेल्या synthetic data मध्ये अशी कोणतीही माहिती नसते जी त्या दहा vintages मध्ये आधीच नव्हती. time-series foundation models fermentation सारख्या curve चा वाजवी zero-shot forecast देऊ शकतात, पण त्यांना तुमच्या vineyard बद्दल काहीच माहीत नसते. भक्कम रचनेत दोन्ही उपयुक्त आहेत, आणि दोघांपैकी कोणीही हरवलेला इतिहास निर्माण करत नाही."
  - q: "वायनरीत AI खरोखर कुठे चालते?"
    a: "जिथे एकाच हंगामात डेटा समृद्ध असतो तिथे: प्रत्येक tank ची fermentation curve, cellar मधील sensor streams, पिकण्याच्या काळातील berry sampling, आणि tasting notes व cellar logs सारखा मुक्त मजकूर. ferment ची dynamics शिकणाऱ्या models कडे, किंवा logs वाचणाऱ्या LLM कडे, वर्षाला शेकडो किंवा हजारो उदाहरणे असतात."
---

**थोडक्यात उत्तर: वायनरींना विकले जाणारे बहुतेक AI harvest date, yield किंवा quality score सारखा vintage चा परिणाम भाकीत करण्याचा प्रयत्न करते, आणि वायनरीला वर्षाला एकच vintage मिळते. दहा वर्षांचा इतिहास म्हणजे प्रत्येक block साठी दहा rows. त्यावर train झालेली models बहुतेक पाठ करतात, आणि ज्या हवामानातून ती दहा वर्षे आली ते आधीच बदलत आहे. पण हंगामाच्या आत डेटा समृद्ध असतो: प्रत्येक tank ची fermentation curve, प्रत्येक sensor, प्रत्येक berry sample आणि प्रत्येक cellar note. AI तिथे बांधा, जिथे वर्षांपलीकडे भाकीत करावेच लागते तिथे blocks एकत्र करा, आणि foundation model, synthetic data किंवा LLM ने दहा rows चे हजार केले असा दावा करणाऱ्या कोणत्याही गोष्टीबद्दल अतिशय साशंक राहा.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="दहा वर्षांच्या training examples ची तुलना करणारे तीन आडवे bars. वर्षाला 300 batches बनवणाऱ्या brewery कडे 3,000 batch rows आहेत. वर्षाला 120 fermentations असलेल्या वायनरीकडे 1,200 fermentation curves आहेत. harvest date किंवा yield सारख्या प्रश्नांसाठी त्याच वायनरीकडे प्रत्येक block साठी 10 vintage rows आहेत. 10 rows चा bar अगदी छोटा आहे आणि गुलाबी रंगात ठळक केलेला आहे.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">दहा वर्षांचा इतिहास, TRAINING EXAMPLES मध्ये मोजलेला (उदाहरणादाखल)</text>
<g font-family="sans-serif">
<text x="40" y="80" font-size="12" font-weight="700" fill="#06483f">brewery batches</text>
<text x="40" y="97" font-size="10.5" fill="#4a6b64">वर्षाला 300</text>
<rect x="260" y="66" width="600" height="34" rx="6" fill="#06483f"/>
<text x="872" y="89" font-size="13" font-weight="700" fill="#06483f">3,000</text>
<text x="40" y="150" font-size="12" font-weight="700" fill="#06483f">वायनरी fermentations</text>
<text x="40" y="167" font-size="10.5" fill="#4a6b64">वर्षाला 120 tanks, हंगामाच्या आत</text>
<rect x="260" y="136" width="240" height="34" rx="6" fill="#4db6a2"/>
<text x="512" y="159" font-size="13" font-weight="700" fill="#06483f">1,200</text>
<text x="40" y="220" font-size="12" font-weight="700" fill="#06483f">वायनरी vintages</text>
<text x="40" y="237" font-size="10.5" fill="#4a6b64">प्रति block, harvest date किंवा yield साठी</text>
<rect x="260" y="206" width="4" height="34" rx="1" fill="#ff4081"/>
<text x="276" y="229" font-size="13" font-weight="700" fill="#ff4081">10</text>
<rect x="40" y="266" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="291" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">जिथे ROWS आहेत तिथे AI बांधा &#183; जिथे नाहीत तिथे प्रामाणिक राहा</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">तीच वायनरी, तीच दहा वर्षे. हंगामाच्या आत डेटा समृद्ध आहे, हंगामांपलीकडे तुटपुंजा.</figcaption>
</figure>

एक vendor वायनरीला असे model दाखवतो जे प्रत्येक block साठी सर्वोत्तम harvest date भाकीत करते. demo छान दिसतो. accuracy chart त्याहून छान. मग कोणीतरी विचारते की ते किती vintages वर train झाले, आणि उत्तर येते अकरा.

अकरा harvests म्हणजे प्रत्येक block साठी अकरा rows. वर्षाला 300 batches करणारी brewery दोन आठवड्यांत fermentation ची जितकी उदाहरणे गोळा करते, तितक्या harvest dates ती वायनरी एका दशकातही गोळा करत नाही. ही vendor किंवा वायनरीवरची टीका नाही. हा व्यवसायाचा आकार आहे, आणि म्हणूनच बरेच वायनरी AI demo मध्ये तेजस्वी दिसते आणि दुसऱ्या हंगामात सामान्य.

**The Cellar Ledger** मधील ही शेवटची पोस्ट आहे. पहिल्या पाच पोस्ट data foundation बांधण्याबद्दल होत्या. ही त्यावर तुम्ही प्रामाणिकपणे काय बांधू शकता याबद्दल आहे.

## दहा rows तुम्हाला कसे फसवतात

दहा rows आणि मोजक्या features (growing degree days, पाऊस, काही berry मोजमापे) असताना जवळजवळ कोणतेही model भूतकाळाशी जवळून fit होऊ शकते. समस्या हीच आहे. दहा बिंदूंशी जवळचा fit म्हणजे बहुतेक स्मृती. model ने कोणते वर्ष कोणते हे शिकले आहे, vineyard कसे काम करते हे नाही.

wine मध्ये तीन गोष्टी हे आणखी वाईट करतात:

- **हवामान बदलत आहे.** training set मधील दहा वर्षे पुढच्या दहा वर्षांचा न्याय्य नमुना नाहीत. तापमानवाढीचा कल म्हणजे पुढचे vintage, रचनेनेच, model ने पाहिलेल्या श्रेणीबाहेर असते.
- **vineyard बदलते.** वेली म्हाताऱ्या होतात, blocks पुन्हा लावले जातात, irrigation आणि canopy पद्धती बदलतात. block चे दहावे vintage हा त्याच्या पहिल्या vintage इतका तोच block नसतो.
- **target मऊ आहे.** harvest date हा अंशतः निर्णय असतो, हवामान अंदाज, तोडणी करणारे मजूर आणि tank मधील जागा यांनी घडवलेला. quality scores म्हणजे panel चा निर्णय. निर्णय भाकीत करण्यासाठी model train करणे म्हणजे जुने निर्णय, सवयींसकट, पुन्हा निर्माण करणे.

अशा model ची प्रामाणिक चाचणी म्हणजे leave-one-vintage-out: नऊ वर्षांवर train करा, दहावे भाकीत करा, प्रत्येक वर्षासाठी पुन्हा करा. त्यातही एक अडचण आहे. दहा folds त्रुटीचाच गोंगाटी अंदाज देतात, म्हणून winemaker च्या ढोबळ नियमापेक्षा थोडे चांगले दिसणारे model प्रत्यक्षात अजिबात चांगले नसू शकते.

## rows प्रत्यक्षात कुठे आहेत

चांगली बातमी अशी की वायनरीकडे डेटाची कमतरता नाही. vintages ची कमतरता आहे. प्रत्येक हंगामाच्या आत भरपूर आहे:

- **fermentation curves.** प्रत्येक tank म्हणजे स्वतःचे fermentation, दिवसातून अनेकदा density आणि तापमान नोंदवलेले. वर्षाला 120 ferments असलेल्या वायनरीकडे दहा वर्षांनंतर 1,200 curves असतात, प्रत्येकीत शेकडो बिंदू. निरोगी ferment कसा दिसतो हे शिकायला आणि मंदावलेला ferment लवकर flag करायला ते पुरेसे आहे, आणि [fermentation control पोस्ट]({{ '/2024/ai-wine-fermentation-control/' | relative_url }}) याच विषयावर आहे.
- **sensor streams.** tank तापमाने, cellar मधील आर्द्रता, barrel room ची स्थिती. सतत येणारा डेटा, anomaly detection आणि soft sensors साठी चांगला.
- **पिकण्याच्या काळातील berry sampling.** हंगामभर प्रत्येक block साठी साप्ताहिक Brix, acid आणि pH. vintage चा परिणाम सुरुवातीपासून भाकीत करायला पुरेसे नाही, पण या हंगामाची पिकण्याची curve मागील काहींशी तुलना करत पाहायला पुरेसे.
- **मजकूर.** tasting notes, cellar logs, work orders, adjustment कारणे. वर्षानुवर्षांचा, बहुतेक न वाचलेला. इथे large language models खरोखर चमकतात.

नमुना असा: **हंगामाच्या आतील dynamics** शिकणाऱ्या models कडे खरा डेटा असतो. **हंगामांपलीकडील परिणाम** शिकणाऱ्या models कडे बहुतेक नसतो.

## तुटपुंज्या डेटाचा पुरेपूर वापर

जेव्हा vintages पलीकडे भाकीत करावेच लागते, तेव्हा मोठ्या model पेक्षा काही तंत्रे जास्त मदत करतात.

**blocks एकत्र करा.** hierarchical (mixed-effects) model प्रत्येक block ला वेगळे राहू देत blocks मध्ये माहिती वाटून घेते. चाळीस blocks गुणिले दहा vintages म्हणजे चारशे स्वतंत्र rows नव्हेत, पण दहापेक्षा खूपच चांगले.

**विज्ञानापासून सुरुवात करा.** उष्णता संचयावर आधारित phenology models, [ripeness prediction]({{ '/2024/predicting-grape-ripeness-harvest-date/' | relative_url }}) मागचेच growing degree day तर्क, आपल्यासोबत दशकांचे viticulture संशोधन आणतात. दहा बिंदूंवरून वनस्पतिशास्त्र शोधायला सांगण्याऐवजी डेटाला भक्कम model समायोजित करू द्या.

**vintage नव्हे, हंगाम भाकीत करा.** April मध्ये harvest date भाकीत करण्याऐवजी, berry samples येतील तसा दर आठवड्याला ripening forecast update करा. प्रत्येक आठवड्याचा sample ही नवी row आहे, आणि forecast ला फक्त काही आठवडे पुढे पोहोचायचे असते.

**प्रादेशिक आणि सार्वजनिक डेटा वापरा.** weather station च्या नोंदी, प्रादेशिक harvest reports आणि satellite vegetation indices कोणत्याही एका वायनरीच्या नोंदींपेक्षा जास्त वर्षे आणि जास्त vineyards व्यापतात.

## नवे tools काय करू शकतात आणि काय नाही

2026 मधील स्पष्ट प्रश्न असा आहे की AI ची नवी पिढी हे बदलते का. अंशतः.

**time-series foundation models** (Chronos किंवा TimesFM सारखी models, असंबंधित series च्या प्रचंड संख्येवर pretrain केलेली) कधीही न पाहिलेल्या curve चा zero-shot forecast करू शकतात. fermentation curve साठी हे उपयुक्त आहे: पहिल्या तीन दिवसांवरून पुढच्या दोन दिवसांचा वाजवी forecast, तुमच्या डेटावर कोणतेही training न करता. vintage च्या परिणामासाठी त्यांच्याकडे काम करायला काहीच नसते. curves साधारणपणे कशा दिसतात हे त्यांना माहीत असते. तुमचे vineyard त्यांना माहीत नसते.

**synthetic data** छोट्या डेटावरचा उपाय म्हणून अनेकदा सुचवला जातो. तो असू शकत नाही. तुमच्या दहा खऱ्या vintages वरून तयार केलेल्या synthetic vintages मध्ये अशी कोणतीही माहिती नसते जी त्या दहांमध्ये आधीच नव्हती. ते pipeline तपासायला किंवा टोकाच्या परिस्थितींविरुद्ध model ची stress-test घ्यायला मदत करू शकतात, पण ते model ला द्राक्षांबद्दल काहीही नवे शिकवत नाहीत.

**LLMs** मजकुरासोबत अप्रतिम आहेत: दहा वर्षांच्या cellar logs चा सारांश, tasting-note भाषेचे clustering, तुमच्या SOPs वरील प्रश्नांची उत्तरे, reports चे मसुदे, हे सगळे या मालिकेत आधी आले आहे. harvest date भाकीत करायला सांगितल्यावर LLM आत्मविश्वासपूर्ण वाक्यात एक date देईल. तिथे पोहोचण्यासाठी त्याने तुमच्या डेटामधून काहीही शिकलेले नसेल. demo मध्ये नेमके यावरच लक्ष ठेवा.

## हे कुठे मोडते

**मोठे उत्पादक वेगळे आहेत.** डझनभर estates आणि शेकडो blocks असलेल्या group कडे कितीतरी जास्त rows असतात, आणि vintages पलीकडील models अधिक वाजवी ठरतात. दहा rows ची समस्या एकाच estate साठी सर्वात तीव्र असते.

**हंगामातील models नव्या परिस्थितीत तरीही अपयशी ठरू शकतात.** दहा सामान्य vintages वर train झालेले fermentation model कधीही न पाहिलेल्या heatwave harvest चे ताणाचे नमुने ओळखू शकणार नाही. हंगामातील समृद्ध डेटा असामान्य वर्षांवर लक्ष ठेवण्याची गरज संपवत नाही.

**एकत्रीकरण असे गृहीत धरते की blocks पुरेसे सारखे आहेत.** थंड डोंगरउतारावरचा block आणि उष्ण दरीतला block यांत माहिती वाटली, तर model दोघांनाही अशा सरासरीकडे ओढू शकते जी कोणालाच बसत नाही. एकत्रीकरणाची रचना हा सांख्यिकीय तितकाच viticulture चा निर्णय आहे.

**winemaker चा निर्णयसुद्धा मोजक्या vintages वर train झालेला असतो.** वीस harvests पाहिलेल्या winemaker कडेही वीस rows असतात, जरी त्यांच्यासोबत model कडे नसलेला भरपूर संदर्भ येतो. ध्येय त्या निर्णयाला चांगले पुरावे देणे आहे, कोणत्याही बाजूकडे big data आहे असे भासवणे नाही.

## निष्कर्ष

वायनरी AI vintage ला batch सारखे वागवते तेव्हा मोडते. दहा वर्षे म्हणजे दहा rows, हवामान बदलत आहे, आणि भूतकाळाशी जवळचा fit म्हणजे बहुतेक स्मृती. जिथे डेटा समृद्ध आहे तिथे, हंगामाच्या आत, models बांधा: fermentation curves, sensors, berry sampling आणि वर्षानुवर्षांचा न वाचलेला मजकूर. जिथे vintages पलीकडे भाकीत करावेच लागते तिथे blocks एकत्र करा, विज्ञानापासून सुरुवात करा आणि दर आठवड्याला update करा. नवे tools curves आणि मजकुरासाठी मदत करतात. त्यापैकी कोणीही दहा rows चे हजार करत नाही, आणि जो कोणी वेगळे सांगतो त्याला विचारा की त्याने किती vintages वर train केले.

इथे **The Cellar Ledger** पूर्ण होते. त्याची सुरुवात [तीन उत्तरे देणाऱ्या chatbot]({{ '/mr/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) पासून झाली आणि शेवट इथे होतो, आणि सहाही पोस्ट्समधून जाणारा धागा एकच आहे: GenAI त्याच्या खालच्या data model इतकाच विश्वासार्ह असतो. संपूर्ण मालिका [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे, आणि wine वरील व्यापक संग्रह [Winemaking &amp; AI track]({{ '/mr/tracks/winemaking-ai/' | relative_url }}) वर आहे.

## वारंवार विचारले जाणारे प्रश्न

**brewery पेक्षा वायनरीत machine learning कठीण का आहे?**
कारण शिकण्याचे एकक बहुतेकदा vintage असते, आणि वायनरीला वर्षाला एकच मिळते. harvest date, yield किंवा quality score सारख्या प्रश्नांसाठी दहा वर्षांचा इतिहास प्रत्येक block साठी दहा rows देतो, तर वर्षाला शेकडो batches बनवणाऱ्या brewery कडे हजारो असतात. दहा rows वर train झालेली models भूतकाळातून शिकण्याऐवजी बहुतेक तो पाठ करतात.

**synthetic data किंवा foundation model छोटा वायनरी dataset दुरुस्त करू शकतो का?**
स्वतःहून नाही. तुमच्या दहा vintages वरून बनवलेल्या synthetic data मध्ये अशी कोणतीही माहिती नसते जी त्या दहा vintages मध्ये आधीच नव्हती. time-series foundation models fermentation सारख्या curve चा वाजवी zero-shot forecast देऊ शकतात, पण त्यांना तुमच्या vineyard बद्दल काहीच माहीत नसते. भक्कम रचनेत दोन्ही उपयुक्त आहेत, आणि दोघांपैकी कोणीही हरवलेला इतिहास निर्माण करत नाही.

**वायनरीत AI खरोखर कुठे चालते?**
जिथे एकाच हंगामात डेटा समृद्ध असतो तिथे: प्रत्येक tank ची fermentation curve, cellar मधील sensor streams, पिकण्याच्या काळातील berry sampling, आणि tasting notes व cellar logs सारखा मुक्त मजकूर. ferment ची dynamics शिकणाऱ्या models कडे, किंवा logs वाचणाऱ्या LLM कडे, वर्षाला शेकडो किंवा हजारो उदाहरणे असतात.
