# Indic Translation Spec (parametrised per language)

Your prompt gives you a **language name** and a **CODE** (one of: hi=Hindi,
mr=Marathi, kn=Kannada, bn=Bangla/Bengali, ta=Tamil). Translate English posts
in `_posts/<file>.md` into that language at `_<CODE>/<same-file>.md`. Keep the
filename identical. Write in the **native script** (Devanagari for hi/mr,
Kannada script for kn, Bengali script for bn, Tamil script for ta).

This mirrors the German spec exactly, with `/de/` → `/<CODE>/` and `lang: de`
→ `lang: <CODE>`.

## Front matter — keep keys English, translate values
- `layout: post`              (add)
- `lang: <CODE>`              (add)
- `title:`                    TRANSLATE
- `description:`              TRANSLATE
- `image:`                    KEEP unchanged (shared OG image)
- `date:` / `updated:`        KEEP byte-for-byte identical
- `author:`                   KEEP if present
- `tags:`                     KEEP English, unchanged (they drive track filters)
- `faq:`                      TRANSLATE each q/a; keep list structure
- `permalink: /<CODE>/<YEAR>/<slug>/`   (add)
    - YEAR = year of the `date:` field
    - slug = filename minus the leading `YYYY-MM-DD-` and minus `.md`

## Body — translate
All prose, headings, lists, blockquotes, table text, the bold "short answer"
lead, SVG visible `<text>` + `aria-label` + `<figcaption>`, image alt text, and
the FAQ section body (mirror the translated `faq:`).

## Body — DO NOT change
- Code/inline code, numbers, units, math, dates inside text.
- Brand/tool/standard names stay in Latin script: Power BI, Tableau, Power Apps,
  Claude, ChatGPT, Databricks, Snowflake, Microsoft Fabric, Excel, NDVI, ABV,
  IBU, TTB, CSRD, SECR, EPR, S&OP, FP&A, COGS, OEE, CIP, NIR, IoT, ESG, EHS, DTC,
  "AI" (you may keep the acronym "AI" in Latin within native prose).
- `/assets/...` links and external `http(s)://` links — keep unchanged.

## Internal links → prefix with `/<CODE>`
Every site-internal link starting with `/` (except `/assets/...`) gets `/<CODE>`
prepended, in both Liquid and markdown form:
- `{{ '/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}`
  → `{{ '/<CODE>/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}`
- `/tracks/...`, `/series/...`, `/tags/...`, `/archive/`, `/about/`, etc. → `/<CODE>/...`

## YAML safety (IMPORTANT)
Inside a double-quoted YAML value (title/description/faq q/a), NEVER use a
straight ASCII double-quote `"`. For quotation inside the text, use the target
language's typographic quotes or guillemets. A stray ASCII `"` breaks the build.

## Format reference
For the exact output shape, look at an existing German post as a structural
template (same layout, just a different language + `/de/` prefix):
`_de/2026-05-25-can-ai-predict-wine-quality.md` and its English source
`_posts/2026-05-25-can-ai-predict-wine-quality.md`.

## Tone
Native, professional, practitioner-grounded, hype-free — matching the English
register. Translate idioms by meaning. Keep widely-used English technical terms
where a forced translation would read awkwardly to a practitioner.

## Gate note
If a `Write` returns a `[Fact-Forcing Gate]` message, briefly state the file,
that it mirrors the matching `_posts/` source and no `_<CODE>/` file serves it,
and the user's instruction; then retry the IDENTICAL Write once — it succeeds.
