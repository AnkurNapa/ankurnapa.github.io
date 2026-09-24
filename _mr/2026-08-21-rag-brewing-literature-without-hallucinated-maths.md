---
layout: post
lang: mr
title: "brewing साहित्यावर RAG, पण भ्रामक गणिताशिवाय"
image: /assets/og/rag-brewing-literature-without-hallucinated-maths.png
description: "The Brewer's Agent चा भाग 1. brewing साहित्य काय सांगते ते शोधण्यात retrieval-augmented generation चांगले आहे, आणि ते जे सांगते ते करण्यात वाईट. formulas आणि tables चे chunking कसे करावे, brewing ला hybrid search का लागतो, प्रत्येक उत्तराला संदर्भ का हवा, आणि गणित tool कडे का जाते."
date: 2026-08-21 09:00:00 -0700
updated: 2026-08-21
permalink: /mr/2026/rag-brewing-literature-without-hallucinated-maths/
tags: [brewing-science, brewers-agent, generative-ai, rag, data-engineering]
faq:
  - q: "RAG म्हणजे काय आणि brewing ज्ञानासाठी ते का वापरावे?"
    a: "retrieval-augmented generation म्हणजे model उत्तर देण्याआधी तुमच्या स्वतःच्या documents मधील परिच्छेद शोधते, आणि त्या परिच्छेदांवरून उत्तर देते. brewing साठी यामुळे उत्तरे model ला internet वरून अर्धवट आठवणाऱ्या गोष्टींऐवजी तुमचा विश्वास असलेल्या पाठ्यपुस्तकांशी, papers शी आणि lab methods शी जोडलेली राहतात, आणि प्रत्येक उत्तर आपल्या स्रोताचा संदर्भ देऊ शकते."
  - q: "RAG system ABV किंवा IBU बरोबर काढू शकते का?"
    a: "ते योग्य formula शोधू शकते, पण त्याने बेरजा करू नयेत. अनेक पायऱ्यांच्या गणितात language models अविश्वसनीय असतात, आणि brewing formulas मध्ये units आणि तापमानाचे असे संकेत असतात जे सहज गोंधळतात. स्पष्टीकरणासाठी formula retrieve करा आणि आकडे तपासलेल्या calculation tool कडे पाठवा."
  - q: "retrieval साठी brewing documents चे chunking कसे करावे?"
    a: "formulas, त्यांच्या variables च्या व्याख्या आणि त्यांची units एकाच chunk मध्ये ठेवा, आणि tables त्यांच्या headers आणि footnotes सह पूर्ण ठेवा. प्रत्येक chunk सोबत तापमानाचा आधार आणि units सारखा metadata साठवा. ठरावीक अक्षरसंख्येवर तुकडे केल्यास formula आणि त्याच्या चिन्हांचा अर्थ सांगणारी ओळ नेहमीच वेगळी पडतात."
---

