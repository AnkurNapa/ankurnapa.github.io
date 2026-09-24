---
layout: post
lang: mr
title: "OpEx साठी AI चा roadmap, आणि तो कुठे मोडतो: आधी data, loss च्या मूल्यानुसार pilots, प्रामाणिक ROI आणि AGI चा गाजावाजा"
image: /assets/og/ai-opex-roadmap-where-it-breaks-agi-hype.png
description: "Beverage plants मधील Operational Excellence साठी AI, भाग 8. Beverage plant मध्ये AI चा क्रम कसा लावायचा: आधी data चा पाया, loss च्या मूल्यानुसार निवडलेले pilots, baseline च्या तुलनेत मोजलेला ROI, shop floor वरील change management, आणि AGI च्या चर्चेने काय बदलावे आणि काय बदलू नये याची स्पष्ट समज. या लेखाने मालिका संपते."
date: 2026-09-23 09:00:00 -0700
updated: 2026-09-23
permalink: /mr/2026/ai-opex-roadmap-where-it-breaks-agi-hype/
tags: [brewing-science, ai-opex, ai-strategy, operational-excellence, generative-ai]
faq:
  - q: "Beverage plant ने AI ची सुरुवात कुठून करावी?"
    a: "Data च्या पायापासून: विश्वासार्ह stop codes, समान asset आणि batch keys वर जोडलेले MES, historian, CMMS आणि LIMS, आणि OEE व six big losses च्या मान्य व्याख्या. मग सर्वात जास्त किमतीच्या loss वर एक pilot निवडा, आणि तो सोडवू शकणारी AI च्या शिडीची सर्वात खालची पायरी वापरा. Generative AI आणि agents नंतर येतात, त्याच data वर उभे राहून."
  - q: "Plant मधील AI project चा ROI कसा मोजायचा?"
    a: "Baseline च्या तुलनेत, आधी भौतिक एककांमध्ये. Pilot आधीचा loss नोंदवा, pilot चालवा, आणि मिनिटे, bottles, kilowatt hours किंवा litres मधील बदल मोजा, शक्य असल्यास हा बदल न मिळालेल्या तुलनीय line च्या तुलनेत. पैशात रूपांतर फक्त शेवटी करा, आणि data चे काम व लोकांचा वेळ धरून सर्व खर्च मोजा."
  - q: "AI मध्ये गुंतवणूक करण्याआधी plant ने AGI ची वाट पाहावी का?"
    a: "नाही. AGI अस्तित्वात नाही, ती केव्हा येईल किंवा येईल की नाही हे कुणीच सांगू शकत नाही, आणि आजचा प्रत्येक उपयुक्त AI project स्वच्छ data, जोडलेल्या systems आणि स्पष्ट मंजुऱ्यांवर अवलंबून आहे. भविष्यातील कोणत्याही system लाही नेमके हेच लागेल. वाट पाहण्याची किंमत म्हणजे त्या दरम्यान तुम्ही वाचवू शकला असता ते losses."
---

