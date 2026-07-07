---
layout: post
lang: mr
title: "Pilot ते पूर्ण Scale: NPD ची ती डेटा समस्या जिच्याबद्दल कोणी इशारा देत नाही"
image: /assets/og/npd-scale-up-pilot-to-production-data.png
description: "pilot kettle वर परिपूर्ण असणारी बिअर पूर्ण scale वर spec-बाहेर भरकटू शकते. AB InBev, SABMiller आणि United Breweries साठी बिअर विकसित करताना scale-up दरी भरून काढायला मी batch डेटा, control charts आणि AI कसे वापरले ते इथे आहे."
date: 2026-05-29
updated: 2026-05-29
permalink: /mr/2026/npd-scale-up-pilot-to-production-data/
tags: [beer-npd, brewing-science, scale-up, data-science]
faq:
  - q: "pilot पेक्षा पूर्ण scale वर बिअरची चव वेगळी का लागते?"
    a: "मोठी भांडी भौतिकशास्त्र बदलतात: hop utilisation, boil ची तीव्रता, आणि खासकरून उंच cylindroconical tanks मधील fermentation — तापमान gradients, hydrostatic दाब आणि CO2 scrubbing हे सर्व ester व attenuation रूपरेषा pilot निकालापासून दूर सरकवतात."
  - q: "एक pilot बिअर production scale वर कशी वागेल हे AI वर्तवू शकते का?"
    a: "अंशतः. मागील scale-ups वर प्रशिक्षित मॉडेल परिचित styles व परिचित plant साठी सरकावण्याची संभाव्य दिशा आणि आकार वर्तवू शकते, म्हणून तुम्ही पहिल्या पूर्ण batch आधी रेसिपी समायोजित करता. नवीन style किंवा ज्यावर इतिहास नाही अशा भांड्यासाठी ते कितीतरी कमी विश्वासार्ह असते."
  - q: "production मध्ये नवीन बिअर स्थिर व्हायला किती batches लागतात?"
    a: "ते बदलते, पण पहिल्या काही पूर्ण-scale batches जवळपास नेहमीच भरकटतात; प्रत्येक batch वरील statistical process control हाच एकवटण्याचा मार्ग. डेटा ती शिकण्याची वळणवाट लहान करतो — तो ती काढून टाकत नाही."
---

**थोडक्यात उत्तर: नवीन उत्पादन विकासातील सर्वांत क्रूर धक्का म्हणजे pilot kettle वर परिपूर्ण केलेली बिअर पूर्ण scale वर चुकीची निघू शकते. मोठ्या भांड्याचे भौतिकशास्त्र हे लहानाचे भौतिकशास्त्र नसते. batch डेटा, control charts आणि AI ने मला scale-up सरकाव वर्तवायला आणि पहिल्या production runs मध्ये अधिक जलद एकवटायला मदत केली — पण पहिल्या काही batches अजूनही भरकटतात, आणि डेटा ती वळणवाट लहान करतो, मिटवत नाही.** NPD चा ज्याबद्दल कोणी इशारा देत नाही तो भाग इथे आहे.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 820 340" width="100%" style="max-width:820px;height:auto" role="img" aria-label="एक control chart जे pilot batch लक्ष्यावर दाखवते, पहिल्या पूर्ण-scale batches spec पट्ट्याबाहेर भरकटताना, मग पुढील batches मध्ये प्रक्रिया दुरुस्त होत असताना त्या आत परत एकवटताना दाखवते."><rect x="0" y="0" width="820" height="340" fill="#ffffff"/><text x="410" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">SCALE-UP दरी</text><rect x="90" y="120" width="680" height="80" fill="#f0f6f5" opacity="0.6"/><line x1="90" y1="160" x2="770" y2="160" stroke="#4a6b64" stroke-width="1.4" stroke-dasharray="5 4"/><text x="96" y="114" font-family="sans-serif" font-size="11.5" fill="#4a6b64">वरची spec</text><text x="96" y="214" font-family="sans-serif" font-size="11.5" fill="#4a6b64">खालची spec</text><text x="778" y="164" font-family="sans-serif" font-size="11" fill="#4a6b64">लक्ष्य</text><g stroke="#06483f" stroke-width="1.4"><line x1="90" y1="60" x2="90" y2="270"/><line x1="90" y1="270" x2="780" y2="270"/></g><polyline points="130,160 220,96 310,92 400,128 490,150 580,156 670,159 740,160" fill="none" stroke="#06483f" stroke-width="2.6"/><g fill="#06483f"><circle cx="130" cy="160" r="5"/><circle cx="220" cy="96" r="5"/><circle cx="310" cy="92" r="5"/><circle cx="400" cy="128" r="5"/><circle cx="490" cy="150" r="5"/><circle cx="580" cy="156" r="5"/><circle cx="670" cy="159" r="5"/><circle cx="740" cy="160" r="5"/></g><text x="130" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#4a6b64">pilot</text><text x="265" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">पहिल्या पूर्ण batches भरकटतात</text><text x="660" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#00695c">दुरुस्त आणि स्थिर</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">pilot लक्ष्यावर; पहिल्या पूर्ण-scale batches spec बाहेर भरकटतात, मग प्रक्रिया batch दर batch दुरुस्त होत एकवटतात.</figcaption>
</figure>

