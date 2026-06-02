# German Translation Spec (`/de/` edition)

How to translate one English post in `_posts/<file>.md` into a German post at
`_de/<same-file>.md`. Keep the filename **identical** (same `YYYY-MM-DD-slug.md`).

## Front matter
Keep all keys in **English**. Translate only the human-readable *values* noted below.

- `layout: post`  ← add/keep explicitly
- `lang: de`      ← add explicitly
- `title:`        ← TRANSLATE to natural German
- `description:`  ← TRANSLATE
- `image:`        ← KEEP unchanged (shared OG image, e.g. `/assets/og/<slug>.png`)
- `date:`         ← KEEP byte-for-byte identical to source
- `updated:`      ← KEEP identical (if present)
- `author:`       ← KEEP (if present)
- `tags:`         ← KEEP English, unchanged (they drive track filters & cross-refs)
- `faq:`          ← TRANSLATE each `q:` and `a:` value; keep the list structure
- `permalink:`    ← ADD: `/de/<YEAR>/<slug>/`
    - `<YEAR>` = the year of the `date:` field
    - `<slug>` = filename with the leading `YYYY-MM-DD-` removed and `.md` removed
    - Example: `_posts/2026-05-29-claude-opus-ipa-hop-workflow.md`
      → `permalink: /de/2026/claude-opus-ipa-hop-workflow/`
- Preserve any other front-matter keys as-is (prefix internal-path values with `/de` if they are site links).

## Body — translate
- All prose, headings, list items, blockquotes, table cell text.
- The bold "short answer" lead paragraph.
- SVG diagrams: translate visible `<text>` content, the `aria-label`, and `<figcaption>`. Keep every coordinate, color, width, path, viewBox, and tag exactly.
- `alt` text on any image/figure.
- The "Frequently asked questions" section body (mirror the translated `faq:`).

## Body — DO NOT translate / change
- Code blocks and inline `code`, numbers, units, dates inside text, math.
- Brand/tool/standard names: Power BI, Tableau, Power Apps, Power Platform, Claude, ChatGPT, Databricks, Snowflake, Microsoft Fabric, Excel, NDVI, ABV, IBU, OG, TTB, CSRD, SECR, EPR, S&OP, FP&A, COGS, OEE, TPO, CIP, NIR, IoT, ESG, EHS, DTC, etc. (German prose may surround them.)
- `/assets/...` links (images) — keep unchanged.
- External `http(s)://` links — keep unchanged.

## Internal links → prefix with `/de`
Any **site-internal** link target that starts with `/` and points to a page (NOT `/assets/...`) must get `/de` prepended. This covers both Liquid form and plain markdown:
- `{{ '/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}` → `{{ '/de/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}`
- `]({{ '/series/brewer-to-ai/' | relative_url }})` → `]({{ '/de/series/brewer-to-ai/' | relative_url }})`
- `/tracks/...`, `/tags/...`, `/archive/`, `/about/`, `/contact/`, `/search/` → all get `/de` prefixed.
- Leave `/assets/...` and external URLs alone.

## Tone
Native, professional German. Keep it practitioner-grounded and hype-free, like the source. Translate idioms by meaning, not word-for-word ("the angel's share" → keep "Angels' Share" as the term of art; "grain to glass" → "vom Korn ins Glas"). Match the English register (casual-expert; "du" is acceptable for direct address).

## Gate note (for the agent)
When a `Write` is intercepted by a `[Fact-Forcing Gate]` message, briefly state: the file being written, that it mirrors the matching `_posts/` source, that no existing `_de/` file serves it, and the user's instruction (build the German edition). Then **retry the identical Write once** — it will succeed.
