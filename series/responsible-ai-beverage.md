---
layout: page
title: "Responsible AI for Beer, Whisky and Wine"
permalink: /series/responsible-ai-beverage/
description: "An 8-part series on Responsible AI for breweries, distilleries and wineries: the principles and a use-case register, GenAI marketing for an age-restricted product, recommenders with harm caps, food safety release gates, sensory bias and hallucinated tasting notes, provenance and synthetic labels, agent accountability and a playbook for small producers. By Ankur Napa."
---

Drinks is an odd industry to put AI into. The product is legal, loved and age-restricted. It is regulated for safety, taxed by the litre and faked by the case. A model that is fine for recommending shoes can do real harm when it recommends a fourth bottle of whisky to someone who already buys one a week.

This series is about the guardrails. Each part takes one Responsible AI principle and turns it into something you can build: a register table, a policy file, an eval set, a release gate, a ledger. The beer, whisky and wine examples are there to make the principle concrete. None of it is legal advice, and the regulatory dates are as they stood in September 2026.

## The series

1. **[What Responsible AI actually means for a drinks business]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }})**: six principles, the frameworks behind them, and a use-case register in SQL.
2. **[GenAI marketing for a product you cannot sell to minors]({{ '/2026/genai-alcohol-marketing-guardrails-age-codes/' | relative_url }})**: policy-as-code, a pre-publish classifier and a red-team eval set against the age codes.
3. **[Responsible recommenders]({{ '/2026/responsible-recommenders-harm-caps-consent/' | relative_url }})**: harm caps, consent-aware features and why the heaviest drinkers should not get the best offers.
4. **[When the model touches food safety]({{ '/2026/ai-food-safety-human-release-model-cards/' | relative_url }})**: flag-only release gates, abstain thresholds and model cards.
5. **[Whose palate did the model learn?]({{ '/2026/sensory-ai-bias-tasting-note-hallucination-evals/' | relative_url }})**: bias in sensory AI, and evals that catch hallucinated tasting notes.
6. **[Provenance, fakes and synthetic labels]({{ '/2026/provenance-fakes-c2pa-traceability-whisky-wine/' | relative_url }})**: a hash-chained cask ledger, C2PA and label claims you can prove.
7. **[Accountability when an agent drafts the decision]({{ '/2026/agent-accountability-audit-logs-worker-monitoring/' | relative_url }})**: owners, audit logs, red teams and safety cameras that are not surveillance.
8. **[A Responsible AI playbook for a small beverage business]({{ '/2026/responsible-ai-playbook-small-beverage-business/' | relative_url }})**: the lightweight version of ISO/IEC 42001, a 90-day plan, and where it breaks.

Start with part 1: the register it builds is used by every later part. Every post is tagged [#rai-beverage]({{ '/tags/' | relative_url }}#rai-beverage). For the agents and plant-floor guardrails underneath parts 4 and 7, see [AI for Operational Excellence]({{ '/series/ai-operational-excellence/' | relative_url }}).
