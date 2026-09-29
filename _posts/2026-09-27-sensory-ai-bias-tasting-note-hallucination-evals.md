---
layout: post
title: "Whose Palate Did the Model Learn? Bias in Sensory AI, and Evals That Catch Hallucinated Tasting Notes"
image: /assets/og/sensory-ai-bias-tasting-note-hallucination-evals.png
description: "Part 5 of Responsible AI for Beer, Whisky and Wine. Flavour models and LLMs learn a Western tasting vocabulary and a narrow panel, then write confident notes that invent casks, vineyards and awards. How to find the bias in descriptor data and panels, how to ground note drafting in the batch record, and how to build an eval set that checks every claim in a tasting note against its source."
date: 2026-09-27 15:00:00 -0700
updated: 2026-09-27
tags: [winemaking, rai-beverage, sensory, genai, llm-evals]
faq:
  - q: "Why are sensory AI models biased?"
    a: "They learn from the data they are given, and most flavour descriptor data comes from Western lexicons, Western wine and beer writing, and small trained panels with similar backgrounds. A model trained on that data describes flavour in words many drinkers do not use, weights the perceptions of a narrow group of tasters, and treats that group's thresholds as the truth."
  - q: "How do you stop an LLM inventing facts in a tasting note?"
    a: "Only let it write from the batch record. Retrieve the spec, the lab results and the approved panel descriptors for that batch, pass them in as the only permitted facts, and instruct the model to use nothing else. Then check the output: extract every factual claim in the draft and match it to a source field. Any claim without a source fails the note, and it goes back or to a person."
  - q: "Should AI-written tasting notes be disclosed?"
    a: "Yes, in plain words, wherever a reader could reasonably assume a person tasted the wine, beer or whisky and wrote the note. Say the note was drafted with AI from the production record and reviewed by a named role. It costs nothing, it keeps trust, and in some markets transparency rules for AI-generated content are moving in the same direction."
---

**Short answer: a sensory model learns whoever was in the room when the data was made. If the descriptor data came from Western lexicons and a panel of twelve similar tasters, the model will describe a Nashik Sauvignon Blanc as gooseberry to a drinker who would call it amla, and it will treat those twelve people's thresholds as the truth. Then a language model turns that into a tasting note, and adds a sherry cask, a single vineyard and a gold medal that nobody ever recorded. The fixes are dull and effective: audit who and what the training data represents, let the model write only from the batch record, and run an eval set that checks every claim in a note against a source field before anyone publishes it.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A grounded tasting-note pipeline. On the left, three sources: the batch spec, the lab results and the panel descriptors, each mapped through a local descriptor dictionary. They feed a retrieval step that builds a fact sheet. An LLM drafts the note from the fact sheet only. A claim checker extracts every claim in the draft and matches it to a source field. Claims with a source pass. Claims without a source, such as an invented sherry cask or an award, fail and send the note back. Passed notes go to a named reviewer and are published with a disclosure line.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">A TASTING NOTE THAT CAN ONLY SAY WHAT THE RECORD SAYS</text>
<g font-family="sans-serif">
<rect x="30" y="54" width="190" height="52" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="76" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Batch spec</text>
<text x="125" y="94" text-anchor="middle" font-size="10.5" fill="#4a6b64">variety &#183; cask &#183; ABV</text>
<rect x="30" y="118" width="190" height="52" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Lab results</text>
<text x="125" y="158" text-anchor="middle" font-size="10.5" fill="#4a6b64">RS &#183; TA &#183; IBU &#183; esters</text>
<rect x="30" y="182" width="190" height="52" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="204" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Panel descriptors</text>
<text x="125" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">approved, calibrated</text>
<rect x="30" y="250" width="190" height="42" rx="9" fill="#ffffff" stroke="#4db6a2" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="125" y="276" text-anchor="middle" font-size="10.5" fill="#00695c">local dictionary: cassis &#183; jamun</text>
<line x1="220" y1="144" x2="262" y2="144" stroke="#00695c" stroke-width="2"/>
<rect x="262" y="112" width="150" height="64" rx="9" fill="#06483f"/>
<text x="337" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Fact sheet</text>
<text x="337" y="158" text-anchor="middle" font-size="10.5" fill="#cfe6df">the only allowed facts</text>
<line x1="412" y1="144" x2="450" y2="144" stroke="#00695c" stroke-width="2"/>
<rect x="450" y="112" width="140" height="64" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="520" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">LLM drafts</text>
<text x="520" y="158" text-anchor="middle" font-size="10.5" fill="#4a6b64">from facts only</text>
<line x1="590" y1="144" x2="628" y2="144" stroke="#00695c" stroke-width="2"/>
<rect x="628" y="112" width="160" height="64" rx="9" fill="#06483f"/>
<text x="708" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Claim checker</text>
<text x="708" y="158" text-anchor="middle" font-size="10.5" fill="#cfe6df">every claim to a field</text>
<path d="M788 134 L830 96" stroke="#2e9e7c" stroke-width="2.5" fill="none"/>
<rect x="830" y="66" width="140" height="56" rx="9" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/>
<text x="900" y="90" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">all sourced</text>
<text x="900" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">to a named reviewer</text>
<path d="M788 156 L830 196" stroke="#ff4081" stroke-width="2.5" fill="none"/>
<rect x="830" y="176" width="140" height="56" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="1.5"/>
<text x="900" y="200" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">unsourced claim</text>
<text x="900" y="218" text-anchor="middle" font-size="10.5" fill="#4a6b64">sherry cask? medal?</text>
<path d="M830 222 C700 270 560 250 520 176" fill="none" stroke="#ff4081" stroke-width="2" stroke-dasharray="5 4"/>
<text x="640" y="262" text-anchor="middle" font-size="10" fill="#ff4081">back to draft, or to a person</text>
<rect x="30" y="316" width="940" height="44" rx="10" fill="#06483f"/>
<text x="500" y="343" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">PUBLISHED WITH A LINE: DRAFTED WITH AI FROM THE PRODUCTION RECORD &#183; REVIEWED BY THE CELLAR TEAM</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The model writes from a fact sheet, a checker traces every claim back to a field, and anything unsourced goes back. The reader is told how the note was made.</figcaption>
</figure>

