#!/usr/bin/env python3
"""
Generate the Databricks and Snowflake article series (12 posts):
  platform (databricks, snowflake) x beverage (beer, whiskey, wine)
  x kind (use_cases, verticals)

Each post follows the house format (answer-first, sections, FAQ, track footer)
and carries two bespoke inline-SVG diagrams. Backdated into 2026 gaps.

Usage:  python tools/gen_platform_articles.py --write   (omit --write for dry run)
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
BG="#fdfbf7"; INK="#1c1a17"; MUTED="#6b6258"; AMBER="#b45309"; PEACH="#f7ece0"
LINE="#e0d8cc"; WINE="#7a1f3d"; OAK="#8a5a2b"; BLUE="#2f6f9f"; WINEBG="#f4e9ee"


def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def L(text,url): return "["+text+"]({{ '"+url+"' | relative_url }})"

biname_hdr=""


def arch_svg(title, accent, chip, sources, workloads, biname, bisub, people):
    p=[f'<rect x="0" y="0" width="1000" height="360" fill="{BG}"/>',
       f'<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>',
       '<g font-family="sans-serif">',
       f'<text x="105" y="76" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="1" fill="{accent}">SOURCES</text>']
    for i,s in enumerate(sources):
        y=86+i*48
        p.append(f'<rect x="20" y="{y}" width="170" height="40" rx="6" fill="{chip}" stroke="{accent}" stroke-width="1.5"/><text x="105" y="{y+25}" text-anchor="middle" font-size="12.5" fill="{INK}">{esc(s)}</text>')
    p.append(f'<rect x="220" y="70" width="560" height="225" rx="10" fill="#ffffff" stroke="{accent}" stroke-width="1.5"/>')
    p.append(f'<text x="500" y="92" text-anchor="middle" font-size="13.5" font-weight="700" fill="{accent}">{esc(biname_hdr)}</text>')
    pos=[(236,104),(502,104),(236,196),(502,196)]
    for (x,y),(nm,sub) in zip(pos,workloads):
        cx=x+131
        p.append(f'<rect x="{x}" y="{y}" width="262" height="80" rx="8" fill="{chip}" stroke="{MUTED}"/><text x="{cx}" y="{y+34}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{INK}">{esc(nm)}</text><text x="{cx}" y="{y+54}" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(sub)}</text>')
    p.append(f'<rect x="810" y="104" width="170" height="74" rx="8" fill="{accent}"/><text x="895" y="138" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{esc(biname)}</text><text x="895" y="158" text-anchor="middle" font-size="11" fill="{chip}">{esc(bisub)}</text>')
    p.append(f'<rect x="810" y="188" width="170" height="38" rx="8" fill="{chip}" stroke="{accent}" stroke-width="1.5"/><text x="895" y="212" text-anchor="middle" font-size="12.5" fill="{INK}">AI assistant</text>')
    p.append(f'<rect x="810" y="236" width="170" height="38" rx="8" fill="{chip}" stroke="{WINE}" stroke-width="1.5"/><text x="895" y="260" text-anchor="middle" font-size="12.5" fill="{WINE}">alerts</text>')
    p.append('</g>')
    p.append(f'<g fill="{accent}" stroke="{accent}" stroke-width="2"><line x1="190" y1="182" x2="213" y2="182"/><polygon points="213,177 220,182 213,187" stroke="none"/><line x1="780" y1="141" x2="803" y2="141"/><polygon points="803,136 810,141 803,146" stroke="none"/></g>')
    p.append(f'<text x="500" y="332" text-anchor="middle" font-family="sans-serif" font-size="12.5" fill="{MUTED}">{esc(people)}</text>')
    svg=f'<svg viewBox="0 0 1000 360" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return _fig(svg, "One platform: every source lands once, then ingestion, streaming, analytics and AI run as workloads over it.", False)


def medallion_svg(title, accent, chip, layers, biname):
    p=[f'<rect x="0" y="0" width="1000" height="240" fill="{BG}"/>',
       f'<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    xs=[10,220,430,640]
    for x,(nm,s1,s2,col) in zip(xs,layers):
        cx=x+85
        p.append(f'<rect x="{x}" y="70" width="170" height="110" rx="8" fill="{chip}" stroke="{col}" stroke-width="1.5"/><text x="{cx}" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="{col}">{esc(nm)}</text><text x="{cx}" y="120" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(s1)}</text><text x="{cx}" y="138" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(s2)}</text>')
    p.append(f'<rect x="850" y="70" width="140" height="110" rx="8" fill="{accent}"/><text x="920" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{esc(biname)}</text>')
    p.append('</g>')
    p.append(f'<g fill="{accent}" stroke="{accent}" stroke-width="2">')
    for x in [180,390,600,810]:
        p.append(f'<line x1="{x}" y1="125" x2="{x+33}" y2="125"/><polygon points="{x+33},120 {x+40},125 {x+33},130" stroke="none"/>')
    p.append('</g>')
    svg=f'<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return _fig(svg, "Each layer adds trust: raw lands, gets cleaned, becomes decision-ready, and BI reads it live.", True)


def radial_svg(title, accent, chip, center, spokes):
    pts=[(890,210),(775,316),(500,360),(224,316),(110,210),(224,104),(500,60),(775,104)]
    p=[f'<rect x="0" y="0" width="1000" height="420" fill="{BG}"/>',
       f'<text x="500" y="24" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="{INK}">{esc(title)}</text>',
       f'<g stroke="{LINE}" stroke-width="1.5">']
    for x,y in pts: p.append(f'<line x1="500" y1="210" x2="{x}" y2="{y}"/>')
    p.append('</g><g font-family="sans-serif" font-size="11.5" text-anchor="middle">')
    for (x,y),lab in zip(pts,spokes):
        p.append(f'<rect x="{x-80}" y="{y-22}" width="160" height="44" rx="8" fill="{chip}" stroke="{accent}" stroke-width="1.5"/><text x="{x}" y="{y+4}" fill="{INK}">{esc(lab)}</text>')
    p.append('</g>')
    p.append(f'<circle cx="500" cy="210" r="62" fill="{accent}"/><text x="500" y="206" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#fff">{esc(center)}</text><text x="500" y="226" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="{chip}">every vertical</text>')
    svg=f'<svg viewBox="0 0 1000 420" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return _fig(svg,"One governed platform reaching every part of the business — not a tool per department.",False)


def gov_svg(title, accent, chip, plat, govern, share):
    boxes=[(plat,40),(govern,300),(share,560),("Consumers",820)]
    subs=["one copy of data","RBAC, lineage, masking","governed sharing","BI, AI, partners"]
    p=[f'<rect x="0" y="0" width="1000" height="240" fill="{BG}"/>',
       f'<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    for (lab,x),sub in zip(boxes,subs):
        fill=accent if (lab==plat or lab=="Consumers") else chip
        tc="#fff" if fill==accent else INK
        subcol=chip if tc=="#fff" else MUTED
        p.append(f'<rect x="{x}" y="95" width="140" height="80" rx="8" fill="{fill}" stroke="{accent}" stroke-width="1.5"/><text x="{x+70}" y="130" text-anchor="middle" font-size="12.5" font-weight="700" fill="{tc}">{esc(lab)}</text><text x="{x+70}" y="150" text-anchor="middle" font-size="10.5" fill="{subcol}">{esc(sub)}</text>')
    p.append('</g>')
    p.append(f'<g fill="{accent}" stroke="{accent}" stroke-width="2">')
    for x in [180,440,700]:
        p.append(f'<line x1="{x}" y1="135" x2="{x+33}" y2="135"/><polygon points="{x+33},130 {x+40},135 {x+33},140" stroke="none"/>')
    p.append('</g>')
    svg=f'<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>"
    return _fig(svg,"Govern once, share safely: the same data reaches BI, AI and partners under one set of controls.",True)


def _fig(svg, caption, d2):
    mark=' data-d2="1"' if d2 else ''
    return (f'<figure{mark} style="margin:1.6rem 0;text-align:center">\n{svg}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(caption)}</figcaption>\n</figure>')


PLAT = {
 "databricks": dict(name="Databricks", accent=AMBER, hdr="Databricks Lakehouse Platform",
    ingest="Lakeflow & Auto Loader", stream="Structured Streaming & Delta Live Tables",
    engineer="the Delta Lakehouse & Spark", analyse="Databricks SQL & AI/BI",
    aigs="Mosaic AI, Unity Catalog & Delta Sharing", bi="Databricks SQL", bisub="AI/BI dashboards",
    govern="Unity Catalog", share="Delta Sharing",
    layers=[("Bronze","raw, as landed","Delta",OAK),("Silver","cleaned &","conformed",AMBER),("Gold","decision-ready","KPIs",AMBER),("Lakehouse","Unity Catalog","governed",MUTED)],
    blurb="Databricks is a lakehouse — Delta Lake tables on your own cloud storage, with Spark, streaming, SQL, governance (Unity Catalog) and ML (MLflow, Mosaic AI) over one copy of the data."),
 "snowflake": dict(name="Snowflake", accent=BLUE, hdr="Snowflake Data Cloud",
    ingest="Snowpipe & Snowpipe Streaming", stream="Snowpipe Streaming, Streams & Tasks",
    engineer="Dynamic Tables & Snowpark", analyse="Snowsight & Cortex Analyst",
    aigs="Cortex AI, RBAC & Secure Data Sharing", bi="Snowsight", bisub="dashboards + Cortex",
    govern="RBAC & masking", share="Secure Data Sharing",
    layers=[("RAW","as ingested","tables",OAK),("STAGING","cleaned &","conformed",BLUE),("MART","decision-ready","models",BLUE),("Governance","RBAC + tags","+ sharing",MUTED)],
    blurb="Snowflake is a data cloud — elastic virtual warehouses over shared storage, with streaming ingest (Snowpipe), in-database transforms (Dynamic Tables, Snowpark), built-in LLM functions (Cortex AI) and secure data sharing."),
}

BEV = {
 "beer": dict(noun="brewery", plural="breweries", track="brewing-science", chip=PEACH,
    footer=("Brewing Science & AI","/tracks/brewing-science-ai/"),
    fabric="/2026/microsoft-fabric-for-breweries-20-use-cases/", claude="/2026/claude-ai-claude-code-for-breweries/",
    sources=["Brewhouse SCADA / PLC","Brewing ERP","Distributor depletions","Taproom POS"],
    uc=[("Ingest and unify",["Land brewhouse SCADA and historian tags","Replicate the brewing ERP","Bring in distributor depletion files","Capture fermentation sensor streams (gravity, temp, pressure)"]),
        ("Monitor in real time",["Store high-frequency tank telemetry for fast queries","A live view of every active fermenter","Alert when a fermentation stalls or drifts out of band","Live packaging-line OEE from line counts"]),
        ("Engineer and model",["Clean raw telemetry into per-batch records","Compute attenuation, ABV and efficiency per batch","Model COGS per hectolitre and margin by SKU","Serve gold batch KPIs to BI with no refresh lag"]),
        ("Analyse and report",["Grain-to-glass traceability (lot to tank to package to shipment)","QC control charts across batches","Depletions and sell-through, distributor plus internal","Margin by SKU and channel"]),
        ("Predict, govern and share",["A stuck-fermentation or curve model","Natural-language questions over the data","Lineage and certified datasets for TTB and finance","Share certified reports with leadership and distributors"])],
    verts=[("R&D & recipe","store every batch and trial so recipe calls draw on history, not memory"),
        ("Production","land brewhouse and fermentation data continuously and compute batch KPIs as each brew finishes"),
        ("Quality / QC","track specs and control charts across batches and trace any lot grain-to-glass"),
        ("Supply & procurement","reconcile ERP stock with supplier data to see what is below par and what a malt or hop move costs"),
        ("Sales & distribution","blend distributor depletions with internal shipments for one sell-through view"),
        ("Marketing & brand","bring campaign and social data alongside sales to see what actually moved volume"),
        ("Finance","model COGS per hectolitre and margin by SKU and channel on governed numbers"),
        ("Compliance (TTB)","assemble excise and reporting figures from traceable records, with lineage for audit")]),
 "whiskey": dict(noun="distillery", plural="distilleries", track="distilling-maturation", chip=PEACH,
    footer=("Distilling &amp; Maturation","/tracks/distilling-maturation/"),
    fabric="/2026/microsoft-fabric-for-distilleries-20-use-cases/", claude="/2026/claude-ai-claude-code-for-distilleries/",
    sources=["Still telemetry","Cask / warehouse system","Warehouse climate","ERP & bottling"],
    uc=[("Ingest and unify",["Land still and distillation telemetry","Replicate the cask and warehouse system","Bring in warehouse scan and movement logs","Capture warehouse climate streams (temp, humidity)"]),
        ("Monitor in real time",["Store years of rackhouse microclimate for fast queries","A live view of a spirit run and its cut timing","Alert on a still excursion or humidity drift","Live bottling-line monitoring"]),
        ("Engineer and model",["Clean raw cask events into a clean ledger","Compute angel's-share loss per cask over regauges","Model maturing-stock value, duty and bond","Serve cask inventory to BI with no refresh lag"]),
        ("Analyse and report",["Cask maturation tracking (age, strength, location)","Rackhouse microclimate versus evaporation","Maturing-stock valuation for finance and auditors","Blend component availability across warehouses"]),
        ("Predict, govern and share",["Angel's-share and bottling-maturity models","Natural-language questions over the warehouse","Lineage and certified data for excise and valuation","Share certified maturing-stock data with finance and auditors"])],
    verts=[("New make & R&D","store every run and trial so spirit decisions draw on the record"),
        ("Distillation","land still telemetry and flag a cut or excursion as it happens"),
        ("Quality / QC","track new-make and cask COAs and trace any parcel of spirit"),
        ("Cask & warehouse","keep a living cask ledger with loss, location and age on every cask"),
        ("Sales & distribution","blend distributor depletions with allocation and release data"),
        ("Marketing & brand","tie campaign and release data to sell-through by expression"),
        ("Finance & valuation","value bonded maturing stock on governed, traceable figures"),
        ("Excise & compliance","assemble duty and bond figures from measured regauges, with lineage")]),
 "wine": dict(noun="winery", plural="wineries", track="winemaking", chip=WINEBG,
    footer=("Winemaking &amp; AI","/tracks/winemaking-ai/"),
    fabric="/2026/microsoft-fabric-for-wineries-20-use-cases/", claude="/2026/claude-ai-claude-code-for-wineries/",
    sources=["Vineyard sensors / NDVI","Cellar & lab data","Winery ERP","DTC / e-commerce"],
    uc=[("Ingest and unify",["Land cellar tank telemetry and lab panels","Replicate the winery ERP and DTC system","Bring in vineyard sensor, weather and NDVI data","Capture fermentation streams (Brix, temperature)"]),
        ("Monitor in real time",["Store fermentation time series across every tank","A live view of each active ferment's Brix and temperature","Alert on a stuck ferment, temperature spike or due pump-over","Live bottling-line monitoring"]),
        ("Engineer and model",["Clean vineyard and cellar data into a lot ledger","Run blend-trial and barrel-lot aggregation at scale","Model COGS per case and margin by varietal and channel","Serve vintage and DTC data to BI with no refresh lag"]),
        ("Analyse and report",["Barrel ageing and cellar inventory","Vineyard yield and harvest readiness","DTC and wine-club analytics (retention, lifetime value)","Tasting and blending sensory views"]),
        ("Predict, govern and share",["Yield, ripeness and harvest-date models","Natural-language questions over the vintage","Lineage and certified data for allocations and TTB/COLA","Share certified vintage and inventory data with the trade"])],
    verts=[("Vineyard & viticulture","bring sensor, weather and NDVI data together to time the pick"),
        ("Winemaking & cellar","land ferment and lab data and keep a lot ledger from crush to bottle"),
        ("Lab / quality","track chemistry and panels and trace any lot or barrel"),
        ("Barrel & supply","keep a barrel program with age, cooperage and topping on every barrel"),
        ("Sales & distribution","blend distributor depletions with allocation and release data"),
        ("Marketing & brand","tie campaign and club data to sell-through by varietal"),
        ("Finance","model COGS per case and margin by varietal and channel"),
        ("Compliance & DTC","assemble TTB/COLA and allocation records from traceable data")]),
}

DATES = {
 ("databricks","beer","use"):"2026-01-10",("databricks","beer","vert"):"2026-01-23",
 ("databricks","whiskey","use"):"2026-02-02",("databricks","whiskey","vert"):"2026-02-09",
 ("databricks","wine","use"):"2026-02-15",("databricks","wine","vert"):"2026-02-21",
 ("snowflake","beer","use"):"2026-02-27",("snowflake","beer","vert"):"2026-03-05",
 ("snowflake","whiskey","use"):"2026-03-11",("snowflake","whiskey","vert"):"2026-03-17",
 ("snowflake","wine","use"):"2026-03-24",("snowflake","wine","vert"):"2026-04-02",
}


def use_slug(p,b): return f"{p}-for-{BEV[b]['plural']}-20-use-cases"
def vert_slug(p,b): return f"{p}-across-the-{BEV[b]['noun']}-business"
def use_url(p,b): return f"/2026/{use_slug(p,b)}/"
def vert_url(p,b): return f"/2026/{vert_slug(p,b)}/"


def fm(title, desc, date, tags, faqs):
    out=["---","layout: post",f'title: "{title}"',f'description: "{desc}"',
         f"date: {date} 09:00:00 -0700",f"updated: {date}",f"tags: [{', '.join(tags)}]","faq:"]
    for q,a in faqs: out+=[f'  - q: "{q}"',f'    a: "{a}"']
    out.append("---")
    return "\n".join(out)


def use_cases_article(plat_key, bev_key):
    global biname_hdr
    P=PLAT[plat_key]; B=BEV[bev_key]; pn=P["name"]; noun=B["noun"]
    title=f"{pn} for {B['plural'].capitalize()}: 20 Use Cases"
    desc=f"How a {noun} uses {pn} end to end — ingestion, real-time monitoring, {P['engineer']}, BI and AI — across 20 concrete use cases grouped by capability."
    faqs=[(f"What is {pn} used for in a {noun}?",
           f"{pn} unifies a {noun}'s data — production telemetry, ERP, sales and quality — then runs ingestion ({P['ingest']}), real-time monitoring ({P['stream']}), modelling on {P['engineer']} and BI ({P['bi']}) over one copy, so every team works from the same numbers."),
          (f"Can {pn} handle real-time {noun} data?",
           f"Yes. {P['stream']} ingests sensor streams continuously and serves them for fast queries and live dashboards, with alerts when a process drifts out of band."),
          (f"Does {pn} replace our ERP or historian?",
           f"No. {pn} sits beside them: it ingests or replicates their data into one governed copy for analytics and AI. The ERP and historian stay your systems of record; {pn} is where the cross-system questions get answered.")]
    biname_hdr=P["hdr"]
    arch=arch_svg(f"A {noun} on {pn} — one copy of the data", P["accent"], B["chip"], B["sources"],
        [("Ingestion",P["ingest"]),("Storage & model",P["engineer"]),("Streaming",P["stream"]),("AI & ML",P["aigs"].split(",")[0])],
        P["bi"], P["bisub"], "production, quality, finance and sales all read the same governed data")
    med=medallion_svg(f"From raw data to a live {noun} view on {pn}", P["accent"], B["chip"], P["layers"], P["bi"])
    body=[fm(title,desc,DATES[(plat_key,bev_key,"use")],[B["track"],plat_key,"data-platform","power-bi",bev_key],faqs),"",
        f"**Short answer: {pn} gives a {noun} one governed home for every data source — production telemetry, ERP, quality and sales — then layers ingestion ({P['ingest']}), real-time monitoring ({P['stream']}), modelling on {P['engineer']} and BI ({P['bi']}) on top. Below are 20 use cases grouped by capability. It's a platform, not magic — the value still comes from clean data and a real question.**","",
        f"{P['blurb']} For a {noun} with data scattered across production, ERP and spreadsheets, that consolidation is the point. It complements the assistant-and-build view in the {L('Claude ecosystem for '+B['plural'],B['claude'])} piece, and overlaps with {L('Microsoft Fabric for '+B['plural'],B['fabric'])} — same idea, different platform.","",arch,""]
    n=1
    comps={"Ingest and unify":P["ingest"],"Monitor in real time":P["stream"],"Engineer and model":P["engineer"],"Analyse and report":P["bi"],"Predict, govern and share":P["aigs"]}
    for grp,items in B["uc"]:
        body.append(f"## {grp} ({comps[grp]})\n")
        for it in items:
            body.append(f"{n}. **{it}.**"); n+=1
        body.append("")
    body+=[med,"",
        "## Where it's oversold\n",
        f"Three honest limits. First, **it's a platform, not a fix for bad data** — replicating a messy ERP just surfaces the mess faster; the cleaning layer is the real work. Second, **compute costs money** — {pn} bills on usage, and always-on streaming plus heavy jobs add up, so size it to the workload and watch it. Third, **a model never replaces a measurement of record** — anything that touches excise, safety or a label must trace to instruments and signed-off process, not a prediction. Start with one painful question, prove it, then expand.","",
        "## The bottom line\n",
        f"{pn}'s value to a {noun} is consolidation: one governed copy, with real-time, analytics and AI as workloads over it. The 20 above are a menu — pick the two that hurt most, land them, and let the platform earn the rest. See also {L(pn+' across the '+noun+' business',vert_url(plat_key,bev_key))} for the vertical-by-vertical view.","",
        "## Frequently asked questions\n",
        f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
        f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
        f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
        f"*Part of the {L(B['footer'][0],B['footer'][1])} track.*",""]
    return "\n".join(body)


def verticals_article(plat_key, bev_key):
    P=PLAT[plat_key]; B=BEV[bev_key]; pn=P["name"]; noun=B["noun"]
    title=f"{pn} Across the {noun.capitalize()} Business, Vertical by Vertical"
    desc=f"A department-by-department tour of where {pn} helps a {noun} — from the floor through quality, supply chain, sales, marketing, finance and compliance — on one governed platform."
    faqs=[(f"Which {noun} departments benefit from {pn}?",
           f"All of them, because they share one governed copy of the data: production, quality, supply chain, sales, marketing, finance and compliance each read and contribute to the same {pn} platform instead of keeping separate spreadsheets."),
          (f"Does {pn} only help the production side of a {noun}?",
           f"No. Production telemetry is one input; the bigger win is connecting it to ERP, sales and DTC so finance sees true margin, sales sees sell-through, and compliance can assemble figures — all from the same source."),
          (f"How should a {noun} start with {pn}?",
           f"Pick the one vertical with the most painful question — often finance margin or live production — land that data on {pn}, prove the answer, then extend to the next department rather than boiling the ocean.")]
    rad=radial_svg(f"{pn} across a {noun}", P["accent"], B["chip"], pn, [v[0] for v in B["verts"]])
    gov=gov_svg(f"Govern once, share safely on {pn}", P["accent"], B["chip"], pn, P["govern"], P["share"])
    groups=[("Make it",B["verts"][0:3]),("Move it",B["verts"][3:6]),("Run it",B["verts"][6:8])]
    body=[fm(title,desc,DATES[(plat_key,bev_key,"vert")],[B["track"],plat_key,"data-platform",bev_key],faqs),"",
        f"**Short answer: on {pn}, every {noun} vertical works from one governed copy of the data — production, quality, supply chain, sales, marketing, finance and compliance. Below is the department-by-department tour: what {pn} does in each, and how they connect. The platform unifies; clean records and a real question still do the work.**","",
        f"{P['blurb']} The use-case view is in {L(pn+' for '+B['plural']+': 20 use cases',use_url(plat_key,bev_key))}; this piece walks the business instead — vertical by vertical — so each department can see itself. It complements the {L('Claude ecosystem for '+B['plural'],B['claude'])} and {L('Microsoft Fabric',B['fabric'])} pieces.","",rad,""]
    for gname,verts in groups:
        body.append(f"## {gname}\n")
        for vname,vdesc in verts:
            body.append(f"- **{vname}** — {vdesc}.")
        body.append("")
    body+=[gov,"",
        "## Where it's oversold\n",
        f"Three honest limits. First, **one platform is not one clean dataset** — each vertical still has to define its terms, and the conformed layer is real work. Second, **governance is ongoing** — {P['govern']} and certified, shared datasets need stewardship, not a one-off setup. Third, **a measurement of record stays a measurement** — excise, safety and label figures trace to instruments and sign-off, never to a model. The platform makes the verticals share; people still own the meaning.","",
        "## The bottom line\n",
        f"Seen vertical by vertical, {pn}'s value to a {noun} is the same data serving every department under one set of controls — no more reconciling spreadsheets across teams. Start with the vertical whose question hurts most, then let the shared copy pull the next one in. The 20-use-case companion is {L(pn+' for '+B['plural'],use_url(plat_key,bev_key))}.","",
        "## Frequently asked questions\n",
        f"**{faqs[0][0]}**\n{faqs[0][1]}\n",
        f"**{faqs[1][0]}**\n{faqs[1][1]}\n",
        f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
        f"*Part of the {L(B['footer'][0],B['footer'][1])} track.*",""]
    return "\n".join(body)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    made=[]
    for p in ("databricks","snowflake"):
        for b in ("beer","whiskey","wine"):
            for kind,slugfn,gen in (("use",use_slug,use_cases_article),("vert",vert_slug,verticals_article)):
                date=DATES[(p,b,kind)]; slug=slugfn(p,b)
                fname=POSTS/f"{date}-{slug}.md"; content=gen(p,b)
                made.append(fname.name)
                if a.write: fname.write_text(content,encoding="utf-8")
    print(("WROTE " if a.write else "WOULD WRITE ")+str(len(made))+" files:")
    for m in made: print("  ",m)


if __name__=="__main__":
    main()
