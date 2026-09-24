---
layout: post
lang: mr
title: "बेरीज स्वतः न करता गणनेची tools वापरणारा agent"
image: /assets/og/brewing-agent-calculation-tools-not-sums.png
description: "The Brewer's Agent चा भाग 2. ब्रूइंग सहायकाला gravity, attenuation, ABV आणि IBU साठी tools द्या, आणि प्रत्येक वेळी पद्धतीचे नाव सांगायला लावा. उदाहरणे कारण दाखवतात: तीच बिअर एका scale वर 64.9% आणि दुसऱ्या scale वर 78.6% attenuated दिसते, आणि एकाच hop addition साठी तीन IBU मॉडेल 34, 45 आणि 46 देतात."
date: 2026-08-26 09:00:00 -0700
updated: 2026-08-26
permalink: /mr/2026/brewing-agent-calculation-tools-not-sums/
tags: [brewing-science, brewers-agent, generative-ai, tool-use, brewing-calculations]
faq:
  - q: "ब्रूइंग AI सहायकाने गणनेसाठी tools का वापरावीत?"
    a: "कारण language models अनेक पायऱ्यांच्या अंकगणितात भरवशाची नसतात, आणि ब्रूइंगच्या सूत्रांमध्ये एकक आणि तापमानाचे असे संकेत असतात जे सहज गोंधळतात. Tool म्हणजे साधा, तपासलेला code: तो सांगितलेल्या एककांत inputs घेतो, एक दस्तऐवजीकृत पद्धत लावतो आणि त्या पद्धतीच्या नावासह निकाल परत देतो. कोणते tool बोलवायचे ते मॉडेल ठरवते आणि उत्तर समजावून सांगते."
  - q: "Real आणि apparent degree of fermentation मध्ये काय फरक आहे?"
    a: "Apparent attenuation मूळ extract ची तुलना तयार बिअरमध्ये hydrometer जो apparent extract दाखवतो त्याच्याशी करते. Alcohol पाण्यापेक्षा हलके असल्याने हे वाचन खाली ओढले जाते. Real attenuation खरा उरलेला extract वापरते. एकाच बिअरवर apparent आकडा नेहमी जास्त येतो, इथे 64.9% विरुद्ध 78.6%, म्हणून scale शिवायचा आकडा संदिग्ध असतो."
  - q: "कोणते IBU सूत्र बरोबर, Tinseth की Rager?"
    a: "सर्वसाधारणपणे दोन्हीपैकी एकही बरोबर नाही. ती वेगवेगळ्या डेटावर बसवलेली empirical सूत्रे आहेत, आणि 13 degrees Plato wort मधील 60 मिनिटांच्या addition साठी त्यांच्यात साधारण एक तृतीयांश फरक पडतो. तुमच्या brewery साठी एक निवडा, लॅबमध्ये मोजलेल्या bitterness शी त्याचे calibration करा, आणि कोणते मॉडेल वापरले ते tool कडून सांगून घ्या."
---

