---
layout: post
lang: mr
title: "250 सार्वजनिक Homebrew Recipes चे Scraping आणि Trend-Mining: जमेल तिथे Regex, गरज असेल तिथेच LLM"
image: /assets/og/scraping-trend-mining-250-homebrew-recipes.png
description: "The Brewer's Agent चा भाग 4. नुकत्याच शेअर केलेल्या 250 homebrew recipes वरचा एक छोटा data engineering प्रकल्प: सभ्य scraping, parsing चे सापळे, base units मध्ये normalise करणे, regex LLM ला कधी हरवते आणि कधी नाही, डेटा 12 वेळा नापास झालेली सुसंगतता तपासणी, आणि 2025 व 2026 च्या ब्रूइंगबद्दल recipes खरोखर काय सांगतात."
date: 2026-09-05 09:00:00 -0700
updated: 2026-09-05
permalink: /mr/2026/scraping-trend-mining-250-homebrew-recipes/
tags: [brewing-science, brewers-agent, data-engineering, generative-ai, recipe-design]
faq:
  - q: "सार्वजनिक homebrew recipe sites scrape करणे योग्य आहे का?"
    a: "फक्त site च्या अटी आणि robots.txt च्या मर्यादेत, हळू request दराने, आणि पुनर्प्रकाशनासाठी नव्हे तर विश्लेषणासाठी. Login न करता सार्वजनिक असलेली पाने scrape करा, स्वतःची ओळख द्या, जे fetch केले ते cache करा म्हणजे एकच पान दोनदा मागवले जाणार नाही, आणि लोकांच्या recipes copy करण्याऐवजी एकत्रित निष्कर्ष प्रकाशित करा."
  - q: "Recipe डेटा parse करण्यासाठी LLM वापरावे की regular expressions?"
    a: "Gravity, bitterness आणि प्रमाण यांसारख्या संरचित fields साठी regular expressions आणि साधे parsing वापरा, कारण ते जलद, मोफत आणि अचूक आहेत. गोंधळलेल्या भागांसाठी LLM वापरा, जसे अनेक प्रकारे लिहिलेली hop आणि yeast नावे सोडवणे, आणि त्याचा output ओळखीच्या varieties च्या यादीविरुद्ध तपासा."
  - q: "नुकत्याच 250 homebrew recipes नी trends बद्दल काय दाखवले?"
    a: "26 recipes सह American IPA सर्वाधिक शेअर केलेली style होती, सर्वाधिक वापरलेल्या hops मध्ये Citra आणि Cascade 84 आणि 83 वापरांसह जवळपास बरोबरीत होते, आणि दोन clean American ale yeasts नी जवळपास एक चतुर्थांश recipes व्यापल्या. 13 recipes सह Hazy आणि New England IPA हा सर्वात स्पष्ट आधुनिक trend होता. हा एका site चा अलीकडचा feed आहे, म्हणून याला जनगणना नव्हे तर संकेत माना."
---

