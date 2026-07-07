---
layout: post
title: "Co-Packing and Contract Brewing Analytics: Making Capacity Pay"
image: /assets/og/co-packing-contract-brewing-analytics.png
description: "Contract brewing and co-packing live or die on capacity utilisation and true cost per contract. The analytics that decide whether each customer brand actually makes money — and where AI helps."
date: 2026-05-06 09:00:00 -0700
updated: 2026-05-06
tags: [brewing-science, contract-brewing, co-packing, capacity-planning, commercial-planning]
faq:
  - q: "What is contract brewing and co-packing?"
    a: "Contract brewing is making beer for another company's brand; co-packing (co-manufacturing) is packaging it — canning, bottling or kegging — for them. In both, the producer sells capacity and execution rather than its own brand, so the business is run on tank-days, line hours and cost per contract, not on depletions."
  - q: "What metrics matter most in contract brewing?"
    a: "Capacity utilisation (fermentation tank-days and packaging-line hours are the real constraints), changeover and CIP time between brands, yield and brewhouse efficiency per recipe, true cost-to-serve per contract, and margin per customer after every loss. Shipments tell you little; utilisation and margin per contract tell you everything."
  - q: "How does analytics help a contract brewery?"
    a: "It answers the two questions the business turns on: is the plant full, and does each contract make money? Scheduling analytics maximise tank-days and minimise changeovers; cost-to-serve and yield analytics expose unprofitable contracts; and batch genealogy keeps every customer's brand traceable and on-spec across shared lines."
---

**Short answer: contract brewing and co-packing sell capacity, not a brand — so the whole business runs on two numbers: how full the plant is, and whether each customer contract actually makes money after every loss. The analytics that matter are capacity utilisation (fermentation tank-days and line hours), changeover and CIP time, yield per recipe, and true cost-to-serve and margin per contract. AI sharpens the schedule and the costing; it does not change the fundamentals.**

A contract brewery's product is its brewhouse, fermentation tanks and packaging lines — sold by the tank-day and the line hour. That makes it a different analytical animal from a brand-owning brewery: success is not depletions, it is a full plant of profitable contracts. The same lens applies whether you *are* the co-packer or you *use* one. It builds on [cost of goods per hectolitre]({{ '/2025/cost-of-goods-per-hectoliter/' | relative_url }}) and [cost-to-serve profitability]({{ '/2025/cost-to-serve-na-beer-profitability/' | relative_url }}).

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Contract brewing analytics flow: capacity, schedule, brew per brand, cost and yield, bill and margin">
<rect x="0" y="0" width="1000" height="270" fill="#ffffff"/>
<text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">The contract brewery, by the numbers</text>
<g font-family="sans-serif">
<rect x="20" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><circle cx="106" cy="114" r="15" fill="#00695c"/><text x="106" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">1</text><text x="106" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Capacity</text><text x="106" y="193" text-anchor="middle" font-size="11" fill="#4a6b64">tank-days, line hours</text>
<rect x="216" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><circle cx="302" cy="114" r="15" fill="#00695c"/><text x="302" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">2</text><text x="302" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Schedule</text><text x="302" y="193" text-anchor="middle" font-size="11" fill="#4a6b64">fit the brands in</text>
<rect x="412" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><circle cx="498" cy="114" r="15" fill="#00695c"/><text x="498" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">3</text><text x="498" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Brew per brand</text><text x="498" y="193" text-anchor="middle" font-size="11" fill="#4a6b64">to each spec</text>
<rect x="608" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><circle cx="694" cy="114" r="15" fill="#00695c"/><text x="694" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">4</text><text x="694" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Cost & yield</text><text x="694" y="193" text-anchor="middle" font-size="11" fill="#4a6b64">per contract</text>
<rect x="804" y="80" width="172" height="150" rx="8" fill="#00695c"/><circle cx="890" cy="114" r="15" fill="#fff"/><text x="890" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#00695c">5</text><text x="890" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">Bill & margin</text><text x="890" y="193" text-anchor="middle" font-size="11" fill="#f0f6f5">the true profit</text>
</g>
<g fill="#00695c" stroke="#00695c" stroke-width="2">
<line x1="192" y1="155" x2="209" y2="155"/><polygon points="209,150 216,155 209,160" stroke="none"/>
<line x1="388" y1="155" x2="405" y2="155"/><polygon points="405,150 412,155 405,160" stroke="none"/>
<line x1="584" y1="155" x2="601" y2="155"/><polygon points="601,150 608,155 601,160" stroke="none"/>
<line x1="780" y1="155" x2="797" y2="155"/><polygon points="797,150 804,155 797,160" stroke="none"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A contract brewery's value chain runs on capacity and cost per contract — not on its own depletions.</figcaption>
</figure>

## Capacity is the product

