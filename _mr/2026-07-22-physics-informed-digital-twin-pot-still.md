---
layout: post
lang: mr
title: "pot still चा physics-informed digital twin: केवळ ML वर आधारित twins का भरकटतात"
image: /assets/og/physics-informed-digital-twin-pot-still.png
description: "The Still and the Model चा भाग 1. batch pot still Rayleigh equation पाळतो, आणि आत गेलेले alcohol बाहेर आलेल्या alcohol इतकेच असले पाहिजे. पूर्णपणे डेटावर चालणारा twin हा नियम गुपचूप कसा मोडतो, आणि रचनेसाठी physics व काही fitted parameters साठी run data वापरणारे hybrid model प्रामाणिक कसे राहते."
date: 2026-07-22 09:00:00 -0700
updated: 2026-07-22
permalink: /mr/2026/physics-informed-digital-twin-pot-still/
tags: [distilling-maturation, still-and-model, digital-twin, machine-learning, data-engineering]
faq:
  - q: "still चा physics-informed digital twin म्हणजे काय?"
    a: "असे model ज्याची रचना distillation च्या physics मधून येते, जसे Rayleigh equation आणि vapour-liquid equilibrium, आणि ज्याचे मोजके parameters distillery च्या स्वतःच्या run data वरून fit केलेले असतात. alcohol conservation सारख्या गोष्टींची हमी physics देते. data हे model या विशिष्ट still ला, त्याच्या heat input ला आणि त्याच्या condenser ला जुळवून घेतो."
  - q: "पूर्णपणे डेटावर चालणारा still twin का भरकटतो?"
    a: "केवळ मागील runs वर train झालेले machine learning model नियम नव्हे तर correlations शिकते. ते heads, hearts आणि feints चे असे volumes भाकीत करू शकते ज्यांची बेरीज charge केलेल्या alcohol पेक्षा जास्त होते, आणि charge strength किंवा heat input त्याच्या training श्रेणीबाहेर गेल्यावर काय करायचे हे त्याला कळत नाही. त्याच्या रचनेतील काहीही त्याला conservation मोडण्यापासून रोखत नाही."
  - q: "hybrid pot still model fit करायला कोणता डेटा लागतो?"
    a: "प्रत्येक run साठी: charge volume आणि strength, वेळेनुसार heat input किंवा steam flow, spirit safe वरील distillate flow आणि strength, आणि cut times. hybrid model ला लागणारे मोजके parameters fit करायला चांगल्या नोंदी असलेले काही डझन runs सहसा पुरेसे असतात, कारण बहुतेक काम physics करते."
---

**थोडक्यात उत्तर: batch pot still असे दोन नियम पाळतो ज्यांच्याशी data scientist वाटाघाटी करू शकत नाही. run पुढे सरकतो तसे pot आणि vapour कसे बदलतात याचे वर्णन Rayleigh equation करते, आणि तुम्ही charge केलेले alcohol heads, hearts, feints आणि residue मध्ये गोळा केलेल्या alcohol इतकेच असले पाहिजे. मागील runs वरील केवळ machine learning ने बांधलेल्या digital twin ला यापैकी कोणताच नियम माहीत नसतो, म्हणून परिस्थिती बदलताक्षणी तो भरकटतो आणि आत गेलेल्यापेक्षा जास्त alcohol असलेले fractions भाकीत करू शकतो. twin उलट्या पद्धतीने बांधा: रचनेसाठी physics, मोजक्या fitted parameters साठी run data. त्याला कमी डेटा लागतो, तो समजूतदारपणे extrapolate करतो, आणि तो spirit शोधून काढू शकत नाही.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="उदाहरणादाखल spirit still run. 22 टक्क्यांवरील 10,000 litres low wines च्या charge मध्ये 2,200 litres absolute alcohol आहे. hybrid twin त्याचे heads 60, hearts 1,050, feints 1,070 आणि residue 20 असे विभाजन करतो, ज्याची बेरीज 2,200 होते. केवळ machine learning twin heads 60, hearts 1,120, feints 1,110 आणि residue 20 असे भाकीत करतो, ज्याची बेरीज 2,310 होते, म्हणजे charge केलेल्यापेक्षा जास्त alcohol.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">आत गेलेले ALCOHOL = बाहेर आलेले ALCOHOL (उदाहरणादाखल RUN, ABSOLUTE ALCOHOL चे LITRES)</text>
<g font-family="sans-serif">
<rect x="40" y="110" width="200" height="90" rx="10" fill="#06483f"/>
<text x="140" y="140" text-anchor="middle" font-size="12" fill="#cfe6df">charge</text>
<text x="140" y="166" text-anchor="middle" font-size="20" font-weight="700" fill="#ffffff">2,200 LAA</text>
<text x="140" y="187" text-anchor="middle" font-size="10.5" fill="#cfe6df">22% वर 10,000 L</text>
<line x1="240" y1="155" x2="300" y2="100" stroke="#4db6a2" stroke-width="2"/>
<line x1="240" y1="155" x2="300" y2="220" stroke="#4db6a2" stroke-width="2"/>
<text x="310" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#2e9e7c">HYBRID TWIN</text>
<rect x="300" y="72" width="660" height="56" rx="9" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="330" y="106" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,050 &#183; feints 1,070 &#183; residue 20</text>
<text x="940" y="106" text-anchor="end" font-size="15" font-weight="700" fill="#2e9e7c">= 2,200 &#10003;</text>
<text x="310" y="172" font-size="11" font-weight="700" letter-spacing="1" fill="#ff4081">केवळ ML TWIN</text>
<rect x="300" y="182" width="660" height="56" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="330" y="216" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,120 &#183; feints 1,110 &#183; residue 20</text>
<text x="940" y="216" text-anchor="end" font-size="15" font-weight="700" fill="#ff4081">= 2,310 &#10007;</text>
<rect x="40" y="272" width="920" height="42" rx="10" fill="#06483f"/>
<text x="500" y="298" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">110 LITRES ALCOHOL शोधून काढू शकणारा TWIN हा TWIN नाही</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरणादाखल आकडे. प्रत्येक fraction स्वतंत्रपणे पटण्यासारखे दिसते. केवळ बेरीजच केवळ ML twin चे बिंग फोडते.</figcaption>
</figure>