**थोडक्यात उत्तर: नुकत्याच शेअर केलेल्या 250 homebrew recipes हा एक चांगला छोटा data engineering प्रकल्प आहे, आणि त्यातले बहुतेक काम scraping नाही. ते parsing आहे: एका ओळीत दोन-दोन छापलेले stats, "7 lbs 14.00 oz" सारखी प्रमाणे, asterisk ने चिन्हांकित custom ingredients, आणि तीन प्रकारे लिहिलेला एकच hop. संरचित fields साध्या code ने parse करा, सगळे base units मध्ये normalise करा, LLM फक्त गोंधळलेली नावे सोडवण्यासाठी वापरा, आणि डेटा स्वतःशीच ताडून पाहा (12 recipes चा ABV त्यांच्याच gravities शी जुळत नव्हता). निष्कर्ष: American IPA आघाडीवर, Citra आणि Cascade अगदी बरोबरीत, आणि hazy IPA हा खरोखर पुढे सरकणारा trend.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="250 homebrew recipes साठी एक pipeline. सार्वजनिक पानांचे सभ्य scraping raw cache मध्ये, मग regex ने संरचित fields चे parsing, मग किलोग्रॅम, लिटर आणि ग्रॅम प्रति लिटर अशा base units मध्ये normalise, मग ओळखीच्या यादीविरुद्ध तपासलेल्या LLM ने गोंधळलेली hop आणि yeast नावे सोडवणे, मग सुसंगतता तपासणी, जिथे 12 recipes चा ABV त्यांच्याच gravities पेक्षा 0.3 गुणांहून अधिक वेगळा होता, मग trends एकत्र करणे. मुख्य निकाल: American IPA 26 recipes, Citra 84 वापर, Cascade 83 वापर, hazy IPA 13 recipes.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">250 RECIPES, सहा पायऱ्या, LLM लागणारा एकच भाग</text>
<g font-family="sans-serif">
<rect x="20" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="94" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">सभ्य scraping</text>
<text x="94" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">सार्वजनिक पाने, cached</text>
<rect x="183" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="257" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">parse</text>
<text x="257" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">labels वर regex</text>
<rect x="346" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="420" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">normalise</text>
<text x="420" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">kg, L, g/L, &#176;P</text>
<rect x="509" y="60" width="148" height="80" rx="9" fill="#06483f"/>
<text x="583" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">नावे सोडवा</text>
<text x="583" y="112" text-anchor="middle" font-size="10" fill="#cfe6df">LLM + ओळखीची यादी</text>
<rect x="672" y="60" width="148" height="80" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="746" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">तपासा</text>
<text x="746" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">12 ABV विसंगती</text>
<rect x="835" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="909" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">एकत्र करा</text>
<text x="909" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">trends, copies नव्हे</text>
<g font-size="11" fill="#06483f">
<rect x="20" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="135" y="198" text-anchor="middle" font-weight="700">American IPA</text><text x="135" y="220" text-anchor="middle">26 recipes, आघाडीची style</text>
<rect x="266" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="381" y="198" text-anchor="middle" font-weight="700">Citra 84 &#183; Cascade 83</text><text x="381" y="220" text-anchor="middle">hop वापर, अगदी बरोबरीत</text>
<rect x="512" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="627" y="198" text-anchor="middle" font-weight="700">2 ale yeasts</text><text x="627" y="220" text-anchor="middle">250 पैकी 58 recipes</text>
<rect x="758" y="170" width="225" height="70" rx="9" fill="#f0f6f5"/>
<text x="870" y="198" text-anchor="middle" font-weight="700">Hazy / NEIPA</text><text x="870" y="220" text-anchor="middle">13 recipes, पुढे सरकणारा</text>
</g>
<rect x="20" y="268" width="963" height="46" rx="10" fill="#06483f"/>
<text x="500" y="296" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SCRAPING ला एक तास लागतो &#183; PARSING ला पूर्ण वीकेंड</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">2026 च्या मध्यात एका सार्वजनिक site वरून घेतलेल्या, सर्वात अलीकडे शेअर केलेल्या 250 recipes मधील आकडे. एका समुदायाचा संकेत, ब्रूइंगची जनगणना नव्हे.</figcaption>
</figure>

Code लिहिणाऱ्या प्रत्येक brewer ला कधी ना कधी जाणून घ्यायचे असते की बाकीचे सगळे काय brew करत आहेत. Recipe-sharing sites हजारो recipes उघडपणे प्रकाशित करतात, आणि सगळ्या ओढून language model ला trends विचारण्याचा मोह होतो. मी एक छोटी, अधिक काळजीपूर्वक आवृत्ती केली: एका सार्वजनिक site वरील सर्वात अलीकडे शेअर केलेल्या 250 recipes. तो एक नेटका, पूर्ण data engineering सराव ठरला, ज्यात एका ठिकाणी LLM खरोखर मदत करते आणि अनेक ठिकाणी त्याने गोष्टी बिघडवल्या असत्या.

## सभ्यपणे scrape करा, नाहीतर करूच नका

कोणताही code लिहिण्याआधी तीन तपासण्या:

1. **robots.txt आणि वापराच्या अटी वाचा.** Site नाही म्हणत असेल तर प्रकल्प तिथेच थांबतो.
2. **फक्त सार्वजनिक पाने.** इतरांचा मजकूर scrape करण्यासाठी login नाही, paywalls ना वळसा घालणे नाही.
3. **विश्लेषण, पुनर्प्रकाशन नव्हे.** लोकांनी या recipes आपल्या समुदायासोबत शेअर केल्या. एकत्रित आकडे प्रकाशित करणे योग्य आहे. त्यांच्या recipes घाऊकपणे पुन्हा post करणे नाही.

मग ठसा छोटा ठेवा: संपर्क पत्त्यासह खरा user agent, दर दोन-तीन सेकंदांनी एक request, आणि local cache म्हणजे प्रत्येक पान नेमके एकदाच fetch होईल. नवीन-आधी listing पानांवर प्रत्येकी साधारण 20 recipes होत्या, म्हणून 250 recipes म्हणजे डझनभर listing पाने आणि 250 detail पाने. हळू गतीने तासाभराचे काम. कोणाच्याही server ला तुमची जाणीवही होऊ नये.

## Parsing चे सापळे

वेळ इथेच गेला. Recipe पाने माणसांसाठी लिहिलेली असतात, आणि माणसांना सुसंगत formatting ची गरज नसते.

**एका ओळीत दोन stats.** पानावर "Batch Size: 5.00 gal" आणि "Style: American IPA" कोणत्याही विभाजकाशिवाय एकाच ओळीत छापलेले होते. ओळींवर तोडले तर मूर्खपणा हाती येतो. उपाय म्हणजे labels वरच anchor करणे आणि पुढच्या ओळखीच्या label पर्यंत वाचणे.

**मिश्र-एकक प्रमाणे.** Grain ची प्रमाणे "7 lbs 14.00 oz", "12.00 oz" किंवा "3 lbs" अशी आली. 250 recipes मध्ये 529 grain ओळींनी pounds आणि ounces एकत्र वापरले, 276 नी फक्त ounces आणि 189 नी फक्त pounds. पहिला आकडा आणि पहिले एकक वाचणारा parser 7 pounds घेतो आणि शांतपणे 14 ounces गमावतो.

**Custom ingredients.** जे brewers स्वतःचा ingredient define करतात त्याच्या आधी asterisk लागतो. Asterisk तसाच ठेवला तर "*Safale US-05" आणि "Safale US-05" दोन वेगळे yeasts म्हणून मोजले जातात.

**भरकटलेली whitespace.** नावांमधल्या दुहेरी spaces कोणत्याही मोजणीत एका hop चे दोन करतात. काहीही एकत्र करण्याआधी whitespace एकवटा.

**प्रकार शीर्षकात.** Recipe all-grain आहे की extract, हे field नसून शीर्षक ओळीतला शेवटचा शब्द होता. नोंदीसाठी, 250 पैकी 243 all-grain होत्या.

## Base units मध्ये, एकदाच normalise करा

प्रत्येक प्रमाण आत येतानाच रूपांतरित केले: grain किलोग्रॅममध्ये, hops ग्रॅममध्ये, आकारमान लिटरमध्ये, आणि hop दर ग्रॅम प्रति लिटरमध्ये, म्हणजे 5-gallon homebrew आणि 20-लिटरची batch यांची तुलना करता येते. Gravities site ने दिल्या तशाच ठेवल्या (specific gravity), आणि तपासलेल्या रूपांतराने Plato column काढला.