**थोडक्यात उत्तर: brewing साहित्य काय सांगते ते शोधण्यात RAG खूप चांगले आहे आणि ते जे सांगते ते करण्यात बरेच वाईट. त्याला तुमची पाठ्यपुस्तके, papers आणि lab methods कडे वळवा, त्यांचे chunking असे करा की formula कधीच त्याच्या units पासून वेगळा होणार नाही, hybrid search वापरा कारण brewing मध्ये embeddings धूसर करतात अशा संक्षेपांचा भरणा असतो, आणि प्रत्येक उत्तराला ज्या परिच्छेदातून ते आले त्याचा संदर्भ द्यायला लावा. मग गणित model कडून पूर्णपणे काढून घ्या. ते स्पष्टीकरणासाठी formula retrieve करते. आकडा तपासलेले tool काढते.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="brewing चा एक प्रश्न pipeline मध्ये येतो. hybrid retrieval chunk केलेल्या पाठ्यपुस्तकांवर, papers वर आणि lab methods वर keyword search आणि vector search एकत्र करते, मग reranker सर्वोत्तम परिच्छेद निवडतो. language model संदर्भांसह स्पष्टीकरण लिहिते. प्रश्नातील कोणतेही आकडे वेगळ्या फांदीवरून calculation tool कडे पाठवले जातात, जे पद्धत आणि units सह काढलेले मूल्य परत करते. एक banner सांगतो: ज्ञान retrieve करा, आकडे compute करा.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">एका प्रश्नासाठी दोन मार्ग: शब्द RETRIEVAL मधून, आकडे TOOLS मधून</text>
<g font-family="sans-serif">
<rect x="30" y="110" width="160" height="70" rx="9" fill="#06483f"/>
<text x="110" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">brewer चा प्रश्न</text>
<text x="110" y="160" text-anchor="middle" font-size="10.5" fill="#cfe6df">"13 &#176;P, 64.9% RDF वर ABV?"</text>
<line x1="190" y1="130" x2="240" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="190" y1="160" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">hybrid retrieval</text>
<text x="340" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">keyword + vector, मग rerank</text>
<line x1="440" y1="86" x2="480" y2="86" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">LLM समजावते</text>
<text x="580" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">परिच्छेदांवरून, संदर्भांसह</text>
<rect x="240" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">calculation tool</text>
<text x="340" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">तपासलेले code, base units</text>
<line x1="440" y1="216" x2="480" y2="216" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">5.46% ABV</text>
<text x="580" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">पद्धत आणि units सह परत</text>
<line x1="680" y1="86" x2="740" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="216" x2="740" y2="165" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="115" width="230" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="855" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">उत्तर</text>
<text x="855" y="162" text-anchor="middle" font-size="10.5" fill="#4a6b64">समजावलेले, संदर्भासह, compute केलेले</text>
<rect x="30" y="270" width="940" height="38" rx="10" fill="#06483f"/>
<text x="500" y="294" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">ज्ञान RETRIEVE करा &#183; आकडे COMPUTE करा &#183; कधीच उलटे नाही</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">model आणि calculator दोघांनाही ज्यात ते चांगले आहेत ते काम मिळते. brewer ला स्रोत आणि पद्धतीसह एकच उत्तर मिळते.</figcaption>
</figure>

एखाद्या सर्वसाधारण chatbot ला विचारा की original extract आणि real degree of fermentation वरून बिअरमधील alcohol कसे काढायचे. तुम्हाला आत्मविश्वासपूर्ण परिच्छेद आणि एक formula मिळेल. कधी तो योग्य formula असतो. कधी specific gravity वर चालणारा homebrew शॉर्टकट असतो, ज्याला अशा Plato आकड्यांचा साज चढवलेला असतो ज्यांच्यासाठी तो कधीच नव्हता. कोणत्याही परिस्थितीत शेवटचा आकडा model च्या डोक्यात काढलेला असतो, आणि अडचण तिथूनच सुरू होते.

**The Brewer's Agent** मधील ही पहिली पोस्ट आहे. ही मालिका brewing साठी असे GenAI tools बांधण्यावर आहे ज्यांच्यावर brewer खरोखर विश्वास ठेवू शकेल. वायनरीत [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}) जिथे थांबली तिथून ही पुढे जाते: model त्याच्या खालच्या डेटा आणि tools इतकेच चांगले असते.

## RAG प्रत्यक्षात काय करते

retrieval-augmented generation ही साधी कल्पना आहे. model उत्तर देण्याआधी एक search पायरी तुमच्या नियंत्रणातील संग्रहातून सर्वात संबंधित परिच्छेद काढते. मग model स्मृतीऐवजी त्या परिच्छेदांवरून उत्तर देते.

brewery साठी हा संग्रह असा असू शकतो:

- काही पाठ्यपुस्तके आणि त्यांतील लोक प्रत्यक्ष वापरतात ती प्रकरणे
- hop chemistry, mashing आणि fermentation वरील प्रकाशित papers
- तुमच्या स्वतःच्या lab methods आणि SOPs
- supplier specifications आणि certificates of analysis

