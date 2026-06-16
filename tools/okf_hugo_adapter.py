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

import yaml


class OkfYamlLoader(yaml.SafeLoader):
    """YAML loader that leaves OKF scalar values such as timestamps as strings."""


for first_character, resolvers in list(OkfYamlLoader.yaml_implicit_resolvers.items()):
    OkfYamlLoader.yaml_implicit_resolvers[first_character] = [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


FRONT_MATTER = re.compile(r"\A---\n(?P<meta>.*?)\n---\n(?P<body>.*)\Z", re.DOTALL)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<target>[^)]+)\)")
TAG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RECOMMENDED_CONCEPT_FIELDS = ("title", "description", "tags", "timestamp")
ROOT_INDEX_ALLOWED_FIELDS = {"okf_version"}
RESERVED_NAMES = {"index.md", "log.md"}
HUGO_TOP_LEVEL_KEYS = {"title", "description", "tags", "resource", "timestamp"}


@dataclass(frozen=True)
class OkfDocument:
    """Parsed OKF Markdown document."""

    source: Path
    destination: Path
    metadata: dict[str, Any]
    body: str
    reserved: bool
    has_front_matter: bool


def split_front_matter(path: Path) -> tuple[dict[str, Any], str, bool]:
    """Split optional YAML front matter from an OKF Markdown file."""
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if match is None:
        return {}, text, False
    metadata = yaml.load(match.group("meta"), Loader=OkfYamlLoader)
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        msg = f"OKF conformance error: {path}: front matter must be a YAML mapping"
        raise TypeError(msg)
    return metadata, match.group("body"), True


def dump_yaml(metadata: dict[str, Any]) -> str:
    """Serialize metadata deterministically for Hugo front matter."""
    return yaml.safe_dump(
        metadata,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    )


def destination_for(source: Path, src_root: Path, dst_root: Path) -> Path:
    """Return the Hugo destination path for an OKF Markdown source path."""
    relative = source.relative_to(src_root)
    if relative.name == "index.md":
        relative = relative.with_name("_index.md")
    return dst_root / relative


def iter_markdown(root: Path) -> list[Path]:
    """List Markdown files below a root in stable order."""
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def is_reserved(path: Path) -> bool:
    """Return whether an OKF Markdown path is reserved by OKF v0.1."""
    return path.name in RESERVED_NAMES


def load_documents(
    src_root: Path, dst_root: Path
) -> tuple[list[OkfDocument], list[str]]:
    """Load OKF documents from source root and capture parse errors."""
    documents: list[OkfDocument] = []
    errors: list[str] = []
    for source in iter_markdown(src_root):
        try:
            metadata, body, has_front_matter = split_front_matter(source)
        except yaml.YAMLError as exc:
            errors.append(
                "OKF conformance error: "
                f"{source}: YAML front matter does not parse: {exc}"
            )
            continue
        except (TypeError, ValueError) as exc:
            errors.append(str(exc))
            continue
        documents.append(
            OkfDocument(
                source=source,
                destination=destination_for(source, src_root, dst_root),
                metadata=metadata,
                body=body,
                reserved=is_reserved(source),
                has_front_matter=has_front_matter,
            )
        )
    return documents, errors


def heading_title(body: str, fallback: str) -> str:
    """Extract a title from the first Markdown H1 or use a fallback."""
    for line in body.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return fallback


def hugo_metadata(document: OkfDocument, src_root: Path) -> dict[str, Any]:
    """Map OKF metadata to Hugo-safe metadata."""
    converted = {
        key: value
        for key, value in document.metadata.items()
        if key in HUGO_TOP_LEVEL_KEYS
    }
    extra = {
        key: value
        for key, value in document.metadata.items()
        if key not in HUGO_TOP_LEVEL_KEYS and key != "type"
    }
    params: dict[str, Any] = {}
    okf_type = document.metadata.get("type")
    if okf_type is not None:
        params["okf_type"] = okf_type
    if extra:
        params["okf_extra"] = extra
    if document.reserved:
        params["okf_reserved"] = document.source.name.removesuffix(".md")
    converted["params"] = params
    converted["type"] = "knowledge"
    converted.setdefault(
        "title", heading_title(document.body, document.source.stem.title())
    )
    converted.setdefault(
        "description", f"Generated from {document.source.relative_to(src_root)}."
    )
    converted.setdefault(
        "resource", {"path": str(document.source.relative_to(src_root))}
    )
    return converted


def hugo_url_for_okf_path(path: Path, src_root: Path) -> str:
    """Return the Hugo knowledge URL for an OKF Markdown source path."""
    relative = path.resolve().relative_to(src_root.resolve())
    if relative.name == "index.md":
        section = relative.parent.as_posix()
        return "/knowledge/" if section == "." else f"/knowledge/{section}/"
    page = relative.with_suffix("").as_posix()
    return f"/knowledge/{page}/"


def split_link_target(target: str) -> tuple[str, str]:
    """Split a Markdown link target into path and suffix components."""
    separators = [
        index for index in (target.find("?"), target.find("#")) if index != -1
    ]
    if not separators:
        return target, ""
    split_at = min(separators)
    return target[:split_at], target[split_at:]


def hugo_body(document: OkfDocument, src_root: Path) -> str:
    """Rewrite OKF internal Markdown links for Hugo knowledge URLs."""

    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        target_path, suffix = split_link_target(target)
        if (
            not target_path
            or "://" in target_path
            or target_path.startswith("mailto:")
            or pending_link(target)
        ):
            return match.group(0)
        if target_path.startswith("/"):
            okf_path = src_root / target_path.removeprefix("/")
        else:
            okf_path = document.source.parent / target_path
        if okf_path.suffix != ".md":
            return match.group(0)
        rewritten = f"{hugo_url_for_okf_path(okf_path, src_root)}{suffix}"
        return match.group(0).replace(target, rewritten)

    return LINK.sub(replace, document.body)


