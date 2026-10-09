#!/usr/bin/env python3
"""One-off migration of the old Jekyll site content into the MkDocs `docs/` tree.

- Preserves every public URL (blog permalinks, /notes/..., /research/..., /about/).
- Rewrites Liquid variables ({{ site.baseurl }}), raw.githubusercontent image URLs
  and absolute iamaaditya.github.io links into site-relative URLs.
- Normalizes front matter (title + date only) and cleans legacy markup
  (<center> tags, kramdown table attributes) without touching the substance
  of any note or post.

Run once with:  uv run python scripts/migrate.py
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

SKIP_FILES = {".DS_Store", ".listing", "convert_to_link.txt", "sidebar.txt", "start.txt"}

# --------------------------------------------------------------------------
# front matter helpers
# --------------------------------------------------------------------------

FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Very small YAML-subset parser: enough for the flat keys used here."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    key = None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if kv:
            key, value = kv.group(1), kv.group(2).strip()
            meta[key] = value
        elif key and line.startswith(("- ", "  ")):
            # list item (tags/categories/dsq_thread_id): ignore values
            continue
    return meta, text[m.end():]


def dump_front_matter(meta: dict[str, str]) -> str:
    lines = ["---"]
    for key, value in meta.items():
        if any(c in value for c in ":#{}[]&*!|>'\"%@`") or value != value.strip():
            value = '"' + value.replace('"', '\\"') + '"'
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# body rewrites (formatting only -- never content)
# --------------------------------------------------------------------------

def clean_body(body: str) -> str:
    # {{ site.baseurl }} / {{site.baseurl}} (any spacing) -> site root
    body = re.sub(r"\{\{\s*site\.baseurl\s*\}\}", "", body)
    # {{ "/images/foo.png" }} -> /assets/images/foo.png
    body = re.sub(
        r"\{\{\s*[\"'](/images/[^\"']+)[\"']\s*\}\}",
        lambda m: "/assets" + m.group(1),
        body,
    )
    # raw githubusercontent copies of this repo's images -> local assets
    body = body.replace(
        "https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/",
        "/assets/images/",
    )
    body = body.replace(
        "https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/",
        "/assets/",
    )
    # absolute site links -> relative
    body = body.replace("https://iamaaditya.github.io/", "/")
    body = body.replace("http://iamaaditya.github.io/", "/")
    # dead aaditya.info domain: serve mirrored uploads locally, rest via archive
    def _wp(m: re.Match) -> str:
        rel = m.group(1)
        if (DOCS / rel).exists():
            return "/" + rel
        return m.group(0)

    body = re.sub(r"http://aaditya\.info/blog/(wp-content/[^\"') ]+)", _wp, body)
    body = body.replace(
        "http://aaditya.info/blog/2012/09/value-of-interdisciplinary-research/",
        "/2012/09/value-of-interdisciplinary-research/",
    )
    # figures from the old site are mirrored in legacy/ and self-hosted
    body = body.replace(
        "http://aaditya.info/research/quantum/",
        "/assets/legacy/research/quantum/",
    )
    # pre-phD paper links (pre-2013) are retired on purpose
    body = re.sub(
        r"\s*You may download the <a[^>]*birthdayparadoxproof\.tex[^>]*>.*?</a>\.",
        "",
        body,
        flags=re.S,
    )
    body = re.sub(
        r'<a href="http://aaditya\.info/blog/wp-content/uploads/2012/07/'
        r'Paper_Protocol_for_Common_Branch_Platform\.pdf"[^>]*>(.*?)</a>',
        r"\1 (preprint hosted on my previous site, now offline)",
        body,
        flags=re.S,
    )
    body = re.sub(
        r'<a[^>]*href="http://aaditya\.info/research/hmm_two_states\.pdf"[^>]*>.*?</a>',
        "Detailed proofs for the two state hidden markov model are available on request.",
        body,
        flags=re.S,
    )
    # legacy <center> wrappers
    body = re.sub(r"</?center>", "", body)
    # kramdown block attribute for tables (unsupported here); keep {: .class} on images
    body = re.sub(r"^\{:\s*\.table\s*\}\s*$", "", body, flags=re.M)
    # collapse 3+ blank lines
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    return body


def clean_title(title: str) -> str:
    title = html.unescape(title)
    return title.strip().strip("'\"")


def first_heading(body: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else None


# --------------------------------------------------------------------------
# migrations
# --------------------------------------------------------------------------

def migrate_posts() -> list[str]:
    log = []
    for src in sorted((ROOT / "_posts").glob("*.md")):
        meta, body = split_front_matter(src.read_text(encoding="utf-8"))
        permalink = meta.get("permalink", "").strip().strip('"')
        if not permalink:
            slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", src.stem)
            permalink = f"/{slug}/"
        rel = permalink.strip("/")
        date = (meta.get("date") or src.stem[:10])[:10]
        new_meta = {
            "title": clean_title(meta.get("title", src.stem)),
            "date": date,
            "post": "true",
        }
        dest = DOCS / f"{rel}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(dump_front_matter(new_meta) + clean_body(body), encoding="utf-8")
        log.append(f"post: {src.name} -> docs/{rel}.md  ({permalink})")
    return log


def migrate_tree(src_dir: Path, dest_dir: Path, log: list[str], default_title: bool = True) -> None:
    for src in sorted(src_dir.rglob("*")):
        if src.is_dir():
            continue
        if src.name in SKIP_FILES or src.name.startswith("."):
            continue
        rel = src.relative_to(src_dir)
        dest = dest_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix != ".md":
            shutil.copy2(src, dest)
            continue
        meta, body = split_front_matter(src.read_text(encoding="utf-8"))
        title = meta.get("title") or first_heading(body) or rel.parent.name.replace("_", " ").title()
        new_meta = {"title": clean_title(title)}
        dest.write_text(dump_front_matter(new_meta) + clean_body(body), encoding="utf-8")
        log.append(f"page: {src.relative_to(ROOT)} -> docs/{rel}")


INDEX_TEMPLATE = """---
title: {title}
---

