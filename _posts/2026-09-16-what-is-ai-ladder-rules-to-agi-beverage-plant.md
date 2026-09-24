---
layout: post
title: "What Is AI, Really? The Ladder From Rules to AGI, Told on a Beverage Plant Floor"
image: /assets/og/what-is-ai-ladder-rules-to-agi-beverage-plant.png
description: "Part 1 of AI for Operational Excellence in Beverage Plants. Rules, machine learning, deep learning, generative AI, agentic AI and AGI, one rung at a time, each with a real example from a brewery, winery, distillery or packaging line. Honest about AGI: it does not exist yet, and Monday's shift does not need it."
date: 2026-09-16 09:00:00 -0700
updated: 2026-09-16
tags: [brewing-science, ai-opex, ai-basics, generative-ai, operational-excellence]
faq:
  - q: "What is the difference between AI, machine learning and generative AI?"
    a: "AI is the umbrella for any software that does a task we would call intelligent. Machine learning is the part of AI that learns patterns from data instead of following rules someone wrote. Generative AI is a kind of machine learning that produces new content, such as text or images, rather than a prediction or a label. Each is a rung on the same ladder, not a separate technology."
  - q: "Does AGI exist in 2026?"
    a: "No. AGI, artificial general intelligence, means a system that can learn and perform any intellectual task a person can, across domains, reliably. Today's large language models are impressive and broad, but they still make basic errors, cannot be trusted without checks, and do not learn on the job the way a person does. For a beverage plant, AGI is a debate to follow, not a tool to plan around."
  - q: "Which kind of AI should a brewery or bottling plant start with?"
    a: "Usually the lowest rung that solves the problem. Many plant problems are solved by better rules and statistical process control. Machine learning helps where patterns are too complex for rules, such as predicting a pump failure. Generative AI helps with text: SOPs, handovers and root-cause notes. Agentic AI comes last, once the data and the approvals are in place."
---

**Short answer: "AI" is not one thing. It is a ladder. The bottom rung is plain rules, the kind already running in your PLC. Above that sits machine learning, which learns patterns from data, then deep learning, which learns from images, sound and long sensor streams. Generative AI produces text and images. Agentic AI uses tools and takes steps towards a goal. At the top is AGI, a general intelligence that can do anything a person can, and it does not exist yet. A beverage plant gets value from every rung except the top one. The skill is picking the lowest rung that solves the problem in front of you.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A six-rung ladder of AI. From the bottom: rules, such as a PLC interlock that stops the filler when the air pressure drops; machine learning, such as predicting a pump failure from vibration; deep learning, such as a camera spotting crooked labels; generative AI, such as drafting a shift handover from the log; agentic AI, such as an agent that reads line stops and drafts a maintenance work order; and AGI at the top, shown dashed because it does not exist yet.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE AI LADDER ON A BEVERAGE PLANT FLOOR</text>
<g font-family="sans-serif">
<rect x="60" y="48" width="880" height="42" rx="8" fill="#ffffff" stroke="#4a6b64" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="80" y="74" font-size="12.5" font-weight="700" fill="#4a6b64">AGI</text>
<text x="300" y="74" font-size="11.5" fill="#4a6b64">does anything a person can, across domains &#183; does not exist yet</text>
<rect x="60" y="98" width="880" height="42" rx="8" fill="#06483f"/>
<text x="80" y="124" font-size="12.5" font-weight="700" fill="#ffffff">Agentic AI</text>
<text x="300" y="124" font-size="11.5" fill="#cfe6df">reads line stops, drafts a maintenance work order for approval</text>
<rect x="60" y="148" width="880" height="42" rx="8" fill="#00695c"/>
<text x="80" y="174" font-size="12.5" font-weight="700" fill="#ffffff">Generative AI</text>
<text x="300" y="174" font-size="11.5" fill="#ffffff">drafts the shift handover from the log and the operator notes</text>
<rect x="60" y="198" width="880" height="42" rx="8" fill="#4db6a2"/>
<text x="80" y="224" font-size="12.5" font-weight="700" fill="#06483f">Deep learning</text>
<text x="300" y="224" font-size="11.5" fill="#06483f">a camera spots crooked labels and low fills at line speed</text>
<rect x="60" y="248" width="880" height="42" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="80" y="274" font-size="12.5" font-weight="700" fill="#06483f">Machine learning</text>
<text x="300" y="274" font-size="11.5" fill="#06483f">predicts a pasteuriser pump failure from vibration and current</text>
<rect x="60" y="298" width="880" height="42" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="80" y="324" font-size="12.5" font-weight="700" fill="#06483f">Rules</text>
<text x="300" y="324" font-size="11.5" fill="#06483f">PLC interlock stops the filler when air pressure drops</text>
<text x="500" y="366" text-anchor="middle" font-size="11" fill="#4a6b64">each rung contains the ones below it &#183; pick the lowest rung that solves the problem</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Six rungs, one plant. Five of them are already useful. The top one is still a research question.</figcaption>
</figure>

