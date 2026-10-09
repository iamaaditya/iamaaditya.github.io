"""Site hooks: blog listing on the home page, post meta lines and RSS feed.

The home page (`docs/index.md`) contains a `<!-- BLOG_LISTING -->` placeholder
which is replaced at build time with a card per blog post (newest first),
mirroring the behaviour of the old Jekyll landing page.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

import mkdocs
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
LISTING_PLACEHOLDER = "<!-- BLOG_LISTING -->"


def _front_matter(text: str) -> tuple[dict[str, str], str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip().strip('"')
    return meta, text[m.end():]


def _iter_posts(docs_dir: Path) -> list[dict]:
    posts = []
    for path in docs_dir.rglob("*.md"):
        meta, body = _front_matter(path.read_text(encoding="utf-8"))
        if meta.get("post") != "true":
            continue
        rel = path.relative_to(docs_dir).with_suffix("")
        url = "/" + rel.as_posix() + "/"
        posts.append(
            {
                "title": meta.get("title", path.stem),
                "date": meta.get("date", "")[:10],
                "url": url,
                "excerpt": _excerpt(body),
            }
        )
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def _excerpt(body: str, limit: int = 340) -> str:
    """First meaningful paragraph, lightly de-markdowned."""
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block[0] in "#|<!" or block.startswith("!["):
            continue
        lines = block.splitlines()
        # skip setext headings ("Title\n=====") and pure lists / tables
        if len(lines) > 1 and re.fullmatch(r"[=\-]+", lines[1].strip()):
            continue
        if all(re.match(r"\s*(?:[*+-]|\d+\.)\s+", ln) for ln in lines):
            continue
        if all(ln.strip().startswith("|") for ln in lines):
            continue
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", block)
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"[`*_]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) < 60:
            continue
        if len(text) > limit:
            text = text[:limit].rsplit(" ", 1)[0] + "…"
        return text
    return ""


def _format_date(iso: str) -> str:
    try:
        d = datetime.strptime(iso[:10], "%Y-%m-%d")
    except ValueError:
        return iso
    return f"{d:%B} {d.day}, {d.year}"


def _listing_markdown(posts: list[dict]) -> str:
    out = []
    for p in posts:
        out.append(
            f'<article class="post-card" markdown="1">\n'
            f'### [{p["title"]}]({p["url"]})\n\n'
            f'<span class="post-date">{_format_date(p["date"])}</span>\n\n'
            f'{p["excerpt"]}\n\n'
            f'[Read more]({p["url"]}){{ .read-more }}\n'
            f"</article>\n"
        )
    return "\n".join(out)


def on_page_markdown(markdown: str, *, page: Page, config: MkDocsConfig, files: Files) -> str:
    docs_dir = Path(config["docs_dir"])
    if page.file.src_uri == "index.md" and LISTING_PLACEHOLDER in markdown:
        return markdown.replace(LISTING_PLACEHOLDER, _listing_markdown(_iter_posts(docs_dir)))
    meta, body = _front_matter(markdown)
    if meta.get("post") == "true" and not markdown.lstrip().startswith("<div class=\"post-meta\""):
        date = _format_date(meta.get("date", ""))
        markdown = f'<div class="post-meta">Written on {date}</div>\n\n' + markdown
    return markdown


def on_post_build(*, config: MkDocsConfig) -> None:
    """Emit /feed.xml so the historical RSS URL keeps working."""
    site_url = (config.get("site_url") or "https://iamaaditya.github.io/").rstrip("/")
    posts = _iter_posts(Path(config["docs_dir"]))
    items = []
    for p in posts:
        try:
            dt = datetime.strptime(p["date"][:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            pub = format_datetime(dt)
        except ValueError:
            pub = ""
        items.append(
            "    <item>\n"
            f"      <title>{escape(p['title'])}</title>\n"
            f"      <link>{site_url}{p['url']}</link>\n"
            f"      <guid isPermaLink=\"true\">{site_url}{p['url']}</guid>\n"
            f"      <pubDate>{pub}</pubDate>\n"
            f"      <description>{escape(p['excerpt'])}</description>\n"
            "    </item>"
        )
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n  <channel>\n'
        f"    <title>{escape(config['site_name'])}</title>\n"
        f"    <link>{site_url}/</link>\n"
        f"    <description>{escape(config.get('site_description') or '')}</description>\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )
    (Path(config["site_dir"]) / "feed.xml").write_text(feed, encoding="utf-8")
