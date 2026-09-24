---
layout: post
title: "Agentic AI for OpEx: An OEE Loss Agent That Drafts Work Orders, and the Guardrails That Keep It Off the PLC"
image: /assets/og/agentic-ai-opex-oee-agent-cmms-guardrails.png
description: "Part 7 of AI for Operational Excellence in Beverage Plants. An agent that watches OEE losses every shift, finds recurring faults, checks the CMMS and drafts work orders and changeover plans for people to approve. Plus the guardrails that matter: the Purdue model, read-only access to OT data, no writes to PLC or SCADA, approvals, an audit log and replay evals."
date: 2026-09-22 09:00:00 -0700
updated: 2026-09-22
tags: [brewing-science, ai-opex, agentic-ai, predictive-maintenance, ot-security]
faq:
  - q: "What can an AI agent safely do in a beverage plant?"
    a: "Read production, maintenance and quality data, work out which losses matter, and draft actions for people: maintenance work orders, changeover plans, shift summaries, messages to a planner. Each draft carries its evidence and waits for approval. It should have no path to write to PLCs, SCADA or process setpoints."
  - q: "What is the Purdue model and why does it matter for AI agents?"
    a: "The Purdue model is a reference architecture that separates a plant's networks into levels, from the physical process and its controllers at the bottom to business systems at the top, with a demilitarised zone between operations and enterprise IT. An agent belongs on the IT side, reading replicated data from the DMZ. It should never open connections down into the control levels."
  - q: "How do you test an AI agent before letting it loose on a plant?"
    a: "Replay history. Run the agent over the last month or two of shifts, using the data as it was at the time, and compare its drafts with what planners and engineers actually did. Measure how many real issues it caught, how many drafts were noise, and how many would have been wrong. Repeat the replay whenever the model, the prompts or the tools change."
---

**Short answer: the most useful agent in a beverage plant is not a robot operator. It is a patient analyst that, at the end of every shift, reads the stop log, ranks the OEE losses, notices that the labeller glue unit has stopped the line six times this week, checks the maintenance system, finds no open work order and drafts one with the evidence attached for a planner to approve. The same agent can draft a changeover sequence that cuts flush time. What makes it safe is not the model. It is the architecture: read-only access to replicated OT data on the IT side of the Purdue model, no path to PLCs or SCADA, write tools that only create drafts, an audit log of every tool call and replay tests before it goes live.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The Purdue model with an AI agent placed on it. Levels 0 to 2 at the bottom hold the process, the PLCs and SCADA. Level 3 holds the historian, MES and CMMS. A DMZ holds a read-only replica of historian and MES data. Levels 4 and 5 hold enterprise IT, where the agent runs. The agent reads from the DMZ replica and writes only draft work orders to the CMMS, which a planner approves. A crossed-out arrow from the agent to the PLCs and SCADA shows that it has no write path to process control. An audit log records every tool call.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">WHERE THE AGENT LIVES, AND WHAT IT CAN REACH</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="600" height="62" rx="9" fill="#06483f"/>
<text x="60" y="76" font-size="11" font-weight="700" fill="#cfe6df">LEVELS 4-5 &#183; ENTERPRISE IT</text>
<rect x="330" y="60" width="160" height="42" rx="8" fill="#ffffff"/>
<text x="410" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">OEE loss agent</text>
<rect x="40" y="124" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="60" y="148" font-size="11" font-weight="700" fill="#00695c">DMZ</text>
<text x="60" y="166" font-size="10.5" fill="#4a6b64">read-only replica: historian tags, MES stops</text>
<rect x="40" y="192" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="60" y="216" font-size="11" font-weight="700" fill="#06483f">LEVEL 3 &#183; SITE OPERATIONS</text>
<text x="60" y="234" font-size="10.5" fill="#4a6b64">historian &#183; MES &#183; CMMS &#183; LIMS</text>
<rect x="40" y="260" width="600" height="56" rx="9" fill="#ffffff" stroke="#4a6b64" stroke-width="1.5"/>
<text x="60" y="284" font-size="11" font-weight="700" fill="#06483f">LEVELS 0-2 &#183; PROCESS AND CONTROL</text>
<text x="60" y="302" font-size="10.5" fill="#4a6b64">sensors &#183; PLCs &#183; SCADA &#183; HMIs</text>
<line x1="410" y1="102" x2="410" y2="124" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="425" y="118" font-size="10" fill="#2e9e7c">reads</text>
<path d="M490 81 C560 81 560 220 520 220" fill="none" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="566" y="150" font-size="10" fill="#2e9e7c">drafts only</text>
<text x="500" y="224" font-size="10" text-anchor="end" fill="#2e9e7c">CMMS draft</text>
<line x1="345" y1="102" x2="345" y2="260" stroke="#ff4081" stroke-width="2.5" stroke-dasharray="5 4"/>
<line x1="335" y1="244" x2="355" y2="264" stroke="#ff4081" stroke-width="3"/>
<line x1="355" y1="244" x2="335" y2="264" stroke="#ff4081" stroke-width="3"/>
<text x="352" y="188" font-size="10" font-weight="700" fill="#ff4081">no write path to control</text>
<rect x="680" y="50" width="280" height="266" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="820" y="76" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">GUARDRAILS</text>
<g font-size="11" fill="#06483f">
<text x="700" y="106">1. read-only OT data, via DMZ</text>
<text x="700" y="134">2. never write to PLC or SCADA</text>
<text x="700" y="162">3. write tools create drafts only</text>
<text x="700" y="190">4. a person approves every draft</text>
<text x="700" y="218">5. audit log of every tool call</text>
<text x="700" y="246">6. replay evals before go-live</text>
<text x="700" y="274">7. step, cost and rate limits</text>
<text x="700" y="302">8. one switch turns it off</text>
</g>
<rect x="40" y="330" width="920" height="38" rx="10" fill="#06483f"/>
<text x="500" y="354" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">THE MODEL CAN BE WRONG &#183; THE ARCHITECTURE MAKES SURE THAT IS CHEAP</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The agent sits with the business systems, reads a replica of the plant data and can only create drafts. Process control is out of reach by design.</figcaption>
</figure>

