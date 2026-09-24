---
layout: post
title: "The AI for OpEx Roadmap, and Where It Breaks: Data First, Pilots by Loss Value, Honest ROI and the AGI Hype"
image: /assets/og/ai-opex-roadmap-where-it-breaks-agi-hype.png
description: "Part 8 of AI for Operational Excellence in Beverage Plants. How to sequence AI in a beverage plant: data foundations first, pilots chosen by the value of the loss, ROI measured against a baseline, change management on the floor, and a clear view of what AGI talk should and should not change. Closes the series."
date: 2026-09-23 09:00:00 -0700
updated: 2026-09-23
tags: [brewing-science, ai-opex, ai-strategy, operational-excellence, generative-ai]
faq:
  - q: "Where should a beverage plant start with AI?"
    a: "With the data foundations: reliable stop codes, the MES, historian, CMMS and LIMS joined on common asset and batch keys, and agreed definitions for OEE and the six big losses. Then pick one pilot on the loss worth the most, using the lowest rung of AI that can solve it. Generative AI and agents come after, on top of the same data."
  - q: "How do you measure the ROI of an AI project in a plant?"
    a: "Against a baseline, in physical units first. Record the loss before the pilot, run the pilot, and measure the change in minutes, bottles, kilowatt hours or litres, ideally against a comparable line that did not get the change. Convert to money only at the end, and count all the costs, including the data work and the people's time."
  - q: "Should a plant wait for AGI before investing in AI?"
    a: "No. AGI does not exist, nobody can say when or whether it will, and every useful AI project today depends on clean data, joined systems and clear approvals. Those are exactly what any future system would also need. Waiting costs the losses you could have recovered in the meantime."
---

**Short answer: the order matters more than the technology. First, fix the data foundations: stop codes people trust, the historian, MES, CMMS and LIMS joined, and one agreed definition of OEE. Second, pick one pilot by the value of the loss, on the lowest rung of AI that can solve it. On an illustrative line making 300,000 bottles a shift, one point of OEE is 3,000 bottles a shift and about 2.7 million a year on three shifts. Third, measure against a baseline in physical units before anyone converts it to money. Fourth, add generative AI for the text of the plant and agents that draft, not act. And treat AGI as news to follow, not a reason to wait.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A four-phase roadmap for AI in a beverage plant, illustrative timing over about a year. Phase 1, foundations: stop codes, joined systems, OEE definitions. Phase 2, a classic AI pilot chosen by loss value, such as predictive maintenance or anomaly detection. Phase 3, generative AI for text: handovers, SOP answers, root-cause support. Phase 4, an agent at autonomy level 2 that drafts work orders and changeover plans. Underneath runs a continuous band: measure against a baseline, and bring the floor with you.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">A ROADMAP THAT STARTS WITH DATA AND ENDS WITH AGENTS (ILLUSTRATIVE TIMING)</text>
<g font-family="sans-serif">
<rect x="40" y="60" width="215" height="150" rx="10" fill="#06483f"/>
<text x="147" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">1. Foundations</text>
<text x="147" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">months 0 to 3</text>
<text x="147" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">stop codes people trust</text>
<text x="147" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">MES, historian, CMMS joined</text>
<text x="147" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">one OEE definition</text>
<rect x="270" y="60" width="215" height="150" rx="10" fill="#00695c"/>
<text x="377" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">2. Classic AI pilot</text>
<text x="377" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">months 3 to 6</text>
<text x="377" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">chosen by loss value</text>
<text x="377" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">predictive maintenance or</text>
<text x="377" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">anomaly detection on SPC</text>
<rect x="500" y="60" width="215" height="150" rx="10" fill="#4db6a2"/>
<text x="607" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">3. GenAI for text</text>
<text x="607" y="108" text-anchor="middle" font-size="10.5" fill="#06483f">months 6 to 9</text>
<text x="607" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">shift handovers</text>
<text x="607" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">SOP answers with citations</text>
<text x="607" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">root-cause support</text>
<rect x="730" y="60" width="230" height="150" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="845" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">4. Agent at L2</text>
<text x="845" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">months 9 to 12</text>
<text x="845" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">drafts work orders</text>
<text x="845" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">drafts changeover plans</text>
<text x="845" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">a person approves</text>
<rect x="40" y="226" width="920" height="40" rx="10" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="251" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">ALL THE WAY THROUGH: MEASURE AGAINST A BASELINE &#183; BRING THE FLOOR WITH YOU</text>
<text x="500" y="298" text-anchor="middle" font-size="11" fill="#4a6b64">AGI is not a phase on this roadmap &#183; everything here works without it</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative timing for one site. The order is the point: each phase stands on the one before.</figcaption>
</figure>