A plant manager once asked me whether the new vision system on the labeller was "AI or just a camera". Fair question. The vendor called it AI. The maintenance lead called it a camera. The quality manager called it the thing that stops the line for no reason. All three were right, and none of them had a shared picture of what AI actually is.

This is the first post in **AI for Operational Excellence in Beverage Plants**, an eight-part series that starts from the basics and ends with agents that draft work orders. It covers breweries, wineries, distilleries and the packaging lines they all share. Before we get to OEE and agents, we need one clear picture of what the words mean. Here it is, rung by rung.

## Rung 1: rules

Every beverage plant already runs on artificial intelligence of the oldest kind: rules written by a person. If the air pressure drops below a setpoint, stop the filler. If the pasteuriser's PU value falls below the minimum, divert the pack. If the CIP return conductivity has not reached its target, extend the caustic step.

Nobody calls this AI any more, but in the textbook sense it is. A rule-based system makes decisions that would otherwise need a person, using logic a person wrote down.

Rules have two big strengths. They are predictable and they are auditable. When the filler stops, you can point to the line of logic that stopped it. For safety and food-safety decisions, that is exactly what you want, and it is why the bottom rung is not going anywhere.

Their weakness is that someone has to know the rule. When the pattern is too complicated to write down, you need the next rung.

## Rung 2: machine learning

Machine learning is software that learns the rule from data instead of being told it.

Take a pasteuriser pump. Nobody can write a rule that says "this combination of vibration, motor current and temperature means the bearing will fail in about ten days". But if you have a few years of sensor data and a maintenance log that records when bearings failed, a machine learning model can find that pattern. It learns what "normal" looks like and flags the drift before the failure.

That is the core idea, and it covers most of the useful AI in plants today: predicting downtime, forecasting demand, estimating a value you cannot measure directly, spotting an unusual batch. I wrote a longer plain-language version for distillers in [What Is Machine Learning?]({{ '/2026/what-is-machine-learning-distillery/' | relative_url }}), and it applies just as well to a canning line.

The catch is in the phrase "if you have the data". Machine learning needs examples, labelled well, from a process that has not changed underneath them. That turns out to be the hard part in every plant I have worked in.

## Rung 3: deep learning

Deep learning is machine learning with neural networks of many layers. It earns its own rung because it can learn from messy, high-volume signals that older methods struggle with: images, sound and long streams of sensor data.

On a packaging line, this is the camera that inspects every bottle at 40,000 an hour for fill level, cap position and label alignment. On a filler, it might be an acoustic model that hears a valve starting to stick. In a malt house, it might count acrospires under a microscope.

Deep learning needs even more data than classic machine learning, and it is harder to explain. When a vision system rejects a bottle, it cannot tell you why in words. It can show you the image. That difference matters when a quality manager has to defend a reject rate.

## Rung 4: generative AI

Generative AI is deep learning trained to produce new content: text, images, code, speech. The large language models behind ChatGPT, Claude, Gemini and Copilot are the best-known examples.

The shift here is that the output is not a number or a label. It is language. On a plant floor, that is useful in places the lower rungs never reached:

- turning a night shift's log and operator notes into a clear handover
- answering "what is the caustic concentration for the bright beer tank CIP?" from the SOP, with the page cited
- drafting a first version of a five-whys analysis after a line stop
- translating a one-point lesson for a multilingual crew

