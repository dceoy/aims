from pathlib import Path

from tools import okf_hugo_adapter


def test_adapter_generates_hugo_metadata_and_index(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    dst = tmp_path / "content" / "knowledge"
    src.mkdir()
    (src / "index.md").write_text(
        "---\n"
        "title: Knowledge\n"
        "description: Test index\n"
        "type: index\n"
        "tags:\n"
        "  - okf\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "---\n"
        "# Knowledge\n"
    )

    logs = src / "logs"
    logs.mkdir()
    (logs / "log.md").write_text(
        "---\n"
        "title: Log\n"
        "description: Test log\n"
        "type: log\n"
        "tags:\n"
        "  - okf\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "---\n"
        "# Log\n"
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst)]) == 0

    generated = dst / "_index.md"
    text = generated.read_text()
    assert "type: knowledge" in text
    assert "  okf_type: index" in text
    assert "# Knowledge" in text
    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 0


def test_check_reports_broken_links_and_drift(tmp_path: Path) -> None:
    src = tmp_path / "okf"
    concepts = src / "concepts"
    dst = tmp_path / "content" / "knowledge"
    concepts.mkdir(parents=True)
    (src / "index.md").write_text(
        "---\n"
        "title: Knowledge\n"
        "description: Test index\n"
        "type: index\n"
        "tags:\n"
        "  - okf\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "---\n"
        "# Knowledge\n"
    )
    (concepts / "broken.md").write_text(
        "---\n"
        "title: Broken\n"
        "description: Broken concept\n"
        "type: concept\n"
        "tags:\n"
        "  - bad-tag\n"
        "timestamp: 2026-06-16T00:00:00Z\n"
        "---\n"
        "[Missing](./missing.md)\n"
    )

    assert okf_hugo_adapter.main(["--src", str(src), "--dst", str(dst), "--check"]) == 1
