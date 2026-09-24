---
layout: post
title: "What 1,000 Beverage-AI Companies Are Actually Building"
image: /assets/og/what-1000-beverage-ai-companies-are-building.png
description: "Part 6 of The Brewer's Agent. A dataset of just over 1,000 companies and people applying AI to beer, wine and whiskey, counted properly. Almost as many make no AI claim as ship AI, the shipping work is operational rather than showy, sensory and recipe AI stays in pilot, equipment makers barely use it, and genuine GenAI is a small slice."
date: 2026-09-15 09:00:00 -0700
updated: 2026-09-15
tags: [brewing-science, brewers-agent, generative-ai, industry, data-strategy]
faq:
  - q: "How many beverage companies are really using AI?"
    a: "In a curated dataset of 1,015 companies and people around beer, wine and whiskey, 447 are graded as shipping AI in a product or operation, 60 as piloting and 21 as research. 431 were checked and make no AI claim at all. The rest are ungraded. Shipping here means the company says so publicly, checked against its own site where possible."
  - q: "Where is AI actually used in the drinks industry?"
    a: "Mostly in operational work. Process and operations, vineyard and crop monitoring, sales and demand forecasting, and quality inspection account for most of the shipping AI. Sensory and recipe AI gets more attention but has the highest share of pilots, and equipment makers make the fewest AI claims of any group."
  - q: "How common is generative AI among beverage-AI companies?"
    a: "Less common than the headlines suggest. Only about 35 of the 1,015 entries describe generative AI or large language models in their use case, and the GenAI and marketing theme holds 18 companies. Most of what ships is forecasting, computer vision, anomaly detection and classic machine learning."
---

**Short answer: I counted just over 1,000 companies and people around beer, wine and whiskey that come up in conversations about AI, and graded each one. 447 ship AI in a product or operation. 431 were checked and make no AI claim at all. The AI that ships is operational: process control, vineyards, demand forecasting, quality inspection. Sensory and recipe AI, the part that makes headlines, has the highest share of pilots. Equipment makers barely claim AI. And only about 35 entries describe generative AI or LLMs at all. The GenAI layer in drinks is thin, and it sits on data engineering most of the industry has not finished.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Companies by theme, split into those shipping AI and those making no AI claim. Process and operations: 98 shipping, 121 no claim. Agriculture and crop: 64 shipping, 47 no claim. Sales, demand and pricing: 61 shipping, 24 no claim. Quality and inspection: 45 shipping, 22 no claim. Sensory and recipe: 38 shipping, 15 no claim, 17 pilot or research. Engineering and equipment: 3 shipping, 26 no claim. GenAI and marketing: 13 shipping, 4 no claim.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">1,015 ENTRIES BY THEME: SHIPPING AI vs NO AI CLAIM</text>
<g font-family="sans-serif" font-size="11.5">
<text x="290" y="56" font-weight="700" fill="#06483f">shipping AI</text>
<text x="620" y="56" font-weight="700" fill="#ff4081">no AI claim</text>
<g fill="#06483f">
<text x="40" y="84">Process &amp; operations</text>
<text x="40" y="114">Agriculture &amp; crop</text>
<text x="40" y="144">Sales, demand &amp; pricing</text>
<text x="40" y="174">Quality &amp; inspection</text>
<text x="40" y="204">Sensory &amp; recipe</text>
<text x="40" y="234">Engineering &amp; equipment</text>
<text x="40" y="264">GenAI &amp; marketing</text>
</g>
<rect x="290" y="70" width="216" height="20" rx="3" fill="#06483f"/><text x="512" y="85" fill="#06483f">98</text>
<rect x="290" y="100" width="141" height="20" rx="3" fill="#06483f"/><text x="437" y="115" fill="#06483f">64</text>
<rect x="290" y="130" width="134" height="20" rx="3" fill="#06483f"/><text x="430" y="145" fill="#06483f">61</text>
<rect x="290" y="160" width="99" height="20" rx="3" fill="#06483f"/><text x="395" y="175" fill="#06483f">45</text>
<rect x="290" y="190" width="84" height="20" rx="3" fill="#06483f"/><text x="380" y="205" fill="#06483f">38 (+17 pilot or research)</text>
<rect x="290" y="220" width="7" height="20" rx="2" fill="#06483f"/><text x="303" y="235" fill="#06483f">3</text>
<rect x="290" y="250" width="29" height="20" rx="3" fill="#06483f"/><text x="325" y="265" fill="#06483f">13</text>
<rect x="620" y="70" width="266" height="20" rx="3" fill="#ff4081"/><text x="892" y="85" fill="#06483f">121</text>
<rect x="620" y="100" width="103" height="20" rx="3" fill="#ff4081"/><text x="729" y="115" fill="#06483f">47</text>
<rect x="620" y="130" width="53" height="20" rx="3" fill="#ff4081"/><text x="679" y="145" fill="#06483f">24</text>
<rect x="620" y="160" width="48" height="20" rx="3" fill="#ff4081"/><text x="674" y="175" fill="#06483f">22</text>
<rect x="620" y="190" width="33" height="20" rx="3" fill="#ff4081"/><text x="659" y="205" fill="#06483f">15</text>
<rect x="620" y="220" width="57" height="20" rx="3" fill="#ff4081"/><text x="683" y="235" fill="#06483f">26</text>
<rect x="620" y="250" width="9" height="20" rx="3" fill="#ff4081"/><text x="635" y="265" fill="#06483f">4</text>
</g>
<rect x="40" y="288" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="313" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">THE AI THAT SHIPS IS OPERATIONAL &#183; THE KIT MAKERS BARELY CLAIM IT &#183; GENAI IS A SLIVER</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Selected themes from a public dataset of 1,015 entries at the time of writing. Themes come from keyword rules on each entry's use-case text.</figcaption>
</figure>

