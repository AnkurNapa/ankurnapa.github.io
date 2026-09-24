---
layout: post
lang: mr
title: "graph म्हणून lot genealogy: recursive queries आणि MCP tools वर बांधलेला recall agent"
image: /assets/og/wine-lot-genealogy-graph-recall-agent.png
description: "The Cellar Ledger चा भाग 4. कोणत्या bottles मध्ये block 7 चे फळ आहे, आणि किती? cellar ला lots आणि volume-weighted movements चा graph म्हणून model करा, recursive query ने त्याचा माग काढा, आणि गणित करणाऱ्या MCP tools मार्फत त्यासमोर GenAI agent ठेवा, म्हणजे model ला गणित करावे लागत नाही."
date: 2026-07-07 09:00:00 -0700
updated: 2026-07-07
permalink: /mr/2026/wine-lot-genealogy-graph-recall-agent/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, traceability]
faq:
  - q: "wine blend चा माग vineyard block पर्यंत कसा काढावा?"
    a: "प्रत्येक lot ला node आणि प्रत्येक movement ला volume वाहणारी edge माना. wine एखाद्या vessel मध्ये जाते तेव्हा नवी composition म्हणजे आधी जे होते आणि जे आले त्यांचे volume-weighted मिश्रण. recursive query bottling lot पासून मागे त्याच्या sources पर्यंत, किंवा vineyard block पासून पुढे तो असलेल्या प्रत्येक lot आणि bottling पर्यंत edges वरून चालते, आणि वाटेत shares गुणत जाते."
  - q: "वायनरी traceability साठी graph database लागतो का?"
    a: "सहसा नाही. वायनरीत वर्षाला हजारो movements असतात, अब्जावधी नाही, आणि तुम्ही आधीच चालवत असलेल्या lakehouse किंवा warehouse मधील recursive common table expression ते सहज हाताळते. अनेक sites, खूप लांब barrel इतिहास असेल, किंवा tracing पलीकडचे graph algorithms हवे असतील तेव्हा graph database फायद्याचा ठरतो."
  - q: "वायनरी recall agent मध्ये MCP काय भर घालतो?"
    a: "MCP, म्हणजे Model Context Protocol, language model ला tools चा संच देण्याची प्रमाणित पद्धत आहे. recall agent साठी tools म्हणजे trace_back, trace_forward आणि bottling_status, प्रत्येक एक तपासलेली query चालवतो. कोणते tool call करायचे ते model ठरवते आणि निकाल लिहिते, पण प्रत्येक share आणि volume tool कडून येते, model च्या स्वतःच्या गणितातून नाही."
---

**थोडक्यात उत्तर: grower फोन करून सांगतो की block 7 मध्ये residue ची समस्या असू शकते, तेव्हा प्रश्न असतो की कोणत्या bottles मध्ये block 7 चे फळ आहे, आणि किती प्रमाणात. cellar lots आणि volume-weighted movements चा graph म्हणून नोंदवलेले असेल, तर ही काही सेकंदांत चालणारी recursive query आहे. काही MCP tools (trace back, trace forward, bottling status) मार्फत त्यासमोर GenAI agent ठेवा, आणि winemaker साध्या भाषेत प्रश्न विचारून असे उत्तर मिळवू शकतो ज्यातील प्रत्येक टक्केवारी तपासलेल्या code ने काढलेली असते. agent recall memo लिहितो. recall चा निर्णय तो कधीच घेत नाही.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="lot genealogy graph. block 7 चे फळ tank A मध्ये 10,000 litres, 100 टक्के block 7. tank A मधील 3,000 litres tank B मध्ये जातात, ज्यात आधीच block 9 चे 7,000 litres होते, म्हणून tank B 30 टक्के block 7 होतो. tank B चे 5,000 litres tank C च्या 5,000 litres शी blend होतात, जो block 12 आहे, आणि 15 टक्के block 7 असलेला bottling lot D तयार होतो. म्हणजे block 7 पासून पुढे माग काढल्यावर 15 टक्क्यांवर bottling lot D सापडतो.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">BLOCK 7 पासून पुढे माग: EDGES वरून SHARES गुणत जातात</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="150" height="56" rx="9" fill="#06483f"/>
<text x="105" y="85" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">block 7</text>
<text x="105" y="103" text-anchor="middle" font-size="10.5" fill="#cfe6df">grower ने flag केलेला</text>
<rect x="30" y="160" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">block 9</text>
<rect x="30" y="250" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="275" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">block 12</text>
<rect x="250" y="60" width="170" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank A &#183; 10,000 L</text>
<text x="335" y="102" text-anchor="middle" font-size="10.5" fill="#00695c">100% block 7</text>
<rect x="490" y="140" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank B &#183; 10,000 L</text>
<text x="585" y="182" text-anchor="middle" font-size="10.5" fill="#00695c">30% block 7</text>
<rect x="490" y="250" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="274" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank C &#183; 5,000 L</text>
<text x="585" y="292" text-anchor="middle" font-size="10.5" fill="#4a6b64">0% block 7</text>
<rect x="770" y="190" width="200" height="66" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="870" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">bottling lot D</text>
<text x="870" y="238" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">15% block 7</text>
<line x1="180" y1="88" x2="250" y2="88" stroke="#4db6a2" stroke-width="2"/>
<line x1="420" y1="100" x2="490" y2="155" stroke="#4db6a2" stroke-width="2"/>
<text x="470" y="118" text-anchor="middle" font-size="10" fill="#4a6b64">3,000 L</text>
<line x1="180" y1="188" x2="490" y2="170" stroke="#4db6a2" stroke-width="2"/>
<text x="330" y="172" text-anchor="middle" font-size="10" fill="#4a6b64">7,000 L</text>
<line x1="180" y1="278" x2="490" y2="278" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="175" x2="770" y2="215" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="185" text-anchor="middle" font-size="10" fill="#4a6b64">5,000 L</text>
<line x1="680" y1="278" x2="770" y2="235" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="272" text-anchor="middle" font-size="10" fill="#4a6b64">5,000 L</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">10,000 पैकी 3,000 litres मुळे tank B 30% block 7 होतो. tank D चा अर्धा भाग B मधून येतो, म्हणून D 15% आहे. गणित सोपे आहे. संपूर्ण cellar भर ते हाताने करणे सोपे नाही.</figcaption>
</figure>

