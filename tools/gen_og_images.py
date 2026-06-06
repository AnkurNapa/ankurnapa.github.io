#!/usr/bin/env python3
"""
Generate a unique Open Graph share image (1200x630) for every post.

Why: jekyll-seo-tag emits <meta property="og:image">, which is what WhatsApp,
LinkedIn, X, etc. show as the link-preview card. Without a per-post `image:`
in front matter, every post falls back to the single site default
(/assets/og-default.png) -- so every shared link looks identical.

What this does, for each file in _posts/:
  1. renders a branded card (cream background, amber kicker, the post TITLE as
     the headline, the post TAGS as the footer line) matching og-default.png,
  2. writes it to  assets/og/<slug>.png,
  3. inserts  `image: /assets/og/<slug>.png`  into the post front matter
     (right after the title: line) if it isn't already there.

Re-running is safe: artwork is always regenerated; the front-matter line is
only inserted once. New posts are picked up automatically on the next run.

Usage:
    python tools/gen_og_images.py            # generate + patch front matter
    python tools/gen_og_images.py --no-patch # only (re)generate images
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

# --- paths -----------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
OG_DIR = ROOT / "assets" / "og"
OG_URL_PREFIX = "/assets/og"

# --- brand (from assets/css/style.css :root) -------------------------------
BG = (253, 251, 247)     # --bg     #fdfbf7  cream
INK = (28, 26, 23)       # --ink    #1c1a17  near-black
MUTED = (107, 98, 88)    # --muted  #6b6258
ACCENT = (180, 83, 9)    # --accent #b45309  amber (beer)
MAROON = (122, 31, 61)   #          #7a1f3d  wine
CIRCLE = (247, 236, 224) # pale peach decorative blob (top-right)

W, H = 1200, 630
MARGIN = 80

# Cross-platform font lookup: Segoe UI on Windows, Arial on macOS.
_FONT_CANDIDATES = [
    ("C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"),  # Windows
    ("/System/Library/Fonts/Supplemental/Arial Bold.ttf",
     "/System/Library/Fonts/Supplemental/Arial.ttf"),                   # macOS
]
for _bold, _reg in _FONT_CANDIDATES:
    if Path(_bold).exists() and Path(_reg).exists():
        F_BOLD, F_REG = _bold, _reg
        break
else:
    sys.exit("No usable font found - add your platform's fonts to _FONT_CANDIDATES.")

KICKER = "BEER . WINE . WHISKEY . AI"


# --- text helpers ----------------------------------------------------------
def wrap(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    """Greedy word-wrap to a pixel width."""
    lines: list[str] = []
    cur = ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if font.getlength(trial) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_tracked(draw, xy, text, font, fill, tracking):
    """Draw text with manual letter-spacing; return the end x position."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking
    return x


def tracked_width(text, font, tracking):
    return sum(font.getlength(ch) + tracking for ch in text) - tracking


# --- card rendering --------------------------------------------------------
def render_card(title: str, tags: list[str], out_path: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # decorative pale blob, top-right (drawn first so headline sits on top)
    draw.ellipse([W - 360, -170, W + 220, 410], fill=CIRCLE)

    # kicker
    kfont = ImageFont.truetype(F_BOLD, 30)
    draw_tracked(draw, (MARGIN, 56), KICKER, kfont, ACCENT, 4)

    # headline = post title, largest size that fits <=4 lines
    max_w = W - 2 * MARGIN
    for size in range(82, 44, -2):
        hfont = ImageFont.truetype(F_BOLD, size)
        lines = wrap(title, hfont, max_w)
        line_h = int(size * 1.13)
        if len(lines) <= 4:
            break
    total_h = line_h * len(lines)
    # vertically center the headline block in the band between kicker & footer
    y = 150 + max(0, (350 - total_h) // 2)
    for line in lines:
        draw.text((MARGIN, y), line, font=hfont, fill=INK)
        y += line_h

    # footer = tags, uppercased, maroon — shrink to fit one line
    if tags:
        label = " . ".join(t.replace("-", " ").upper() for t in tags)
        for size in range(28, 15, -2):
            ffont = ImageFont.truetype(F_BOLD, size)
            if tracked_width(label, ffont, 2) <= max_w:
                break
        else:
            # still too wide at the smallest size: keep the first few tags
            while tags and tracked_width(label, ffont, 2) > max_w:
                tags = tags[:-1]
                label = " . ".join(t.replace("-", " ").upper() for t in tags) + " ..."
        draw_tracked(draw, (MARGIN, 548), label, ffont, MAROON, 2)

    img.save(out_path, "PNG", optimize=True)


# --- front matter ----------------------------------------------------------
FM_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)


def parse_front_matter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


def insert_image_line(text: str, image_url: str) -> str | None:
    """Insert `image: <url>` right after the title: line. Returns new text,
    or None if no change is needed (already present) or possible."""
    m = FM_RE.match(text)
    if not m:
        return None
    fm = m.group(1)
    if re.search(r"^image:", fm, re.MULTILINE):
        return None  # already has an image
    lines = fm.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if ln.startswith("title:"):
            lines.insert(i + 1, f"image: {image_url}\n")
            break
    else:
        return None
    new_fm = "".join(lines)
    return text[: m.start(1)] + new_fm + text[m.end(1):]


# --- main ------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-patch", action="store_true",
                    help="only (re)generate images; do not edit front matter")
    args = ap.parse_args()

    OG_DIR.mkdir(parents=True, exist_ok=True)
    posts = sorted(POSTS_DIR.glob("*.md"))
    if not posts:
        print(f"No posts found in {POSTS_DIR}", file=sys.stderr)
        return 1

    made, patched, skipped = 0, 0, 0
    for post in posts:
        text = post.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        if not fm or "title" not in fm:
            print(f"  skip (no title): {post.name}")
            skipped += 1
            continue

        title = str(fm["title"]).strip()
        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]

        # slug = filename minus the YYYY-MM-DD- date prefix and .md
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)
        out = OG_DIR / f"{slug}.png"
        render_card(title, list(tags), out)
        made += 1

        if not args.no_patch:
            new_text = insert_image_line(text, f"{OG_URL_PREFIX}/{slug}.png")
            if new_text:
                post.write_text(new_text, encoding="utf-8")
                patched += 1

    print(f"\nimages generated: {made}")
    print(f"front matter patched: {patched}")
    if skipped:
        print(f"skipped: {skipped}")
    print(f"output dir: {OG_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
