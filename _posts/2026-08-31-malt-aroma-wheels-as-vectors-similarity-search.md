---
layout: post
title: "Malt Aroma Wheels as Vectors: Similarity Search and the Blend That Averaging Hides"
image: /assets/og/malt-aroma-wheels-as-vectors-similarity-search.png
description: "Part 3 of The Brewer's Agent. Turn published malt aroma wheels into 22-number vectors and you can search for substitutes and predict grist character. Real numbers from 51 digitised Weyermann wheels show the traps: raw cosine says every malt is alike, variants collapse onto one vector, and a plain average hides 10% of roasted malt."
date: 2026-08-31 09:00:00 -0700
updated: 2026-08-31
tags: [brewing-science, brewers-agent, embeddings, vector-search, malting]
faq:
  - q: "Can you use vector similarity to find a malt substitute?"
    a: "Yes, with care. Turn each malt's aroma wheel into a vector of descriptor intensities and compare vectors to find close matches. Centre the vectors on the average malt first, because raw cosine similarity rates almost every pair as similar, and filter on colour and extract as hard constraints so the aroma match cannot suggest a malt of the wrong colour."
  - q: "Why does averaging aroma vectors underestimate specialty malts?"
    a: "Because a strong minority character is diluted by the mass of base malt. In a 90% Pilsner and 10% roasted malt grist, a plain mass-weighted average puts coffee at 0.4 on a 0 to 5 scale, while brewers know 10% of a dark roasted malt is clearly noticeable. A model that weights by aroma potency and lets the strongest contributor show through gives about 2.6."
  - q: "Should malt aroma vectors go in a vector database?"
    a: "For a few dozen malts, no. A table and a few lines of code are enough. A vector database earns its place when you combine many sources, such as hundreds of malts, hop descriptors and tasting notes as text embeddings, and need filtered search across them."
---

**Short answer: a malt aroma wheel is already a vector. Twenty-two descriptors scored 0 to 5, from coffee to honey to biscuit, is 22 numbers per malt, and once you have those you can search for substitutes and estimate the character of a grist. The real numbers from 51 digitised wheels show three traps. Raw cosine similarity rates almost every malt as similar (median 0.91), so centre the vectors first. Malt variants that share a published wheel collapse onto one vector, so colour and extract have to come from the specification. And a plain average of 90% Pilsner and 10% CARAFA Special puts coffee at 0.4 out of 5, which every brewer knows is wrong.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two findings from 51 digitised malt aroma wheels. On the left, cosine similarity between Pilsner malt and CARAFA Special Type 2 is 0.82 on raw vectors, suggesting they are alike, and minus 0.66 after centring on the average malt, correctly showing they are opposites. The median raw cosine across all malt pairs is 0.91. On the right, for a grist of 90 percent Pilsner and 10 percent CARAFA Special Type 2, the coffee note is 0.4 out of 5 by plain mass averaging and 2.6 out of 5 by potency-weighted superposition.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">51 MALT WHEELS AS VECTORS: TWO THINGS THE NAIVE MATHS GETS WRONG</text>
<g font-family="sans-serif">
<text x="245" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">PILSNER vs CARAFA SPECIAL 2: SIMILARITY</text>
<rect x="40" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#ff4081" stroke-width="2"/>
<text x="140" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">raw cosine</text>
<text x="140" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#ff4081">0.82</text>
<rect x="260" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="360" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">centred cosine</text>
<text x="360" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#2e9e7c">&#8722;0.66</text>
<text x="250" y="200" text-anchor="middle" font-size="11" fill="#06483f">median raw cosine across all pairs: 0.91</text>
<text x="250" y="218" text-anchor="middle" font-size="11" fill="#06483f">everything looks alike until you subtract the average malt</text>
<text x="745" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">90% PILSNER + 10% CARAFA SPECIAL 2: COFFEE (0 TO 5)</text>
<rect x="560" y="90" width="30" height="34" rx="4" fill="#ff4081"/>
<text x="600" y="113" font-size="12" font-weight="700" fill="#06483f">0.4 plain mass average</text>
<rect x="560" y="140" width="195" height="34" rx="4" fill="#06483f"/>
<text x="765" y="163" font-size="12" font-weight="700" fill="#06483f">2.6 potency-weighted</text>
<text x="745" y="205" text-anchor="middle" font-size="11" fill="#06483f">CARAFA alone scores 4 for coffee, Pilsner scores 0</text>
<text x="745" y="223" text-anchor="middle" font-size="11" fill="#06483f">averaging buries the note a brewer can taste</text>
<rect x="40" y="262" width="920" height="50" rx="10" fill="#06483f"/>
<text x="500" y="285" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">A VECTOR IS A GOOD START &#183; THE MATHS ON TOP IS WHERE THE BREWING KNOWLEDGE GOES</text>
<text x="500" y="302" text-anchor="middle" font-size="10.5" fill="#cfe6df">computed from 22-descriptor vectors digitised from published Weyermann wort aroma wheels</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Two numbers that look reasonable and are wrong, and the two small changes that fix them.</figcaption>
</figure>

