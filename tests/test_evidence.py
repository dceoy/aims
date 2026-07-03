from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from xml.etree.ElementTree import ParseError  # noqa: S405

import pytest

import aims.evidence as ev

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture

_RETRIEVED = "2024-01-01T09:00:00+00:00"

_RSS_DOC = """<?xml version="1.0"?>
<rss version="2.0"><channel>
<item>
  <title>Fed holds &amp; signals patience</title>
  <link>https://example.gov/press/1</link>
  <pubDate>Mon, 01 Jan 2024 08:00:00 GMT</pubDate>
  <description><![CDATA[<p>The committee held rates.</p>]]></description>
</item>
<item>
  <title>No date item</title>
  <link>https://example.gov/press/2</link>
</item>
</channel></rss>
"""

_ATOM_DOC = """<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
<entry>
  <title>Policy account published</title>
  <link href="https://example.eu/press/9"/>
  <updated>2024-01-01T07:30:00Z</updated>
  <summary>Minutes released.</summary>
</entry>
<entry>
  <title>No link entry</title>
  <published>2024-01-01T07:00:00Z</published>
</entry>
</feed>
"""


def _valid_item(**overrides: Any) -> dict[str, Any]:
    item = {
        "id": "a" * 16,
        "source": "feed:test",
        "category": "macro",
        "title": "Title",
        "url": "https://example.com/a",
        "published_at": "2024-01-01T08:00:00+00:00",
        "retrieved_at": _RETRIEVED,
        "instruments": [],
        "summary": "Summary.",
    }
    item.update(overrides)
    return item