Every plant has a list of losses everyone knows about and nobody has time to chase. The labeller that stops for thirty seconds a dozen times a shift. The changeover that always runs twenty minutes long. The pump that trips when the ambient temperature passes 35 degrees. Each is small. Together they are often the biggest bar on the [OEE waterfall]({{ '/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}).

The [third post in this series]({{ '/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}) explained how agents work. This one, the seventh, puts one to work on those losses and spends at least as long on the fences around it.

## The OEE loss agent, step by step

Here is what a well-scoped agent does at the end of each shift. Every step is a tool call to a tested query or a controlled system.

1. **Rank the losses.** Pull the shift's stops from the MES replica and group them by the six big losses and by asset. The labeller glue unit accounts for 31 minutes across six stops.
2. **Check for recurrence.** Look back over the last two weeks. The same fault code appears 23 times, rising.
3. **Look at the asset.** Query the CMMS: the last work order on the glue unit was closed four weeks ago, "cleaned nozzles". No open order now.
4. **Look at the signals.** Pull the glue temperature tag from the historian replica around each stop. It dips below its setpoint band just before most of them.
5. **Draft the action.** Create a draft work order in the CMMS: asset, symptom, the 23 stops, the temperature pattern with a chart link, the previous work order, a suggested priority. Status: draft, awaiting planner.
6. **Report.** Add one line to the shift handover: "Draft WO raised for L2 labeller glue unit, recurring temperature dips, see link."

A planner reviews the draft the next morning, adjusts the priority and releases it. The agent did in two minutes what would have taken an engineer an hour, and it did it every shift, not just when someone had time.

## Changeover plans, drafted not scheduled

The same pattern works for changeovers, the second of the six big losses. Given the week's production plan from the ERP and the known changeover times between products and formats, an agent can draft a run sequence that reduces flushes and format changes. Dark beer after pale, not pale after dark. Group the 330 ml runs together. It can also flag where the plan forces an avoidable changeover.

It hands the draft to the planner, who knows things the agent does not: the customer order that has to ship on Thursday, the operator who is on leave, the tank that will not be ready. The planner edits and publishes. The agent never touches the live schedule.

## Guardrail 1: the Purdue model

Most beverage plants organise their networks along the lines of the Purdue model, and OT security standards such as IEC 62443 build on the same separation. At the bottom, levels 0 to 2 hold the process, the PLCs, SCADA and HMIs. Level 3 holds site operations: historian, MES, CMMS, LIMS. Levels 4 and 5 are enterprise IT. Between operations and IT sits a demilitarised zone, the DMZ, where data can be shared without opening the control network.

An agent belongs on the IT side. It reads a replica of historian and MES data published into the DMZ. It never opens a connection down into levels 0 to 2. If your architecture would require it to, the architecture is not ready for an agent.

## Guardrail 2: no writes to process control

This one deserves its own line. **Nothing an agent does should change a PLC, a SCADA value or a process setpoint.** Not through a tool, not through a script, not "just for this one low-risk parameter". Process control is engineered, validated and interlocked for good reasons, and a language model that is right 98 percent of the time is not acceptable in a loop where the other 2 percent is a caustic line or a pressurised vessel.

The simplest way to enforce this is to never build the tool. If there is no `set_value` function on any MCP server the agent can reach, and its service account has no write rights anywhere near OT, the question never comes up.

## Guardrails 3 to 8: drafts, approvals, logs, evals, limits, off switch

- **Write tools create drafts only.** The CMMS tool can create a work order in draft status. It cannot release one, close one or change a released one.
- **A person approves every draft.** With the evidence shown, not just the conclusion. Track edit and rejection rates, because a rate of zero usually means nobody is reading.
- **An audit log of every tool call.** Which tool, which inputs, what came back, what the agent drafted. When someone asks why a work order exists, the answer is in the log.
- **Replay evals before go-live.** Run the agent over the last one or two months of shifts, with the data as it was at the time, and compare its drafts with what planners and engineers actually did. Count the real issues it caught, the noise it raised and the drafts that would have been wrong. Repeat whenever the model, the prompts or the tools change.
- **Step, cost and rate limits.** A cap on tool calls per run and drafts per shift, so a confused agent cannot flood the CMMS.
- **One switch turns it off.** Someone in operations, not only in IT, can stop the agent immediately.

On the autonomy ladder from post 3, this agent sits at **L2**: it reads freely and drafts, and a person approves. That is where it should stay.

## Where this breaks

**The agent inherits every data problem.** If stop codes are vague, the ranking is vague. If the CMMS asset hierarchy does not match the MES, the agent cannot link a stop to a work order. Fix these first. They are cheaper than any model.

**Too many drafts kill trust.** An agent that raises fifteen drafts a shift will be ignored within a week. Start with one loss type and one line, and tune for precision over coverage.

**Prompt injection through plant text.** The agent reads operator notes and old work orders. Treat all of that as data, never as instructions, and keep every write tool behind approval so a strange note cannot become an action.

**Replica lag.** If the DMZ replica runs hours behind, the agent works on stale data. Show the data timestamp on every draft.

**Approval fatigue.** Oversight that consists of clicking approve forty times at the end of a shift is not oversight. Keep volumes low and evidence clear.

## The bottom line

A good plant agent is an analyst, not an operator. It reads the losses every shift, connects the stop log, the historian and the maintenance history, and drafts the work order or changeover plan a busy engineer never gets to. It is safe because of where it sits and what it can touch: the IT side of the Purdue model, read-only OT data, draft-only write tools, a person approving, every call logged, tested by replaying history. The model will sometimes be wrong. The architecture makes sure that being wrong costs a rejected draft, not a batch.

Next, and last: [the roadmap and where it breaks]({{ '/2026/ai-opex-roadmap-where-it-breaks-agi-hype/' | relative_url }}). For the predictive side of line downtime, see [Predicting Packaging Line Downtime and Lifting OEE]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**What can an AI agent safely do in a beverage plant?**
Read production, maintenance and quality data, work out which losses matter, and draft actions for people: maintenance work orders, changeover plans, shift summaries, messages to a planner. Each draft carries its evidence and waits for approval. It should have no path to write to PLCs, SCADA or process setpoints.

**What is the Purdue model and why does it matter for AI agents?**
The Purdue model is a reference architecture that separates a plant's networks into levels, from the physical process and its controllers at the bottom to business systems at the top, with a demilitarised zone between operations and enterprise IT. An agent belongs on the IT side, reading replicated data from the DMZ. It should never open connections down into the control levels.

**How do you test an AI agent before letting it loose on a plant?**
Replay history. Run the agent over the last month or two of shifts, using the data as it was at the time, and compare its drafts with what planners and engineers actually did. Measure how many real issues it caught, how many drafts were noise, and how many would have been wrong. Repeat the replay whenever the model, the prompts or the tools change.