I once watched a trained panel argue for ten minutes about whether a wheat beer smelled of clove or of "that thing my grandmother put in the pickle". Same compound, 4-vinyl guaiacol. Different kitchen. The panel lead wrote "clove" on the form because clove was on the flavour wheel. The grandmother's pickle never made it into the data.

Multiply that by a few hundred thousand tasting records and you have the training set for most sensory AI. This is part 5 of the series. [Part 1]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}) set out the principles, and this post is about two of them in the one place drinks businesses rarely look for them: fairness and inclusiveness in flavour models, and honesty in the notes a language model writes.

## Where the bias gets in

Sensory AI usually means one of three things. A model that predicts descriptors from chemistry, like the ones in [predicting beer flavour from malt COAs and flavour wheels]({{ '/2026/predicting-beer-flavour-malt-coa-flavour-wheels/' | relative_url }}). A model that scores or calibrates tasters. Or a language model that turns data into prose. Each one inherits bias from a different place.

**The lexicon.** The standard wheels and wine aroma vocabularies were built in Europe, the US and Australia. They are good tools. They also encode a produce aisle. Gooseberry, cassis, blackcurrant leaf, quince, greengage: these are precise words for someone who grew up with them and near-useless for many drinkers in India, who would reach for amla, jamun, kokum, raw mango or jaggery. A model trained only on the first list cannot produce the second, and a recommender built on it will describe your local wine to your local customer in a foreign language.

**The panel.** A trained panel is a small group, often a dozen people, often similar in age, background and diet. Their detection thresholds become the reference. If nobody on the panel is sensitive to a compound, the model learns that the compound does not matter. The [post on taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) covers how to measure each taster's reliability, and that same data tells you who is missing.

**The corpus.** Language models learned wine and whisky from published notes, reviews and marketing copy. That corpus is heavy on expensive bottles from famous regions, and it has a house style: generous, romantic, occasionally untethered from the glass. Ask a model to "write a tasting note" and it will write in that style, because that is what a tasting note looked like in its training data.

None of this is anyone being malicious. It is a sampling problem. Sampling problems are fixable, but only once someone writes them down.

## Auditing the descriptor data

Start with a count. Take your descriptor table, the one that feeds the flavour model or the note generator, and ask three questions of it.

