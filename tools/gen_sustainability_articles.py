#!/usr/bin/env python3
"""
Generate a 20-article sustainability series for beer/whiskey/wine producers:
saving electricity, water and the environment using AI, data science and
generative AI (Claude, ChatGPT), with UK/EU/USA/India regulatory angles.

House format + two inline-SVG diagrams each. Spread across 2026.
Usage: python tools/gen_sustainability_articles.py --write
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent; POSTS=ROOT/"_posts"
BG="#fdfbf7"; INK="#1c1a17"; MUTED="#6b6258"; AMBER="#b45309"; PEACH="#f7ece0"
LINE="#e0d8cc"; WINE="#7a1f3d"; OAK="#8a5a2b"; OLIVE="#5b7a1f"
ACC=OLIVE; CHIP="#eef2e3"
FOOT=("ESG Analytics for Beverage","/tracks/esg/")


def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def L(text,url): return "["+text+"]({{ '"+url+"' | relative_url }})"
def figw(svg,cap,d2=False):
    m=' data-d2="1"' if d2 else ''
    return (f'<figure{m} style="margin:1.6rem 0;text-align:center">\n{svg}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(cap)}</figcaption>\n</figure>')


def steps_svg(title, steps, cap):
    n=len(steps); W=1000; bw=int((W-40-(n-1)*24)/n); by,bh=80,150; cy=by+bh//2
    p=[f'<rect x="0" y="0" width="{W}" height="270" fill="{BG}"/>',
       f'<text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    xs=[20+i*(bw+24) for i in range(n)]
    for i,(lab,sub) in enumerate(steps):
        x=xs[i]; cx=x+bw//2
        p.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="{CHIP}" stroke="{ACC}" stroke-width="1.5"/>')
        p.append(f'<circle cx="{cx}" cy="{by+34}" r="15" fill="{ACC}"/><text x="{cx}" y="{by+39}" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">{i+1}</text>')
        p.append(f'<text x="{cx}" y="{cy+18}" text-anchor="middle" font-size="13.5" font-weight="700" fill="{INK}">{esc(lab)}</text>')
        p.append(f'<text x="{cx}" y="{cy+40}" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(sub)}</text>')
    p.append('</g>')
    p.append(f'<g fill="{ACC}" stroke="{ACC}" stroke-width="2">')
    for i in range(n-1):
        r=xs[i]+bw; nl=xs[i+1]
        p.append(f'<line x1="{r}" y1="{cy}" x2="{nl-7}" y2="{cy}"/><polygon points="{nl-7},{cy-5} {nl},{cy} {nl-7},{cy+5}" stroke="none"/>')
    p.append('</g>')
    return figw(f'<svg viewBox="0 0 {W} 270" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap)


def pyramid_svg(title, tiers, cap):
    W=720; cx=360; p=[f'<rect x="0" y="0" width="{W}" height="300" fill="{BG}"/>',
       f'<text x="{cx}" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    widths=[150,270,400]; ytop=70; th=62; prev=64; cols=[ACC,OAK,CHIP]
    for i,(lab,desc) in enumerate(tiers):
        bw=widths[i]; tw=prev; y1=ytop+i*(th+6); y2=y1+th; fillc=cols[i]; tc="#fff" if fillc!=CHIP else INK
        p.append(f'<polygon points="{cx-tw/2},{y1} {cx+tw/2},{y1} {cx+bw/2},{y2} {cx-bw/2},{y2}" fill="{fillc}" stroke="{ACC}"/>')
        p.append(f'<text x="{cx}" y="{y1+28}" text-anchor="middle" font-size="13" font-weight="700" fill="{tc}">{esc(lab)}</text>')
        p.append(f'<text x="{cx}" y="{y1+46}" text-anchor="middle" font-size="11" fill="{tc}">{esc(desc)}</text>')
        prev=bw
    p.append('</g>')
    return figw(f'<svg viewBox="0 0 {W} 300" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap,d2=True)


def footprint_svg(title, cap):
    W=720; p=[f'<rect x="0" y="0" width="{W}" height="300" fill="{BG}"/>',
       f'<text x="360" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>']
    p.append(f'<rect x="280" y="70" width="120" height="40" fill="{OLIVE}"/><rect x="280" y="110" width="120" height="40" fill="{AMBER}"/><rect x="280" y="150" width="120" height="100" fill="{WINE}"/>')
    for lab,c,yy in [("Scope 1 — direct fuel & process",OLIVE,96),("Scope 2 — purchased energy",AMBER,136),("Scope 3 — packaging, transport, supply (largest)",WINE,200)]:
        p.append(f'<rect x="440" y="{yy-12}" width="14" height="14" fill="{c}"/><text x="462" y="{yy}" font-family="sans-serif" font-size="12.5" fill="{INK}">{esc(lab)}</text>')
    return figw(f'<svg viewBox="0 0 {W} 300" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap,d2=True)


def ladder_svg(title, phases, cap):
    W=1000; n=len(phases); p=[f'<rect x="0" y="0" width="{W}" height="360" fill="{BG}"/>',
       f'<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    bw=176; base=320; rise=46; xs=[16+i*(bw+10) for i in range(n)]
    for i,(name,lab) in enumerate(phases):
        x=xs[i]; top=base-(i+1)*rise; h=base-top
        p.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{h}" rx="6" fill="{CHIP}" stroke="{ACC}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+bw//2}" y="{top+24}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{ACC}">{esc(name)}</text>')
        p.append(f'<text x="{x+bw//2}" y="{top+44}" text-anchor="middle" font-size="11.5" fill="{INK}">{esc(lab)}</text>')
    p.append('</g>')
    p.append(f'<line x1="16" y1="334" x2="{16+n*(bw+10)-10}" y2="334" stroke="{MUTED}" stroke-width="1"/>')
    p.append(f'<text x="{W-30}" y="352" text-anchor="end" font-family="sans-serif" font-size="11.5" fill="{MUTED}">more value, more rigour →</text>')
    return figw(f'<svg viewBox="0 0 {W} 360" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap)


def radial_svg(title, center, spokes, cap):
    pts=[(890,210),(775,316),(500,360),(224,316),(110,210),(224,104),(500,60),(775,104)][:len(spokes)]
    p=[f'<rect x="0" y="0" width="1000" height="420" fill="{BG}"/>',
       f'<text x="500" y="24" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="{INK}">{esc(title)}</text>',
       f'<g stroke="{LINE}" stroke-width="1.5">']
    for x,y in pts: p.append(f'<line x1="500" y1="210" x2="{x}" y2="{y}"/>')
    p.append('</g><g font-family="sans-serif" font-size="11.5" text-anchor="middle">')
    for (x,y),lab in zip(pts,spokes):
        p.append(f'<rect x="{x-85}" y="{y-22}" width="170" height="44" rx="8" fill="{CHIP}" stroke="{ACC}" stroke-width="1.5"/><text x="{x}" y="{y+4}" fill="{INK}">{esc(lab)}</text>')
    p.append('</g>')
    p.append(f'<circle cx="500" cy="210" r="64" fill="{ACC}"/><text x="500" y="206" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fff">{esc(center)}</text><text x="500" y="226" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="{CHIP}">on data + AI</text>')
    return figw(f'<svg viewBox="0 0 1000 420" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap)


def fm(title,desc,date,tags,faqs):
    out=["---","layout: post",f'title: "{title}"',f'description: "{desc}"',f"date: {date} 09:00:00 -0700",f"updated: {date}",f"tags: [{', '.join(tags)}]","faq:"]
    for q,a in faqs: out+=[f'  - q: "{q}"',f'    a: "{a}"']
    out.append("---"); return "\n".join(out)


REG="Across regions the levers are the same but the rules differ: the **UK** (SECR energy/carbon reporting, packaging EPR), the **EU** (CSRD, the EU ETS, and the Packaging and Packaging Waste Regulation), the **USA** (EPA water and Energy Star, state programmes like California's, and TTB for labelling), and **India** (the Bureau of Energy Efficiency's PAT scheme and CPCB effluent norms). Measure to your own meters first; map to whichever framework applies."


def article(s):
    lever=s["lever"]; d1=steps_svg(s["d1title"], s["steps"], s["d1cap"])
    if s["cat"]=="carbon": d2=footprint_svg("Where the emissions sit — by scope","Most of a drinks producer's footprint is Scope 3 (packaging, transport, supply) — measure it, don't guess it.")
    elif s["cat"]=="roadmap": d2=pyramid_svg("Sustainability sits on measured data",[("AI & GenAI","models, copilots, reports"),("Analytics","dashboards & KPIs"),("Metering","energy, water, waste meters")],"The pyramid is the point: AI cuts what you can measure; meters come first.")
    elif s["cat"]=="pillar": d2=steps_svg("The improvement loop, every lever",[("Meter","energy, water, waste"),("Baseline","per unit produced"),("Reduce","AI finds the waste"),("Verify","measured savings"),("Report","UK/EU/US/India")],"One loop behind every lever — meter, baseline, reduce, verify, report.")
    else: d2=pyramid_svg("Every saving sits on a meter",[("AI & GenAI","optimise & report"),("Analytics","dashboards & KPIs"),("Metering","the sub-metered data")],"You cannot cut what you do not measure — sub-metering is the unglamorous first step.")
    faqs=[(f"How can data and AI cut {lever}?", s["ai"]),
          ("Where do Claude and ChatGPT fit in sustainability?", s["genai"]),
          (s["faq3q"], s["faq3a"])]
    links=" · ".join(L(t,u) for t,u in s.get("links",[]))
    body=[fm(s["title"],s["desc"],s["date"],["esg","sustainability"]+s.get("tags",[]),faqs),"",
      f"**Short answer: {s['short']}**","",
      f"{s['intro']}",""]
    if links: body+=[f"Related: {links}.",""]
    body+=[d1,"",
      "## Measure first, model second\n",
      f"{s['measure']}","",
      f"## Where AI and data cut {lever}\n",
      f"{s['ai']}","",
      "## Where generative AI (Claude, ChatGPT) helps\n",
      f"{s['genai']} The rule holds: it drafts and explains, a person verifies anything that reaches a regulator.","",
      "## The rules, region by region\n",
      f"{s.get('region',REG)}","",d2,"",
      "## Where it breaks\n",
      f"{s['limit']}","",
      "## The bottom line\n",
      f"{s['bottom']}","",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
      f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
      f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      f"*Part of the {L(FOOT[0],FOOT[1])} track.*",""]
    return "\n".join(body)


PILLAR=dict(slug="sustainable-drinks-business-ai-data", date="2026-01-13", cat="pillar",
  lever="energy, water and waste", tags=["energy","water","carbon"],
  title="Making a Beer, Wine and Whiskey Business More Sustainable with AI and Data",
  desc="How drinks producers cut electricity, water and emissions using AI, data science and generative AI — the levers, the data foundation, and the UK, EU, USA and India rules, with links to each deep dive.",
  short="sustainability in a drinks business is an engineering and data problem before it is an AI one. Meter your energy, water and waste; baseline per unit produced; let AI find and cut the waste; verify the savings; and report to whichever framework applies. Generative AI helps draft the reports. This is the map, with a deep dive behind each lever.",
  intro="Beer, wine and whiskey are energy- and water-hungry to make, and most of their footprint hides in packaging and transport. The good news: nearly every saving starts with a meter and a baseline, not an algorithm. This series walks the levers — energy, water, carbon, circular by-products — and the data and AI that cut each, with honest limits throughout. It builds on the idea of "+L("collecting data before AI","/2026/collect-your-data-before-ai/")+".",
  d1title="Where a drinks producer saves", steps=[("Energy","power & heat"),("Water","ratio & effluent"),("Carbon","Scope 1/2/3"),("Circular","by-products"),("Reporting","UK/EU/US/India")],
  d1cap="Five levers, one method — and a regional reporting layer on top.",
  measure="Before any model, sub-meter the plant: electricity by area, water in and out, gas and steam, and waste by stream. Baseline everything per hectolitre or per case. Most 'AI sustainability' projects fail here, not in the model — you cannot optimise what you never measured.",
  ai="Across the levers, machine learning forecasts demand and load, flags anomalies (a leaking valve, a drifting chiller), and optimises schedules — running energy-hungry steps off-peak, sizing refrigeration to real need, and predicting effluent loads before they breach a limit.",
  genai="A generative-AI copilot (Claude or ChatGPT) turns the metered data into the ESG narrative — drafting CSRD or SECR sections, answering 'what was our water ratio last quarter?' in plain language, and writing the SOPs that make savings stick.",
  faq3q="Do I need AI to make my brewery or winery more sustainable?",
  faq3a="No. The biggest wins come from metering, baselining and basic engineering. AI and generative AI amplify a measured operation — they forecast, optimise and report — but they cannot save energy or water you are not yet measuring.",
  limit="Two honest limits. First, AI cuts what you measure; without sub-metering it has nothing to work on. Second, the carbon that matters most (Scope 3 — packaging and transport) is the hardest to measure and the least under your direct control, so beware diversion claims you cannot verify.",
  bottom="Sustainability in drinks is a measured loop — meter, baseline, reduce, verify, report — and AI makes each step sharper once the data exists. Pick the lever that costs you most today, follow its deep dive, and start with a meter.",
  links=[("carbon accounting deep dive","/2026/carbon-accounting-beverage-ai-data/"),("the sustainability data roadmap","/2026/sustainability-data-roadmap-beverage/")])

SPECS=[
 dict(slug="cutting-brewery-electricity-ai", date="2026-01-27", cat="energy", lever="brewery electricity use", tags=["energy","brewing"],
   title="Cutting Brewery Electricity Use with AI: Refrigeration, Compressors and Load",
   desc="Refrigeration and compressed air dominate a brewery's power bill. How data and AI cut electricity use — load forecasting, anomaly detection and off-peak scheduling — across UK, EU, US and India.",
   short="refrigeration and compressed air are most of a brewery's electricity bill, and both are full of waste. Sub-meter them, baseline kWh per hectolitre, and use AI to forecast load, flag drifting equipment and shift flexible cooling to off-peak. The savings are measured in the meter, not the model.",
   intro="Glycol chillers, cold liquor tanks and air compressors run around the clock, often oversized and under-monitored. That makes electricity a brewery's most tractable sustainability lever — and a cost line.",
   d1title="Cutting brewery power, step by step", steps=[("Sub-meter","by area"),("Baseline","kWh / hL"),("Forecast","cooling load"),("Optimise","off-peak & setpoints"),("Verify","measured kWh")],
   d1cap="The path from a single power bill to a measured, optimised load.",
   measure="Put sub-meters on refrigeration, compressed air, lighting and the packaging hall, and baseline kWh per hectolitre. A brewery that only sees one monthly bill cannot tell a failing compressor from a busy week.",
   ai="Machine learning forecasts cooling demand from the brew schedule and weather, so refrigeration runs to real need rather than a fixed setpoint; anomaly detection flags a chiller losing efficiency or compressed-air leaks (often 20-30% of air load); and load-shifting moves flexible cooling to cheaper, lower-carbon off-peak hours.",
   genai="A Claude or ChatGPT copilot reads the meter data and drafts the energy section of your SECR or CSRD return, and writes the operator SOP for the new setpoints.",
   faq3q="What uses the most electricity in a brewery?", faq3a="Typically refrigeration (glycol, cold liquor, cellar cooling) and compressed air, followed by packaging and lighting. They are also the most controllable, which is why metering them first pays off fastest.",
   region=REG, limit="AI tunes a system; it cannot fix an oversized or failing chiller — some savings are capital, not software. And load-shifting only helps where tariffs or grid carbon vary by time of day, which differs by region.",
   bottom="A brewery's power bill is mostly refrigeration and air, and most of that is waste you can meter, forecast and trim. Start by sub-metering the cold side; the model comes after.",
   links=[("brewery energy and utilities optimisation","/2024/ai-brewery-energy-utilities-optimization/")]),
 dict(slug="distillery-energy-heat-recovery-ai", date="2026-02-10", cat="energy", lever="distillery energy and fuel", tags=["energy","whiskey","distilling"],
   title="Distillery Energy and Heat Recovery: Using Data to Cut Fuel and Power",
   desc="Distillation is heat-intensive. How data and AI cut a distillery's fuel and power — heat recovery, load forecasting and anomaly detection — with UK, EU, US and India context.",
   short="distillation is the most energy-intensive step in drinks, dominated by heat. The savings come from recovering and reusing that heat, running stills efficiently, and metering fuel per litre of alcohol. AI forecasts and optimises; the heat exchanger does the real work.",
   intro="A still boils and condenses enormous amounts of energy, much of it currently thrown away as waste heat. That makes heat recovery a distillery's biggest sustainability prize.",
   d1title="Cutting distillery energy, step by step", steps=[("Meter","fuel & steam"),("Baseline","MJ / LPA"),("Recover","waste heat"),("Optimise","still & schedule"),("Verify","measured fuel")],
   d1cap="From fuel bill to a heat-recovered, optimised distillation.",
   measure="Meter steam, fuel and power, and baseline energy per litre of pure alcohol. Without it, a distillery cannot see how much heat leaves in the spent lees and condenser cooling water.",
   ai="ML forecasts run schedules and optimises charge timing so heat is reused across runs; anomaly detection flags fouling heat exchangers and steam-trap failures; and modelling sizes heat-recovery (vapour recompression, thermal stores) against the real load.",
   genai="A copilot drafts the energy and decarbonisation narrative for reporting and writes the heat-recovery SOP, grounded in your metered MJ-per-LPA figures.",
   faq3q="How can a distillery cut its carbon footprint?", faq3a="Mostly by addressing heat: recover and reuse waste heat, switch fuel where viable, and run stills efficiently. Energy is Scope 1 and 2; the model helps optimise, but heat-recovery hardware delivers the structural cut.",
   region=REG, limit="The largest cuts (mechanical vapour recompression, fuel switching, electrification) are capital projects with long paybacks — AI builds the business case and optimises operation, but it is not a substitute for the kit.",
   bottom="A distillery's footprint is heat, and most of that heat is currently wasted. Meter fuel per LPA, recover what you can, and let AI optimise the rest.",
   links=[("wort boiling energy optimisation","/2023/ai-wort-boiling-energy-optimization/")]),
 dict(slug="winery-energy-cooling-ai", date="2026-02-23", cat="energy", lever="winery energy use", tags=["energy","wine","winemaking"],
   title="Winery Energy: AI for Cooling, Presses and Peak Demand",
   desc="Winery energy spikes at harvest with refrigeration and presses. How data and AI cut power and peak demand — load forecasting, setpoint optimisation and demand management — across regions.",
   short="a winery's energy is peaky — refrigeration for cold-soak and fermentation, plus presses, all spiking at harvest. Meter it, baseline per case, and use AI to forecast and flatten the peak. Demand charges, not just kWh, are where the money leaks.",
   intro="Harvest concentrates a winery's whole energy year into a few intense weeks, with refrigeration and presses driving sharp demand peaks that utilities bill heavily.",
   d1title="Cutting winery energy, step by step", steps=[("Meter","by load"),("Baseline","kWh / case"),("Forecast","harvest load"),("Flatten","peak demand"),("Verify","kWh & kW")],
   d1cap="From a peaky harvest bill to a forecast, flattened load.",
   measure="Sub-meter refrigeration, presses and the cellar, and baseline both energy (kWh per case) and peak demand (kW). Demand charges can rival energy charges, and only metering reveals them.",
   ai="ML forecasts harvest cooling load from intake and weather, pre-cools tanks off-peak, and staggers presses to shave the demand peak; anomaly detection flags refrigeration faults during the one period a winery cannot afford them.",
   genai="A copilot turns the season's meter data into the energy section of an ESG report and drafts the harvest energy-management SOP.",
   faq3q="When does a winery use the most energy?", faq3a="At harvest, when refrigeration for cold-soak and fermentation runs alongside presses — creating both high consumption and sharp demand peaks. That concentration is exactly what makes forecasting and peak-flattening valuable.",
   region=REG, limit="Peak-shaving helps most where utilities levy demand charges or time-of-use tariffs — common in the US and parts of Europe, less so elsewhere — so the saving depends on your tariff, not just your kWh.",
   bottom="Winery energy is a harvest-peak problem. Meter consumption and demand, forecast the peak, and flatten it; the algorithm earns its keep only against a real tariff.",
   links=[("ai wine fermentation control","/2024/ai-wine-fermentation-control/")]),
 dict(slug="cutting-water-use-brewing-data", date="2026-03-09", cat="water", lever="brewing water use", tags=["water","brewing"],
   title="Cutting Water Use in Brewing: The Water-to-Beer Ratio, with Data",
   desc="Breweries use several litres of water per litre of beer. How data and AI cut the water-to-beer ratio — sub-metering, anomaly detection and benchmarking — across UK, EU, US and India.",
   short="most breweries use 3-7 litres of water per litre of beer, and the best push below 3. The lever is the water-to-beer ratio: sub-meter every use, baseline it, and use data to find and fix the losses (CIP, rinsing, cooling). AI flags leaks; people fix them.",
   intro="Water is a brewery's quiet sustainability story — used in mashing, but far more in cleaning, rinsing and cooling. The water-to-beer ratio is the single number that tells you how well you run.",
   d1title="Cutting the water-to-beer ratio", steps=[("Sub-meter","every use"),("Baseline","HL water / HL beer"),("Find","losses & leaks"),("Reduce","CIP & reuse"),("Verify","ratio trend")],
   d1cap="From a site water bill to a measured, falling water-to-beer ratio.",
   measure="Meter water into each area — brewhouse, cellar, packaging, utilities — not just the site inlet. The water-to-beer ratio only becomes actionable when you can see which use is heavy.",
   ai="Anomaly detection on sub-meters flags leaks and runaway rinsing in real time; benchmarking compares the ratio across shifts and sites; and modelling identifies where treated water can be safely reused (last rinse to first rinse, cooling blowdown).",
   genai="A copilot benchmarks your ratio against context, drafts the water section of a CSRD or sustainability report, and writes the reduced-water SOP for the cellar team.",
   faq3q="What is a good water-to-beer ratio?", faq3a="Typical breweries sit around 4-7:1; efficient ones reach 3:1 or below. The number matters less than the trend — measure your own baseline and drive it down, because reuse limits and beer quality set a practical floor.",
   region=REG, limit="Water reuse is constrained by hygiene and, in many regions, by regulation — you cannot reuse water into product contact freely. The ratio has a floor set by biology and law, not by the model.",
   bottom="The water-to-beer ratio is the brewery's clearest sustainability KPI. Sub-meter, baseline, and chase the losses; AI finds them faster, but quality and rules set the floor.",
   links=[("water stewardship analytics","/2025/water-stewardship-analytics-brewing/")]),
 dict(slug="wastewater-effluent-analytics-beverage", date="2026-03-23", cat="water", lever="wastewater and effluent load", tags=["water","ehs"],
   title="Wastewater and Effluent Analytics for Breweries and Distilleries",
   desc="Brewery and distillery effluent is high-strength and tightly regulated. How data and AI manage effluent load — forecasting, anomaly detection and load-balancing — with UK, EU, US, India rules.",
   short="brewery and distillery effluent is high-strength (high COD/BOD) and surcharged or capped by regulators. The lever is managing the load: meter and forecast it, balance discharges, and catch breaches before they happen. AI predicts the load; treatment and process changes cut it.",
   intro="Spent grain, yeast, trub and cleaning chemicals make drinks effluent some of the strongest industrial wastewater, and discharge limits carry real fines.",
   d1title="Managing effluent, step by step", steps=[("Meter","flow & COD"),("Baseline","load per HL"),("Forecast","discharge load"),("Balance","equalise flow"),("Verify","within limits")],
   d1cap="From surprise surcharges to a forecast, balanced, compliant discharge.",
   measure="Meter effluent flow and strength (COD/BOD) by source. Most producers discover their effluent profile only from the surcharge invoice — too late to manage it.",
   ai="ML forecasts discharge load from the production schedule, so flows can be balanced and equalised rather than dumped; anomaly detection flags a lost tank of beer heading to drain (a huge COD spike) before it breaches consent; and optimisation targets the cleaning and recovery changes that cut load at source.",
   genai="A copilot drafts discharge-consent and CSRD water sections and writes the spill-response SOP, grounded in your metered COD data.",
   faq3q="Why is brewery wastewater a problem?", faq3a="It is high-strength — rich in sugars, yeast and chemicals — so it overloads municipal treatment and attracts surcharges or limits. Lost product to drain is the biggest avoidable spike, which is why real-time monitoring pays.",
   region=REG, limit="Effluent limits and surcharge formulas are local and vary widely; AI forecasts and balances load, but meeting consent often needs treatment capital (balancing tanks, anaerobic digestion) the model only helps justify.",
   bottom="Effluent is a measured, regulated load — forecast it, balance it, and stop product reaching the drain. AI gives early warning; treatment and process discipline cut the load.",
   links=[("process water and effluent reduction","/2024/ai-process-water-effluent-reduction/")]),
 dict(slug="cip-optimisation-water-chemicals-ai", date="2026-04-07", cat="water", lever="CIP water, chemicals and energy", tags=["water","energy","brewing"],
   title="CIP Optimisation: Saving Water, Chemicals and Energy with AI",
   desc="Clean-in-place is a top consumer of water, chemicals and heat. How data and AI optimise CIP cycles — conductivity-based endpoints, anomaly detection and right-sizing — across regions.",
   short="clean-in-place quietly consumes a huge share of a plant's water, caustic and heat, mostly because cycles run on fixed timers 'to be safe'. The lever is data-driven CIP: end cycles on measured cleanliness, not the clock, and right-size flows. AI optimises; hygiene sets the limit.",
   intro="Every tank and line gets cleaned, and most CIP runs longer, hotter and wetter than needed because the cycle is timed, not measured. That conservatism is expensive in water, chemicals and energy.",
   d1title="Optimising CIP, step by step", steps=[("Meter","water, caustic, heat"),("Baseline","per cycle"),("Sense","conductivity & turbidity"),("Right-size","time & flow"),("Verify","clean + saved")],
   d1cap="From fixed-timer CIP to measured, right-sized cycles.",
   measure="Meter water, chemical and energy use per CIP cycle, and instrument return-line conductivity and turbidity. A timed cycle hides how much rinse and caustic is wasted after the line is already clean.",
   ai="ML learns the real cleaning endpoint from conductivity and turbidity so cycles stop when clean, not on the timer; it recovers and reuses final rinse and caustic; and anomaly detection catches a cycle that fails — protecting quality while cutting inputs.",
   genai="A copilot drafts the optimised CIP SOP and the water-and-chemical savings section of a sustainability report from the per-cycle data.",
   faq3q="How much can CIP optimisation save?", faq3a="It varies, but CIP is often one of the largest single users of water, caustic and heat in a plant, and fixed-timer cycles leave clear slack. The saving is real but bounded by hygiene — you optimise to a verified-clean endpoint, never below it.",
   region=REG, limit="CIP touches food safety, so changes must be validated and may need sign-off; you optimise toward a proven-clean endpoint and never past it. The model advises; hygiene rules decide.",
   bottom="CIP is a hidden giant in water, chemicals and energy. Measure each cycle, end on cleanliness rather than the clock, and reuse rinses — within the hygiene limits that always win.",
   links=[("ai optimised CIP cleaning cycles","/2024/ai-optimized-cip-cleaning-cycles/")]),
 dict(slug="carbon-accounting-beverage-ai-data", date="2026-04-20", cat="carbon", lever="carbon emissions", tags=["carbon","esg-reporting"],
   title="Carbon Accounting for Beverage Producers: Scope 1, 2 and 3 with Data",
   desc="Most of a drinks producer's carbon is Scope 3 — packaging and transport. How data and AI build a credible Scope 1/2/3 inventory, and where generative AI drafts the disclosure.",
   short="a drinks producer's carbon splits into Scope 1 (on-site fuel), Scope 2 (purchased energy) and Scope 3 (packaging, transport, supply) — and Scope 3 is usually the biggest and the hardest. Build the inventory on real meters and supplier data; use AI to fill gaps and generative AI to draft the disclosure, never the numbers.",
   intro="You cannot manage what you have not counted, and for drinks the count is dominated by glass, cans and freight, not the brewhouse. A credible carbon inventory is the foundation of every other sustainability claim.",
   d1title="Building a carbon inventory", steps=[("Collect","energy, materials, freight"),("Map","to Scope 1/2/3"),("Factor","emission factors"),("Model","fill the gaps"),("Report","UK/EU/US/India")],
   d1cap="From scattered data to a Scope 1/2/3 inventory you can defend.",
   measure="Pull energy meters (Scope 1/2) and material and freight records (Scope 3) into one place, with activity data per unit produced. Scope 3 is where the carbon and the measurement difficulty both concentrate.",
   ai="ML and data engineering reconcile messy supplier and logistics data, apply emission factors consistently, and estimate gaps where primary data is missing — flagging which assumptions move the total most.",
   genai="A Claude or ChatGPT copilot drafts the CSRD, SECR or voluntary disclosure narrative and answers 'what drove our Scope 3 last year?' — but the figures must trace to data, and a person owns the disclosure.",
   faq3q="What is the biggest source of carbon for a brewery or winery?", faq3a="Usually Scope 3 — packaging (especially glass) and transport — not the energy used to make the drink. That is why carbon accounting that stops at Scope 1 and 2 misses most of the footprint.",
   region=REG, limit="Scope 3 relies on estimates and supplier data of varying quality, so the number carries uncertainty — be transparent about method, and never let generative AI invent a figure or a reduction you cannot substantiate.",
   bottom="Carbon accounting is data engineering before it is climate science: collect, map to scope, factor, and disclose. AI fills gaps and drafts the report; the credibility lives in the measured data.",
   links=[("carbon accounting for breweries","/2025/carbon-accounting-breweries-scope/"),("avoiding greenwashing with AI","/2026/avoiding-greenwashing-ai-verify/")]),
 dict(slug="co2-recovery-refrigeration-emissions", date="2026-05-04", cat="carbon", lever="CO2 and refrigeration emissions", tags=["carbon","energy","brewing"],
   title="CO2 Recovery and Refrigeration: Cutting Emissions and Cost",
   desc="Fermentation CO2 and refrigerant leaks are emissions and cost. How data and AI manage CO2 recovery and refrigeration emissions, with regional context.",
   short="fermentation throws off pure CO2 that most breweries vent and then buy back, while refrigerant leaks are a quiet, high-impact emission. The levers are recovering CO2 and tightening refrigeration. Meter both; AI forecasts and flags; the recovery plant and leak fixes do the work.",
   intro="A brewery emits CO2 from every fermentation and often purchases CO2 for packaging — paying twice while emitting. Refrigerant leaks, meanwhile, carry global-warming potential hundreds of times that of CO2.",
   d1title="Cutting CO2 and refrigeration emissions", steps=[("Meter","CO2 & refrigerant"),("Baseline","vented vs bought"),("Recover","fermentation CO2"),("Tighten","leak detection"),("Verify","emissions down")],
   d1cap="From venting-and-buying to recovered CO2 and a tight refrigeration loop.",
   measure="Meter CO2 vented, CO2 purchased, and refrigerant top-ups. The gap between vented and bought is the recovery prize; refrigerant top-up frequency reveals leaks.",
   ai="ML forecasts fermentation CO2 availability against packaging demand to size recovery; anomaly detection on refrigerant pressure and top-up logs flags leaks early — both an emission and a compliance issue in many regions.",
   genai="A copilot drafts the refrigerant and CO2 sections of an emissions report and the leak-response SOP from the metered logs.",
   faq3q="Can a brewery recover its own CO2?", faq3a="Yes — fermentation CO2 can be captured, cleaned and reused for packaging, cutting both purchased CO2 and emissions. Whether it pays depends on scale and CO2 prices, which is exactly what a model can assess from your data.",
   region=REG, limit="CO2 recovery is a capital investment whose payback swings with CO2 prices and brewery scale; refrigerant rules (e.g., F-gas phase-downs in the UK/EU) force change regardless of the model. AI sizes and times the decision, not the cheque.",
   bottom="Stop venting CO2 you then buy back, and stop leaking refrigerant you then top up. Meter both, let AI size and flag, and invest where the data shows it pays.",
   links=[("CO2 evolution and fermentation monitoring","/2023/co2-evolution-fermentation-monitoring/")]),
 dict(slug="packaging-footprint-sustainability-data", date="2026-06-08", cat="carbon", lever="packaging emissions", tags=["carbon","packaging"],
   title="Cutting Packaging Footprint: Glass, Can and Keg Emissions with Data",
   desc="Packaging is the largest slice of most drinks footprints. How data and AI cut packaging emissions — material choice, lightweighting, reuse and recycled content — across UK, EU, US, India rules.",
   short="for most drinks producers, packaging is the single biggest emission — glass especially. The levers are material choice, lightweighting, recycled content and reuse. Data quantifies each option per SKU; AI optimises the mix; regulation (EPR, PPWR) increasingly forces the issue.",
   intro="A bottle or can often carries more carbon than the beer or wine inside it. That makes packaging the highest-leverage — and most regulated — sustainability decision a producer makes.",
   d1title="Cutting packaging footprint", steps=[("Measure","kg CO2 / SKU"),("Compare","glass/can/keg"),("Lightweight","& recycled content"),("Reuse","where viable"),("Report","EPR / PPWR")],
   d1cap="From a default bottle to a measured, optimised packaging mix.",
   measure="Attribute packaging carbon per SKU using material weights, recycled content and transport. Without per-SKU data you cannot compare a heavy bottle against a can or a returnable keg.",
   ai="Models compare packaging options per SKU and route, optimise lightweighting and recycled-content choices against cost and carbon, and forecast EPR fees under different mixes.",
   genai="A copilot drafts EPR and PPWR compliance text and the packaging section of a sustainability report, and explains the trade-offs to commercial teams in plain language.",
   faq3q="Which is more sustainable: glass, cans or kegs?", faq3a="Usually returnable kegs and lightweight cans beat single-use glass on carbon, but it depends on recycled content, transport distance and reuse rates — which is why you measure per SKU and route rather than assume.",
   region=REG, limit="Packaging carbon depends heavily on local recycling rates and grid energy, so a global answer misleads — measure for your region. And reuse only wins above a break-even number of trips, which logistics, not the model, determine.",
   bottom="Packaging is where most drinks carbon lives and where regulation is tightening fastest. Measure per SKU, optimise the mix, and let EPR/PPWR sharpen the case.",
   links=[("packaging footprint glass, can, keg","/2025/packaging-footprint-glass-can-keg/"),("reducing packaging material waste","/2024/reducing-packaging-material-waste-ai/")]),
 dict(slug="cold-chain-distribution-emissions-ai", date="2026-06-22", cat="carbon", lever="distribution and cold-chain emissions", tags=["carbon","logistics"],
   title="Cold Chain and Distribution Emissions: Route and Refrigeration Analytics",
   desc="Getting drinks to market burns fuel and refrigeration. How data and AI cut distribution and cold-chain emissions — route optimisation, load-fill and temperature analytics — across regions.",
   short="distribution is a large, often-ignored slice of drinks carbon: trucks, fuel, and refrigeration for chilled product. The levers are route optimisation, fuller loads and tighter cold-chain control. AI plans routes and flags waste; the savings show up in fuel and spoilage.",
   intro="Beer, wine and (chilled) drinks travel far and heavy, and refrigerated transport adds an energy penalty on top of the freight. Distribution is squarely in Scope 3 and squarely controllable.",
   d1title="Cutting distribution emissions", steps=[("Measure","fuel & km / case"),("Optimise","routes & loads"),("Fill","load utilisation"),("Control","cold chain"),("Verify","CO2 / case")],
   d1cap="From ad-hoc deliveries to optimised, full, temperature-controlled loads.",
   measure="Capture fuel, distance and load-fill per delivery, and temperature along the chilled chain. Half-empty trucks and over-cooling are invisible without the data.",
   ai="Route-optimisation and load-planning models cut kilometres and raise fill; demand forecasting reduces emergency part-loads; and cold-chain analytics flag over-refrigeration and excursions that waste energy or spoil product.",
   genai="A copilot drafts the logistics emissions section of a Scope 3 report and explains route and load trade-offs to the distribution team.",
   faq3q="Is distribution a big part of drinks carbon?", faq3a="Yes — freight and refrigerated transport are a significant Scope 3 source, especially for heavy glass and chilled product shipped long distances. Fuller loads and shorter routes cut both carbon and cost.",
   region=REG, limit="Route and load gains depend on your network and where production sits relative to demand; some emissions are structural (long export routes) and only relocation or modal shift moves them — beyond what any optimiser can do.",
   bottom="Distribution carbon is fuel, fill and refrigeration — all measurable, all improvable. Optimise routes and loads, tighten the cold chain, and report it in Scope 3.",
   links=[("route optimisation for beer distribution","/2021/route-optimisation-beer-distribution/")]),
 dict(slug="spent-grain-pomace-draff-value-data", date="2026-07-06", cat="circular", lever="by-product waste", tags=["circular-economy","brewing"],
   title="Turning Spent Grain, Pomace and Draff into Value with Data",
   desc="Spent grain, grape pomace and draff are big by-products. How data and AI route each to its highest-value use — feed, food, or energy — net of haulage and spoilage, across regions.",
   short="spent grain, grape pomace and distillery draff are the biggest things leaving a drinks plant, usually treated as waste. The lever is routing each batch to its highest-value use — feed, food or energy — net of haulage and spoilage. Data forecasts volumes; AI allocates; biology sets the clock.",
   intro="The largest by-product on site is often handled as a chore, given away or landfilled. But high in protein and fibre, it is a circular-economy opportunity the moment you start weighing it.",
   d1title="Valorising by-products", steps=[("Weigh","tonnes & moisture"),("Forecast","weekly volume"),("Allocate","feed/food/energy"),("Net off","haulage & spoilage"),("Verify","value & diversion")],
   d1cap="From a disposal cost to a routed, valued by-product stream.",
   measure="Put a scale and a moisture reading on the by-product stream and log off-take. You cannot optimise — or claim diversion — for tonnes you never weighed.",
   ai="ML forecasts weekly by-product volume from the production schedule and allocates it across feed, food and energy routes to maximise value net of haulage distance and the spoilage clock.",
   genai="A copilot drafts the circular-economy narrative for a CSRD or GRI disclosure and answers 'how much went to feed versus landfill?' from the by-product ledger.",
   faq3q="What can a brewery do with spent grain?", faq3a="Route it to its highest-value use: animal feed (cheapest, fastest), food-grade flour or protein (highest value, demand-limited), or biogas/energy (closes the loop). The right split depends on your volumes, moisture and haulage — an allocation problem AI handles well.",
   region=REG, limit="Perishability beats cleverness — by-product spoils in days, so an optimiser is useless without the drying or off-take to act in time. And drying can erase the carbon win unless you use waste heat.",
   bottom="By-products are the biggest, most overlooked stream leaving a drinks plant. Weigh them, forecast them, and route each batch to its highest net value before the clock runs out.",
   links=[("what to do with spent grain","/2026/spent-grain-feed-food-fuel/")]),
 dict(slug="byproduct-circular-economy-analytics", date="2026-07-20", cat="circular", lever="resource and by-product flows", tags=["circular-economy","esg-reporting"],
   title="By-Product and Circular-Economy Analytics for Drinks Producers",
   desc="Closing loops needs a material balance. How data and AI track every resource and by-product flow, find circular opportunities, and substantiate diversion claims, across regions.",
   short="a circular economy needs a material balance — what comes in, what leaves, and where it goes. The lever is a measured ledger of every resource and by-product flow. Data builds the balance; AI spots the loops worth closing; verification stops the diversion claim from becoming greenwashing.",
   intro="Circularity sounds strategic but starts mundane: knowing, in tonnes, what enters and leaves the site. Only then can you find the loops worth closing and prove the ones you claim.",
   d1title="Building a circular ledger", steps=[("Inventory","inputs & outputs"),("Balance","material balance"),("Spot","loops to close"),("Match","off-takers"),("Verify","diversion claims")],
   d1cap="From scattered waste invoices to a verified material balance.",
   measure="Build a material balance: raw materials and water in, product and every by-product and waste stream out, all weighed. The gaps in that balance are where loss and opportunity hide.",
   ai="Analytics reconcile the balance, flag the largest loss streams, and match by-products to nearby off-takers; modelling ranks circular options by value and carbon.",
   genai="A copilot drafts the circular-economy and waste sections of an ESG report and turns the ledger into a story for regulators and customers — substantiated, not invented.",
   faq3q="How do you prove a circular-economy or zero-waste claim?", faq3a="With a measured material balance and an off-take ledger that traces each stream to its destination. A claim you cannot trace to weighed tonnes is greenwashing risk, which is why measurement precedes marketing.",
   region=REG, limit="Circular claims are increasingly policed (the EU and UK in particular), so unverifiable diversion or 'zero-waste' statements are a real liability — generative AI must report only what the ledger substantiates.",
   bottom="Circularity is a measured material balance before it is a strategy. Build the ledger, close the loops the data ranks highest, and only claim what you can trace.",
   links=[("avoiding greenwashing with AI","/2026/avoiding-greenwashing-ai-verify/")]),
 dict(slug="claude-chatgpt-csrd-esg-reports", date="2026-08-10", cat="genai", lever="ESG reporting effort", tags=["generative-ai","esg-reporting","claude"],
   title="Using Claude and ChatGPT to Draft Your CSRD and ESG Reports",
   desc="ESG reporting is heavy on writing. How generative AI like Claude and ChatGPT drafts CSRD, SECR and voluntary reports from your data — and where a human must own the numbers.",
   short="ESG and CSRD reporting is mostly structured writing over data you already have. Generative AI — Claude or ChatGPT — drafts the narrative, maps your metrics to the framework, and answers plain-language questions, cutting the reporting burden. But it must be grounded in measured data, and a responsible person owns every figure.",
   intro="The hardest part of sustainability reporting is rarely the data — it is turning it into the long, structured, framework-specific prose regulators expect. That is exactly what generative AI is good at, and exactly where it is dangerous if ungrounded.",
   d1title="Drafting a report with generative AI", steps=[("Gather","metered data"),("Map","to the framework"),("Draft","with Claude/ChatGPT"),("Verify","every figure"),("Sign off","a human owner")],
   d1cap="Generative AI drafts; a person verifies and signs — never the other way round.",
   measure="The report is only as good as the data under it. Assemble your energy, water, waste and carbon metrics first; generative AI cannot substitute for measurement, only narrate it.",
   ai="Beyond drafting, ML and analytics produce the metrics the report cites — the energy ratios, carbon inventory and water figures — so the narrative rests on real numbers.",
   genai="Claude or ChatGPT maps your data to CSRD, SECR or GRI structure, drafts each disclosure section, summarises year-on-year change, and answers reviewer questions — with retrieval grounded in your documents so it quotes your figures, not invented ones.",
   faq3q="Can ChatGPT or Claude write my CSRD report?", faq3a="They can draft it and assemble the structure fast, but not own it. The figures must trace to measured data, a person must verify and sign, and you should ground the model in your own documents so it cannot invent numbers or claims.",
   region="CSRD applies in the EU (phasing in by company size), the UK uses SECR and TCFD-aligned disclosure, the US has a patchwork of state and SEC rules in flux, and India has BRSR for listed firms. Generative AI helps map one dataset to whichever framework you face — but a human confirms the mapping.",
   limit="Generative AI hallucinates confidently, so an ungrounded draft can fabricate a figure or a compliance claim. Always retrieve from your own verified data, and never let the model be the final authority on a regulated disclosure.",
   bottom="Generative AI turns ESG reporting from a writing marathon into an editing task — drafting from your data and mapping to the framework. Keep it grounded, keep a human owning the numbers, and it earns its place.",
   links=[("avoiding greenwashing with AI","/2026/avoiding-greenwashing-ai-verify/"),("ESG reporting automation (CSRD)","/2025/esg-reporting-automation-csrd/")]),
 dict(slug="generative-ai-sustainability-sops-training", date="2026-08-24", cat="genai", lever="sustainability knowledge and training", tags=["generative-ai","claude"],
   title="Generative AI for Sustainability SOPs, Training and Audits",
   desc="Savings only stick if people follow them. How generative AI drafts sustainability SOPs, training and audit prep — grounded in your data — across UK, EU, US and India.",
   short="energy and water savings evaporate without SOPs, training and audits to make them stick. Generative AI drafts the procedures, builds the training, and prepares audit responses from your data and standards — turning a one-off project into routine practice. A person still owns accuracy and sign-off.",
   intro="The gap between a sustainability project and lasting savings is human: the new setpoint that drifts back, the rinse step nobody changed. Generative AI is unusually good at closing that gap cheaply.",
   d1title="Making savings stick with generative AI", steps=[("Capture","the new practice"),("Draft","SOPs & training"),("Translate","for every shift"),("Prep","audit answers"),("Verify","accuracy & sign-off")],
   d1cap="From a project that fades to procedures, training and audit-readiness.",
   measure="Ground the assistant in your real procedures, standards and metered results, so the SOPs it writes reflect how the plant actually runs — not a generic template.",
   ai="Analytics show whether the new practice is holding (did the water ratio stay down?), feeding back into where training is needed.",
   genai="Claude or ChatGPT drafts SOPs from a rough description, translates them for different shifts and languages, builds quiz-based training, and assembles audit evidence and responses against ISO 14001 or a customer questionnaire — grounded in your documents.",
   faq3q="Can generative AI help pass a sustainability audit?", faq3a="It can prepare you: drafting procedures, organising evidence, and answering questionnaire items from your records. It cannot make a claim true — the underlying data and practice must be real, and a responsible person verifies every answer.",
   region=REG, limit="An SOP or audit answer the model writes can be plausibly wrong, so a person must verify it against the real standard and practice. Generative AI scales the writing, not the responsibility.",
   bottom="Savings stick when procedures, training and audits keep them in place — and generative AI makes all three cheap to produce and maintain. Ground it in your data, verify the output, and the project becomes a habit.",
   links=[("gen AI search over brewery SOPs","/2022/gen-ai-search-brewery-sops/")]),
 dict(slug="sustainable-drinks-uk-secr-epr", date="2026-09-07", cat="regional", lever="UK sustainability compliance", tags=["regional","esg-reporting","uk"],
   title="Sustainable Drinks in the UK: SECR, EPR and the Data Behind Compliance",
   desc="UK drinks producers face SECR energy reporting and packaging EPR. How data and AI meet UK sustainability rules, and where generative AI drafts the disclosures.",
   short="UK drinks producers face Streamlined Energy and Carbon Reporting (SECR), extended producer responsibility (EPR) for packaging, and the plastic packaging tax. The data work is the same as anywhere — meter energy, weigh packaging — mapped to UK rules. AI assembles the figures; generative AI drafts the filings.",
   intro="The UK's regime rewards producers who already measure: SECR wants energy and carbon, EPR wants packaging data by material and weight. Both are data exercises before they are compliance ones.",
   d1title="Meeting UK rules with data", steps=[("Meter","energy & carbon"),("Weigh","packaging by material"),("Map","to SECR / EPR"),("Draft","the filing"),("Verify","and submit")],
   d1cap="From metered data to SECR and EPR filings.",
   measure="SECR needs energy use and emissions; EPR needs packaging placed on market by material and weight. Producers who sub-meter and track packaging per SKU already hold most of what both require.",
   ai="Data engineering consolidates energy and packaging data and applies UK emission factors; analytics model EPR fees under different packaging mixes so the commercial choice is informed.",
   genai="A copilot maps your data to the SECR narrative and EPR submission and drafts both, citing your verified figures.",
   faq3q="What sustainability reporting do UK breweries need?", faq3a="Larger companies report energy and carbon under SECR; producers placing packaging on the UK market face EPR obligations and the plastic packaging tax. Thresholds and exact duties depend on size and packaging volumes, so check current rules with an adviser.",
   region="This piece focuses on the UK; companion pieces cover the EU (CSRD, ETS, PPWR), the USA (EPA, state programmes, TTB) and India (BEE, CPCB).",
   limit="UK rules and thresholds change, and EPR in particular has been phasing in with shifting detail — treat this as orientation, not legal advice, and confirm obligations for your size and packaging with a specialist.",
   bottom="UK sustainability compliance rewards measurement: meter energy for SECR, weigh packaging for EPR, and let AI assemble and generative AI draft. The data you need is mostly data you should already keep.",
   links=[("ESG reporting automation","/2025/esg-reporting-automation-csrd/")]),
 dict(slug="sustainable-drinks-eu-csrd-ets-ppwr", date="2026-09-21", cat="regional", lever="EU sustainability compliance", tags=["regional","esg-reporting","eu"],
   title="Sustainable Drinks in the EU: CSRD, EU ETS and Packaging (PPWR)",
   desc="EU drinks producers face CSRD reporting, the EU ETS and the Packaging and Packaging Waste Regulation. How data and AI meet EU rules, with generative AI drafting disclosures.",
   short="the EU has the world's most demanding regime: CSRD double-materiality reporting, the EU Emissions Trading System for larger sites, and the Packaging and Packaging Waste Regulation (PPWR) reshaping packaging. The data demand is high — but it is still meter, weigh, map. AI consolidates; generative AI drafts the lengthy disclosures.",
   intro="The EU sets the global high-water mark for sustainability rules, and CSRD's breadth makes data quality, not willingness, the binding constraint for drinks producers.",
   d1title="Meeting EU rules with data", steps=[("Meter","energy, water, carbon"),("Weigh","packaging & recyclability"),("Map","CSRD / ETS / PPWR"),("Draft","disclosures"),("Assure","audit-ready")],
   d1cap="From operational data to CSRD-grade, assurable disclosures.",
   measure="CSRD demands broad, audit-ready data across energy, water, waste, carbon and value chain; PPWR pushes recyclability and recycled content; ETS needs verified emissions. The bar is high — measurement and data lineage are everything.",
   ai="Data engineering builds the consolidated, traceable dataset CSRD assurance requires; analytics model packaging against PPWR targets and forecast ETS exposure.",
   genai="A copilot drafts CSRD disclosure sections against the ESRS structure and answers assurance questions — grounded in lineage-tracked data so every figure is defensible.",
   faq3q="Does CSRD apply to drinks companies?", faq3a="It applies to companies meeting EU size thresholds (phasing in over several years), and indirectly to suppliers asked for data by in-scope customers. Even smaller producers feel it through the value chain, so the data foundation matters regardless.",
   region="This piece focuses on the EU; companion pieces cover the UK (SECR, EPR), the USA (EPA, state, TTB) and India (BEE, CPCB).",
   limit="CSRD is being phased and adjusted, and assurance raises the bar on data quality — ungrounded or estimated figures are a real liability. Generative AI drafts; verified, traceable data and a human signatory carry the legal weight.",
   bottom="The EU regime is demanding but mechanically familiar: measure broadly, trace everything, map to CSRD/ETS/PPWR, and let generative AI draft the volume of prose. Data lineage is the differentiator.",
   links=[("ESG reporting automation (CSRD)","/2025/esg-reporting-automation-csrd/"),("supply chain ESG: barley and hops","/2025/supply-chain-esg-barley-hops/")]),
 dict(slug="sustainable-drinks-usa-epa-state-ttb", date="2026-10-05", cat="regional", lever="US sustainability practice", tags=["regional","esg-reporting","usa"],
   title="Sustainable Drinks in the USA: EPA, State Programs and TTB",
   desc="US drinks producers navigate EPA rules, state programs and TTB. How data and AI drive sustainability where federal mandates are lighter and state rules vary, with generative AI support.",
   short="the US has lighter federal sustainability mandates than the EU, but real EPA water and energy rules, strong state programmes (California especially), utility incentives, and TTB for labelling. The lever is the same — meter and measure — but the driver is often cost and state rules, not a single federal report. AI optimises; generative AI handles the patchwork of paperwork.",
   intro="In the US, sustainability for drinks is driven less by one mandate than by utility costs, state programmes, customer demands and voluntary commitments — which makes the business case, not compliance, the usual starting point.",
   d1title="Driving US sustainability with data", steps=[("Meter","energy & water"),("Target","utility incentives"),("Comply","EPA & state"),("Optimise","cost & carbon"),("Report","voluntary / customer")],
   d1cap="From cost and state rules to a measured, optimised programme.",
   measure="Meter energy and water to qualify for utility rebates and demand-response programmes, meet EPA Clean Water Act discharge limits, and answer the voluntary and customer ESG questionnaires that increasingly gate shelf space.",
   ai="ML optimises against time-of-use tariffs and demand charges (significant in US utilities), targets rebate-eligible projects, and manages discharge to EPA and local limits.",
   genai="A copilot assembles voluntary disclosures, customer ESG questionnaires and state-program applications from one dataset — useful where the paperwork is fragmented across states and buyers.",
   faq3q="Do US breweries have to report carbon?", faq3a="Federal mandatory carbon reporting is limited and in flux; most pressure comes from states (notably California), utilities, customers and voluntary commitments. EPA water rules and TTB labelling do apply, so the practical drivers are cost, state rules and market demand.",
   region="This piece focuses on the USA; companion pieces cover the UK (SECR, EPR), the EU (CSRD, ETS, PPWR) and India (BEE, CPCB).",
   limit="US rules vary sharply by state and shift with federal policy, so a national answer is rough — the reliable drivers are utility economics and customer demands, which reward measurement regardless of mandate.",
   bottom="In the US, measurement pays through utility incentives, EPA compliance and customer questionnaires more than a single federal report. Meter, optimise for cost and carbon, and let generative AI handle the state-by-state paperwork.",
   links=[("can AI write your TTB reports","/2026/can-ai-write-your-ttb-reports/")]),
 dict(slug="sustainable-drinks-india-bee-cpcb", date="2026-10-19", cat="regional", lever="India sustainability compliance", tags=["regional","esg-reporting","india"],
   title="Sustainable Drinks in India: BEE, CPCB and Water Norms",
   desc="Indian drinks producers face BEE energy rules, CPCB effluent norms and water stress. How data and AI cut energy and water and meet Indian regulations, with generative AI support.",
   short="Indian drinks producers operate under the Bureau of Energy Efficiency (and its PAT scheme for large users), CPCB and state-board effluent and water norms, and acute water stress in many regions. The lever is energy and water efficiency, measured and reported. AI optimises both; generative AI drafts the BRSR and regulatory paperwork.",
   intro="In India, water stress and energy cost make efficiency a business necessity, not just a compliance task — and regulators (BEE, CPCB, state boards) increasingly require the data to prove it.",
   d1title="Meeting India's rules with data", steps=[("Meter","energy & water"),("Baseline","per unit"),("Comply","CPCB / state norms"),("Improve","PAT targets"),("Report","BRSR")],
   d1cap="From metered data to CPCB compliance and BRSR reporting.",
   measure="Meter energy and water tightly: water is scarce and regulated, CPCB and state boards set effluent norms, and large energy users face PAT efficiency targets. Baselining per unit produced is the foundation for all of it.",
   ai="ML optimises energy against PAT targets, manages effluent to CPCB limits, and prioritises water reuse where stress and cost are highest — often a sharper driver in India than carbon.",
   genai="A copilot drafts BRSR (Business Responsibility and Sustainability Reporting) sections for listed firms and the CPCB and state-board paperwork from your metered data.",
   faq3q="What sustainability rules apply to breweries and distilleries in India?", faq3a="Energy efficiency under the Bureau of Energy Efficiency (with PAT targets for large consumers), effluent and water norms under CPCB and state pollution control boards, and BRSR reporting for listed companies. Water scarcity makes water efficiency especially material.",
   region="This piece focuses on India; companion pieces cover the UK (SECR, EPR), the EU (CSRD, ETS, PPWR) and the USA (EPA, state, TTB).",
   limit="Indian rules vary by state board and evolve, and water availability is a hard physical constraint in stressed regions that no model relaxes — efficiency and reuse have real, local limits. Confirm obligations with a specialist.",
   bottom="In India, water and energy efficiency are business-critical and increasingly mandated. Meter both, optimise with AI against PAT and CPCB norms, and let generative AI draft the BRSR and board paperwork.",
   links=[("water stewardship analytics","/2025/water-stewardship-analytics-brewing/")]),
 dict(slug="sustainability-data-roadmap-beverage", date="2026-11-09", cat="roadmap", lever="sustainability data maturity", tags=["data-strategy","esg-reporting"],
   title="A Sustainability Data Roadmap for Beverage Producers: The Phases",
   desc="Where to start with sustainability data and AI. A phased roadmap for drinks producers — meter, baseline, optimise, automate, report — with what to do and watch at each phase.",
   short="a drinks producer's sustainability journey is a phased data roadmap: meter the plant, baseline per unit, optimise with analytics and AI, automate the routine, and report to the framework. Each phase stands on the last. The most common failure is buying AI or a report before the meters exist.",
   intro="Every producer wants to know where to start on sustainability. The answer is the same as for any AI journey: with measurement. The clever parts come later and stand on the data.",
   d1title="The sustainability data roadmap", steps=[("Meter","energy, water, waste"),("Baseline","per unit produced"),("Optimise","analytics & AI"),("Automate","alerts & control"),("Report","UK/EU/US/India")],
   d1cap="Climb in order — each phase builds on the meters and baselines below it.",
   measure="Phase 0 is sub-metering: energy by area, water in and out, waste by stream. Phase 1 is baselining everything per hectolitre or case. Skip these and every later phase has nothing real to stand on.",
   ai="Phase 2 adds analytics and ML — forecasting load, flagging anomalies, optimising schedules; Phase 3 automates the routine with alerts and closed-loop control, keeping a human on anything consequential.",
   genai="Phase 4 is reporting, where generative AI drafts CSRD, SECR, BRSR or voluntary disclosures from the now-trustworthy data — grounded, with a human owner.",
   faq3q="Where should a drinks producer start with sustainability data?", faq3a="With meters, not models or reports. Sub-meter energy, water and waste and baseline per unit produced; only then do analytics, automation and AI-drafted reporting pay off. Buying the top of the pyramid before the base is the classic, costly mistake.",
   region=REG, limit="The roadmap is a ladder, not a leap — skipping metering to jump to an AI dashboard or a generated report gives confident output over hollow data. And reporting frameworks differ by region, so the top rung is shaped by where you operate.",
   bottom="Sustainability is a phased data climb: meter, baseline, optimise, automate, report. Start at the bottom — sub-metering — and earn each rung. The producers who win got boring about measurement first.",
   links=[("collect your data before AI","/2026/collect-your-data-before-ai/"),("building a brewery data foundation","/2024/building-brewery-data-foundation-ai/")]),
]


def pillar_article():
    s=PILLAR
    rad=radial_svg("Sustainability levers for a drinks business","Cut waste",
        ["Energy / power","Energy / heat","Water ratio","Effluent","Carbon (1/2/3)","By-products","Packaging","Reporting"],
        "Every lever runs on data and AI — and a regional reporting layer sits on top.")
    d2=steps_svg("The improvement loop, every lever",[("Meter","energy, water, waste"),("Baseline","per unit produced"),("Reduce","AI finds the waste"),("Verify","measured savings"),("Report","UK/EU/US/India")],
        "One loop behind every lever — meter, baseline, reduce, verify, report.")
    faqs=[("How can a beer, wine or whiskey business become more sustainable with AI?", s["ai"]),
          ("Where do Claude and ChatGPT fit in sustainability?", s["genai"]),
          (s["faq3q"], s["faq3a"])]
    links=" · ".join(L(t,u) for t,u in s["links"])
    body=[fm(s["title"],s["desc"],s["date"],["esg","sustainability","energy","water","carbon"],faqs),"",
      f"**Short answer: {s['short']}**","",s["intro"],"",f"Related: {links}.","",rad,"",
      "## The levers, in one place\n",
      "- **Energy** — refrigeration, compressed air, distillation heat and winery cooling: meter, forecast and optimise.\n- **Water** — the water-to-product ratio, effluent load and CIP: the clearest efficiency KPIs in drinks.\n- **Carbon** — Scope 1, 2 and especially Scope 3 (packaging and transport), built on real data.\n- **Circular** — spent grain, pomace and draff routed to their highest value, not landfill.\n- **Reporting** — UK, EU, US and India frameworks, drafted by generative AI over verified data.","",
      "## Measure first, model second\n",s["measure"],"",
      f"## Where AI and data cut {s['lever']}\n",s["ai"],"",
      "## Where generative AI (Claude, ChatGPT) helps\n",s["genai"]+" It drafts; a person verifies anything bound for a regulator.","",
      "## The rules, region by region\n",REG,"",d2,"",
      "## Where it breaks\n",s["limit"],"",
      "## The bottom line\n",s["bottom"],"",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",f"**{faqs[1][0]}**\n{faqs[1][1]}\n",f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      f"*Part of the {L(FOOT[0],FOOT[1])} track.*",""]
    return "\n".join(body)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    jobs=[(f"{PILLAR['date']}-{PILLAR['slug']}.md", pillar_article())]
    for s in SPECS: jobs.append((f"{s['date']}-{s['slug']}.md", article(s)))
    for fname,content in jobs:
        if a.write: (POSTS/fname).write_text(content,encoding="utf-8")
        print(("WROTE " if a.write else "WOULD WRITE ")+fname)
    print("total:",len(jobs))


if __name__=="__main__":
    main()