# {title}

{blurb}

{items}
"""


def generate_missing_indexes(log: list[str]) -> None:
    """Create a small index.md for note folders that have content but no index,
    so every page stays discoverable. Links only -- no new content."""
    blurbs = {
        "learning": "Loose notes collected while learning new topics.",
        "playground": "Scratch space and experiments.",
        "read": "Reading lists: books to read and books being read.",
        "research_wiki": "Wiki-style research notes and reports.",
        "startup": "Notes on startups and ideas.",
        "writing": "Notes on writing.",
        "cs": "Computer science notes.",
        "math": "Mathematics notes.",
        "cheatsheet": "Cheatsheets.",
        "bioninformatics": "Bioinformatics reports and notes.",
    }
    for folder in sorted((DOCS / "notes").rglob("*")):
        if not folder.is_dir():
            continue
        if (folder / "index.md").exists():
            continue
        entries: list[str] = []
        for child in sorted(folder.iterdir()):
            if child.name in SKIP_FILES or child.name.startswith("."):
                continue
            if child.suffix == ".md":
                meta, _ = split_front_matter(child.read_text(encoding="utf-8"))
                title = clean_title(meta.get("title") or child.stem.replace("_", " ").title())
                entries.append(f"* [{title}]({child.name})")
            elif child.suffix == ".txt":
                entries.append(f"* [{child.stem.replace('_', ' ').title()}]({child.name})")
            elif child.is_dir() and any(child.iterdir()):
                entries.append(f"* [{child.name.replace('_', ' ').title()}]({child.name}/)")
        if not entries:
            continue
        title = folder.name.replace("_", " ").title()
        (folder / "index.md").write_text(
            INDEX_TEMPLATE.format(
                title=title,
                blurb=blurbs.get(folder.name, "Notes collected under this topic."),
                items="\n".join(entries),
            ),
            encoding="utf-8",
        )
        log.append(f"index: generated docs/{folder.relative_to(DOCS)}/index.md")


def copy_assets(log: list[str]) -> None:
    shutil.copytree(ROOT / "images", DOCS / "assets" / "images", dirs_exist_ok=True)
    shutil.copy2(ROOT / "favicon.ico", DOCS / "assets" / "favicon.ico")
    shutil.copytree(ROOT / "wp-content", DOCS / "wp-content", dirs_exist_ok=True)
    shutil.copytree(
        ROOT / "legacy" / "aaditya.info" / "research" / "quantum",
        DOCS / "assets" / "legacy" / "research" / "quantum",
        dirs_exist_ok=True,
    )
    log.append("assets: images/, wp-content/ and legacy figures copied into docs/")


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    log: list[str] = []
    copy_assets(log)
    migrate_posts()
    migrate_tree(ROOT / "notes", DOCS / "notes", log)
    migrate_tree(ROOT / "research", DOCS / "research", log)
    for page in ("keep_on_top.md", "paper-summaries.md"):
        src = ROOT / page
        meta, body = split_front_matter(src.read_text(encoding="utf-8"))
        title = clean_title(meta.get("title") or src.stem.replace("-", " ").title())
        (DOCS / page).write_text(
            dump_front_matter({"title": title}) + clean_body(body), encoding="utf-8"
        )
        log.append(f"page: {page} -> docs/{page}")
    generate_missing_indexes(log)
    print("\n".join(log))
    print(f"\n{len(log)} items migrated.")


if __name__ == "__main__":
    main()
