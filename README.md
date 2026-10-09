# iamaaditya.github.io

Personal website of **Aaditya (Adi) Prakash** — blog, about/CV and collected notes.

Built with [MkDocs](https://www.mkdocs.org/) +
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), managed with
[uv](https://docs.astral.sh/uv/). Content lives in `docs/`; every historical URL
(blog permalinks, `/notes/...`, `/research/...`) is preserved.

## Local development

```bash
uv sync                # install mkdocs-material into .venv (Python via uv)
uv run mkdocs serve    # http://127.0.0.1:8000
```

Useful extras:

```bash
uv run mkdocs build             # build into site/
uv run python scripts/check_links.py   # validate internal links of the built site
```

## How the site is put together

* `docs/index.md` — landing page. The blog listing is generated at build time by
  `hooks/site_hooks.py`, which replaces the `<!-- BLOG_LISTING -->` placeholder with
  one card per page that has `post: true` in its front matter (newest first), and
  also emits `/feed.xml` (RSS).
* `docs/about/` — biography, experience timeline, publications, patents, teaching.
* `docs/notes/` — the notes collection; `docs/notes/index.md` is the curated,
  card-based directory. Sub-pages keep their original content.
* `docs/stylesheets/extra.css` — theme customization (light/dark, cards, timeline).
* `docs/javascripts/email.js` — assembles the contact `mailto:` link at render time
  so the address is never present in the served HTML (spam-bot protection).
* `docs/javascripts/mathjax.js` — MathJax v3 config for `\( \)` / `$$ $$` math.
* `scripts/migrate.py` — the one-off Jekyll → MkDocs migration (kept for provenance).
* `legacy/` — mirrored figures from the old aaditya.info site, self-hosted under
  `/assets/legacy/`.

## Deployment (GitHub Pages)

The site is deployed by `.github/workflows/deploy-pages.yml` (build with uv +
mkdocs, upload and deploy with the official Pages actions).

One-time repository setting (Settings → Pages → *Build and deployment* →
**Source: GitHub Actions**). After that, every push to `master` publishes the site.

## Adding a blog post

Create `docs/<year>/<month>/<slug>.md` (any path works) with front matter:

```markdown
---
title: My new post
date: 2026-01-01
post: true
---
```

It automatically appears on the landing page and in `/feed.xml`.

Test
