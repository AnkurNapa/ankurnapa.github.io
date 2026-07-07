---
layout: post
title: "AI-Optimised Mash Temperature Profiles"
image: /assets/og/ai-mash-temperature-profile-optimization.png
description: "How AI optimises saccharification rest temperatures and times to hit a target fermentability and body consistently across varying malt lots."
date: 2023-05-25
updated: 2023-05-25
tags: [brewing-science, brewhouse, process-optimization]
faq:
  - q: "How does mash temperature change the beer?"
    a: "Lower saccharification rests around 62–65 °C favour beta-amylase, giving more fermentable maltose and a drier beer. Higher rests around 68–72 °C favour alpha-amylase, leaving more dextrins and fuller body."
  - q: "Can AI keep fermentability consistent across malt lots?"
    a: "It can recommend rest adjustments to hold a target fermentability as malt enzyme potential varies, but only within what the malt allows. A low-diastatic-power lot has a hard limit no schedule can beat."
  - q: "Does the model assume my mash temperature is accurate?"
    a: "Yes. It assumes the rest temperature you ask for is the temperature the whole mash reaches. Uneven mixing or a miscalibrated probe will undermine any optimised schedule."
---

**Short answer: AI can tune your saccharification rest temperatures and times to hit a target fermentability consistently across varying malt lots — but only within the enzyme potential the malt actually carries, and only if your mash temperatures are accurate and even.** It standardises the lever you already control; it cannot create enzyme that is not there.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI-Optimised Mash Temperature Profiles</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Temperature is the fermentability dial
The mash is where you decide how fermentable your wort will be, and temperature is the dial. Starch is broken down by two enzymes with different temperature preferences. Beta-amylase, which produces fermentable maltose, works best at lower saccharification rests around 62–65 °C — favour it and you get a more fermentable wort and a drier, more attenuated beer. Alpha-amylase, which produces dextrins, dominates at higher rests around 68–72 °C — favour it and you leave more unfermentable dextrins and a fuller body. Mash pH around 5.2–5.4 keeps both working properly.

The brewer's real goal is usually not a single temperature but an outcome: a target attenuation and mouthfeel that the recipe is supposed to hit every time. The problem is that malt varies. Two lots of the same malt can carry different enzyme potential and modification, so a fixed mash schedule that nailed the target last month can drift this month. That is the gap an optimisation model is built to close.

## Optimising rests against a target
Framed properly, this is an optimisation: choose the rest temperatures and durations that get closest to a target fermentability, given the malt in front of you. The model's inputs are the malt analysis — diastatic power, modification, protein — and the achievable mash profile; its objective is the fermentability and body you have specified. As enzyme potential shifts from lot to lot, it nudges the schedule: a touch lower or longer on the beta-amylase rest when you need more fermentability, a higher rest when you want to protect body.

The data-science work is, again, measure first. You need the malt figures and a record of what mash schedules actually produced what fermentability on your kit. With that history, the model learns your brewhouse's real response rather than a textbook curve, and it can hold a target steady across lots that would otherwise pull your attenuation around. Without it, you are optimising against assumptions.

## Where it breaks
The fundamental limit is that the malt sets the ceiling. Enzyme potential is fixed by the time the grain reaches your mill; if a lot is low in diastatic power, no schedule will conjure the fermentability you wanted, and the honest answer is to adjust the grist or expectations, not the rest. An optimiser that promises a target a low-enzyme malt cannot reach is misleading you.

The second limit is the assumption underneath the maths: that the temperature you ask for is the temperature the whole mash reaches. Uneven mixing, dough-ball formation, a slow ramp or a miscalibrated probe all mean the real mash sits somewhere other than the setpoint, and the optimised schedule quietly fails. Get your mash temperatures accurate and even before trusting any model — and validate predicted fermentability against your [wort fermentability]({{ '/2023/predicting-wort-fermentability/' | relative_url }}) measurements rather than assuming the schedule worked.

## Designing a schedule by description
The generative-AI angle is a design assistant: tell it the outcome and it drafts the schedule. A brewer types "design a mash schedule for high attenuation and a light body using this malt lot" and the system proposes rest temperatures and times — for example a longer rest near 63 °C to push beta-amylase — with a note on what the malt's diastatic power allows. It generates the candidate, explains the reasoning in plain language, and the brewer adjusts and approves. For recipe development across many target profiles, that turns a slow trial-and-error loop into a fast, documented one.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI-Optimised Mash Temperature Profiles</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Optimising mash temperature profiles is one of the cleaner wins for AI in the brewhouse because the science is well understood and the lever is squarely under your control. Use it to hold fermentability and body steady as malt varies, respect the hard ceiling that enzyme potential sets, and make sure your mash actually reaches the temperatures you command. Within those limits, it makes a recipe repeatable rather than lucky.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting wort fermentability]({{ '/2023/predicting-wort-fermentability/' | relative_url }}).

## Frequently asked questions

**How does mash temperature change the beer?**
Lower saccharification rests around 62–65 °C favour beta-amylase, giving more fermentable maltose and a drier beer. Higher rests around 68–72 °C favour alpha-amylase, leaving more dextrins and fuller body.

**Can AI keep fermentability consistent across malt lots?**
It can recommend rest adjustments to hold a target fermentability as malt enzyme potential varies, but only within what the malt allows. A low-diastatic-power lot has a hard limit no schedule can beat.

**Does the model assume my mash temperature is accurate?**
Yes. It assumes the rest temperature you ask for is the temperature the whole mash reaches. Uneven mixing or a miscalibrated probe will undermine any optimised schedule.