Every week someone announces AI in beer. An AI-designed IPA, an AI sommelier, an agent that runs the brewhouse. If you only read the announcements, you would think the industry had moved on from spreadsheets. So I started counting.

Over the last few months I have kept a public dataset, the [Beverage-AI Radar](https://ankurnapa.github.io/beverage-ai-radar/), of companies and people applying AI and data to beer, wine and whiskey. At the time of writing it holds 1,015 entries. This last post in **The Brewer's Agent** is what those entries say when you count them honestly, and what that means for anyone building GenAI tools like the ones in this series.

## How the counting works

Each entry is graded on AI maturity from its own public material:

- **Shipping**: the company says AI is in a live product or operation.
- **Pilot**: a named trial or proof of concept.
- **Research**: academic or lab work.
- **No AI claim**: checked, and the company does not claim AI. This is a real finding, not a blank.

Where possible, claims are checked against the company's own site rather than press coverage. That matters more than it sounds. Launch press regularly describes a product as using an LLM when the vendor's own documentation says it uses deterministic rules. The vendor's version wins.

Each entry is also filed under a theme (process, agriculture, quality and so on) by keyword rules on its use-case description. Those rules have regression tests, but they are still rules, and some entries land in "Other".

## Finding 1: nearly as many make no AI claim as ship AI

Of 1,015 entries, **447 are shipping** AI (44%), **60 are piloting** and **21 are research**. **431, or 42%, were checked and make no AI claim at all**. Another 56 are not yet graded.

That no-claim group is not noise. It is full of brewing software, equipment makers, consultancies and ingredient suppliers that sit at the centre of how drinks are made and that turn up in any serious list of the industry's technology. They hold the data. They mostly have not put AI on top of it yet. For anyone building, that is the most interesting number in the dataset.

## Finding 2: the AI that ships is operational

Where AI does ship, it is not glamorous:

- **Process and operations**: 98 shipping. Fermentation monitoring, scheduling, energy, yield.
- **Agriculture and crop**: 64 shipping, much of it vineyard sensing and disease prediction.
- **Sales, demand and pricing**: 61 shipping. Forecasting, route planning, depletion analysis.
- **Quality and inspection**: 45 shipping. Vision on the packaging line, lab data, anomaly detection.

That is the list a brewery operations manager would have written. Measurable problems, existing data, a clear number to improve. It is the same conclusion as [What AI in Beer Actually Looks Like in 2026]({{ '/2026/what-ai-in-beer-actually-looks-like-2026/' | relative_url }}), now with counts behind it.

## Finding 3: sensory and recipe AI stays in pilot

**Sensory and recipe** has 70 entries. 38 ship, but **17 are pilots or research**, about a quarter of the theme and the highest share of any major theme. This is the AI that gets the headlines: designed beers, predicted flavour, digital tasting panels.

It stays experimental for good reasons. Sensory data is small, subjective and expensive, the target (does it taste good?) is soft, and the [evals]({{ '/2026/evals-for-a-brewing-assistant/' | relative_url }}) for "is this recipe good" are much harder to write than for "is this ABV right". The [malt vector post]({{ '/2026/malt-aroma-wheels-as-vectors-similarity-search/' | relative_url }}) in this series shows how quickly the maths gets shaky once perception is involved.

## Finding 4: equipment makers barely claim AI

**Engineering and equipment** has 36 entries and only **3 ship AI**. 26 make no AI claim.

These are the companies whose tanks, brewhouses and filling lines generate most of the process data in a brewery. The data exists, sitting in control systems and historians. Very little of it is being used for anything beyond control, at least publicly. Whoever joins that equipment data to the operational AI in finding 2 has a clear run.

## Finding 5: GenAI is a sliver

Only about **35 of the 1,015 entries** mention generative AI or large language models in their use case, and the **GenAI and marketing** theme holds just 18 companies. Most of the AI shipping in drinks is forecasting, computer vision, anomaly detection and classic machine learning.

That is not a criticism. It is the right order of work. Everything in this series (retrieval that cites its source, tools that do the maths, vectors with brewing knowledge in them, clean scraped data, evals that block bad releases) depends on data engineering most of the industry is still doing. GenAI is a layer on top of that foundation, and the dataset says the foundation comes first.

## Finding 6: whiskey is thin

By vertical, **beer has 277** entries and **wine 274**, while **whiskey has 82**. Another 374 cover several drinks, mostly horizontal platforms and consultancies. Whiskey's thinness partly reflects where I have looked so far, and partly that distillers talk less publicly about technology. Either way, the evidence for spirits is shallower, and any claim about "AI in whiskey" rests on fewer examples.

Geographically, the United States leads with 295 entries, then the United Kingdom and Germany on 72 each, France on 59 and India on 37. 174 entries have no clear country, usually online-only companies.

## Where this breaks

**It is desk research.** Everything comes from public material. A brewery quietly running a good forecasting model and never talking about it is invisible here, and a vendor with loud marketing is overrepresented.

**"Shipping" is a company's own claim.** Checking against the vendor's site catches exaggerated press, but it cannot confirm that a product works well or that anyone uses it.

**Themes come from keyword rules.** A company that does three things is filed under one, and wording can misfile it. The rules are tested and the misfires I found were fixed, but the counts are approximate at the edges. The GenAI count in particular is a keyword search and could be off by a handful either way.

**The dataset keeps growing.** These counts are a snapshot. Rerun them in three months and every number will have moved. The shape, I suspect, will not.

## The bottom line

Counted properly, beverage AI looks less like the announcements and more like an operations plan. Nearly half the companies that matter make no AI claim. The AI that ships forecasts, inspects and monitors. Sensory and recipe work stays in pilot for honest reasons, the equipment makers are sitting on data they barely use, and generative AI is a thin layer that only works on top of the data engineering underneath it. That is the case this whole series has made, one tool at a time.

That closes **The Brewer's Agent**. It started with [RAG that cites its source and leaves the maths to a tool]({{ '/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }}) and ends with the evidence that the foundation is the hard part. The full series is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}), and the wine companion is [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**How many beverage companies are really using AI?**
In a curated dataset of 1,015 companies and people around beer, wine and whiskey, 447 are graded as shipping AI in a product or operation, 60 as piloting and 21 as research. 431 were checked and make no AI claim at all. The rest are ungraded. Shipping here means the company says so publicly, checked against its own site where possible.

**Where is AI actually used in the drinks industry?**
Mostly in operational work. Process and operations, vineyard and crop monitoring, sales and demand forecasting, and quality inspection account for most of the shipping AI. Sensory and recipe AI gets more attention but has the highest share of pilots, and equipment makers make the fewest AI claims of any group.

**How common is generative AI among beverage-AI companies?**
Less common than the headlines suggest. Only about 35 of the 1,015 entries describe generative AI or large language models in their use case, and the GenAI and marketing theme holds 18 companies. Most of what ships is forecasting, computer vision, anomaly detection and classic machine learning.
