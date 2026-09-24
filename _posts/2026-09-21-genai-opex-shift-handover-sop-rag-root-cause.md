---
layout: post
title: "GenAI for OpEx: Shift Handovers, SOP Search, Root-Cause Assistants and a Multilingual Floor"
image: /assets/og/genai-opex-shift-handover-sop-rag-root-cause.png
description: "Part 6 of AI for Operational Excellence in Beverage Plants. Where generative AI earns its place on the plant floor: shift handover summaries built from the MES and operator notes, SOP answers with citations, a five-whys and Ishikawa assistant that proposes causes but never concludes, one-point lessons, and translation for a crew that speaks four languages."
date: 2026-09-21 09:00:00 -0700
updated: 2026-09-21
tags: [brewing-science, ai-opex, generative-ai, operational-excellence, root-cause-analysis]
faq:
  - q: "How can generative AI help with shift handovers in a brewery or bottling plant?"
    a: "It can read the shift's line stops from the MES, the alarms and the operator notes, and draft a structured handover: safety issues, quality holds, open faults, and what the next shift needs to do first. The figures come straight from the systems, the model writes the summary around them, and the outgoing supervisor checks and signs it before handing over."
  - q: "Can an LLM do root-cause analysis?"
    a: "It can help, not conclude. A good assistant proposes candidate causes under each Ishikawa heading, pulls similar past incidents and asks the next why. It cannot see the machine, and it will happily produce a neat causal chain that is wrong. The team still has to verify each link with evidence from the floor."
  - q: "Is machine translation safe for SOPs and safety instructions?"
    a: "It is useful for drafts and for everyday notes, and it needs control for anything safety-critical. Use a fixed glossary for hazard terms, chemical names and equipment names, and have a fluent person who knows the plant review translated SOPs and safety instructions before they are issued."
---

**Short answer: generative AI earns its place on a plant floor wherever the work is text, and a beverage plant produces a lot of text nobody reads. It can draft the shift handover from the MES stop log, the alarms and the operators' notes. It can answer SOP questions with the section cited. It can help a team through five whys and an Ishikawa diagram by proposing causes and pulling similar past incidents, while the team verifies. It can draft one-point lessons and translate for a crew that speaks several languages. In every case the pattern is the same: data from systems, words from the model, judgement and signature from a person.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A shift handover pipeline. Three inputs on the left: line stops from the MES, alarms from SCADA, and operator notes, some in Hindi or Kannada. They feed a language model, which drafts a structured handover with four sections: safety, quality holds, open faults, and first actions for the next shift. Every number in the draft comes from the systems. The outgoing supervisor edits and signs the handover before it is issued.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">A SHIFT HANDOVER THE NEXT SHIFT WILL ACTUALLY READ</text>
<g font-family="sans-serif">
<rect x="40" y="60" width="210" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="145" y="84" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">line stops</text>
<text x="145" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">MES, with durations</text>
<rect x="40" y="130" width="210" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="145" y="154" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">alarms</text>
<text x="145" y="172" text-anchor="middle" font-size="10.5" fill="#4a6b64">SCADA, grouped</text>
<rect x="40" y="200" width="210" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="145" y="224" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">operator notes</text>
<text x="145" y="242" text-anchor="middle" font-size="10.5" fill="#4a6b64">English, Hindi, Kannada</text>
<line x1="250" y1="88" x2="330" y2="158" stroke="#4db6a2" stroke-width="2"/>
<line x1="250" y1="158" x2="330" y2="158" stroke="#4db6a2" stroke-width="2"/>
<line x1="250" y1="228" x2="330" y2="158" stroke="#4db6a2" stroke-width="2"/>
<rect x="330" y="120" width="170" height="76" rx="9" fill="#06483f"/>
<text x="415" y="152" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">LLM drafts</text>
<text x="415" y="172" text-anchor="middle" font-size="10.5" fill="#cfe6df">numbers from systems</text>
<line x1="500" y1="158" x2="560" y2="158" stroke="#4db6a2" stroke-width="2"/>
<rect x="560" y="56" width="240" height="204" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="680" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">HANDOVER, LINE 2, NIGHTS</text>
<text x="580" y="112" font-size="11" fill="#06483f">1. Safety</text>
<text x="580" y="140" font-size="11" fill="#06483f">2. Quality holds</text>
<text x="580" y="168" font-size="11" fill="#06483f">3. Open faults</text>
<text x="580" y="196" font-size="11" fill="#06483f">4. First actions, next shift</text>
<text x="680" y="238" text-anchor="middle" font-size="10" fill="#4a6b64">each item links to its source</text>
<line x1="800" y1="158" x2="840" y2="158" stroke="#4db6a2" stroke-width="2"/>
<rect x="840" y="120" width="120" height="76" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="900" y="152" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">supervisor</text>
<text x="900" y="172" text-anchor="middle" font-size="10.5" fill="#4a6b64">edits and signs</text>
<rect x="40" y="284" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="309" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DATA FROM SYSTEMS &#183; WORDS FROM THE MODEL &#183; SIGNATURE FROM A PERSON</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The model does the writing. The systems supply the facts. The supervisor owns the handover.</figcaption>
</figure>

Every plant I have worked in had a shift handover book. Most of them had the same three entries, night after night: "line ran OK", "labeller issues", "see maintenance". The information the next shift needed was somewhere else, in the stop log, in the alarm list, in the head of the operator who had just gone home.

