#!/usr/bin/env python3
"""
Add a SECOND, content-specific diagram to every post, chosen from a wide
library so articles vary by topic instead of all sharing one archetype.
The first diagram (from add_contextual_diagrams.py) is left in place; this one
is inserted deeper in the post (before "The bottom line" / FAQ).

Idempotent: skips any post already containing `data-d2` (its marker), so it is
safe to re-run. Routing is by fine-grained keywords in slug + tags + title, so
a forecasting post gets a forecast chart, a sales post a funnel, a safety post
a pyramid, a vision post a detection frame, and so on.

Usage:
    python tools/add_more_diagrams.py            # dry run: report only
    python tools/add_more_diagrams.py --write      # actually edit posts
"""
from __future__ import annotations
import argparse, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
BG="#fdfbf7"; INK="#1c1a17"; MUTED="#6b6258"; AMBER="#b45309"; PEACH="#f7ece0"
LINE="#e0d8cc"; WINE="#7a1f3d"; OLIVE="#5b7a1f"; OAK="#8a5a2b"; SKY="#3b6ea5"


def esc(s):
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
             .replace('"',"&quot;").replace("'","&#39;"))


def head(title, kicker, w):
    t = esc(title if len(title) <= 78 else title[:76].rstrip()+"…")
    cx = w/2
    return (f'<text x="{cx}" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" '
            f'font-weight="700" letter-spacing="1.5" fill="{AMBER}">{kicker}</text>'
            f'<text x="{cx}" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" '
            f'font-weight="700" fill="{INK}">{t}</text>')


def fig(svg, caption, w, h):
    s = (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto" '
         f'role="img" aria-label="{esc(caption)}">{svg}</svg>')
    return (f'<figure data-d2="1" style="margin:1.6rem 0;text-align:center">\n{s}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(caption)}</figcaption>\n</figure>')


def bg(w, h):
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="{BG}"/>'


def forecast_ts(title):
    w,h=720,300; p=[bg(w,h),head(title,"FORECAST",w)]
    p.append(f'<g stroke="{INK}" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g>')
    p.append(f'<polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="{AMBER}" opacity="0.15"/>')
    p.append(f'<polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="{AMBER}" stroke-width="3"/>')
    p.append(f'<polyline points="430,162 540,140 660,120" fill="none" stroke="{WINE}" stroke-width="3" stroke-dasharray="6 4"/>')
    p.append(f'<line x1="430" y1="70" x2="430" y2="250" stroke="{MUTED}" stroke-width="1" stroke-dasharray="3 3"/>')
    p.append(f'<text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="{MUTED}">today</text>')
    p.append(f'<text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="{MUTED}">history</text>')
    p.append(f'<text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="{WINE}">forecast</text>')
    return fig("".join(p),"History (solid) and the model's forward forecast (dashed); the shaded band is its uncertainty.",w,h)


def anomaly(title):
    w,h=720,300; p=[bg(w,h),head(title,"ANOMALY DETECTION",w)]
    p.append(f'<rect x="60" y="120" width="620" height="70" fill="{OLIVE}" opacity="0.12"/>')
    p.append(f'<line x1="60" y1="120" x2="680" y2="120" stroke="{OLIVE}" stroke-width="1" stroke-dasharray="4 3"/>')
    p.append(f'<line x1="60" y1="190" x2="680" y2="190" stroke="{OLIVE}" stroke-width="1" stroke-dasharray="4 3"/>')
    dots=[(110,150),(160,140),(210,165),(265,148),(320,158),(380,143),(440,168),(500,150),(560,160),(620,146)]
    for x,y in dots: p.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{MUTED}"/>')
    p.append(f'<circle cx="345" cy="92" r="7" fill="{WINE}"/>')
    p.append(f'<text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="{WINE}">anomaly</text>')
    p.append(f'<text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="{OLIVE}">normal band</text>')
    return fig("".join(p),"Most readings sit inside the normal band; the model flags the one that doesn't.",w,h)


