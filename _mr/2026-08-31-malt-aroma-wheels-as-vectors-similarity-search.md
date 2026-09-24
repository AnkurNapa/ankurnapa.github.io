---
layout: post
lang: mr
title: "Malt Aroma Wheels vectors म्हणून: Similarity Search आणि सरासरी लपवते ते blend"
image: /assets/og/malt-aroma-wheels-as-vectors-similarity-search.png
description: "The Brewer's Agent चा भाग 3. प्रकाशित malt aroma wheels ना 22 आकड्यांच्या vectors मध्ये बदला, मग पर्यायी malt शोधता येतो आणि grist च्या स्वभावाचा अंदाज लावता येतो. 51 digitised Weyermann wheels चे खरे आकडे सापळे दाखवतात: raw cosine नुसार प्रत्येक malt सारखाच दिसतो, variants एकाच vector वर कोसळतात, आणि साधी सरासरी 10% roasted malt लपवते."
date: 2026-08-31 09:00:00 -0700
updated: 2026-08-31
permalink: /mr/2026/malt-aroma-wheels-as-vectors-similarity-search/
tags: [brewing-science, brewers-agent, embeddings, vector-search, malting]
faq:
  - q: "पर्यायी malt शोधण्यासाठी vector similarity वापरता येते का?"
    a: "हो, काळजीपूर्वक. प्रत्येक malt चे aroma wheel descriptor तीव्रतांच्या vector मध्ये बदला आणि जवळचे जुळणारे शोधण्यासाठी vectors ची तुलना करा. आधी vectors सरासरी malt वर centre करा, कारण raw cosine similarity जवळपास प्रत्येक जोडीला सारखी ठरवते. रंग आणि extract यांना कडक अटी म्हणून filter करा, म्हणजे aroma जुळले तरी चुकीच्या रंगाचा malt सुचवला जाणार नाही."
  - q: "Aroma vectors ची सरासरी specialty malts ला कमी का लेखते?"
    a: "कारण मजबूत पण अल्पसंख्य स्वभाव base malt च्या वस्तुमानात पातळ होतो. 90% Pilsner आणि 10% roasted malt च्या grist मध्ये साधी वस्तुमान-भारित सरासरी 0 ते 5 scale वर coffee 0.4 वर ठेवते, पण brewers ना माहीत आहे की 10% गडद roasted malt स्पष्टपणे जाणवतो. जे मॉडेल aroma potency नुसार वजन देते आणि सर्वात मजबूत योगदान दिसू देते ते साधारण 2.6 देते."
  - q: "Malt aroma vectors vector database मध्ये ठेवावेत का?"
    a: "काही डझन malts साठी नाही. एक table आणि code च्या काही ओळी पुरेशा आहेत. Vector database तेव्हा उपयोगी ठरतो जेव्हा तुम्ही अनेक स्रोत एकत्र करता, जसे शेकडो malts, hop descriptors आणि text embeddings म्हणून tasting notes, आणि त्या सगळ्यांवर filtered search हवा असतो."
---

