---
layout: post
title: "Provenance, Fakes and Synthetic Labels: A Hash-Chained Cask Ledger, C2PA and Label Claims You Can Prove"
image: /assets/og/provenance-fakes-c2pa-traceability-whisky-wine.png
description: "Part 6 of Responsible AI for Beer, Whisky and Wine. GenAI makes a convincing fake label, bottle photo or heritage story in seconds, and it can just as easily draft an illegal age statement for your own product. How an append-only, hash-chained traceability ledger from cask or tank to bottle, label claims derived from that ledger, and C2PA Content Credentials on your images give you provenance you can actually prove."
date: 2026-09-28 09:00:00 -0700
updated: 2026-09-28
tags: [distilling-maturation, rai-beverage, provenance, event-sourcing, genai]
faq:
  - q: "How does generative AI make whisky and wine fraud easier?"
    a: "It lowers the cost of every piece of a fake that used to take skill: a convincing label, a period-correct bottle photograph, an invented provenance story, a forged certificate. It also creates a quieter risk inside honest businesses, where a model drafting label or marketing copy invents an age, a cask or a region that the product cannot support."
  - q: "What does the Scotch Whisky Regulations 2009 say about age statements?"
    a: "If a Scotch Whisky carries an age statement, the age must be that of the youngest whisky in the bottle. A blend of 12, 15 and 18 year old whiskies can only be called 12 years old. A system that generates label copy should derive the age from the component records rather than let anyone, or any model, type it in."
  - q: "What is C2PA and does it stop fakes?"
    a: "C2PA is an open standard for Content Credentials: signed, tamper-evident metadata that records where an image or video came from and how it was edited. It helps you prove your own photographs and labels are genuine, and it lets platforms flag unsigned or AI-generated media. It does not stop anyone making a fake, and credentials can be stripped, so it proves authenticity rather than preventing forgery."
---