I have seen more plant AI projects stall than fail. They rarely die from a bad model. They die in month four, when the team discovers the stop codes are unusable, the maintenance system uses different asset names from the MES, and nobody agrees what counts as planned downtime. The model sits finished, waiting for data that was never going to arrive on its own.

This is the last post in **AI for Operational Excellence in Beverage Plants**. The first seven built the vocabulary: the [AI ladder]({{ '/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}), [LLMs]({{ '/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}), [agents]({{ '/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), [OEE]({{ '/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}), [classic AI]({{ '/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), [generative AI]({{ '/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}) and [agentic AI]({{ '/2026/agentic-ai-opex-oee-agent-cmms-guardrails/' | relative_url }}) on the floor. This one puts them in order.

## Phase 1: data foundations first

Nothing later in the roadmap works without these, so they go first, even though they are the least exciting to present to a board:

- **Stop codes people trust.** Automatic stop detection from the PLC, plus a short list of reasons that map to the six big losses. Test it with the operators, not just the engineers.
- **Joined systems.** The MES, historian, CMMS and LIMS linked on common keys: the same asset IDs, the same batch or order numbers, the same clock. This is usually the biggest job on the list.
- **One definition of OEE.** What counts as planned time, what the ideal rate is for each product and format, written down and published.
- **A place for the data.** A lakehouse or warehouse on the IT side, fed from a DMZ replica, where the data model can be built without touching the control network.

It is the same lesson as the [winery data work in the Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}): the definitions and the data model come before any assistant.

## Phase 2: pick a pilot by the value of the loss

With the losses measured, the choice of pilot becomes arithmetic, not enthusiasm. For each candidate loss, ask four questions:

1. **How much is it worth?** Minutes or bottles lost per week, times what a bottle or a minute is worth to you.
2. **Is the data ready?** Does the signal exist, at the right frequency, joined to the stop log?
3. **What is the lowest rung that can fix it?** A rule, SPC, a model, generative AI or an agent.
4. **What happens if it is wrong?** A wrong suggestion on a changeover is cheap. A wrong call on a pasteuriser is not.

Scale helps focus the mind. On the illustrative filler line from post 4, the ideal output is 300,000 bottles a shift. One point of OEE is 3,000 bottles a shift. On three shifts for 300 days, that is 2.7 million bottles a year. Multiply by your own contribution per bottle and you know what a one-point improvement is worth before you have spent anything.

The pilot is usually classic AI: predictive maintenance on the asset behind the biggest breakdown loss, or anomaly detection on the process behind the biggest quality loss. It should be narrow: one line, one asset family, one loss.

## Phase 3: generative AI for the text of the plant

Once there is a reliable data layer, generative AI has something to stand on. Shift handovers drafted from the stop log and notes, SOP answers with citations, root-cause support that proposes and never concludes. These tend to spread quickly because people feel the time saved every shift. They also expose any remaining data problems quickly, because a handover built on bad stop codes reads obviously wrong.

## Phase 4: an agent that drafts

Only now does an agent make sense: the OEE loss agent from post 7, at autonomy level 2, reading replicated data, drafting work orders and changeover plans for a person to approve, with every tool call logged and no path to process control. It builds on everything before it: the stop codes to rank losses, the joined systems to connect a stop to an asset, and the handover to report what it did.

## Honest ROI

AI projects in plants are prone to generous maths. A few habits keep it honest:

- **Measure the baseline before you start.** Four to eight weeks of the loss as it is, recorded the same way you will record it afterwards.
- **Count in physical units first.** Minutes, bottles, kilowatt hours, litres of water, kilograms of product lost. Convert to money only at the end, with the finance team.
- **Use a comparison where you can.** A similar line that did not get the pilot shows how much of the change came from the season, the product mix or a new supervisor.
- **Count every cost.** Licences and compute, yes, but also the data engineering, the operators' time in design sessions and the ongoing care of the models.
- **Credit the whole team.** Often the biggest gain comes from fixing the stop codes in phase 1, not from the model in phase 2. Say so.

## Change management on the floor

The technology is the easy part. People decide whether any of this works:

- **Design with operators.** They know which stop codes are nonsense and which alarms everyone ignores. Involve them from the first week.
- **Never use it to blame.** If the handover summary or the loss agent becomes a tool for finding who to blame, the data will get worse within a month.
- **Give it an owner on the floor.** A production supervisor, not only the data team, owns each tool and can switch it off.
- **Train for the failure modes.** Teach people that the model can be confidently wrong, and that checking the citation or the evidence is part of the job.

## AGI hype versus reality

Every few months there is a headline that AGI is close, and someone in a plant meeting asks whether it is worth investing now or waiting for the systems that will do everything. The honest answer has three parts.

AGI does not exist today. Nobody can say reliably when or whether it will. And every useful system in this series, from a vibration model to a work-order agent, depends on clean data, joined systems, clear definitions and approval processes. A future general intelligence would need exactly the same things to be trusted in a plant. The foundations are not wasted whatever happens. Waiting, on the other hand, has a known cost: every shift of losses you could have recovered.

## Where this breaks

**Phase 1 takes longer than planned.** Joining systems and cleaning codes always does. Protect the time, and resist pressure to skip to the demo.

**Pilots that never scale.** A pilot on one line that needs a data scientist to keep it running will not reach the other five lines. Build the second line into the plan from the start.

**ROI claims that cannot be checked.** If a vendor's savings cannot be traced to a measured change against a baseline, treat them as marketing.

**Autonomy creeps.** After a good year at level 2, there will be pressure to let the agent act on its own. Decide that deliberately, by the cost of a mistake, and keep process control out of it.

## The bottom line

AI for operational excellence in a beverage plant is a sequence, not a purchase. Foundations first, then one pilot chosen by the value of the loss on the lowest rung that works, then generative AI for the plant's text, then an agent that drafts for people to approve. Measure against a baseline in bottles and minutes, bring the floor with you, and do not wait for AGI. The losses are on the line today, and so is almost everything you need to recover them.

That closes the series. The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}). For the winery version of the data foundations, see [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}); for distillery basics, [AI Foundations for Distillers]({{ '/series/distilling-ai-foundations/' | relative_url }}); and for the spirit and beer sides of GenAI and data engineering, [The Still and the Model]({{ '/series/still-and-model/' | relative_url }}) and [The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**Where should a beverage plant start with AI?**
With the data foundations: reliable stop codes, the MES, historian, CMMS and LIMS joined on common asset and batch keys, and agreed definitions for OEE and the six big losses. Then pick one pilot on the loss worth the most, using the lowest rung of AI that can solve it. Generative AI and agents come after, on top of the same data.

**How do you measure the ROI of an AI project in a plant?**
Against a baseline, in physical units first. Record the loss before the pilot, run the pilot, and measure the change in minutes, bottles, kilowatt hours or litres, ideally against a comparable line that did not get the change. Convert to money only at the end, and count all the costs, including the data work and the people's time.

**Should a plant wait for AGI before investing in AI?**
No. AGI does not exist, nobody can say when or whether it will, and every useful AI project today depends on clean data, joined systems and clear approvals. Those are exactly what any future system would also need. Waiting costs the losses you could have recovered in the meantime.
