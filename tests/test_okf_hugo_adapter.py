from pathlib import Path

import pytest

from tools import okf_hugo_adapter


def write_concept(path: Path, body: str = "# Concept\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        "title: Concept\n"
        "description: Test concept\n"
        "type: concept\n"
        "tags: [sales]\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "unknown_key:\n"
        "  nested: preserved\n"
        "---\n"
        f"{body}",
        encoding="utf-8",
    )


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

    generated = dst / "_index.md"
    text = generated.read_text(encoding="utf-8")
    assert "type: knowledge" in text
    assert "okf_reserved: index" in text
    assert "# Knowledge" in text
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_adapter_accepts_root_index_with_okf_version_and_preserves_unknown_fields(
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

    generated = (dst / "concepts" / "concept.md").read_text(encoding="utf-8")
    assert "  okf_type: concept" in generated
    assert "unknown_key:" in generated
    assert "  nested: preserved" in generated
    assert "tags:" in generated
    assert "- sales" in generated
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