1. **Who produced these labels?** Panel members, their training, their location. If every label came from one site's panel, say so in the model card.
2. **Which words are allowed?** List the controlled vocabulary. Count how many terms have a local equivalent your customers actually use. For most Indian wineries I have seen, that count starts near zero.
3. **Where does the model fail?** Split evaluation results by product origin and by customer segment. A model that is 85 percent accurate on Old World reds and 60 percent on Indian whites is not an 80 percent model. It is two models, and one of them is not ready.

The fix for the lexicon is a mapping table, not a new model. Keep the standard term as the key, because it anchors you to the chemistry and to published research, and add local equivalents per market. Cassis maps to jamun. Gooseberry maps to amla, with a note that the match is loose. The model predicts the standard descriptor; the display layer picks the word for the reader.

The fix for the panel is harder and slower: recruit wider, and record who tasted what so that you can at least measure the gap. You will not fix it this quarter. You can stop pretending it is not there.

## The hallucinated tasting note

Now the language model. Give a general-purpose LLM a product name and ask for a tasting note, and within three sentences it will usually tell you something that nobody recorded. "Aged in first-fill Oloroso casks." "From old vines on the estate's north slope." "Awarded gold at a major international competition." It sounds like every note it has ever read, which is the problem.

For a drinks business these are not harmless flourishes. A cask type is a production fact. A vineyard is a provenance claim, and in many markets a regulated one. An award is a claim someone can check. A whisky note that invents a sherry cask is a false statement about the product, and it is the business that published it, not the model, that answers for it. [Part 6]({{ '/2026/provenance-fakes-c2pa-traceability-whisky-wine/' | relative_url }}) goes further into label claims and provenance.

I wrote about [AI tasting notes]({{ '/2026/ai-tasting-notes-beer-wine-whiskey/' | relative_url }}) earlier this year as a drafting tool. That still stands. The responsible version has two extra parts: grounding and checking.

## Grounded drafting: the record is the only source

The pattern is retrieval-augmented generation with a hard boundary. For each batch, lot or cask release, build a fact sheet from the systems that already hold the truth:

- **The spec:** style or variety, blend components, cask types and fill numbers, vintage, ABV.
- **The lab:** residual sugar, TA and pH for wine; IBU, colour and attenuation for beer; ABV and key congeners for spirit.
- **The panel:** only the descriptors your calibrated panel approved for this batch, with their intensities.
- **The approved claims list:** awards, certifications, region names, only if they sit in a table someone signed off.

The model gets the fact sheet and an instruction that it may describe, order and phrase these facts, and may use no other factual claim. Style is its job. Facts are not. It is allowed to say "bright acidity" because TA is in the sheet. It is not allowed to say "old vines" unless vine age is in the sheet.

A prompt alone will not hold that line every time. So you check.

## The eval set: every claim to a field

This is the artefact. Build a small eval harness that runs on every draft before a person sees it, and a larger test suite that runs whenever you change the model, the prompt or the retrieval.

Each test case is a fact sheet plus the claims the note must not make. The checker uses a second, cheaper model call (or rules, for the easy cases) to extract claims from the draft, then matches each claim to a field in the fact sheet.

```python
# test case: one release, the facts, and the traps
CASE = {
  "id": "wine-2026-sb-lot14",
  "facts": {
    "variety": "Sauvignon Blanc", "vintage": 2026, "region": "Nashik",
    "oak": None,  # unoaked: a trap for the model
    "rs_g_l": 3.1, "ta_g_l": 7.4, "abv": 12.5,
    "descriptors": ["gooseberry", "green chilli", "lime zest"],
    "awards": []
  },
  "must_not_claim": ["oak", "barrel", "award", "medal", "old vines", "single vineyard"]
}

def check_note(note, case, extract_claims):
    """Fail the note if any claim lacks a source field or hits a trap."""
    claims = extract_claims(note)  # [{"text": "...", "field": "ta_g_l" | None}]
    unsourced = [c for c in claims if c["field"] is None]
    traps = [t for t in case["must_not_claim"] if t in note.lower()]
    return {"pass": not unsourced and not traps,
            "unsourced": unsourced, "traps": traps}

# the check itself must be checked: a known-bad note has to fail
bad = "Aged gently in French oak, this gold-medal Sauvignon Blanc..."
fake_extract = lambda n: [{"text": "aged in French oak", "field": None}]
assert not check_note(bad, CASE, fake_extract)["pass"]
```

