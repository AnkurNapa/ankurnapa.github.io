---
layout: post
title: "Excise Returns as Data Contracts: Tests Reconcile, the LLM Drafts, a Person Signs"
image: /assets/og/wine-excise-returns-data-contracts-genai.png
description: "Part 5 of The Cellar Ledger. A winery excise return is a balance equation per tax class. Treat its inputs as a data contract, test the equation in the pipeline every night, and use GenAI for what it is good at here: classifying messy removal notes, drafting the explanations and finding the right paragraph of guidance."
date: 2026-07-12 09:00:00 -0700
updated: 2026-07-12
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, compliance]
faq:
  - q: "What is a data contract in a winery context?"
    a: "It is a written, enforced agreement about what a dataset must contain. For excise, the contract on the movement ledger might say every removal has a tax class, a destination type and a measured alcohol, and every month's opening balance equals the previous month's closing. The pipeline tests those rules and stops bad records before they reach the return."
  - q: "Can an LLM fill in a wine excise return?"
    a: "It should not fill in the numbers. The figures come from tested queries over the ledger. An LLM is useful around the return: classifying free-text removal notes into categories, drafting the explanation for an unusual loss, and finding the relevant guidance paragraph for a person to read. A named person reviews and signs every return."
  - q: "Why do wine tax classes cause reconciliation problems?"
    a: "Because a lot can change class without leaving the building. In the US, for example, still wine is taxed in bands by alcohol, with a line at 16 percent. Blending, fortification or a corrected lab result can move a lot across that line, and if the change is not recorded as an event, the per-class balance stops adding up."
---

**Short answer: an excise return is a balance equation per tax class: opening, plus produced and received, minus removals and losses, equals closing. If that equation is copied into a form by hand at month-end, every error surfaces at the worst possible moment. Treat the return's inputs as a data contract on the movement ledger, test the equation in the pipeline every night, and the return becomes a query that has already passed its checks. GenAI helps around the edges: sorting messy removal notes, drafting the explanation for an odd loss, and finding the right paragraph of guidance. It does not produce the figures, and it does not sign.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The excise balance equation for one tax class: opening balance, plus produced and received, minus removed tax-paid, minus transferred in bond or exported, minus losses, equals closing balance. Underneath, three nightly tests from the data contract: opening equals last month's closing, the equation balances to zero per class, and every class change is recorded as an event. A banner says the return is a query that already passed its tests.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ONE TAX CLASS, ONE EQUATION, TESTED EVERY NIGHT</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="95" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">opening</text>
<text x="95" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="177" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">+</text>
<rect x="195" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">produced</text>
<text x="260" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; received</text>
<text x="342" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="360" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="425" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">removed</text>
<text x="425" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">tax-paid</text>
<text x="507" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="525" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="590" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">in bond</text>
<text x="590" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; export</text>
<text x="672" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="690" y="60" width="110" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="745" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">losses</text>
<text x="817" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">=</text>
<rect x="835" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="900" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">closing</text>
<text x="900" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">balance</text>
<text x="500" y="160" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">DATA CONTRACT TESTS</text>
<rect x="30" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="180" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; opening = last closing</text>
<text x="180" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">no silent edits between months</text>
<rect x="350" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; equation balances to 0</text>
<text x="500" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">per tax class, per month</text>
<rect x="670" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="820" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; class changes are events</text>
<text x="820" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">a blend across 16% is recorded</text>
<rect x="30" y="262" width="940" height="42" rx="10" fill="#06483f"/>
<text x="500" y="288" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">THE RETURN IS A QUERY THAT ALREADY PASSED ITS TESTS</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The same equation the excise officer checks, tested by the pipeline every night instead of by a person at month-end.</figcaption>
</figure>

It is the second working day of the month and the excise return is due. Somebody opens last month's return, opens the cellar system, and starts copying numbers into the form. The opening balance does not match last month's closing. Someone edited a tank volume in between. The next three hours go on finding which one, while the deadline gets closer.

