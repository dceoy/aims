#!/usr/bin/env python3
r"""Lint the AIMS Market Knowledge Wiki structure."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Final

_REQUIRED: Final[tuple[str, ...]] = ("index.md", "log.md", "wiki/overview.md")
_LINK_RE: Final[re.Pattern[str]] = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
_SHA_RE: Final[re.Pattern[str]] = re.compile(r"<!-- source-sha256: ([0-9a-f]{64}) -->")


def _markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def _links(markdown: str) -> list[str]:
    return [m.group(1) for m in _LINK_RE.finditer(markdown)]


def _is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:", "#"))


def lint_wiki(wiki_root: Path) -> list[str]:
    """Return lint errors for a wiki root."""
    errors: list[str] = []
    for required in _REQUIRED:
        path = wiki_root / required
        if not path.is_file():
            errors.append(f"missing required file: {required}")

    files = _markdown_files(wiki_root) if wiki_root.exists() else []
    for path in files:
        rel = path.relative_to(wiki_root).as_posix()
        text = path.read_text()
        if not text.strip():
            errors.append(f"empty markdown page: {rel}")
        for link in _links(text):
            if _is_external(link):
                continue
            target = link.split("#", 1)[0]
            if not target:
                continue
            if not (path.parent / target).resolve().is_file():
                errors.append(f"broken link in {rel}: {link}")

    index = wiki_root / "index.md"
    if index.is_file():
        index_text = index.read_text()
        for page in sorted((wiki_root / "wiki").rglob("*.md")):
            rel = page.relative_to(wiki_root).as_posix()
            if rel not in index_text:
                errors.append(f"wiki page not reachable from index.md: {rel}")

    for source in sorted((wiki_root / "sources").glob("*.md")):
        text = source.read_text()
        rel = source.relative_to(wiki_root).as_posix()
        if not text.startswith(
            "<!-- generated-by: market-wiki/render_wiki_source.py -->"
        ):
            errors.append(f"source missing generated marker: {rel}")
        if not _SHA_RE.search(text):
            errors.append(f"source missing artifact fingerprint: {rel}")

    sources = sorted((wiki_root / "sources").glob("*.md"))
    log = wiki_root / "log.md"
    if sources and log.is_file():
        latest = sources[-1].relative_to(wiki_root).as_posix()
        if latest not in log.read_text():
            errors.append(f"log missing latest source entry: {latest}")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-root", default=Path("knowledge"), type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = lint_wiki(args.wiki_root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"Wiki lint passed: {args.wiki_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
