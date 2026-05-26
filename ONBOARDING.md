# 🍺 Beer, Wine, Whiskey & AI — Project Handover

Everything you need to run, edit, and grow this blog **from any laptop**. Carry this one file (or just clone the repo — this file is inside it).

- **Live site:** https://ankurnapa.github.io
- **GitHub repo:** https://github.com/AnkurNapa/ankurnapa.github.io
- **Author:** Ankur Napa
- **What it is:** A Jekyll static blog (hosted free on GitHub Pages) about AI & data analytics in the drinks industry — beer, non-alcoholic beer, wine, whiskey, mead. ~75 posts, 7 analytics "tracks", 2 narrative series, full SEO + GEO.

---

## 1. Get it on a new laptop

**Prerequisites:** install [Git](https://git-scm.com/) and the [GitHub CLI](https://cli.github.com/) (`gh`). Ruby is optional (only for local preview).

```bash
# 1. Log in to GitHub on the new machine
gh auth login

# 2. Clone the repo
git clone https://github.com/AnkurNapa/ankurnapa.github.io.git
cd ankurnapa.github.io
```

That's it — you now have the entire site, this guide included.

---

## 2. The only workflow you need (write → publish)

The site auto-deploys: **push to `main` → GitHub Pages rebuilds in ~1 minute.**

```bash
# write or edit a post (see template below), then:
git add -A
git commit -m "post: <short description>"
git push origin main
# wait ~1 min, changes are live at https://ankurnapa.github.io
```

Check the build status anytime:
```bash
gh api repos/AnkurNapa/ankurnapa.github.io/pages/builds/latest --jq '.status'
# "built" = live, "building" = wait, "errored" = something broke
```

---

## 3. Write a new post

Create a file in `_posts/` named **`YYYY-MM-DD-url-slug.md`**. It will live at `https://ankurnapa.github.io/YEAR/url-slug/`.

```markdown
---
layout: post
title: "Your Headline as a Question Works Best for AI Search"
description: "One-sentence summary (~150 chars) with your main keyword — used for meta + AI snippets."
date: 2026-06-01
updated: 2026-06-01
tags: [topic-tag, another-tag]
faq:
  - q: "A real question readers ask?"
    a: "A direct, quotable 1-2 sentence answer."
  - q: "Second question?"
    a: "Answer."
---

**Short answer: lead with a bold, direct answer in the first paragraph.** AI engines
(ChatGPT, Perplexity, Google AI) quote concise factual openings — put the payoff up top.

## A section with a clear heading
Body text. Link internally like this: [related post]({{ "{{" }} '/2026/some-slug/' | relative_url }}).

## Frequently asked questions
**A real question readers ask?**
The same answer as the faq above (must match — it powers the FAQ rich result).

**Second question?**
Answer.
```

**Rules that keep things working:**
- Always wrap `title:` and `description:` in **double quotes** (titles have colons → YAML breaks unquoted).
- The visible `## Frequently asked questions` text must **match** the `faq:` block (Google requires the schema content to be visible).
- Open with a **bold "Short answer:"** paragraph (this is the GEO superpower).
- Keep the honest, anti-hype voice — always note where things break.

**House article rule (the standard every post follows):**
- **McKinsey style** — decision-oriented and crisp: lead with the bold `Short answer:` payoff, then 3–4 tightly-argued `##` sections, then a `## The bottom line` close. Vary section headings between posts; don't reuse a template of identical headings.
- **Three lenses in every post** — weave in all three, naturally, not as headings: (1) **AI / machine learning** (the predictive or optimisation model), (2) **data science** (what data/sensors/features are needed; "measure first, model second"), and (3) **generative AI** (one concrete angle — an LLM copilot that explains an anomaly, synthetic data for rare events, generative design/optimisation, auto-drafted reports/SOPs, or natural-language querying of process data).
- **Always an honest "where it breaks" section** — state the real limits; predict the routine well, the rare failure poorly.
- **Length** — a "small read", roughly 650–900 words of body plus the FAQ.
- **At least one diagram** — every post should carry a contextual illustration where it aids understanding: a flow/process diagram, a block diagram, an operating loop, a dashboard wireframe, or a bespoke schematic/chart (e.g. a strike-water heat balance, a utilisation curve, a Pearson's square, an efficiency waterfall). Rules that keep it working:
  - **Inline SVG only** — text-only `<svg>`, no image files (renders natively on GitHub Pages through kramdown). Wrap it in `<figure style="margin:1.6rem 0;text-align:center"> … <figcaption>caption</figcaption></figure>` and place it after the intro (before the first `##`) or beside the section it explains.
  - **Responsive** — `width="100%"` + `viewBox` + `style="max-width:NNNpx;height:auto"`, plus `role="img"` and an `aria-label`.
  - **Site palette** — amber `#b45309`, ink `#1c1a17`, cream `#fdfbf7`, peach `#f7ece0`, muted `#6b6258`, wine `#7a1f3d` (escape `&` as `&amp;` inside SVG text).
  - **Back-fill tool** — `python tools/add_contextual_diagrams.py --write` inserts a contextual diagram (production-flow / pipeline / operating-loop / dashboard, chosen by track tag + slug, titled per post) into any post that has none. It's idempotent: it skips any post already containing `<svg>`, so hand-authored diagrams always win — run it after a batch of new posts to catch any you left bare.
- **3 FAQs** in the `faq:` block, mirrored word-for-word in the visible FAQ section.
- **1–2 internal links** using `{{ "{{" }} '/YEAR/slug/' | relative_url }}`, and a track footer line: `*Part of the [Track Name]({{ "{{" }} '/tracks/<tag>/' | relative_url }}) track.*`
- **Grounding** — use real beverage-science facts and realistic numbers; never invent company names or fake adoption statistics. International/British spelling (optimise, flavour, colour).
- First tag = the track tag (see below) so the post slots into its track hub.
- **Title banner is automatic** — every post renders a framed-minimal title banner (the title inside a thin line/square frame with a faint light circle behind it, and the track name beneath), tinted by a per-track accent: brewing = amber, distilling = oak, winemaking = plum, all other tracks = neutral ink. It lives in `_layouts/post.html` + the `.post-banner`/`.banner-*` rules in `assets/css/style.css`, so it applies to **every post — new and historical — with no per-post work**. The accent keys off the post's first tag; to add a track colour, extend the `banner-*` map in both files. Banners are CSS/SVG (text only, no image files); social/OG share images are a separate optional add-on.

---

## 4. How content is organised

| Type | Where | Tag / URL |
|---|---|---|
| **Posts** | `_posts/*.md` | `/YEAR/slug/` |
| **Tracks** (exec themes) | hubs in `tracks/`, auto-list by tag | `/tracks/<name>/` |
| **Series** (narrative) | `series/brewer-to-ai.md` | `/series/brewer-to-ai/` |
| Topics (all tags) | auto-generated | `/tags/` |
| Archive (timeline) | auto-generated | `/archive/` |

**Track tags** (use one as a post's first tag to slot it into a track): `commercial-planning`, `sales-intelligence`, `marketing`, `fpna`, `esg`, `ehs`, `forecasting` (business tracks); `brewing-science`, `distilling-maturation`, `winemaking` (production & science tracks). Series tag: `brewer-to-ai`.

**Folder map:**
```
_config.yml          ← site settings + analytics IDs (the main control file)
_posts/              ← all blog posts
_layouts/            ← default / post / page templates
_includes/           ← head, header, footer, share, related, analytics, structured-data
tracks/              ← 7 track hub pages + index
series/              ← narrative series landing page
assets/css/style.css ← all styling
assets/favicon.svg   ← logo/favicon
index.html           ← homepage (SEO/GEO landing)
about.md             ← About + bio + press + contact + privacy
feed.xml / feed.xsl  ← styled RSS feed
robots.txt / llms.txt← crawler + AI-crawler instructions
sitemap.xml          ← auto-generated (jekyll-sitemap)
```

---

## 5. Analytics — what's connected & where to look

Configured in `_config.yml` (only loads on the live site, not local preview):

| Tool | ID | Dashboard | Shows |
|---|---|---|---|
| **Google Analytics 4** | `G-1ZHW47YJDC` | analytics.google.com | Visitors, location, time, traffic source |
| **Microsoft Clarity** | `ww9jrvdoh1` | clarity.microsoft.com | Session recordings + heatmaps |

Both are anonymous/aggregate (no individual identities). Data needs **real browser visits** + a processing delay (Clarity up to ~2h). Ad blockers can hide your own visits.

To add another provider, set its key in `_config.yml`: `cloudflare_analytics` or `goatcounter`.

---

## 6. SEO & GEO (already built in)

- **SEO:** `jekyll-seo-tag` (titles, meta, OpenGraph, canonical), `sitemap.xml`, styled RSS, clean permalinks, internal linking via tracks/related/tags.
- **GEO (AI answer engines):** `FAQPage` + `BlogPosting` + `Person`/`Blog` JSON-LD, answer-first posts, `llms.txt`, and `robots.txt` that welcomes GPTBot/PerplexityBot/ClaudeBot.
- **Google Search Console:** property verified via the GA4 tag. Sitemap submitted: `sitemap.xml`. New sites take days–weeks to index — be patient; nudge via "Request indexing" in Search Console.

---

## 7. Security

- **Branch protection** is ON for `main` (no force-push, no deletion).
- Repo is **public** (readable/forkable — normal for a blog) but only you can push/edit.
- **⚠️ Enable 2FA** on your GitHub account (Settings → Password and authentication) — the most important protection.

---

## 8. Local preview (optional — needs Ruby)

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000  (analytics are OFF locally by design)
```

---

## 9. Gotchas & fixes (learned the hard way)

- **Post dated today not showing?** `future: true` is set in `_config.yml` so today-dated posts publish — keep it.
- **A `.txt`/`.xml` file showing as HTML?** It needs `layout: null` in its front matter (the global default layout otherwise wraps it). `robots.txt` and `llms.txt` already have this.
- **Build "errored"?** Almost always an unquoted `title:`/`description:` with a colon, or a broken `faq:` block. Quote them.
- **Sitemap "Couldn't fetch" in Search Console?** Normal for a new site — Google just hasn't crawled yet. Wait 1–3 days.

---

## 10. Quick command cheat-sheet

```bash
gh auth login                                              # sign in on a new machine
git clone https://github.com/AnkurNapa/ankurnapa.github.io.git
git add -A && git commit -m "..." && git push origin main  # publish
gh api repos/AnkurNapa/ankurnapa.github.io/pages/builds/latest --jq '.status'  # build status
```

**Tip:** open this repo in **Claude Code** on the new laptop and point it at this file — it can pick up exactly where we left off.