September मधला मंगळवार आहे आणि एका grower चा फोन येतो. block 7 वरील फवारणी कदाचित withholding period च्या आत झाली असावी. याचा काही परिणाम होतो का हे अजून कोणालाच माहीत नाही, पण ते फळ कुठे गेले हे वायनरीला आजच कळायला हवे. कोणत्या tanks? कोणते blends? कोणती bottlings, आणि त्यापैकी कोणती आधीच पाठवली गेली?

बहुतेक वायनरींमध्ये हे work orders चा ढीग आणि एक spreadsheet घेऊन दोन दिवसांचे काम बनते. तसे असण्याची गरज नाही. या मालिकेत आधी आलेल्या [movement ledger]({{ '/mr/2026/event-sourced-cellar-records-winery/' | relative_url }}) मध्ये प्रत्येक उत्तर आधीच आहे. फक्त तो graph म्हणून वाचायला हवा.

## cellar आधीच एक graph आहे

wine चा प्रत्येक lot हा node आहे. प्रत्येक movement ही त्यावर volume असलेली edge आहे. block मधील फळ tank मध्ये जाते. त्या tank चा काही भाग दुसऱ्या tank मध्ये जातो ज्यात आधीच काहीतरी आहे. दोन tanks तिसऱ्यामध्ये blend होतात, आणि तो bottle होतो.

wine एखाद्या vessel मध्ये जाते तेव्हा नवी composition म्हणजे volume-weighted सरासरी:

> नवा share = (आधी असलेले volume x त्याचा share + येणारे volume x त्याचा share) / एकूण volume

आकृतीत tank B मध्ये block 9 चे 7,000 litres होते आणि त्याला block 7 चे 3,000 litres मिळाले, म्हणून तो 30% block 7 आहे. bottling lot D ने B मधून 5,000 litres आणि C मधून 5,000 घेतले, म्हणून तो 15% block 7 आहे. संपूर्ण यंत्रणा एवढीच. फक्त ती प्रत्येक movement ला योग्य क्रमाने लावावी लागते, आणि नेमक्या याच कामासाठी computers असतात आणि घाईत असलेली माणसे नेमके हेच चुकवतात.

## recursive query

यासाठी graph database ची गरज नाही. वायनरीत वर्षाला हजारो movements असतात, आणि तुम्ही आधीच चालवत असलेल्या warehouse मधील recursive common table expression त्यांच्यावरून सहज चालते.

```sql
WITH RECURSIVE forward AS (
  SELECT to_lot AS lot_id, share AS source_share, 1 AS depth
  FROM   lot_edges
  WHERE  from_lot = 'BLOCK-07-2025'
  UNION ALL
  SELECT e.to_lot, f.source_share * e.share, f.depth + 1
  FROM   forward f
  JOIN   lot_edges e ON e.from_lot = f.lot_id
  WHERE  f.depth < 30
)
SELECT lot_id, SUM(source_share) AS block7_share
FROM   forward
GROUP  BY lot_id;
```