**Short answer: GenAI has made faking a bottle cheaper than ever. A label, a period photograph, a heritage story and a certificate of authenticity are a few prompts away. The same tools create a quieter risk inside honest businesses: a model drafting label copy that calls a blend "aged 18 years" when one component is 12, which under the Scotch Whisky Regulations 2009 is simply unlawful. The defence is the same for both. Keep an append-only, hash-chained ledger of every event from cask or tank to bottle, generate every label claim from that ledger instead of typing it, and sign your own images with C2PA Content Credentials so that genuine media can prove it is genuine.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A provenance chain from cask to label. Five ledger events in a row: fill, re-rack, sample, vat and bottle. Each event box shows its own hash and the previous event's hash, linked by arrows to show the chain. From the vat event, a query derives the age statement as the youngest component, 12 years. The label generator takes claims only from the ledger query. A red crossed-out path shows a typed or model-invented claim of 18 years being rejected. On the right, the bottle photograph is signed with C2PA Content Credentials.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EVERY LABEL CLAIM COMES FROM THE LEDGER, NEVER FROM A PROMPT</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="150" height="70" rx="9" fill="#06483f"/>
<text x="105" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">FILL</text>
<text x="105" y="98" text-anchor="middle" font-size="10" fill="#cfe6df">cask 4471 &#183; 2014</text>
<text x="105" y="115" text-anchor="middle" font-size="9.5" fill="#4db6a2">hash a3f9 &#183; prev 0000</text>
<rect x="210" y="56" width="150" height="70" rx="9" fill="#06483f"/>
<text x="285" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">RE-RACK</text>
<text x="285" y="98" text-anchor="middle" font-size="10" fill="#cfe6df">to refill hogshead</text>
<text x="285" y="115" text-anchor="middle" font-size="9.5" fill="#4db6a2">hash 7c21 &#183; prev a3f9</text>
<rect x="390" y="56" width="150" height="70" rx="9" fill="#06483f"/>
<text x="465" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">SAMPLE</text>
<text x="465" y="98" text-anchor="middle" font-size="10" fill="#cfe6df">ABV 58.2 &#183; lab</text>
<text x="465" y="115" text-anchor="middle" font-size="9.5" fill="#4db6a2">hash 19be &#183; prev 7c21</text>
<rect x="570" y="56" width="150" height="70" rx="9" fill="#06483f"/>
<text x="645" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">VAT</text>
<text x="645" y="98" text-anchor="middle" font-size="10" fill="#cfe6df">12 + 15 + 18 yr</text>
<text x="645" y="115" text-anchor="middle" font-size="9.5" fill="#4db6a2">hash e04d &#183; prev 19be</text>
<rect x="750" y="56" width="150" height="70" rx="9" fill="#06483f"/>
<text x="825" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">BOTTLE</text>
<text x="825" y="98" text-anchor="middle" font-size="10" fill="#cfe6df">lot B-2026-091</text>
<text x="825" y="115" text-anchor="middle" font-size="9.5" fill="#4db6a2">hash 5a8e &#183; prev e04d</text>
<line x1="180" y1="91" x2="210" y2="91" stroke="#4db6a2" stroke-width="2.5"/>
<line x1="360" y1="91" x2="390" y2="91" stroke="#4db6a2" stroke-width="2.5"/>
<line x1="540" y1="91" x2="570" y2="91" stroke="#4db6a2" stroke-width="2.5"/>
<line x1="720" y1="91" x2="750" y2="91" stroke="#4db6a2" stroke-width="2.5"/>
<line x1="645" y1="126" x2="645" y2="164" stroke="#00695c" stroke-width="2"/>
<rect x="520" y="164" width="250" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="645" y="187" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">age = MIN(component age)</text>
<text x="645" y="206" text-anchor="middle" font-size="11" fill="#2e9e7c">12 years old, the only legal claim</text>
<line x1="645" y1="220" x2="645" y2="252" stroke="#2e9e7c" stroke-width="2.5"/>
<rect x="520" y="252" width="250" height="46" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="1.5"/>
<text x="645" y="280" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">label generator</text>
<rect x="60" y="178" width="360" height="100" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="240" y="204" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">typed or model-invented claim</text>
<text x="240" y="226" text-anchor="middle" font-size="11" fill="#4a6b64">"aged 18 years" &#183; "sherry cask"</text>
<text x="240" y="248" text-anchor="middle" font-size="11" fill="#4a6b64">"single estate" &#183; "gold medal"</text>
<text x="240" y="268" text-anchor="middle" font-size="10" fill="#4a6b64">no ledger row, no claim</text>
<line x1="420" y1="275" x2="520" y2="275" stroke="#ff4081" stroke-width="2.5" stroke-dasharray="5 4"/>
<line x1="460" y1="263" x2="480" y2="287" stroke="#ff4081" stroke-width="3"/>
<line x1="480" y1="263" x2="460" y2="287" stroke="#ff4081" stroke-width="3"/>
<rect x="800" y="164" width="170" height="134" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="885" y="190" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">C2PA</text>
<text x="885" y="212" text-anchor="middle" font-size="10.5" fill="#06483f">bottle photo signed</text>
<text x="885" y="230" text-anchor="middle" font-size="10.5" fill="#06483f">at capture</text>
<text x="885" y="256" text-anchor="middle" font-size="10.5" fill="#4a6b64">edits recorded</text>
<text x="885" y="274" text-anchor="middle" font-size="10.5" fill="#4a6b64">AI use declared</text>
<line x1="770" y1="275" x2="800" y2="275" stroke="#00695c" stroke-width="2"/>
<rect x="30" y="318" width="940" height="44" rx="10" fill="#06483f"/>
<text x="500" y="345" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">CHANGE ONE EVENT AND EVERY LATER HASH BREAKS &#183; THE LABEL CAN ONLY SAY WHAT THE CHAIN PROVES</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Each event carries the hash of the one before it, so history cannot be quietly rewritten. The label pulls its claims from a query over that chain, and the photos that sell the bottle carry signed credentials.</figcaption>
</figure>

Anyone who has worked a bonded warehouse knows the stencil on a cask end is the first document and the least reliable one. It fades, it gets painted over when the cask is reused, and a cask moved in a hurry on a Friday afternoon ends up in the wrong row. The real record lives in the warehouse system, and the question this post asks is simple: can that record prove what the label says?

This is part 6. [Part 5]({{ '/2026/sensory-ai-bias-tasting-note-hallucination-evals/' | relative_url }}) stopped a language model inventing casks and awards in a tasting note. This one goes up a level, to the label and the image, where invented claims stop being a trust problem and become a legal one.

## The fraud problem GenAI made cheaper

Fine wine and rare whisky have always attracted forgers. The best-known wine case, Rudy Kurniawan, was convicted in the US in 2013 for selling counterfeit Burgundy and Bordeaux into the top of the market. On the whisky side, a widely reported 2018 test of rare Scotch by a specialist firm found that a large share of the supposedly vintage bottles it sampled were fake. These fakes took skill: sourcing old glass, printing period-correct labels, building a story.

