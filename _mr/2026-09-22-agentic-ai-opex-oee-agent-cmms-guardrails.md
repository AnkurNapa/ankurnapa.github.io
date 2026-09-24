---
layout: post
lang: mr
title: "OpEx साठी Agentic AI: work orders चा मसुदा बनवणारा OEE loss agent, आणि त्याला PLC पासून दूर ठेवणारे guardrails"
image: /assets/og/agentic-ai-opex-oee-agent-cmms-guardrails.png
description: "Beverage plants मधील Operational Excellence साठी AI, भाग 7. प्रत्येक shift मध्ये OEE losses वर लक्ष ठेवणारा, वारंवार येणारे faults शोधणारा, CMMS तपासणारा आणि लोकांनी मंजूर करण्यासाठी work orders व changeover plans चा मसुदा बनवणारा agent. सोबत महत्त्वाचे guardrails: Purdue model, OT data ला फक्त read-only प्रवेश, PLC किंवा SCADA मध्ये कोणतेही write नाही, मंजुरी, audit log आणि replay evals."
date: 2026-09-22 09:00:00 -0700
updated: 2026-09-22
permalink: /mr/2026/agentic-ai-opex-oee-agent-cmms-guardrails/
tags: [brewing-science, ai-opex, agentic-ai, predictive-maintenance, ot-security]
faq:
  - q: "Beverage plant मध्ये AI agent सुरक्षितपणे काय करू शकतो?"
    a: "Production, maintenance आणि quality data वाचणे, कोणते losses महत्त्वाचे आहेत ते ठरवणे, आणि लोकांसाठी कृतींचा मसुदा बनवणे: maintenance work orders, changeover plans, shift summaries, planner ला संदेश. प्रत्येक मसुद्यासोबत त्याचा पुरावा असतो आणि तो मंजुरीची वाट पाहतो. PLCs, SCADA किंवा process setpoints मध्ये लिहिण्याचा कोणताही मार्ग त्याच्याकडे नसावा."
  - q: "Purdue model म्हणजे काय आणि AI agents साठी तो का महत्त्वाचा आहे?"
    a: "Purdue model ही एक reference architecture आहे जी plant चे networks स्तरांमध्ये विभागते: तळाशी प्रत्यक्ष process आणि त्याचे controllers, सर्वात वर business systems, आणि operations व enterprise IT यांच्यामध्ये एक demilitarised zone. Agent ची जागा IT बाजूला आहे, जिथे तो DMZ मधील replicated data वाचतो. त्याने control स्तरांमध्ये खाली कधीही connection उघडू नये."
  - q: "AI agent ला plant वर मोकळे सोडण्याआधी त्याची चाचणी कशी करायची?"
    a: "इतिहास replay करा. गेल्या एक किंवा दोन महिन्यांच्या shifts वर, त्या वेळी जसा data होता तसाच वापरून agent चालवा, आणि त्याच्या मसुद्यांची तुलना planners आणि engineers नी प्रत्यक्षात जे केले त्याच्याशी करा. त्याने किती खरे प्रश्न पकडले, किती मसुदे निव्वळ गोंगाट होते, आणि किती चुकीचे ठरले असते ते मोजा. Model, prompts किंवा tools बदलतील तेव्हा प्रत्येक वेळी replay पुन्हा करा."
---

