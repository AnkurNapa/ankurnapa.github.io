---
layout: post
title: "Modeling a Maltery as a Digital Twin on Microsoft Fabric"
image: /assets/og/anbc-maltery-digital-twin-microsoft-fabric.png
description: "After the brewery, the maltery. A live 3D digital twin of the whole malting process — intake, steeping, germination, kilning, deculming, malt storage and dispatch — built on Microsoft Fabric with the Rayfin SDK, every vessel clickable for its real process curve."
date: 2026-06-14 12:00:00 -0700
updated: 2026-06-14
tags: [digital-twin, microsoft-fabric, malting, data-visualization, brewing]
faq:
  - q: "What are the main steps of the malting process?"
    a: "Five core stages turn raw barley into malt. Intake and cleaning receives, de-stones and grades the barley. Steeping raises grain moisture from roughly 12% to 45% in alternating wet and dry cycles to wake the grain. Germination lets the grain sprout under conditioned air for a few days, developing enzymes — this is where green malt forms. Kilning then dries and cures it with heated air, locking in colour and flavour and stopping growth. Finally deculming removes the rootlets and the finished malt goes to silos and dispatch."
  - q: "What is a germination-kilning vessel (GKV)?"
    a: "A GKV is a single circular vessel that performs both germination and kilning without moving the grain bed, common in modern maltings. Conditioned air is blown up through a perforated floor while a turner keeps the bed even; then the same vessel switches to heated air for kilning. Older plants split these into Saladin boxes for germination and separate kilns — the twin models the steps either way."
  - q: "Why build a maltery digital twin instead of a dashboard?"
    a: "Malting is a slow, sequential, condition-driven process: moisture, bed temperature and airflow over days, not instantaneous readings. A 3D twin keeps the geography of that flow — silo to steep to germination to kiln to malt store — so an operator sees where a batch physically is and what each vessel is doing, with the real curve (steep moisture uptake, germination growth, the kilning ramp) one click away. A grid of tiles loses that sequence."
  - q: "Is this the same stack as the brewery twin?"
    a: "Yes. It reuses the same engine — procedural React/Three.js geometry, one data file describing every asset and flow edge, and deployment to Microsoft Fabric via the Rayfin SDK as its own separate item. Only the model changed: malting vessels, malting flow, and malting-specific charts. That reuse is the point — model the process, keep the platform."
---

**Short answer: after the brewery twins, I built the step before beer even starts — a live 3D digital twin of a maltery on Microsoft Fabric. It models the whole malting process: barley intake and cleaning, six barley silos, four steep tanks, four germination vessels, two kilns with burner and heat recovery, deculming, malt silos and dispatch, plus the air, water, effluent and dust utilities that make it run. Click any vessel and you get the curve that stage actually lives by — steep moisture uptake, germination growth, the classic kilning ramp. Same engine as the brewery twins, same one-data-file architecture, same one-command deploy to Fabric — only the process changed.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 250" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The malting process as a flow: barley intake and cleaning, to barley silos, to steeping, to germination, to kilning, to deculming and malt storage, then dispatch — with steeping raising moisture, germination growing rootlets, and kilning drying and curing."><rect width="1000" height="250" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">BARLEY TO MALT — THE FLOW THE TWIN KEEPS</text><line x1="60" y1="120" x2="940" y2="120" stroke="#06483f" stroke-width="2"/><g font-family="sans-serif"><g><circle cx="110" cy="120" r="7" fill="#00695c"/><text x="110" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Intake</text><text x="110" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">clean · destone · grade</text></g><g><circle cx="250" cy="120" r="7" fill="#00695c"/><text x="250" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Barley silos</text><text x="250" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">storage</text></g><g><circle cx="400" cy="120" r="7" fill="#4dd0e1"/><text x="400" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Steeping</text><text x="400" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">12% → 45% moisture</text></g><g><circle cx="550" cy="120" r="7" fill="#2e9e7c"/><text x="550" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Germination</text><text x="550" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">green malt · enzymes</text></g><g><circle cx="700" cy="120" r="7" fill="#ff4081"/><text x="700" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Kilning</text><text x="700" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">dry &amp; cure to ~85°C</text></g><g><circle cx="850" cy="120" r="7" fill="#00695c"/><text x="850" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Malt &amp; dispatch</text><text x="850" y="146" text-anchor="middle" font-size="10" fill="#4a6b64">deculm · store · load</text></g></g><text x="500" y="210" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">a slow, sequential, condition-driven process — which is exactly why geography beats a grid of tiles</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Malting is five stages over days; the twin keeps them in order and in place.</figcaption>
</figure>

This follows the brewery digital twin work — [the craft twin]({{ '/2026/brewery-3d-digital-twin-microsoft-fabric/' | relative_url }}) and how its [vessels are modeled]({{ '/2026/brewery-digital-twin-part-2-modeling-vessels/' | relative_url }}). Same engine, one step upstream: this is where the grain becomes malt.

## The whole malthouse on one screen

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/maltery-twin-overview.png' | relative_url }}" alt="The ANBC maltery digital twin: barley silos and cleaning on the left, steep tanks, large round germination vessels, two kilns, malt silos and dispatch on the right, with utilities and a plant-zone index." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Intake → barley silos → steeping → germination → kilning → malt silos → dispatch, with air, water, effluent and dust utilities.</figcaption>
</figure>