## मोठे kettle म्हणजे वेगळी बिअर

तुम्ही pilot ला मंजुरी देता, सगळे खूश होतात, आणि मग पहिला पूर्ण-scale brew थोडा गडद, थोडा अधिक कडू, आणि पॅनेलला न ओळखता येणाऱ्या ester रूपरेषेसह उतरतो. काहीही चुकीचे केले नव्हते. plant ही फक्त एक वेगळी भौतिक प्रणाली आहे, आणि [एखादी रेसिपी scale up करणे]({{ '/mr/2022/scaling-homebrew-recipe-to-production/' | relative_url }}) हीच ती जागा जिथे अनेक आशादायक बिअर शांतपणे मरतात.

कारणे शुद्ध process engineering आहेत. hop utilisation kettle आकार व boil तीव्रतेनुसार बदलतो, म्हणून तोच hop bill वेगळा IBU देतो. सर्वांत महत्त्वाचे, उंच cylindroconical tank मधील fermentation हे pilot भांड्यातील fermentation नसते: hydrostatic दाब, वरून-खाली तापमान gradients, आणि CO₂ scrubbing हे सर्व यीस्टला वेगळ्या ester व attenuation रूपरेषेकडे ढकलतात. रेसिपी सारखीच आहे; बिअर नाही.

## scale-up ला एक भविष्यवाणी समस्या म्हणून हाताळणे

जुना मार्ग म्हणजे पूर्ण batch brew करून शोधणे. महाग, कारण पूर्ण scale वर एक चुकलेली batch म्हणजे हजारो लिटर. म्हणून मी ते पुनर्रचले: scale-up ही एक भविष्यवाणी समस्या आहे, आणि माझ्याकडे शिकण्यासाठी इतिहास होता — pilot ते plant पर्यंतचे प्रत्येक मागील स्थलांतर, त्याने केलेल्या सरकावासह.

त्या मागील scale-ups वर प्रशिक्षित मॉडेल परिचित भांड्यांवरील परिचित style साठी दरीची *दिशा आणि ढोबळ आकार* वर्तवू शकले — हा hop bill या kettle वर काही IBU वाढवेल, हे fermentation tank ४ मध्ये अधिक ester फेकेल. त्यामुळे मला पहिल्या production brew नंतरऐवजी आधी रेसिपी पूर्व-समायोजित करता आली. त्याने दरी नाहीशी केली नाही, पण मला चुकीच्या जागेपासून सुरुवात करण्यापासून थांबवले.

त्याखाली, नेहमीप्रमाणे, काम data science होते: plant process variables सुसंगतपणे नोंदवणे — knockout तापमाने, tank भूमिती, खऱ्या fermentation curves — आणि प्रत्येक production batch ला तिच्या pilot शी जोडणे. त्या वंशावळीशिवाय शिकण्यासारखे काही नाही.

## batch दर batch एकवटणे

भविष्यवाणी तुम्हाला जवळ आणते; statistical process control तुम्हाला स्थिर करते. एक नवीन बिअर production मध्ये आल्यावर मी प्रत्येक critical parameter [control charts वर]({{ '/mr/2023/tableau-qc-control-charts-brewing/' | relative_url }}) batch दर batch मागोवा घेतला, प्रक्रिया स्थिरावत असल्याचे दर्शवणाऱ्या भरकटीवर लक्ष ठेवत. त्याला [brewhouse yield अॅनालिटिक्सशी]({{ '/mr/2023/brewhouse-yield-loss-analytics/' | relative_url }}) जोडा आणि तुम्ही केवळ batch हलली एवढेच नव्हे, तर तोटा किंवा सरकाव कुठून आला तेही पाहू शकता.