**थोडक्यात उत्तर: beverage plant मधील सर्वात उपयुक्त agent हा robot operator नसतो. तो एक संयमी analyst असतो जो प्रत्येक shift च्या शेवटी stop log वाचतो, OEE losses ची क्रमवारी लावतो, labeller चे glue unit या आठवड्यात सहा वेळा line थांबवून गेले आहे हे लक्षात घेतो, maintenance system तपासतो, कोणताही उघडा work order नाही हे पाहतो आणि planner ने मंजूर करावा म्हणून पुराव्यासह एक work order चा मसुदा बनवतो. हाच agent flush time कमी करणाऱ्या changeover क्रमाचाही मसुदा बनवू शकतो. त्याला सुरक्षित बनवतो तो model नव्हे, तर architecture: Purdue model च्या IT बाजूला replicated OT data ला read-only प्रवेश, PLCs किंवा SCADA कडे कोणताही मार्ग नाही, फक्त मसुदे तयार करणारी write tools, प्रत्येक tool call चा audit log, आणि live होण्याआधी replay चाचण्या.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Purdue model आणि त्यावर ठेवलेला एक AI agent. तळाशी स्तर 0 ते 2 मध्ये process, PLCs आणि SCADA आहेत. स्तर 3 मध्ये historian, MES आणि CMMS आहेत. DMZ मध्ये historian आणि MES data ची read-only replica आहे. स्तर 4 आणि 5 मध्ये enterprise IT आहे, जिथे agent चालतो. Agent DMZ replica मधून वाचतो आणि CMMS मध्ये फक्त work orders चे मसुदे लिहितो, जे planner मंजूर करतो. Agent पासून PLCs आणि SCADA कडे जाणारा काट मारलेला बाण दाखवतो की process control मध्ये लिहिण्याचा त्याला कोणताही मार्ग नाही. Audit log प्रत्येक tool call नोंदवतो.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">AGENT कुठे राहतो, आणि तो कुठपर्यंत पोहोचू शकतो</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="600" height="62" rx="9" fill="#06483f"/>
<text x="60" y="76" font-size="11" font-weight="700" fill="#cfe6df">स्तर 4-5 &#183; ENTERPRISE IT</text>
<rect x="330" y="60" width="160" height="42" rx="8" fill="#ffffff"/>
<text x="410" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">OEE loss agent</text>
<rect x="40" y="124" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="60" y="148" font-size="11" font-weight="700" fill="#00695c">DMZ</text>
<text x="60" y="166" font-size="10.5" fill="#4a6b64">read-only replica: historian tags, MES stops</text>
<rect x="40" y="192" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="60" y="216" font-size="11" font-weight="700" fill="#06483f">स्तर 3 &#183; SITE OPERATIONS</text>
<text x="60" y="234" font-size="10.5" fill="#4a6b64">historian &#183; MES &#183; CMMS &#183; LIMS</text>
<rect x="40" y="260" width="600" height="56" rx="9" fill="#ffffff" stroke="#4a6b64" stroke-width="1.5"/>
<text x="60" y="284" font-size="11" font-weight="700" fill="#06483f">स्तर 0-2 &#183; PROCESS आणि CONTROL</text>
<text x="60" y="302" font-size="10.5" fill="#4a6b64">sensors &#183; PLCs &#183; SCADA &#183; HMIs</text>
<line x1="410" y1="102" x2="410" y2="124" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="425" y="118" font-size="10" fill="#2e9e7c">वाचतो</text>
<path d="M490 81 C560 81 560 220 520 220" fill="none" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="566" y="150" font-size="10" fill="#2e9e7c">फक्त मसुदे</text>
<text x="500" y="224" font-size="10" text-anchor="end" fill="#2e9e7c">CMMS मसुदा</text>
<line x1="345" y1="102" x2="345" y2="260" stroke="#ff4081" stroke-width="2.5" stroke-dasharray="5 4"/>
<line x1="335" y1="244" x2="355" y2="264" stroke="#ff4081" stroke-width="3"/>
<line x1="355" y1="244" x2="335" y2="264" stroke="#ff4081" stroke-width="3"/>
<text x="352" y="188" font-size="10" font-weight="700" fill="#ff4081">control मध्ये write चा मार्ग नाही</text>
<rect x="680" y="50" width="280" height="266" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="820" y="76" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">GUARDRAILS</text>
<g font-size="11" fill="#06483f">
<text x="700" y="106">1. OT data फक्त read-only, DMZ मार्गे</text>
<text x="700" y="134">2. PLC किंवा SCADA मध्ये कधीही write नाही</text>
<text x="700" y="162">3. write tools फक्त मसुदे बनवतात</text>
<text x="700" y="190">4. प्रत्येक मसुदा माणूस मंजूर करतो</text>
<text x="700" y="218">5. प्रत्येक tool call चा audit log</text>
<text x="700" y="246">6. go-live आधी replay evals</text>
<text x="700" y="274">7. step, cost आणि rate मर्यादा</text>
<text x="700" y="302">8. एका switch ने बंद होतो</text>
</g>
<rect x="40" y="330" width="920" height="38" rx="10" fill="#06483f"/>
<text x="500" y="354" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">MODEL चुकू शकतो &#183; ती चूक स्वस्त राहील याची खात्री ARCHITECTURE करते</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Agent business systems सोबत बसतो, plant data ची replica वाचतो आणि फक्त मसुदे तयार करू शकतो. Process control त्याच्या आवाक्याबाहेर आहे, आणि ते जाणूनबुजून तसे रचलेले आहे.</figcaption>
</figure>