**थोडक्यात उत्तर: ब्रूइंग सहायकासाठी तुम्ही करू शकता ती सर्वात उपयुक्त गोष्ट म्हणजे त्याच्याकडून अंकगणित काढून घेणे. Agent ला थोडी tools द्या (gravity रूपांतर, attenuation, alcohol, bitterness). प्रत्येक tool साधा तपासलेला code असतो, base units मध्ये काम करतो आणि निकालासोबत आपली पद्धत परत देतो. Agent tool निवडतो आणि उत्तर समजावतो. खालची दोन उदाहरणे दाखवतात की पद्धत आकड्यासोबत का जायला हवी: एकच बिअर real scale वर 64.9% आणि apparent scale वर 78.6% attenuated दिसते, आणि तीन मान्यताप्राप्त IBU मॉडेल एकाच hop addition साठी 34, 45 आणि 46 देतात.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="दोन उदाहरणे. डावीकडे, 13.0 degrees Plato मूळ extract असलेली एक बिअर real degree of fermentation 64.9 टक्के आणि apparent degree of fermentation 78.6 टक्के दाखवते, एकाच बिअरवर 13.7 गुणांचा फरक. उजवीकडे, 10 टक्के alpha acid चे 30 ग्रॅम hops, 20 लिटरमध्ये 60 मिनिटे उकळल्यावर Tinseth नुसार 33.8 IBU, Rager नुसार 45.7 आणि first-order kinetic मॉडेलनुसार 45.2 देतात.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">तीच बिअर, वेगळे आकडे: पद्धत निकालासोबत का जाते</text>
<g font-family="sans-serif">
<text x="245" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">ATTENUATION, एक बिअर (13.0 &#176;P)</text>
<rect x="60" y="90" width="260" height="36" rx="5" fill="#4db6a2"/>
<text x="70" y="113" font-size="12" font-weight="700" fill="#06483f">real (RDF)</text>
<text x="330" y="113" font-size="13" font-weight="700" fill="#06483f">64.9%</text>
<rect x="60" y="140" width="314" height="36" rx="5" fill="#06483f"/>
<text x="70" y="163" font-size="12" font-weight="700" fill="#ffffff">apparent (ADF)</text>
<text x="384" y="163" font-size="13" font-weight="700" fill="#06483f">78.6%</text>
<text x="245" y="208" text-anchor="middle" font-size="11" fill="#ff4081" font-weight="700">13.7 गुणांचा फरक, तीच टाकी</text>
<text x="745" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">IBU, एक HOP ADDITION</text>
<text x="745" y="76" text-anchor="middle" font-size="10" fill="#4a6b64">30 g, 10% alpha, 20 L, 60 min</text>
<rect x="560" y="90" width="203" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="113" font-size="12" font-weight="700" fill="#06483f">Tinseth</text>
<text x="773" y="113" font-size="13" font-weight="700" fill="#06483f">33.8</text>
<rect x="560" y="140" width="274" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="163" font-size="12" font-weight="700" fill="#06483f">Rager</text>
<text x="844" y="163" font-size="13" font-weight="700" fill="#06483f">45.7</text>
<rect x="560" y="190" width="271" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="213" font-size="12" font-weight="700" fill="#06483f">kinetic मॉडेल</text>
<text x="841" y="213" font-size="13" font-weight="700" fill="#06483f">45.2</text>
<rect x="40" y="258" width="920" height="54" rx="10" fill="#06483f"/>
<text x="500" y="282" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">यापैकी एकही आकडा चुकीचा नाही &#183; पण पद्धतीशिवाय प्रत्येक आकडा निरर्थक आहे</text>
<text x="500" y="300" text-anchor="middle" font-size="10.5" fill="#cfe6df">base units मध्ये तपासलेल्या code ने मोजले; IBU आकडे cellar losses आधीचे wort अंदाज आहेत</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">जो सहायक पद्धत न सांगता "attenuation 78% आहे" किंवा "साधारण 40 IBU" म्हणतो, त्याने प्रश्नाचे उत्तर दिलेलेच नाही.</figcaption>
</figure>

एक brewer सहायकाला विचारतो: "batch 212 ला किती attenuation मिळाले?" प्रामाणिक उत्तर म्हणजे दुसरा प्रश्न: कोणते attenuation? लॅब report सहसा real degree of fermentation देतो. Homebrewer किंवा sales sheet सहसा apparent अभिप्रेत धरतात. आकृतीतल्या बिअरवर हे 64.9% आणि 78.6% आहेत. तीच टाकी, तोच दिवस, तोच नमुना.