Every asset is modeled and clickable, grouped into eight zones: **intake and cleaning** (pit, pre-cleaner, destoner, grader), **barley storage** (six silos), **steeping** (four conical steep tanks, steep-water tank, CO₂ extraction), **germination** (four vessels with turners), **kilning** (two kilns, burner, heat recovery), **malt handling and dispatch** (deculmer, four malt silos, bagging, bulk loadout), the **utilities** that make it run (air handling, chiller, water plant, ETP, dust cyclone), and the **buildings** (admin, QC lab, control room, gate). Product flows colour-coded between them — barley, steep water, green malt, finished malt, heat, air, CO₂, effluent and dust.

## Each stage shows the curve it lives by

A maltster doesn't think in instantaneous numbers; they think in curves over hours and days. So clicking a vessel gives you the one that matters for that stage.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/maltery-twin-steep.png' | relative_url }}" alt="A steep tank selected, showing the moisture-uptake curve climbing in wet and dry steps from about 12% to 45%." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Steeping: grain moisture climbs in wet/dry steps toward ~45% — the signal that the grain is ready to germinate.</figcaption>
</figure>

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/maltery-twin-kiln.png' | relative_url }}" alt="A kiln selected, showing the kilning temperature curve — free drying, the break, then the curing ramp to about 85 degrees — with moisture falling." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Kilning: the classic ramp — free drying, the break, then curing to ~85 °C — with grain moisture dropping to a few percent.</figcaption>
</figure>

Steep tanks show **moisture uptake**; germination vessels show **bed temperature and rootlet growth**; kilns show the **kilning ramp** (free drying → break → curing) with moisture falling; silos show level; the cleaning and bagging machines show throughput; heat recovery shows efficiency. Each chart is just a function of the asset's id — the right curve appears for the right vessel.

## Same engine, one step upstream

The honest reason this took an afternoon and not a month: nothing about the platform changed. It's the same architecture as the brewery twins — procedural React and Three.js geometry, a single data file that lists every asset (id, position, size, content, topper) and every flow edge, and deployment to **Microsoft Fabric** via the **Rayfin SDK**. The maltery is its own separate Fabric item; deploying it created a brand-new app and didn't touch the brewery twins. I only rewrote the *model*: malting vessels, malting flow, malting charts. Model the process; keep the platform.

## Where this breaks

The honest caveats. **The data is simulated** — moisture, bed temperature and the kilning ramp are believable curves, not your plant's instruments; the architecture has one data seam a real Fabric model replaces, but today the numbers are illustrative. **Germination and kilning are simplified shapes** — the vessels render as large round forms, which reads correctly as "big circular bed" but isn't a faithful Saladin-box or GKV internal; for a true operator tool the perforated floor, turner geometry and air ducting would matter. **Malting is mostly invisible to the eye** — the real action is moisture and enzymes inside a grain bed, so a twin must lean on the *charts* to tell the story the geometry can't. And **a twin wired to nothing is a diagram** — the value only arrives when these vessels carry real moisture, temperature and airflow tags.

## The bottom line

Malting is the quiet first half of beer, and it's a textbook case for a digital twin: slow, sequential, and driven by conditions you can't see by looking. Keep the flow — barley to steep to germination to kiln to malt store — so the data lands where it happens, and let each stage surface the curve it actually lives by. Then let Microsoft Fabric carry the hosting, auth and data so the work goes into the model, not the plumbing. Brewery, plant, and now maltery — three twins, one engine, grain to glass.

## Frequently asked questions

**What are the main steps of the malting process?**
Five core stages turn raw barley into malt. Intake and cleaning receives, de-stones and grades the barley. Steeping raises grain moisture from roughly 12% to 45% in alternating wet and dry cycles to wake the grain. Germination lets the grain sprout under conditioned air for a few days, developing enzymes — this is where green malt forms. Kilning then dries and cures it with heated air, locking in colour and flavour and stopping growth. Finally deculming removes the rootlets and the finished malt goes to silos and dispatch.

**What is a germination-kilning vessel (GKV)?**
A GKV is a single circular vessel that performs both germination and kilning without moving the grain bed, common in modern maltings. Conditioned air is blown up through a perforated floor while a turner keeps the bed even; then the same vessel switches to heated air for kilning. Older plants split these into Saladin boxes for germination and separate kilns — the twin models the steps either way.

**Why build a maltery digital twin instead of a dashboard?**
Malting is a slow, sequential, condition-driven process: moisture, bed temperature and airflow over days, not instantaneous readings. A 3D twin keeps the geography of that flow — silo to steep to germination to kiln to malt store — so an operator sees where a batch physically is and what each vessel is doing, with the real curve (steep moisture uptake, germination growth, the kilning ramp) one click away. A grid of tiles loses that sequence.

**Is this the same stack as the brewery twin?**
Yes. It reuses the same engine — procedural React/Three.js geometry, one data file describing every asset and flow edge, and deployment to Microsoft Fabric via the Rayfin SDK as its own separate item. Only the model changed: malting vessels, malting flow, and malting-specific charts. That reuse is the point — model the process, keep the platform.