**थोडक्यात उत्तर: तंत्रज्ञानापेक्षा क्रम जास्त महत्त्वाचा आहे. पहिले, data चा पाया दुरुस्त करा: लोकांचा विश्वास असलेले stop codes, जोडलेले historian, MES, CMMS आणि LIMS, आणि OEE ची एकच मान्य व्याख्या. दुसरे, loss च्या मूल्यानुसार एक pilot निवडा, तो सोडवू शकणाऱ्या AI च्या सर्वात खालच्या पायरीवर. एका shift मध्ये 300,000 bottles बनवणाऱ्या उदाहरणादाखल line वर OEE चा एक point म्हणजे shift ला 3,000 bottles, आणि तीन shifts मध्ये वर्षाला सुमारे 2.7 million. तिसरे, कुणी त्याचे पैशात रूपांतर करण्याआधी भौतिक एककांमध्ये baseline च्या तुलनेत मोजा. चौथे, plant मधील मजकुरासाठी generative AI आणि कृती न करता मसुदे बनवणारे agents जोडा. आणि AGI कडे वाट पाहण्याचे कारण म्हणून नव्हे, तर लक्ष ठेवण्याजोगी बातमी म्हणून पाहा.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Beverage plant मधील AI साठी चार टप्प्यांचा roadmap, सुमारे एका वर्षाची उदाहरणादाखल वेळ. टप्पा 1, पाया: stop codes, जोडलेल्या systems, OEE च्या व्याख्या. टप्पा 2, loss च्या मूल्यानुसार निवडलेला classic AI pilot, जसे predictive maintenance किंवा anomaly detection. टप्पा 3, मजकुरासाठी generative AI: handovers, SOP उत्तरे, root-cause मदत. टप्पा 4, autonomy स्तर 2 वरील agent जो work orders आणि changeover plans चा मसुदा बनवतो. खाली सलग एक पट्टा चालतो: baseline च्या तुलनेत मोजा, आणि shop floor ला सोबत घ्या.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATA ने सुरू होऊन AGENTS वर संपणारा ROADMAP (उदाहरणादाखल वेळ)</text>
<g font-family="sans-serif">
<rect x="40" y="60" width="215" height="150" rx="10" fill="#06483f"/>
<text x="147" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">1. पाया</text>
<text x="147" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">महिने 0 ते 3</text>
<text x="147" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">विश्वासार्ह stop codes</text>
<text x="147" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">MES, historian, CMMS जोडलेले</text>
<text x="147" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">OEE ची एकच व्याख्या</text>
<rect x="270" y="60" width="215" height="150" rx="10" fill="#00695c"/>
<text x="377" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">2. Classic AI pilot</text>
<text x="377" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">महिने 3 ते 6</text>
<text x="377" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">loss च्या मूल्यानुसार निवड</text>
<text x="377" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">predictive maintenance किंवा</text>
<text x="377" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">SPC वर anomaly detection</text>
<rect x="500" y="60" width="215" height="150" rx="10" fill="#4db6a2"/>
<text x="607" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">3. मजकुरासाठी GenAI</text>
<text x="607" y="108" text-anchor="middle" font-size="10.5" fill="#06483f">महिने 6 ते 9</text>
<text x="607" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">shift handovers</text>
<text x="607" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">संदर्भांसह SOP उत्तरे</text>
<text x="607" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">root-cause मदत</text>
<rect x="730" y="60" width="230" height="150" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="845" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">4. L2 वरील agent</text>
<text x="845" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">महिने 9 ते 12</text>
<text x="845" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">work orders चा मसुदा</text>
<text x="845" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">changeover plans चा मसुदा</text>
<text x="845" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">माणूस मंजूर करतो</text>
<rect x="40" y="226" width="920" height="40" rx="10" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="251" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">सुरुवातीपासून शेवटपर्यंत: BASELINE च्या तुलनेत मोजा &#183; SHOP FLOOR ला सोबत घ्या</text>
<text x="500" y="298" text-anchor="middle" font-size="11" fill="#4a6b64">AGI हा या roadmap वरचा टप्पा नाही &#183; इथले सगळे त्याच्याशिवाय चालते</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">एका site साठी उदाहरणादाखल वेळ. मुद्दा क्रमाचा आहे: प्रत्येक टप्पा आधीच्या टप्प्यावर उभा राहतो.</figcaption>
</figure>

मी plant मधील AI projects अयशस्वी होताना कमी आणि रखडताना जास्त पाहिले आहेत. ते क्वचितच वाईट model मुळे मरतात. ते चौथ्या महिन्यात मरतात, जेव्हा team ला कळते की stop codes निरुपयोगी आहेत, maintenance system मधील asset ची नावे MES पेक्षा वेगळी आहेत, आणि planned downtime कशाला म्हणायचे यावर कुणाचेच एकमत नाही. Model तयार होऊन बसलेला असतो, अशा data च्या प्रतीक्षेत जो आपोआप कधीच येणार नव्हता.