Three things make this work in practice.

**Traps per product family.** Unoaked whites get an oak trap. NAS whisky gets an age trap. A beer with no dry hop gets a dry-hop trap. Write them once per family, not per batch.

**A golden set from real failures.** Every time a reviewer rejects a draft for an invented claim, the fact sheet and the bad draft go into the test suite. After a few months you have a suite shaped like your actual risk, not like a vendor's benchmark.

**Track the numbers.** Unsourced claims per hundred notes, trap hits, reviewer rejection rate. If the rejection rate falls to zero, check that someone is still reading.

The same check runs on the descriptor side. If the note says "jamun" and the fact sheet says "cassis", that is a pass only because the mapping table says so. The mapping table is itself a source.

## Disclosure

Say how the note was made. One plain line under it is enough: "Drafted with AI from our production and lab records, reviewed by the cellar team." Put a role there, not a vague "our experts".

This costs nothing and it matters. A tasting note carries an implied promise that someone tasted the product. If a model wrote it from data, the reader deserves to know, and the business is better off being the one to tell them. Transparency rules are moving the same way: the EU AI Act's Article 50 obligations on AI-generated content are coming in during 2026, and a disclosure habit now saves a scramble later. I would do it regardless.

## Where this breaks

**The mapping table becomes a stereotype.** Mapping cassis to jamun for every Indian reader is its own bias. Drinkers in Mumbai and Kolkata do not share one fruit bowl, and plenty of them say cassis. Let the reader choose, or test the vocabulary with real customers before you ship it.

**The claim extractor misses claims.** The checker is a model too. It will sometimes miss a soft claim like "a nod to the estate's heritage". Keep the rules-based trap list alongside it, and keep a person reviewing anything published.

**Grounding does not fix the panel.** A perfectly grounded note repeats the panel's descriptors faithfully. If the panel is narrow, the note is faithfully narrow. Grounding stops invention. It does not stop bias.

**The record is wrong.** If the spec says first-fill bourbon and the cask was a refill, the note will be confidently, verifiably wrong. The model sees the number. The cellar hand sees the stencil on the barrel end. The fix is in the record, and that is [part 6]({{ '/2026/provenance-fakes-c2pa-traceability-whisky-wine/' | relative_url }}).

**Style drift into claims.** "Rich, as if kissed by sherry" is style or claim depending on who reads it. Put simile-shaped claims about casks and regions in the trap list.

## The bottom line

Sensory AI is only as broad as the people and words it learned from, and most of it learned from a narrow room with a Western fruit bowl. Count who and what your data represents, map descriptors to the words your drinkers use, and split your evaluation by origin before you trust an average. When a language model writes the note, let it write only from the batch record, check every claim against a field, fail anything unsourced, and tell the reader how the note was made. The model is good at phrasing. The facts belong to the record, and the palate belongs to people.

Next: [provenance, fakes and synthetic labels]({{ '/2026/provenance-fakes-c2pa-traceability-whisky-wine/' | relative_url }}), where label claims come from a ledger instead of a prompt. For the wider sensory data picture, see [the AI brewery lab sensory QA system]({{ '/2026/ai-brewery-lab-sensory-qa-system/' | relative_url }}). The full list is on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**Why are sensory AI models biased?**
They learn from the data they are given, and most flavour descriptor data comes from Western lexicons, Western wine and beer writing, and small trained panels with similar backgrounds. A model trained on that data describes flavour in words many drinkers do not use, weights the perceptions of a narrow group of tasters, and treats that group's thresholds as the truth.

**How do you stop an LLM inventing facts in a tasting note?**
Only let it write from the batch record. Retrieve the spec, the lab results and the approved panel descriptors for that batch, pass them in as the only permitted facts, and instruct the model to use nothing else. Then check the output: extract every factual claim in the draft and match it to a source field. Any claim without a source fails the note, and it goes back or to a person.

**Should AI-written tasting notes be disclosed?**
Yes, in plain words, wherever a reader could reasonably assume a person tasted the wine, beer or whisky and wrote the note. Say the note was drafted with AI from the production record and reviewed by a named role. It costs nothing, it keeps trust, and in some markets transparency rules for AI-generated content are moving in the same direction.