digital twin project सुरू करणाऱ्या प्रत्येक distillery ला तोच pitch मिळतो: model ला काही वर्षांचा run data द्या, आणि ते run भाकीत करेल. heads volume, hearts volume, cut times, सगळे शिकलेले. गेल्या वर्षीच्या runs वरचा demo उत्कृष्ट दिसतो. मग charge नेहमीपेक्षा दीड point जास्त strong येतो, किंवा boiler दुरुस्तीनंतर steam पुरवठा बदलतो, आणि twin अशा गोष्टी सांगू लागतो ज्या निरर्थक आहेत हे stillman ला माहीत असते.

**The Still and the Model** मधील ही पहिली पोस्ट आहे. ही मालिका distillery च्या आकड्यांखालील data engineering आणि GenAI वर आहे. तिची सुरुवात twin पासून होते, कारण डेटाशी fit होणारे model आणि physics चा आदर करणारे model यांतील अंतर सर्वात आधी twin मध्येच दिसते.

## pot still प्रत्यक्षात काय करतो

batch pot still हे पाठ्यपुस्तकातील उदाहरण आहे, आणि पाठ्यपुस्तकाकडे त्याचे उत्तर शंभराहून अधिक वर्षांपासून आहे. charge उकळतो तसे vapour त्याने मागे सोडलेल्या द्रवापेक्षा alcohol ने अधिक समृद्ध असते, म्हणून pot सातत्याने कमजोर होत जातो आणि run भर distillate strength घसरते. Lord Rayleigh ने 1902 मध्ये हा संबंध लिहून ठेवला: run च्या प्रत्येक छोट्या तुकड्यात vapour मधून बाहेर जाणारे alcohol pot मधून गमावलेल्या alcohol इतके असते.

code मध्ये याची एक पायरी जवळजवळ लाजिरवाणी वाटावी इतकी छोटी आहे:

```python
def rayleigh_step(W, x, dW, vle, eff):
    # W: moles in pot, x: alcohol mole fraction in pot, dW: moles boiled off
    y = x + eff * (vle(x) - x)        # vapour composition, eff fitted from runs
    x_new = (W * x - y * dW) / (W - dW)
    return W - dW, x_new, y
```

`vle(x)` म्हणजे ethanol आणि पाण्याचे vapour-liquid equilibrium, जे प्रकाशित डेटामधून येते, तुमच्या runs मधून नाही. `eff` म्हणजे तुमचा विशिष्ट still, त्याच्या neck मधील reflux, lyne arm चा कोन आणि condenser सह, त्या equilibrium च्या किती जवळ पोहोचतो. आणि यात अंगभूत असलेले conservation पाहा: पायरीआधी pot मधील alcohol बरोबर पायरीनंतर pot मधील alcohol अधिक vapour मधील alcohol. model ते मोडू शकत नाही, कारण गणित त्याला परवानगीच देत नाही.

खऱ्या still मध्ये reflux, heat input मधील बदल आणि flavour साठी महत्त्वाची copper पृष्ठभाग यांची भर पडते, म्हणून production twin मध्ये आणखी काही पदे असतात. आकार तोच राहतो: ज्ञात physics, आणि तुमच्या still चे वर्णन करणारे मोजके parameters.

## केवळ ML twin का भरकटतो