**थोडक्यात उत्तर: malt aroma wheel आधीच एक vector आहे. Coffee पासून honey आणि biscuit पर्यंत 0 ते 5 गुण दिलेले बावीस descriptors म्हणजे प्रत्येक malt साठी 22 आकडे, आणि ते हाती आले की पर्यायी malt शोधता येतो आणि grist च्या स्वभावाचा अंदाज लावता येतो. 51 digitised wheels चे खरे आकडे तीन सापळे दाखवतात. Raw cosine similarity जवळपास प्रत्येक malt ला सारखा ठरवते (median 0.91), म्हणून आधी vectors centre करा. एकच प्रकाशित wheel वाटून घेणारे malt variants एकाच vector वर कोसळतात, म्हणून रंग आणि extract specification मधूनच यायला हवेत. आणि 90% Pilsner व 10% CARAFA Special ची साधी सरासरी coffee 5 पैकी 0.4 वर ठेवते, जे चुकीचे आहे हे प्रत्येक brewer ला माहीत आहे.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="51 digitised malt aroma wheels मधील दोन निष्कर्ष. डावीकडे, Pilsner malt आणि CARAFA Special Type 2 मधील cosine similarity raw vectors वर 0.82 आहे, जणू ते सारखे आहेत, आणि सरासरी malt वर centre केल्यावर उणे 0.66, म्हणजे बरोबरपणे विरुद्ध. सर्व malt जोड्यांवरील median raw cosine 0.91 आहे. उजवीकडे, 90 टक्के Pilsner आणि 10 टक्के CARAFA Special Type 2 च्या grist साठी coffee नोंद साध्या वस्तुमान सरासरीने 5 पैकी 0.4 आणि potency-भारित superposition ने 5 पैकी 2.6 येते.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">51 MALT WHEELS VECTORS म्हणून: भोळे गणित चुकवते त्या दोन गोष्टी</text>
<g font-family="sans-serif">
<text x="245" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">PILSNER vs CARAFA SPECIAL 2: साम्य</text>
<rect x="40" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#ff4081" stroke-width="2"/>
<text x="140" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">raw cosine</text>
<text x="140" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#ff4081">0.82</text>
<rect x="260" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="360" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">centred cosine</text>
<text x="360" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#2e9e7c">&#8722;0.66</text>
<text x="250" y="200" text-anchor="middle" font-size="11" fill="#06483f">सर्व जोड्यांवरील median raw cosine: 0.91</text>
<text x="250" y="218" text-anchor="middle" font-size="11" fill="#06483f">सरासरी malt वजा करेपर्यंत सगळे सारखेच दिसतात</text>
<text x="745" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">90% PILSNER + 10% CARAFA SPECIAL 2: COFFEE (0 ते 5)</text>
<rect x="560" y="90" width="30" height="34" rx="4" fill="#ff4081"/>
<text x="600" y="113" font-size="12" font-weight="700" fill="#06483f">0.4 साधी वस्तुमान सरासरी</text>
<rect x="560" y="140" width="195" height="34" rx="4" fill="#06483f"/>
<text x="765" y="163" font-size="12" font-weight="700" fill="#06483f">2.6 potency-भारित</text>
<text x="745" y="205" text-anchor="middle" font-size="11" fill="#06483f">एकट्या CARAFA ला coffee साठी 4, Pilsner ला 0</text>
<text x="745" y="223" text-anchor="middle" font-size="11" fill="#06483f">सरासरी brewer ला चाखता येणारी नोंद गाडून टाकते</text>
<rect x="40" y="262" width="920" height="50" rx="10" fill="#06483f"/>
<text x="500" y="285" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">VECTOR ही चांगली सुरुवात &#183; त्यावरचे गणित म्हणजे ब्रूइंग ज्ञान जिथे जाते ती जागा</text>
<text x="500" y="302" text-anchor="middle" font-size="10.5" fill="#cfe6df">प्रकाशित Weyermann wort aroma wheels मधून digitise केलेल्या 22-descriptor vectors वरून मोजले</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">वाजवी दिसणारे पण चुकीचे दोन आकडे, आणि ते दुरुस्त करणारे दोन छोटे बदल.</figcaption>
</figure>

Weyermann आपल्या बहुतेक malts साठी aroma wheel प्रकाशित करते: descriptors चे एक वर्तुळ (coffee, cacao, bready, honey, toffee, dried fruit वगैरे), प्रत्येकाला तीव्रतेचे गुण. Brewers एका वेळी एक malt वाचायला ती वापरतात. ती एकावर एक रचली की अधिक रोचक गोष्ट मिळते: एक table जिथे प्रत्येक malt म्हणजे आकड्यांची एक ओळ. GenAI च्या भाषेत ते embedding आहे, फक्त माणसाला वाचता येईल असे.

याच्याशी खेळण्यासाठी एक छोटे open tool बनवताना मी त्यापैकी 51 wheels 0 ते 5 scale वरील 22-descriptor vectors मध्ये digitise केली. [Malt flavour wheels रचण्यावरच्या]({{ '/mr/2026/predicting-beer-flavour-malt-coa-flavour-wheels/' | relative_url }}) आधीच्या पोस्टने grist ला भारित बेरीज म्हणून पाहण्याचा मुद्दा मांडला होता. ही पोस्ट त्या आकड्यांवर vector search आणि blending नीट केल्यावर काय होते, आणि भोळी आवृत्ती कुठे शांतपणे अपयशी ठरते, याबद्दल आहे.

