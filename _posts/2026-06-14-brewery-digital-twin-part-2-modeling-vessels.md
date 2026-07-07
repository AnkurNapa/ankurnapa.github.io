---
layout: post
title: "Modeling a Brewery in 3D: Procedural Vessels and Process Flow (Part 2)"
image: /assets/og/brewery-digital-twin-part-2-modeling-vessels.png
description: "Part 2 of building a brewery digital twin: how I modeled every vessel — mash tun, lauter tun, kettle, cylindro-conical fermenters — from code instead of Blender, drove the whole plant from one process-data file, and animated the flow between tanks. With an honest take on when Blender is the right call."
date: 2026-06-14 11:00:00 -0700
updated: 2026-06-14
tags: [digital-twin, microsoft-fabric, threejs, data-visualization, brewing]
faq:
  - q: "Do you need Blender to model a brewery in 3D?"
    a: "No. Brewhouse vessels are mostly cylinders, cones and domes, so they can be built procedurally in code with React Three Fiber and Three.js primitives. That keeps the bundle tiny, removes the asset pipeline, and means the geometry is driven by data instead of files. Blender earns its place when you need organic shapes, branded detail, or photoreal materials that primitives can't express — then you export glTF and load it. For a process twin where clarity beats realism, procedural wins."
  - q: "How do you make different tanks look like different vessels?"
    a: "Function-specific detail. A mash tun gets an agitator gearbox on top, a lauter tun gets a rake drive bridge, a kettle gets a tall vapor stack, fermenters are cylindro-conical on legs with glycol bands. I encoded these as a 'topper' field on each vessel so the geometry maps to what the vessel actually does — you can read the brewhouse at a glance without labels."
  - q: "How is the flow between vessels animated?"
    a: "Each connection is an edge in a data file with a 'from', a 'to' and what's flowing (hot liquor, mash, wort, beer). The 3D layer draws a pipe between the two vessel positions and runs small particles along it, colored by content, using the render loop to interpolate their position. It reads as product physically moving through the plant, and adding a new pipe is one line of data, not new geometry."
  - q: "Why drive everything from a single data file?"
    a: "Because a digital twin is only maintainable if the model is the source of truth. One file lists every vessel — id, name, position, size, content, topper — and every flow edge. The scene, the labels, the flow animation and the charts all read from it. Change the plant in one place and the whole twin updates, which is what separates a maintainable twin from a hand-placed 3D scene that rots."
---

**Short answer: every vessel in the brewery twin — mash tun, lauter tun, kettle, whirlpool, the cylindro-conical fermenters, the bright tanks — was modeled in code with React Three Fiber, not sculpted in Blender. Brewhouse equipment is mostly cylinders, cones and domes, so procedural geometry keeps the bundle tiny, kills the asset pipeline, and makes the geometry data-driven. The real trick isn't the meshes; it's that one file describes the whole plant — every vessel and every flow edge — and the scene, labels, flowing pipes and charts all read from it. Model once, render everywhere. And yes, there's a clear line where Blender becomes the right tool — I'll draw it honestly at the end.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From primitives to a living plant: procedural geometry (cylinders, cones, domes plus function toppers) and one process-data file of vessels and flow edges feed a React Three Fiber scene that renders vessels, animates product flow, and draws per-vessel charts."><rect width="1000" height="320" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">MODEL ONCE, RENDER EVERYWHERE</text><g font-family="sans-serif"><rect x="40" y="56" width="290" height="216" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="185" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">PROCEDURAL GEOMETRY</text><text x="185" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">no Blender, no files</text><text x="185" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">cylinders · cones · domes</text><text x="185" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">legs, cladding, hoop bands</text><text x="185" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">toppers: agitator · rake · stack</text><text x="185" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">tiny bundle, instant load</text><text x="185" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">shape from code</text><rect x="355" y="56" width="290" height="216" rx="10" fill="#06483f"/><text x="500" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#ffffff">ONE PROCESS-DATA FILE</text><text x="500" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#f3c6d3">the source of truth</text><text x="500" y="134" text-anchor="middle" font-size="11" fill="#cfe6df">vessels: id, pos, size</text><text x="500" y="158" text-anchor="middle" font-size="11" fill="#cfe6df">content &amp; topper per vessel</text><text x="500" y="182" text-anchor="middle" font-size="11" fill="#cfe6df">flow edges: from &#8594; to</text><text x="500" y="206" text-anchor="middle" font-size="11" fill="#cfe6df">change plant in one place</text><text x="500" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">data drives it all</text><rect x="670" y="56" width="290" height="216" rx="10" fill="#ffffff" stroke="#06483f" stroke-width="1.5"/><text x="815" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">THE LIVING SCENE</text><text x="815" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">React Three Fiber</text><text x="815" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">renders every vessel</text><text x="815" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">flow particles by content</text><text x="815" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">click → per-vessel chart</text><text x="815" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">labels &amp; status from data</text><text x="815" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">a plant you read</text></g><text x="500" y="300" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">the file in the middle is the twin — geometry and scene are just how it's expressed</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Geometry from code, plant from data, scene from both. Edit one file and the whole twin moves with it.</figcaption>
</figure>

