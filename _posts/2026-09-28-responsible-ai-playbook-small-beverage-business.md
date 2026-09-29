---
layout: post
title: "A Responsible AI Playbook for a Small Beverage Business, and Where It Breaks"
image: /assets/og/responsible-ai-playbook-small-beverage-business.png
description: "Part 8 of Responsible AI for Beer, Whisky and Wine. A lightweight version of ISO/IEC 42001 for a craft brewery, small distillery or winery with no AI team: a use-case register, a one-page impact assessment, an eval harness, monitoring, an incident log and a quarterly review, mapped to the NIST AI RMF. Plus AI's own energy and water footprint against your ESG claims, the regulatory calendar as of September 2026, and a 90-day plan."
date: 2026-09-28 15:00:00 -0700
updated: 2026-09-28
tags: [brewing-science, rai-beverage, ai-governance, iso-42001, nist-ai-rmf]
faq:
  - q: "Does a small brewery, distillery or winery need ISO/IEC 42001 certification?"
    a: "Usually not. Certification is expensive and mostly useful when a customer or regulator asks for it. What a small business needs is the habits underneath the standard: a list of every AI use, a short impact assessment for each, tests before go-live, monitoring after it, a log of incidents and a quarterly review. That can run on a spreadsheet or a small database and a couple of hours a quarter."
  - q: "How does the NIST AI Risk Management Framework apply to a small beverage business?"
    a: "Its four functions map onto a simple routine. Govern is naming owners and writing the few rules you will hold. Map is the use-case register and the impact assessment. Measure is the eval set and the monitoring. Manage is the incident log, the quarterly review and the decision to change or retire a use. You do not need the full playbook of subcategories to get the value."
  - q: "What AI rules apply to beverage businesses in India and Europe as of September 2026?"
    a: "At the time of writing, the EU AI Act has been amended by the AI Omnibus, in force since 27 July 2026, which moved the main high-risk obligations to 2 December 2027 for Annex III uses and 2 August 2028 for Annex I products. Transparency duties under Article 50 are unchanged, with the machine-readable marking of AI-generated content applying from 2 December 2026. In India, the DPDP Rules phase in on 14 November 2026 and 14 May 2027, and the India AI Governance Guidelines of November 2025 are principles-based rather than a new law. This is a summary, not legal advice."
---