This is the least glamorous post in the series and possibly the most useful. Every winery that pays duty lives with it, and most of them solve it with a person and a calculator. The [movement ledger]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) and the [loss map]({{ '/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) have already done most of the work. This post adds the rules that make the return trustworthy before anyone opens the form.

## The return is a balance equation

Whatever the country, a winery excise return comes down to the same identity for each tax class:

> opening + produced and received - removed tax-paid - transferred in bond or exported - losses = closing

In the US it is the monthly Report of Wine Premises Operations, broken out by tax class. In the EU, duty-suspended movements run through EMCS. In India, each state excise department has its own registers and formats. The forms differ. The arithmetic does not.

That is good news for a data team, because an identity is something a pipeline can test.

## The tax class trap

The subtle part is the "per tax class". Wine is taxed in bands. In the US, still wine at or under 16% alcohol is one class, over 16 to 21% another, over 21 to 24% another, with sparkling and carbonated wines separate. Other markets draw their own lines.

A lot can change class without leaving the building. Blend a 15.8% lot with a 16.6% lot and the result may sit either side of 16% depending on the volumes. Fortify, and a lot jumps classes. Correct a lab result, and a lot that was reported under 16% last month turns out to be over it.

If those changes are not recorded, the per-class equation stops balancing, and nobody knows why. So the class change itself becomes an event in the ledger: lot 24-SH-03 moves from class A to class B on this date, with this volume, because of this blend. It is also why the [first post in this series]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) insisted on measured alcohol replacing predicted alcohol. A tax class based on a rule-of-thumb conversion is a problem waiting for an auditor.

## Writing the data contract

A data contract is a written agreement about what a dataset must contain, enforced by the pipeline rather than by good intentions. For excise, the contract on the movement ledger is short:

1. **Every removal has a tax class, a destination type and a measured alcohol.** Tax-paid, in bond, export, sample, destroyed. A removal with no destination is rejected.
2. **Every class change is an event.** If a lot's measured alcohol crosses a class boundary, the pipeline expects a class change event and flags its absence.
3. **Opening equals last closing.** For every class, every month. This one test catches every silent edit.
4. **The identity balances to zero.** Per class, per month, within a tolerance you agree with your accountant. A non-zero residual blocks the return until someone explains it.
5. **No negative balances.** A class with a negative closing volume means an event is missing or misclassified.

In practice these are a handful of tests in whatever you already use: dbt tests, Great Expectations, Fabric data quality rules, or plain SQL assertions that fail the nightly job. The important choice is running them **every night**, not at month-end. A test that fails on the 14th gives you two weeks to fix the record while people still remember what happened. A test that fails on the 2nd gives you a bad morning.

Records that fail go to a quarantine table with the failed rule attached, not into the void. The cellar team sees a short list of things to fix. The return never sees them until they are fixed.

## Where GenAI actually helps

With the numbers handled by tested queries, the useful jobs for a language model are the ones that involve messy text.

**Classifying removal notes.** Operators write things like "2 cs to Sunday tasting", "breakage, dropped pallet" or "sample for show". Those need to become categories: sample, tasting room, breakage, destroyed. A model classifies them well, with a confidence score, and sends anything uncertain to a person. It is a small job that saves hours every month.

**Drafting the explanations.** When a loss is larger than usual, the return or the internal file needs a note saying why. The model drafts it from the loss map figures and the adjustment reasons, in the same pattern as the [variance note]({{ '/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}): SQL supplies every number, the model writes the words around them.

**Finding the right paragraph.** Excise guidance is long and often updated. A retrieval assistant over the regulator's published guidance, which quotes the paragraph and links to it, saves real time when a question comes up: "how do we treat wine used for topping another bonded premises?". It is a librarian. The person still reads the paragraph and makes the call.

**Answering the officer.** When an excise officer asks why a class balance moved, an agent with read access to the ledger can pull the exact events, dates and operators, and draft a reply with the rows attached. The reply goes out after a person checks it.

What it must not do is fill in the return, interpret the law, or decide how a grey-area movement should be treated. Those are judgements with legal weight, and they belong to a named person.

## Where this breaks

**Rules differ and change.** Tax classes, allowable losses and reporting formats vary by country, and within India by state. The contract has to encode your rules, reviewed by someone who knows them, and be updated when they change.

**Contracts that block month-end get bypassed.** If a failing test stops the return on the 2nd with no way through, someone will find a way round it. Run the tests nightly and design the quarantine path so fixing a record is easier than working round the pipeline.

**Allowable loss is a regulatory question, not a statistical one.** The loss map can tell you a loss is unusual. Whether it is within what the regulator allows, and whether it is taxable, is for the rules and the person who signs.

**Retrieval can surface the wrong paragraph.** Outdated guidance in the index, or a paragraph that is close but not quite relevant, will be returned with confidence. Keep the index current and always read the source.

## The bottom line

The excise return is the one report where every number is checked by someone outside the business. That makes it the best place to stop copying figures by hand. Write the return's rules down as a data contract, test them every night, and month-end becomes a review instead of a hunt. Use GenAI where the mess is text, sorting notes and drafting explanations, and keep the figures and the signature with people and tested code.

Next, and last, in the series: [where winery AI breaks]({{ '/2026/where-winery-ai-breaks-ten-vintages-ten-rows/' | relative_url }}), and why ten vintages is only ten rows. The full list is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**What is a data contract in a winery context?**
It is a written, enforced agreement about what a dataset must contain. For excise, the contract on the movement ledger might say every removal has a tax class, a destination type and a measured alcohol, and every month's opening balance equals the previous month's closing. The pipeline tests those rules and stops bad records before they reach the return.

**Can an LLM fill in a wine excise return?**
It should not fill in the numbers. The figures come from tested queries over the ledger. An LLM is useful around the return: classifying free-text removal notes into categories, drafting the explanation for an unusual loss, and finding the relevant guidance paragraph for a person to read. A named person reviews and signs every return.

**Why do wine tax classes cause reconciliation problems?**
Because a lot can change class without leaving the building. In the US, for example, still wine is taxed in bands by alcohol, with a line at 16 percent. Blending, fortification or a corrected lab result can move a lot across that line, and if the change is not recorded as an event, the per-class balance stops adding up.
