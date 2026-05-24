---
layout: post
title: "An Account-Churn Dashboard in Tableau"
image: /assets/og/tableau-account-churn-dashboard.png
description: "Build an account-churn dashboard in Tableau with RFM recency and frequency measures, at-risk flags, and an ML churn score fed from TabPy for beverage sales."
date: 2023-08-21
updated: 2023-08-21
tags: [sales-intelligence, tableau, analytics]
faq:
  - q: "How do you flag at-risk accounts in Tableau?"
    a: "Compute recency and frequency per account with calculated fields and LOD expressions, then flag accounts whose recency has stretched well beyond their normal ordering rhythm. It is a simple, explainable rule that catches most slipping accounts."
  - q: "Can Tableau run a churn prediction model?"
    a: "Not natively, but you can call an external model through TabPy and return a churn probability per account as a field. Tableau then visualises and monitors the score; the model itself is trained and maintained outside Tableau."
  - q: "Why is churn hard to define in a three-tier market?"
    a: "When you sell through distributors, you often cannot see the end account's ordering directly, and a quiet account may be buying through another route. The churn signal is fuzzy and lagging, so treat flags as prompts to investigate, not confirmed losses."
---

**Short answer: an account-churn dashboard works when you start with explainable RFM-style recency and frequency flags, then optionally layer an ML score from TabPy — while staying honest that churn is fuzzy and lagging in a three-tier world.** Begin with the signal you can defend.

## Measure first: recency and frequency
Before any model, define the signal in plain measures. Recency is days since an account's last order; frequency is its order count or cadence over a window. Compute both per account with a FIXED LOD expression — `{ FIXED [Account ID] : MAX([Order Date]) }` gives a clean last-order date that a date diff turns into recency, regardless of the view's filters. Add a monetary measure (trailing revenue) and you have a full RFM frame.

The power of RFM is that it is explainable. An at-risk flag built from "recency has stretched well past this account's normal gap between orders" is a rule a sales manager can understand, trust and act on. Build that flag as a calculated field comparing current recency to the account's own historical cadence, so a fortnightly buyer and a quarterly buyer are each judged against their own rhythm rather than a single blanket threshold. This explainable baseline should ship first; the model comes later, if at all.

## Layering the ML score and alerts
Once the RFM view is solid, you can add predictive lift through TabPy. Train a churn model outside Tableau — on order history, payment behaviour, support tickets, whatever you have — and call it via a TabPy script that returns a churn probability per account. Tableau receives that probability as a field and visualises it alongside the RFM flags. The two views reinforce each other: where the explainable flag and the model agree, confidence is high; where they disagree, you have found an account worth a human look. The modelling detail behind that score lives in [account-churn prediction for beverage]({{ '/2026/account-churn-prediction-beverage/' | relative_url }}); the dashboard is the surface that puts it in front of reps.

Plot accounts on a recency-versus-frequency scatter, size by revenue and colour by churn score, and the high-value, high-risk corner becomes the call list for the week. Publish to Tableau Cloud and let Tableau Pulse monitor the at-risk count and score so reps get a natural-language alert when a key account drifts. Pair Pulse with row-level security via user filters so each rep sees only their own accounts — alerts are useful only when they reach the right person.

## Where it breaks
The honest limit is that churn is genuinely fuzzy in a three-tier market. If you sell through distributors, you may not see the end account's orders at all; an account that looks dormant might be buying through a different route, and one that looks healthy might be running down old stock. Your recency signal is then measuring your visibility, not their loyalty. The dashboard will flag confidently on data that is structurally incomplete.

The second limit is lag. By the time recency has stretched far enough to trip a flag, the account may already be gone — the signal trails the decision. An ML score helps by reading subtler early signals, but it is only as current as its training data and its feature pipeline; a model fed stale features quietly decays. And no model resolves the visibility gap above. Treat every flag and score as a prompt to pick up the phone and confirm, not as a settled verdict on the relationship.

## The bottom line
Anchor the dashboard in explainable RFM recency and frequency flags judged against each account's own cadence, then layer a TabPy churn score where it adds lift and let Pulse alert the right rep. But keep your eyes open: in a three-tier market the churn signal is incomplete and lagging, so the dashboard's job is to start the conversation, not to declare the account lost.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.* Related: [account-churn prediction for beverage]({{ '/2026/account-churn-prediction-beverage/' | relative_url }}).

## Frequently asked questions

**How do you flag at-risk accounts in Tableau?**
Compute recency and frequency per account with calculated fields and LOD expressions, then flag accounts whose recency has stretched well beyond their normal ordering rhythm. It is a simple, explainable rule that catches most slipping accounts.

**Can Tableau run a churn prediction model?**
Not natively, but you can call an external model through TabPy and return a churn probability per account as a field. Tableau then visualises and monitors the score; the model itself is trained and maintained outside Tableau.

**Why is churn hard to define in a three-tier market?**
When you sell through distributors, you often cannot see the end account's ordering directly, and a quiet account may be buying through another route. The churn signal is fuzzy and lagging, so treat flags as prompts to investigate, not confirmed losses.