Generative AI has taken most of the skill out. Image models produce a convincing label in any period style. They will render a bottle photograph with the right dust, the right fill level and the right auction-house lighting. Language models write the provenance story, the letter from the late collector, the certificate. None of this makes the liquid, and the liquid is still where most fakes are caught. But the paper trail around a bottle, which used to be the hard part, is now the cheap part.

I covered the classic ML side of detecting fakes in [beer authentication and counterfeit detection]({{ '/2022/beer-authentication-counterfeit-ml/' | relative_url }}). Detection matters. This post is about the other half: making your genuine products provable, so that a fake has to beat a record and not just a photograph.

## The quieter risk: honest businesses, invented claims

The more common failure is not a forger. It is a marketing team using a model to draft label copy, a web page or a sell sheet, and the model doing what models do: filling gaps with plausible detail.

The Scotch Whisky Regulations 2009 are clear on age. If a Scotch Whisky carries an age statement, the age must be that of the youngest whisky in the bottle. Vat a 12, a 15 and an 18 year old and the most you may say is 12 years old. Ask a general-purpose model for "premium label copy for our 18-year-inspired blend" and there is a real chance it gives you "aged 18 years" in the first line, because that is what premium copy looks like in its training data. A tired reviewer approves it. The product is now mislabelled.

The same pattern shows up with regions and geographical indications. Champagne, Scotch Whisky and, in India, Goa Cashew Feni are protected names with rules behind them. "Single estate", "old vines", "first-fill sherry" and "small batch" may be less regulated in some markets, but each is a factual claim a customer or a regulator can test. A model does not know which of your claims are true. Only your records do.

## The data pattern: an append-only, hash-chained ledger

The fix is to make the production record the single source of every claim, and to make that record tamper-evident.

**Event-sourced.** Do not store a cask as a row you update. Store every event that happened to it: filled, re-racked, sampled, topped, vatted, bottled. The current state is a query over the events. I made the case for this in [event-sourced cellar records for wineries]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) and for spirit in [cask inventory data engineering with SCD2]({{ '/2026/cask-inventory-data-engineering-scd2/' | relative_url }}). The same design holds for a beer tank or a wine lot.

**Append-only.** Events are never edited or deleted. A mistake is corrected by a new correcting event that references the old one. The history shows both.

**Hash-chained.** Each event stores a hash of its own content plus the hash of the previous event for that cask or lot. Change any past event and every later hash stops matching. You do not need a blockchain for this. A column and a trigger do the job, and an auditor can recompute the chain with a script.

**Claims are queries.** The label generator does not accept free text for factual fields. Age, cask types, region, vintage and ABV are the results of queries over the ledger. The language model, if you use one, writes the tone around those facts, the same grounded pattern as the tasting notes in part 5.

Here is the core of it in Postgres-flavoured SQL.

```sql
-- one row per thing that happened; never updated, never deleted
CREATE TABLE lot_event (
  event_id     bigserial PRIMARY KEY,
  lot_id       text        NOT NULL,     -- cask, tank or bottling lot
  event_type   text        NOT NULL,     -- fill | rerack | sample | vat | bottle | correction
  occurred_at  timestamptz NOT NULL,
  spirit_born  date,                     -- date the spirit first went into oak (fill events)
  source_lots  text[],                   -- component lots (vat events)
  payload      jsonb       NOT NULL,     -- cask type, ABV, litres, operator
  prev_hash    text        NOT NULL,
  hash         text        NOT NULL      -- sha256(prev_hash || lot_id || event_type || occurred_at || payload)
);

REVOKE UPDATE, DELETE ON lot_event FROM PUBLIC;  -- append-only by permission, not by promise

-- the only legal age statement for a vatting: the youngest component, in whole years
SELECT v.lot_id AS vatted_lot,
       MIN(EXTRACT(YEAR FROM age(v.occurred_at, f.spirit_born)))::int AS age_statement_years
FROM   lot_event v
CROSS  JOIN LATERAL unnest(v.source_lots) AS c(component_lot)
JOIN   lot_event f
       ON f.lot_id = c.component_lot AND f.event_type = 'fill'
WHERE  v.event_type = 'vat'
GROUP  BY v.lot_id;
```

That query is deliberately boring. It takes the maturation start for each component and the date the components left the wood, and it takes the minimum. The label field reads from it. Nobody types an age. If the query returns 12, the label cannot say 18, however good the copy sounds.

Two cautions. Real maturation accounting is messier than one fill date: re-racked spirit, finishing casks and partial vattings need care, and the legal definitions vary by category and country. Treat this as the shape of the answer, not a compliance ruling, and have the rules checked by whoever signs your labels. And the hash chain proves the record was not changed after the fact. It does not prove the first entry was true. A cask entered wrongly on day one is wrong forever, with a perfect hash.