Language model ला एकटे सोडले तर ते शांतपणे यापैकी एक निवडेल, आणि कदाचित वाटेत रूपांतर मनातच करेल. [या मालिकेतील पहिल्या पोस्टने]({{ '/mr/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }}) मांडले होते की ज्ञान retrieval ने पुरवावे आणि आकडे code ने. ही पोस्ट तो code बांधते.

## Tool म्हणजे काय

आजच्या agent frameworks मध्ये (Claude आणि OpenAI APIs, Model Context Protocol, बहुतेक orchestration libraries), tool म्हणजे असे function जे चालवायला मॉडेल सांगू शकते. तुम्ही त्याचे नाव, हेतू आणि inputs साठी schema देऊन वर्णन करता. ते कधी आणि कोणत्या arguments सह बोलवायचे ते मॉडेल ठरवते. तुमचा code ते चालवतो आणि निकाल परत देतो.

ब्रूइंगचा toolset मोठा असण्याची गरज नाही. पाच tools बहुतेक प्रश्नांना पुरतात:

- **`gravity_convert`**: specific gravity पासून degrees Plato आणि उलट, सांगितलेल्या तापमान आधारावर.
- **`attenuation`**: मूळ, real आणि apparent extract वरून real आणि apparent degree of fermentation.
- **`alcohol`**: मूळ extract आणि RDF वरून वजनाने आणि आकारमानाने alcohol.
- **`bitterness`**: एका hop addition साठी IBU, मॉडेलचे नाव argument म्हणून.
- **`unit_convert`**: लिटर, hectolitre, barrel, किलोग्रॅम, pound, कोणताही अंदाज न लावता.

मॉडेलला एक tool असे दिसते:

```json
{
  "name": "bitterness",
  "description": "Estimate IBU in wort for one hop addition. Returns the value and the model used.",
  "input_schema": {
    "type": "object",
    "properties": {
      "hop_mass_g": {"type": "number"},
      "alpha_acid_pct": {"type": "number"},
      "volume_l": {"type": "number"},
      "boil_min": {"type": "number"},
      "wort_plato": {"type": "number"},
      "model": {"type": "string", "enum": ["tinseth", "rager", "kinetic"]}
    },
    "required": ["hop_mass_g", "alpha_acid_pct", "volume_l", "boil_min", "wort_plato", "model"]
  }
}
```

`model` field मुद्दाम आवश्यक ठेवला आहे, म्हणजे सहायक "IBU" असे मागूच शकत नाही. त्याला Tinseth IBU किंवा Rager IBU मागावे लागते. हा एक design निर्णय अचूकतेसाठी कोणत्याही prompt पेक्षा जास्त काम करतो.

## उदाहरण 1: attenuation scale चा सापळा

13.0 degrees Plato मूळ extract असलेली एक lager घ्या, जी 64.9% real degree of fermentation पर्यंत fermented झाली आहे.

Alcohol tool Balling चा संकेत वापरतो (प्रत्येक ग्रॅम alcohol साठी साधारण 2.0665 ग्रॅम extract खर्च होतो) आणि 4.77% real extract व वजनाने 4.27% alcohol काढतो. वजनावरून आकारमानाकडे जाण्यासाठी त्याला तयार बिअरची घनता लागते, जी उरलेला extract आणि alcohol दोन्हींवर एकत्र अवलंबून असते. म्हणून तो shortcut ऐवजी बिअर घनतेचे fitted मॉडेल वापरतो. त्यातून साधारण 1.0109 specific gravity आणि **5.46% ABV** मिळते.

मग attenuation tool त्या बिअरमध्ये hydrometer काय दाखवेल ते काढतो. Alcohol पाण्यापेक्षा हलके असल्याने hydrometer साधारण 2.78 degrees Plato चा apparent extract दाखवतो, खऱ्या 4.77 पेक्षा बराच कमी. Apparent degree of fermentation मूळ extract ची तुलना या वाचनाशी करते: **78.6%**. Real degree of fermentation तुलना खऱ्या उरलेल्या extract शी करते: **64.9%**.

दोन्ही आकडे बरोबर आहेत. ते वेगवेगळ्या गोष्टी मोजतात. जो brewer ही बिअर yeast पुरवठादाराच्या datasheet शी (जिथे apparent attenuation दिलेले असते) आणि लॅब report शी (जिथे real दिलेले असते) ताडून पाहतो, त्याला 13.7 गुणांचा फरक दिसेल आणि काय चुकले असा प्रश्न पडेल. काहीच चुकले नाही. कोणीतरी label गाळले.

चांगला tool दोन्ही आकडे नावासह परत देतो:

```text
attenuation(og_plato=13.0, rdf_pct=64.9)
  -> real_df_pct: 64.9, apparent_df_pct: 78.6,
     real_extract_plato: 4.77, apparent_extract_plato: 2.78,
     method: "Balling 2.0665; beer SG from extract-alcohol density model; 20/20 C"
```

## उदाहरण 2: तीन प्रामाणिक IBU आकडे

आता एक hop addition: 10% alpha acid चे 30 ग्रॅम hops, त्याच 13.0 degrees Plato wort च्या 20 लिटरमध्ये 60 मिनिटे उकळलेले (specific gravity साधारण 1.0525).

- **Tinseth** साधारण 22.5% utilisation आणि **33.8 IBU** देते.
- **Rager** साधारण 30.4% utilisation आणि **45.7 IBU** देते.
- Alpha acid isomerisation आणि degradation चे **first-order kinetic मॉडेल** (उकळबिंदूवरचे Malowicki आणि Shellhammer rate constants, gravity correction सह) wort मध्ये साधारण 30.1% alpha acid isomerised आणि **45.2 IBU** देते.

तीन प्रकाशित, मोठ्या प्रमाणावर वापरल्या जाणाऱ्या पद्धती. एकाच addition वर साधारण 12 IBU चा, म्हणजे जवळपास एक तृतीयांश, फरक. 15 मिनिटांच्या addition वर गेलात तर क्रम उलटतो: Tinseth 11.2% utilisation देते आणि Rager 8.1%.

यापैकी कोणतेही सत्य नाही. ती वेगवेगळ्या डेटावर बसवलेली empirical मॉडेल आहेत, आणि प्रत्येक आकडा cellar व packaging losses आपला वाटा घेण्याआधीचा wort मधील अंदाज आहे. सत्य म्हणजे लॅब तयार बिअरमध्ये जे मोजते ते. सहायकासाठी महत्त्वाचे इतकेच की त्याने "साधारण 40 IBU" असे जणू काही ठरल्यासारखे कधीच सांगू नये. तो "Rager नुसार 45.7 IBU, wort अंदाज" असे सांगतो, आणि Tinseth विरुद्ध calibration करणाऱ्या brewer ला लगेच कळते की हा आकडा कमी करून धरायचा.

ही मॉडेल spreadsheet मध्ये शेजारीशेजारी पाहायची असतील तर [Excel मधील IBU recipe builder]({{ '/2026/ibu-recipe-builder-excel/' | relative_url }}) अनेक additions साठी Tinseth समजावतो, आणि [machine learning ने hop bitterness चे भाकीत]({{ '/2023/predicting-hop-bitterness-ibu/' | relative_url }}) मोजलेल्या मूल्यांविरुद्ध calibration कसे करायचे ते सांगते.

## Agent ला भरवशाचा बनवणारे नियम

1. **गद्यात अंकगणित नाही.** System prompt सांगतो की इतर आकड्यांवरून काढलेला कोणताही आकडा tool call मधूनच यायला हवा. मॉडेलला shortcut घ्यायचा मोह होईल असे प्रश्न विचारून हे तपासा, आणि मागे tool call नसलेला कोणताही मोजलेला आकडा असलेले उत्तर नापास करा.
2. **आत base units, बाहेर display units.** Tools किलोग्रॅम, लिटर आणि सांगितलेल्या तापमानावरील degrees Plato मध्ये काम करतात. Pound, barrel किंवा specific gravity मध्ये रूपांतर एकदाच, कडेला होते.
3. **पद्धत हा output चाच भाग.** प्रत्येक tool वापरलेली पद्धत, constants आणि तापमान आधार परत देतो, आणि agent उत्तरात ते पुन्हा सांगतो.
4. **Tools इतर code सारखेच तपासले जातात.** प्रत्येक tool साठी प्रकाशित उदाहरणांविरुद्ध unit tests असतात. वरचे attenuation उदाहरण त्यापैकी एक आहे: त्या input साठी tool ने 4.77 real extract आणि 4.27 alcohol देणे थांबवले तर build अपयशी होतो.
5. **गृहीत धरण्याआधी विचारा.** Brewer scale न सांगता "attenuation" किंवा "gravity" म्हणाला, तर agent कोणते ते विचारतो, किंवा दोन्ही देतो.

## हे कुठे मोडते

**Tools मध्ये निवडी दडलेल्या असतात.** Balling चा constant, घनतेचे मॉडेल किंवा utilisation मॉडेल निवडणे हा तांत्रिक निर्णय आहे. Tool तो सुसंगत बनवतो, बरोबर नाही. निवडी दस्तऐवजीकृत करा आणि ज्या brewer ला अधिक माहिती आहे त्याला त्या बदलू द्या.

**वाईट inputs अजूनही वाईट outputs देतात.** चुकीच्या तापमानावर वाचलेला मूळ extract दिलेला tool अचूकपणे चुकीचे उत्तर देतो. आकडे मर्यादेबाहेर दिसले तर ते कुठून आले ते agent ने विचारायला हवे.

**Agent चुकीचे tool बोलवू शकतो.** मॉडेलला `attenuation` हवा असताना ते `alcohol` निवडू शकते, किंवा specific gravity अपेक्षित असताना Plato देऊ शकते. Field नावांमध्ये एकके असलेले कडक schema आणि खऱ्या प्रश्नांचा test set यातले बहुतेक पकडतात.

**Tools लॅबची जागा घेत नाहीत.** इथला प्रत्येक आकडा इतर मोजमापांवरून केलेली गणना आहे. विशेषतः bitterness मोजलीच पाहिजे, आणि मोजलेले मूल्य नियोजनाचा अंदाज म्हणूनच धरावे.

## सार

जो सहायक मनातच बेरीज करतो तो एक दिवस brewer ला आत्मविश्वासाच्या आवाजात चुकीचा आकडा देईल. जो सहायक tools बोलवतो तो प्रत्येक वेळी तोच आकडा, पद्धतीसह देतो. इथली उदाहरणे अपवादात्मक नाहीत: एका साध्या lager वर real आणि apparent attenuation मध्ये 13.7 गुणांचा फरक आहे, आणि तीन प्रमाणित IBU मॉडेल एकाच hop addition वर एक तृतीयांशाने वेगळे पडतात. Tool निवडणे आणि निकाल समजावणे मॉडेलवर सोडा. गणित तपासलेल्या code ला करू द्या.

या मालिकेत पुढे: [malt aroma wheels vectors म्हणून]({{ '/mr/2026/malt-aroma-wheels-as-vectors-similarity-search/' | relative_url }}). पूर्ण यादी [The Brewer's Agent मालिकेच्या पानावर]({{ '/series/brewers-agent/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**ब्रूइंग AI सहायकाने गणनेसाठी tools का वापरावीत?**
कारण language models अनेक पायऱ्यांच्या अंकगणितात भरवशाची नसतात, आणि ब्रूइंगच्या सूत्रांमध्ये एकक आणि तापमानाचे असे संकेत असतात जे सहज गोंधळतात. Tool म्हणजे साधा, तपासलेला code: तो सांगितलेल्या एककांत inputs घेतो, एक दस्तऐवजीकृत पद्धत लावतो आणि त्या पद्धतीच्या नावासह निकाल परत देतो. कोणते tool बोलवायचे ते मॉडेल ठरवते आणि उत्तर समजावून सांगते.

**Real आणि apparent degree of fermentation मध्ये काय फरक आहे?**
Apparent attenuation मूळ extract ची तुलना तयार बिअरमध्ये hydrometer जो apparent extract दाखवतो त्याच्याशी करते. Alcohol पाण्यापेक्षा हलके असल्याने हे वाचन खाली ओढले जाते. Real attenuation खरा उरलेला extract वापरते. एकाच बिअरवर apparent आकडा नेहमी जास्त येतो, इथे 64.9% विरुद्ध 78.6%, म्हणून scale शिवायचा आकडा संदिग्ध असतो.

**कोणते IBU सूत्र बरोबर, Tinseth की Rager?**
सर्वसाधारणपणे दोन्हीपैकी एकही बरोबर नाही. ती वेगवेगळ्या डेटावर बसवलेली empirical सूत्रे आहेत, आणि 13 degrees Plato wort मधील 60 मिनिटांच्या addition साठी त्यांच्यात साधारण एक तृतीयांश फरक पडतो. तुमच्या brewery साठी एक निवडा, लॅबमध्ये मोजलेल्या bitterness शी त्याचे calibration करा, आणि कोणते मॉडेल वापरले ते tool कडून सांगून घ्या.