def _valid_bundle(items: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    return {
        "version": "1.0.0",
        "metadata": {
            "generated_at": _RETRIEVED,
            "analysis_date": "2024-01-01",
            "max_age_days": 7,
            "coverage": {"sources": {}, "item_count": 0},
        },
        "items": items if items is not None else [_valid_item()],
    }


# ── load_evidence_sources ───────────────────────────────────────────────────────


def test_load_evidence_sources(tmp_path: Path) -> None:
    path = tmp_path / "sources.csv"
    path.write_text(
        "name,url,category\n"
        "fed,https://example.gov/rss,macro\n"
        ",https://skip.example/rss,macro\n"
        "nourl,,macro\n"
    )
    sources = ev.load_evidence_sources(path)
    assert len(sources) == 1
    assert sources[0].name == "fed"
    assert sources[0].category == "macro"


# ── evidence_id / _plain_text ───────────────────────────────────────────────────


def test_evidence_id_is_stable_16_hex() -> None:
    first = ev.evidence_id("https://a", "2024-01-01T00:00:00+00:00")
    second = ev.evidence_id("https://a", "2024-01-01T00:00:00+00:00")
    assert first == second
    assert len(first) == 16
    assert ev.evidence_id("https://b", "2024-01-01T00:00:00+00:00") != first


def test_plain_text_strips_markup_and_truncates() -> None:
    assert ev._plain_text("<p>a &amp; b</p>", 100) == "a & b"
    assert ev._plain_text("  x   y  ", 100) == "x y"
    assert ev._plain_text("abcdef", 3) == "abc"


# ── _format_timestamp ───────────────────────────────────────────────────────────


def test_format_timestamp_unix() -> None:
    assert ev._format_timestamp(1704096000) == "2024-01-01T08:00:00+00:00"


def test_format_timestamp_unix_overflow() -> None:
    assert ev._format_timestamp(1e30) is None


def test_format_timestamp_bool_rejected() -> None:
    assert ev._format_timestamp(True) is None  # noqa: FBT003


def test_format_timestamp_iso_z() -> None:
    assert ev._format_timestamp("2024-01-01T08:00:00Z") == ("2024-01-01T08:00:00+00:00")


def test_format_timestamp_iso_naive_assumed_utc() -> None:
    assert ev._format_timestamp("2024-01-01T08:00:00") == ("2024-01-01T08:00:00+00:00")


def test_format_timestamp_rfc822() -> None:
    assert ev._format_timestamp("Mon, 01 Jan 2024 08:00:00 GMT") == (
        "2024-01-01T08:00:00+00:00"
    )


def test_format_timestamp_rfc822_naive() -> None:
    assert ev._format_timestamp("Mon, 01 Jan 2024 08:00:00") == (
        "2024-01-01T08:00:00+00:00"
    )


def test_format_timestamp_invalid() -> None:
    assert ev._format_timestamp("not a timestamp !!") is None


def test_format_timestamp_empty_or_none() -> None:
    assert ev._format_timestamp("") is None
    assert ev._format_timestamp(None) is None


# ── normalize_news_item ─────────────────────────────────────────────────────────


def test_normalize_news_item_new_shape() -> None:
    raw = {
        "content": {
            "title": "S&P rallies",
            "summary": "<b>Up big.</b>",
            "pubDate": "2024-01-01T05:00:00Z",
            "canonicalUrl": {"url": "https://news.example/spx"},
        }
    }
    item = ev.normalize_news_item(
        raw, symbol="^SPX", canonical_id="spx", retrieved_at=_RETRIEVED
    )
    assert item is not None
    assert item["source"] == "yfinance:^SPX"
    assert item["category"] == "instrument_news"
    assert item["instruments"] == ["spx"]
    assert item["summary"] == "Up big."
    assert item["url"] == "https://news.example/spx"


def test_normalize_news_item_old_shape() -> None:
    raw = {
        "title": "Dow slips",
        "link": "https://news.example/dji",
        "providerPublishTime": 1704096000,
    }
    item = ev.normalize_news_item(
        raw, symbol="^DJI", canonical_id="dji", retrieved_at=_RETRIEVED
    )
    assert item is not None
    assert item["published_at"] == "2024-01-01T08:00:00+00:00"
    assert item["summary"] == ""


def test_normalize_news_item_missing_fields() -> None:
    assert (
        ev.normalize_news_item(
            {"content": {"title": ""}},
            symbol="X",
            canonical_id="x",
            retrieved_at=_RETRIEVED,
        )
        is None
    )
    assert (
        ev.normalize_news_item(
            {"title": "t", "link": "", "providerPublishTime": 1704096000},
            symbol="X",
            canonical_id="x",
            retrieved_at=_RETRIEVED,
        )
        is None
    )
    assert (
        ev.normalize_news_item(
            {"title": "t", "link": "https://a", "providerPublishTime": None},
            symbol="X",
            canonical_id="x",
            retrieved_at=_RETRIEVED,
        )
        is None
    )
    assert (
        ev.normalize_news_item(
            {"title": None, "link": "https://a", "providerPublishTime": 1},
            symbol="X",
            canonical_id="x",
            retrieved_at=_RETRIEVED,
        )
        is None
    )


# ── parse_feed ──────────────────────────────────────────────────────────────────


def test_parse_feed_rss() -> None:
    items = ev.parse_feed(_RSS_DOC, source_name="fed", retrieved_at=_RETRIEVED)
    assert len(items) == 1
    assert items[0]["title"] == "Fed holds & signals patience"
    assert items[0]["summary"] == "The committee held rates."
    assert items[0]["source"] == "feed:fed"
    assert items[0]["published_at"] == "2024-01-01T08:00:00+00:00"


def test_parse_feed_atom() -> None:
    items = ev.parse_feed(_ATOM_DOC, source_name="ecb", retrieved_at=_RETRIEVED)
    assert len(items) == 1
    assert items[0]["title"] == "Policy account published"
    assert items[0]["url"] == "https://example.eu/press/9"


def test_parse_feed_max_items() -> None:
    items = ev.parse_feed(
        _RSS_DOC, source_name="fed", retrieved_at=_RETRIEVED, max_items=1
    )
    assert len(items) == 1


def test_parse_feed_malformed_xml() -> None:
    with pytest.raises(ParseError):
        ev.parse_feed("<rss><oops", source_name="x", retrieved_at=_RETRIEVED)


# ── build_bundle ────────────────────────────────────────────────────────────────


def test_build_bundle_dedupe_filter_sort() -> None:
    fresh = _valid_item(id="b" * 16, published_at="2024-01-01T08:00:00+00:00")
    duplicate = dict(fresh)
    earlier = _valid_item(id="a" * 16, published_at="2023-12-30T08:00:00+00:00")
    too_old = _valid_item(id="c" * 16, published_at="2023-12-01T08:00:00+00:00")
    future = _valid_item(id="d" * 16, published_at="2024-01-05T08:00:00+00:00")
    bundle = ev.build_bundle(
        [fresh, duplicate, earlier, too_old, future],
        analysis_date="2024-01-01",
        max_age_days=7,
        coverage={"sources": {}},
        generated_at=_RETRIEVED,
    )
    ids = [item["id"] for item in bundle["items"]]
    assert ids == ["a" * 16, "b" * 16]
    assert bundle["metadata"]["coverage"]["item_count"] == 2
    assert bundle["metadata"]["analysis_date"] == "2024-01-01"
    assert not ev.validate_bundle(bundle)


def test_build_bundle_allows_next_day_publication() -> None:
    item = _valid_item(published_at="2024-01-02T01:00:00+00:00")
    bundle = ev.build_bundle(
        [item],
        analysis_date="2024-01-01",
        max_age_days=7,
        coverage={},
        generated_at=_RETRIEVED,
    )
    assert len(bundle["items"]) == 1


# ── fetch_bundle ────────────────────────────────────────────────────────────────


def _mapping_csv(tmp_path: Path) -> Path:
    path = tmp_path / "mappings.csv"
    path.write_text(
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,"
        "tradable,notes\n"
        "spx,S&P 500,equity_index,,,,yfinance,^SPX,d,true,\n"
        "dji,Dow,equity_index,,,,yfinance,^DJI,d,true,\n"
    )
    return path


def _sources_csv(tmp_path: Path) -> Path:
    path = tmp_path / "sources.csv"
    path.write_text("name,url,category\nfed,https://example.gov/rss,macro\n")
    return path


def test_fetch_bundle_success(tmp_path: Path, mocker: MockerFixture) -> None:
    mocker.patch.object(
        ev,
        "_fetch_symbol_news",
        return_value=[
            {
                "title": "Index news",
                "link": "https://news.example/1",
                "providerPublishTime": 1704096000,
            },
            "not a dict",
        ],
    )
    mocker.patch.object(ev, "_http_get", return_value=_RSS_DOC)
    bundle = ev.fetch_bundle(
        mapping_path=_mapping_csv(tmp_path),
        provider="yfinance",
        interval="d",
        sources_path=_sources_csv(tmp_path),
        analysis_date="2024-01-01",
    )
    coverage = bundle["metadata"]["coverage"]["sources"]
    assert coverage["yfinance_news"] == {
        "attempted": 2,
        "fetched": 2,
        "failed": [],
    }
    assert coverage["feeds"] == {"attempted": 1, "fetched": 1, "failed": []}
    # ^DJI and ^SPX news share the same URL/timestamp, so they dedupe to one.
    assert bundle["metadata"]["coverage"]["item_count"] == 2
    assert not ev.validate_bundle(bundle)


def test_fetch_bundle_records_failures(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    mocker.patch.object(ev, "_fetch_symbol_news", side_effect=RuntimeError("boom"))
    mocker.patch.object(ev, "_http_get", side_effect=OSError("down"))
    bundle = ev.fetch_bundle(
        mapping_path=_mapping_csv(tmp_path),
        provider="yfinance",
        interval="d",
        sources_path=_sources_csv(tmp_path),
        analysis_date="2024-01-01",
    )
    coverage = bundle["metadata"]["coverage"]["sources"]
    assert coverage["yfinance_news"]["failed"] == ["^DJI", "^SPX"]
    assert coverage["feeds"]["failed"] == ["fed"]
    assert bundle["items"] == []
    out = capsys.readouterr().out
    assert "news fetch failed" in out
    assert "feed fetch failed" in out


def test_fetch_symbol_news_non_list(mocker: MockerFixture) -> None:
    ticker = mocker.MagicMock()
    ticker.news = None
    mocker.patch.object(ev.yf, "Ticker", return_value=ticker)
    assert ev._fetch_symbol_news("^SPX") == []


def test_fetch_symbol_news_list(mocker: MockerFixture) -> None:
    ticker = mocker.MagicMock()
    ticker.news = [{"title": "x"}]
    mocker.patch.object(ev.yf, "Ticker", return_value=ticker)
    assert ev._fetch_symbol_news("^SPX") == [{"title": "x"}]


def test_http_get(mocker: MockerFixture) -> None:
    response = mocker.MagicMock()
    response.read.return_value = b"<rss/>"
    response.__enter__.return_value = response
    mocker.patch.object(ev.urllib.request, "urlopen", return_value=response)
    assert ev._http_get("https://example.gov/rss") == "<rss/>"


# ── validate_bundle ─────────────────────────────────────────────────────────────


def test_validate_bundle_valid() -> None:
    assert ev.validate_bundle(_valid_bundle()) == []


def test_validate_bundle_missing_top_key() -> None:
    errors = ev.validate_bundle({"version": "1.0.0"})
    assert any("metadata" in e for e in errors)


def test_validate_bundle_wrong_version() -> None:
    bundle = _valid_bundle()
    bundle["version"] = "9.9.9"
    assert any("unsupported version" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_metadata_not_dict() -> None:
    bundle = _valid_bundle()
    bundle["metadata"] = "bad"
    assert any("'metadata'" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_metadata_missing_key() -> None:
    bundle = _valid_bundle()
    del bundle["metadata"]["coverage"]
    assert any("coverage" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_coverage_not_dict() -> None:
    bundle = _valid_bundle()
    bundle["metadata"]["coverage"] = "bad"
    assert any("coverage must be" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_items_not_list() -> None:
    bundle = _valid_bundle()
    bundle["items"] = "bad"
    assert any("'items'" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_item_not_dict() -> None:
    bundle = _valid_bundle(items=["bad"])
    assert any("item[0]" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_item_missing_key() -> None:
    item = _valid_item()
    del item["url"]
    errors = ev.validate_bundle(_valid_bundle(items=[item]))
    assert any("missing required key: 'url'" in e for e in errors)


def test_validate_bundle_non_string_id() -> None:
    item = _valid_item()
    item["id"] = 123
    errors = ev.validate_bundle(_valid_bundle(items=[item]))
    assert not any("hex" in e for e in errors)


def test_validate_bundle_bad_id() -> None:
    bundle = _valid_bundle(items=[_valid_item(id="XYZ")])
    assert any("not 16 hex" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_duplicate_id() -> None:
    bundle = _valid_bundle(items=[_valid_item(), _valid_item()])
    assert any("duplicate id" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_bad_category() -> None:
    bundle = _valid_bundle(items=[_valid_item(category="rumor")])
    assert any("category" in e for e in ev.validate_bundle(bundle))


def test_validate_bundle_bad_instruments() -> None:
    errors = ev.validate_bundle(_valid_bundle(items=[_valid_item(instruments="x")]))
    assert any("instruments" in e for e in errors)
    errors = ev.validate_bundle(_valid_bundle(items=[_valid_item(instruments=[1])]))
    assert any("instruments" in e for e in errors)


def test_validate_bundle_summary_too_long() -> None:
    bundle = _valid_bundle(items=[_valid_item(summary="x" * 501)])
    assert any("summary exceeds" in e for e in ev.validate_bundle(bundle))


# ── main ────────────────────────────────────────────────────────────────────────


def test_main_fetch(tmp_path: Path, mocker: MockerFixture) -> None:
    bundle = _valid_bundle(items=[])
    mocker.patch.object(ev, "fetch_bundle", return_value=bundle)
    output = tmp_path / "evidence"
    result = ev.main([
        "fetch",
        "--mapping",
        str(tmp_path / "m.csv"),
        "--sources",
        str(tmp_path / "s.csv"),
        "--analysis-date",
        "2024-01-01",
        "--output",
        str(output),
    ])
    assert result == 0
    written = json.loads((output / "2024-01-01.json").read_text())
    assert written["version"] == "1.0.0"


def test_main_validate_ok(tmp_path: Path) -> None:
    path = tmp_path / "bundle.json"
    path.write_text(json.dumps(_valid_bundle()))
    assert ev.main(["validate", "--input", str(path)]) == 0


def test_main_validate_errors(tmp_path: Path) -> None:
    path = tmp_path / "bundle.json"
    path.write_text(json.dumps({"version": "1.0.0"}))
    assert ev.main(["validate", "--input", str(path)]) == 1


def test_main_validate_missing_file(tmp_path: Path) -> None:
    assert ev.main(["validate", "--input", str(tmp_path / "nope.json")]) == 1


def test_main_validate_bad_json(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{{{")
    assert ev.main(["validate", "--input", str(path)]) == 1
