---
layout: post
lang: mr
title: "Data लोकांसाठी Operational Excellence च्या मूलभूत गोष्टी: OEE, सहा मोठी नुकसाने, SPC आणि प्लांटचा data कुठे असतो"
image: /assets/og/operational-excellence-basics-oee-for-data-people.png
description: "Beverage प्लांटमधील Operational Excellence साठी AI, भाग 4. कोणत्याही AI आधी प्लांटची भाषा: filler line च्या सविस्तर उदाहरणासह OEE, सहा मोठी नुकसाने, TPM, lean मधील अपव्यय, statistical process control, आणि data प्रत्यक्षात कुठे असतो याचा ISA-95 नकाशा (historian, MES, CMMS, LIMS, ERP)."
date: 2026-09-19 09:00:00 -0700
updated: 2026-09-19
permalink: /mr/2026/operational-excellence-basics-oee-for-data-people/
tags: [brewing-science, ai-opex, operational-excellence, packaging, data-engineering]
faq:
  - q: "Bottling line वर OEE कसा मोजतात?"
    a: "OEE म्हणजे availability गुणिले performance गुणिले quality. Availability म्हणजे run time भागिले नियोजित उत्पादन वेळ. Performance म्हणजे प्रत्यक्ष संख्या भागिले त्या run time मध्ये line ने ideal rate ने जेवढे बनवले असते तेवढे. Quality म्हणजे चांगली units भागिले एकूण units. 90 टक्के availability, 83.3 टक्के performance आणि 98 टक्के quality असलेल्या line चा OEE 73.5 टक्के असतो."
  - q: "OEE मधील सहा मोठी नुकसाने कोणती?"
    a: "Breakdowns आणि setup किंवा changeover नुकसाने availability कमी करतात. छोटे stops आणि कमी वेग performance कमी करतात. Process defects आणि start-up rejects quality कमी करतात. गमावलेले प्रत्येक मिनिट या सहांपैकी एकाशी जोडणे ही कोणत्याही सुधारणा कार्यक्रमाची पहिली पायरी आहे, आणि प्लांटमधील कोणत्याही AI प्रकल्पाला लागणारा पहिला dataset."
  - q: "Beverage प्लांटमध्ये उत्पादनाचा data कुठे असतो?"
    a: "तो ISA-95 च्या पातळ्यांवर विखुरलेला असतो. Sensor आणि PLC data control पातळ्यांवर असतो आणि historian मध्ये साठवला जातो. Production orders, line stops आणि batch records सहसा MES मध्ये असतात. Maintenance इतिहास CMMS मध्ये, lab निकाल LIMS मध्ये, आणि orders, stock आणि खर्च ERP मध्ये. बहुतेक AI प्रकल्प पहिले काही महिने हे सगळे एकत्र जोडण्यात घालवतात."
---