प्रत्येक plant मध्ये अशा losses ची एक यादी असते जी सगळ्यांना माहीत असते आणि जिच्या मागे लागायला कुणालाच वेळ नसतो. एका shift मध्ये डझनभर वेळा तीस सेकंदांसाठी थांबणारा labeller. नेहमी वीस मिनिटे जास्त चालणारा changeover. बाहेरचे तापमान 35 अंशांच्या पुढे गेले की trip होणारा pump. प्रत्येक loss लहान असतो. पण एकत्र पाहिले तर [OEE waterfall]({{ '/mr/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}) वरचा सर्वात मोठा खांब बहुतेक वेळा तोच असतो.

या मालिकेतील [तिसऱ्या लेखात]({{ '/mr/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}) agents कसे काम करतात ते समजावले होते. हा सातवा लेख एका agent ला याच losses वर कामाला लावतो, आणि त्याच्या भोवतीच्या कुंपणांवर किमान तेवढाच वेळ घालवतो.

## OEE loss agent, टप्प्याटप्प्याने

नीट मर्यादा आखलेला agent प्रत्येक shift च्या शेवटी काय करतो ते असे. प्रत्येक टप्पा म्हणजे एखाद्या चाचणी केलेल्या query ला किंवा नियंत्रित system ला केलेला tool call.

1. **Losses ची क्रमवारी.** MES replica मधून shift चे stops काढा आणि ते six big losses नुसार आणि asset नुसार गटात लावा. Labeller चे glue unit सहा stops मध्ये मिळून 31 मिनिटांसाठी जबाबदार आहे.
2. **पुनरावृत्ती तपासा.** गेल्या दोन आठवड्यांकडे मागे वळून पाहा. तोच fault code 23 वेळा आला आहे, आणि वाढतो आहे.
3. **Asset पाहा.** CMMS ला query करा: glue unit वरचा शेवटचा work order चार आठवड्यांपूर्वी बंद झाला, "cleaned nozzles". आत्ता कोणताही उघडा order नाही.
4. **Signals पाहा.** प्रत्येक stop च्या आसपास historian replica मधून glue temperature tag काढा. बहुतेक stops च्या अगदी आधी ते त्याच्या setpoint band च्या खाली घसरते.
5. **कृतीचा मसुदा.** CMMS मध्ये work order चा मसुदा तयार करा: asset, लक्षण, ते 23 stops, chart link सह temperature pattern, आधीचा work order, सुचवलेली priority. Status: draft, planner च्या प्रतीक्षेत.
6. **अहवाल.** Shift handover मध्ये एक ओळ जोडा: "L2 labeller glue unit साठी draft WO तयार, temperature वारंवार घसरते, link पाहा."

Planner दुसऱ्या दिवशी सकाळी मसुदा पाहतो, priority बदलतो आणि तो release करतो. ज्या कामाला engineer ला एक तास लागला असता ते agent ने दोन मिनिटांत केले, आणि फक्त कुणाला वेळ मिळेल तेव्हा नव्हे, तर प्रत्येक shift मध्ये केले.

## Changeover plans: मसुदा, schedule नव्हे

हाच pattern changeovers साठीही चालतो, जे six big losses पैकी दुसरे आहेत. ERP मधील आठवड्याचा production plan आणि products व formats मधील ज्ञात changeover वेळा दिल्या, तर agent असा run क्रम सुचवू शकतो ज्यात flushes आणि format बदल कमी होतील. फिकट बिअर नंतर गडद, गडद नंतर फिकट नव्हे. 330 ml चे runs एकत्र लावा. Plan मुळे टाळता येण्याजोगा changeover करावा लागत असेल तर तेही तो दाखवू शकतो.

तो मसुदा planner कडे देतो, ज्याला agent ला माहीत नसलेल्या गोष्टी माहीत असतात: गुरुवारी पाठवायलाच हवी अशी customer order, रजेवर असलेला operator, वेळेत तयार न होणारी tank. Planner बदल करतो आणि प्रसिद्ध करतो. Agent live schedule ला कधीच हात लावत नाही.

## Guardrail 1: Purdue model

बहुतेक beverage plants आपले networks Purdue model च्या धर्तीवर आखतात, आणि IEC 62443 सारखी OT security standards याच विभागणीवर उभी आहेत. तळाशी, स्तर 0 ते 2 मध्ये process, PLCs, SCADA आणि HMIs असतात. स्तर 3 मध्ये site operations: historian, MES, CMMS, LIMS. स्तर 4 आणि 5 म्हणजे enterprise IT. Operations आणि IT यांच्यामध्ये एक demilitarised zone, म्हणजे DMZ, असते, जिथे control network उघडे न करता data शेअर करता येतो.

Agent ची जागा IT बाजूला आहे. तो DMZ मध्ये प्रसिद्ध केलेल्या historian आणि MES data ची replica वाचतो. तो स्तर 0 ते 2 मध्ये खाली कधीही connection उघडत नाही. तुमच्या architecture मध्ये तसे करावे लागणार असेल, तर ती architecture अजून agent साठी तयार नाही.

## Guardrail 2: process control मध्ये कोणतेही write नाही

हा मुद्दा स्वतंत्र ओळीचा हक्कदार आहे. **Agent जे काही करेल त्याने PLC, SCADA value किंवा process setpoint बदलता कामा नये.** Tool मधून नाही, script मधून नाही, "फक्त या एका कमी जोखमीच्या parameter साठी" असेही नाही. Process control चांगल्या कारणांसाठी engineer, validate आणि interlock केलेले असते, आणि 98 टक्के वेळा बरोबर असणारे language model अशा loop मध्ये स्वीकारार्ह नाही जिथे उरलेले 2 टक्के म्हणजे caustic line किंवा दाबाखालील vessel असते.

हे लागू करण्याचा सर्वात सोपा मार्ग म्हणजे ते tool कधी बनवायचेच नाही. Agent पोहोचू शकेल अशा कोणत्याही MCP server वर `set_value` function नसेल, आणि त्याच्या service account ला OT च्या आसपास कुठेही write हक्क नसतील, तर हा प्रश्नच उद्भवत नाही.

## Guardrails 3 ते 8: मसुदे, मंजुरी, logs, evals, मर्यादा, off switch

- **Write tools फक्त मसुदे तयार करतात.** CMMS tool draft status मध्ये work order तयार करू शकते. ते तो release करू शकत नाही, बंद करू शकत नाही किंवा release झालेला order बदलू शकत नाही.
- **प्रत्येक मसुदा माणूस मंजूर करतो.** फक्त निष्कर्ष नव्हे, तर पुरावा समोर ठेवून. Edit आणि rejection चे दर मोजा, कारण शून्य दर म्हणजे बहुतेक वेळा कुणीच वाचत नाही.
- **प्रत्येक tool call चा audit log.** कोणते tool, कोणते inputs, काय परत आले, agent ने कशाचा मसुदा बनवला. एखादा work order का अस्तित्वात आहे असे कुणी विचारले, तर उत्तर log मध्ये असते.
- **Go-live आधी replay evals.** गेल्या एक किंवा दोन महिन्यांच्या shifts वर, त्या वेळी जसा data होता तसाच वापरून agent चालवा, आणि त्याच्या मसुद्यांची तुलना planners आणि engineers नी प्रत्यक्षात जे केले त्याच्याशी करा. त्याने पकडलेले खरे प्रश्न, त्याने केलेला गोंगाट आणि चुकीचे ठरले असते असे मसुदे मोजा. Model, prompts किंवा tools बदलतील तेव्हा प्रत्येक वेळी हे पुन्हा करा.
- **Step, cost आणि rate मर्यादा.** प्रत्येक run मधील tool calls आणि प्रत्येक shift मधील मसुद्यांवर मर्यादा, जेणेकरून गोंधळलेला agent CMMS मध्ये पूर आणू शकणार नाही.
- **एका switch ने बंद होतो.** फक्त IT मधील नव्हे, तर operations मधील कुणीही agent लगेच थांबवू शकतो.

लेख 3 मधील autonomy शिडीवर हा agent **L2** वर आहे: तो मोकळेपणाने वाचतो आणि मसुदे बनवतो, आणि माणूस मंजुरी देतो. तो तिथेच राहायला हवा.

## हे कुठे मोडते

**Agent ला data मधील प्रत्येक दोष वारशाने मिळतो.** Stop codes अस्पष्ट असतील तर क्रमवारीही अस्पष्ट असेल. CMMS ची asset hierarchy MES शी जुळत नसेल, तर agent stop ला work order शी जोडू शकत नाही. हे आधी दुरुस्त करा. कोणत्याही model पेक्षा ते स्वस्त आहे.

**जास्त मसुदे विश्वास संपवतात.** प्रत्येक shift ला पंधरा मसुदे काढणाऱ्या agent कडे आठवड्याभरात दुर्लक्ष होईल. एका loss प्रकाराने आणि एका line ने सुरुवात करा, आणि coverage पेक्षा precision साठी tune करा.

**Plant मधील मजकुरातून prompt injection.** Agent operator notes आणि जुने work orders वाचतो. ते सगळे data म्हणून हाताळा, सूचना म्हणून कधीच नाही, आणि प्रत्येक write tool मंजुरीच्या मागे ठेवा, जेणेकरून एखादी विचित्र नोंद कृतीत बदलू शकणार नाही.

**Replica lag.** DMZ replica काही तास मागे चालत असेल, तर agent शिळ्या data वर काम करतो. प्रत्येक मसुद्यावर data चा timestamp दाखवा.

**मंजुरीचा थकवा.** Shift च्या शेवटी चाळीस वेळा approve वर click करणे म्हणजे देखरेख नव्हे. संख्या कमी ठेवा आणि पुरावा स्पष्ट ठेवा.

## सारांश

चांगला plant agent हा operator नसून analyst असतो. तो प्रत्येक shift ला losses वाचतो, stop log, historian आणि maintenance इतिहास यांची सांगड घालतो, आणि व्यस्त engineer कधीच हाती घेऊ शकत नाही असा work order किंवा changeover plan चा मसुदा बनवतो. तो सुरक्षित आहे कारण तो कुठे बसतो आणि कशाला हात लावू शकतो यामुळे: Purdue model ची IT बाजू, read-only OT data, फक्त मसुदे बनवणारी write tools, मंजुरी देणारा माणूस, प्रत्येक call चा log, आणि इतिहास replay करून केलेली चाचणी. Model कधी कधी चुकेल. ती चूक एखादा batch नव्हे, तर फक्त नाकारलेला मसुदा एवढ्याच किमतीची राहील याची खात्री architecture करते.

पुढे, आणि शेवटी: [roadmap आणि ते कुठे मोडते]({{ '/mr/2026/ai-opex-roadmap-where-it-breaks-agi-hype/' | relative_url }}). Line downtime च्या predictive बाजूसाठी [Predicting Packaging Line Downtime and Lifting OEE]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}) पाहा. संपूर्ण यादी [मालिकेच्या पानावर]({{ '/series/ai-operational-excellence/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**Beverage plant मध्ये AI agent सुरक्षितपणे काय करू शकतो?**
Production, maintenance आणि quality data वाचणे, कोणते losses महत्त्वाचे आहेत ते ठरवणे, आणि लोकांसाठी कृतींचा मसुदा बनवणे: maintenance work orders, changeover plans, shift summaries, planner ला संदेश. प्रत्येक मसुद्यासोबत त्याचा पुरावा असतो आणि तो मंजुरीची वाट पाहतो. PLCs, SCADA किंवा process setpoints मध्ये लिहिण्याचा कोणताही मार्ग त्याच्याकडे नसावा.

**Purdue model म्हणजे काय आणि AI agents साठी तो का महत्त्वाचा आहे?**
Purdue model ही एक reference architecture आहे जी plant चे networks स्तरांमध्ये विभागते: तळाशी प्रत्यक्ष process आणि त्याचे controllers, सर्वात वर business systems, आणि operations व enterprise IT यांच्यामध्ये एक demilitarised zone. Agent ची जागा IT बाजूला आहे, जिथे तो DMZ मधील replicated data वाचतो. त्याने control स्तरांमध्ये खाली कधीही connection उघडू नये.

**AI agent ला plant वर मोकळे सोडण्याआधी त्याची चाचणी कशी करायची?**
इतिहास replay करा. गेल्या एक किंवा दोन महिन्यांच्या shifts वर, त्या वेळी जसा data होता तसाच वापरून agent चालवा, आणि त्याच्या मसुद्यांची तुलना planners आणि engineers नी प्रत्यक्षात जे केले त्याच्याशी करा. त्याने किती खरे प्रश्न पकडले, किती मसुदे निव्वळ गोंगाट होते, आणि किती चुकीचे ठरले असते ते मोजा. Model, prompts किंवा tools बदलतील तेव्हा प्रत्येक वेळी replay पुन्हा करा.
