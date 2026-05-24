# Per-post social share images (OG images)

How WhatsApp / LinkedIn / X / iMessage link previews get a **unique image per
article** instead of one shared default.

## How it works

- `jekyll-seo-tag` emits `<meta property="og:image">` from each page's `image:`
  front matter. That tag is what chat/social apps read to build the preview card.
- Every post in `_posts/` declares its own:
  ```yaml
  image: /assets/og/<slug>.png
  ```
  where `<slug>` is the post filename minus the `YYYY-MM-DD-` date prefix.
- The matching 1200×630 card lives at `assets/og/<slug>.png`.
- Non-article pages (homepage, about, tracks, tags, archive) fall back to the
  site default `/assets/og-default.png` (set in `_config.yml` → `defaults`).

## Generating the cards

`tools/gen_og_images.py` (Python + Pillow) renders every card from the post's
**title** (headline) and **tags** (footer), in the site's brand palette
(cream bg, amber kicker, near-black headline, wine-maroon tags).

```bash
# from the repo root
python tools/gen_og_images.py            # (re)generate cards + add image: to new posts
python tools/gen_og_images.py --no-patch # only (re)generate images, don't touch front matter
```

**It is idempotent.** Re-running:
- always regenerates the PNGs (safe to re-run after tweaking the design), and
- only inserts the `image:` line into posts that don't have one yet.

So the routine after writing a new post is simply: run the script, then commit
the new `assets/og/*.png` plus the post.

Requirements: `pip install pillow pyyaml`. Fonts: Segoe UI (Windows). On another
OS, point `F_BOLD`/`F_REG` in the script at a local bold/regular TTF.

## Gotchas

- **WhatsApp caches previews.** New links show the new card immediately, but a
  URL you already shared may keep showing the old image until the cache expires.
  Force a refresh by re-scraping the URL in Facebook's **Sharing Debugger**
  (WhatsApp uses the same crawler).
- **Title drives the image.** If you change a post's title and want the card to
  match, delete `assets/og/<slug>.png` and re-run the script (it regenerates all
  cards anyway, so just re-running is enough).
- Keep cards lean (these are ~60 KB PNGs) — well under social-preview size limits.