Weyermann publishes an aroma wheel for most of its malts: a circle of descriptors (coffee, cacao, bready, honey, toffee, dried fruit and so on), each scored for intensity. Brewers use them to read one malt at a time. Stack them and you have something more interesting: a table where every malt is a row of numbers. In the language of GenAI, that is an embedding, just one a person can read.

I digitised 51 of those wheels into 22-descriptor vectors on a 0 to 5 scale while building a small open tool to play with this. The earlier post on [stacking malt flavour wheels]({{ '/2026/predicting-beer-flavour-malt-coa-flavour-wheels/' | relative_url }}) made the case for treating a grist as a weighted sum. This one is about what happens when you do vector search and blending on those numbers properly, and where the naive version quietly fails.

## A wheel is a vector

Each malt becomes a row like this, trimmed to a few descriptors:

| malt | coffee | dark chocolate | bready | honey | toffee | ... |
|---|---|---|---|---|---|---|
| Pilsner Malt | 0.0 | 1.0 | 2.0 | 1.0 | 1.5 | ... |
| CARAFA Special Type 2 | 4.0 | 3.0 | 4.0 | 1.5 | 2.5 | ... |

Put a few dozen of those in a table and two useful questions become one-liners. Which malt is most like this one? And what does this grist smell like?

These are the same operations a RAG system runs on text embeddings, similarity search and combination, only here the dimensions have names. That makes this a very good place to learn how vector maths behaves, because you can check every result against what a brewer knows.

## Trap 1: raw cosine says every malt is alike

Cosine similarity is the default way to compare vectors. It measures the angle between them, ignoring length, and runs from 1 (same direction) to minus 1 (opposite).

On the raw wheel vectors, the median cosine similarity across every pair of malts is **0.91**. Pilsner malt and CARAFA Special Type 2, a pale base malt and a dehusked roasted malt, score **0.82**. By that measure they are close relatives.

The reason is simple. Every wheel has a baseline of low scores across most descriptors: a bit of bready, a bit of sweet, a bit of honey. All the vectors point roughly the same way because they all share that floor. Cosine sees the shared floor and misses the difference on top.

The fix is to **centre** the vectors: subtract the average malt from each one before comparing. Now each vector describes how a malt differs from a typical malt. Pilsner against CARAFA Special 2 drops to **minus 0.66**, correctly opposite. Pilsner against Munich Type 1 comes out at 0.44, related but distinct, which is about what a brewer would say.

The same thing happens with text embeddings in RAG systems, where it is called anisotropy: everything clusters in one corner of the space and scores look higher than they should. It is much easier to see with malt.

## Trap 2: variants collapse onto one vector

Of the 51 malts, only **40 distinct vectors** exist. Weyermann publishes one wheel for several malts in a family, so CARAMUNICH Types 1, 2 and 3 share a wheel, and so do the three CARAFA Special types. Their cosine similarity to each other is exactly 1.0.

That is not a data error. It is what the source says. But it means an aroma-only search for "something like CARAMUNICH Type 2" will happily return Type 1 or Type 3 as perfect matches, although the family runs from 80 to 160 EBC and Type 2 sits at 110 to 130. CARAFA Special spans 800 to 1,500 EBC on one shared wheel. The vectors hold aroma. They do not hold colour, extract or enzyme activity.

So substitute search has to be **hybrid**: hard filters on the specification first (colour band, extract, maximum addition rate), then vector similarity to rank what is left. That is exactly the pattern for RAG over documents, where you filter by metadata such as date or source before ranking by meaning. Pure vector search, in either setting, will return confident nonsense when the thing that matters is not in the vector.

