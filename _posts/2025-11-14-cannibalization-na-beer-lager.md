---
layout: post
title: "Cannibalization: Does Non-Alcoholic Beer Eat Your Lager's Sales?"
image: /assets/og/cannibalization-na-beer-lager.png
description: "A framework for measuring cannibalization between non-alcoholic beer and conventional lager — and how to separate cannibalised volume from genuine category expansion."
date: 2025-11-14
updated: 2025-11-14
tags: [forecasting, cannibalization-analysis]
faq:
  - q: "What is cannibalization in beverage demand forecasting?"
    a: "Cannibalization occurs when a new product in a portfolio draws sales from an existing product rather than attracting incremental buyers or occasions. In the beer context, the question is whether NA beer drinkers are replacing conventional lager purchases or adding new drinking occasions."
  - q: "Does non-alcoholic beer genuinely cannibalise conventional lager?"
    a: "The evidence across markets is mixed and highly brand-dependent. Some research suggests NA beer is primarily an incremental occasion product — bought for specific situations where alcohol is unsuitable — while other data shows meaningful switching behaviour, particularly among health-conscious frequent lager drinkers. A brand-level analysis is more informative than a category generalisation."
  - q: "How do you measure cannibalization rate in a beer portfolio?"
    a: "The standard approach is a controlled market or test-and-learn design: track conventional lager volume in markets or accounts where NA is newly introduced versus matched control markets where NA is not yet distributed. The difference in lager performance across these groups, controlling for seasonality and other factors, provides a cannibalization rate estimate."
---

**Short answer:** Non-alcoholic beer's impact on conventional lager is one of the most commercially consequential questions facing beer portfolio managers today, and the honest answer is: it depends significantly on the brand, the distribution channel, and the consumer segment. Building a measurement framework is more valuable than relying on category generalisations — the variance across brand portfolios is wide enough to make generic claims misleading.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Cannibalization: Does Non-Alcoholic Beer Eat Your Lager&#39;s Sales?</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">change the floor</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## Why Cannibalization Analysis Is Not Optional

When a major brewer introduces an NA variant of its flagship lager, the financial model almost certainly assumes the new SKU will be additive — capturing new occasions and new buyers without meaningfully reducing conventional lager sales. That assumption is almost never tested rigorously at launch.

If the assumption is wrong, the commercial arithmetic changes substantially. A NA SKU that generates $X in incremental revenue but displaces 0.7X of conventional lager revenue is creating $0.3X of net value — and that net figure must be weighed against the additional supply complexity, packaging investment, and shelf space trade-offs the new SKU requires.

The analysis is uncomfortable, which is precisely why it is avoided. Bringing it into the forecasting process is a mark of commercial maturity.

---

## The Incremental Occasion Hypothesis

The optimistic view of NA beer — and the one most commonly cited in category growth narratives — is that it serves fundamentally different occasions than conventional beer. The designated driver, the weeknight recovery occasion, the midday social setting, the health-conscious moderation moment: these are times when many conventional beer drinkers would not have purchased alcohol regardless. NA beer captures a previously unserved moment.

If the incremental occasion hypothesis is correct, the cannibalization rate is close to zero and the NA SKU is genuinely additive to portfolio volume. Distribution of NA adds accounts and occasions; conventional lager velocity in existing accounts is unaffected.

Supporting this hypothesis: the fact that NA beer's fastest growth appears to be in occasions and dayparts where conventional beer was historically absent or marginal.

---

## The Switching Behaviour Risk

The pessimistic view — backed by at least some scanner data and consumer panel evidence in more mature NA markets — is that a meaningful share of NA beer volume comes from consumers who were previously buying conventional lager and have shifted their occasion allocation. This is particularly plausible for brand-loyal drinkers of a flagship lager who now occasionally choose the NA variant of the same brand.

For these buyers, each NA purchase is a direct substitution. The within-brand switching rate — the share of NA volume purchased by existing conventional lager buyers — is the key metric to track. Consumer panels or loyalty card data, where available, provide the cleanest signal.

