#!/usr/bin/env python3
"""
Generate two sets of articles:
  A) Lager-brewery SALES blueprints: a pillar + 5 channel blueprints
     (distributors, off-premise, on-premise, national accounts, e-commerce).
  B) AI / GenAI phased ADOPTION guides for beer, whiskey and wine companies.

House format (answer-first, sections, FAQ, track footer) + two inline-SVG
diagrams each. Backdated into 2026 gaps.

Usage: python tools/gen_sales_and_ai_articles.py --write   (omit for dry run)
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent; POSTS=ROOT/"_posts"
BG="#fdfbf7"; INK="#1c1a17"; MUTED="#6b6258"; AMBER="#b45309"; PEACH="#f7ece0"
LINE="#e0d8cc"; WINE="#7a1f3d"; OAK="#8a5a2b"; OLIVE="#5b7a1f"; WINEBG="#f4e9ee"


def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def L(text,url): return "["+text+"]({{ '"+url+"' | relative_url }})"
def esc_q(s): return s.replace('"',"")
def fig(svg,cap,d2=False):
    m=' data-d2="1"' if d2 else ''
    return (f'<figure{m} style="margin:1.6rem 0;text-align:center">\n{svg}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(cap)}</figcaption>\n</figure>')


def steps_svg(title, accent, chip, steps, cap):
    n=len(steps); W=1000; bw=int((W-40-(n-1)*24)/n); by,bh=80,150; cy=by+bh//2
    p=[f'<rect x="0" y="0" width="{W}" height="270" fill="{BG}"/>',
       f'<text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    xs=[20+i*(bw+24) for i in range(n)]
    for i,(lab,sub) in enumerate(steps):
        x=xs[i]; cx=x+bw//2
        p.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="{chip}" stroke="{accent}" stroke-width="1.5"/>')
        p.append(f'<circle cx="{cx}" cy="{by+34}" r="15" fill="{accent}"/><text x="{cx}" y="{by+39}" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">{i+1}</text>')
        p.append(f'<text x="{cx}" y="{cy+18}" text-anchor="middle" font-size="14" font-weight="700" fill="{INK}">{esc(lab)}</text>')
        p.append(f'<text x="{cx}" y="{cy+40}" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(sub)}</text>')
    p.append('</g>')
    p.append(f'<g fill="{accent}" stroke="{accent}" stroke-width="2">')
    for i in range(n-1):
        r=xs[i]+bw; nl=xs[i+1]
        p.append(f'<line x1="{r}" y1="{cy}" x2="{nl-7}" y2="{cy}"/><polygon points="{nl-7},{cy-5} {nl},{cy} {nl-7},{cy+5}" stroke="none"/>')
    p.append('</g>')
    svg=f'<svg viewBox="0 0 {W} 270" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return fig(svg,cap)


def funnel_svg(title, accent, stages, cap):
    W=720; p=[f'<rect x="0" y="0" width="{W}" height="320" fill="{BG}"/>',
       f'<text x="360" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>']
    cx=360; topw=460; yy=64; sh=44; gap=8; n=len(stages)
    for i,(lab,val) in enumerate(stages):
        tw=topw-i*(360//n); bw=topw-(i+1)*(360//n); y2=yy+sh
        p.append(f'<polygon points="{cx-tw/2},{yy} {cx+tw/2},{yy} {cx+bw/2},{y2} {cx-bw/2},{y2}" fill="{accent}" opacity="{1-i*0.16}"/>')
        p.append(f'<text x="{cx}" y="{yy+29}" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fff">{esc(lab)} · {esc(val)}</text>')
        yy+=sh+gap
    svg=f'<svg viewBox="0 0 {W} 320" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return fig(svg,cap,d2=True)


def radial_svg(title, accent, chip, center, spokes, cap):
    pts=[(890,210),(775,316),(500,360),(224,316),(110,210),(224,104),(500,60),(775,104)][:len(spokes)]
    p=[f'<rect x="0" y="0" width="1000" height="420" fill="{BG}"/>',
       f'<text x="500" y="24" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="{INK}">{esc(title)}</text>',
       f'<g stroke="{LINE}" stroke-width="1.5">']
    for x,y in pts: p.append(f'<line x1="500" y1="210" x2="{x}" y2="{y}"/>')
    p.append('</g><g font-family="sans-serif" font-size="11.5" text-anchor="middle">')
    for (x,y),lab in zip(pts,spokes):
        p.append(f'<rect x="{x-85}" y="{y-22}" width="170" height="44" rx="8" fill="{chip}" stroke="{accent}" stroke-width="1.5"/><text x="{x}" y="{y+4}" fill="{INK}">{esc(lab)}</text>')
    p.append('</g>')
    p.append(f'<circle cx="500" cy="210" r="64" fill="{accent}"/><text x="500" y="206" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#fff">{esc(center)}</text><text x="500" y="226" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="{chip}">by channel</text>')
    svg=f'<svg viewBox="0 0 1000 420" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return fig(svg,cap)


def ladder_svg(title, accent, chip, phases, cap):
    W=1000; n=len(phases); p=[f'<rect x="0" y="0" width="{W}" height="360" fill="{BG}"/>',
       f'<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    bw=176; base=320; rise=46
    xs=[16+i*(bw+10) for i in range(n)]
    for i,(name,lab) in enumerate(phases):
        x=xs[i]; top=base-(i+1)*rise; h=base-top
        p.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{h}" rx="6" fill="{chip}" stroke="{accent}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+bw//2}" y="{top+24}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{accent}">{esc(name)}</text>')
        p.append(f'<text x="{x+bw//2}" y="{top+44}" text-anchor="middle" font-size="11.5" fill="{INK}">{esc(lab)}</text>')
    p.append('</g>')
    p.append(f'<line x1="16" y1="334" x2="{16+n*(bw+10)-10}" y2="334" stroke="{MUTED}" stroke-width="1"/>')
    p.append(f'<text x="30" y="352" font-family="sans-serif" font-size="11.5" fill="{MUTED}">start here</text>')
    p.append(f'<text x="{W-30}" y="352" text-anchor="end" font-family="sans-serif" font-size="11.5" fill="{MUTED}">more value, more rigour →</text>')
    svg=f'<svg viewBox="0 0 {W} 360" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return fig(svg,cap)


def pyramid_svg(title, accent, chip, tiers, cap):
    W=720; cx=360; p=[f'<rect x="0" y="0" width="{W}" height="300" fill="{BG}"/>',
       f'<text x="{cx}" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    widths=[140,260,400]; ytop=70; th=62; prev=60; cols=[accent,OAK,chip]
    for i,(lab,desc) in enumerate(tiers):
        bw=widths[i]; tw=prev; y1=ytop+i*(th+6); y2=y1+th
        fillc=cols[i]; tc="#fff" if fillc!=chip else INK
        p.append(f'<polygon points="{cx-tw/2},{y1} {cx+tw/2},{y1} {cx+bw/2},{y2} {cx-bw/2},{y2}" fill="{fillc}" stroke="{accent}"/>')
        p.append(f'<text x="{cx}" y="{y1+28}" text-anchor="middle" font-size="13" font-weight="700" fill="{tc}">{esc(lab)}</text>')
        p.append(f'<text x="{cx}" y="{y1+46}" text-anchor="middle" font-size="11" fill="{tc}">{esc(desc)}</text>')
        prev=bw
    p.append('</g>')
    svg=f'<svg viewBox="0 0 {W} 300" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return fig(svg,cap,d2=True)


def fm(title,desc,date,tags,faqs):
    out=["---","layout: post",f'title: "{title}"',f'description: "{desc}"',f"date: {date} 09:00:00 -0700",f"updated: {date}",f"tags: [{', '.join(tags)}]","faq:"]
    for q,a in faqs: out+=[f'  - q: "{q}"',f'    a: "{a}"']
    out.append("---"); return "\n".join(out)


SALES_FOOT=("Sales Intelligence for Beverage","/tracks/sales-intelligence/")
STEPS=[("Segment","by volume & fit"),("Target","priority accounts"),("Offer","price-pack & program"),("Execute","POS, calls, resets"),("Measure","depletions & velocity")]

CHANNELS=[
 dict(key="distributors", date="2026-01-31", slug="lager-sales-blueprint-distributors", player="distributors & wholesalers",
   title="Lager Sales Blueprint: Winning with Distributors",
   buyer="the distributor's sales reps and management", motion="win share of the distributor's book and pull lager through on depletions, not just sell-in",
   steps=[("Segment","territories & books"),("Target","depletion-gap accounts"),("Offer","incentives & programming"),("Execute","joint calls + POS"),("Measure","depletions & days-on-hand")],
   kpis="depletions (not just shipments), distribution points (% ACV), days-on-hand, out-of-stock rate, and share of the distributor's portfolio",
   ai="A depletion forecast and an account-scoring model turn the distributor's data into a ranked call list — which accounts are slipping, which are white space.",
   links=[("distributor scorecards","/2025/distributor-management-data-scorecard/"),("depletion analytics","/2026/depletion-data-analytics/")],
   limit="shipments are not sales — if you steer on sell-in rather than depletions, you just load the distributor's warehouse and pay for it later in returns and stale beer"),
 dict(key="off-premise", date="2026-04-09", slug="lager-sales-blueprint-off-premise-retail", player="off-premise retail",
   title="Lager Sales Blueprint: Off-Premise Retail (Grocery, C-Store, Liquor)",
   buyer="the category manager and the store", motion="win shelf space, the right price-pack, and feature windows so velocity does the rest",
   steps=[("Segment","stores by format & volume"),("Target","resets & feature windows"),("Offer","price-pack & promo"),("Execute","planograms & displays"),("Measure","sell-through & velocity")],
   kpis="ACV distribution, velocity (units per store per week), share of shelf, promotional lift, and price/feature compliance",
   ai="Price-pack and promo-lift models show which pack at which price moves volume without eroding margin; a perfect-store score flags the outlets losing distribution.",
   links=[("price-pack architecture","/2025/price-pack-architecture-na-beer/"),("perfect-store execution","/2025/perfect-store-execution-ai/")],
   limit="a promo that spikes volume but trains shoppers to buy only on deal can quietly destroy margin — measure lift net of cannibalisation and forward-buying, not gross"),
 dict(key="on-premise", date="2026-04-21", slug="lager-sales-blueprint-on-premise", player="on-premise (bars & restaurants)",
   title="Lager Sales Blueprint: Winning On-Premise Tap Handles",
   buyer="the owner, GM or beverage director", motion="win and hold tap handles and menu placement, where lager throughput and brand visibility are highest",
   steps=[("Segment","venues by volume & occasion"),("Target","tap-handle openings"),("Offer","draft program & training"),("Execute","installs & menu placement"),("Measure","kegs per account & quality")],
   kpis="tap handles won and held, kegs per account per month, menu presence, draught quality (line cleaning), and staff advocacy",
   ai="An account-propensity model ranks venues by their fit and likely throughput; draught-quality data keeps the beer you fought for tasting like it should.",
   links=[("on- vs off-premise intelligence","/2025/on-premise-off-premise-intelligence/")],
   limit="a tap handle you win but don't maintain (dirty lines, slow turnover) pours flat, stale lager and costs you the brand — placement without quality follow-through backfires"),
 dict(key="national-accounts", date="2026-04-27", slug="lager-sales-blueprint-national-accounts", player="national & key accounts",
   title="Lager Sales Blueprint: National and Key Accounts",
   buyer="the national or regional category buyer", motion="win mandated authorisations through joint business plans, then defend compliance at store level",
   steps=[("Segment","chains by fit & scale"),("Target","JBP cycles"),("Offer","national price-pack + shopper marketing"),("Execute","authorise & comply"),("Measure","scan data & compliance")],
   kpis="authorisations won, distribution compliance versus the planogram, scan velocity, shopper-marketing ROI, and the JBP scorecard",
   ai="Assortment-optimisation and compliance models read scan data to show where the mandate is honoured and where authorised SKUs are missing from the shelf.",
   links=[("trade promotion optimisation","/2025/trade-promotion-optimization-breweries/")],
   limit="a national authorisation is worthless if stores don't execute it — without scan-level compliance tracking you celebrate a win that never reaches the shelf"),
 dict(key="ecommerce", date="2026-05-02", slug="lager-sales-blueprint-ecommerce-dtc", player="e-commerce, delivery apps & DTC",
   title="Lager Sales Blueprint: E-Commerce, Delivery and DTC",
   buyer="the drinker via delivery apps and online retail (and DTC where law allows)", motion="win digital availability, search presence and repeat purchase on the platforms where beer can legally sell",
   steps=[("Segment","platforms & legal geos"),("Target","listings & search"),("Offer","digital price-pack & content"),("Execute","ads & fulfilment"),("Measure","conversion & repeat")],
   kpis="listing coverage, digital share of search, conversion rate, basket size, repeat rate, and delivery on-time-in-full",
   ai="Demand-sensing and personalisation lift conversion and repeat; search-term analysis shows which queries you're winning and losing on the delivery apps.",
   links=[("beverage DTC personalisation","/2025/beverage-dtc-personalization/")],
   limit="alcohol e-commerce is tightly regulated and varies by jurisdiction — the channel is real but bounded, so don't model it like unrestricted retail or you'll overbuild for volume that the law caps"),
]


def channel_article(c):
    title=c["title"]; player=c["player"]
    desc=f"A practical sales blueprint for lager breweries selling through {player}: how to segment, target, offer, execute and measure — with the metrics and analytics that matter."
    k0=c['kpis'].split(',')[0]
    faqs=[(f"How do lager breweries sell through {esc_q(player)}?",
           f"Run the five-step blueprint: segment {player} by volume and fit, target the priority openings, build the right price-pack and program offer, execute at the point of sale, and measure on {k0} rather than shipments. Lager is a velocity game, so availability and turnover beat one-off sell-in."),
          ("What sales metrics matter most here?",
           f"Track {c['kpis']}. The common trap is steering on shipments instead of the metric that proves the beer actually moved."),
          ("Where does data and AI help in this channel?", c['ai'])]
    d1=steps_svg(f"The blueprint: selling lager through {player}", AMBER, PEACH, c["steps"],
        "Five steps, in order — each one is only as good as the measurement that closes the loop.")
    d2=funnel_svg("From every outlet to repeat orders", AMBER,
        [("Universe","all outlets"),("Targeted","priority"),("Sold-in","authorised"),("Stocked","on shelf/tap"),("Repeat","reordering")],
        "The sales funnel for this channel — the blueprint's job is to move outlets down it and keep them there.")
    body=[fm(title,desc,c["date"],["sales-intelligence","lager","beer-sales","commercial-planning"],faqs),"",
      f"**Short answer: selling lager through {player} is a five-step blueprint — segment, target, offer, execute, measure — run on data, not gut. Lager wins on velocity and availability, so the metric that matters is {k0}, not shipments. Below is the blueprint, the KPIs, and where analytics earns its keep.**","",
      f"Lager is a volume business with thin margins: it's won by being available, fresh and turning fast wherever the drinker reaches for it. The sales motion differs by market player, and for {player} the buyer is {c['buyer']} — the motion is to {c['motion']}. This is one of the {L('lager sales blueprints by channel','/2026/lager-brewery-sales-blueprints/')}.","",d1,"",
      "## The blueprint, step by step\n"]
    names=["Segment","Target","Offer","Execute","Measure"]
    expl=[f"Split {player} by volume potential and fit so effort goes where the return is.",
          "Rank the specific openings — the depletion gaps, resets, tap openings or authorisations — into a call list.",
          "Build the price-pack, program and incentive that fits this channel's economics.",
          "Do the unglamorous work at the point of sale: calls, planograms, installs, displays.",
          f"Close the loop on {k0} and feed it back into next cycle's targeting."]
    for i,(nm,ex) in enumerate(zip(names,expl)):
        body.append(f"{i+1}. **{nm}** — {ex}")
    body+=["","## The metrics that matter\n",
      f"Steer on {c['kpis']}. {c['ai']}","",d2,"",
      "## The data and AI stack behind it\n",
      "At scale this runs on a modern stack, not spreadsheets. **Data engineering** pipelines land depletions, scan and CRM data into a cloud **lakehouse or warehouse** — on **AWS** (S3, Redshift, SageMaker, Bedrock) or **Azure** (Fabric or Synapse, Azure ML, Azure OpenAI). On top, **AI / ML** runs the forecasting, account scoring and price-and-promo models; **generative AI** copilots draft account plans and answer questions in plain language; and a **vector database** (pgvector, Pinecone, Azure AI Search, OpenSearch) powers semantic search and RAG over account notes, distributor agreements and rep call history — so a rep can ask \"what did we promise this account last quarter?\" and get a grounded answer. The stack is the engine; the blueprint is the steering.","",
      "## Where this blueprint breaks\n",
      f"The honest caveat for this channel: {c['limit']}. The blueprint is a discipline, not a guarantee — it works when the measurement is real and the follow-through happens.","",
      "## The bottom line\n",
      f"For {player}, lager sales come down to availability and velocity, and the five-step blueprint keeps the team honest about both. Run it on {k0}, link it to "+L("the channel overview",'/2026/lager-brewery-sales-blueprints/')+", and let the data pick the next account.","",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
      f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
      f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      "Related: "+L(c["links"][0][0],c["links"][0][1])+(" · "+L(c["links"][1][0],c["links"][1][1]) if len(c["links"])>1 else "")+".","",
      f"*Part of the {L(SALES_FOOT[0],SALES_FOOT[1])} track.*",""]
    return "\n".join(body)


def lager_pillar():
    title="Beer Sales Blueprints for Lager Breweries: Five Plays by Channel"
    desc="How lager breweries sell, market player by market player — distributor, off-premise, on-premise, national accounts and e-commerce — with a use-case blueprint and the metrics for each channel."
    faqs=[("How do lager breweries grow sales?",
           "By winning availability and velocity across five market players — distributors, off-premise retail, on-premise, national accounts and e-commerce — each with its own buyer and sales motion. Lager's thin margins mean the game is turning volume fast wherever the drinker reaches for it, measured on depletions and velocity rather than shipments."),
          ("What is a sales blueprint?",
           "A repeatable five-step play — segment, target, offer, execute, measure — adapted to each channel. It turns selling from gut feel into a disciplined loop where the next account is chosen from data and every cycle is measured."),
          ("Which sales channel matters most for lager?",
           "It depends on the market, but distribution breadth (distributors and off-premise retail) drives the volume base, on-premise drives visibility, national accounts drive scale, and e-commerce is a bounded but growing add-on. The blueprint is the same shape; the buyer and metrics differ.")]
    rad=radial_svg("How lager breweries sell — five market players", AMBER, PEACH, "Lager sales",
        ["Distributors","Off-premise retail","On-premise","National accounts","E-commerce / DTC"],
        "One brewery, five market players — each needs its own blueprint, run on its own metrics.")
    steps=steps_svg("The blueprint every channel shares", AMBER, PEACH, STEPS,
        "Segment, target, offer, execute, measure — the shape is constant; the content changes by channel.")
    body=[fm(title,desc,"2026-01-16",["sales-intelligence","lager","beer-sales","commercial-planning"],faqs),"",
      "**Short answer: lager is a volume game won on availability and velocity, and it's sold through five market players — distributors, off-premise retail, on-premise, national accounts and e-commerce. Each needs its own use-case blueprint, but they share one shape: segment, target, offer, execute, measure. Below is the map and a link to each channel's blueprint.**","",
      "Lagers live or die on being everywhere, fresh, and turning fast. That makes sales less about persuasion and more about a disciplined, measured motion repeated across every channel. The buyer and the metrics change by market player; the five-step blueprint does not. It connects to the bigger picture in "+L("route-to-market for beer",'/2025/route-to-market-beer-vs-na/')+".","",rad,"",
      "## The five channel blueprints\n"]
    for c in CHANNELS:
        body.append(f"- **{c['player'].capitalize()}** — {c['motion'][0].upper()+c['motion'][1:]}. {L('Read the blueprint','/2026/'+c['slug']+'/')}.")
    body+=["","## The blueprint they share\n",
      "Every channel runs the same loop, only the content differs: **segment** the market players by volume and fit, **target** the specific openings, build the **offer** that fits the channel's economics, **execute** at the point of sale, and **measure** on depletions and velocity — then feed it back.","",steps,"",
      "## The data and AI stack behind it\n",
      "At scale, every blueprint here rides a modern data and AI stack rather than spreadsheets. **Data engineering** pipelines feed depletions, scan and CRM data into a cloud **lakehouse or warehouse** — on **AWS** (S3, Redshift, SageMaker, Bedrock) or **Azure** (Fabric or Synapse, Azure ML, Azure OpenAI). On top, **AI / ML** runs the forecasts and the account, price and promo models; **generative AI** copilots draft account plans and answer plain-language questions; and a **vector database** (pgvector, Pinecone, Azure AI Search, OpenSearch) powers semantic search and RAG over account notes and rep history. The stack is the engine; the blueprint is the steering.","",
      steps_svg("The data & AI stack under the blueprint", AMBER, PEACH, [("Sources","depletions, scan, CRM"),("Data engineering","pipelines"),("Cloud lakehouse","AWS / Azure"),("AI layer","ML · GenAI · vectors"),("Sales team","decisions")], "Sources to decision: data engineering and a cloud lakehouse feed an AI layer — machine learning, generative AI and a vector database — that the sales team acts on."),"",
      "## Where it breaks\n",
      "Two honest limits. First, **shipments are not sales** — every blueprint here steers on depletions and velocity, because selling-in to a distributor or a retailer's back room just defers the problem. Second, **lager's thin margins punish bad promotion** — volume bought with deep, untracked discounts can lose money, so measure lift net of cannibalisation. The blueprint is a discipline; the data keeps it honest.","",
      "## The bottom line\n",
      "Lager sales are won channel by channel, with the same five-step blueprint tuned to each market player and run on the right metric. Start with the channel that carries your volume, measure on depletions, and let the data choose the next account. Pick a blueprint above to go deep.","",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
      f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
      f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      f"*Part of the {L(SALES_FOOT[0],SALES_FOOT[1])} track.*",""]
    return "\n".join(body)


AIBEV={
 "beer": dict(noun="brewery", date="2026-01-06", slug="how-a-brewery-starts-with-ai-and-gen-ai", track="brewing-science",
   foot=("Brewing Science & AI","/tracks/brewing-science-ai/"), accent=AMBER, chip=PEACH,
   ex0="put a scale on the spent-grain auger and log every batch's gravity and temperature",
   ex1="a Power BI view of batch KPIs, COGS per hectolitre and depletions",
   ex2="a stuck-fermentation or demand-forecast model",
   ex3="a Claude copilot that drafts the TTB report and answers questions over your data",
   ex4="an agent that assembles the weekly ops report for sign-off",
   plat=("Microsoft Fabric for breweries","/2026/microsoft-fabric-for-breweries-20-use-cases/"),
   claude=("the Claude ecosystem for breweries","/2026/claude-ai-claude-code-for-breweries/")),
 "whiskey": dict(noun="distillery", date="2026-02-04", slug="how-a-distillery-starts-with-ai-and-gen-ai", track="distilling-maturation",
   foot=("Distilling &amp; Maturation","/tracks/distilling-maturation/"), accent=OAK, chip=PEACH,
   ex0="record every regauge so the cask ledger is real, not estimated",
   ex1="a Power BI view of maturing stock, cask inventory and valuation",
   ex2="an angel's-share or bottling-maturity model",
   ex3="a Claude copilot that drafts the maturing-stock report and answers cask questions",
   ex4="an agent that assembles the weekly warehouse and valuation report for sign-off",
   plat=("Microsoft Fabric for distilleries","/2026/microsoft-fabric-for-distilleries-20-use-cases/"),
   claude=("the Claude ecosystem for distilleries","/2026/claude-ai-claude-code-for-distilleries/")),
 "wine": dict(noun="winery", date="2026-03-27", slug="how-a-winery-starts-with-ai-and-gen-ai", track="winemaking",
   foot=("Winemaking &amp; AI","/tracks/winemaking-ai/"), accent=WINE, chip=WINEBG,
   ex0="log ferment Brix and temperature and keep a clean lot ledger from crush",
   ex1="a Power BI view of barrel inventory, vintage KPIs and DTC sales",
   ex2="a yield, ripeness or harvest-date model",
   ex3="a Claude copilot that drafts club emails and answers inventory questions",
   ex4="an agent that assembles the weekly cellar and DTC report for sign-off",
   plat=("Microsoft Fabric for wineries","/2026/microsoft-fabric-for-wineries-20-use-cases/"),
   claude=("the Claude ecosystem for wineries","/2026/claude-ai-claude-code-for-wineries/")),
}


def ai_guide(bev_key):
    A=AIBEV[bev_key]; noun=A["noun"]
    title=f"How a {noun.capitalize()} Should Start with AI and Gen AI: The Phases"
    desc=f"A phased roadmap for a {noun} adopting AI and generative AI — from collecting data to dashboards, predictive models, GenAI copilots and agents — with what to do, need and watch at each phase."
    faqs=[(f"How should a {noun} start with AI?",
           f"Not with AI — with data. Phase 0 is measuring and collecting: {A['ex0']}. Only once you have a clean, single source of truth do dashboards (Phase 1), predictive models (Phase 2), generative AI (Phase 3) and agents (Phase 4) pay off. Skipping the foundation is the most common and most expensive mistake."),
          (f"What are the phases of AI adoption for a {noun}?",
           "Five: Phase 0 collect and measure; Phase 1 see it (dashboards/BI); Phase 2 predict it (machine learning); Phase 3 generate and assist (generative AI copilots); Phase 4 automate it (agents with human oversight). Each phase builds on the last."),
          (f"Where does generative AI fit for a {noun}?",
           f"At Phase 3, once the data and analytics exist: {A['ex3']}. Generative AI drafts, explains and answers in plain language, but it must be grounded in your data and a human owns anything touching safety, compliance or a measurement of record.")]
    ladder=ladder_svg(f"The AI adoption phases for a {noun}", A["accent"], A["chip"],
        [("Phase 0","Collect & measure"),("Phase 1","See it (BI)"),("Phase 2","Predict it (ML)"),("Phase 3","Generate (GenAI)"),("Phase 4","Automate (agents)")],
        "Climb in order — each phase stands on the data and trust built by the one before it.")
    pyr=pyramid_svg("Everything sits on the data", A["accent"], A["chip"],
        [("AI & GenAI","copilots, agents, models"),("Analytics","dashboards & KPIs"),("Data foundation","meters, logs, one source of truth")],
        "The pyramid is the point: GenAI at the top is only as good as the measured data at the base.")
    body=[fm(title,desc,A["date"],[A["track"],"ai-adoption","generative-ai","data-strategy",bev_key],faqs),"",
      f"**Short answer: a {noun} should start with data, not AI. The path has five phases — collect and measure, see it (dashboards), predict it (machine learning), generate and assist (generative AI), and automate it (agents) — each built on the last. Below is what to do, what you need, and what to watch at each phase. The most expensive mistake is buying AI before the data foundation exists.**","",
      f"Every {noun} wants to know where to start with AI. The honest answer disappoints and then pays off: start by {A['ex0']}. AI is the top of a pyramid that stands on measured data — skip the base and the clever part has nothing to stand on. This builds on {L('collecting your data before AI','/2026/collect-your-data-before-ai/')}.","",ladder,"",
      "## Phase 0 — Collect and measure\n",
      f"Before any model, get a clean, single source of truth. For a {noun}, that means {A['ex0']} — meters, logs and records that are trustworthy. You can't optimise what you don't measure, and most failed AI projects die here, not in the algorithm.","",
      "## Phase 1 — See it (dashboards and BI)\n",
      f"Once the data exists, make it visible: {A['ex1']}. Dashboards turn data into decisions and surface the questions worth modelling later. This phase alone pays for the foundation.","",
      "## Phase 2 — Predict it (machine learning)\n",
      f"With history in place, add prediction: {A['ex2']}. Models earn their keep on the routine and steady; they predict the rare failure poorly, so treat them as decision support, not autopilot.","",
      "## Phase 3 — Generate and assist (generative AI)\n",
      f"Now generative AI fits: {A['ex3']}. Grounded in your data — see the {L(A['claude'][0],A['claude'][1])} guide — it drafts, explains and answers in plain language, with a human checking anything that reaches a regulator, a label or a customer.","",
      "## Phase 4 — Automate it (agents)\n",
      f"Finally, agents close routine loops: {A['ex4']}. This is the most powerful and the most over-sold phase — keep a person approving anything consequential, and only automate what you already trust by hand.","",pyr,"",
      "## Where companies get it wrong\n",
      "Three honest limits. First, **don't skip phases** — buying a GenAI copilot before you have clean data gives confident answers over rubbish. Second, **a model never owns a measurement of record** — excise, safety and label figures trace to instruments and sign-off, not predictions. Third, **the platform is not the point** — whether you build on "+L(A['plat'][0],A['plat'][1])+" or a spreadsheet, the phases are the same; tools serve the roadmap, not the reverse.","",
      "## The bottom line\n",
      f"A {noun}'s AI journey is a ladder, not a leap: collect, see, predict, generate, automate. Start at Phase 0 — {A['ex0']} — and earn each rung before the next. The companies that win with AI are the ones that got boring about data first.","",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
      f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
      f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      f"*Part of the {L(A['foot'][0],A['foot'][1])} track.*",""]
    return "\n".join(body)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    jobs=[("2026-01-16-lager-brewery-sales-blueprints.md", lager_pillar())]
    for c in CHANNELS: jobs.append((f"{c['date']}-{c['slug']}.md", channel_article(c)))
    for k in ("beer","whiskey","wine"): jobs.append((f"{AIBEV[k]['date']}-{AIBEV[k]['slug']}.md", ai_guide(k)))
    for fname,content in jobs:
        if a.write: (POSTS/fname).write_text(content,encoding="utf-8")
        print(("WROTE " if a.write else "WOULD WRITE ")+fname)


if __name__=="__main__":
    main()