**Short answer: a small brewery, distillery or winery does not need an AI governance department. It needs six habits, the ones that sit underneath ISO/IEC 42001 with the paperwork stripped out. Keep a register of every place AI is used. Write a one-page impact assessment before anything goes live. Test it against a small set of cases you know the answers to. Watch it after launch. Log every incident, however small. And sit down once a quarter to decide what to keep, change or switch off. Map those to the NIST AI RMF functions (Govern, Map, Measure, Manage) and you have a defensible programme that one person can run in a few hours a quarter. The hard part is not the template. It is keeping the habit alive when the only person running it is also the head brewer.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A quarterly Responsible AI loop for a small beverage business, mapped to the NIST AI Risk Management Framework. Govern, at the centre, holds named owners and a short set of rules. Around it, four steps in a cycle: Map, with the use-case register and the one-page impact assessment; Measure, with the eval set and monitoring; Manage, with the incident log and the decision to keep, change or retire; and back to Map through a quarterly review. A side panel shows the regulatory calendar at the time of writing: EU AI Act Article 50 marking from 2 December 2026, India DPDP phases on 14 November 2026 and 14 May 2027, EU Annex III high-risk from 2 December 2027 and Annex I from 2 August 2028.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">SIX HABITS, ONE QUARTERLY LOOP</text>
<g font-family="sans-serif">
<rect x="250" y="140" width="200" height="90" rx="10" fill="#06483f"/>
<text x="350" y="168" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">GOVERN</text>
<text x="350" y="192" text-anchor="middle" font-size="10.5" fill="#cfe6df">named owners</text>
<text x="350" y="210" text-anchor="middle" font-size="10.5" fill="#cfe6df">a few written rules</text>
<rect x="40" y="50" width="220" height="76" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="150" y="74" text-anchor="middle" font-size="11" font-weight="700" fill="#00695c">MAP</text>
<text x="150" y="96" text-anchor="middle" font-size="10.5" fill="#06483f">1. use-case register</text>
<text x="150" y="114" text-anchor="middle" font-size="10.5" fill="#06483f">2. one-page impact assessment</text>
<rect x="440" y="50" width="220" height="76" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="550" y="74" text-anchor="middle" font-size="11" font-weight="700" fill="#00695c">MEASURE</text>
<text x="550" y="96" text-anchor="middle" font-size="10.5" fill="#06483f">3. eval set before go-live</text>
<text x="550" y="114" text-anchor="middle" font-size="10.5" fill="#06483f">4. monitoring after it</text>
<rect x="440" y="244" width="220" height="76" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="550" y="268" text-anchor="middle" font-size="11" font-weight="700" fill="#00695c">MANAGE</text>
<text x="550" y="290" text-anchor="middle" font-size="10.5" fill="#06483f">5. incident log</text>
<text x="550" y="308" text-anchor="middle" font-size="10.5" fill="#06483f">keep &#183; change &#183; retire</text>
<rect x="40" y="244" width="220" height="76" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="1.5"/>
<text x="150" y="268" text-anchor="middle" font-size="11" font-weight="700" fill="#2e9e7c">EVERY QUARTER</text>
<text x="150" y="290" text-anchor="middle" font-size="10.5" fill="#06483f">6. review, two hours,</text>
<text x="150" y="308" text-anchor="middle" font-size="10.5" fill="#06483f">one query, one decision each</text>
<path d="M260 88 L440 88" stroke="#4db6a2" stroke-width="2.5" fill="none"/>
<path d="M550 126 L550 244" stroke="#4db6a2" stroke-width="2.5" fill="none"/>
<path d="M440 282 L260 282" stroke="#4db6a2" stroke-width="2.5" fill="none"/>
<path d="M150 244 L150 126" stroke="#4db6a2" stroke-width="2.5" fill="none"/>
<rect x="700" y="50" width="270" height="270" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="76" text-anchor="middle" font-size="11" font-weight="700" fill="#00695c">CALENDAR, AS OF SEPT 2026</text>
<g font-size="10.5" fill="#06483f">
<text x="718" y="108" font-weight="700">14 Nov 2026</text>
<text x="718" y="124" fill="#4a6b64">India DPDP: Board powers, consent managers</text>
<text x="718" y="154" font-weight="700">2 Dec 2026</text>
<text x="718" y="170" fill="#4a6b64">EU Art. 50(2): mark AI-made content</text>
<text x="718" y="200" font-weight="700">14 May 2027</text>
<text x="718" y="216" fill="#4a6b64">India DPDP: remaining obligations</text>
<text x="718" y="246" font-weight="700">2 Dec 2027</text>
<text x="718" y="262" fill="#4a6b64">EU Annex III high-risk uses</text>
<text x="718" y="292" font-weight="700">2 Aug 2028</text>
<text x="718" y="308" fill="#4a6b64">EU Annex I regulated products</text>
</g>
<rect x="40" y="336" width="930" height="34" rx="10" fill="#06483f"/>
<text x="505" y="358" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">THE TEMPLATE IS EASY &#183; KEEPING THE HABIT IS THE WORK</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The six habits as one loop, mapped to the NIST AI RMF functions, with the dates worth putting in the diary. Dates are as of September 2026 and not legal advice.</figcaption>
</figure>

Every brewery I have known has a cleaning schedule on the wall. Nobody thinks of it as governance. It is just the list of what gets cleaned, how, how often and who signs it. Most of the time it is a laminated sheet with a column of initials and one coffee ring. It works because it is small enough to keep doing.

That is the bar for Responsible AI in a business with fifteen people and no data team. The previous seven posts in this series went deep on single risks: [the principles and the register]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}), [marketing to adults only]({{ '/2026/genai-alcohol-marketing-guardrails-age-codes/' | relative_url }}), [recommenders that do not push the heaviest drinkers]({{ '/2026/responsible-recommenders-harm-caps-consent/' | relative_url }}), [food safety]({{ '/2026/ai-food-safety-human-release-model-cards/' | relative_url }}), [sensory bias]({{ '/2026/sensory-ai-bias-tasting-note-hallucination-evals/' | relative_url }}), [provenance and fakes]({{ '/2026/provenance-fakes-c2pa-traceability-whisky-wine/' | relative_url }}) and [accountability for agents]({{ '/2026/agent-accountability-audit-logs-worker-monitoring/' | relative_url }}). This one pulls them into a routine that fits on the wall next to the cleaning schedule.

## Why not just get certified

ISO/IEC 42001, published in 2023, is the management-system standard for AI. It does for AI what ISO 9001 does for quality and ISO 22000 does for food safety: policies, roles, risk assessment, controls, internal audit, management review. It is a good standard. For a small brewery or a single-site distillery, certification is usually not worth it unless a large customer or an export market asks for it.

The value is in the habits underneath. A small business can take those, drop the certification paperwork, and get most of the protection. If a certificate is ever needed, the habits will already be there and the audit becomes a matter of formatting.

