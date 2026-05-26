#!/usr/bin/env python3
"""
Insert one contextual inline-SVG diagram into every post that doesn't already
have one. Idempotent: any post already containing `<svg` is skipped, so it is
safe to re-run (new posts get picked up, existing diagrams are left alone).

Archetype is chosen from the post's first tag (its track) and slug:
  - tableau-* slug                       -> dashboard wireframe (B)
  - brewing-science/distilling/winemaking-> production flow      (C)
  - commercial/sales/marketing/fpna/...  -> operating loop       (D)
  - everything else (AI/ML/opinion)      -> data->decision pipe  (A)

The post's own title is rendered in the diagram header, so each diagram is
contextual to its article. Diagrams use the site palette and are responsive
(viewBox + width:100%), text-only SVG (no image files).

Usage:
    python tools/add_contextual_diagrams.py            # dry run: report only
    python tools/add_contextual_diagrams.py --write     # actually edit posts
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"

# palette (from assets/css/style.css :root)
BG = "#fdfbf7"; INK = "#1c1a17"; MUTED = "#6b6258"
AMBER = "#b45309"; PEACH = "#f7ece0"; LINE = "#e0d8cc"
WINE = "#7a1f3d"; OAK = "#8a5a2b"; OLIVE = "#5b7a1f"

SCI = {"brewing-science", "distilling-maturation", "winemaking"}
BIZ = {"commercial-planning", "sales-intelligence", "marketing", "fpna",
       "financial-planning-analytics", "esg", "ehs", "forecasting",
       "sales-forecasting"}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))


def header(title: str, kicker: str) -> str:
    t = esc(title if len(title) <= 86 else title[:84].rstrip() + "…")
    return (f'<text x="500" y="26" text-anchor="middle" font-family="sans-serif" '
            f'font-size="12" font-weight="700" letter-spacing="1.5" fill="{AMBER}">{kicker}</text>'
            f'<text x="500" y="52" text-anchor="middle" font-family="sans-serif" '
            f'font-size="17" font-weight="700" fill="{INK}">{t}</text>')


def arrows(edges):
    """edges: list of (x_right_of_box, x_left_of_next, cy)."""
    out = [f'<g fill="{AMBER}" stroke="{AMBER}" stroke-width="2">']
    for (r, nl, cy) in edges:
        out.append(f'<line x1="{r}" y1="{cy}" x2="{nl-7}" y2="{cy}"/>'
                   f'<polygon points="{nl-7},{cy-5} {nl},{cy} {nl-7},{cy+5}" stroke="none"/>')
    out.append("</g>")
    return "".join(out)


def five_box(title, kicker, labels, subs, caption, accent_last=AMBER):
    xs = [4, 203, 402, 601, 800]; w = 172; by, bh = 80, 150; cy = by + bh / 2
    parts = [f'<rect x="0" y="0" width="1000" height="270" fill="{BG}"/>', header(title, kicker)]
    parts.append('<g font-family="sans-serif">')
    for i, x in enumerate(xs):
        stroke = accent_last if i == len(xs) - 1 else AMBER
        parts.append(f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="8" fill="{PEACH}" stroke="{stroke}" stroke-width="1.5"/>')
        cx = x + w / 2
        if subs:
            parts.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">{labels[i]}</text>')
            parts.append(f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="12.5" fill="{MUTED}">{subs[i]}</text>')
        else:
            parts.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="15.5" font-weight="700" fill="{INK}">{labels[i]}</text>')
    parts.append("</g>")
    edges = [(176, 203, cy), (375, 402, cy), (574, 601, cy), (773, 800, cy)]
    parts.append(arrows(edges))
    svg = (f'<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" '
           f'role="img" aria-label="{esc(caption)}">' + "".join(parts) + "</svg>")
    return figure(svg, caption)


def pipeline(title):
    return five_box(
        title, "DATA → DECISION",
        ["Data", "Features", "Model", "Prediction", "Action"],
        ["sensors, logs", "clean &amp; shape", "train / score", "what happens next", "the team acts"],
        "From raw data to a decision the team can act on — the pipeline behind this post.")


def process(title, beverage):
    flows = {
        "beer":    (["Grain", "Mash", "Boil &amp; hops", "Ferment", "Package"], "beer"),
        "wine":    (["Harvest", "Crush / press", "Ferment", "Age", "Bottle"], "wine"),
        "whiskey": (["Mash", "Ferment", "Distil", "Mature", "Bottle"], "whiskey"),
        "mead":    (["Honey must", "Pitch", "Ferment", "Age", "Bottle"], "mead"),
    }
    labels, name = flows[beverage]
    return five_box(
        title, "PRODUCTION FLOW", labels, None,
        f"Where this sits in the {name} production flow, start to finish.")


def loop(title):
    xs = [40, 260, 500, 740]; w = 200; by, bh = 96, 140; cy = by + bh / 2
    labels = ["Measure", "Analyse", "Decide", "Act"]
    subs = ["data in", "find the signal", "choose", "change the floor"]
    parts = [f'<rect x="0" y="0" width="1000" height="280" fill="{BG}"/>', header(title, "THE OPERATING LOOP")]
    parts.append('<g font-family="sans-serif">')
    for i, x in enumerate(xs):
        parts.append(f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="8" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        cx = x + w / 2
        parts.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">{labels[i]}</text>')
        parts.append(f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="12.5" fill="{MUTED}">{subs[i]}</text>')
    parts.append("</g>")
    edges = [(240, 260, cy), (460, 500, cy), (700, 740, cy)]
    parts.append(arrows(edges))
    parts.append(f'<path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" '
                 f'fill="none" stroke="{WINE}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<polygon points="135,90 140,98 145,90" fill="{WINE}"/>')
    parts.append(f'<text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="{WINE}">repeat</text>')
    svg = (f'<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" '
           f'role="img" aria-label="The operating loop this post describes">' + "".join(parts) + "</svg>")
    return figure(svg, "The operating loop this post describes: measure, analyse, decide, act — then repeat.")


def dashboard(title):
    parts = [f'<rect x="0" y="0" width="1000" height="380" fill="{BG}"/>', header(title, "DASHBOARD LAYOUT")]
    parts.append(f'<rect x="40" y="64" width="920" height="30" rx="6" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
    parts.append(f'<text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="{MUTED}">Filters:</text>')
    for lx in [120, 250, 380]:
        parts.append(f'<rect x="{lx}" y="71" width="100" height="16" rx="8" fill="{BG}" stroke="{AMBER}"/>')
    for i, x in enumerate([40, 355, 670]):
        parts.append(f'<rect x="{x}" y="108" width="290" height="74" rx="8" fill="{PEACH}" stroke="{AMBER}" stroke-width="1.5"/>')
        parts.append(f'<text x="{x+18}" y="134" font-family="sans-serif" font-size="12" fill="{MUTED}">KPI {i+1}</text>')
        parts.append(f'<rect x="{x+18}" y="144" width="120" height="20" rx="3" fill="{AMBER}"/>')
    parts.append(f'<rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    parts.append(f'<text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="{MUTED}">Trend</text>')
    bx = [120, 200, 280, 360, 440, 520]; bh = [70, 95, 60, 110, 85, 120]
    for x, h in zip(bx, bh):
        parts.append(f'<rect x="{x}" y="{338-h}" width="46" height="{h}" fill="{AMBER}"/>')
    parts.append(f'<rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    parts.append(f'<text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="{MUTED}">Breakdown</text>')
    for j, ry in enumerate([238, 264, 290, 316]):
        parts.append(f'<rect x="656" y="{ry}" width="200" height="10" rx="3" fill="{PEACH}"/>')
        parts.append(f'<rect x="876" y="{ry}" width="{60-j*10}" height="10" rx="3" fill="{AMBER}"/>')
    svg = (f'<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" '
           f'role="img" aria-label="Typical dashboard layout for {esc(title)}">' + "".join(parts) + "</svg>")
    return figure(svg, "A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.")


def figure(svg, caption):
    return (f'<figure style="margin:1.6rem 0;text-align:center">\n{svg}\n'
            f'<figcaption style="font-size:.85rem;color:{MUTED};margin-top:.4rem">{esc(caption)}</figcaption>\n</figure>')


def beverage_for(first_tag, blob):
    if "mead" in blob:
        return "mead"
    if first_tag == "winemaking" or any(k in blob for k in ["wine", "grape", "vineyard", "varietal", "terroir", "brett"]):
        return "wine"
    if first_tag == "distilling-maturation" or any(k in blob for k in ["whisk", "distill", "distil", "cask", "barrel", "rackhouse", "angels-share", "congener", "new-make", "spirit", "gin"]):
        return "whiskey"
    return "beer"


def classify(slug, first_tag, blob):
    if "tableau" in slug:
        return "B"
    if first_tag in SCI:
        return "C"
    if first_tag in BIZ:
        return "D"
    return "A"


def build(title, slug, first_tag, blob):
    a = classify(slug, first_tag, blob)
    if a == "B":
        return dashboard(title), "dashboard"
    if a == "C":
        return process(title, beverage_for(first_tag, blob)), "process"
    if a == "D":
        return loop(title), "loop"
    return pipeline(title), "pipeline"


FM_RE = re.compile(r"^(---\n.*?\n---\n)(.*)$", re.DOTALL)
TITLE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.MULTILINE)
TAGS_RE = re.compile(r'^tags:\s*\[([^\]]*)\]', re.MULTILINE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    counts = {}; skipped = 0; done = 0
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not m:
            print("NO FRONT MATTER:", path.name); continue
        fm, body = m.group(1), m.group(2)
        if "<svg" in body or "<figure" in body:
            skipped += 1; continue
        tm = TITLE_RE.search(fm); title = tm.group(1).strip() if tm else path.stem
        tags_m = TAGS_RE.search(fm)
        tags = [t.strip().strip('"') for t in tags_m.group(1).split(",")] if tags_m else []
        first_tag = tags[0] if tags else ""
        slug = path.stem[11:]
        blob = (slug + " " + " ".join(tags) + " " + title).lower()

        fig, kind = build(title, slug, first_tag, blob)
        counts[kind] = counts.get(kind, 0) + 1

        lines = body.split("\n")
        insert_at = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
        if insert_at is None:
            print("NO H2, skipping:", path.name); skipped += 1; continue
        before = "\n".join(lines[:insert_at]).rstrip()
        after = "\n".join(lines[insert_at:])
        new_body = before + "\n\n" + fig + "\n\n" + after
        done += 1
        if args.write:
            path.write_text(fm + new_body, encoding="utf-8")

    print(f"\n{'WROTE' if args.write else 'WOULD WRITE'}: {done}   skipped (already had diagram): {skipped}")
    print("by archetype:", counts)


if __name__ == "__main__":
    main()
