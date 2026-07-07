---
layout: post
title: "Ten Prompts from the Brewery Floor: Bad Ask → Good Ask"
image: /assets/og/brewery-floor-prompts-bad-to-good.png
description: "Ten real brewery situations — stuck fermentation, recipe scaling, costing, off-flavours — each shown as the vague prompt beginners type and the specific rewrite that actually gets a useful AI answer."
date: 2026-06-06
updated: 2026-06-06
tags: [brewing-science, asking-better-questions, generative-ai, ai-tools, process-optimization]
faq:
  - q: "What is the difference between a bad and a good brewing prompt?"
    a: "A bad prompt describes a feeling ('my beer tastes off'); a good one describes a situation: style, stage, measured numbers, timeline, and the decision you need to make. The rewrite is almost always the same move — add the numbers, name the stage, ask one question."
  - q: "Should I share my recipe and batch data with an AI assistant?"
    a: "Process data (gravities, temperatures, times) is what makes answers useful, so share it for the batch in question. Be more careful with commercially sensitive material — full proprietary recipes, supplier pricing, customer names — especially in consumer tools."
  - q: "Which brewing tasks does AI prompt-rewriting help most?"
    a: "Diagnosis (off-flavours, stuck fermentations), planning (recipe scaling, water adjustment, brew-day scheduling) and explanation (reading a COA, explaining a lab result, drafting an SOP). Anything where the answer depends on tasting or measuring still ends at the bench."
---

**Short answer: nearly every weak brewing prompt fails the same way — it describes a feeling instead of a situation. The fix is mechanical and learnable: add the measured numbers, name the process stage, state the timeline, and end with one specific decision you need to make. Below are ten real situations, each as the vague ask a new brewer actually types and the rewrite that earns a useful answer.** Steal the pattern, not the prompts.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The five-part rewrite that turns a vague brewing prompt into a useful one: style plus stage plus numbers plus timeline plus one decision."><rect width="1000" height="270" fill="#ffffff"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE REWRITE FORMULA</text><rect x="120" y="50" width="760" height="46" rx="10" fill="#f0f6f5" stroke="#4a6b64" stroke-width="1.3"/><text x="500" y="79" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#4a6b64">"Why does my beer taste bad?"&#160;&#160;&#8212; a feeling, not a situation</text><g stroke="#00695c" stroke-width="2" fill="#00695c"><line x1="500" y1="96" x2="500" y2="126"/><polygon points="495,126 500,135 505,126" stroke="none"/></g><g font-family="sans-serif"><rect x="30" y="140" width="172" height="76" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.6"/><text x="116" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#06483f">STYLE</text><text x="116" y="196" text-anchor="middle" font-size="10.5" fill="#4a6b64">American wheat, 20L</text><rect x="222" y="140" width="172" height="76" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.6"/><text x="308" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#06483f">STAGE</text><text x="308" y="196" text-anchor="middle" font-size="10.5" fill="#4a6b64">bottled 3 weeks ago</text><rect x="414" y="140" width="172" height="76" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.6"/><text x="500" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#06483f">NUMBERS</text><text x="500" y="196" text-anchor="middle" font-size="10.5" fill="#4a6b64">OG 1.048 &#183; FG 1.010 &#183; 19&#176;C</text><rect x="606" y="140" width="172" height="76" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.6"/><text x="692" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#06483f">TIMELINE</text><text x="692" y="196" text-anchor="middle" font-size="10.5" fill="#4a6b64">fades as the glass warms</text><rect x="798" y="140" width="172" height="76" rx="9" fill="#06483f"/><text x="884" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">ONE DECISION</text><text x="884" y="196" text-anchor="middle" font-size="10.5" fill="#f0f6f5">what do I change next batch?</text></g><text x="500" y="248" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#00695c">style + stage + numbers + timeline + one decision &#8212; every rewrite in this post is this move</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Every bad ask in this post is fixed by the same five-part move — write it on a sticky note above the keyboard.</figcaption>
</figure>

## Diagnosis: from symptom to situation

**1. The off-flavour.**
*Bad:* "Why does my beer taste bad?"
*Good:* "My 20L American wheat (OG 1.048, FG 1.010, US-05 at 19°C, bottled 3 weeks ago) has a green-apple note that fades as the glass warms. Acetaldehyde? What in my process — fermentation length, yeast health, packaging — most likely caused it, and what do I change next batch?"
The rewrite names a candidate, but stays open — and the model can now reason over an actual timeline.

**2. The stuck fermentation.**
*Bad:* "My fermentation stopped, help."
*Good:* "Day 9, gravity stuck at 1.024 from OG 1.062 (expected FG ~1.014). English ale strain, pitched one sachet without rehydration at 23°C, now at 17°C ambient. Rank the likely causes and give me a check order from cheapest to most invasive."
"Rank" and "check order" force triage instead of an essay.

