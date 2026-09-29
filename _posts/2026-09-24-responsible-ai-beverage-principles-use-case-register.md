---
layout: post
title: "What Responsible AI Actually Means for a Drinks Business: Six Principles and a Use-Case Register in SQL"
image: /assets/og/responsible-ai-beverage-principles-use-case-register.png
description: "Part 1 of Responsible AI for Beer, Whisky and Wine. The six Responsible AI principles, mapped to breweries, distilleries and wineries, the frameworks behind them (NIST AI RMF, ISO/IEC 42001, the EU AI Act, India's AI Governance Guidelines and the DPDP Act), and the one artefact every drinks business should build first: an AI use-case register with a risk-tiering query."
date: 2026-09-24 09:00:00 -0700
updated: 2026-09-24
tags: [brewing-science, rai-beverage, ai-governance, data-modelling]
faq:
  - q: "What is Responsible AI in plain terms?"
    a: "It is the discipline of building and running AI so that it is fair, reliable and safe, respects privacy and security, works for everyone who has to use it, can be explained, and has a named person accountable for it. For a brewery, distillery or winery it mostly comes down to three questions per use case: who can this harm, how would we know, and who signs off."
  - q: "Which Responsible AI framework should a small drinks business follow?"
    a: "Use the NIST AI Risk Management Framework as the working method (Govern, Map, Measure, Manage), because it is free, practical and not tied to one country. Treat ISO/IEC 42001 as the destination if you ever need certification. Then check the specific laws where you sell: the EU AI Act for Europe, and in India the AI Governance Guidelines plus the DPDP Act for personal data."
  - q: "What is an AI use-case register?"
    a: "A single table that lists every AI system the business uses or is building, with its owner, purpose, data, who it affects, whether it touches personal data, product safety or minors, and a risk tier. It is the first Responsible AI artefact to build because every other control (reviews, evals, monitoring) hangs off it. Without it you cannot answer the simplest audit question: what AI do we actually run?"
---