Generative AI आता यावर स्वाभाविकपणे बसते. जेव्हा एखादी batch control limit ओलांडते, तेव्हा LLM copilot त्या batch चे process record spec-मधील batches विरुद्ध काढू शकते आणि एक साध्या-भाषेतील पहिले गृहीतक मसुदा करू शकते — "attenuation कमी, fermentation tank च्या खालच्या तिसऱ्या भागात अधिक थंड चालले" — आणि deviation report व सुधारित scale-up SOP स्वयं-मसुदा करू शकते. ब्रूअरच्या तपासासाठी हा एक वेगवान सुरुवातीचा बिंदू आहे, निकाल नव्हे. ब्रूअर अजूनही कारण पक्के करतो.

## हे कुठे मोडते

मॉडेल त्यामागील plant इतिहासाइतकेच चांगले असते. एक अगदी नवीन style, ज्याला त्याने कधी पाहिले नाही असे भांडे, किंवा मागील स्थलांतरांच्या टप्प्याबाहेरील रेसिपी, आणि scale-up भविष्यवाणी म्हणजे confidence interval घातलेला एक अंदाज. ते परिचित सरकाव चांगले वर्तवते आणि अभूतपूर्व वाईट — आणि अशा-प्रकारची-पहिली बिअर म्हणजे नेमके ते अभूतपूर्व प्रकरण.

ते अमूर्त गोष्टीही जाणवू शकत नाही. Mouthfeel, पिण्याची सुलभता, पूर्ण-scale आवृत्तीने pilot ची मोहकता गमावली आहे ती नाव न देता येणारी जाणीव — यातील काहीही control chart वर नसते. आकडे पुन्हा spec च्या आत असू शकतात आणि तरीही बिअर तुम्ही मंजूर केलेली नसते. ती शेवटची दरी भरून काढणे म्हणजे निर्णय, आणि तो [माझा करायचा]({{ '/mr/2026/from-brewer-to-data-scientist/' | relative_url }}) राहिला.

## सारांश

scale-up हीच ती जागा जिथे नवीन उत्पादन विकास जिंकला किंवा हरला जातो, आणि ती निरंतरपणे एक डेटा समस्या आहे: मागील स्थलांतरांवरून सरकाव वर्तवा, मग जिवंत batches वर process control ने एकवटा. AI आणि अॅनालिटिक्सने ती शिकण्याची वळणवाट लहान केली आणि मी अन्यथा वाया घालवले असते असे पूर्ण-scale brews वाचवले. पण ते वळणवाट लहान करतात; ती काढून टाकत नाहीत. पहिल्या batches अजूनही भरकटतात, आणि scale-up केलेली बिअर अखेर *बरोबर* आहे — केवळ spec मध्ये नव्हे — हा निर्णय प्रत्येक वेळी ब्रूअरचा. ते, तीन पोस्टांत मिळून, माझ्या विकसित केलेल्या बिअरमागील आकड्यांचे डेटाने कसे विश्लेषण केले ते आहे: त्याने क्षेत्र अरुंद केले, trials वेगवान केल्या, आणि scale-up आटोक्यात आणला — तर निर्णय माणसाकडेच राहिला.

*Beer NPD with Data — ३ पैकी भाग ३. [संपूर्ण मालिका]({{ '/mr/series/beer-npd/' | relative_url }}) · [मागील: रेसिपी आणि सेन्सरी डेटा]({{ '/mr/2026/npd-recipe-sensory-data-development/' | relative_url }})*

## वारंवार विचारले जाणारे प्रश्न

**pilot पेक्षा पूर्ण scale वर बिअरची चव वेगळी का लागते?**
मोठी भांडी भौतिकशास्त्र बदलतात: hop utilisation, boil ची तीव्रता, आणि खासकरून उंच cylindroconical tanks मधील fermentation — तापमान gradients, hydrostatic दाब आणि CO₂ scrubbing हे सर्व ester व attenuation रूपरेषा pilot निकालापासून दूर सरकवतात.

**एक pilot बिअर production scale वर कशी वागेल हे AI वर्तवू शकते का?**
अंशतः. मागील scale-ups वर प्रशिक्षित मॉडेल परिचित styles व परिचित plant साठी सरकावण्याची संभाव्य दिशा आणि आकार वर्तवू शकते, म्हणून तुम्ही पहिल्या पूर्ण batch आधी रेसिपी समायोजित करता. नवीन style किंवा ज्यावर इतिहास नाही अशा भांड्यासाठी ते कितीतरी कमी विश्वासार्ह असते.

**production मध्ये नवीन बिअर स्थिर व्हायला किती batches लागतात?**
ते बदलते, पण पहिल्या काही पूर्ण-scale batches जवळपास नेहमीच भरकटतात; प्रत्येक batch वरील statistical process control हाच एकवटण्याचा मार्ग. डेटा ती शिकण्याची वळणवाट लहान करतो — तो ती काढून टाकत नाही.