## Signing the pictures: C2PA Content Credentials

The ledger covers the liquid and the label. The images need their own proof, because images are where fakes now look most convincing.

C2PA, from the Coalition for Content Provenance and Authenticity, is an open standard for Content Credentials: signed, tamper-evident metadata attached to an image or video that records where it came from, what edited it, and whether AI was used. The current specification is in the 2.x family. Adoption is real: Google's Pixel 10 signs every photo taken in its camera app by default, with hardware-backed keys, and Samsung's Galaxy line has moved from signing only AI-edited images towards signing at capture. Several professional cameras and editing tools support it too.

For a distillery or winery, the practical use is modest and useful.

- **Shoot product and cask photography on devices that sign at capture**, and keep the credentials through your editing tools.
- **Declare AI use in the credentials** when a background is generated or a label is mocked up. Honest disclosure is the point.
- **Publish signed originals** on your own site and press page, so that a buyer, an auction house or a journalist can check a photo against your credentials.
- **Link the image to the ledger.** A bottle shot's credentials can reference the bottling lot, so that the photo and the record point at each other.

Regulation is heading the same way. The EU AI Act's Article 50(2) requires providers of generative AI systems to mark synthetic output in a machine-readable way, with that obligation applying from 2 December 2026 under the recently amended timeline. That duty sits with the model providers rather than with a winery, but it means signed and marked media are becoming the norm, and unsigned media will attract more questions over time.

## Where this breaks

**Garbage in, hashed forever.** The chain makes history tamper-evident, not true. If the warehouse team scans the wrong cask on fill day, the error is permanent and perfectly hashed. Put the effort into capture: barcodes or RFID on casks, scans at every move, and correction events that are easy to raise.

**Credentials get stripped.** Screenshots, re-uploads and some social platforms drop C2PA metadata. A missing credential proves nothing either way. Credentials help genuine media prove itself; they do not catch fakes on their own.

**The liquid is still the test.** A perfect ledger and a signed photo do not tell you what is in a bottle on the secondary market. Closures, glass, and analytical testing of the liquid still carry most of the weight for fakes already in circulation.

**People bypass the generator.** If marketing can still paste copy into a design tool, the ledger-derived fields are a suggestion. Lock factual fields in the artwork workflow, and make the approval step show the ledger source next to each claim.

**Rules differ by market.** Age, vintage and region rules for Scotch, bourbon, Indian whisky, wine GIs and beer differ. Encode each as a separate, reviewed rule. A single "age = min" query is right for Scotch and needs checking everywhere else.

## The bottom line

GenAI made a convincing fake label, photograph and provenance story nearly free, and it made it just as easy for an honest team to publish an age or a cask the product cannot support. The answer for both is to make the record the source of every claim. Keep an append-only, hash-chained ledger from cask or tank to bottle. Generate factual label fields from queries over it, so the only age a blend can carry is its youngest component. Sign your own images with C2PA Content Credentials and declare any AI use in them. None of it stops a determined forger. All of it means your genuine bottle can prove itself, and your own copy cannot drift past the truth.

Next: [accountability when an agent drafts the decision]({{ '/2026/agent-accountability-audit-logs-worker-monitoring/' | relative_url }}), where the ledger idea becomes an audit log for every tool call. For traceability on the brewing side, see [food safety traceability from grain to glass]({{ '/2025/food-safety-traceability-grain-to-glass/' | relative_url }}). The full list is on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**How does generative AI make whisky and wine fraud easier?**
It lowers the cost of every piece of a fake that used to take skill: a convincing label, a period-correct bottle photograph, an invented provenance story, a forged certificate. It also creates a quieter risk inside honest businesses, where a model drafting label or marketing copy invents an age, a cask or a region that the product cannot support.

**What does the Scotch Whisky Regulations 2009 say about age statements?**
If a Scotch Whisky carries an age statement, the age must be that of the youngest whisky in the bottle. A blend of 12, 15 and 18 year old whiskies can only be called 12 years old. A system that generates label copy should derive the age from the component records rather than let anyone, or any model, type it in.

**What is C2PA and does it stop fakes?**
C2PA is an open standard for Content Credentials: signed, tamper-evident metadata that records where an image or video came from and how it was edited. It helps you prove your own photographs and labels are genuine, and it lets platforms flag unsigned or AI-generated media. It does not stop anyone making a fake, and credentials can be stripped, so it proves authenticity rather than preventing forgery.