def buckets(title):
    w,h=720,300; p=[bg(w,h),head(title,"CLASSIFICATION",w)]
    labels=["Class A","Class B","Class C"]; cols=[AMBER,OLIVE,WINE]
    for i,(lx,lab,c) in enumerate(zip([120,330,540],labels,cols)):
        p.append(f'<rect x="{lx}" y="120" width="150" height="120" rx="8" fill="{PEACH}" stroke="{c}" stroke-width="1.5"/>')
        p.append(f'<text x="{lx+75}" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="{c}">{lab}</text>')
        for j in range(3+i):
            cxp=lx+25+(j%4)*32; cyp=145+(j//4)*30
            p.append(f'<circle cx="{cxp}" cy="{cyp}" r="6" fill="{c}"/>')
    p.append(f'<text x="360" y="92" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{MUTED}">new sample → sorted into the best-fit class</text>')
    return fig("".join(p),"The model sorts each sample into a class from its measured features.",w,h)


def vision(title):
    w,h=720,300; p=[bg(w,h),head(title,"COMPUTER VISION",w)]
    p.append(f'<rect x="80" y="80" width="360" height="180" rx="6" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<rect x="120" y="120" width="110" height="90" fill="none" stroke="{OLIVE}" stroke-width="2.5"/>')
    p.append(f'<rect x="270" y="150" width="120" height="70" fill="none" stroke="{AMBER}" stroke-width="2.5"/>')
    p.append(f'<text x="120" y="114" font-family="sans-serif" font-size="11" font-weight="700" fill="{OLIVE}">ok</text>')
    p.append(f'<text x="270" y="144" font-family="sans-serif" font-size="11" font-weight="700" fill="{AMBER}">flag</text>')
    p.append(f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2.5"><line x1="450" y1="170" x2="500" y2="170"/><polygon points="500,163 512,170 500,177" stroke="none"/></g>')
    p.append(f'<rect x="525" y="140" width="150" height="60" rx="8" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
    p.append(f'<text x="600" y="176" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="{INK}">label + score</text>')
    return fig("".join(p),"A vision model locates and labels features in each image, then scores them.",w,h)


def text_signal(title):
    w,h=720,300; p=[bg(w,h),head(title,"TEXT → SIGNAL",w)]
    p.append(f'<rect x="80" y="90" width="200" height="150" rx="6" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    for k,yy in enumerate([118,140,162,184,206]):
        p.append(f'<rect x="100" y="{yy}" width="{160-(k%2)*40}" height="9" rx="3" fill="{PEACH}"/>')
    p.append(f'<text x="180" y="262" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="{MUTED}">reviews / notes</text>')
    p.append(f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2.5"><line x1="300" y1="165" x2="350" y2="165"/><polygon points="350,158 362,165 350,172" stroke="none"/></g>')
    p.append(f'<rect x="385" y="150" width="200" height="26" rx="4" fill="{OLIVE}"/>')
    p.append(f'<rect x="525" y="150" width="60" height="26" rx="4" fill="{WINE}"/>')
    p.append(f'<text x="485" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{MUTED}">sentiment / topics scored</text>')
    return fig("".join(p),"Free text in, a structured signal out — sentiment and themes scored from the words.",w,h)


def recommend(title):
    w,h=720,300; p=[bg(w,h),head(title,"RECOMMENDER",w)]
    p.append(f'<circle cx="140" cy="165" r="34" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
    p.append(f'<text x="140" y="170" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="{INK}">profile</text>')
    p.append(f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2.5"><line x1="184" y1="165" x2="240" y2="165"/><polygon points="240,158 252,165 240,172" stroke="none"/></g>')
    for k,(yy,wd,lab) in enumerate([(120,300,"best match"),(160,230,"#2"),(200,170,"#3")]):
        c = AMBER if k==0 else PEACH; tc = "#ffffff" if k==0 else INK
        p.append(f'<rect x="280" y="{yy}" width="{wd}" height="28" rx="4" fill="{c}" stroke="{AMBER}"/>')
        p.append(f'<text x="294" y="{yy+19}" font-family="sans-serif" font-size="12" font-weight="700" fill="{tc}">{lab}</text>')
    return fig("".join(p),"From one profile to a ranked shortlist — the strongest match on top.",w,h)


def gauge(title):
    w,h=720,300; p=[bg(w,h),head(title,"SCORE",w)]
    cx,cy=360,230
    p.append(f'<path d="M180,230 A180,180 0 0,1 280,72" fill="none" stroke="{WINE}" stroke-width="22"/>')
    p.append(f'<path d="M280,72 A180,180 0 0,1 440,72" fill="none" stroke="{AMBER}" stroke-width="22"/>')
    p.append(f'<path d="M440,72 A180,180 0 0,1 540,230" fill="none" stroke="{OLIVE}" stroke-width="22"/>')
    p.append(f'<line x1="{cx}" y1="{cy}" x2="470" y2="120" stroke="{INK}" stroke-width="4"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{INK}"/>')
    p.append(f'<text x="{cx}" y="180" text-anchor="middle" font-family="sans-serif" font-size="30" font-weight="700" fill="{INK}">72</text>')
    p.append(f'<text x="180" y="252" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{MUTED}">low</text>')
    p.append(f'<text x="540" y="252" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{MUTED}">high</text>')
    return fig("".join(p),"A single score ranks each account or sample at a glance.",w,h)


def matrix(title):
    w,h=720,320; p=[bg(w,h),head(title,"2×2 MATRIX",w)]
    x0,y0,x1,y1=180,70,560,280; mx,my=(x0+x1)/2,(y0+y1)/2
    p.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{y1}" stroke="{LINE}"/><line x1="{x0}" y1="{my}" x2="{x1}" y2="{my}" stroke="{LINE}"/>')
    p.append(f'<rect x="{mx}" y="{y0}" width="{x1-mx}" height="{my-y0}" fill="{AMBER}" opacity="0.12"/>')
    for lab,tx,ty in [("low / low",x0+12,y1-14),("high focus",mx+12,y0+24),("watch",x0+12,y0+24),("hold",mx+12,y1-14)]:
        p.append(f'<text x="{tx}" y="{ty}" font-family="sans-serif" font-size="12" fill="{MUTED}">{lab}</text>')
    for px,py in [(mx+70,y0+60),(mx+110,y0+90),(mx+50,y0+95),(x0+60,my+50),(mx+40,my+60)]:
        p.append(f'<circle cx="{px}" cy="{py}" r="6" fill="{AMBER}"/>')
    return fig("".join(p),"Two dimensions, four quadrants — where each item lands tells you what to do.",w,h)


def funnel(title):
    w,h=720,310; p=[bg(w,h),head(title,"FUNNEL",w)]
    stages=[("Reach","100%"),("Interest","52%"),("Trial","24%"),("Win","9%")]
    cx=360; topw=440; yy=78; sh=48; gap=8
    for i,(lab,val) in enumerate(stages):
        tw=topw-i*100; bw=topw-(i+1)*100
        x_tl=cx-tw/2; x_tr=cx+tw/2; x_bl=cx-bw/2; x_br=cx+bw/2; y2=yy+sh
        p.append(f'<polygon points="{x_tl},{yy} {x_tr},{yy} {x_br},{y2} {x_bl},{y2}" fill="{AMBER}" opacity="{1-i*0.18}"/>')
        p.append(f'<text x="{cx}" y="{yy+31}" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">{lab} · {val}</text>')
        yy+=sh+gap
    return fig("".join(p),"Each stage loses some — the funnel shows where the drop-off is.",w,h)


def waterfall(title):
    w,h=720,300; p=[bg(w,h),head(title,"BRIDGE",w)]
    p.append(f'<line x1="60" y1="250" x2="680" y2="250" stroke="{INK}" stroke-width="1.5"/>')
    draw=[("Start",90,100,150,AMBER),("−40",230,140,40,WINE),("−30",350,170,30,WINE),("+40",470,130,40,OLIVE),("End",590,130,120,AMBER)]
    for lab,x,top,bh,c in draw:
        p.append(f'<rect x="{x}" y="{top}" width="80" height="{bh}" fill="{c}"/>')
        p.append(f'<text x="{x+40}" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="{MUTED}">{lab}</text>')
    for x1c,y1c,x2c in [(170,100,230),(310,140,350),(430,170,470),(550,130,590)]:
        p.append(f'<line x1="{x1c}" y1="{y1c}" x2="{x2c}" y2="{y1c}" stroke="{MUTED}" stroke-width="1" stroke-dasharray="3 3"/>')
    return fig("".join(p),"Start to finish, broken into the pieces that move the number.",w,h)


def footprint(title):
    w,h=720,300; p=[bg(w,h),head(title,"FOOTPRINT BY SCOPE",w)]
    p.append(f'<rect x="300" y="80" width="120" height="40" fill="{OLIVE}"/>')
    p.append(f'<rect x="300" y="120" width="120" height="40" fill="{AMBER}"/>')
    p.append(f'<rect x="300" y="160" width="120" height="90" fill="{WINE}"/>')
    for lab,c,yy in [("Scope 1 — direct",OLIVE,96),("Scope 2 — energy",AMBER,136),("Scope 3 — value chain (largest)",WINE,196)]:
        p.append(f'<rect x="460" y="{yy-12}" width="14" height="14" fill="{c}"/>')
        p.append(f'<text x="482" y="{yy}" font-family="sans-serif" font-size="12.5" fill="{INK}">{lab}</text>')
    return fig("".join(p),"Emissions split by scope — most of the footprint usually hides in Scope 3.",w,h)


def cycle(title):
    w,h=720,320; p=[bg(w,h),head(title,"THE CYCLE",w)]
    cx,cy,r=360,190,95; nodes=["Plan","Do","Check","Act"]
    pos=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="5 5"/>')
    for (x,y),lab in zip(pos,nodes):
        p.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        p.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="{INK}">{lab}</text>')
    for ax,ay in [(cx+68,cy-50),(cx+50,cy+68),(cx-68,cy+50),(cx-50,cy-68)]:
        p.append(f'<circle cx="{ax}" cy="{ay}" r="4" fill="{AMBER}"/>')
    return fig("".join(p),"A continuous cycle — each step feeds the next, then round again.",w,h)


def pyramid(title):
    w,h=720,300; p=[bg(w,h),head(title,"SAFETY PYRAMID",w)]
    cx=360; spec=[("Serious",110,WINE,"1"),("Minor injuries",200,AMBER,"~30"),("Near-misses",320,OLIVE,"~300")]
    ytop=80; th=58
    for i,(lab,bw,c,n) in enumerate(spec):
        tw=spec[i-1][1] if i>0 else 50
        y1=ytop+i*(th+6); y2=y1+th
        x_tl=cx-tw/2; x_tr=cx+tw/2; x_bl=cx-bw/2; x_br=cx+bw/2
        p.append(f'<polygon points="{x_tl},{y1} {x_tr},{y1} {x_br},{y2} {x_bl},{y2}" fill="{c}"/>')
        p.append(f'<text x="{cx}" y="{y1+38}" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">{lab} · {n}</text>')
    return fig("".join(p),"The safety pyramid: many near-misses underlie each serious event — act on the base.",w,h)


def attribution(title):
    w,h=720,300; p=[bg(w,h),head(title,"CONTRIBUTION",w)]
    yy=90
    for lab,bw in [("Channel A",300),("Channel B",230),("Channel C",150),("Channel D",90)]:
        p.append(f'<text x="60" y="{yy+19}" font-family="sans-serif" font-size="12.5" fill="{INK}">{lab}</text>')
        p.append(f'<rect x="180" y="{yy}" width="{bw}" height="26" rx="4" fill="{AMBER}"/>')
        yy+=44
    return fig("".join(p),"How much each channel contributes — the longer the bar, the bigger the effect.",w,h)


def map_pins(title):
    w,h=720,320; p=[bg(w,h),head(title,"ON THE GROUND",w)]
    p.append(f'<rect x="120" y="80" width="480" height="200" rx="10" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    for gx in range(180,600,80): p.append(f'<line x1="{gx}" y1="80" x2="{gx}" y2="280" stroke="{LINE}"/>')
    for gy in range(120,280,60): p.append(f'<line x1="120" y1="{gy}" x2="600" y2="{gy}" stroke="{LINE}"/>')
    p.append('<polyline points="220,150 360,200 470,130 540,240" fill="none" stroke="'+AMBER+'" stroke-width="2" stroke-dasharray="5 4"/>')
    for x,y in [(220,150),(360,200),(470,130),(540,240)]:
        p.append(f'<circle cx="{x}" cy="{y-6}" r="9" fill="{WINE}"/><polygon points="{x-6},{y-2} {x+6},{y-2} {x},{y+8}" fill="{WINE}"/>')
    return fig("".join(p),"Where it happens on the ground — sites, routes and territory.",w,h)


def control_loop(title):
    w,h=720,300; p=[bg(w,h),head(title,"CONTROL LOOP",w)]
    for lab,x in [("Sensor",70),("Controller",250),("Actuator",430),("Process",610)]:
        p.append(f'<rect x="{x}" y="120" width="120" height="60" rx="8" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+60}" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="{INK}">{lab}</text>')
    p.append(f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2.5">')
    for r,nl in [(190,250),(370,430),(550,610)]:
        p.append(f'<line x1="{r}" y1="150" x2="{nl-8}" y2="150"/><polygon points="{nl-8},143 {nl},150 {nl-8},157" stroke="none"/>')
    p.append('</g>')
    p.append(f'<path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="{WINE}" stroke-width="2" stroke-dasharray="5 4"/>')
    p.append(f'<polygon points="124,186 130,178 136,186" fill="{WINE}"/>')
    p.append(f'<text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="{WINE}">feedback</text>')
    return fig("".join(p),"A closed control loop: measure, compute, actuate — then feed the result back.",w,h)


def driver(title, central):
    w,h=720,300; p=[bg(w,h),head(title,"WHAT DRIVES IT",w)]
    ins=["input 1","input 2","input 3"]
    for i,yy in enumerate([90,150,210]):
        p.append(f'<rect x="50" y="{yy}" width="130" height="44" rx="8" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        p.append(f'<text x="115" y="{yy+28}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{MUTED}">{ins[i]}</text>')
        p.append(f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2"><line x1="180" y1="{yy+22}" x2="285" y2="150"/></g>')
    p.append(f'<rect x="290" y="116" width="140" height="68" rx="10" fill="{AMBER}"/>')
    p.append(f'<text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">{esc(central)}</text>')
    outs=["quality","cost / risk"]
    for i,yy in enumerate([120,180]):
        p.append(f'<g fill="{OLIVE}" stroke="{OLIVE}" stroke-width="2"><line x1="430" y1="150" x2="535" y2="{yy+22}"/><polygon points="535,{yy+15} 547,{yy+22} 535,{yy+29}" stroke="none"/></g>')
        p.append(f'<rect x="550" y="{yy}" width="130" height="44" rx="8" fill="{PEACH}" stroke="{OLIVE}" stroke-width="1.5"/>')
        p.append(f'<text x="615" y="{yy+28}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{INK}">{outs[i]}</text>')
    return fig("".join(p),f"What drives {central.lower()}, and what it changes downstream.",w,h)


def kpi_cards(title):
    w,h=720,260; p=[bg(w,h),head(title,"THE NUMBERS",w)]
    for i,x in enumerate([70,280,490]):
        p.append(f'<rect x="{x}" y="90" width="160" height="120" rx="10" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+20}" y="120" font-family="sans-serif" font-size="12" fill="{MUTED}">metric {i+1}</text>')
        p.append(f'<rect x="{x+20}" y="135" width="{120-i*20}" height="22" rx="3" fill="{AMBER}"/>')
        p.append(f'<text x="{x+20}" y="190" font-family="sans-serif" font-size="11.5" fill="{MUTED}">vs target</text>')
    return fig("".join(p),"The handful of numbers this comes down to.",w,h)


CENTRAL = [("mash","Mashing"),("lauter","Lautering"),("wort","Wort"),("boil","The boil"),
    ("hop","Hopping"),("yeast","Yeast"),("ferment","Fermentation"),("water","Water"),
    ("malt","Malt"),("carbonation","Carbonation"),("filtration","Filtration"),
    ("maturation","Maturation"),("cask","Cask maturation"),("barrel","Barrel ageing"),
    ("distill","Distillation"),("blend","Blending"),("grape","The harvest"),
    ("harvest","The harvest"),("oxygen","Oxygen control"),("haze","Colloidal stability")]


def has(blob, *kw):
    return any(k in blob for k in kw)


def choose(slug, first_tag, blob):
    if has(blob,"computer-vision","vision","fill-level","label-inspection","grain-malt-qc","grape-sorting","sorting","inspection"):
        return vision
    if has(blob,"nlp","review","sentiment","social-listening","chatbot","sommelier","gen-ai-search","sops","naming","trademark"):
        return text_signal
    if has(blob,"anomaly","contamination","fault","detecting","detect","leak","spoil","stuck","off-flavour","counterfeit","authentication","hygiene","staling"):
        return anomaly
    if has(blob,"recommend","pairing","personalization","personalisation"):
        return recommend
    if has(blob,"scoring","churn","propensity"):
        return gauge
    if has(blob,"segment","white-space","portfolio","price-pack"):
        return matrix
    if has(blob,"classif","style","variety","grade","calibration","panel"):
        return buckets
    if has(blob,"safety","hazard","incident","confined-space") or first_tag=="ehs":
        return pyramid
    if has(blob,"carbon","scope","csrd","footprint"):
        return footprint
    if has(blob,"esg","sustainability","water-stewardship","circular","greenwashing"):
        return cycle
    if has(blob,"attribution","mix-model","marketing-mix","brand-equity","promotion","marketing"):
        return attribution
    if has(blob,"geospatial","route","distribution","maps","logistics"):
        return map_pins
    if has(blob,"funnel","sales","conversion","perfect-store","distributor","account","route-to-market","sell-through","depletion","scorecard","productivity"):
        return funnel
    if has(blob,"margin","cogs","cost","working-capital","capex","profitability","revenue","rgm","volume-to-value","cost-to-serve","bridge","price","pricing"):
        return waterfall
    if has(blob,"forecast","forecasting","demand","seasonality","weather","prices","procurement","hierarchical","driver-based"):
        return forecast_ts
    if has(blob,"control","monitoring","optimis","optimiz","scheduling","cip","energy","maintenance","centrifugation"):
        return control_loop
    if first_tag in ("brewing-science","distilling-maturation","winemaking"):
        central="The process"
        for k,name in CENTRAL:
            if k in blob: central=name; break
        return lambda t: driver(t, central)
    return kpi_cards


FM = re.compile(r"^(---\n.*?\n---\n)(.*)$", re.DOTALL)
T = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.MULTILINE)
TG = re.compile(r'^tags:\s*\[([^\]]*)\]', re.MULTILINE)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    done=skip=0; counts={}
    for path in sorted(POSTS.glob("*.md")):
        text=path.read_text(encoding="utf-8"); m=FM.match(text)
        if not m: continue
        fms,body=m.group(1),m.group(2)
        if "data-d2" in body: skip+=1; continue
        if "excel" in path.stem[11:]: skip+=1; continue  # Excel posts already richly illustrated
        tm=T.search(fms); title=tm.group(1).strip() if tm else path.stem
        tgm=TG.search(fms); tags=[t.strip().strip('"') for t in tgm.group(1).split(",")] if tgm else []
        first=tags[0] if tags else ""; slug=path.stem[11:]
        blob=(slug+" "+" ".join(tags)+" "+title).lower()
        gen=choose(slug,first,blob)
        figblock=gen(title)
        name=getattr(gen,"__name__","driver")
        counts[name]=counts.get(name,0)+1
        lines=body.split("\n")
        idx=None
        for want in ("## the bottom line","## frequently asked questions"):
            for i,l in enumerate(lines):
                if l.strip().lower()==want: idx=i; break
            if idx is not None: break
        if idx is None:
            h2=[i for i,l in enumerate(lines) if l.startswith("## ")]
            idx=h2[-1] if h2 else None
        if idx is None: skip+=1; continue
        before="\n".join(lines[:idx]).rstrip(); after="\n".join(lines[idx:])
        new=before+"\n\n"+figblock+"\n\n"+after
        done+=1
        if a.write: path.write_text(fms+new,encoding="utf-8")
    print(f"{'WROTE' if a.write else 'WOULD WRITE'}: {done}  skipped: {skip}")
    print("by type:",counts)


if __name__=="__main__":
    main()