फायदा हा नाही की model अधिक हुशार होते. फायदा हा आहे की उत्तर तुम्ही निवडलेल्या document मधून येते, आणि उत्तर तुम्हाला कोणते ते सांगू शकते. brewer पान उघडून तपासू शकतो. स्रोत तपासण्याची ती सवय हीच संपूर्ण safety system आहे.

## chunking: brewing documents कुठे मोडतात

index करण्याआधी documents chunks मध्ये विभागले जातात, आणि तांत्रिक क्षेत्रांतील बहुतेक RAG अपयशांची सुरुवात नेमकी इथे होते.

default पद्धत दर हजार-एक अक्षरांवर मजकूर तोडते. brewing साहित्य अशा formulas ने भरलेले आहे ज्यांच्यानंतर चिन्हे, units आणि तापमानाचा आधार समजावणारी ओळ येते. चुकीच्या ठिकाणी तुकडा पडला की एका chunk मध्ये formula राहतो आणि पुढच्यात "where OG is in degrees Plato at 20/20 degrees C". model पहिला retrieve करते आणि दुसऱ्याचा अंदाज बांधते.

बहुतेक समस्या दूर करणारे नियम:

1. **formula त्याच्या व्याख्यांसोबत ठेवा.** अक्षरसंख्येवर नव्हे तर विभागांच्या सीमांवर तुकडे करा, आणि equation अधिक त्यानंतरचा परिच्छेद एक घटक माना.
2. **tables पूर्ण ठेवा.** header row नसलेले hop utilisation table म्हणजे आकड्यांची यादी. संपूर्ण table, headers, footnotes आणि सगळे, एकच chunk म्हणून साठवा, तो लांब असला तरी.
3. **संकेत metadata मध्ये ठेवा.** प्रत्येक chunk सोबत units, तापमानाचा आधार आणि स्रोताची आवृत्ती साठवा. 20/20 degrees C वरील Plato आणि 60/60 degrees F वरील specific gravity अदलाबदल करता येत नाहीत, आणि model ला आपल्या हातात कोणते आहे ते दिसायला हवे.
4. **लांब derivations साठी parent retrieval.** अचूक जुळणीसाठी छोटे chunks index करा, पण model ला ते ज्या संपूर्ण विभागातून आले तो द्या.

## hybrid search, कारण brewing संक्षेपांत बोलते

vector search समान अर्थाचे परिच्छेद शोधतो. "माझ्या lager ला शिजवलेल्या मक्याचा वास का येतो" DMS वर पोहोचण्यासाठी हे उत्तम आहे. जिथे एका अक्षराला महत्त्व असते अशा शब्दांसाठी ते कमी चांगले आहे.

RDF आणि ADF ही attenuation ची दोन वेगळी मापे आहेत, आणि एकाच बिअरवर त्यांच्यात दहापेक्षा जास्त points चा फरक असू शकतो. embedding model ला ती जवळजवळ सारखी दिसतात: छोटी, capital अक्षरांत, fermentation बद्दल. keyword search (BM25 किंवा तत्सम) त्यांना ते जसे आहेत तसे वेगळे शब्द मानतो.

म्हणून दोन्ही चालवा आणि निकाल एकत्र करा, मग reranker ला सर्वात संबंधित परिच्छेद आधी ठेवू द्या. बहुतेक vector databases आणि search services आता हे थेट support करतात. तांत्रिक RAG system मध्ये तुम्ही करू शकता ती ही एकमेव सर्वात स्वस्त सुधारणा आहे.

## ज्ञानासाठी retrieval, गणितासाठी tools

संपूर्ण मालिका ज्या नियमावर उभी आहे तो हा. **model formula समजावू शकते. ते formula चे मूल्य काढू शकत नाही.**

