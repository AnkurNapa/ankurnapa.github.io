---
layout: post
title: "Quality-Control Charts for Brewing in Tableau"
image: /assets/og/tableau-qc-control-charts-brewing.png
description: "Build statistical process control charts for brewing QC in Tableau using reference bands, control limits and Explain Data for out-of-control points."
date: 2023-01-21
updated: 2023-01-21
tags: [brewing-science, tableau, quality-control]
faq:
  - q: "How do I draw control limits on a Tableau chart?"
    a: "Calculate the process mean and standard deviation as fixed values from a stable baseline period, then add reference lines or a reference band at the mean plus and minus three standard deviations. Tableau does not generate control limits for you; you supply them as calculated fields or constants."
  - q: "Which brewing parameters suit an SPC chart?"
    a: "Any measurable, repeated parameter with a stable target: original and final gravity, pH, diacetyl, dissolved oxygen and package fill levels are all good candidates. The parameter needs enough consistent history to set meaningful limits."
  - q: "Does an out-of-control point mean something is broken?"
    a: "It means the value is statistically unusual relative to your baseline, which warrants investigation. It is a signal, not a verdict — correlation with a cause still has to be established by people who know the process."
---

**Short answer: a control chart in Tableau is a time-series with honest limits bolted on.** The chart is easy; the discipline is defining limits from a genuinely stable baseline and resisting the urge to react to ordinary noise.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for Quality-Control Charts for Brewing in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Quality-Control Charts for Brewing in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## The data model behind a control chart
Statistical process control (SPC) catches when a process drifts beyond its normal variation. In a brewery that means tracking parameters such as gravity, pH, diacetyl or fill volume sample by sample and asking: is this point part of normal variation, or a signal?

Before any charting, decide the grain. One row per measurement, tagged with the parameter, the batch or fill, the timestamp and ideally the sampling point. With that tidy, your "measure first" calculated fields are simple: the process mean and the standard deviation, computed from a chosen baseline window — not from all data, and certainly not recomputed live as new points arrive, because then today's drift quietly widens its own limits.

This is the same QC mindset that underpins more advanced work; for the AI extension of it, see [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Building the chart in Tableau
Plot your parameter on a continuous time axis. Then add the limits. The cleanest approach is calculated fields holding the baseline mean and the upper and lower control limits at mean ± three standard deviations, surfaced as **reference lines** with a shaded **reference band** between them. A second band at ± two standard deviations gives you warning zones if you want Western Electric-style rules.

Use a calculated field to flag any point outside the limits, and a colour encoding to make those points jump out in red. A parameter lets the user switch between QC variables — gravity today, diacetyl tomorrow — reusing the same sheet. Filter and highlight actions let an analyst click an out-of-control point and drill into the batch behind it.

On the AI layer, Tableau's **Explain Data** (now part of the Einstein Copilot family) is genuinely handy here: select a suspicious mark and it surfaces statistical explanations — which underlying fields most contribute to that value standing out. It is a fast way to generate hypotheses, and a generative-AI summary can turn that into a readable note for the shift handover. Treat both as a starting point for investigation, never the conclusion.

## Where it breaks
Control charts assume a stable, well-characterised baseline. If you set limits during a chaotic commissioning period, or across a recipe change, the limits are meaningless and the chart will either cry wolf constantly or stay silent through real problems. Recompute limits only when the process genuinely changes, and document when you did.

The second trap is mistaking correlation for cause. Explain Data will happily tell you that a field is "associated" with an outlier; that is not the same as that field causing it. A high diacetyl reading correlated with a particular tank might be the tank, or the yeast generation, or the sampling method — Tableau cannot tell you which. And critically, SPC tells you *that* something changed, not *whether the beer is good*. That still needs the lab and the panel.

Finally, an out-of-control point is a prompt to look, not a fault report. Overreacting to every signal — "tampering" — adds variation rather than removing it.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Quality-Control Charts for Brewing in Tableau</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
A Tableau control chart is one of the highest-value, lowest-effort dashboards a brewery can build: a clean time-series, baseline-derived limits as reference bands, and a flag for points that breach them. Explain Data accelerates the hunt for why, but the baseline discipline and the human judgement are what make it trustworthy.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Frequently asked questions

**How do I draw control limits on a Tableau chart?**
Calculate the process mean and standard deviation as fixed values from a stable baseline period, then add reference lines or a reference band at the mean plus and minus three standard deviations. Tableau does not generate control limits for you; you supply them as calculated fields or constants.

**Which brewing parameters suit an SPC chart?**
Any measurable, repeated parameter with a stable target: original and final gravity, pH, diacetyl, dissolved oxygen and package fill levels are all good candidates. The parameter needs enough consistent history to set meaningful limits.

**Does an out-of-control point mean something is broken?**
It means the value is statistically unusual relative to your baseline, which warrants investigation. It is a signal, not a verdict — correlation with a cause still has to be established by people who know the process.
