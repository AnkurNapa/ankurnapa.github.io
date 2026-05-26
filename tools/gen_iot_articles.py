#!/usr/bin/env python3
"""
IoT in beer/whiskey/wine making — three articles grounded in IBD-level process
knowledge: which sensors sit at which process stage, the edge-to-cloud stack,
and the AI on the streams. House format + two inline-SVG diagrams each.

Usage: python tools/gen_iot_articles.py --write
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent; POSTS=ROOT/"_posts"
BG="#fdfbf7"; INK="#1c1a17"; MUTED="#6b6258"; AMBER="#b45309"; PEACH="#f7ece0"
LINE="#e0d8cc"; WINE="#7a1f3d"; OAK="#8a5a2b"; WINEBG="#f4e9ee"


def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def L(text,url): return "["+text+"]({{ '"+url+"' | relative_url }})"
def figw(svg,cap,d2=False):
    m=' data-d2="1"' if d2 else ''
    return (f'<figure{m} style="margin:1.6rem 0;text-align:center">\n{svg}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(cap)}</figcaption>\n</figure>')


def steps_svg(title, accent, chip, steps, cap, d2=False):
    n=len(steps); W=1000; bw=int((W-40-(n-1)*24)/n); by,bh=80,150; cy=by+bh//2
    p=[f'<rect x="0" y="0" width="{W}" height="270" fill="{BG}"/>',
       f'<text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="{INK}">{esc(title)}</text>','<g font-family="sans-serif">']
    xs=[20+i*(bw+24) for i in range(n)]
    for i,(lab,sub) in enumerate(steps):
        x=xs[i]; cx=x+bw//2
        p.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="{chip}" stroke="{accent}" stroke-width="1.5"/>')
        p.append(f'<circle cx="{cx}" cy="{by+34}" r="15" fill="{accent}"/><text x="{cx}" y="{by+39}" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">{i+1}</text>')
        p.append(f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-size="13" font-weight="700" fill="{INK}">{esc(lab)}</text>')
        p.append(f'<text x="{cx}" y="{cy+38}" text-anchor="middle" font-size="11" fill="{MUTED}">{esc(sub)}</text>')
    p.append('</g>')
    p.append(f'<g fill="{accent}" stroke="{accent}" stroke-width="2">')
    for i in range(n-1):
        r=xs[i]+bw; nl=xs[i+1]
        p.append(f'<line x1="{r}" y1="{cy}" x2="{nl-7}" y2="{cy}"/><polygon points="{nl-7},{cy-5} {nl},{cy} {nl-7},{cy+5}" stroke="none"/>')
    p.append('</g>')
    return figw(f'<svg viewBox="0 0 {W} 270" width="100%" style="max-width:{W}px;height:auto" role="img" aria-label="{esc(title)}">'+"".join(p)+"</svg>",cap,d2)


def fm(title,desc,date,tags,faqs):
    out=["---","layout: post",f'title: "{title}"',f'description: "{desc}"',f"date: {date} 09:00:00 -0700",f"updated: {date}",f"tags: [{', '.join(tags)}]","faq:"]
    for q,a in faqs: out+=[f'  - q: "{q}"',f'    a: "{a}"']
    out.append("---"); return "\n".join(out)


BEV={
 "beer": dict(noun="brewery", accent=AMBER, chip=PEACH, track="brewing-science",
   foot=("Brewing Science & AI","/tracks/brewing-science-ai/"), date="2026-11-23",
   slug="iot-in-the-brewery-sensors-process",
   title="IoT in the Brewery: Sensors at Every Step, from Mash to Package",
   desc="An IBD-grounded guide to IoT in brewing — which sensors belong at mashing, lautering, the boil, fermentation and packaging, the edge-to-cloud stack, and the AI that reads the streams.",
   stages=[("Mash","temp, pH"),("Lauter","flow, turbidity"),("Boil","temp, energy"),("Ferment","gravity, temp, CO2"),("Package","DO, fill, TPO")],
   process="Walk the brewhouse the way the IBD process does — mashing, lautering, the boil and whirlpool, wort cooling, fermentation, conditioning, filtration and packaging — and each stage has a measurement that decides quality. IoT puts that measurement online: mash temperature and pH (for conversion and the right wort fermentability), lauter flow and turbidity, kettle energy and evaporation, wort cooling and dissolved oxygen at pitching, then fermentation temperature, gravity and pressure, and finally dissolved oxygen, fill level and total package oxygen at the filler.",
   sense="Inline sensors that matter: mash thermometry and pH; lauter wort turbidity and flow; an inline densitometer or refractometer for wort gravity; dissolved-oxygen probes at knockout and at the filler (oxygen is the enemy of flavour stability); and in-fermenter temperature, density and pressure so you watch attenuation in real time rather than drawing a sample.",
   faq3q="What should a brewery monitor with IoT first?", faq3a="Start where a miss is expensive and invisible: fermentation (temperature and gravity, so you catch a stall or a runaway early) and dissolved oxygen at the filler (which drives flavour stability and shelf life). Both reward continuous data over spot samples."),
 "whiskey": dict(noun="distillery", accent=OAK, chip=PEACH, track="distilling-maturation",
   foot=("Distilling &amp; Maturation","/tracks/distilling-maturation/"), date="2026-12-07",
   slug="iot-in-the-distillery-sensors-process",
   title="IoT in the Distillery: Sensors from Mash to Cask",
   desc="An IBD-grounded guide to IoT in distilling — sensors at mashing, washback fermentation, the wash and spirit stills, the spirit cut, and the maturation warehouse, plus the edge-to-cloud stack and AI.",
   stages=[("Mash","temp"),("Washback","gravity, temp, CO2"),("Still","temp, flow"),("Spirit cut","ABV, timing"),("Warehouse","temp, humidity")],
   process="Follow the IBD distilling process — mashing, fermentation in the washbacks, the wash still and spirit still, the cut to collect the heart, cask filling and years in the warehouse — and each step has a number that defines the spirit. IoT brings them online: mash temperature, washback gravity, temperature and CO2 evolution through fermentation, still pot temperature and vapour/condenser readings, the spirit-safe strength and timing that define the foreshots-heart-feints cut, and the warehouse temperature and humidity that govern maturation and the angel's share.",
   sense="Inline sensors that matter: washback temperature and gravity (to track attenuation and ester development), still and condenser temperatures and cooling-water flow, an inline densitometer at the spirit safe for continuous ABV through the cut, and long-life temperature/humidity loggers throughout the maturation warehouse — the data behind evaporation loss and cask performance.",
   faq3q="What should a distillery monitor with IoT first?", faq3a="The spirit run and the warehouse: continuous spirit-safe strength and timing make the cut consistent, and warehouse temperature/humidity over years explain evaporation loss and cask-to-cask variation — both hard to manage from spot readings alone."),
 "wine": dict(noun="winery", accent=WINE, chip=WINEBG, track="winemaking",
   foot=("Winemaking &amp; AI","/tracks/winemaking-ai/"), date="2026-12-21",
   slug="iot-in-the-winery-sensors-process",
   title="IoT in the Winery: Sensors from Vineyard to Bottle",
   desc="A process-grounded guide to IoT in winemaking — sensors in the vineyard, at crush and fermentation, in the barrel room and at bottling, the edge-to-cloud stack, and the AI on the streams.",
   stages=[("Vineyard","soil, weather, NDVI"),("Ferment","Brix, temp"),("Cap","pump-over"),("Barrel room","temp, humidity"),("Bottle","DO, fill")],
   process="Follow the wine the way it is made — vineyard, harvest and crush, fermentation, cap management, pressing, malolactic, barrel ageing, blending and bottling — and each stage has a measurement the winemaker lives by. IoT brings them online: vineyard soil moisture, weather and canopy (NDVI) to time the pick; must and ferment temperature and Brix/density across every tank at harvest; cap-management and pump-over timing; barrel-room temperature and humidity; and dissolved oxygen and fill at bottling.",
   sense="Inline sensors that matter: vineyard soil-moisture and weather stations; in-tank temperature and density/Brix probes so every active ferment is visible at once during the harvest crush; barrel-room temperature and humidity; and dissolved-oxygen and fill monitoring at bottling, where oxygen pick-up sets shelf life.",
   faq3q="What should a winery monitor with IoT first?", faq3a="Fermentation at harvest — temperature and Brix across every active tank — because that is when the most decisions happen fastest and a stuck or hot ferment does lasting damage. Vineyard weather and barrel-room climate are strong second steps."),
}


def iot_article(k):
    B=BEV[k]; noun=B["noun"]; acc=B["accent"]; chip=B["chip"]
    title=B["title"]; desc=B["desc"]
    faqs=[(f"How is IoT used in a {noun}?",
           f"IoT puts a sensor at each process stage and streams the readings to the cloud: in a {noun} that means {', '.join(s[0].lower()+' ('+s[1]+')' for s in B['stages'][:3])} and beyond. The data flows sensor to edge gateway to connectivity to platform, where dashboards show it live and AI flags anomalies."),
          ("What is the difference between IoT and just having sensors?",
           "Sensors measure; IoT connects. The value is the chain — edge gateways, connectivity (often MQTT over wifi, cellular or LoRa), a time-series platform and alerting — that turns isolated gauges into a live, queryable, alertable picture of the whole process."),
          (B["faq3q"], B["faq3a"])]
    stack=steps_svg(f"The IoT stack in a {noun}", acc, chip,
        [("Sensors","at each stage"),("Edge","gateway & buffer"),("Connectivity","MQTT / cellular / LoRa"),("Platform","time-series + dashboards"),("Action","alerts & AI")],
        "Sensor to action: the chain that turns gauges into a live, alertable process picture.")
    pmap=steps_svg(f"Where the sensors sit — {noun} process", acc, chip, B["stages"],
        "IBD-grounded: a measurement at every stage of the process, brought online.", d2=True)
    fab="breweries" if k=="beer" else "distilleries" if k=="whiskey" else "wineries"
    body=[fm(title,desc,B["date"],[B["track"],"iot","sensors","automation",k],faqs),"",
      f"**Short answer: IoT in a {noun} means a sensor at every process stage, streamed sensor to edge to connectivity to platform to action. Grounded in the process itself — {', '.join(s[0].lower() for s in B['stages'])} — it turns spot samples into a live, alertable picture, and feeds the AI that flags a problem before it becomes a loss. The value is the connected chain, not the sensor alone.**","",
      f"Good process control has always been about measurement at the right point. IoT does not change what matters in {noun} work — it makes the measurement continuous, connected and actionable. This is the production-floor companion to {L('a '+noun+' data foundation','/2024/building-brewery-data-foundation-ai/')} and the platform piece on {L('Microsoft Fabric','/2026/microsoft-fabric-for-'+fab+'-20-use-cases/')}.","",stack,"",
      "## Sense the process, stage by stage\n",
      f"{B['process']}","",
      "## The sensors that earn their place\n",
      f"{B['sense']}","",
      "## Edge, connectivity and the platform\n",
      "Raw sensors are not enough. An edge gateway buffers readings (so a network drop does not lose data), does first-line filtering, and publishes over a protocol like MQTT across wifi, cellular or LoRa to a time-series platform — an Eventhouse, historian or cloud store — where dashboards render it live and rules fire alerts. Build for the realities of a wet, electrically noisy production floor: rugged, hygienic, calibrated sensors and a gateway that survives a washdown.","",
      "## The AI on the streams\n",
      f"Once the data flows, machine learning earns its keep: anomaly detection flags a drift the moment it starts, forecasting predicts where a {('fermentation' if k!='whiskey' else 'run')} is heading, and a generative-AI copilot (Claude or ChatGPT) summarises the shift and explains an alert in plain language. The model is only as good as the calibrated sensor under it.","",pmap,"",
      "## Where IoT breaks\n",
      "Three honest limits. First, **a sensor is only as good as its calibration** — an un-calibrated probe streams confident nonsense, and IoT scales that nonsense. Second, **never close a safety- or quality-critical loop on a single sensor** — fermentation control, pressure and the readings of record need redundancy and human oversight, not blind automation. Third, **connectivity and security are real work** — a production floor is hostile to wireless, and every connected device is an attack surface to segment and patch.","",
      "## The bottom line\n",
      f"IoT in a {noun} is the process you already run, made continuous and connected: a calibrated sensor at each stage, an edge-to-cloud chain, and AI that reads the streams. Start where a miss hurts most, calibrate ruthlessly, and keep a human on anything that touches safety or the spirit.","",
      "## Frequently asked questions\n",
      f"**{faqs[0][0]}**\n{faqs[0][1]}\n",f"**{faqs[1][0]}**\n{faqs[1][1]}\n",f"**{faqs[2][0]}**\n{faqs[2][1]}\n",
      f"*Part of the {L(B['foot'][0],B['foot'][1])} track.*",""]
    return "\n".join(body)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    for k in ("beer","whiskey","wine"):
        B=BEV[k]; fname=f"{B['date']}-{B['slug']}.md"
        if a.write: (POSTS/fname).write_text(iot_article(k),encoding="utf-8")
        print(("WROTE " if a.write else "WOULD WRITE ")+fname)


if __name__=="__main__":
    main()