आकृतीतील प्रश्न घ्या. 13.0 degrees Plato चा wort 64.9% real degree of fermentation पर्यंत fermented झाला. ABV किती?

नीट केल्यास हे Balling च्या वापरलेले extract आणि तयार झालेले alcohol यांतील संबंधातून जाते, साधारण 4.77% real extract आणि वजनाने साधारण 4.27% alcohol देते, मग बिअरच्या स्वतःच्या density वापरून वजनाचे volume मध्ये रूपांतर करते. उत्तर 5.46% ABV आहे. प्रत्येक पायरीला चार दशांश स्थळांचा constant आणि unit संकेत जोडलेला असतो.

हे डोक्यात करायला सांगितलेले language model बहुतेकदा जवळ पोहोचेल. जवळ पोहोचणे हीच समस्या आहे. ते कधीतरी एखादी पायरी गाळेल, चुकीची density वापरेल किंवा वजन आणि volume यांची अदलाबदल करेल, आणि 4.3% अगदी 5.46% इतक्याच आत्मविश्वासाने मांडेल. गद्यातील काहीही तुम्हाला कोणते उत्तर मिळाले ते सांगत नाही.

उपाय रचनात्मक आहे, अधिक चांगला prompt नव्हे. retrieval पायरी स्पष्टीकरण पुरवते: RDF म्हणजे काय, वजन आणि volume का वेगळे असतात, constants कुठून येतात. calculation tool, म्हणजे साधे तपासलेले code, आकडा पुरवते. [पुढची पोस्ट]({{ '/mr/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) ते tools बांधते. या पोस्टसाठी मुद्दा असा की RAG system ने गणित बाहेर पाठवायला हवे, आणि उत्तरात तसे सांगायला हवे: "OG आणि RDF वरून ABV tool ने काढलेले".

## संदर्भ हेच feature आहे

प्रत्येक उत्तरासोबत त्याचे स्रोत असायला हवेत: document, विभाग आणि शक्य असल्यास पान. system prompt मध्ये ही कठोर अट ठेवा आणि testing मध्ये तपासा. संदर्भ नसलेले उत्तर कितीही चांगले वाटले तरी अपयशी उत्तर मानायला हवे.

दोन छोट्या गोष्टी संदर्भांना कितीतरी जास्त उपयुक्त बनवतात:

- **फक्त शीर्षक नव्हे, परिच्छेद दाखवा.** उद्धृत परिच्छेदावर नजर टाकणारा brewer चुकीची आवृत्ती किंवा homebrew स्रोत कोणत्याही automated check पेक्षा लवकर ओळखेल.
- **काहीच सापडले नाही तर तसे सांगा.** retrieval ने काहीही संबंधित परत केले नाही, तर योग्य उत्तर "माझ्याकडे त्यासाठी स्रोत नाही" हे आहे, सर्वसाधारण ज्ञानावरून अस्खलित अंदाज नव्हे. हे वर्तन मुद्दाम तपासा, कारण models मदत करण्यासाठी train केलेली असतात आणि तुम्ही करू दिले तर पोकळी भरून काढतील.

## हे कुठे मोडते

**तुमच्या संग्रहाला मते असतात.** hop utilisation वर पाठ्यपुस्तके सहमत नसतात, homebrew स्रोत असे शॉर्टकट वापरतात जे व्यावसायिक labs वापरणार नाहीत, आणि जुन्या आवृत्त्यांत रद्द झालेल्या पद्धती असतात. RAG जो परिच्छेद सर्वोत्तम जुळतो तो निष्ठेने retrieve करते. संग्रह निवडून तयार करा, स्रोताचा प्रकार tag करा, आणि जिथे तुमच्या स्वतःच्या lab methods आहेत तिथे त्यांना प्राधान्य द्या.

**scan केलेल्या PDFs मधून गणित हरवते.** OCR subscripts, Greek अक्षरे आणि अपूर्णांकांचा गोंगाट करते. पुस्तकात "E = P/100" असा वाचला जाणारा formula "E - Pl100" असा बाहेर येऊ शकतो. index वर विश्वास ठेवण्याआधी तुमच्या सर्वाधिक वापरल्या जाणाऱ्या formulas चा काढलेला मजकूर डोळ्यांनी तपासा.

**copyright अजूनही लागू आहे.** अंतर्गत वापरासाठी पाठ्यपुस्तक index करणे ही एक गोष्ट आहे. model ला कंपनीबाहेरील लोकांसाठी लांब परिच्छेद उद्धृत करू देणे ही दुसरी. तुम्ही index करत असलेल्या documents ना कोणता licence लागू आहे हे जाणून घ्या.

**संदर्भसुद्धा बनावट असू शकतात.** model असा संदर्भ तयार करू शकते जो बरोबर दिसतो आणि कधीच retrieve झालेला नव्हता. संदर्भ model च्या मजकुरातून नव्हे तर code मध्ये retrieval metadata वरून तयार करा.

## निष्कर्ष

RAG brewing साहित्याच्या ढिगाला अशा गोष्टीत बदलते ज्याला तुम्ही प्रश्न विचारू शकता, आणि उत्तरे पानाकडे परत बोट दाखवतात. हे खरोखर उपयुक्त आहे. ते जे करत नाही ते म्हणजे model ला गणितात चांगले बनवणे, आणि brewing म्हणजे बहुतेक संकेत जोडलेले गणितच आहे. formulas त्यांची units जपतील असे chunking करा, अर्थासोबत keywords नेही शोधा, संदर्भांचा आग्रह धरा, आणि प्रत्येक आकडा tool कडे पाठवा. model पुस्तक वाचते. बेरजा calculator करतो.

breweries मध्ये AI सध्या काय करत आहे याच्या व्यापक चित्रासाठी पाहा [What AI in Beer Actually Looks Like in 2026]({{ '/2026/what-ai-in-beer-actually-looks-like-2026/' | relative_url }}). संपूर्ण यादी [The Brewer's Agent मालिकेच्या पानावर]({{ '/series/brewers-agent/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**RAG म्हणजे काय आणि brewing ज्ञानासाठी ते का वापरावे?**
retrieval-augmented generation म्हणजे model उत्तर देण्याआधी तुमच्या स्वतःच्या documents मधील परिच्छेद शोधते, आणि त्या परिच्छेदांवरून उत्तर देते. brewing साठी यामुळे उत्तरे model ला internet वरून अर्धवट आठवणाऱ्या गोष्टींऐवजी तुमचा विश्वास असलेल्या पाठ्यपुस्तकांशी, papers शी आणि lab methods शी जोडलेली राहतात, आणि प्रत्येक उत्तर आपल्या स्रोताचा संदर्भ देऊ शकते.

**RAG system ABV किंवा IBU बरोबर काढू शकते का?**
ते योग्य formula शोधू शकते, पण त्याने बेरजा करू नयेत. अनेक पायऱ्यांच्या गणितात language models अविश्वसनीय असतात, आणि brewing formulas मध्ये units आणि तापमानाचे असे संकेत असतात जे सहज गोंधळतात. स्पष्टीकरणासाठी formula retrieve करा आणि आकडे तपासलेल्या calculation tool कडे पाठवा.

**retrieval साठी brewing documents चे chunking कसे करावे?**
formulas, त्यांच्या variables च्या व्याख्या आणि त्यांची units एकाच chunk मध्ये ठेवा, आणि tables त्यांच्या headers आणि footnotes सह पूर्ण ठेवा. प्रत्येक chunk सोबत तापमानाचा आधार आणि units सारखा metadata साठवा. ठरावीक अक्षरसंख्येवर तुकडे केल्यास formula आणि त्याच्या चिन्हांचा अर्थ सांगणारी ओळ नेहमीच वेगळी पडतात.