इथे प्रत्येक edge वरील `share` म्हणजे destination lot चा जो अंश source lot मधून आला तो, silver layer मध्ये ledger volumes वरून एकदाच काढलेला. block पासून पुढे edges वरून चाला आणि वाटेत shares गुणा: त्यातून प्रत्येक downstream lot आणि त्यात तो block किती आहे हे मिळते. bottling lot पासून मागे चाला आणि vineyard blocks पर्यंत त्याची संपूर्ण रेसिपी मिळते.

depth limit ही सजावट नाही. वर्षानुवर्षे topping असलेले barrel programmes लांब साखळ्या तयार करतात, आणि data-entry चुकीतून आलेला एखादा loop नाहीतर warehouse हार मानेपर्यंत चालत राहील.

## तीच query label सिद्ध करते

genealogy फक्त वाईट दिवसांसाठी नाही. तीच composition marketing team दर vintage ला विचारते त्या प्रश्नाचे उत्तर देते: या blend वर आपल्याला हवे ते label लावता येईल का?

thresholds बाजारानुसार बदलतात. EU मध्ये label वर variety किंवा vintage साठी साधारणपणे किमान 85% wine पात्र असावी लागते. US मध्ये varietal नावासाठी बहुतेक प्रकरणांत 75% लागतात, AVA साठी 85%, आणि vintage date साठी AVA नमूद असल्यास 95% आणि नसल्यास 85%. backwards trace नेमक्या याच टक्केवाऱ्या देतो: variety, vintage आणि origin नुसार lot चा share. तुमच्या बाजारांचे नियम एका छोट्या table मध्ये ठेवा, आणि artwork छापण्याआधीच एक check सांगू शकतो की blend ते पार करतो का आणि किती फरकाने.

## त्यासमोर GenAI agent ठेवणे

grower अजून फोनवर असताना winemaker ला recursive CTE लिहावी लागू नये. agent साठी हे चांगले काम आहे, जर agent असा बांधला असेल की त्याला आकडे चुकवताच येणार नाहीत.

2026 मध्ये language model ला tools चा संच देण्याची प्रमाणित पद्धत म्हणजे Model Context Protocol (MCP). traceability साठी तीन tools पुरेसे आहेत:

- **`trace_forward(source, min_share)`** एखादा block किंवा lot असलेला प्रत्येक lot आणि bottling, threshold पेक्षा जास्त shares सह परत करते.
- **`trace_back(lot)`** एखाद्या lot ची block, variety आणि vintage नुसार संपूर्ण composition परत करते.
- **`bottling_status(lot)`** तयार झालेल्या, हातात असलेल्या आणि पाठवलेल्या cases, आणि कोणाला पाठवल्या, हे परत करते.

प्रत्येक tool ही तपासलेली query आहे. agent चे काम म्हणजे प्रश्न समजून घेणे, योग्य tools योग्य क्रमाने call करणे आणि ते जे परत करतात ते लिहून काढणे. "block 7 कुठे गेला, आणि त्यातले काही पाठवले गेले का?" असे विचारल्यावर तो `trace_forward` call करतो, मग सापडलेल्या प्रत्येक bottling साठी `bottling_status`, आणि छोटा memo तयार करतो: cellar मध्ये अजून दोन tanks, 15% block 7 असलेली एक bottling जिच्या 400 cases तीन distributors ना पाठवल्या गेल्या, आणि त्या distributors ची यादी.

काही नियम त्याला विश्वासार्ह ठेवतात:

1. **फक्त वाचणारे tools.** agent पाहू शकतो, पण wine हलवू किंवा नोंदी बदलू शकत नाही. hold आणि recall या कृती एखादी व्यक्ती करते.
2. **आकडे फक्त tool output मधूनच येतात.** memo tools ने परत केलेले shares आणि case counts उद्धृत करतो. model ने स्वतः एखादा आकडा काढला, तर तो prompt मधील bug आहे.
3. **mock recalls वर चाचणी घ्या.** अनेक अन्न आणि पेय नियमावल्या एक पाऊल मागे आणि एक पाऊल पुढे माग काढता यावा अशी अपेक्षा ठेवतात, आणि चांगल्या वायनरी mock recall drills घेतात. शेवटच्या काही drills चा ज्ञात उत्तरांसह test set बनवा आणि काहीही बदलल्यावर agent त्यावर चालवा.