**Beverage Plants मधील Operational Excellence साठी AI** या मालिकेतील हा शेवटचा लेख आहे. पहिल्या सात लेखांनी शब्दसंग्रह उभा केला: [AI शिडी]({{ '/mr/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}), [LLMs]({{ '/mr/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}), [agents]({{ '/mr/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), [OEE]({{ '/mr/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}), आणि shop floor वरील [classic AI]({{ '/mr/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), [generative AI]({{ '/mr/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}) व [agentic AI]({{ '/mr/2026/agentic-ai-opex-oee-agent-cmms-guardrails/' | relative_url }}). हा लेख त्यांना क्रमाने लावतो.

## टप्पा 1: आधी data चा पाया

Roadmap मधील पुढचे काहीही यांच्याशिवाय चालत नाही, म्हणून ते आधी येतात, जरी board समोर मांडायला ते सर्वात कमी रोमांचक असले तरी:

- **लोकांचा विश्वास असलेले stop codes.** PLC मधून आपोआप stop ओळख, आणि six big losses शी जुळणारी कारणांची छोटी यादी. फक्त engineers सोबत नव्हे, तर operators सोबत त्याची चाचणी करा.
- **जोडलेल्या systems.** MES, historian, CMMS आणि LIMS समान keys वर जोडलेले: तेच asset IDs, तेच batch किंवा order numbers, तेच घड्याळ. यादीतील हे सहसा सर्वात मोठे काम असते.
- **OEE ची एकच व्याख्या.** Planned time कशाला म्हणायचे, प्रत्येक product आणि format साठी ideal rate किती, हे लिहून प्रसिद्ध केलेले.
- **Data साठी एक जागा.** IT बाजूला एक lakehouse किंवा warehouse, DMZ replica मधून भरले जाणारे, जिथे control network ला हात न लावता data model बांधता येईल.

[Cellar Ledger मधील winery data च्या कामाचाही]({{ '/series/cellar-ledger/' | relative_url }}) हाच धडा होता: कोणत्याही assistant आधी व्याख्या आणि data model येतात.

## टप्पा 2: loss च्या मूल्यानुसार pilot निवडा

Losses मोजलेले असले की pilot ची निवड उत्साहाचा नव्हे, तर गणिताचा प्रश्न बनते. प्रत्येक संभाव्य loss साठी चार प्रश्न विचारा:

1. **त्याची किंमत किती?** दर आठवड्याला गमावलेली मिनिटे किंवा bottles, गुणिले तुमच्यासाठी एका bottle ची किंवा एका मिनिटाची किंमत.
2. **Data तयार आहे का?** Signal अस्तित्वात आहे का, योग्य वारंवारतेने, stop log शी जोडलेला?
3. **तो दुरुस्त करू शकणारी सर्वात खालची पायरी कोणती?** Rule, SPC, model, generative AI किंवा agent.
4. **ते चुकले तर काय होते?** Changeover वरची चुकीची सूचना स्वस्त पडते. Pasteuriser वरचा चुकीचा निर्णय नाही.

प्रमाण लक्षात घेतले की मन केंद्रित होते. लेख 4 मधील उदाहरणादाखल filler line वर ideal output shift ला 300,000 bottles आहे. OEE चा एक point म्हणजे shift ला 3,000 bottles. 300 दिवस तीन shifts मध्ये, ते वर्षाला 2.7 million bottles होतात. त्याला प्रति bottle तुमच्या स्वतःच्या contribution ने गुणा, आणि एका point च्या सुधारणेची किंमत काहीही खर्च करण्याआधीच तुम्हाला कळते.

Pilot सहसा classic AI असतो: सर्वात मोठ्या breakdown loss मागील asset वर predictive maintenance, किंवा सर्वात मोठ्या quality loss मागील process वर anomaly detection. तो अरुंद असावा: एक line, एक asset family, एक loss.

## टप्पा 3: plant मधील मजकुरासाठी generative AI

विश्वासार्ह data layer तयार झाला की generative AI ला उभे राहायला काहीतरी मिळते. Stop log आणि notes मधून मसुदा केलेले shift handovers, संदर्भांसह SOP उत्तरे, आणि कारणे सुचवणारी पण कधीच निष्कर्ष न काढणारी root-cause मदत. हे झपाट्याने पसरतात कारण लोकांना प्रत्येक shift मध्ये वाचलेला वेळ जाणवतो. उरलेले data चे प्रश्नही ते लवकर उघड करतात, कारण वाईट stop codes वर बांधलेला handover उघडपणे चुकीचा वाटतो.

## टप्पा 4: मसुदे बनवणारा agent

आत्ताच agent अर्थपूर्ण ठरतो: लेख 7 मधील OEE loss agent, autonomy स्तर 2 वर, replicated data वाचणारा, माणसाने मंजूर करावेत म्हणून work orders आणि changeover plans चा मसुदा बनवणारा, प्रत्येक tool call नोंदवलेला आणि process control कडे कोणताही मार्ग नसलेला. तो आधीच्या सगळ्यावर उभा राहतो: losses ची क्रमवारी लावण्यासाठी stop codes, stop ला asset शी जोडण्यासाठी जोडलेल्या systems, आणि त्याने काय केले ते कळवण्यासाठी handover.

## प्रामाणिक ROI

Plants मधील AI projects मध्ये उदार गणित करण्याची प्रवृत्ती असते. काही सवयी ते प्रामाणिक ठेवतात:

- **सुरू करण्याआधी baseline मोजा.** Loss जसा आहे तसा चार ते आठ आठवडे, नंतर ज्या पद्धतीने नोंदवाल त्याच पद्धतीने नोंदवलेला.
- **आधी भौतिक एककांमध्ये मोजा.** मिनिटे, bottles, kilowatt hours, पाण्याचे litres, गमावलेल्या product चे kilograms. पैशात रूपांतर फक्त शेवटी, finance team सोबत करा.
- **शक्य तिथे तुलना वापरा.** Pilot न मिळालेली तशीच line दाखवते की बदलापैकी किती भाग ऋतू, product mix किंवा नव्या supervisor मुळे आला.
- **प्रत्येक खर्च मोजा.** Licences आणि compute, हो, पण data engineering, design sessions मधील operators चा वेळ आणि models ची सततची देखभालही.
- **संपूर्ण team ला श्रेय द्या.** बहुतेक वेळा सर्वात मोठा फायदा टप्पा 2 मधील model मुळे नव्हे, तर टप्पा 1 मध्ये stop codes दुरुस्त केल्यामुळे होतो. ते स्पष्ट सांगा.

## Shop floor वरील change management

तंत्रज्ञान हा सोपा भाग आहे. यापैकी काहीही चालेल की नाही ते लोक ठरवतात:

- **Operators सोबत design करा.** कोणते stop codes निरर्थक आहेत आणि कोणत्या alarms कडे सगळे दुर्लक्ष करतात हे त्यांना माहीत असते. पहिल्या आठवड्यापासून त्यांना सहभागी करा.
- **दोष देण्यासाठी कधीच वापरू नका.** Handover summary किंवा loss agent दोषी शोधण्याचे साधन बनले, तर महिन्याभरात data आणखी खराब होईल.
- **Shop floor वर त्याचा एक मालक ठेवा.** फक्त data team नव्हे, तर एखादा production supervisor प्रत्येक tool चा मालक असतो आणि तो बंद करू शकतो.
- **अपयशाच्या प्रकारांसाठी प्रशिक्षण द्या.** Model आत्मविश्वासाने चुकू शकतो, आणि संदर्भ किंवा पुरावा तपासणे हा कामाचाच भाग आहे, हे लोकांना शिकवा.

## AGI चा गाजावाजा विरुद्ध वास्तव

दर काही महिन्यांनी AGI जवळ आली आहे अशी बातमी येते, आणि plant च्या meeting मध्ये कुणीतरी विचारतो की आत्ता गुंतवणूक करावी की सगळे काही करणाऱ्या systems ची वाट पाहावी. प्रामाणिक उत्तराचे तीन भाग आहेत.

आज AGI अस्तित्वात नाही. ती केव्हा येईल किंवा येईल की नाही हे कुणीच विश्वासाने सांगू शकत नाही. आणि या मालिकेतील प्रत्येक उपयुक्त system, vibration model पासून work-order agent पर्यंत, स्वच्छ data, जोडलेल्या systems, स्पष्ट व्याख्या आणि मंजुरी प्रक्रियांवर अवलंबून आहे. भविष्यातील general intelligence वर plant मध्ये विश्वास ठेवायचा झाला तरी तिलाही नेमक्या याच गोष्टी लागतील. काहीही झाले तरी हा पाया वाया जात नाही. उलट, वाट पाहण्याची किंमत ठाऊक आहे: तुम्ही वाचवू शकला असता अशा losses ची प्रत्येक shift.

## हे कुठे मोडते

**टप्पा 1 ला ठरवल्यापेक्षा जास्त वेळ लागतो.** Systems जोडणे आणि codes स्वच्छ करणे याला नेहमीच लागतो. तो वेळ जपा, आणि थेट demo कडे उडी मारण्याच्या दबावाला विरोध करा.

**कधीच न वाढणारे pilots.** एका line वरचा pilot जो चालू ठेवायला data scientist लागतो, तो इतर पाच lines पर्यंत पोहोचणार नाही. दुसरी line सुरुवातीपासूनच plan मध्ये धरा.

**तपासता न येणारे ROI दावे.** Vendor ची बचत baseline च्या तुलनेत मोजलेल्या बदलापर्यंत शोधता येत नसेल, तर तिला marketing समजा.

**Autonomy हळूहळू वाढत जाते.** स्तर 2 वर चांगले वर्ष गेल्यावर agent ला स्वतः कृती करू द्यावी असा दबाव येईल. तो निर्णय चुकीच्या किमतीनुसार जाणीवपूर्वक घ्या, आणि process control त्यापासून दूर ठेवा.

## सारांश

Beverage plant मधील operational excellence साठी AI ही खरेदी नसून एक क्रम आहे. आधी पाया, मग loss च्या मूल्यानुसार निवडलेला आणि चालणाऱ्या सर्वात खालच्या पायरीवरचा एक pilot, मग plant मधील मजकुरासाठी generative AI, मग माणसाने मंजूर करावे म्हणून मसुदे बनवणारा agent. Bottles आणि मिनिटांमध्ये baseline च्या तुलनेत मोजा, shop floor ला सोबत घ्या, आणि AGI ची वाट पाहू नका. Losses आज line वर आहेत, आणि ते वाचवण्यासाठी लागणारे जवळजवळ सगळेही आजच तिथे आहे.

यासह ही मालिका संपते. संपूर्ण यादी [मालिकेच्या पानावर]({{ '/series/ai-operational-excellence/' | relative_url }}) आहे. Data च्या पायाच्या winery आवृत्तीसाठी [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}) पाहा; distillery च्या मूलभूत गोष्टींसाठी [AI Foundations for Distillers]({{ '/series/distilling-ai-foundations/' | relative_url }}); आणि GenAI व data engineering च्या spirit आणि beer बाजूंसाठी [The Still and the Model]({{ '/series/still-and-model/' | relative_url }}) आणि [The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## वारंवार विचारले जाणारे प्रश्न

**Beverage plant ने AI ची सुरुवात कुठून करावी?**
Data च्या पायापासून: विश्वासार्ह stop codes, समान asset आणि batch keys वर जोडलेले MES, historian, CMMS आणि LIMS, आणि OEE व six big losses च्या मान्य व्याख्या. मग सर्वात जास्त किमतीच्या loss वर एक pilot निवडा, आणि तो सोडवू शकणारी AI च्या शिडीची सर्वात खालची पायरी वापरा. Generative AI आणि agents नंतर येतात, त्याच data वर उभे राहून.

**Plant मधील AI project चा ROI कसा मोजायचा?**
Baseline च्या तुलनेत, आधी भौतिक एककांमध्ये. Pilot आधीचा loss नोंदवा, pilot चालवा, आणि मिनिटे, bottles, kilowatt hours किंवा litres मधील बदल मोजा, शक्य असल्यास हा बदल न मिळालेल्या तुलनीय line च्या तुलनेत. पैशात रूपांतर फक्त शेवटी करा, आणि data चे काम व लोकांचा वेळ धरून सर्व खर्च मोजा.

**AI मध्ये गुंतवणूक करण्याआधी plant ने AGI ची वाट पाहावी का?**
नाही. AGI अस्तित्वात नाही, ती केव्हा येईल किंवा येईल की नाही हे कुणीच सांगू शकत नाही, आणि आजचा प्रत्येक उपयुक्त AI project स्वच्छ data, जोडलेल्या systems आणि स्पष्ट मंजुऱ्यांवर अवलंबून आहे. भविष्यातील कोणत्याही system लाही नेमके हेच लागेल. वाट पाहण्याची किंमत म्हणजे त्या दरम्यान तुम्ही वाचवू शकला असता ते losses.