**थोडक्यात उत्तर: beverage प्लांटमधील operational excellence काही कल्पनांवर चालते, ज्या प्रत्येक data व्यक्तीने AI ला हात लावण्यापूर्वी जाणून घ्याव्यात. OEE (availability गुणिले performance गुणिले quality) एका shift ला एका आकड्यात बदलतो, आणि त्याहून उपयोगी म्हणजे नाव देता येईल अशा नुकसानांमध्ये. तासाला 40,000 बाटल्या बनवणाऱ्या एका उदाहरणादाखल filler line वर 90 टक्के availability, 83.3 टक्के performance आणि 98 टक्के quality मिळून 73.5 टक्के OEE येतो: एकाच shift मध्ये 79,500 बाटल्या बनल्याच नाहीत. सहा मोठी नुकसाने त्या कुठे गेल्या ते सांगतात. TPM, lean आणि SPC या पद्धती प्लांट त्या परत मिळवण्यासाठी आधीच वापरतात. आणि या सगळ्याचा data पाच प्रणालींमध्ये विखुरलेला असतो, म्हणूनच प्लांटमधील AI प्रकल्प मुख्यतः data प्रकल्प असतात.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="एका filler line वरच्या उदाहरणादाखल shift चा OEE waterfall. तासाला 40,000 च्या ideal rate ने 450 मिनिटांच्या नियोजित वेळेत line 300,000 बाटल्या बनवू शकली असती. 45 मिनिटांच्या stops मुळे availability नुकसान 30,000 बाटल्यांचे. हळू चालणे आणि छोटे stops यामुळे performance नुकसान 45,000 बाटल्यांचे. Quality नुकसान 4,500 नाकारलेल्या बाटल्यांचे. 220,500 चांगल्या बाटल्या उरतात, म्हणजे 73.5 टक्के OEE. उभा अक्ष 200,000 बाटल्यांपासून सुरू होतो.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">FILLER LINE वरची एक SHIFT, बाटल्यांमध्ये (उदाहरणार्थ)</text>
<g font-family="sans-serif">
<line x1="60" y1="250" x2="960" y2="250" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">अक्ष 200,000 बाटल्यांपासून सुरू</text>
<rect x="80" y="70" width="120" height="180" fill="#06483f"/>
<text x="140" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">300,000</text>
<rect x="260" y="70" width="120" height="54" fill="#4db6a2"/>
<text x="320" y="142" text-anchor="middle" font-size="12" fill="#06483f">&#8722;30,000</text>
<rect x="440" y="124" width="120" height="81" fill="#4db6a2"/>
<text x="500" y="223" text-anchor="middle" font-size="12" fill="#06483f">&#8722;45,000</text>
<rect x="620" y="205" width="120" height="8.1" fill="#ff4081"/>
<text x="680" y="232" text-anchor="middle" font-size="12" fill="#ff4081">&#8722;4,500</text>
<rect x="800" y="213.1" width="120" height="36.9" fill="#06483f"/>
<text x="860" y="205" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">220,500</text>
<g font-size="10.5" fill="#4a6b64" text-anchor="middle">
<text x="140" y="268">नियोजित वेळेतील</text><text x="140" y="282">ideal उत्पादन</text>
<text x="320" y="268">availability नुकसान</text><text x="320" y="282">45 min चे stops</text>
<text x="500" y="268">performance नुकसान</text><text x="500" y="282">हळू चालणे, छोटे stops</text>
<text x="680" y="268">quality नुकसान</text><text x="680" y="282">rejects</text>
<text x="860" y="268">चांगल्या बाटल्या</text><text x="860" y="282">73.5% OEE</text>
</g>
<rect x="40" y="298" width="920" height="32" rx="8" fill="#06483f"/>
<text x="500" y="319" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">A = 90% &#183; P = 83.3% &#183; Q = 98% &#183; OEE = 73.5% &#183; 79,500 बाटल्या बनल्याच नाहीत</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">उदाहरणादाखल shift. सर्वात मोठा स्तंभ बहुतेकदा performance चा असतो, असे नुकसान जे कोणी लिहून ठेवत नाही कारण line प्रत्यक्षात कधी थांबलीच नाही.</figcaption>
</figure>

Beverage प्लांटमध्ये येणारे data लोक सहसा 'data' मागतात आणि मग मॉडेल बांधतात. प्लांटमधली माणसे हे सौजन्यपूर्ण संयमाने पाहत राहतात, कारण प्लांटकडे सुधारणेसाठी आधीच एक भाषा आहे, आणि मॉडेल ती भाषा बोलत नाही.

ही मालिकेतील चौथी पोस्ट आहे, आणि पहिल्या तीन पोस्टमधील AI च्या मूलभूत गोष्टी व शेवटच्या चार पोस्टमधील प्रत्यक्ष उपयोग यांच्यातील पूल. तुम्ही data क्षेत्रातून आला असाल तर ही प्लांटची शब्दसंपदा आहे. तुम्ही प्लांटमधून आला असाल तर ती तुमच्या data टीमला कशी समजावायची ते हे आहे.

## OEE: एक आकडा, तीन प्रश्न

