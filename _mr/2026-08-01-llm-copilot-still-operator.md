---
layout: post
lang: mr
title: "still operator साठी LLM copilot: SOPs वर RAG, फक्त वाचणारे tools, setpoints नाहीत"
image: /assets/og/llm-copilot-still-operator.png
description: "The Still and the Model चा भाग 3. still house च्या floor वरील GenAI copilot ने काय करावे आणि काय करू नये: नियंत्रित SOPs आणि run logs मधून संदर्भासह उत्तरे देणे, फक्त वाचणाऱ्या tools मार्फत live values वाचणे, shift handover लिहिणे, आणि setpoint, interlock किंवा cut ला कधीही हात न लावणे."
date: 2026-08-01 09:00:00 -0700
updated: 2026-08-01
permalink: /mr/2026/llm-copilot-still-operator/
tags: [distilling-maturation, still-and-model, generative-ai, rag, ai-agents]
faq:
  - q: "LLM copilot distillery operator साठी काय करू शकतो?"
    a: "तो नियंत्रित SOPs मधून परिच्छेदाच्या संदर्भासह procedure च्या प्रश्नांची उत्तरे देऊ शकतो, तत्सम परिस्थितींसाठी मागील run logs शोधू शकतो, फक्त वाचणाऱ्या tools मार्फत live process values वाचू शकतो, आणि historian व operator च्या notes वरून shift handover चा मसुदा तयार करू शकतो. तो शोधण्याचा आणि लिहिण्याचा वेळ वाचवतो, आणि shift चा मोठा भाग त्यातच जातो."
  - q: "AI copilot ला still setpoints बदलू द्यावेत का?"
    a: "नाही. copilot कडे लिहिणारे कोणतेही tools नसावेत. setpoints, interlocks आणि cut चे निर्णय operator आणि control system कडेच राहतात. सर्वात सोपी safety रचना म्हणजे अस्तित्वातच नसलेले tool: model set_setpoint call करूच शकत नसेल, तर कोणताही prompt त्याला ते करायला लावू शकत नाही."
  - q: "still-house copilot ला procedure ची चुकीची उत्तरे देण्यापासून कसे रोखावे?"
    a: "retrieval फक्त SOPs च्या सध्याच्या नियंत्रित आवृत्त्यांकडे वळवा, model ला वापरलेला परिच्छेद उद्धृत करून त्याची link द्यायला लावा, स्रोत सापडला नाही तर उत्तर नाकारायला लावा, आणि प्रत्येक बदलाआधी व नंतर तपासलेल्या उत्तरांसह operators च्या खऱ्या प्रश्नांच्या संचावर त्याची चाचणी घ्या. safety शी संबंधित कोणतीही कृती करण्याआधी operator मूळ स्रोत वाचतो."
---

