---
layout: post
title: "Quality-Control Charts for Brewing in Tableau"
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
