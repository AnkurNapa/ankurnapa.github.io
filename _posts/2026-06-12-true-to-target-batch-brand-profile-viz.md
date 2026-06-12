---
layout: post
title: "True-to-Target: Visualizing Whether a Batch Matches Its Brand Profile"
image: /assets/og/true-to-target-batch-brand-profile-viz.png
description: "True-to-target (TTT) tasting asks a different question than 'is it in spec' — does this batch still taste like the brand? How to visualize brand conformance with radar profiles, target bands and deviation tracking, so a panel's verdict becomes a picture the whole brewery reads."
date: 2026-06-12 11:40:00 -0700
updated: 2026-06-12
tags: [brewing-science, brewing-data-viz, sensory-analysis, quality-control, data-visualization]
faq:
  - q: "What is a true-to-target (or true-to-type) tasting?"
    a: "True-to-target tasting is a brand-conformance sensory assessment: a trained panel judges whether a production batch still matches the established target profile for that brand, attribute by attribute. Unlike a difference test, the comparison is against the brand's defined profile, not another sample — the question is 'is this still our beer', and a pass/fail or a deviation score is the output."
  - q: "How do you visualize brand conformance in brewing?"
    a: "A radar (spider) chart overlays the batch's attribute intensities on the brand's target band, so conformance reads as a shape that fits inside the band or pokes outside it. Pair it with a deviation chart (batch attribute minus target) and a batch-over-time conformance trend, so you see both where this batch deviates and whether the brand is drifting across batches."
  - q: "Is true-to-target the same as a triangle test?"
    a: "No. A triangle (difference) test asks whether two samples are detectably different. True-to-target asks whether one batch matches the brand's established profile. They answer different questions and use different visuals — difference tests visualize correct-identification counts and significance, while true-to-target visualizes a profile against a target band."
---

**Short answer: true-to-target (TTT) tasting asks "does this batch still taste like our brand?" — a conformance question, not an in-spec or a difference question. Its natural visualization is a radar/profile chart with the brand's target band drawn in, so a batch reads at a glance as a shape that fits the band or pokes outside it. Add a deviation chart (batch minus target, attribute by attribute) and a conformance-over-time trend, and a panel's verdict stops being a number in a logbook and becomes a picture the brewer, the panel and the brand owner all read the same way.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="True-to-target visualization: a radar chart of a batch profile inside a brand target band, a deviation bar chart of batch minus target per attribute, and a conformance-over-time trend across batches."><rect width="1000" height="340" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">TRUE-TO-TARGET — THREE VIEWS OF ONE VERDICT</text><g font-family="sans-serif"><text x="180" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#1c1a17">1 &#183; Profile vs target band</text><polygon points="180,90 246,128 232,206 128,206 114,128" fill="none" stroke="#cbb89a" stroke-width="14" stroke-linejoin="round" opacity="0.55"/><polygon points="180,98 238,131 226,198 134,198 122,131" fill="none" stroke="#8a5a2b" stroke-width="1" stroke-dasharray="3 3"/><polygon points="180,108 232,134 214,196 150,190 130,140" fill="#b45309" fill-opacity="0.3" stroke="#b45309" stroke-width="1.6"/><text x="180" y="232" text-anchor="middle" font-size="9.5" fill="#6b6258">batch shape inside the band = conforms</text><text x="60" y="120" font-size="8.5" fill="#6b6258">malt</text><text x="248" y="120" font-size="8.5" fill="#6b6258">hop</text><text x="232" y="216" font-size="8.5" fill="#6b6258">bitter</text><text x="108" y="216" font-size="8.5" fill="#6b6258">ester</text><text x="86" y="135" font-size="8.5" fill="#6b6258">body</text><text x="500" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#1c1a17">2 &#183; Deviation from target</text><line x1="400" y1="150" x2="600" y2="150" stroke="#6b6258"/><g><rect x="415" y="120" width="22" height="30" fill="#b45309"/><rect x="447" y="150" width="22" height="14" fill="#7a1f3d"/><rect x="479" y="138" width="22" height="12" fill="#b45309"/><rect x="511" y="150" width="22" height="26" fill="#7a1f3d"/><rect x="543" y="132" width="22" height="18" fill="#b45309"/></g><text x="500" y="200" text-anchor="middle" font-size="9.5" fill="#6b6258">above / below target, attribute by attribute</text><text x="820" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#1c1a17">3 &#183; Conformance over batches</text><rect x="712" y="86" width="216" height="120" rx="6" fill="#f7ece0" stroke="#cbb89a"/><line x1="712" y1="120" x2="928" y2="120" stroke="#2f6b3a" stroke-dasharray="4 3"/><text x="934" y="123" font-size="8" fill="#2f6b3a"></text><polyline points="722,150 752,142 782,148 812,138 842,176 872,150 902,144" fill="none" stroke="#b45309" stroke-width="2"/><circle cx="842" cy="176" r="4" fill="#7a1f3d"/><text x="820" y="226" text-anchor="middle" font-size="9.5" fill="#6b6258">one batch fell out of band — caught</text></g><text x="500" y="262" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b45309">"Is it in spec?" and "Is it still our beer?" are different questions.</text><text x="500" y="286" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">a batch can pass every numeric spec and still drift off-brand — the profile shape is what reveals it</text><text x="500" y="312" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#6b6258">target band = the agreed brand profile, set once from reference batches the brand owner signs off</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The same panel verdict, three ways: profile shape, per-attribute deviation, and conformance trend across batches.</figcaption>
</figure>