That is the problem generative AI is actually good at. Not controlling the process, not predicting failures (the [previous post]({{ '/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}) covered the models that do that), but reading and writing the text that holds a plant together. This is the sixth post in the series, and it covers five places where that pays.

## Shift handover summaries

A useful handover answers four questions: is anything unsafe, is any product on hold, what is still broken, and what must the next shift do first. The data to answer them already exists:

- the MES stop log, with durations and reason codes
- the alarm history from SCADA, which a script can group so forty repeats of one alarm count as one issue
- the operators' free-text notes
- quality holds from the LIMS or the QA system

A language model drafts the handover from those inputs in a fixed structure. Two rules make it trustworthy. Every number (stop minutes, hold quantities, batch numbers) is passed in from the systems, never written by the model from memory. And every line of the draft links back to its source, so the incoming supervisor can click through. The outgoing supervisor reads, edits and signs. The handover book gets better and the supervisor spends ten minutes instead of thirty.

## SOP answers with citations

The [second post in this series]({{ '/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}) explained retrieval-augmented generation through a CIP example. On the floor, the use is simple: an operator asks "what is the torque setting for the 330 ml capper after a format change?" and gets the answer with the SOP number and section.

The value is not the chatbot. It is shortening the distance between a question and the controlled document. What makes or breaks it is the document library: one current version of each SOP, clearly titled, with superseded versions out of the index. A plant with a messy SOP folder will get messy answers, faster.

## A root-cause assistant for five whys and Ishikawa

When a line stops for two hours, a good team runs a structured root-cause analysis: five whys to follow a chain of causes, an Ishikawa (fishbone) diagram to make sure no category is missed. The usual headings are man, machine, method, material, measurement and environment.

A language model is a useful facilitator here. Given the incident description, the stop data and the maintenance history, it can:

- propose candidate causes under each Ishikawa heading, so the team does not fixate on the first idea
- pull similar past incidents from the CMMS and the incident log, which is often the most valuable thing it does
- ask the next "why" when the team stops too early at "operator error"
- draft the incident report once the team has agreed the cause

What it must not do is conclude. A language model has never seen your filler. It will produce a tidy, logical chain of five whys that reads beautifully and is wrong, because plausible is what it is built for. Each link in the chain needs evidence from the floor: a photo, a reading, a worn part. The model proposes, the team verifies.

## Training and one-point lessons

A one-point lesson is a single page, mostly pictures, teaching one thing: how to check a crown crimp, how to set a guide rail. They are among the best training tools in TPM and among the most neglected, because writing them takes time nobody has.

A model can draft one from the SOP section and a few photos taken by the operator who knows the job. The subject-matter expert edits and approves it. The same approach works for quizzes after training, and for turning a long SOP into a short checklist. Keep the approved version in the document system like any other controlled document.

## A multilingual floor

Many beverage plants run in several languages at once. In an Indian brewery, an operator may write notes in Hindi, Kannada or Marathi, the supervisor may read English and the SOPs may exist only in English. Current models translate between these well enough to be genuinely useful for everyday notes and questions.

Two controls matter. Use a fixed glossary for hazard terms, chemical names and equipment names, so "caustic" never becomes a vague word for "strong". And have a fluent person who knows the plant review translated SOPs and safety instructions before they are issued. Translation for reading is low risk. Translation of an instruction someone will follow near a hot caustic line is not.

## Where this breaks

**Garbage stop codes make garbage handovers.** If half the stops are "other", the handover will faithfully summarise "other". The model cannot recover what was never recorded.

**Fluent text hides missing information.** A well-written handover that leaves out the one quality hold that mattered is worse than a scruffy one, because people trust it. Build a check that every open hold and every safety alarm appears in the draft.

**Root-cause assistants anchor teams.** If the model's first suggestion is shown first, the team may never look past it. Show several candidate causes, from different headings, and ask the team for theirs before revealing them.

**Controlled documents stay controlled.** A drafted SOP or one-point lesson is not issued until someone with authority approves it. The model speeds up writing, not approval.

## The bottom line

Generative AI in a plant is at its best with text: the handover nobody writes properly, the SOP nobody can find, the root-cause meeting that stops at "operator error", the lesson nobody has time to draw, the note written in a language the supervisor does not read. In each case the systems supply the facts, the model writes, and a person checks and signs. That division of labour is not a limitation. It is the design.

Next: [agentic AI for OpEx]({{ '/2026/agentic-ai-opex-oee-agent-cmms-guardrails/' | relative_url }}), an agent that watches OEE losses and drafts work orders, and the guardrails that keep it away from process control. For the earlier take on SOP search, see [Knowledge Search Over Brewery SOPs With Gen AI]({{ '/2022/gen-ai-search-brewery-sops/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**How can generative AI help with shift handovers in a brewery or bottling plant?**
It can read the shift's line stops from the MES, the alarms and the operator notes, and draft a structured handover: safety issues, quality holds, open faults, and what the next shift needs to do first. The figures come straight from the systems, the model writes the summary around them, and the outgoing supervisor checks and signs it before handing over.

**Can an LLM do root-cause analysis?**
It can help, not conclude. A good assistant proposes candidate causes under each Ishikawa heading, pulls similar past incidents and asks the next why. It cannot see the machine, and it will happily produce a neat causal chain that is wrong. The team still has to verify each link with evidence from the floor.

**Is machine translation safe for SOPs and safety instructions?**
It is useful for drafts and for everyday notes, and it needs control for anything safety-critical. Use a fixed glossary for hazard terms, chemical names and equipment names, and have a fluent person who knows the plant review translated SOPs and safety instructions before they are issued.