## Wheel म्हणजे vector

प्रत्येक malt अशी एक ओळ बनतो, इथे काही descriptors पुरती छाटलेली:

| malt | coffee | dark chocolate | bready | honey | toffee | ... |
|---|---|---|---|---|---|---|
| Pilsner Malt | 0.0 | 1.0 | 2.0 | 1.0 | 1.5 | ... |
| CARAFA Special Type 2 | 4.0 | 3.0 | 4.0 | 1.5 | 2.5 | ... |

अशा काही डझन ओळी table मध्ये ठेवल्या की दोन उपयुक्त प्रश्न एका ओळीचे होतात. कोणता malt याच्यासारखा सर्वात जास्त आहे? आणि या grist चा वास कसा असेल?

RAG system text embeddings वर ज्या क्रिया करते त्याच या आहेत, similarity search आणि संयोजन, फक्त इथे मितींना नावे आहेत. म्हणून vector गणित कसे वागते हे शिकण्यासाठी ही फार चांगली जागा आहे, कारण प्रत्येक निकाल brewer च्या माहितीशी ताडून पाहता येतो.

## सापळा 1: raw cosine नुसार प्रत्येक malt सारखाच

Vectors ची तुलना करण्याची default पद्धत cosine similarity आहे. ती लांबी दुर्लक्षित करून त्यांच्यातील कोन मोजते, आणि 1 (एकच दिशा) पासून उणे 1 (विरुद्ध दिशा) पर्यंत जाते.

Raw wheel vectors वर malts च्या प्रत्येक जोडीतील median cosine similarity **0.91** आहे. Pilsner malt आणि CARAFA Special Type 2, म्हणजे एक फिका base malt आणि एक dehusked roasted malt, यांना **0.82** मिळते. त्या मापाने ते जवळचे नातेवाईक ठरतात.

कारण सोपे आहे. प्रत्येक wheel मध्ये बहुतेक descriptors वर कमी गुणांचा एक पाया असतो: थोडे bready, थोडे sweet, थोडे honey. सगळे vectors साधारण एकाच दिशेला बोट दाखवतात कारण तो तळ सगळ्यांचा सामायिक आहे. Cosine सामायिक तळ पाहतो आणि वरचा फरक चुकवतो.

उपाय म्हणजे vectors **centre** करणे: तुलना करण्याआधी प्रत्येकातून सरासरी malt वजा करा. आता प्रत्येक vector सांगतो की एखादा malt सामान्य malt पेक्षा कसा वेगळा आहे. Pilsner विरुद्ध CARAFA Special 2 **उणे 0.66** वर येतो, बरोबरपणे विरुद्ध. Pilsner विरुद्ध Munich Type 1 0.44 वर येतो, संबंधित पण वेगळा, जे साधारण brewer सुद्धा म्हणेल.

RAG systems मधील text embeddings बरोबरही हेच घडते, तिथे त्याला anisotropy म्हणतात: सगळे जागेच्या एकाच कोपऱ्यात जमा होते आणि गुण असायला हवेत त्यापेक्षा जास्त दिसतात. Malt बरोबर ते पाहणे खूप सोपे आहे.

## सापळा 2: variants एकाच vector वर कोसळतात

51 malts पैकी फक्त **40 वेगळे vectors** आहेत. Weyermann एका कुटुंबातील अनेक malts साठी एकच wheel प्रकाशित करते, म्हणून CARAMUNICH Types 1, 2 आणि 3 एकच wheel वाटून घेतात, आणि तीन CARAFA Special types सुद्धा. त्यांची एकमेकांशी cosine similarity नेमकी 1.0 आहे.

ही डेटाची चूक नाही. स्रोत तेच सांगतो. पण याचा अर्थ असा की "CARAMUNICH Type 2 सारखे काहीतरी" यासाठी फक्त aroma वरचा search आनंदाने Type 1 किंवा Type 3 परिपूर्ण जुळणारे म्हणून देईल, जरी हे कुटुंब 80 ते 160 EBC पर्यंत पसरलेले असले आणि Type 2 110 ते 130 वर बसत असला. CARAFA Special एकाच सामायिक wheel वर 800 ते 1,500 EBC व्यापतो. Vectors मध्ये aroma असतो. रंग, extract किंवा enzyme activity नसते.