**3. The inconsistent batch.**
*Bad:* "Why is this batch different?"
*Good:* "Same pale ale recipe, batches 14 and 15. Batch 15 came in at 68% efficiency vs our usual 75%, same grain bill, new malt lot. Here are both COAs. What in the malt spec could explain the gap, and what should I adjust — crush, mash temp or grain weight?"
Pointing the model at two certificates of analysis is exactly the document-reading work it's good at.

## Planning: from wish to brief

**4. Recipe scaling.**
*Bad:* "Scale my recipe to 200L."
*Good:* "Scaling this 20L recipe to 200L on a system with 72% efficiency (vs 80% on my kit) and a 90-minute whirlpool instead of 20. Walk through what does NOT scale linearly — hop utilisation, evaporation, trub loss — and flag where the aroma will drift."
The good ask knows scaling isn't multiplication and says so.

**5. Water adjustment.**
*Bad:* "What water profile for an IPA?"
*Good:* "My water report: Ca 35, Mg 8, Na 12, SO₄ 40, Cl 25, HCO₃ 120 (mg/L). Target: a soft-bitter West Coast IPA, mash pH 5.3 at this grist. What salt additions per 25L, and what does the bicarbonate force me to deal with first?"
Without the report, every answer is someone else's water.

**6. The brew-day plan.**
*Bad:* "Make me a brew day checklist."
*Good:* "Single-vessel BIAB, 25L batch, solo brewer, 5-hour window. Build me a brew-day timeline with the two points where a mistake is hardest to recover (my guess: strike temperature and chill/pitch), and what I'd pre-stage to protect them."
Asking the model to identify *irreversible* moments is a genuinely good use of its breadth.

## Numbers and paperwork: the quiet wins

**7. Costing.**
*Bad:* "Is my beer profitable?"
*Good:* "Here's my ingredient cost per 20L batch (table pasted), packaging at ₹38/can, and I sell at ₹180. Build the per-can cost including a 12% loss allowance, and show which single input moves margin most."
A sensitivity ask ("which input moves margin most") turns arithmetic into insight.

**8. Reading a lab result or COA.**
*Bad:* "What does this report mean?"
*Good:* "This is the COA for my new hop lot (photo attached). Compare it to the variety's typical alpha and oil ranges, tell me what's unusual, and how the 2% lower alpha changes my 60-minute addition for 35 IBU."
Vision plus a concrete recalculation — the same pattern as the [Claude IPA hop workflow]({{ '/2026/claude-opus-ipa-hop-workflow/' | relative_url }}).

**9. The SOP.**
*Bad:* "Write a cleaning SOP."
*Good:* "Draft a CIP SOP for a 500L unitank: caustic at 2% and 80°C isn't possible on my rig — I'm limited to 60°C. Adjust concentrations/contact times accordingly, and flag every step where my constraint weakens the clean so I can compensate."
Telling the model your *constraint* is what separates a usable SOP from a template.

**10. Learning itself.**
*Bad:* "Teach me brewing science."
*Good:* "Here are the last five questions I couldn't answer about my own batches (list). Build me a four-week study plan that covers exactly these, with one trusted source each, ordered so each topic builds on the last."
This is the loop from [asking AI what to ask]({{ '/2026/ask-ai-what-to-ask-brewing/' | relative_url }}) closing on itself: your question backlog becomes your syllabus.

## Where this breaks

The rewrites share a dependency: **numbers you actually recorded.** No gravity log, no prompt #2 — which is why the [map of your own data]({{ '/2026/brewery-data-map-what-it-answers/' | relative_url }}) precedes this post. Second, a well-formed prompt **does not guarantee a correct answer** — the model can still misstate a hop spec or a salt addition with total confidence, so anything that changes the beer gets checked against a calculator, a COA or a trusted text before brew day. And third, prompts 1, 2 and 8 end at the bench: AI narrates hypotheses; the hydrometer, the pH meter and your palate decide.

## The bottom line

Every rewrite above is the same five-part move: **style + stage + numbers + timeline + one decision.** Write it on a sticky note above the keyboard. A new brewer who internalises that pattern gets more from a free chatbot than a careless brewer gets from an enterprise AI platform — because in brewing, as in data science, the quality of the answer was always set by the quality of the question.

## Frequently asked questions

**What is the difference between a bad and a good brewing prompt?**
A bad prompt describes a feeling ("my beer tastes off"); a good one describes a situation: style, stage, measured numbers, timeline, and the decision you need to make. The rewrite is almost always the same move — add the numbers, name the stage, ask one question.

**Should I share my recipe and batch data with an AI assistant?**
Process data (gravities, temperatures, times) is what makes answers useful, so share it for the batch in question. Be more careful with commercially sensitive material — full proprietary recipes, supplier pricing, customer names — especially in consumer tools.

**Which brewing tasks does AI prompt-rewriting help most?**
Diagnosis (off-flavours, stuck fermentations), planning (recipe scaling, water adjustment, brew-day scheduling) and explanation (reading a COA, explaining a lab result, drafting an SOP). Anything where the answer depends on tasting or measuring still ends at the bench.

*Part of the [Brewing Science]({{ '/tracks/brewing-science/' | relative_url }}) track.*