**थोडक्यात उत्तर: still-house copilot बांधणे तेव्हाच योग्य आहे जेव्हा तो shift खाऊन टाकणारे वाचन आणि लेखन करतो, आणि दुसरे काहीही नाही. त्याला नियंत्रित SOPs आणि वर्षानुवर्षांच्या run logs कडे वळवा, वापरलेल्या परिच्छेदाचा संदर्भ द्यायला लावा, historian मधील live values साठी फक्त वाचणारे tools द्या, आणि shift च्या शेवटी त्याला handover चा मसुदा लिहू द्या. त्याला लिहिणारे कोणतेही tools देऊ नका. setpoints, interlocks आणि cuts operator आणि control system कडेच राहतात. still वरील सर्वात सुरक्षित tool म्हणजे जे model ला कधीच दिले गेले नाही.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="मध्यभागी LLM copilot. डावीकडे त्याचे स्रोत: retrieval मार्फत नियंत्रित SOPs, run logs आणि shift notes, आणि get_value, get_trend व get_run_summary नावाच्या फक्त वाचणाऱ्या tools मार्फत live historian values. उजवीकडे त्याचे outputs: SOP परिच्छेदाच्या संदर्भासह उत्तरे, shift handover चा मसुदा, आणि एखाद्या व्यक्तीने पूर्ण करायचा deviation note चा मसुदा. तळाशी set_setpoint नावाचे खोडलेले tool, आणि setpoints, interlocks आणि cuts operator कडेच राहतात असा संदेश.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">शब्द वाचणारा आणि लिहिणारा COPILOT, SETPOINTS कधीच नाही</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">retrieval</text>
<text x="165" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">नियंत्रित SOPs (सध्याच्या आवृत्त्या)</text>
<text x="165" y="120" text-anchor="middle" font-size="10.5" fill="#4a6b64">run logs &#183; shift notes</text>
<rect x="30" y="160" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="186" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">फक्त वाचणारे tools</text>
<text x="165" y="206" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_value &#183; get_trend</text>
<text x="165" y="224" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_run_summary</text>
<line x1="300" y1="101" x2="400" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="300" y1="205" x2="400" y2="170" stroke="#4db6a2" stroke-width="2"/>
<rect x="400" y="110" width="200" height="90" rx="12" fill="#06483f"/>
<text x="500" y="150" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">LLM copilot</text>
<text x="500" y="172" text-anchor="middle" font-size="10.5" fill="#cfe6df">उत्तर देतो, संदर्भ देतो, मसुदा लिहितो</text>
<line x1="600" y1="140" x2="700" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="155" x2="700" y2="155" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="170" x2="700" y2="225" stroke="#4db6a2" stroke-width="2"/>
<rect x="700" y="60" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="90" text-anchor="middle" font-size="11.5" fill="#06483f">उत्तर + SOP परिच्छेदाचा संदर्भ</text>
<rect x="700" y="130" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="160" text-anchor="middle" font-size="11.5" fill="#06483f">shift handover चा मसुदा</text>
<rect x="700" y="200" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="230" text-anchor="middle" font-size="11.5" fill="#06483f">deviation note चा मसुदा</text>
<rect x="30" y="272" width="940" height="44" rx="10" fill="#06483f"/>
<text x="180" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081" text-decoration="line-through">set_setpoint()</text>
<text x="600" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SETPOINTS, INTERLOCKS आणि CUTS OPERATOR कडेच राहतात</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">डावीकडील सगळे वाचले जाते. उजवीकडील सगळे मसुदे आहेत. तळाशी नसलेले tool हीच safety रचना आहे.</figcaption>
</figure>

shift बदलण्याच्या वेळी सकाळचे सहा वाजले आहेत. रात्रीच्या operator कडे notes चे एक पान आहे, दोनच्या सुमारास थोडा संथ गेलेला एक run आहे, आणि फुसफुसणारा एक steam trap आहे. दिवसाच्या operator ला पाच मिनिटांचा handover मिळतो, त्यातला अर्धा वेळ संथ run कोणत्या क्रमांकाचा होता हे शोधण्यात जातो. त्याच सकाळी नंतर एक trainee विचारतो की CIP नंतर feints receiver changeover कसा करतात, आणि त्याचे उत्तर shared drive वरील अशा SOP मध्ये आहे जे कोणालाच सापडत नाही.

यापैकी काहीही control समस्या नाही. ही वाचण्याची आणि लिहिण्याची समस्या आहे, आणि large language models खरोखर यातच चांगले आहेत. ही पोस्ट त्या कामासाठीच्या copilot बद्दल आहे, आणि अशा एका गोष्टीबद्दल जी त्याला कधीच करता येऊ नये.

## copilot कशासाठी आहे

चार कामे, साधारण मूल्याच्या क्रमाने:

**1. procedure चे प्रश्न, स्रोतातून उत्तर दिलेले.** नियंत्रित SOPs वर retrieval-augmented generation (RAG): operator साध्या शब्दांत विचारतो, copilot संबंधित परिच्छेद शोधतो, उत्तर देतो आणि document क्रमांक व आवृत्तीसह तो उद्धृत करतो. त्याला स्रोत सापडला नाही, तर तो मनाने काही रचण्याऐवजी तसे सांगतो.

**2. "हे आधी घडले आहे का?"** वर्षानुवर्षांच्या run logs आणि shift notes म्हणजे प्रत्येक विचित्र run आणि तो कशाने दुरुस्त झाला याची नोंद. त्यांच्यावरील semantic search "boiler trip नंतर संथ run, strength लवकर घसरते" याचे तत्सम मागील runs आणि त्या वेळी operator ने लिहिलेल्या गोष्टींच्या यादीत रूपांतर करते. यादीतील ही बहुतेकदा सर्वात उपयुक्त गोष्ट असते, आणि आज कोणीही न वाचणारा हा दडलेला मजकूर आहे.