मागील runs वर train झालेले machine learning model अगदी वेगळे काहीतरी करते. ते शिकते की त्याने पाहिलेल्या runs मध्ये अशा charge मधून तसा hearts cut येत असे. ते correlation आहे, आणि still वर correlations च्या दोन कमकुवत बाजू असतात.

**ते काहीच conserve करत नाहीत.** heads, hearts आणि feints तीन स्वतंत्र models ने, किंवा तीन outputs असलेल्या एका model ने भाकीत करा, आणि त्यांची बेरीज जुळायलाच हवी असे काहीही त्यांना भाग पाडत नाही. वरील उदाहरणादाखल run मध्ये प्रत्येक भाकीत fraction त्याच्या ऐतिहासिक श्रेणीत आहे. एकत्रितपणे त्यांत 110 litres absolute alcohol आहे जे charge मध्ये कधीच नव्हते. dashboard वर कोणीही त्यांची बेरीज करत नाही. excise reconciliation मध्ये कोणीतरी नक्की करेल.

**ते extrapolate करत नाहीत.** training set मधील runs distillery ने योगायोगाने वापरलेल्या charge strengths, heat inputs आणि fill levels व्यापतात. त्यापैकी एक बदला आणि model अंदाज बांधू लागते. physics model तसे करत नाही: charge 21% आहे की 24% याची Rayleigh equation ला पर्वा नसते, ते फक्त चालते.

खोल समस्या अशी आहे की केवळ डेटावरचा twin नेमका तेव्हाच कमी विश्वासार्ह होतो जेव्हा त्याची सर्वात जास्त गरज असते, म्हणजे असामान्य run वर.

## hybrid: रचनेसाठी physics, parameters साठी data

चालणारा दृष्टिकोन म्हणजे hybrid, ज्याला कधी कधी grey-box modelling म्हणतात. physics रचना ठरवते: mass आणि alcohol balances, Rayleigh, vapour-liquid equilibrium, साधा heat balance. physics ला माहीत असू शकत नाहीत असे मोजके आकडे run data fit करतो:

- या still ची **enrichment efficiency** (वरील `eff`),
- दिलेल्या steam valve position किंवा burner setting साठी **effective heat input**,
- **condenser आणि safe lag**, म्हणजे vapour pot सोडल्यापासून spirit hydrometer पर्यंत पोहोचेपर्यंतचा विलंब.

चांगल्या नोंदी असलेल्या काही डझन runs वर fit केलेले तीन-चार parameters सहसा खऱ्या still चा बारकाईने मागोवा घेतात. training श्रेणीच्या आत तेवढीच अचूकता गाठायला केवळ ML twin ला कितीतरी जास्त runs लागतात, आणि त्या श्रेणीबाहेर तो तरीही हरवतो.

hybrid मध्ये machine learning ला जागा आहे: residual चे modelling, म्हणजे physics जे भाकीत करते आणि still ने जे केले यातील अंतर. residual ला काही नमुना असेल (तो बाहेरच्या तापमानासोबत, किंवा प्रत्येक CIP नंतर सरकतो), तर एक छोटे model तो शिकू शकते. फरक असा की ML भक्कम model ची दुरुस्ती करत आहे, त्याची जागा घेत नाही.

## खालचे data engineering

twin त्याच्या run नोंदींइतकाच चांगला असतो, आणि इथेच बहुतेक distilleries ना कळते की ते काय नोंदवत आले आहेत:

1. **charge volume आणि strength, मोजलेले.** नियोजित charge नव्हे. 20 degrees C वरील strength, hydrometer किंवा density meter मधून, instrument सह नोंदवलेली.
2. **time series म्हणून heat input.** दर काही सेकंदांनी steam flow किंवा valve position, historian मधून, run sheet वर लिहिलेले setting नव्हे.
3. **spirit safe वरील distillate flow आणि strength.** strength curve काढता येईल इतकी readings, cut times आणि ते कोणी केले यासह.
4. **प्रत्येक fraction, मोजलेले.** run च्या शेवटी heads, hearts आणि feints चे volumes आणि strengths, म्हणजे प्रत्येक run साठी alcohol balance तपासता येईल.

ही शेवटची बाब तुम्हाला data quality test फुकट देते. प्रत्येक run साठी charge alcohol वजा fractions ची बेरीज शून्याच्या जवळ असायला हवी. 5% ने चुकणारा run ही modelling समस्या नाही. ती meter, hydrometer किंवा नोंदीची समस्या आहे, आणि तो run काहीही fit करायला वापरण्याआधी ती दुरुस्त व्हायला हवी. [wine मालिकेतील cellar ledger]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) volumes साठी हाच मुद्दा मांडतो: movements नोंदवा, आणि balances ना स्वतःच स्वतःची तपासणी करू द्या.

## twin कशासाठी आहे

विश्वासार्ह twin असताना उपयुक्त गोष्टी तशा माफक आहेत:

- charge वरून **run चा forecast**: अपेक्षित cut times आणि fraction volumes, म्हणजे stillman आणि planner यांना तेच आकडे दिसतात.
- **बदल आधी model वर तपासा.** वेगळी charge strength किंवा heat profile still वर चालवण्याआधी twin वर चालवता येते.
- **physics सांगते तसा न वागणारा run ओळखा.** हा [पुढच्या पोस्ट]({{ '/mr/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}) चा विषय आहे.

तो जे करत नाही ते म्हणजे cut निवडणे. cut हा sensory आणि व्यावसायिक निर्णय आहे, ज्याचा तपशील [cut points पोस्ट]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}) मध्ये आहे. run कुठे चालला आहे हे twin सांगतो. तो कुठे थांबवायचा हे अजूनही stillman ठरवतो.

## हे कुठे मोडते

**congeners म्हणजे ethanol नव्हे.** ethanol-पाणी equilibrium सह Rayleigh alcohol चा चांगला मागोवा घेते. esters, higher alcohols आणि copper काढून टाकणारी sulphur संयुगे वेगळे वागतात, आणि flavour ठरवणारी संयुगे तीच आहेत. strength चा मागोवा घेणारा twin हा flavour चा twin नाही.

**equilibrium डेटाला मर्यादा आहेत.** प्रकाशित vapour-liquid डेटा शुद्ध ethanol आणि पाण्यासाठी आहे. low wines मध्ये इतर volatiles असतात, आणि run च्या अगदी सुरुवातीला व शेवटी साधे model सर्वात कमी अचूक असते. twin run च्या मधल्या भागावर fit करा आणि तिथेच त्याचे मूल्यमापन करा.

**fitted parameters सरकतात.** copper पातळ होते, heating surfaces मळतात, condenser बदलला जातो. parameters ठरलेल्या वेळापत्रकाने पुन्हा fit करा आणि कालांतराने त्यांच्यावर लक्ष ठेवा. सातत्याने सरकणारा parameter model बद्दल नव्हे तर still बद्दल सांगत असतो.

**वाईट नोंदींमुळे आत्मविश्वासू वाईट twin तयार होतो.** charge strengths मोजलेल्या नसून नियोजित असतील, तर twin कल्पनेशी fit होतो आणि ती दोन दशांश स्थळांसह सांगतो.

## निष्कर्ष

पेय व्यवसायातील still ही अशा मोजक्या जागांपैकी एक आहे जिथे physics पूर्णपणे ज्ञात आहे आणि डेटा तुटक आहे. केवळ machine learning ला जे हवे असते त्याच्या हे नेमके उलटे आहे. रचनेसाठी physics वापरा, म्हणजे alcohol conserve होते आणि model न पाहिलेल्या runs वरही नीट वागते. त्याला तुमचा still बनवणाऱ्या मोजक्या parameters साठी डेटा वापरा. model ला run log दिसतो. stillman ला copper, steam आणि विचित्र charge दिसतो. hybrid twin ही दोघांचाही आदर करणारी आवृत्ती आहे.

twin ला पुरवठा करणाऱ्या sensors साठी पाहा [IoT in the Distillery]({{ '/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). संपूर्ण यादी [The Still and the Model मालिकेच्या पानावर]({{ '/series/still-and-model/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**still चा physics-informed digital twin म्हणजे काय?**
असे model ज्याची रचना distillation च्या physics मधून येते, जसे Rayleigh equation आणि vapour-liquid equilibrium, आणि ज्याचे मोजके parameters distillery च्या स्वतःच्या run data वरून fit केलेले असतात. alcohol conservation सारख्या गोष्टींची हमी physics देते. data हे model या विशिष्ट still ला, त्याच्या heat input ला आणि त्याच्या condenser ला जुळवून घेतो.

**पूर्णपणे डेटावर चालणारा still twin का भरकटतो?**
केवळ मागील runs वर train झालेले machine learning model नियम नव्हे तर correlations शिकते. ते heads, hearts आणि feints चे असे volumes भाकीत करू शकते ज्यांची बेरीज charge केलेल्या alcohol पेक्षा जास्त होते, आणि charge strength किंवा heat input त्याच्या training श्रेणीबाहेर गेल्यावर काय करायचे हे त्याला कळत नाही. त्याच्या रचनेतील काहीही त्याला conservation मोडण्यापासून रोखत नाही.

**hybrid pot still model fit करायला कोणता डेटा लागतो?**
प्रत्येक run साठी: charge volume आणि strength, वेळेनुसार heat input किंवा steam flow, spirit safe वरील distillate flow आणि strength, आणि cut times. hybrid model ला लागणारे मोजके parameters fit करायला चांगल्या नोंदी असलेले काही डझन runs सहसा पुरेसे असतात, कारण बहुतेक काम physics करते.
