# CLAUDE.md — Beer, Wine, Whiskey & AI (main blog)

Working instructions for this repo. Deeper build detail lives in [ONBOARDING.md](ONBOARDING.md); this file is the fast, authoritative summary of **how to write and style posts**. Its sibling is the guidebook at `../brewing-distilling-ai` (the design source this blog matches).

## What this is
Jekyll blog on GitHub Pages. Remote `AnkurNapa/ankurnapa.github.io`, branch `main`, permalink `/:year/:title/`. `_config.yml` sets `future: false` — never date a post later than build time. No local Jekyll/bundler; validate output with Python/curl, not `jekyll serve`.

Multi-language: English in `_posts/`, translations in `_hi/` (Hindi), `_de/` (German), `_mr/` (Marathi). Any change to shared markup, palette, or diagrams must be applied to the translated collections too.

## Writing a post
Filename `_posts/YYYY-MM-DD-slug.md`. Required structure, in order:
1. Frontmatter: `layout: post`, `title`, `image: /assets/og/<slug>.png`, `description`, `date` (`HH:MM:SS -0700`), `updated`, `tags`, and a `faq:` block (3 Q&A) that is reproduced **verbatim** as the closing `## Frequently asked questions`.
2. A single bold lead paragraph starting `**Short answer: ` and ending `**`.
3. **One** inline SVG `<figure>` (see palette below), with `role="img"`, a descriptive `aria-label`, HTML entities (never raw `&` or smart quotes), and a `<figcaption>`.
4. Body `##` sections, then `## Where this breaks` (honest caveats), then `## The bottom line`, then the FAQ.
5. Cross-links via `{{ '/YYYY/slug/' | relative_url }}` — verify the year against the actual post filename.

Tags: **first tag = track** (drives the post banner and auto-populates `/tracks/<track>/`). Add a series tag when the post belongs to a series; series index pages live in `series/`, track pages in `tracks/`.

## Reading flow (industry-aware)
So a reader who arrives from one industry (wine, beer, whiskey, or a business track) stays in it:
- **Related reading** (`_includes/related.html`) weights the reader's first tag heavily (+1000 vs +1 per other shared tag) so same-industry articles lead, and shows a **"More in <track> →"** hub link mapping the first tag to its `/tracks/<track>/` page.
- **Prev/next** (`_layouts/post.html`) walk the same first-tag track (wine → wine), not site-wide chronology; they fall back to chronological only for posts with no track tag.
- The first-tag → track-hub map (in both files) must stay in sync with the track pages: `winemaking`→winemaking-ai, `brewing-science`→brewing-science-ai, `distilling-maturation`, `commercial-planning`, `sales-intelligence`, `marketing`, `fpna`→financial-planning-analytics, `esg`, `ehs`, `forecasting`→sales-forecasting.

## House style
- **No em dashes.** Despite the older back-catalogue, new writing must avoid `—`, en dashes, curly quotes, and stray spaces. Use colons (introduce/explain), commas or parentheses (asides), semicolons (join clauses), or a sentence split. Keep compound-word hyphens (soft-sensor, off-batch).
- Honest, no-hype, practitioner voice. International/British spellings (colour, flavour, litre).
- Proper grammar and punctuation, every language.

## Design system (teal "guidebook" theme, since 2026-07-07)
The whole site uses the teal design ported from `../brewing-distilling-ai`. Light-only (no dark mode).
- Palette: teal `#00695c`, deep `#06483f`, mid `#4db6a2`, section `#f0f6f5`, card border `#d8e6e1`, tint `#e3f3ec`, pink accent `#ff4081`, muted `#7a8b87`, body text `#4a4a4a`.
- Fonts: Poppins (display) + Open Sans (body) via Google Fonts.
- Single stylesheet: `assets/css/style.css`. Layouts in `_layouts/`, partials in `_includes/`.

### Inline SVG figure palette (teal — do NOT use the retired warm hexes)
bg `#ffffff`; light box fill `#f0f6f5`; primary/stroke/header `#00695c`; deep box fill + ink `#06483f`; light text on deep boxes `#cfe6df`; muted `#4a6b64`; mid teal `#4db6a2`; green accent `#2e9e7c`; pink accent `#ff4081`. Never reintroduce `#fdfbf7`/`#b45309`/`#8a5a2b`/`#7a1f3d`/`#6b6258`/`#1c1a17`.

## OG share images
`python3 tools/gen_og_images.py` regenerates all cards (palette is teal). It patches `image:` into frontmatter when missing. It re-renders every PNG, so when only content changed, stage just the new/changed cards; when the palette itself changes, all cards legitimately change and should be committed.

## Ship checklist
1. Validate frontmatter YAML, balanced `<svg>/<figure>`, no raw `&`, no em dashes.
2. XML-parse each SVG; confirm cross-link targets exist.
3. Generate OG image(s); recolor any new diagram to the teal palette.
4. Commit (conventional commits; attribution disabled globally — no Co-Authored-By trailer) and push to `main`.
5. GitHub Pages CDN serves stale 404s on brand-new paths for ~1 min; verify with a `?cb=` cache-buster.
