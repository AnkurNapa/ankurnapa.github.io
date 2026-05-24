---
layout: post
title: "Cannibalization: Does Non-Alcoholic Beer Eat Your Lager's Sales?"
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

## Frequently asked questions

**What is cannibalization in beverage demand forecasting?**  
Cannibalization occurs when a new product in a portfolio draws sales from an existing product rather than attracting incremental buyers or occasions. In the beer context, the question is whether NA beer drinkers are replacing conventional lager purchases or adding new drinking occasions.

**Does non-alcoholic beer genuinely cannibalise conventional lager?**  
The evidence across markets is mixed and highly brand-dependent. Some research suggests NA beer is primarily an incremental occasion product — bought for specific situations where alcohol is unsuitable — while other data shows meaningful switching behaviour, particularly among health-conscious frequent lager drinkers. A brand-level analysis is more informative than a category generalisation.

**How do you measure cannibalization rate in a beer portfolio?**  
The standard approach is a controlled market or test-and-learn design: track conventional lager volume in markets or accounts where NA is newly introduced versus matched control markets where NA is not yet distributed. The difference in lager performance across these groups, controlling for seasonality and other factors, provides a cannibalization rate estimate.