def render_document(document: OkfDocument, src_root: Path) -> str:
    """Render a Hugo Markdown document from an OKF document."""
    front_matter = dump_yaml(hugo_metadata(document, src_root))
    return f"---\n{front_matter}---\n{hugo_body(document, src_root)}"


def write_documents(
    documents: list[OkfDocument], src_root: Path, dst_root: Path, clean: bool
) -> None:
    """Write generated Hugo content to disk."""
    if clean and dst_root.exists():
        shutil.rmtree(dst_root)
    for document in documents:
        document.destination.parent.mkdir(parents=True, exist_ok=True)
        document.destination.write_text(
            render_document(document, src_root), encoding="utf-8"
        )


def validate_documents(
    documents: list[OkfDocument],
    parse_errors: list[str],
    src_root: Path,
    dst_root: Path,
) -> list[str]:
    """Validate OKF conformance and AIMS repository policy."""
    errors = list(parse_errors)
    sources = {document.source.resolve() for document in documents}
    for document in documents:
        errors.extend(validate_reserved_or_concept(document, src_root))
        errors.extend(validate_aims_policy(document, sources, src_root))
        expected = render_document(document, src_root)
        if not document.destination.exists():
            errors.append(
                f"AIMS policy error: {document.destination}: generated file is missing"
            )
        elif document.destination.read_text(encoding="utf-8") != expected:
            errors.append(
                "AIMS policy error: "
                f"{document.destination}: generated file is out of date"
            )
    if not (src_root / "index.md").exists():
        errors.append(
            f"OKF conformance error: {src_root / 'index.md'}: bundle index is missing"
        )
    for generated in iter_markdown(dst_root) if dst_root.exists() else []:
        if generated not in {document.destination for document in documents}:
            errors.append(f"AIMS policy error: {generated}: stale generated file")
    return errors


def validate_reserved_or_concept(document: OkfDocument, src_root: Path) -> list[str]:
    """Validate OKF v0.1 reserved-file and concept-document rules."""
    errors: list[str] = []
    if document.reserved:
        errors.extend(validate_reserved(document, src_root))
        return errors
    if not document.has_front_matter:
        errors.append(
            "OKF conformance error: "
            f"{document.source}: concept requires YAML front matter"
        )
    elif not str(document.metadata.get("type", "")).strip():
        errors.append(
            "OKF conformance error: "
            f"{document.source}: concept requires non-empty 'type'"
        )
    return errors


def validate_reserved(document: OkfDocument, src_root: Path) -> list[str]:
    """Validate OKF v0.1 reserved Markdown files."""
    errors: list[str] = []
    if document.source.name == "log.md" and document.has_front_matter:
        errors.append(
            "OKF conformance error: "
            f"{document.source}: reserved log.md must not have concept front matter"
        )
    if document.source.name != "index.md" or not document.has_front_matter:
        return errors
    allowed_fields = (
        ROOT_INDEX_ALLOWED_FIELDS if document.source == src_root / "index.md" else set()
    )
    unknown = sorted(set(document.metadata) - allowed_fields)
    if unknown:
        errors.append(
            "OKF conformance error: "
            f"{document.source}: reserved index.md allows only "
            f"{sorted(allowed_fields)} front matter fields; found {unknown}"
        )
    return errors


def validate_aims_policy(
    document: OkfDocument, sources: set[Path], src_root: Path
) -> list[str]:
    """Validate AIMS metadata, tag, and link policies."""
    errors: list[str] = []
    if not document.reserved:
        for field in RECOMMENDED_CONCEPT_FIELDS:
            if field not in document.metadata:
                errors.append(
                    "AIMS policy error: "
                    f"{document.source}: recommended field '{field}' is missing"
                )
        tags = document.metadata.get("tags")
        if not isinstance(tags, list) or not tags:
            errors.append(
                f"AIMS policy error: {document.source}: tags should be a non-empty list"
            )
        else:
            for tag in tags:
                if not TAG.fullmatch(str(tag)):
                    errors.append(
                        f"AIMS policy error: {document.source}: invalid tag '{tag}'"
                    )
    errors.extend(validate_links(document, sources, src_root))
    return errors


def pending_link(target: str) -> bool:
    """Return whether a link explicitly declares itself pending."""
    return "pending=true" in target or target.endswith("#pending")


def validate_links(
    document: OkfDocument, sources: set[Path], src_root: Path
) -> list[str]:
    """Validate resolvable relative and bundle-absolute Markdown links."""
    errors: list[str] = []
    for match in LINK.finditer(document.body):
        target = match.group("target")
        clean_target = target.split("?", 1)[0].split("#", 1)[0]
        if (
            not clean_target
            or "://" in clean_target
            or clean_target.startswith("mailto:")
            or pending_link(target)
        ):
            continue
        resolved = (
            src_root / clean_target.removeprefix("/")
            if clean_target.startswith("/")
            else document.source.parent / clean_target
        ).resolve()
        if resolved not in sources:
            errors.append(
                f"AIMS policy error: {document.source}: broken link '{target}'"
            )
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
    documents, parse_errors = load_documents(args.src, args.dst)
    if args.check:
        errors = validate_documents(documents, parse_errors, args.src, args.dst)
        for error in errors:
            print(error, file=sys.stderr)
        return 1 if errors else 0
    if parse_errors:
        for error in parse_errors:
            print(error, file=sys.stderr)
        return 1
    write_documents(documents, args.src, args.dst, args.clean)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