हा [भाग 2 मधील calculation tools]({{ '/mr/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) सारखाच नियम आहे: आत base units, कडेला display units. एकाच ठिकाणी, tests असलेल्या code मध्ये रूपांतर केले की trend chart कधीच शांतपणे ounces आणि ग्रॅम मिसळत नाही.

## जमेल तिथे Regex, गरज असेल तिथेच LLM

आता प्रत्येक पान language model कडे फेकून JSON मागणे सोपे झाले आहे. या कामासाठी ते बहुतेक fields वर हळू, महाग आणि कमी अचूक ठरले असते.

**संरचित fields: साधा code.** Original gravity, final gravity, ABV, IBU, रंग, प्रमाणे आणि boil वेळा ठरलेल्या labels शेजारी असतात. Regular expressions ती नेमकी, मोफत, मिलिसेकंदात काढतात. LLM अधूनमधून आकडा round करेल, दशांश गाळेल किंवा "मदत म्हणून" एकक बदलेल.

**नावे: इथे LLM आपली जागा कमावते.** Hop आणि yeast ची नावे म्हणजे गोंधळ. या नमुन्यात "Amarillo Gold" (49 वापर) आणि "Amarillo" (27) हा दोन नावांनी विकला जाणारा एकच hop आहे, आणि "Fuggle" व "Fuggles" 16 आणि 16 असे विभागले. Yeasts लॅब code, brand नाव किंवा टोपणनावाने दिसतात. ते सोडवणे म्हणजे क्षेत्रज्ञानासह fuzzy matching, जे language models चांगले करतात.

ते वापरण्याचा सुरक्षित मार्ग: मॉडेलला मूळ नाव आणि ओळखीच्या varieties ची यादी द्या, त्यातून एक निवडायला किंवा "unknown" म्हणायला सांगा, आणि यादीत नसलेले नाव कधीच स्वीकारू नका. मॉडेल जोडते. यादी ठरवते.

प्रकाशित आकड्यांसाठी मी खरे तर Amarillo आणि Amarillo Gold वेगळेच ठेवले आणि तसे सांगितले, कारण ते एकत्र करणे हा निर्णय आहे आणि वाचकाला तो दिसायला हवा. असा निर्णय pipeline मध्ये गाडण्याऐवजी दृश्य ठेवणे योग्य.

## डेटा स्वतःशीच ताडून पाहा

Scrape केलेल्या डेटामध्ये स्वतःच्या चुका असतात, आणि ब्रूइंग डेटामध्ये एक अंगभूत तपासणी असते: ABV original आणि final gravity वरून निघायला हवा. Homebrew मधील नेहमीचे अंदाजी सूत्र वापरून (gravity मधील घट गुणिले 131.25), 250 पैकी 12 recipes चा ABV त्यांच्याच gravities नुसार यायला हवा त्यापेक्षा 0.3 गुणांहून अधिक दूर होता.

याचा अर्थ 12 brewers नी चुका केल्या असा नाही. Recipe software एकापेक्षा जास्त ABV सूत्रे देते, काही brewers आकडा हाताने बदलतात, आणि काही recipes जुन्या आकड्यांसह templates असतात. याचा अर्थ इतकाच की ABV column वर डोळे झाकून विश्वास ठेवू नका, आणि ABV चा trend chart gravities वरून, एकाच सांगितलेल्या सूत्राने बनवावा.

## 250 recipes काय म्हणाल्या

हा एका site चा अलीकडचा feed आहे, ही अट लक्षात ठेवून:

- **Styles:** 26 recipes सह American IPA आघाडीवर, मग 18 सह American Pale Ale. Saison, Blonde Ale, Witbier आणि Session IPA प्रत्येकी 10 वर बरोबरीत. समुदाय IPA-प्रधान आहे पण फक्त IPA चा नाही.
- **Hops:** Citra (84 वापर) आणि Cascade (83) जवळपास बरोबरीत. मागोमाग Centennial, Amarillo, Magnum, Saaz आणि Simcoe. क्लासिक American C-hops अजूनही नवीन varieties वर वर्चस्व गाजवतात.
- **Yeast:** दोन clean American ale strains नी मिळून 58 recipes व्यापल्या, नमुन्याचा जवळपास एक चतुर्थांश.
- **काय पुढे सरकत आहे:** hazy आणि New England IPA, नावाने किंवा style ने 13 recipes, इतर कोणत्याही नवीन style च्या खूप पुढे. नवीन hazy strains दिसू लागले आहेत पण अजूनही दुर्मीळ.
- **सामान्य बिअर:** median original gravity 1.055, median ABV 5.6%, median bitterness साधारण 33 IBU.

यापैकी काहीही homebrew स्पर्धांमध्ये परीक्षण करणाऱ्या कोणालाही आश्चर्यचकित करणार नाही. ते ठीक आहे. मूल्य एखाद्या साक्षात्कारात नाही, तर हे डेटा म्हणून हाती असण्यात आहे जे पुढच्या तिमाहीत पुन्हा चालवून तुलना करता येते.

## हे कुठे मोडते

**एक site म्हणजे एक समुदाय.** Recipes सार्वजनिकपणे शेअर करणारे सगळे brewers नसतात. व्यावसायिक breweries अनुपस्थित आहेत, आणि काही styles जास्त दिसतात कारण त्यांच्या brewers ना शेअर करायला आवडते.

**अलीकडचे म्हणजे प्रातिनिधिक नव्हे.** काही महिन्यांचा नवीन-आधी feed ऋतूनुसारचे ब्रूइंग पकडतो. हिवाळ्यात पुन्हा चालवा, stouts वर येतील.

**नावे अजूनही निर्णयाचा भाग आहेत.** Spellings एकत्र करणे, hazy आणि NEIPA एका गटात ठेवणे, "Session IPA" ही स्वतंत्र style आहे का ते ठरवणे: प्रत्येक निर्णय आकडा बदलतो. निकालांसोबत नियमही प्रकाशित करा.

**अटी बदलतात.** आज सभ्य crawling ला परवानगी देणारी site उद्या देईलच असे नाही. प्रत्येक पुनर्धावणीआधी पुन्हा तपासा.

## सार

Scraping हा सोपा तास होता. वीकेंड गेला एका ओळीत दोन छापलेल्या stats वर, pounds-आणि-ounces प्रमाणांवर, asterisks वर आणि तीन नावे असलेल्या एका hop वर, आणि कोणत्याही खऱ्या data engineering कामात हेच सामान्य असते. संरचित fields साध्या code ने parse करा, तपासलेल्या functions मध्ये एकदाच normalise करा, गोंधळलेल्या नावांसाठी LLM वापरा पण त्याला निवडायला एक यादी द्या, आणि डेटा त्याच्याच भौतिकशास्त्राशी ताडून पाहा. मग trend chart पाहण्यालायक ठरतो.

या blog वर आधी: [Can AI Design a Beer Recipe?]({{ '/2026/can-ai-design-a-beer-recipe/' | relative_url }}) ने generation पाहिले होते. ही पोस्ट generator ला लागणाऱ्या डेटाबद्दल होती. या मालिकेत पुढे: [ब्रूइंग सहायकासाठी evals]({{ '/mr/2026/evals-for-a-brewing-assistant/' | relative_url }}). पूर्ण यादी [The Brewer's Agent मालिकेच्या पानावर]({{ '/series/brewers-agent/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**सार्वजनिक homebrew recipe sites scrape करणे योग्य आहे का?**
फक्त site च्या अटी आणि robots.txt च्या मर्यादेत, हळू request दराने, आणि पुनर्प्रकाशनासाठी नव्हे तर विश्लेषणासाठी. Login न करता सार्वजनिक असलेली पाने scrape करा, स्वतःची ओळख द्या, जे fetch केले ते cache करा म्हणजे एकच पान दोनदा मागवले जाणार नाही, आणि लोकांच्या recipes copy करण्याऐवजी एकत्रित निष्कर्ष प्रकाशित करा.

**Recipe डेटा parse करण्यासाठी LLM वापरावे की regular expressions?**
Gravity, bitterness आणि प्रमाण यांसारख्या संरचित fields साठी regular expressions आणि साधे parsing वापरा, कारण ते जलद, मोफत आणि अचूक आहेत. गोंधळलेल्या भागांसाठी LLM वापरा, जसे अनेक प्रकारे लिहिलेली hop आणि yeast नावे सोडवणे, आणि त्याचा output ओळखीच्या varieties च्या यादीविरुद्ध तपासा.

**नुकत्याच 250 homebrew recipes नी trends बद्दल काय दाखवले?**
26 recipes सह American IPA सर्वाधिक शेअर केलेली style होती, सर्वाधिक वापरलेल्या hops मध्ये Citra आणि Cascade 84 आणि 83 वापरांसह जवळपास बरोबरीत होते, आणि दोन clean American ale yeasts नी जवळपास एक चतुर्थांश recipes व्यापल्या. 13 recipes सह Hazy आणि New England IPA हा सर्वात स्पष्ट आधुनिक trend होता. हा एका site चा अलीकडचा feed आहे, म्हणून याला जनगणना नव्हे तर संकेत माना.