म्हणून पर्यायी malt चा search **hybrid** असायला हवा: आधी specification वर कडक filters (रंग पट्टा, extract, कमाल addition दर), मग उरलेल्यांची क्रमवारी vector similarity ने. Documents वरील RAG साठी हाच नमुना आहे, जिथे अर्थानुसार क्रमवारी लावण्याआधी तारीख किंवा स्रोतासारख्या metadata ने filter करता. दोन्ही ठिकाणी, जी गोष्ट महत्त्वाची आहे ती vector मध्ये नसेल तर शुद्ध vector search आत्मविश्वासाने मूर्खपणा परत देईल.

## सापळा 3: सरासरी specialty malt लपवते

आता blend करा. Grist साठी स्पष्ट मॉडेल म्हणजे वस्तुमान-भारित सरासरी: 90% Pilsner, 10% CARAFA Special 2, म्हणजे प्रत्येक descriptor = 0.9 गुणिले Pilsner चे गुण अधिक 0.1 गुणिले CARAFA चे गुण.

Coffee साठी यातून **5 पैकी 0.4** येते. Pilsner मध्ये शून्य आणि CARAFA मध्ये 4, म्हणून सरासरी म्हणते अगदी पुसटशी छटा. ज्या brewer ने बिअरमध्ये 10% गडद roasted malt घातला आहे त्याला माहीत आहे की ती पुसटशी छटा नसते. प्रभावी malts चे छोटे प्रमाणही आपल्या वजनापेक्षा खूप जास्त परिणाम करते.

चांगले मॉडेल दोन गोष्टी करते. ते प्रत्येक malt ला त्याच्या वाट्यासोबत aroma **potency** नुसारही वजन देते (roasted malts base malts पेक्षा कित्येक पट प्रभावी मानले जातात), आणि सर्वात मजबूत एकट्या योगदानाला सरासरीत विरघळू न देता दिसू देते. मी वापरलेल्या calibration सह यातून coffee साधारण **2.6** वर येते, स्पष्टपणे उपस्थित, आणि 100% Pilsner grist अजूनही Pilsner चे स्वतःचेच wheel पुन्हा देतो.

त्या मॉडेलमधील constants हे अनुभवावर आधारित निर्णय आहेत, असे बसवलेले की एकटे malts आपले स्वतःचे wheels पुन्हा देतील आणि ओळखीचे grists कागदावर साधारण बरोबर चवीचे वाटतील. त्याची प्रामाणिक स्थिती इतकीच: calibrated knobs असलेली एक समजूतदार रचना, निसर्गाचा नियम नव्हे.

## GenAI कुठे बसते

हे असे प्रकरण आहे जिथे vector गणित साध्या code मध्येच राहावे, आणि बोलण्याचे काम language model करते:

- **भाकीत समजावणे.** Blend केलेला vector आणि प्रत्येक नोंदीसाठी सर्वात मोठे योगदान दिले की LLM tasting-शैलीचा सारांश लिहिते: "roast पुढे, CARAFA मधून coffee आणि dark chocolate, खाली bready malt". त्याला दिलेल्या आकड्यांचे ते वर्णन करते. ते आकडे स्वतः रचत नाही.
- **मोकळा मजकूर descriptors शी जोडणे.** Brewers malts चे वर्णन आपल्या शब्दांत करतात. LLM "toasty, थोडेसे digestive biscuits सारखे" हे biscuit आणि bready अक्षांवर बसवू शकते, म्हणजे text query ने numeric vectors शोधता येतात.
- **Text embeddings शी जोड.** Tasting notes, पुरवठादारांची वर्णने आणि स्पर्धांचा अभिप्राय text म्हणून embed करून numeric wheels सोबत शोधता येतात. तिथे vector database आपली किंमत वसूल करू लागतो. फक्त 51 malts साठी एक table आणि code च्या काही ओळी भरपूर आहेत.

## हे कुठे मोडते

