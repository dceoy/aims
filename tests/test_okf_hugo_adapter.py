import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import pytest
import yaml

import aims.okf_hugo as okf_hugo_adapter


def write_concept(path: Path, body: str = "# Concept\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        "id: okf/concepts/concept\n"
        "title: Concept\n"
        "description: Test concept\n"
        "type: concept\n"
        "tags: [sales]\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "status: seeded\n"
        "url: /unsafe\n"
        "slug: unsafe-slug\n"
        "layout: unsafe-layout\n"
        "draft: true\n"
        "weight: 99\n"
        "unknown_key:\n"
        "  nested: preserved\n"
        "---\n"
        f"{body}",
        encoding="utf-8",
    )


def generated_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    front_matter = text.split("---\n", 2)[1]
    metadata = yaml.safe_load(front_matter)
    assert isinstance(metadata, dict)
    return metadata


def test_adapter_accepts_reserved_files_without_frontmatter(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text(
        "# Knowledge\n\n- [Concept](/concepts/concept.md)\n", encoding="utf-8"
    )
    logs = src / "logs"
    logs.mkdir()
    (logs / "log.md").write_text(
        "# Log\n\n## 2026-06-16\n\n- Created.\n", encoding="utf-8"
    )
    write_concept(src / "concepts" / "concept.md")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    metadata = generated_metadata(dst / "_index.md")
    text = (dst / "_index.md").read_text(encoding="utf-8")
    assert metadata["type"] == "knowledge"
    assert metadata["params"]["okf_reserved"] == "index"
    assert "# Knowledge" in text
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_hugo_metadata_isolates_unknown_and_sensitive_okf_fields(
    tmp_path: Path,
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text(
        '---\nokf_version: "0.1"\n---\n# Knowledge\n', encoding="utf-8"
    )
    write_concept(src / "concepts" / "concept.md")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    metadata = generated_metadata(dst / "concepts" / "concept.md")
    assert metadata["type"] == "knowledge"
    assert metadata["params"]["okf_type"] == "concept"
    assert metadata["tags"] == ["sales"]
    assert metadata["timestamp"] == "2026-06-16T00:00:00Z"
    for key in ["id", "status", "url", "slug", "layout", "draft", "weight"]:
        assert key not in metadata
        assert key in metadata["params"]["okf_extra"]
    assert metadata["params"]["okf_extra"]["unknown_key"] == {"nested": "preserved"}
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_check_labels_okf_and_aims_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    concepts = src / "concepts"
    concepts.mkdir(parents=True)
    (src / "index.md").write_text(
        "---\ntitle: Not allowed\n---\n# Knowledge\n", encoding="utf-8"
    )
    (concepts / "broken.md").write_text(
        "---\n"
        "title: Broken\n"
        "description: Broken concept\n"
        "type: ''\n"
        "tags: [bad_tag]\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "---\n"
        "[Missing](./missing.md)\n",
        encoding="utf-8",
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    captured = capsys.readouterr().err
    assert "OKF conformance error:" in captured
    assert "AIMS policy error:" in captured


def test_bundle_absolute_links_are_validated(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(src / "concepts" / "foo.md", "# Foo\n[Foo](/concepts/foo.md)\n")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0

    write_concept(
        src / "concepts" / "foo.md", "# Foo\n[Broken](/concepts/missing.md)\n"
    )
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert "broken link '/concepts/missing.md'" in capsys.readouterr().err


def test_internal_links_rewrite_to_hugo_urls(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    (src / "areas").mkdir()
    (src / "areas" / "index.md").write_text("# Area Index\n", encoding="utf-8")
    write_concept(src / "concepts" / "bar.md", "# Bar\n")
    write_concept(
        src / "concepts" / "foo.md",
        "# Foo\n[Bar](./bar.md)\n[Area](/areas/index.md)\n",
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    generated = (dst / "concepts" / "foo.md").read_text(encoding="utf-8")
    assert "[Bar](../bar/)" in generated
    assert "[Area](../../areas/)" in generated
    assert "./bar.md" not in generated
    assert "/knowledge/" not in generated


def test_knowledge_index_links_are_relative(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text(
        "# Knowledge\n\n- [Concept](/concepts/concept.md)\n", encoding="utf-8"
    )
    write_concept(src / "concepts" / "concept.md")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    generated = (dst / "_index.md").read_text(encoding="utf-8")
    assert "[Concept](concepts/concept/)" in generated
    assert "/knowledge/" not in generated


def test_okf_yaml_loader_does_not_mutate_safe_loader() -> None:
    parsed = yaml.safe_load("value: 2026-06-16T00:00:00Z")
    assert isinstance(parsed, dict)
    assert isinstance(parsed["value"], datetime)


def test_internal_links_preserve_label_when_it_matches_target(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(src / "concepts" / "bar.md", "# Bar\n")
    write_concept(
        src / "concepts" / "foo.md",
        "# Foo\n[./bar.md](./bar.md)\n",
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    generated = (dst / "concepts" / "foo.md").read_text(encoding="utf-8")
    assert "[./bar.md](../bar/)" in generated


def test_check_detects_generated_drift(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(src / "concepts" / "concept.md")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0
    first = (dst / "concepts" / "concept.md").read_text(encoding="utf-8")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0

    (dst / "concepts" / "concept.md").write_text(f"{first}\n", encoding="utf-8")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert (
        okf_hugo_adapter.render_document(
            okf_hugo_adapter.load_documents(src, dst)[0][0], src, dst
        )
        == first
    )


def test_parent_directory_links_rewrite_to_hugo_urls(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    logs = src / "logs"
    logs.mkdir()
    (logs / "log.md").write_text("# Log\n", encoding="utf-8")
    write_concept(
        src / "concepts" / "foo.md",
        "# Foo\n[Index](../index.md)\n[Log](../logs/log.md)\n",
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    generated = (dst / "concepts" / "foo.md").read_text(encoding="utf-8")
    assert "[Index](../../)" in generated
    assert "[Log](../../logs/log/)" in generated
    assert "../index.md" not in generated
    assert "../logs/log.md" not in generated
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_check_rejects_internal_links_that_escape_okf_bundle(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside\n", encoding="utf-8")
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(src / "concepts" / "foo.md", "# Foo\n[Outside](../../outside.md)\n")

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    captured = capsys.readouterr().err
    assert "unsafe internal link '../../outside.md' escapes OKF bundle" in captured


def test_okf_hugo_adapter_tool_help_exits_successfully() -> None:
    result = subprocess.run(
        [sys.executable, "tools/okf_hugo_adapter.py", "--help"],
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0


def test_split_front_matter_null_yaml_yields_empty_metadata(tmp_path: Path) -> None:
    f = tmp_path / "null.md"
    f.write_text("---\n\n---\nbody text\n", encoding="utf-8")
    metadata, body, has_fm = okf_hugo_adapter.split_front_matter(f)
    assert metadata == {}
    assert "body text" in body
    assert has_fm is True


def test_split_front_matter_non_dict_raises(tmp_path: Path) -> None:
    f = tmp_path / "list.md"
    f.write_text("---\n- item1\n- item2\n---\nbody\n", encoding="utf-8")
    with pytest.raises(TypeError, match="front matter must be a YAML mapping"):
        okf_hugo_adapter.split_front_matter(f)


def test_load_documents_captures_yaml_error(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    src.mkdir()
    (src / "bad.md").write_text("---\n{invalid:\n---\nbody\n", encoding="utf-8")
    docs, errors = okf_hugo_adapter.load_documents(src, tmp_path / "dst")
    assert docs == []
    assert any("YAML front matter does not parse" in e for e in errors)


def test_load_documents_captures_type_error(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    src.mkdir()
    (src / "bad.md").write_text("---\n- item\n---\nbody\n", encoding="utf-8")
    docs, errors = okf_hugo_adapter.load_documents(src, tmp_path / "dst")
    assert docs == []
    assert any("front matter must be a YAML mapping" in e for e in errors)


def test_split_link_target_with_anchor() -> None:
    path_part, suffix = okf_hugo_adapter.split_link_target("./bar.md#section")
    assert path_part == "./bar.md"
    assert suffix == "#section"


def test_hugo_body_preserves_pending_links(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    write_concept(src / "concepts" / "foo.md", "# Foo\n[Pending](./bar.md#pending)\n")
    docs, _ = okf_hugo_adapter.load_documents(src, dst)
    body = okf_hugo_adapter.hugo_body(docs[0], src, dst)
    assert "./bar.md#pending" in body


def test_write_documents_clean_removes_dst(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(src / "concepts" / "c.md")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0
    stale = dst / "stale.md"
    stale.write_text("stale", encoding="utf-8")
    assert stale.exists()
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--clean"]) == 0
    assert not stale.exists()


def test_validate_documents_reports_missing_bundle_index(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    write_concept(src / "concepts" / "c.md")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert "bundle index is missing" in capsys.readouterr().err


def test_validate_concept_without_front_matter(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    (src / "concepts").mkdir()
    (src / "concepts" / "c.md").write_text("# No front matter\n", encoding="utf-8")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert "concept requires YAML front matter" in capsys.readouterr().err


def test_validate_reserved_log_with_front_matter(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    logs = src / "logs"
    logs.mkdir()
    (logs / "log.md").write_text("---\ntitle: Bad\n---\n# Log\n", encoding="utf-8")
    write_concept(src / "concepts" / "c.md")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert (
        "reserved log.md must not have concept front matter" in capsys.readouterr().err
    )


def test_validate_aims_policy_empty_tags(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    (src / "concepts").mkdir()
    (src / "concepts" / "c.md").write_text(
        "---\n"
        "title: C\n"
        "description: Desc\n"
        "type: concept\n"
        "tags: []\n"
        "timestamp: 2026-01-01T00:00:00Z\n"
        "---\n"
        "# C\n",
        encoding="utf-8",
    )
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
    assert "tags should be a non-empty list" in capsys.readouterr().err


def test_validate_links_skips_external_and_mailto(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "index.md").write_text("# Knowledge\n", encoding="utf-8")
    write_concept(
        src / "concepts" / "c.md",
        "# C\n[Ext](https://example.com)\n[Mail](mailto:foo@bar.com)\n",
    )
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_main_parse_errors_in_write_mode(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "dst"
    src.mkdir()
    (src / "bad.md").write_text("---\n{invalid:\n---\nbody\n", encoding="utf-8")
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 1
    assert "YAML front matter does not parse" in capsys.readouterr().err