This is Part 2 of the series. [Part 1]({{ '/2026/brewery-3d-digital-twin-microsoft-fabric/' | relative_url }}) covered the why and the scaffolding — getting a Fabric-hosted app live in an afternoon with the Rayfin SDK. Here we build the thing people actually look at: the vessels, and the flow between them.

## The decision: code the vessels, don't sculpt them

The series teaser said "model the vessels in Blender," and that's the instinct everyone has. But look at a brewhouse honestly: a mash tun is a cylinder with a domed top and a motor on it. A fermenter is a cylinder with a cone welded underneath. A kettle is a cylinder with a chimney. These are *primitives* — and Three.js gives you primitives for free.

So I went procedural. Every vessel is built from `cylinderGeometry`, `coneGeometry` and a half-`sphereGeometry` dome, assembled in React Three Fiber. The payoff is concrete:

- **No asset pipeline** — no exporting glTF, no texture files, no draco compression, nothing to keep in sync with the code.
- **A tiny bundle** — the heavy part of the app is the Three.js library itself, not the models, which matters because the whole thing ships as static assets to Microsoft Fabric.
- **Geometry that's data-driven** — a vessel's size and shape come from numbers, so the same component renders a squat lauter tun and a tall HLT just by changing arguments.

## Making each vessel look like itself

A brewery where every tank is an identical silver cylinder is useless — you can't read it. The fix is **function-specific detail**: the parts that tell a brewer what they're looking at.

- **Mash tun** → an agitator gearbox and drive motor on top.
- **Lauter tun** → a rake-drive bridge across the vessel.
- **Kettle** → a tall vapor stack and condenser.
- **Whirlpool** → a short stack with a tangential inlet pipe.
- **Fermenters** → cylindro-conical, standing on legs, wrapped in glycol-jacket bands.
- **Bright tanks** → pressure-domed and slimmer.

I encoded these as a `topper` on each vessel, so the geometry follows the *function*. Add legs, insulated cladding and hoop bands to the tanks, and the brewhouse becomes legible at a glance — you can find the kettle by its stack before you ever read a label.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-overview.png' | relative_url }}" alt="The brewhouse rendered from primitives: each tank carries function-specific detail — agitator, rake drive, kettle stack, cylindro-conical fermenters on legs — so vessels are distinguishable at a glance." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">All of this is cylinders, cones and domes from code — the toppers and proportions are what make each vessel readable.</figcaption>
</figure>

## The real trick: one file describes the whole plant

Here's the part that separates a maintainable twin from a 3D scene that rots. There's a single process-data file. It lists every vessel — id, display name, position on the floor, radius, height, what it holds, and its topper — and every **flow edge**: a `from` vessel, a `to` vessel, and what's flowing between them (hot liquor, grist, mash, wort, beer).

Everything reads from that file:

- the **scene** places each vessel at its position,
- the **labels** and status rings come from the same records,
- the **pipes** are drawn between the `from` and `to` positions of each edge,
- even the **per-vessel charts** key off the vessel id.

Move a tank, rename it, or add a new transfer line, and you edit *data*, not geometry. The model is the source of truth; the 3D is just one way of expressing it. (The other expression — the live numbers — comes in Part 3.)

## Animating the flow

A static plant is a diagram. What makes it a *twin* is seeing product move. For each flow edge, the scene draws a thin pipe between the two vessels and runs a few small particles along it, **colored by content** — amber for mash, gold for wort, copper for beer, blue for cold liquor. The render loop interpolates each particle's position from `from` to `to` and loops it.