The binding constraint in contract brewing is rarely the brewhouse — it is fermentation and conditioning tank-days, and packaging-line hours. A tank tied up an extra two days for a slow-attenuating recipe is capacity you cannot sell. So the first analytics job is utilisation: how many of your available tank-days and line hours are actually billed, and where they leak to changeovers, CIP between brands, and idle gaps. Scheduling analytics — sequencing brands to minimise CIP and matching recipe fermentation profiles to tank turns — directly create sellable capacity, the theme of [production scheduling]({{ '/2021/ai-brewery-production-scheduling/' | relative_url }}).

## True cost and margin per contract

A contract looks profitable on the quote and loses money in reality when the losses are not attributed. Real cost-to-serve per customer has to carry that brand's actual brewhouse yield and extract efficiency, its fermentation losses and tank time, its changeover and CIP burden, its packaging-line OEE and material waste, and its share of utilities and overhead. Only then does margin per contract become honest — and it routinely reveals that a high-volume customer paying a low rate is worth less than a smaller, simpler one. Attributing yield per recipe (gravity, attenuation and brewhouse efficiency vary by brand) is the unglamorous core of the costing.

## Traceability and spec control across many brands

Running several customers' brands through shared vessels and lines makes traceability and quality non-negotiable. Each brand is a distinct recipe and specification, and the IBD fundamentals still govern: hit the customer's target original gravity and attenuation, their colour and bitterness, their dissolved-oxygen and carbonation specs — on *their* recipe, not a house default. Batch genealogy (lot to tank to package to pallet, per customer) protects against mix-ups, supports each brand's recalls independently, and underpins the billing. Shared lines also raise allergen and cross-contamination control to a first-order analytics concern, not an afterthought.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 210" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Where capacity goes: billed production, changeover and CIP, yield loss, and idle">
<rect x="0" y="0" width="760" height="210" fill="#ffffff"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Where the capacity (the product) goes</text>
<rect x="60" y="62" width="396.8" height="44" fill="#00695c"/>
<rect x="456.8" y="62" width="89.6" height="44" fill="#06483f"/>
<rect x="546.4" y="62" width="51.2" height="44" fill="#06483f"/>
<rect x="597.6" y="62" width="102.4" height="44" fill="#4a6b64"/>
<text x="258" y="90" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Billed production 62%</text>
<g font-family="sans-serif" font-size="12.5" fill="#06483f">
<rect x="60" y="140" width="14" height="14" fill="#00695c"/><text x="80" y="152">Billed production — 62%</text>
<rect x="300" y="140" width="14" height="14" fill="#06483f"/><text x="320" y="152">Changeover & CIP — 14%</text>
<rect x="540" y="140" width="14" height="14" fill="#06483f"/><text x="560" y="152">Yield loss — 8%</text>
<rect x="60" y="166" width="14" height="14" fill="#4a6b64"/><text x="80" y="178">Idle / unsold — 16%</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Only the billed slice earns. Changeover, CIP, yield loss and idle time are capacity you paid for and didn't sell — the analytics target.</figcaption>
</figure>

## Where AI helps — and where it doesn't

Machine learning sharpens the two hard problems: scheduling (sequencing brands and tank turns to maximise billed tank-days and minimise CIP) and forecasting (predicting a brand's fermentation time and yield so the schedule is realistic), with [packaging-line OEE]({{ '/2023/tableau-packaging-line-oee-dashboard/' | relative_url }}) analytics squeezing the line side. A generative-AI copilot can draft the per-contract margin review and the customer-facing production report from the data.

Three honest limits. First, **garbage costing in, garbage margin out** — if you do not attribute yield, tank-time and CIP to the right brand, the per-contract margin is fiction, and AI just computes the fiction faster. Second, **capacity is lumpy and contractual** — you cannot smoothly optimise around minimum-order commitments and a customer's fixed launch date, so the schedule has hard human constraints. Third, **quality is the contract** — a co-packer's reputation is hitting every brand's spec every time; no utilisation gain is worth an off-spec batch that loses the customer.

## The bottom line

Contract brewing and co-packing are a capacity business wearing a brewery's clothes. Measure utilisation in tank-days and line hours, attribute every loss to the brand that caused it, and compute honest margin per contract — then let scheduling and forecasting analytics keep the plant full and the costing tight. Keep traceability and spec control absolute, because the product you actually sell is reliable capacity.

## Frequently asked questions

**What is contract brewing and co-packing?**
Contract brewing is making beer for another company's brand; co-packing (co-manufacturing) is packaging it — canning, bottling or kegging — for them. In both, the producer sells capacity and execution rather than its own brand, so the business is run on tank-days, line hours and cost per contract, not on depletions.

**What metrics matter most in contract brewing?**
Capacity utilisation (fermentation tank-days and packaging-line hours are the real constraints), changeover and CIP time between brands, yield and brewhouse efficiency per recipe, true cost-to-serve per contract, and margin per customer after every loss. Shipments tell you little; utilisation and margin per contract tell you everything.

**How does analytics help a contract brewery?**
It answers the two questions the business turns on: is the plant full, and does each contract make money? Scheduling analytics maximise tank-days and minimise changeovers; cost-to-serve and yield analytics expose unprofitable contracts; and batch genealogy keeps every customer's brand traceable and on-spec across shared lines.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