फरक वेळेचा आहे. ज्या recall प्रश्नाला पूर्वी दोन दिवसांची कागदपत्रे लागत, त्याला आता काही मिनिटे लागतात, आणि winemaker ती मिनिटे उत्तर जुळवण्याऐवजी ते तपासण्यात घालवतो.

## हे कुठे मोडते

**composition परिपूर्ण mixing गृहीत धरते.** गणित tank ला एकसमान मानते. ढवळल्याशिवाय top केलेली tank, किंवा blend मिसळण्याआधीच काढलेली wine, एकसमान नसते. recall साठी सर्वात वाईट परिस्थिती गृहीत धरा आणि उदार thresholds ने माग काढा.

**topping मुळे धूळ तयार होते.** मिश्र sources मधून वर्षानुवर्षे barrels top केल्याने हजारो छोटे अंश उरतात: याचा 0.2%, त्याचा 0.05%. एक threshold ठरवा ज्याखालील source नोंदवला जातो पण त्याचा पाठलाग केला जात नाही, आणि तो memo मध्ये नमूद करा.

**graph ledger इतकाच चांगला असतो.** एक न नोंदवलेला transfer साखळी तोडतो, आणि block 7 tank B वर थांबला नसताना trace तसे सांगेल. [loss map]({{ '/mr/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) मधील adjustment events साखळी कुठे कमकुवत आहे याचा चांगला आगाऊ इशारा देतात.

**agent ने निर्णय घेऊ नये.** stock रोखायचा, distributors ना कळवायचे की recall करायचा, हा कायदेशीर आणि व्यावसायिक वजन असलेला निर्णय आहे. agent वेगाने तथ्ये गोळा करतो. निर्णयावर सही एखादी व्यक्ती करते.

## निष्कर्ष

प्रत्येक blend हा graph आहे, वायनरी तो तसा नोंदवो वा न नोंदवो. movements त्यांच्या volumes सह साठवा, pipeline मध्ये composition एकदाच काढा, आणि grower विचारू शकतो तो सर्वात कठीण प्रश्न recursive query सोडवते. त्या queries MCP tools म्हणून गुंडाळा, आणि GenAI agent प्रत्येक टक्केवारी तुम्ही तपासलेल्या code मधून घेत साध्या भाषेत उत्तर देऊ शकतो. model उत्तरापर्यंत पोहोचणे जलद करते. ते बरोबर ठरते ते ledger मुळे.

मालिकेतील पुढील भाग: [data contracts म्हणून excise returns]({{ '/mr/2026/wine-excise-returns-data-contracts-genai/' | relative_url }}), जिथे तोच ledger कर विभागाशी जुळावा लागतो. उलट्या दिशेने blending, म्हणजे लक्ष्य गाठण्यासाठी घटक निवडणे, [AI for Wine Blending Optimisation]({{ '/2024/ai-wine-blending-optimization/' | relative_url }}) मध्ये आहे. संपूर्ण यादी [Cellar Ledger मालिकेच्या पानावर]({{ '/series/cellar-ledger/' | relative_url }}) आहे.

## वारंवार विचारले जाणारे प्रश्न

**wine blend चा माग vineyard block पर्यंत कसा काढावा?**
प्रत्येक lot ला node आणि प्रत्येक movement ला volume वाहणारी edge माना. wine एखाद्या vessel मध्ये जाते तेव्हा नवी composition म्हणजे आधी जे होते आणि जे आले त्यांचे volume-weighted मिश्रण. recursive query bottling lot पासून मागे त्याच्या sources पर्यंत, किंवा vineyard block पासून पुढे तो असलेल्या प्रत्येक lot आणि bottling पर्यंत edges वरून चालते, आणि वाटेत shares गुणत जाते.

**वायनरी traceability साठी graph database लागतो का?**
सहसा नाही. वायनरीत वर्षाला हजारो movements असतात, अब्जावधी नाही, आणि तुम्ही आधीच चालवत असलेल्या lakehouse किंवा warehouse मधील recursive common table expression ते सहज हाताळते. अनेक sites, खूप लांब barrel इतिहास असेल, किंवा tracing पलीकडचे graph algorithms हवे असतील तेव्हा graph database फायद्याचा ठरतो.

**वायनरी recall agent मध्ये MCP काय भर घालतो?**
MCP, म्हणजे Model Context Protocol, language model ला tools चा संच देण्याची प्रमाणित पद्धत आहे. recall agent साठी tools म्हणजे trace_back, trace_forward आणि bottling_status, प्रत्येक एक तपासलेली query चालवतो. कोणते tool call करायचे ते model ठरवते आणि निकाल लिहिते, पण प्रत्येक share आणि volume tool कडून येते, model च्या स्वतःच्या गणितातून नाही.