This is the flagship of the [brewing data-visualization series]({{ '/2026/brewing-viz-beyond-control-chart/' | relative_url }}). True-to-target tasting is something most breweries *do* — a panel checks the beer is "right" — but rarely *visualize* well, so the verdict lives as a tick in a logbook and its signal is lost. Here's how to turn it into a picture.

## A different question from "in spec"

Your analytical specs check parameters one at a time: ABV in range, IBU in range, colour in range, diacetyl below threshold. A batch can pass *every one* of those and still not taste like your flagship — because brand character lives in the *combination and balance* of attributes, not in any single number staying between two limits. True-to-target tasting (also called true-to-type or true-to-brand) asks the combined question directly: a trained panel rates the batch on the brand's defined attributes — malt, hop aroma, bitterness, ester, body, finish — and the verdict is whether the *whole profile* matches the target. It is a conformance question, and it is distinct from a [difference test]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}), which asks only whether two samples differ at all.

## The target band is the foundation

Before any visualization, the brand needs a **defined target profile with a tolerance band** — the agreed intensity for each attribute, plus how far a batch may deviate and still be "on brand." This is set once from reference batches the brand owner signs off, and it's the unglamorous prerequisite the whole method rests on; without an agreed target, "true-to-target" has no target, and the chart is just one batch's opinion. This is the sensory equivalent of the [data foundation that every analysis needs]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}).

## Three views of one verdict

With a target band defined, the panel's scores become three complementary pictures:

**1 — The radar/profile chart.** Plot the brand's attributes as spokes, draw the target band as a ring, and overlay the batch. Conformance becomes a *shape*: a batch whose profile sits inside the band is true-to-target; one that pokes outside on "hop aroma" and caves in on "body" shows you *how* it's off, not just that it is. The radar is powerful here precisely because brand character is a shape, and humans read shapes instantly.

**2 — The deviation chart.** A simple bar chart of *batch minus target* per attribute, centred on zero. It's the radar's information in a form that's easier to rank and track — which attribute deviated most, and in which direction. Where the radar shows the gestalt, the deviation bars show the priorities.

**3 — The conformance-over-time trend.** One point per batch — an overall conformance score, or the count of attributes outside band — plotted across batches. This is where the method earns its keep beyond a single QC pass: it catches *brand drift*, the slow collective creep where each batch passes but the brand quietly moves over a year. That's a [slow-drift problem]({{ '/2026/spc-capability-cusum-ewma-brewing/' | relative_url }}), and the next post's CUSUM thinking applies directly to it.

## Making the panel's work visible

The quiet payoff is organisational. A logbook tick says "panel approved batch 412." A radar inside its band, a deviation chart, and a conformance trend say *why*, *how confidently*, and *whether we're drifting* — in a picture the brewer, the panel lead and the brand owner all read identically. It turns sensory from a gate people argue about into evidence people act on, the same shift that makes any [tasting-panel data]({{ '/2024/digitising-beer-tasting-panels-ai-power-bi/' | relative_url }}) worth digitising.

## Where this breaks

The honest section. **The radar chart has real flaws** — the enclosed *area* changes with attribute order and axis scaling, so it can exaggerate or hide deviations; keep the attribute order and scales fixed forever, and read it alongside the deviation bars rather than trusting the shape alone. **It's only as honest as the panel** — true-to-target rests on a calibrated, aligned panel; an [un-calibrated panel]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) produces a confident radar built on noise, and averaging disagreeing tasters hides the disagreement. **The target itself can drift or be wrong** — brands evolve, reference batches age, and a target set years ago may no longer reflect the beer you actually sell; revisit it deliberately rather than treating it as permanent. And **conformance is not quality** — a batch can be perfectly true-to-target and still be a beer with a dull target; this method guards consistency, not excellence, and the two are different conversations.

## The bottom line

True-to-target tasting answers "is this still our brand?" — a conformance question that numeric specs miss because brand character is a balance, not a set of independent limits. Visualize it three ways: a radar profile against the target band for the gestalt, a deviation chart for the priorities, and a conformance trend for brand drift across batches. Define the target band first, keep a calibrated panel, fix your axes, and read the radar with its caveats — and a panel's verdict becomes a picture the whole brewery trusts. Next, the SPC that makes the drift trend rigorous: [capability, CUSUM and EWMA]({{ '/2026/spc-capability-cusum-ewma-brewing/' | relative_url }}).

## Frequently asked questions

**What is a true-to-target (or true-to-type) tasting?**
True-to-target tasting is a brand-conformance sensory assessment: a trained panel judges whether a production batch still matches the established target profile for that brand, attribute by attribute. Unlike a difference test, the comparison is against the brand's defined profile, not another sample — the question is "is this still our beer", and a pass/fail or a deviation score is the output.

**How do you visualize brand conformance in brewing?**
A radar (spider) chart overlays the batch's attribute intensities on the brand's target band, so conformance reads as a shape that fits inside the band or pokes outside it. Pair it with a deviation chart (batch attribute minus target) and a batch-over-time conformance trend, so you see both where this batch deviates and whether the brand is drifting across batches.

**Is true-to-target the same as a triangle test?**
No. A triangle (difference) test asks whether two samples are detectably different. True-to-target asks whether one batch matches the brand's established profile. They answer different questions and use different visuals — difference tests visualize correct-identification counts and significance, while true-to-target visualizes a profile against a target band.