## Trap 3: averaging hides the specialty malt

Now blend. The obvious model for a grist is a mass-weighted average: 90% Pilsner, 10% CARAFA Special 2, so each descriptor is 0.9 times Pilsner's score plus 0.1 times CARAFA's.

For coffee, that gives **0.4 out of 5**. Pilsner has none and CARAFA has 4, so the average says a faint hint. Any brewer who has put 10% of a dark roasted malt in a beer knows it is not a faint hint. Small charges of potent malts punch far above their weight.

A better model does two things. It weights each malt by an aroma **potency** as well as its share (roasted malts are rated several times more potent than base malts), and it lets the strongest single contributor show through rather than averaging it away. With the calibration I used, that gives coffee at about **2.6**, clearly present, while a 100% Pilsner grist still reproduces Pilsner's own wheel.

The constants in that model are judgement calls, tuned so single malts reproduce their own wheels and so familiar grists taste roughly right on paper. That is the honest status of it: a sensible structure with calibrated knobs, not a law of nature.

## Where GenAI fits

This is a case where the vector maths should stay in plain code, and the language model does the talking:

- **Explaining a prediction.** Given the blended vector and the top contributors for each note, an LLM writes the tasting-style summary: "roast leads, coffee and dark chocolate from the CARAFA, bready malt underneath". It describes numbers it was handed. It does not invent them.
- **Mapping free text to descriptors.** Brewers describe malts in their own words. An LLM can map "toasty, a bit like digestive biscuits" onto the biscuit and bready axes so a text query can search the numeric vectors.
- **Joining with text embeddings.** Tasting notes, supplier descriptions and competition feedback can be embedded as text and searched alongside the numeric wheels. That is where a vector database starts to earn its keep. For 51 malts on their own, a table and a few lines of code are plenty.

## Where this breaks

**The wheels describe wort, not beer.** The published wheels are for a congress-style wort or the whole kernel. Fermentation, hopping and time change what survives into the glass. Any prediction from them is about the malt's contribution, not the finished beer.

**Digitising a wheel is itself a measurement.** Reading intensities off a printed chart, by eye or with a vision model, adds error of perhaps half a point per descriptor. Treat the vectors as approximate.

**Perception is not linear.** Aromas mask, enhance and suppress each other. No weighted sum captures that fully, which is why the potency model is a calibration rather than a derivation.

**Not an official product.** Vectors derived from a maltster's published material are an independent reading of it. They are not endorsed by the maltster and should not be presented as if they were.

## The bottom line

Malt aroma wheels are a gift for anyone learning vector search, because every dimension has a name a brewer understands. They also show the standard traps in plain sight: raw cosine flatters everything, vectors only hold what you put in them, and averages bury strong minorities. Centre before comparing, filter on specification before ranking, weight by potency before blending, and let the language model explain the numbers rather than make them up.

Next in the series: [scraping and trend-mining 250 public homebrew recipes]({{ '/2026/scraping-trend-mining-250-homebrew-recipes/' | relative_url }}). For hops, the sister problem, see [AI for Hop Aroma Profiling and Smart Substitution]({{ '/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}). The full list is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**Can you use vector similarity to find a malt substitute?**
Yes, with care. Turn each malt's aroma wheel into a vector of descriptor intensities and compare vectors to find close matches. Centre the vectors on the average malt first, because raw cosine similarity rates almost every pair as similar, and filter on colour and extract as hard constraints so the aroma match cannot suggest a malt of the wrong colour.

**Why does averaging aroma vectors underestimate specialty malts?**
Because a strong minority character is diluted by the mass of base malt. In a 90% Pilsner and 10% roasted malt grist, a plain mass-weighted average puts coffee at 0.4 on a 0 to 5 scale, while brewers know 10% of a dark roasted malt is clearly noticeable. A model that weights by aroma potency and lets the strongest contributor show through gives about 2.6.

**Should malt aroma vectors go in a vector database?**
For a few dozen malts, no. A table and a few lines of code are enough. A vector database earns its place when you combine many sources, such as hundreds of malts, hop descriptors and tasting notes as text embeddings, and need filtered search across them.