The within-brand switching story is distinct from cross-brand cannibalisation (where an NA launch by one brewer takes volume from a competitor's conventional products) — a more complex and generally smaller effect.

---

## A Measurement Framework

A practical cannibalization measurement approach for a brewery with reasonable depletion data:

1. **Define the test and control markets.** When introducing NA beer to new distribution accounts or regions, identify matched accounts or regions where the launch is not yet happening. These serve as controls.

2. **Track conventional lager velocity in both groups.** Velocity (volume per point of distribution) isolates the performance effect from the distribution effect. If conventional lager velocity declines in the accounts where NA has been added but holds steady in control accounts, cannibalization is present.

3. **Measure over a sufficient time window.** Initial launch periods often show conventional lager holding steady because NA is drawing trial buyers. The cannibalization signal, if present, may take six to twelve months to become visible as buying patterns stabilise.

4. **Estimate the rate and net value.** A 5% velocity decline on conventional lager in accounts where NA is distributed, against a baseline velocity of X cases per account, provides a dollar-denominated cannibalization estimate that can be weighed against NA's incremental contribution.

For the supply planning implications of cannibalization estimates, see [Hierarchical Forecasting: Reconciling SKU, Brand, and Total Volume]({{ '/2025/hierarchical-forecasting-beverage/' | relative_url }}) — the net portfolio volume after cannibalization is the number that must feed capacity planning, not the gross NA volume in isolation.

---

## Promotions as an Accelerant

Promotional mechanics can amplify or mask cannibalization effects. A price promotion on the NA variant that drives heavy trial from conventional lager buyers creates an apparent cannibalization signal in the data that may not persist at full price. Conversely, a conventional lager promotion can temporarily suppress the NA cannibalization rate by pulling conventional buyers back.

Promotional lift analysis across the portfolio — covered in [Promotional Lift: Separating Real Demand from Discount Noise]({{ '/2025/promotional-lift-forecasting/' | relative_url }}) — should always isolate promoted periods before drawing cannibalization conclusions.

---

## The Honest Caveat

Cannibalization is politically sensitive inside beverage organisations. Commercial teams with NA sales targets have incentives to understate it; conventional brand managers have incentives to overstate it. A measurement process that is designed by finance or supply chain — with commercial inputs but without commercial control over the methodology — produces more credible outputs than one that sits entirely within a single brand team.

The data requirements are also real: scanner data, consumer panels, or carefully matched test-and-control markets. Most regional and craft breweries will not have access to the scanner data that large national brewers use. In that case, honest qualitative assessment of the consumer overlap — informed by customer conversations and distributor feedback — is preferable to a spurious quantitative model built on insufficient data.

*Part of the Sales Forecasting track — [browse all]({{ '/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Each stage loses some — the funnel shows where the drop-off is."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Cannibalization: Does Non-Alcoholic Beer Eat Your Lager&#39;s Sales?</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reach · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interest · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Trial · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Win · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each stage loses some — the funnel shows where the drop-off is.</figcaption>
</figure>

## Frequently asked questions

**What is cannibalization in beverage demand forecasting?**  
Cannibalization occurs when a new product in a portfolio draws sales from an existing product rather than attracting incremental buyers or occasions. In the beer context, the question is whether NA beer drinkers are replacing conventional lager purchases or adding new drinking occasions.

**Does non-alcoholic beer genuinely cannibalise conventional lager?**  
The evidence across markets is mixed and highly brand-dependent. Some research suggests NA beer is primarily an incremental occasion product — bought for specific situations where alcohol is unsuitable — while other data shows meaningful switching behaviour, particularly among health-conscious frequent lager drinkers. A brand-level analysis is more informative than a category generalisation.

**How do you measure cannibalization rate in a beer portfolio?**  
The standard approach is a controlled market or test-and-learn design: track conventional lager volume in markets or accounts where NA is newly introduced versus matched control markets where NA is not yet distributed. The difference in lager performance across these groups, controlling for seasonality and other factors, provides a cannibalization rate estimate.
