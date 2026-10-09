#!/usr/bin/env python3
"""Validate internal links and asset references in the built `site/` directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"')


def resolve(href: str) -> Path | None:
    if href.startswith(("#", "mailto:", "tel:")) or "://" in href or href.startswith("//"):
        return None
    path = href.split("#", 1)[0].split("?", 1)[0]
    if not path or not path.startswith("/"):
        return None  # anchors / relative links are validated by mkdocs itself
    rel = path.lstrip("/")
    candidates = [
        SITE / rel,
        SITE / rel / "index.html",
        SITE / (rel + ".html"),
    ]
    if any(c.exists() for c in candidates):
        return None
    return SITE / rel


def main() -> int:
    bad: list[tuple[str, str]] = []
    for html_file in sorted(SITE.rglob("*.html")):
        text = html_file.read_text(encoding="utf-8", errors="ignore")
        for href in ATTR_RE.findall(text):
            missing = resolve(href)
            if missing is not None:
                bad.append((str(html_file.relative_to(SITE)), href))
    for page, href in bad:
        print(f"{page}: {href}")
    print(f"\n{len(bad)} broken internal references.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