Generative AI is also where hallucination comes in. These models produce fluent, confident text whether or not it is true. The [next post]({{ '/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}) explains why, using a CIP log and an SOP.

## Rung 5: agentic AI

An agent is a language model that can use tools and take steps towards a goal. Instead of answering one question, it plans, calls a tool, looks at the result and decides what to do next.

On a plant floor, a simple agent might watch the line stop log, notice that the same labeller fault has stopped the line six times this week, look up the asset in the maintenance system, check whether a work order already exists and, if not, draft one for a planner to approve.

That last clause is the whole design. An agent that drafts is useful. An agent that writes to a PLC is a safety incident waiting to happen. Post 3 in this series covers how agents work, and post 7 covers the guardrails in detail.

## Rung 6: AGI

AGI, artificial general intelligence, means a system that can learn and do any intellectual task a person can, across any domain, reliably. It is the rung that gets the headlines.

It does not exist in 2026. The best language models are broad and often impressive, and they still make basic mistakes, still need checking, and do not learn from a day on the job the way a new operator does. Serious researchers disagree about how far away AGI is, and about whether the current approach leads there at all.

Here is why I think that debate does not matter much to a plant manager on a Monday morning: every useful thing in this series works on the rungs below AGI. The filler does not need a general intelligence. It needs a good rule, a model that spots bearing wear, a camera that sees crooked labels and an assistant that writes a decent handover. If AGI arrives, it will need the same clean data and the same approvals. Building those now is not wasted either way.

## How to use the ladder

When someone proposes "AI" for a plant problem, ask which rung. Then ask whether a lower rung would do.

- A temperature excursion needs a rule and an alarm, not a model.
- A pump that fails without warning might need machine learning.
- A crooked label at line speed needs deep learning.
- A shift log nobody reads might need generative AI.
- A loss that needs several systems checked before anyone acts might need an agent.

The lower the rung, the cheaper, more predictable and easier to audit the solution. The plants that get value from AI are usually the ones that are honest about this. My earlier [AI vs Machine Learning vs Generative AI]({{ '/2026/ai-vs-machine-learning-vs-generative-ai-distillery/' | relative_url }}) post makes the same point for distilleries.

## Where this breaks

**The rungs blur in real products.** A modern vision system might use deep learning to find the defect and rules to decide whether to reject. A "GenAI assistant" might call a machine learning model underneath. The ladder is a way to think, not a product category.

**Vendors label everything AI.** A threshold alarm with a new dashboard is still a threshold alarm. Asking which rung a product sits on is the quickest way to find out what you are actually buying.

**Higher is not better.** Moving a food-safety decision from a rule to a model makes it harder to audit. Some decisions should stay on the bottom rung on purpose.

**AGI talk can freeze decisions.** "Why invest now if AGI is coming?" is a common and costly question. The data foundations, sensor quality and approval processes you build today are what any future system will need.

## The bottom line

AI is a ladder, not a single technology. Rules, machine learning, deep learning, generative AI and agents all have real jobs on a beverage plant floor. AGI does not exist yet and does not need to for any of this to work. Pick the lowest rung that solves the problem, and move up only when the problem, and the data, ask you to.

Next: [what generative AI and large language models actually are]({{ '/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}), explained through a CIP log. For the distillery version of these basics, see [What Is AI, Really? A Distiller's Plain-Language Guide]({{ '/2026/what-is-ai-distilling-plain-language/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**What is the difference between AI, machine learning and generative AI?**
AI is the umbrella for any software that does a task we would call intelligent. Machine learning is the part of AI that learns patterns from data instead of following rules someone wrote. Generative AI is a kind of machine learning that produces new content, such as text or images, rather than a prediction or a label. Each is a rung on the same ladder, not a separate technology.

**Does AGI exist in 2026?**
No. AGI, artificial general intelligence, means a system that can learn and perform any intellectual task a person can, across domains, reliably. Today's large language models are impressive and broad, but they still make basic errors, cannot be trusted without checks, and do not learn on the job the way a person does. For a beverage plant, AGI is a debate to follow, not a tool to plan around.

**Which kind of AI should a brewery or bottling plant start with?**
Usually the lowest rung that solves the problem. Many plant problems are solved by better rules and statistical process control. Machine learning helps where patterns are too complex for rules, such as predicting a pump failure. Generative AI helps with text: SOPs, handovers and root-cause notes. Agentic AI comes last, once the data and the approvals are in place.