Because flow is data, adding a transfer — say, a new line from a bright tank to a fourth tap — is one entry in the edges list. No new mesh, no manual placement. The pipe and its moving product appear automatically.

## Per-vessel charts that match the process

When you click a vessel you don't get a generic gauge — you get the chart that vessel deserves: a **step-temperature mash profile** for the mash tun, **run-off flow** for the lauter, a **falling-gravity-and-rising-ABV** curve for a fermenter, **carbonation** for a bright tank. These are lightweight hand-drawn SVG line charts rather than a charting library, for the same reason the geometry is procedural — keep the payload small and the control total. Each chart is just a function of the vessel id, so the right curve appears for the right tank.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-mash-profile.png' | relative_url }}" alt="The mash tun selected, with a step-temperature mash profile chart showing protein rest, saccharification rest and mash-out ramps." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Mash tun selected: a step-temperature profile — protein rest, saccharification, mash-out — not a generic gauge.</figcaption>
</figure>

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-fermentation.png' | relative_url }}" alt="A fermenter selected, showing a fermentation curve with specific gravity falling and ABV rising over time." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Fermenter selected: gravity falls as ABV climbs — the chart that vessel actually deserves.</figcaption>
</figure>

## Where this breaks

The honest limits, because "just code it" isn't always right. **Procedural geometry has a ceiling** — it's perfect for cylinders, cones and domes, but the moment you want a branded, organic, or photoreal asset (a sculpted logo, a realistic forklift, a textured brick wall), primitives fight you and **Blender plus a glTF export is the correct tool**; the decision rule is realism-and-uniqueness versus clarity-and-weight. **Detail costs frames** — every leg, band and topper is more meshes to draw, so on a big plant you'll want instancing or merged geometry before the frame rate suffers, and I haven't needed that yet but a 200-vessel site would. **A clean model can still lie** — geometry that looks right tells you nothing about whether it's wired to real data; a beautiful twin on fake numbers is a screensaver, which is exactly the gap Part 3 closes. And **"data-driven" is only true if you're disciplined** — the second someone hard-codes a position in the scene instead of the data file, the single-source-of-truth promise quietly breaks.

## The bottom line

Don't reach for Blender because modeling "should" happen there. Look at what you're modeling: a brewhouse is primitives, so code the vessels, give each one the detail that signals its function, and — most importantly — drive the entire plant from one process-data file so the scene, the flow and the charts all move when you edit it. Reserve Blender for the shapes primitives genuinely can't express. The geometry is the easy part; the discipline of one source of truth is what makes a twin you can actually maintain. Next up, [Part 3]: connecting it to real-time data and plain-language voice, so the twin stops simulating and starts reporting.

## Frequently asked questions

**Do you need Blender to model a brewery in 3D?**
No. Brewhouse vessels are mostly cylinders, cones and domes, so they can be built procedurally in code with React Three Fiber and Three.js primitives. That keeps the bundle tiny, removes the asset pipeline, and means the geometry is driven by data instead of files. Blender earns its place when you need organic shapes, branded detail, or photoreal materials that primitives can't express — then you export glTF and load it. For a process twin where clarity beats realism, procedural wins.

**How do you make different tanks look like different vessels?**
Function-specific detail. A mash tun gets an agitator gearbox on top, a lauter tun gets a rake drive bridge, a kettle gets a tall vapor stack, fermenters are cylindro-conical on legs with glycol bands. I encoded these as a "topper" field on each vessel so the geometry maps to what the vessel actually does — you can read the brewhouse at a glance without labels.

**How is the flow between vessels animated?**
Each connection is an edge in a data file with a "from", a "to" and what's flowing (hot liquor, mash, wort, beer). The 3D layer draws a pipe between the two vessel positions and runs small particles along it, colored by content, using the render loop to interpolate their position. It reads as product physically moving through the plant, and adding a new pipe is one line of data, not new geometry.

**Why drive everything from a single data file?**
Because a digital twin is only maintainable if the model is the source of truth. One file lists every vessel — id, name, position, size, content, topper — and every flow edge. The scene, the labels, the flow animation and the charts all read from it. Change the plant in one place and the whole twin updates, which is what separates a maintainable twin from a hand-placed 3D scene that rots.