The NIST AI Risk Management Framework is the other useful reference. It is free, voluntary and organised around four functions: Govern, Map, Measure and Manage. I use its four words as the spine of the routine below, because they are easy to remember and they stop the routine drifting into all paperwork and no testing.

## Govern: two names and five rules

Govern sounds like the heaviest part. For a small business it is the lightest.

Name one person who owns the programme. In a craft brewery that might be the head brewer or the operations manager. In a winery, the winemaker or the general manager. Name a second person who looks at it once a quarter from outside, perhaps a co-founder, the finance lead, an advisor. One runs it, one checks it.

Then write down no more than five rules, the ones you will actually hold. Mine for a small beverage business would be:

1. Every AI use goes on the register before it goes live, including the free tools staff use for marketing copy.
2. Nothing AI-drafted reaches a customer, a regulator or a release decision without a named person approving it.
3. No customer or staff personal data goes into a tool we have not checked for where it stores data.
4. AI never sets or changes a process value: temperatures, dosing, cut points, release status.
5. Any incident, however small, gets one line in the log the same week.

Five rules fit on an A4 sheet by the office door. Twenty rules fit in a document nobody opens.

## Map: the register and the one-page impact assessment

[Part 1]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}) built the use-case register as a small table with a risk tier for each use. Keep it. That is the Map function's first half.

The second half is an impact assessment for anything above the lowest tier. The trick is to keep it to one page, so it gets written before launch rather than after an incident. Here is the template I would use. It is YAML so it can live in a folder next to the register, or be pasted into a form.

```yaml
# One-page AI impact assessment. Fill before go-live, review every quarter.
use_case_id: UC-07
name: GenAI drafts of taproom social posts
owner: Marketing lead (named person)
checker: Co-founder (named person)
risk_tier: medium          # from the register: low / medium / high
status: live               # proposed / pilot / live / retired

purpose: >
  Draft three social posts a week for new releases, for a person to edit and publish.
not_for: >
  Paid ads, age-gated targeting decisions, health or strength claims.

people_affected:
  - Followers, who must all be of legal drinking age
  - Staff whose photos may appear in images
data_used:
  personal_data: false
  sources: [release notes, tasting notes written by the brewer, brand guide]
  vendor_stores_prompts: checked   # yes / no / checked, with a link to the terms

what_could_go_wrong:
  - Copy that appeals to under-age audiences or implies drinking improves mood
  - Invented tasting notes or ABV that do not match the beer
  - AI-generated image of a person who looks under 25
controls:
  - Prompt includes the marketing code checklist from part 2
  - Every draft checked against the release sheet for ABV and style
  - No AI-generated people in images
  - AI-made images marked as such
evals:
  test_set: 20 past releases with known correct facts and 10 deliberately risky briefs
  pass_rule: zero factual errors on ABV and style; zero code breaches on risky briefs
  last_run: 2026-09-15
monitoring:
  signal: share of drafts edited for facts or tone, per month
  alarm: any published post later corrected; edit rate falls to zero (nobody reading)
footprint:
  model_calls_per_month: ~60
  note: negligible next to the brewhouse; recorded so ESG claims stay honest
decision: keep            # keep / change / retire, decided at quarterly review
review_due: 2026-12-31
```

Every field is there to force a question someone would otherwise skip. The `not_for` line matters as much as `purpose`, because most harm comes from a tool slowly being used for the job next door. `vendor_stores_prompts` makes someone actually read the terms. And an edit rate of zero is listed as an alarm, not a success, for the same reason the [accountability post]({{ '/2026/agent-accountability-audit-logs-worker-monitoring/' | relative_url }}) flagged approvals made in six seconds.

## Measure: a small eval set and one monitoring signal

Measure is where most small programmes quietly stop. It is also the part that does the most good.

Every live use needs a test set: twenty to fifty cases where you already know the right answer, including a few built to make it fail. For a tasting-note drafter, that is past beers with the brewer's own notes. For a sales forecast, last year's weeks held out. For an SOP question-answering bot in a distillery, thirty questions the stillman knows cold, including three whose answers are "that is not in the SOP, ask the shift lead". [Part 5]({{ '/2026/sensory-ai-bias-tasting-note-hallucination-evals/' | relative_url }}) showed what a hallucination eval looks like for tasting notes. Run the set before go-live and again whenever the model, the prompt or the data source changes.

Then pick one monitoring signal per use, the one that would move first if things went wrong. An edit rate, an override rate, a forecast error, the count of questions the bot refused. One number, tracked monthly, with a line where you stop and look. More numbers than that will not get looked at.

## Manage: the incident log and the quarterly review

