#!/usr/bin/env python3
"""Generate and validate Hugo shadow content from AIMS OKF Markdown."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

FRONT_MATTER = re.compile(r"\A---\n(?P<meta>.*?)\n---\n(?P<body>.*)\Z", re.DOTALL)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<target>[^)]+)\)")
TAG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_CONCEPT_FIELDS = ("title", "description", "type", "tags", "timestamp")


@dataclass(frozen=True)
class OkfDocument:
    """Parsed OKF Markdown document."""

    source: Path
    destination: Path
    metadata: dict[str, Any]
    body: str


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    """Parse the YAML-like front matter used by repository OKF files."""
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if match is None:
        msg = f"{path}: missing YAML front matter"
        raise ValueError(msg)
    return parse_simple_yaml(match.group("meta"), path), match.group("body")


def parse_simple_yaml(text: str, path: Path) -> dict[str, Any]:
    """Parse the small YAML subset used by OKF metadata."""
    result: dict[str, Any] = {}
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith(" ") or ":" not in line:
            msg = f"{path}: invalid front matter line: {line}"
            raise ValueError(msg)
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if value:
            result[key] = value
            index += 1
            continue
        index += 1
        items: list[str] = []
        mapping: dict[str, str] = {}
        while index < len(lines) and lines[index].startswith("  "):
            child = lines[index][2:]
            if child.startswith("- "):
                items.append(child[2:].strip())
            elif ":" in child:
                child_key, child_value = child.split(":", 1)
                mapping[child_key.strip()] = child_value.strip()
            else:
                msg = f"{path}: invalid nested front matter line: {lines[index]}"
                raise ValueError(msg)
            index += 1
        result[key] = items or mapping
    return result


def dump_simple_yaml(metadata: dict[str, Any]) -> str:
    """Serialize metadata deterministically for Hugo front matter."""
    lines: list[str] = []
    for key in sorted(metadata):
        value = metadata[key]
        if isinstance(value, dict):
            lines.append(f"{key}:")
            for child_key in sorted(value):
                lines.append(f"  {child_key}: {value[child_key]}")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines) + "\n"


def destination_for(source: Path, src_root: Path, dst_root: Path) -> Path:
    """Return the Hugo destination path for an OKF Markdown source path."""
    relative = source.relative_to(src_root)
    if relative.name == "index.md":
        relative = relative.with_name("_index.md")
    return dst_root / relative


def iter_markdown(root: Path) -> list[Path]:
    """List Markdown files below a root in stable order."""
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def load_documents(src_root: Path, dst_root: Path) -> list[OkfDocument]:
    """Load OKF documents from source root."""
    documents: list[OkfDocument] = []
    for source in iter_markdown(src_root):
        metadata, body = parse_front_matter(source)
        documents.append(
            OkfDocument(
                source=source,
                destination=destination_for(source, src_root, dst_root),
                metadata=metadata,
                body=body,
            )
        )
    return documents


def hugo_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    """Map OKF metadata to Hugo-safe metadata."""
    converted = dict(metadata)
    okf_type = converted.pop("type", None)
    params = dict(converted.pop("params", {}))
    if okf_type is not None:
        params["okf_type"] = okf_type
    converted["params"] = params
    converted["type"] = "knowledge"
    return converted


def render_document(document: OkfDocument) -> str:
    """Render a Hugo Markdown document from an OKF document."""
    return (
        f"---\n{dump_simple_yaml(hugo_metadata(document.metadata))}---\n{document.body}"
    )


def write_documents(documents: list[OkfDocument], dst_root: Path, clean: bool) -> None:
    """Write generated Hugo content to disk."""
    if clean and dst_root.exists():
        shutil.rmtree(dst_root)
    for document in documents:
        document.destination.parent.mkdir(parents=True, exist_ok=True)
        document.destination.write_text(render_document(document), encoding="utf-8")


def validate_documents(
    documents: list[OkfDocument], src_root: Path, dst_root: Path
) -> list[str]:
    """Validate OKF metadata, links, and generated-content drift."""
    errors: list[str] = []
    sources = {document.source.resolve() for document in documents}
    for document in documents:
        errors.extend(validate_metadata(document))
        errors.extend(validate_links(document, sources))
        expected = render_document(document)
        if not document.destination.exists():
            errors.append(f"{document.destination}: generated file is missing")
        elif document.destination.read_text(encoding="utf-8") != expected:
            errors.append(f"{document.destination}: generated file is out of date")
    if not (src_root / "index.md").exists():
        errors.append(f"{src_root / 'index.md'}: required OKF index is missing")
    if not (src_root / "logs" / "log.md").exists():
        errors.append(f"{src_root / 'logs' / 'log.md'}: required OKF log is missing")
    for generated in iter_markdown(dst_root) if dst_root.exists() else []:
        if generated not in {document.destination for document in documents}:
            errors.append(f"{generated}: stale generated file")
    return errors


def validate_metadata(document: OkfDocument) -> list[str]:
    """Validate required OKF metadata fields."""
    errors: list[str] = []
    for field in REQUIRED_CONCEPT_FIELDS:
        if document.source.match("*/concepts/*.md") and field not in document.metadata:
            errors.append(f"{document.source}: missing required field '{field}'")
    tags = document.metadata.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append(f"{document.source}: tags must be a non-empty list")
    else:
        for tag in tags:
            if not TAG.fullmatch(str(tag)):
                errors.append(f"{document.source}: invalid tag '{tag}'")
    return errors


def validate_links(document: OkfDocument, sources: set[Path]) -> list[str]:
    """Validate resolvable relative Markdown links inside OKF bodies."""
    errors: list[str] = []
    for match in LINK.finditer(document.body):
        target = match.group("target").split("#", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "/")):
            continue
        resolved = (document.source.parent / target).resolve()
        if resolved not in sources:
            errors.append(f"{document.source}: broken link '{match.group('target')}'")
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=Path, default=Path("okf"))
    parser.add_argument("--dst", type=Path, default=Path("content/knowledge"))
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--clean", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the OKF-to-Hugo adapter."""
    args = parse_args(sys.argv[1:] if argv is None else argv)
    documents = load_documents(args.src, args.dst)
    if args.check:
        errors = validate_documents(documents, args.src, args.dst)
        for error in errors:
            print(error, file=sys.stderr)
        return 1 if errors else 0
    write_documents(documents, args.dst, args.clean)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
