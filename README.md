# Brews & Bytes — a Jekyll blog on beer + AI

A static blog built with Jekyll, hosted free on GitHub Pages, optimized for both
**SEO** (Google/Bing) and **GEO** (AI answer engines like ChatGPT, Perplexity,
Google AI Overviews, and Claude).

## ✏️ Config

`_config.yml` is already set up for **ankurnapa** / **Ankur Napa**. You can still
tweak `title`, `tagline`, and `description` anytime — canonical URLs, sitemap,
RSS, `llms.txt`, and `robots.txt` all derive from it automatically.

## 🚀 Publish to GitHub Pages (no domain needed)

1. On GitHub, create a **public** repo named exactly `ankurnapa.github.io`.
2. Push this folder to it:
   ```bash
   git init
   git add .
   git commit -m "feat: initial beer + AI blog"
   git branch -M main
   git remote add origin https://github.com/ankurnapa/ankurnapa.github.io.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / root.**
4. Wait ~1 minute. Your blog is live at `https://ankurnapa.github.io`.

## 🖥️ Preview locally (optional)

Requires Ruby. Then:
```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

## ✍️ Writing a new post

Add a file to `_posts/` named `YYYY-MM-DD-title-with-dashes.md`:

```markdown
---
layout: post
title: "Your Headline as a Question Works Great for GEO"
description: "One-sentence summary — used for meta description and AI snippets."
date: 2026-06-01
updated: 2026-06-01
tags: [beer, ai]
faq:
  - q: "A question readers actually ask?"
    a: "A direct, quotable answer in 1–2 sentences."
---

**Lead with a bold, direct answer in the first paragraph.** AI engines cite
concise factual statements, so put the payoff up top, then expand below.
```

### Why this is GEO-optimized
- **Answer-first** posts → AI engines quote your opening paragraph.
- **`faq:` front matter** → renders visible Q&A *and* emits `FAQPage` JSON-LD.
- **`llms.txt`** → tells AI crawlers what the site is and lists every post.
- **`jekyll-seo-tag`** → `BlogPosting` structured data, OpenGraph, canonical URLs.
- **`updated:` dates + author** → E-E-A-T freshness/credibility signals.

## 📁 Structure

```
_config.yml                 ← the only file you must edit
Gemfile                     ← GitHub Pages gem
index.html                  ← home / post list
about.md                    ← about page (E-E-A-T)
llms.txt                    ← AI-crawler guide (auto-generated from posts)
robots.txt                  ← allows all crawlers + points to sitemap
_posts/                     ← your blog posts
_layouts/                   ← default / post / page templates
_includes/                  ← head, header, footer, FAQ JSON-LD
assets/css/style.css        ← styling
```