**Short answer: Responsible AI in a drinks business is not an ethics poster in the canteen. It is six plain principles (fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability) applied to the AI you actually run: the fermentation soft sensor, the GenAI that writes the Instagram captions, the recommender on the webshop, the agent drafting maintenance orders. The frameworks (NIST AI RMF, ISO/IEC 42001, the EU AI Act, India's AI Governance Guidelines) all start in the same place: know what AI you have, who it can harm, and who owns it. So the first artefact is a boring one. A use-case register, in a real table, with a query that sorts it by risk.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 400" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The six Responsible AI principles mapped to beverage examples. Fairness: recommenders and pricing. Reliability and safety: soft sensors near product release. Privacy and security: loyalty and taproom data. Inclusiveness: multilingual plant floor and sensory language. Transparency: AI-written copy and model cards. Accountability: a named owner per system. All six feed into one AI use-case register, which drives a risk tier and the controls each tier needs.">
<rect width="1000" height="400" fill="#ffffff"/>
<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">SIX PRINCIPLES &#183; ONE REGISTER &#183; A TIER PER USE CASE</text>
<g font-family="sans-serif">
<rect x="40" y="52" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="58" y="78" font-size="12.5" font-weight="700" fill="#06483f">Fairness</text>
<text x="58" y="100" font-size="10.5" fill="#4a6b64">recommenders &#183; pricing &#183; hiring</text>
<rect x="355" y="52" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="373" y="78" font-size="12.5" font-weight="700" fill="#06483f">Reliability and safety</text>
<text x="373" y="100" font-size="10.5" fill="#4a6b64">soft sensors near release &#183; spirit cuts</text>
<rect x="670" y="52" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="688" y="78" font-size="12.5" font-weight="700" fill="#06483f">Privacy and security</text>
<text x="688" y="100" font-size="10.5" fill="#4a6b64">loyalty &#183; taproom &#183; cellar door data</text>
<rect x="40" y="136" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="58" y="162" font-size="12.5" font-weight="700" fill="#06483f">Inclusiveness</text>
<text x="58" y="184" font-size="10.5" fill="#4a6b64">multilingual floor &#183; sensory language</text>
<rect x="355" y="136" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="373" y="162" font-size="12.5" font-weight="700" fill="#06483f">Transparency</text>
<text x="373" y="184" font-size="10.5" fill="#4a6b64">AI-written copy &#183; model cards</text>
<rect x="670" y="136" width="290" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="688" y="162" font-size="12.5" font-weight="700" fill="#06483f">Accountability</text>
<text x="688" y="184" font-size="10.5" fill="#4a6b64">a named owner &#183; an audit trail</text>
<line x1="500" y1="210" x2="500" y2="240" stroke="#2e9e7c" stroke-width="2.5"/>
<rect x="250" y="240" width="500" height="58" rx="10" fill="#06483f"/>
<text x="500" y="266" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">AI USE-CASE REGISTER</text>
<text x="500" y="286" text-anchor="middle" font-size="10.5" fill="#cfe6df">owner &#183; purpose &#183; data &#183; who it affects &#183; flags</text>
<line x1="500" y1="298" x2="500" y2="318" stroke="#2e9e7c" stroke-width="2.5"/>
<rect x="100" y="318" width="240" height="48" rx="8" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="220" y="340" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">TIER 1 &#183; HIGH</text>
<text x="220" y="356" text-anchor="middle" font-size="10" fill="#4a6b64">sign-off, evals, monitoring</text>
<rect x="380" y="318" width="240" height="48" rx="8" fill="#ffffff" stroke="#00695c" stroke-width="2"/>
<text x="500" y="340" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">TIER 2 &#183; MEDIUM</text>
<text x="500" y="356" text-anchor="middle" font-size="10" fill="#4a6b64">review, spot checks</text>
<rect x="660" y="318" width="240" height="48" rx="8" fill="#ffffff" stroke="#4db6a2" stroke-width="2"/>
<text x="780" y="340" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">TIER 3 &#183; LOW</text>
<text x="780" y="356" text-anchor="middle" font-size="10" fill="#4a6b64">log it, move on</text>
<text x="500" y="390" text-anchor="middle" font-size="10.5" fill="#4a6b64">the principles tell you what to ask &#183; the register tells you where to ask it</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The six principles become questions you ask of each AI system. The register is where the answers live, and the tier decides how much control each system needs.</figcaption>
</figure>

A few years ago the AI in a typical brewery was a spreadsheet with a trend line in it. Now the same brewery might have a soft sensor estimating gravity from CO2 flow, a language model writing the tap list blurbs, a recommender on the webshop and a vendor pitching an agent for the maintenance system. Nobody sat down and decided to become an AI company. It just accumulated, one tool at a time, the way unlabelled kegs accumulate in the back of a cold room.

That is exactly the situation Responsible AI was written for. This series, eight parts, works through it for beer, whisky and wine. This first part sets out the principles, the frameworks you will hear about, and the one table that turns all of it from talk into something you can query.

## The six principles, in drinks-business language

Most published Responsible AI principles, whether from standards bodies, governments or the large AI vendors, come down to the same six ideas. Here they are, with the examples that make them real in a brewhouse, a still house or a cellar.

**Fairness.** An AI system should not treat people worse because of who they are. In a drinks business this rarely looks like a headline scandal. It looks like a trade-promotion model that quietly stops offering deals to outlets in poorer neighbourhoods because they historically ordered less, or a CV-screening tool for the packaging line that downranks candidates from particular colleges. The question is simple: who gets a worse outcome from this model, and is that justified?

**Reliability and safety.** The system should work as intended, fail in predictable ways and not hurt anyone when it fails. This is where drinks are different from most retail. A soft sensor estimating attenuation is fine as a planning aid. The same model deciding whether a tank can be released, or a model nudging the heads and hearts cut on a spirit run, sits much closer to food safety. Methanol is not a rounding error.

**Privacy and security.** Personal data is handled lawfully, minimally and securely. Loyalty apps, taproom card data, cellar door mailing lists, age-verification records and CCTV all contain personal data. A recommender trained on purchase history is processing it. So is a camera that counts how often an operator is at the filler.

**Inclusiveness.** The system works for the people who actually have to use it. On a plant floor that means the shift supervisor who reads Kannada or Marathi more easily than English, the operator with gloves on, the taster whose flavour vocabulary was not learned from American craft beer reviews. An SOP assistant that only answers well in English is not inclusive, however accurate it is.

**Transparency.** People can tell when AI is involved and can get an explanation of what it did. A tasting note drafted by a model and published under the head distiller's name without a second look fails this one. So does a quality model that flags a batch with no reason attached.

**Accountability.** A named person owns each AI system and answers for it. Not "the data team", not the vendor. A person, with the authority to switch it off.

None of these is exotic. A good brewer already thinks this way about a new yeast strain: what could go wrong, how will I know, who decides. Responsible AI is that habit, applied to models.

## The frameworks you will hear about

There are a lot of acronyms in this space. For a drinks business, four matter, plus one data law for anyone operating in India.

**NIST AI Risk Management Framework (AI RMF 1.0).** Published by the US National Institute of Standards and Technology in 2023, voluntary and free. It organises the work into four functions: **Govern** (policies, roles, culture), **Map** (understand each system and its context), **Measure** (test and track the risks) and **Manage** (act on them). It is the most practical starting point I know, because it tells you what to do on a Monday morning rather than what to believe.

**ISO/IEC 42001:2023.** The international standard for an AI management system, built on the same pattern as ISO 9001 and ISO 22000, which most larger breweries and distilleries already know from quality and food safety. If you ever need to prove to a buyer or a regulator that your AI is governed, this is the certifiable route. For a small craft operation it is a destination, not a starting point.

**The EU AI Act.** A law, not a framework, and it applies if you place AI systems on the EU market or your AI's output is used there. It sorts AI into tiers: prohibited practices, high-risk systems with heavy obligations, systems with transparency duties (chatbots, AI-generated content), and everything else. At the time of writing (September 2026), the Digital Omnibus amendment has pushed the high-risk deadlines back to 2 December 2027 for Annex III systems and 2 August 2028 for Annex I, while the transparency duties in Article 50 kept their original timetable. Most drinks use cases will not be high-risk. Recruitment and worker-management tools can be, and GenAI marketing content falls squarely under the transparency duties. Part 2 goes into that.

**India's AI Governance Guidelines.** Released by MeitY on 5 November 2025. They are principles-based rather than a new AI law: seven guiding "sutras", including trust as the foundation, people first, innovation over restraint, fairness and equity, and accountability, with governance relying mainly on existing law and sector regulators. For a brewery or distillery in India, the practical reading is: nobody is going to hand you an AI rulebook, so the obligations come from the laws you already live under (consumer protection, advertising, food safety, excise) plus the next one.

**The Digital Personal Data Protection Act, 2023 (DPDP).** India's data protection law. The DPDP Rules were notified on 14 November 2025, with obligations phasing in; the bulk of the substantive duties apply from 14 May 2027. Any AI touching customer or employee personal data in India, which means most recommenders, loyalty models and camera systems, will sit under it.

This is not legal advice, and the dates move. The point is that every one of these starts with the same step. NIST calls it Map. ISO 42001 calls it scoping. The EU AI Act assumes you know which of your systems fall into which tier. You cannot do any of that without a list.

## The artefact: an AI use-case register

Most businesses, asked "what AI do you run?", produce an answer from memory and miss half of it. The marketing agency's image generator. The vendor's "smart" CIP optimiser. The ChatGPT subscription the QA manager pays for on their own card. A register fixes that by making the list a table, owned and queried like any other data.

Here is a minimal version. It is deliberately small. Every column earns its place by feeding a control later in the series.

```sql
-- One row per AI system the business uses or is building.
CREATE TABLE ai_use_case (
  use_case_id        TEXT PRIMARY KEY,
  name               TEXT NOT NULL,
  site               TEXT NOT NULL,          -- brewery, distillery, winery, head office
  owner              TEXT NOT NULL,          -- a person, never a team
  purpose            TEXT NOT NULL,
  ai_type            TEXT NOT NULL CHECK (ai_type IN
                       ('classic_ml','genai','agent','computer_vision','vendor_black_box')),
  decision_role      TEXT NOT NULL CHECK (decision_role IN
                       ('informs','drafts','decides')),  -- does a person act on it, edit it, or does it act?
  affects            TEXT NOT NULL,          -- consumers, employees, product, trade customers
  personal_data      BOOLEAN NOT NULL,
  product_safety     BOOLEAN NOT NULL,       -- can its output change what goes in the bottle?
  reaches_public     BOOLEAN NOT NULL,       -- is its output published or seen by consumers?
  minors_exposure    BOOLEAN NOT NULL,       -- could its output reach under-age people?
  markets            TEXT NOT NULL,          -- e.g. 'IN', 'IN,EU', 'UK'
  human_signoff      BOOLEAN NOT NULL,
  last_reviewed      DATE
);

INSERT INTO ai_use_case VALUES
 ('UC01','Fermentation gravity soft sensor','brewery','Head brewer',
  'Estimate gravity from CO2 flow and temperature between samples',
  'classic_ml','informs','product',FALSE,FALSE,FALSE,FALSE,'IN',TRUE,'2026-08-01'),
 ('UC02','GenAI social captions and images','head office','Brand manager',
  'Draft posts, captions and campaign images',
  'genai','drafts','consumers',FALSE,FALSE,TRUE,TRUE,'IN,UK',TRUE,NULL),
 ('UC03','Webshop drinks recommender','head office','E-commerce lead',
  'Rank products for logged-in customers',
  'classic_ml','decides','consumers',TRUE,FALSE,TRUE,FALSE,'IN',FALSE,NULL),
 ('UC04','Sensory note drafter','winery','Winemaker',
  'Turn panel scores into draft tasting notes',
  'genai','drafts','consumers',FALSE,FALSE,TRUE,FALSE,'IN,EU',TRUE,'2026-06-15'),
 ('UC05','CMMS work-order agent','distillery','Maintenance planner',
  'Draft work orders from recurring stops',
  'agent','drafts','employees',FALSE,FALSE,FALSE,FALSE,'IN',TRUE,'2026-09-01'),
 ('UC06','Spirit cut-point advisor','distillery','Head distiller',
  'Suggest heads and hearts cut from inline sensors',
  'classic_ml','informs','product',FALSE,TRUE,FALSE,FALSE,'IN',TRUE,NULL),
 ('UC07','CV safety cameras','brewery','EHS manager',
  'Detect missing PPE and confined-space entry',
  'computer_vision','informs','employees',TRUE,FALSE,FALSE,FALSE,'IN',TRUE,NULL);
```

Two columns do most of the work. `decision_role` separates a model that informs a person from one that drafts for approval and one that decides on its own; that single distinction changes how much can go wrong. The four boolean flags (personal data, product safety, public reach, minors) are the drinks-specific risks. The last one is there because alcohol is one of the few products where "our AI showed this to a sixteen-year-old" is a regulatory event, not just an embarrassment.

Now the tiering query. It is plain SQL on purpose. The rules are readable by the head brewer and the auditor alike, and changing them is a code review, not a meeting.

```sql
-- Assign a risk tier and list what is overdue.
WITH scored AS (
  SELECT *,
    CASE
      WHEN product_safety AND decision_role <> 'informs'           THEN 1
      WHEN minors_exposure AND reaches_public                        THEN 1
      WHEN personal_data AND decision_role = 'decides'               THEN 1
      WHEN ai_type = 'computer_vision' AND affects = 'employees'     THEN 1
      WHEN reaches_public OR personal_data OR product_safety         THEN 2
      ELSE 3
    END AS risk_tier
  FROM ai_use_case
)
SELECT use_case_id, name, owner, risk_tier,
       CASE risk_tier
         WHEN 1 THEN 'sign-off, pre-release evals, monitoring, review every 6 months'
         WHEN 2 THEN 'human review, spot checks, review every 12 months'
         ELSE        'log it'
       END AS required_controls,
       CASE
         WHEN last_reviewed IS NULL THEN 'NEVER REVIEWED'
         WHEN risk_tier = 1 AND last_reviewed < CURRENT_DATE - INTERVAL '6 months'  THEN 'OVERDUE'
         WHEN risk_tier = 2 AND last_reviewed < CURRENT_DATE - INTERVAL '12 months' THEN 'OVERDUE'
         ELSE 'ok'
       END AS review_status
FROM scored
ORDER BY risk_tier, review_status DESC;
```

Run it against the seven rows above and the shape of your Responsible AI work falls out. The GenAI captions (public, could reach minors) land in tier 1. So do the webshop recommender (personal data, deciding on its own) and the safety cameras (watching employees). The spirit cut-point advisor lands in tier 2 only because it informs; the moment someone proposes letting it set the cut, the flag flips and it jumps to tier 1. The gravity soft sensor and the maintenance agent sit lower, which matches instinct: a wrong gravity estimate between samples costs a phone call, not a recall.

The tiers here are my own, not any regulator's. They are not the EU AI Act categories and should not be presented as such. They are a way of deciding where to spend limited attention, which is the actual constraint in a forty-person brewery.

## From register to routine

The register is only useful if it stays true. Three habits keep it that way.

**New AI goes in before it goes live.** Treat it like a new raw material supplier: no approval, no purchase order. That includes free tools and vendor features switched on in an update.

**Owners review on the calendar.** The query above prints `OVERDUE` for a reason. Put the review in the diary, tied to a date, not to someone remembering.

**The register is linked, not duplicated.** Evals, incident notes and model cards later in the series all hang off `use_case_id`. One key, many artefacts. That is basic data modelling, and it is the difference between a governance system and a folder of PDFs.

## Where this breaks

**Nobody owns the vendor black boxes.** The "AI-powered" feature inside the brewhouse control software, the ERP's demand forecast, the label printer's inspection camera. They are AI, they affect product and people, and the vendor will not tell you much. Register them anyway with `ai_type = 'vendor_black_box'` and ask the vendor the tier 1 questions in writing.

**Shadow AI never makes it into the table.** The QA manager pasting complaint emails into a public chatbot is processing personal data through an AI system. A register only catches what people declare. Pair it with a short, sane acceptable-use policy and an approved tool, so the easy path is also the compliant one.

**Tiers become a box-ticking exercise.** A register where every row is tier 3 because tier 1 means paperwork is worse than no register. Have someone outside the owning team look at the flags once a year.

**It feels like overhead for a small operation.** Seven rows and one query is an afternoon. The expensive version is discovering, after a complaint or an inspection, that nobody knew the webshop was running a model on customer data at all.

## The bottom line

Responsible AI for a brewery, distillery or winery is six familiar ideas (fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability) applied to the specific AI you run. Every framework on offer, from the NIST AI RMF to ISO/IEC 42001 to the EU AI Act and India's AI Governance Guidelines, starts with knowing what that AI is. So start with the table. One row per system, a named owner, four drinks-specific risk flags and a tiering query anyone can read. The frameworks will argue about the rest. The register is the part nobody can argue with, because it is just the truth about what you already have.

For how honest limits look in practice, see [The Honest Limits of AI in Brewing]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}), and for the guardrails on an agent, [Agentic AI for OpEx]({{ '/2026/agentic-ai-opex-oee-agent-cmms-guardrails/' | relative_url }}).

Next: [GenAI marketing for a product you cannot sell to minors]({{ '/2026/genai-alcohol-marketing-guardrails-age-codes/' | relative_url }}). The full list is on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**What is Responsible AI in plain terms?**
It is the discipline of building and running AI so that it is fair, reliable and safe, respects privacy and security, works for everyone who has to use it, can be explained, and has a named person accountable for it. For a brewery, distillery or winery it mostly comes down to three questions per use case: who can this harm, how would we know, and who signs off.

**Which Responsible AI framework should a small drinks business follow?**
Use the NIST AI Risk Management Framework as the working method (Govern, Map, Measure, Manage), because it is free, practical and not tied to one country. Treat ISO/IEC 42001 as the destination if you ever need certification. Then check the specific laws where you sell: the EU AI Act for Europe, and in India the AI Governance Guidelines plus the DPDP Act for personal data.

**What is an AI use-case register?**
A single table that lists every AI system the business uses or is building, with its owner, purpose, data, who it affects, whether it touches personal data, product safety or minors, and a risk tier. It is the first Responsible AI artefact to build because every other control (reviews, evals, monitoring) hangs off it. Without it you cannot answer the simplest audit question: what AI do we actually run?
