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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for An Account-Churn Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">An Account-Churn Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Measure first: recency and frequency
Before any model, define the signal in plain measures. Recency is days since an account's last order; frequency is its order count or cadence over a window. Compute both per account with a FIXED LOD expression — `{ FIXED [Account ID] : MAX([Order Date]) }` gives a clean last-order date that a date diff turns into recency, regardless of the view's filters. Add a monetary measure (trailing revenue) and you have a full RFM frame.

The power of RFM is that it is explainable. An at-risk flag built from "recency has stretched well past this account's normal gap between orders" is a rule a sales manager can understand, trust and act on. Build that flag as a calculated field comparing current recency to the account's own historical cadence, so a fortnightly buyer and a quarterly buyer are each judged against their own rhythm rather than a single blanket threshold. This explainable baseline should ship first; the model comes later, if at all.

## Layering the ML score and alerts
Once the RFM view is solid, you can add predictive lift through TabPy. Train a churn model outside Tableau — on order history, payment behaviour, support tickets, whatever you have — and call it via a TabPy script that returns a churn probability per account. Tableau receives that probability as a field and visualises it alongside the RFM flags. The two views reinforce each other: where the explainable flag and the model agree, confidence is high; where they disagree, you have found an account worth a human look. The modelling detail behind that score lives in [account-churn prediction for beverage]({{ '/2026/account-churn-prediction-beverage/' | relative_url }}); the dashboard is the surface that puts it in front of reps.

Plot accounts on a recency-versus-frequency scatter, size by revenue and colour by churn score, and the high-value, high-risk corner becomes the call list for the week. Publish to Tableau Cloud and let Tableau Pulse monitor the at-risk count and score so reps get a natural-language alert when a key account drifts. Pair Pulse with row-level security via user filters so each rep sees only their own accounts — alerts are useful only when they reach the right person.

## Where it breaks
The honest limit is that churn is genuinely fuzzy in a three-tier market. If you sell through distributors, you may not see the end account's orders at all; an account that looks dormant might be buying through a different route, and one that looks healthy might be running down old stock. Your recency signal is then measuring your visibility, not their loyalty. The dashboard will flag confidently on data that is structurally incomplete.

The second limit is lag. By the time recency has stretched far enough to trip a flag, the account may already be gone — the signal trails the decision. An ML score helps by reading subtler early signals, but it is only as current as its training data and its feature pipeline; a model fed stale features quietly decays. And no model resolves the visibility gap above. Treat every flag and score as a prompt to pick up the phone and confirm, not as a settled verdict on the relationship.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A single score ranks each account or sample at a glance."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">SCORE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">An Account-Churn Dashboard in Tableau</text><path d="M180,230 A180,180 0 0,1 280,72" fill="none" stroke="#06483f" stroke-width="22"/><path d="M280,72 A180,180 0 0,1 440,72" fill="none" stroke="#00695c" stroke-width="22"/><path d="M440,72 A180,180 0 0,1 540,230" fill="none" stroke="#2e9e7c" stroke-width="22"/><line x1="360" y1="230" x2="470" y2="120" stroke="#06483f" stroke-width="4"/><circle cx="360" cy="230" r="9" fill="#06483f"/><text x="360" y="180" text-anchor="middle" font-family="sans-serif" font-size="30" font-weight="700" fill="#06483f">72</text><text x="180" y="252" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#4a6b64">low</text><text x="540" y="252" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#4a6b64">high</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A single score ranks each account or sample at a glance.</figcaption>
</figure>

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