Overall equipment effectiveness एका कालावधीत एका line बद्दल तीन प्रश्न विचारतो:

- **Availability:** चालवायचे ठरवलेल्या वेळेपैकी आपण प्रत्यक्षात किती वेळ चालवली?
- **Performance:** चालू असताना आपण ideal rate च्या किती जवळ गेलो?
- **Quality:** जे बनवले त्यापैकी किती चांगले होते?

OEE म्हणजे हे तिन्ही एकमेकांनी गुणलेले. तासाला 40,000 बाटल्यांच्या rating असलेल्या filler वरची ही एक उदाहरणादाखल shift:

```python
planned_min = 450 # 8 h shift less a 30 min planned break
stops_min = 20 + 15 + 10 # changeover overrun, filler jams, labeller faults
run_min = planned_min - stops_min # 405
ideal_per_min = 40_000 / 60 # 666.7 bottles a minute
total, good = 225_000, 220_500 # 4,500 rejects

availability = run_min / planned_min # 0.900
performance = total / (run_min * ideal_per_min) # 0.833
quality = good / total # 0.980
oee = availability * performance * quality # 0.735
```

73.5 टक्के. हा आकडा एकटा फारसा उपयोगी नाही. महत्त्वाचे हे की हेच गणित बाटल्यांमध्ये केले की नुकसान कुठे गेले ते कळते. 450 मिनिटांत ideal rate ने line 300,000 बाटल्या बनवू शकली असती. तिने 220,500 चांगल्या बनवल्या. गहाळ 79,500 पैकी 30,000 stops मुळे गेल्या, 45,000 हळू किंवा अडखळत चालण्यामुळे, आणि 4,500 rejects मुळे.

सर्वात मोठा स्तंभ performance चा आहे, आणि हे सामान्य आहे. चालू असलेली पण हळू चालणारी, किंवा एका वेळी वीस सेकंद थांबणारी line क्वचितच कोणाच्या नोंदीत येते. सोपे फायदे बरेचसे तिथेच असतात.

85 टक्के हा 'world class' आहे असे तुम्ही अनेकदा ऐकाल. त्याला ढोबळ नियम माना, मानक नव्हे. OEE तुम्ही नियोजित वेळ आणि ideal rate कसे ठरवता यावर अवलंबून असतो, आणि ते वेगवेगळ्या प्रकारे ठरवणारे दोन प्लांट आपले आकडे तुलना करू शकत नाहीत. एका line ची तुलना काळानुसार तिच्याशीच करा.

## सहा मोठी नुकसाने

Total productive maintenance, म्हणजे TPM, गमावलेले प्रत्येक मिनिट सहा गटांत वर्गीकृत करते, OEE च्या प्रत्येक भागासाठी दोन:

| OEE घटक | नुकसान | Beverage line वरचे उदाहरण |
|---|---|---|
| Availability | Breakdowns | Filler valve बिघाड, seamer fault |
| Availability | Setup आणि changeover | Label किंवा pack format बदल, flush सह flavour बदल |
| Performance | छोटे stops आणि रिकामे चालणे | Starter wheel वर बाटल्या अडकणे, sensor चुकीचे वाचणे |
| Performance | कमी वेग | Labeller पूर्ण वेगाने बिघडतो म्हणून तो हळू चालवणे |
| Quality | Process defects | कमी भरणे, वाकडी labels, खराब crimps |
| Quality | Start-up rejects | Run च्या सुरुवातीला किंवा stop नंतर वाया गेलेले उत्पादन |

प्लांटमधील कोणत्याही AI प्रकल्पातील हा सर्वात महत्त्वाचा dataset आहे. Line stops या सहांशी जुळणाऱ्या समजूतदार reason codes सह नोंदवलेले असतील, तर या मालिकेतील पुढची जवळजवळ प्रत्येक कल्पना शक्य होते. अर्धे stops 'other' म्हणून नोंदवलेले असतील, तर एकही नाही.

