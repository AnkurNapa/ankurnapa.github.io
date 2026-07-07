---
layout: post
title: "AI for Hot Break, Cold Break, and Wort Clarity"
image: /assets/og/ai-wort-clarity-hot-cold-break.png
description: "Model how boil, whirlpool, and cooling conditions drive hot and cold break, wort clarity, colloidal stability, and fermentation health using turbidity data."
date: 2023-07-11
updated: 2023-07-11
tags: [brewing-science, wort, quality-control]
faq:
  - q: "What is the difference between hot break and cold break?"
    a: "Hot break is the protein-polyphenol coagulation that forms during the boil; cold break forms as the wort cools. Both produce trub. Good break at each stage improves wort and beer clarity and colloidal stability."
  - q: "How is break quality measured?"
    a: "Mainly by turbidity using nephelometry. It is a proxy rather than a direct count of coagulated protein, but tracked consistently it reflects how well your break is forming across the boil, whirlpool, and cooling stages."
  - q: "Is more trub removal always better?"
    a: "No. Trub carries lipids and material that affect fermentation, and the effect is double-edged — too little can stress yeast in some setups, too much carryover hurts clarity and stability. The right target depends on your process."
---

**Short answer: boil, whirlpool, and cooling conditions decide your hot and cold break, and a model linking those conditions to turbidity helps you protect clarity, colloidal stability, and fermentation health.** Break quality is the quiet determinant of how clean your finished beer looks and keeps.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI for Hot Break, Cold Break, and Wort Clarity</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Break quality is a chain, not a moment
Clarity is built across three stages. The hot break forms during the boil as proteins and polyphenols coagulate; the cold break forms as the wort cools after the whirlpool. Both throw down trub. Get good break at each stage and you improve wort and beer clarity, colloidal stability — how long the beer stays bright in the package — and even fermentation health, because trub carries lipids that influence yeast performance.

Each lever feeds the next. Boil vigour and time set the hot break, whirlpool geometry and rest separate the trub, and cooling rate governs the cold break. A weak link anywhere shows up as hazy wort, a slow whirlpool cone, or chill haze weeks later.

## What the model connects
The machine-learning piece links process conditions to break quality and downstream clarity. Inputs are the variables you already touch — boil vigour and time, whirlpool rest, cooling rate — plus turbidity readings at the hot and cold sides. Turbidity, measured by nephelometry, is the workhorse signal here. The model learns which combinations of conditions produce clean break and which leave proteins and polyphenols carried forward to haunt colloidal stability.

That demands measure-first discipline. Without consistent nephelometric readings at consistent sample points, there is nothing to learn from. The data-science task is to standardise where and when you measure turbidity, then pair each reading with the process settings and a downstream clarity or stability outcome.

## Reading the trend and writing the note
The generative-AI angle is a tool that reads turbidity trends and drafts the QC note for you. Point a vision or LLM-based assistant at the nephelometer trend across boil, whirlpool, and cooling, and it summarises: "Cold break turbidity ran high on batches 142-144 after the chiller flow changed; expect reduced colloidal stability — recommend checking cooling rate and whirlpool rest." It turns a wiggly chart into a plain-language clarity QC note that goes straight into the batch record, so the pattern is captured while it is fresh rather than rediscovered at packaging. This pairs naturally with broader [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Where it breaks
Two honest limits. First, the trub effect on fermentation is double-edged: trub carries lipids that yeast can use, so aggressive clarification is not automatically good — the right trub target varies by yeast and process, and a model that optimises clarity alone may quietly hurt fermentation. Second, turbidity is a proxy. Nephelometry tells you light is being scattered, not exactly what is scattering it; chill haze, yeast in suspension, and protein-polyphenol trub all read as turbidity. So the model infers break quality indirectly, and a reading can mislead if you change yeast or process without recalibrating expectations. Keep a human checking that the proxy still tracks reality.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI for Hot Break, Cold Break, and Wort Clarity</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Hot break, cold break, and clarity form a connected chain you can instrument with turbidity and model end to end. Standardise your nephelometry, link conditions to outcomes, and let a generative assistant turn the trends into QC notes nobody otherwise has time to write. Just respect the two caveats — trub helps fermentation as well as hurting clarity, and turbidity is a proxy, not the truth.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Frequently asked questions

**What is the difference between hot break and cold break?**
Hot break is the protein-polyphenol coagulation that forms during the boil; cold break forms as the wort cools. Both produce trub. Good break at each stage improves wort and beer clarity and colloidal stability.

**How is break quality measured?**
Mainly by turbidity using nephelometry. It is a proxy rather than a direct count of coagulated protein, but tracked consistently it reflects how well your break is forming across the boil, whirlpool, and cooling stages.

**Is more trub removal always better?**
No. Trub carries lipids and material that affect fermentation, and the effect is double-edged — too little can stress yeast in some setups, too much carryover hurts clarity and stability. The right target depends on your process.