**Wheels wort चे वर्णन करतात, बिअरचे नाही.** प्रकाशित wheels congress-शैलीच्या wort साठी किंवा संपूर्ण दाण्यासाठी आहेत. Fermentation, hopping आणि वेळ यांमुळे ग्लासपर्यंत काय टिकते ते बदलते. त्यांच्यावरचे कोणतेही भाकीत malt च्या योगदानाबद्दल आहे, तयार बिअरबद्दल नाही.

**Wheel digitise करणे हेच एक मोजमाप आहे.** छापील chart वरून तीव्रता वाचणे, डोळ्यांनी किंवा vision model ने, प्रत्येक descriptor मागे कदाचित अर्ध्या गुणाची चूक आणते. Vectors अंदाजे माना.

**जाणीव रेषीय नसते.** Aromas एकमेकांना झाकतात, वाढवतात आणि दाबतात. कोणतीही भारित बेरीज ते पूर्णपणे पकडत नाही, म्हणूनच potency मॉडेल हे derivation नसून calibration आहे.

**अधिकृत उत्पादन नाही.** Maltster च्या प्रकाशित साहित्यावरून काढलेले vectors म्हणजे त्याचे स्वतंत्र वाचन. त्यांना maltster ची मान्यता नाही आणि तशी असल्यासारखे ते मांडू नयेत.

## सार

Vector search शिकणाऱ्या कोणासाठीही malt aroma wheels ही देणगी आहे, कारण प्रत्येक मितीला brewer ला समजणारे नाव आहे. ते नेहमीचे सापळेही उघडपणे दाखवतात: raw cosine सगळ्यांची स्तुती करतो, vectors मध्ये तुम्ही घातले तेवढेच असते, आणि सरासरी मजबूत अल्पसंख्यांना गाडून टाकते. तुलनेआधी centre करा, क्रमवारीआधी specification वर filter करा, blend आधी potency नुसार वजन द्या, आणि language model ला आकडे रचू न देता ते समजावू द्या.

या मालिकेत पुढे: [250 सार्वजनिक homebrew recipes चे scraping आणि trend-mining]({{ '/mr/2026/scraping-trend-mining-250-homebrew-recipes/' | relative_url }}). Hops साठी, म्हणजे बहिणीसारख्या समस्येसाठी, [AI for Hop Aroma Profiling and Smart Substitution]({{ '/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}) पाहा. पूर्ण यादी [The Brewer's Agent मालिकेच्या पानावर]({{ '/series/brewers-agent/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**पर्यायी malt शोधण्यासाठी vector similarity वापरता येते का?**
हो, काळजीपूर्वक. प्रत्येक malt चे aroma wheel descriptor तीव्रतांच्या vector मध्ये बदला आणि जवळचे जुळणारे शोधण्यासाठी vectors ची तुलना करा. आधी vectors सरासरी malt वर centre करा, कारण raw cosine similarity जवळपास प्रत्येक जोडीला सारखी ठरवते. रंग आणि extract यांना कडक अटी म्हणून filter करा, म्हणजे aroma जुळले तरी चुकीच्या रंगाचा malt सुचवला जाणार नाही.

**Aroma vectors ची सरासरी specialty malts ला कमी का लेखते?**
कारण मजबूत पण अल्पसंख्य स्वभाव base malt च्या वस्तुमानात पातळ होतो. 90% Pilsner आणि 10% roasted malt च्या grist मध्ये साधी वस्तुमान-भारित सरासरी 0 ते 5 scale वर coffee 0.4 वर ठेवते, पण brewers ना माहीत आहे की 10% गडद roasted malt स्पष्टपणे जाणवतो. जे मॉडेल aroma potency नुसार वजन देते आणि सर्वात मजबूत योगदान दिसू देते ते साधारण 2.6 देते.

**Malt aroma vectors vector database मध्ये ठेवावेत का?**
काही डझन malts साठी नाही. एक table आणि code च्या काही ओळी पुरेशा आहेत. Vector database तेव्हा उपयोगी ठरतो जेव्हा तुम्ही अनेक स्रोत एकत्र करता, जसे शेकडो malts, hop descriptors आणि text embeddings म्हणून tasting notes, आणि त्या सगळ्यांवर filtered search हवा असतो.