## TPM, lean आणि SPC, प्रत्येकी एका परिच्छेदात

**TPM** ही OpEx ची maintenance बाजू आहे: operators आपल्याच उपकरणांची मूलभूत निगा राखतात, स्थिती आणि इतिहासावर आधारित नियोजित maintenance, आणि सहा नुकसाने दूर करण्यावर सातत्याने लक्ष. Predictive maintenance इथेच बसते.

**Lean** म्हणजे संपूर्ण प्रवाहातून अपव्यय काढून टाकणे. अपव्ययांची पारंपरिक यादी (transport, inventory, motion, waiting, overproduction, over-processing आणि defects, आणि अनेकदा आठवा म्हणून न वापरलेली कौशल्ये) packaging hall साठी उपयुक्त दृष्टी आहे. दोन दिवस वाट पाहणारा रिकाम्या cans चा pallet म्हणजे inventory. प्रत्येक batch sheet साठी दूरच्या printer पर्यंत चालत जाणारा operator म्हणजे motion.

**SPC**, म्हणजे statistical process control, प्रक्रिया सामान्यपणे वागत आहे की नाही यावर लक्ष ठेवते. Control chart, उदाहरणार्थ, fill volume काळानुसार दाखवतो, आणि मर्यादा प्रक्रियेच्या स्वतःच्या चढउतारावरून मोजलेल्या असतात. मर्यादेबाहेरचे बिंदू, किंवा मर्यादेच्या आतले असामान्य बिंदूंचे क्रम, काहीतरी बदलल्याचा इशारा देतात. SPC दशकानुदशके शांतपणे beverage quality चालवत आला आहे, आणि कोणत्याही AI anomaly detection ला मागे टाकावी लागणारी ही आधाररेषा आहे.

## Data कुठे असतो

ISA-95 मॉडेल उत्पादन प्लांटच्या थरांचे वर्णन करते, आणि तुमचा data कुठे आहे याचा तो चांगला नकाशा आहे:

- **पातळी 0 ते 2, प्रक्रिया आणि तिचे नियंत्रण.** Sensors, PLCs, SCADA आणि HMIs. Readings सहसा **historian** मध्ये साठवली जातात: तापमान, दाब, प्रवाह, वेग आणि संख्या, सेकंदागणिक.
- **पातळी 3, उत्पादन कामकाज.** **MES** मध्ये production orders, line states, stop reasons आणि batch records असतात. **CMMS** मध्ये maintenance work orders आणि asset इतिहास असतो. **LIMS** मध्ये lab निकाल असतात.
- **पातळी 4, व्यावसायिक नियोजन.** **ERP** मध्ये orders, stock, खर्च आणि उत्पादन योजना असते.