**3. shift handover.** shift च्या शेवटी copilot historian मधून runs, [soft sensor पोस्ट]({{ '/mr/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}) मधील band flags, operator च्या notes आणि उघडे work orders काढतो, आणि एका पानाचा handover मसुदा तयार करतो. operator तो संपादित करून त्यावर सही करतो. रात्रीच्या shift ला 5:45 ला जेवढे लिहायची ताकद उरली होती तेवढ्याऐवजी दिवसाच्या shift ला सुसंगत सारांश मिळतो.

**4. कागदपत्रांचे मसुदे.** deviation notes, near-miss reports आणि maintenance requests अशा मसुद्यापासून सुरू होतात ज्यात run क्रमांक, timestamps आणि values आधीच जोडलेले असतात.

## tools: रचनेनेच फक्त वाचणारे

live plant बद्दल बोलण्यासाठी copilot ला डेटा लागतो, आणि 2026 मध्ये तो पुरवण्याची स्वच्छ पद्धत म्हणजे historian वर बसलेला tools चा छोटा संच (सहसा MCP वरून उपलब्ध):

```text
get_value(tag)                      -> current value, unit, timestamp, quality
get_trend(tag, from, to)            -> time series, downsampled
get_run_summary(still, run_id)      -> charge, cuts, fractions, alcohol balance
search_run_logs(query, still)       -> matching notes with run ids
```

प्रत्येक tool वाचते. त्यापैकी एकही लिहीत नाही. `set_setpoint` नाही, `acknowledge_alarm` नाही, `open_valve` नाही. ही prompt मधील मार्गदर्शक सूचना नाही, जिच्याभोवती पुरेसा हुशार prompt मार्ग काढू शकतो. ही क्षमतेचीच अनुपस्थिती आहे. जे tool अस्तित्वातच नाही ते model call करू शकत नाही.

त्याच कारणासाठी historian connection स्वतःसुद्धा network आणि account पातळीवर फक्त वाचणारे असावे. control system चा स्वतःचा safety layer, त्याचे interlocks आणि त्याचे engineers असतात, आणि language model चे त्याच्या आसपासही काही काम नाही.

## उत्तरे विश्वासार्ह बनवणे

procedure बद्दल खात्रीशीर वाटणारा पण चुकीचा copilot हा copilot नसण्यापेक्षा वाईट आहे. काही नियम बहुतेक काम करतात:

1. **index मध्ये फक्त सध्याची, नियंत्रित documents.** SOP सुधारला की जुनी आवृत्ती त्याच दिवशी retrieval मधून बाहेर जाते. index मधील रद्द झालेल्या procedures हा अशा systems कडून आत्मविश्वासाने चुकीची उत्तरे येण्याचा सर्वात सामान्य मार्ग आहे.
2. **संदर्भ द्या किंवा नकार द्या.** procedure चे प्रत्येक उत्तर परिच्छेद उद्धृत करते आणि document ची link देते. स्रोत नाही, उत्तर नाही.
3. **आकडे tools कडून, model कडून कधीच नाहीत.** operator ने condenser outlet तापमान किती आहे असे विचारले, तर copilot `get_value` call करतो आणि जे परत आले ते त्याच्या timestamp सह सांगतो. तो अंदाज लावत नाही.
4. **खरा eval set.** operators नी प्रत्यक्ष विचारलेले पन्नास प्रश्न, shift leader ने तपासलेल्या उत्तरांसह, गोळा करा, आणि model, prompt किंवा document index बदलेल तेव्हा प्रत्येक वेळी ते चालवा. गुण द्या. "तो पुरेसा चांगला आहे का?" याचे हेच एकमेव प्रामाणिक उत्तर आहे.

## हे कुठे मोडते

**safety-critical प्रश्नांना सारांश नव्हे, स्रोत हवा.** isolation, confined space, hot work किंवा ethanol vapour शी संबंधित कोणत्याही गोष्टीसाठी copilot चे काम योग्य SOP उघडणे आहे, त्याचे स्वतःच्या शब्दांत पुनर्लेखन करणे नाही. हा रचनेत आणि training मध्ये कठोर नियम बनवा.

**run logs गोंधळलेले आणि कधी कधी चुकीचे असतात.** semantic search 2021 मधील "steam वाढवून दुरुस्त केले" म्हणणारी note आनंदाने शोधून काढेल, आणि तो चुकीचा उपाय असू शकतो. मागील notes म्हणजे धागे आहेत, सूचना नाहीत.

**handover मसुदे समस्या गुळगुळीत करू शकतात.** नीटनेटका सारांश अस्वस्थ रात्रीला नेहमीची वाटायला लावू शकतो. ज्या operator ने ती shift अनुभवली त्याने तो संपादित करून सही करायला हवी, आणि मसुद्याने band flags आणि उघडे मुद्दे सारांशात विरघळवण्याऐवजी स्पष्टपणे यादीत मांडायला हवेत.

**कालांतराने लोक त्यावर जास्त विश्वास ठेवतील.** तो जितका चांगला होतो तितके कमी लोक तपासतात. म्हणूनच eval set फक्त launch च्या वेळी नव्हे तर कायम चालू ठेवायला हवा.

## निष्कर्ष

still house च्या operating समस्येत वाचण्या-लिहिण्याची समस्या दडलेली आहे: कोणालाही न सापडणाऱ्या procedures, कोणीही न वाचणारे run logs आणि अर्धवट झोपेत लिहिलेले handovers. language model नेमके यातच चांगले आहे. त्याला नियंत्रित documents, logs आणि फक्त वाचणारे tools द्या, त्याला संदर्भ द्यायला लावा, खऱ्या प्रश्नांवर त्याची चाचणी घ्या, आणि तो shift चा खरा वेळ वाचवेल. लिहिणारे काहीही त्याला देऊ नका. still operator चालवतो. कागदपत्रे copilot चालवतो.

distillery मधील Anthropic tools च्या व्यापक दृष्टिकोनासाठी पाहा [Claude AI and Claude Code for Distilleries]({{ '/2026/claude-ai-claude-code-for-distilleries/' | relative_url }}). प्रस्ताव द्या, कधीच लिहू नका हाच नियम wine मालिकेत [cellar चे event-sourcing]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) मध्ये येतो. या मालिकेतील पुढील भाग: [data engineering म्हणून cask inventory]({{ '/mr/2026/cask-inventory-data-engineering-scd2/' | relative_url }}). संपूर्ण यादी [The Still and the Model मालिकेच्या पानावर]({{ '/series/still-and-model/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**LLM copilot distillery operator साठी काय करू शकतो?**
तो नियंत्रित SOPs मधून परिच्छेदाच्या संदर्भासह procedure च्या प्रश्नांची उत्तरे देऊ शकतो, तत्सम परिस्थितींसाठी मागील run logs शोधू शकतो, फक्त वाचणाऱ्या tools मार्फत live process values वाचू शकतो, आणि historian व operator च्या notes वरून shift handover चा मसुदा तयार करू शकतो. तो शोधण्याचा आणि लिहिण्याचा वेळ वाचवतो, आणि shift चा मोठा भाग त्यातच जातो.

**AI copilot ला still setpoints बदलू द्यावेत का?**
नाही. copilot कडे लिहिणारे कोणतेही tools नसावेत. setpoints, interlocks आणि cut चे निर्णय operator आणि control system कडेच राहतात. सर्वात सोपी safety रचना म्हणजे अस्तित्वातच नसलेले tool: model set_setpoint call करूच शकत नसेल, तर कोणताही prompt त्याला ते करायला लावू शकत नाही.

**still-house copilot ला procedure ची चुकीची उत्तरे देण्यापासून कसे रोखावे?**
retrieval फक्त SOPs च्या सध्याच्या नियंत्रित आवृत्त्यांकडे वळवा, model ला वापरलेला परिच्छेद उद्धृत करून त्याची link द्यायला लावा, स्रोत सापडला नाही तर उत्तर नाकारायला लावा, आणि प्रत्येक बदलाआधी व नंतर तपासलेल्या उत्तरांसह operators च्या खऱ्या प्रश्नांच्या संचावर त्याची चाचणी घ्या. safety शी संबंधित कोणतीही कृती करण्याआधी operator मूळ स्रोत वाचतो.