Manage is where decisions happen. It needs two things.

An incident log: one line per event, the same week. An AI-drafted post that got the ABV wrong. A forecast that missed Diwali. A chatbot that told a taproom customer a beer was gluten-free when it was not. Most will be small. Log them anyway, because the pattern across ten small ones is what tells you a use needs changing. Same shape as the audit log in part 7: date, use case, what happened, who noticed, what was done, and a severity.

The quarterly review then takes two hours and one query. Here is the query, against a register table and an incident log with the obvious columns.

```sql
-- Quarterly Responsible AI review: one row per live use case,
-- with what the owner needs to decide keep / change / retire.
SELECT r.use_case_id,
       r.name,
       r.owner,
       r.risk_tier,
       r.last_eval_run,
       (r.last_eval_run < CURRENT_DATE - INTERVAL '90 days')      AS eval_overdue,
       r.last_eval_passed,
       COUNT(i.incident_id)                                        AS incidents_this_qtr,
       COUNT(i.incident_id) FILTER (WHERE i.severity IN ('high','medium'))
                                                                   AS serious_incidents,
       m.signal_name,
       m.value_this_qtr,
       m.alarm_threshold,
       (m.value_this_qtr > m.alarm_threshold)                      AS signal_in_alarm,
       (r.owner_left = TRUE)                                       AS owner_gone
FROM   ai_use_register r
LEFT   JOIN ai_incident_log i
       ON  i.use_case_id = r.use_case_id
       AND i.occurred_on >= date_trunc('quarter', CURRENT_DATE) - INTERVAL '3 months'
       AND i.occurred_on <  date_trunc('quarter', CURRENT_DATE)
LEFT   JOIN ai_monitoring_qtr m
       ON  m.use_case_id = r.use_case_id
       AND m.quarter_start = date_trunc('quarter', CURRENT_DATE) - INTERVAL '3 months'
WHERE  r.status IN ('pilot','live')
GROUP  BY r.use_case_id, r.name, r.owner, r.risk_tier, r.last_eval_run,
          r.last_eval_passed, m.signal_name, m.value_this_qtr,
          m.alarm_threshold, r.owner_left
ORDER  BY serious_incidents DESC, signal_in_alarm DESC, eval_overdue DESC;
```

Each row gets one decision: keep, change or retire. Any row with `owner_gone`, an overdue eval or a signal in alarm cannot be marked keep without a written reason. And "retire" is a respectable outcome. Switching off a tool that is not earning its keep is the most responsible thing a small business can do with AI, and it happens far less than it should.

This works on a spreadsheet too. The SQL is just the shape of the question.

## AI's own footprint against your ESG claims

Many small breweries, distilleries and wineries now publish something about sustainability: water per litre, energy per hectolitre, spent grain to farms, lighter bottles. If the same business adopts AI, the AI's own footprint belongs in the same honest ledger.

For most small users the footprint is genuinely small. A few thousand model calls a month for drafting and question answering is a rounding error next to a boil, a still run or a refrigeration plant. But "small" should be a number, not a feeling. Ask the vendor for per-request energy or emissions figures, or use a published estimate, and record it with the source. If you train or fine-tune your own models, or run image and video generation at volume, the numbers get bigger quickly and deserve their own line.

The honest failure to avoid is claiming AI savings without the AI's cost. "Our forecasting model cut waste by 8 percent" is a real claim only if the waste baseline is fair and the model's footprint sits in the same report. I went through how to check claims like this in [avoiding greenwashing: how to verify AI sustainability claims]({{ '/2026/avoiding-greenwashing-ai-verify/' | relative_url }}). The same test applies to your own.

## The calendar, as of September 2026

A small business does not need to track every consultation paper. It does need a handful of dates. At the time of writing, September 2026, these are the ones worth a diary entry. This is a summary to help you plan, not legal advice. Check the current position with a qualified adviser for your markets.

- **European Union.** The AI Act was amended by the AI Omnibus, which entered into force on 27 July 2026. The main obligations for high-risk AI moved to 2 December 2027 for the uses listed in Annex III and to 2 August 2028 for AI in the regulated products under Annex I. The Article 50 transparency duties were not changed. Machine-readable marking of AI-generated content under Article 50(2) applies from 2 December 2026, which matters to anyone generating marketing images or video. Most beverage uses will not be high-risk, but anything touching employment decisions or safety components deserves a closer look.
- **India.** The Digital Personal Data Protection Rules were notified on 14 November 2025 and come into force in phases. The Data Protection Board's enforcement powers and the consent manager framework start on 14 November 2026, and the remaining substantive obligations on 14 May 2027. If you hold loyalty data, taproom bookings, staff records or camera footage, this is the one to plan for.
- **India, AI specifically.** The India AI Governance Guidelines, released by MeitY on 5 November 2025, are principles-based, built around seven sutras including trust, people first, fairness and accountability, and rely on existing laws rather than creating a new AI statute. Nothing to file, but a good checklist.
- **Marketing codes.** Industry codes on alcohol marketing, covered in [part 2]({{ '/2026/genai-alcohol-marketing-guardrails-age-codes/' | relative_url }}), apply to AI-generated content exactly as they apply to anything else.