बहुतेक प्लांटमध्ये ही पाचही असतात आणि फार थोड्यांमध्ये ती जोडलेली असतात. Filler चे stop events MES मध्ये, त्याचे vibration historian मध्ये, दुरुस्तीचा इतिहास CMMS मध्ये आणि reject नमुने LIMS मध्ये. [मागच्या पोस्टमधला]({{ '/mr/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}) प्रश्न, 'line 2 ची 40 मिनिटे का गेली?', याचे उत्तर द्यायला यापैकी किमान तीन लागतात.

प्लांटमधील AI प्रकल्पांना अपेक्षेपेक्षा जास्त वेळ लागण्याचे हे प्रामाणिक कारण आहे. मॉडेलला काही आठवडे लागतात. प्रणाली जोडणे, व्याख्यांवर सहमती करणे आणि stop codes स्वच्छ करणे यांना काही महिने. [Cellar Ledger मधील winery data पायाभरणीचा]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) धडाही हाच आहे: data model आधी येते.

## हे कुठे मोडते

**OEE चा खेळ करता येतो.** नियोजित वेळ म्हणून काय मोजायचे ते बदला, किंवा ideal rate कमी करा, आणि एकही जास्तीची बाटली न बनता OEE वाढतो. व्याख्या निश्चित करा आणि त्या प्रसिद्ध करा.

**Stop codes पहाटे 3 वाजता ते नोंदवणाऱ्या व्यक्तीइतकेच चांगले असतात.** खूप codes असतील तर operators पहिलाच निवडतात. खूप कमी असतील तर सगळे 'other' होते. PLC वरून आपोआप stop ओळखणे आणि छोटी, नीट निवडलेली reason यादी हे दोन्हीपेक्षा चांगले चालते.

**सरासरी नुकसान लपवते.** आठवड्याचा 75 टक्के OEE एक भयंकर shift आणि अनेक चांगल्या shifts लपवू शकतो. वितरण पाहा, shift नुसार, उत्पादनानुसार आणि format नुसार.

**SPC मर्यादा स्थिर प्रक्रियेतूनच आल्या पाहिजेत.** प्रक्रिया नियंत्रणाबाहेर असलेल्या काळातून control limits मोजल्या, तर chart गोंधळालाच सामान्य म्हणेल.

## निष्कर्ष

OEE एका shift ला availability, performance आणि quality मध्ये, आणि मग मोजता येण्याजोग्या बाटल्यांमध्ये बदलतो. सहा मोठी नुकसाने त्या कुठे गेल्या ते सांगतात. TPM, lean आणि SPC या मार्गांनी प्लांट नेहमीच लढत आले आहेत, आणि त्यांना आधार देणारा data historian, MES, CMMS, LIMS आणि ERP मध्ये असतो, जे क्वचितच एकमेकांशी बोलतात. या मालिकेतील पुढची प्रत्येक AI कल्पना याच पायावर उभी आहे. Stop codes बरोबर करा आणि प्रणाली जोडा, मग AI चा भाग सोपा होतो.

पुढे: [OpEx साठी classic AI]({{ '/mr/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), SPC च्या जोडीला predictive maintenance, soft sensors आणि anomaly detection. Line OEE च्या Tableau दृश्यासाठी [Visualising Packaging-Line OEE in Tableau]({{ '/2023/tableau-packaging-line-oee-dashboard/' | relative_url }}) पाहा. संपूर्ण यादी [मालिकेच्या पानावर]({{ '/series/ai-operational-excellence/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**Bottling line वर OEE कसा मोजतात?**
OEE म्हणजे availability गुणिले performance गुणिले quality. Availability म्हणजे run time भागिले नियोजित उत्पादन वेळ. Performance म्हणजे प्रत्यक्ष संख्या भागिले त्या run time मध्ये line ने ideal rate ने जेवढे बनवले असते तेवढे. Quality म्हणजे चांगली units भागिले एकूण units. 90 टक्के availability, 83.3 टक्के performance आणि 98 टक्के quality असलेल्या line चा OEE 73.5 टक्के असतो.

**OEE मधील सहा मोठी नुकसाने कोणती?**
Breakdowns आणि setup किंवा changeover नुकसाने availability कमी करतात. छोटे stops आणि कमी वेग performance कमी करतात. Process defects आणि start-up rejects quality कमी करतात. गमावलेले प्रत्येक मिनिट या सहांपैकी एकाशी जोडणे ही कोणत्याही सुधारणा कार्यक्रमाची पहिली पायरी आहे, आणि प्लांटमधील कोणत्याही AI प्रकल्पाला लागणारा पहिला dataset.

**Beverage प्लांटमध्ये उत्पादनाचा data कुठे असतो?**
तो ISA-95 च्या पातळ्यांवर विखुरलेला असतो. Sensor आणि PLC data control पातळ्यांवर असतो आणि historian मध्ये साठवला जातो. Production orders, line stops आणि batch records सहसा MES मध्ये असतात. Maintenance इतिहास CMMS मध्ये, lab निकाल LIMS मध्ये, आणि orders, stock आणि खर्च ERP मध्ये. बहुतेक AI प्रकल्प पहिले काही महिने हे सगळे एकत्र जोडण्यात घालवतात.