## A 90-day plan

For a brewery, distillery or winery starting from nothing:

**Days 1 to 30: Govern and Map.** Name the owner and the checker. Write the five rules. Walk the site and the laptops and list every AI use, including free tools staff use on their own phones for marketing, translation and emails. Tier each one. Write impact assessments for anything above low.

**Days 31 to 60: Measure.** Build a test set for each medium and high use. Twenty cases is fine to start. Run them. Fix or pause anything that fails. Pick one monitoring signal per use and set its alarm line. Check where each vendor stores your data.

**Days 61 to 90: Manage.** Start the incident log and tell staff what goes in it and that nobody gets in trouble for logging. Record the AI footprint estimate next to your other sustainability numbers. Hold the first quarterly review, make a keep, change or retire decision for every live use, and book the next one.

At the end you will have a register, a folder of one-page assessments, a few test sets, a handful of monitoring numbers, an incident log and a date in the diary. That is a Responsible AI programme. It is also, not by coincidence, most of what an ISO/IEC 42001 auditor would ask to see.

## Where this breaks

**Paperwork theatre.** The biggest risk is a folder of beautifully filled templates and no tests. Assessments are cheap to write and feel like progress. If the quarterly query shows evals overdue on half the register, the programme is theatre, whatever the folder looks like. Weight the review towards Measure.

**One-person governance.** In a small business the owner, the approver and the tester are often the same person, who is also brewing on Tuesday and doing the excise return on Friday. That person will be tempted to mark their own homework. The checker's quarterly look is the only defence, so protect it. If the checker has not looked for two quarters, you do not have governance, you have a hope.

**Shadow AI.** The tools that matter most are often the ones nobody registered: a salesperson pasting customer lists into a free chatbot, a marketing intern generating images on a personal account. Ask about it every quarter, without blame, or you will never hear about it.

**Rules that go stale.** Vendor terms change, models get swapped under the same product name, and regulatory dates move, as the EU dates did this year. Put "check vendor terms and the calendar" on the quarterly agenda.

**Treating retire as failure.** A programme where nothing is ever switched off is not being honest about what works.

## The bottom line

Responsible AI for a small beverage business is not a department or a certificate. It is six habits that fit on one wall: a register, a one-page impact assessment, a test set, one monitoring number, an incident log and a quarterly review with a decision for every use. Mapped to Govern, Map, Measure and Manage, it lines up with the NIST AI RMF and most of ISO/IEC 42001 without the overhead. Put the AI's own footprint in the same ledger as your water and energy, keep five dates in the diary, and be willing to switch things off. The template is the easy part. Like the cleaning schedule, what matters is that someone initials it every time.

That is the end of the series. Start again from [part 1, what Responsible AI actually means for a drinks business]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}), or see all eight parts on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**Does a small brewery, distillery or winery need ISO/IEC 42001 certification?**
Usually not. Certification is expensive and mostly useful when a customer or regulator asks for it. What a small business needs is the habits underneath the standard: a list of every AI use, a short impact assessment for each, tests before go-live, monitoring after it, a log of incidents and a quarterly review. That can run on a spreadsheet or a small database and a couple of hours a quarter.

**How does the NIST AI Risk Management Framework apply to a small beverage business?**
Its four functions map onto a simple routine. Govern is naming owners and writing the few rules you will hold. Map is the use-case register and the impact assessment. Measure is the eval set and the monitoring. Manage is the incident log, the quarterly review and the decision to change or retire a use. You do not need the full playbook of subcategories to get the value.

**What AI rules apply to beverage businesses in India and Europe as of September 2026?**
At the time of writing, the EU AI Act has been amended by the AI Omnibus, in force since 27 July 2026, which moved the main high-risk obligations to 2 December 2027 for Annex III uses and 2 August 2028 for Annex I products. Transparency duties under Article 50 are unchanged, with the machine-readable marking of AI-generated content applying from 2 December 2026. In India, the DPDP Rules phase in on 14 November 2026 and 14 May 2027, and the India AI Governance Guidelines of November 2025 are principles-based rather than a new law. This is a summary, not legal advice.
