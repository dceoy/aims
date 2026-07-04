"""Tests for aims.evidence — deterministic evidence-bundle generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

from aims import evidence as ev
from aims.market_analysis import InstrumentMappingRow

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

RSS_XML = """﻿<?xml version="1.0" encoding="utf-8" ?>
<rss version="2.0">
  <channel>
    <item>
      <title><![CDATA[Fed holds <b>rates</b> steady &amp; signals patience]]></title>
      <link><![CDATA[https://example.org/fed-holds]]></link>
      <description><![CDATA[The committee kept rates unchanged]]></description>
      <pubDate><![CDATA[Sun, 31 Dec 2023 15:00:00 GMT]]></pubDate>
    </item>
    <item>
      <link>https://example.org/no-title</link>
      <pubDate>Sun, 31 Dec 2023 12:00:00 GMT</pubDate>
    </item>
    <item>
      <title>Ancient item outside the lookback</title>
      <link>https://example.org/old</link>
      <pubDate>Fri, 01 Dec 2023 12:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>"""

ATOM_XML = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>ECB publishes statement</title>
    <link href="https://example.eu/ecb-statement"/>
    <published>2023-12-30T10:00:00Z</published>
    <summary>Statement text.</summary>
  </entry>
  <entry>
    <title>Updated-only entry</title>
    <link href="https://example.eu/updated-only"/>
    <updated>2023-12-30T11:00:00Z</updated>
  </entry>
  <entry>
    <title>Entry without link</title>
    <published>2023-12-30T12:00:00Z</published>
  </entry>
</feed>"""


def _row(**overrides: str) -> InstrumentMappingRow:
    values = {
        "canonical_id": "spx",
        "display_name": "S&P 500",
        "asset_class": "equity_index",
        "broker": "",
        "broker_instrument_name": "",
        "broker_ticker_symbol": "",
        "provider": "yfinance",
        "provider_symbol": "^GSPC",
        "provider_interval": "d",
        "tradable": "true",
    }
    values.update(overrides)
    return InstrumentMappingRow(**values)


def _news_raw(
    url: str, title: str = "Story", pub: str = "2023-12-31T08:00:00Z"
) -> dict[str, Any]:
    return {
        "content": {
            "title": title,
            "summary": "A summary.",
            "pubDate": pub,
            "canonicalUrl": {"url": url},
            "provider": {"displayName": "Newswire"},
        }
    }


# ── git_commit ──────────────────────────────────────────────────────────────


def test_git_commit_success(mocker: MockerFixture) -> None:
    mocker.patch.object(
        ev.subprocess,
        "run",
        return_value=mocker.Mock(returncode=0, stdout="abc1234\n"),
    )
    assert ev.git_commit() == "abc1234"


def test_git_commit_nonzero(mocker: MockerFixture) -> None:
    mocker.patch.object(
        ev.subprocess, "run", return_value=mocker.Mock(returncode=1, stdout="")
    )
    assert ev.git_commit() == "unknown"


def test_git_commit_oserror(mocker: MockerFixture) -> None:
    mocker.patch.object(ev.subprocess, "run", side_effect=OSError("no git"))
    assert ev.git_commit() == "unknown"


# ── sources and instruments ─────────────────────────────────────────────────


def test_load_evidence_sources(tmp_path: Path) -> None:
    csv_path = tmp_path / "sources.csv"
    csv_path.write_text(
        "source_id,name,url,category,asset_classes\n"
        "zed,Zed,https://z.example,central_bank,equity_index|equity\n"
        "abc,Abc,https://a.example,energy,\n",
        encoding="utf-8",
    )
    sources = ev.load_evidence_sources(csv_path)
    assert [s.source_id for s in sources] == ["abc", "zed"]
    assert sources[0].asset_classes == ()
    assert sources[1].asset_classes == ("equity_index", "equity")


def test_load_committed_evidence_sources() -> None:
    sources = ev.load_evidence_sources(Path("data/mappings/evidence_sources.csv"))
    assert sources
    assert all(s.url.startswith("https://") for s in sources)


def test_instruments_from_mappings_dedup_and_filter() -> None:
    rows = [
        _row(),
        _row(provider_interval="w"),
        _row(provider="stooq", provider_symbol="^SPX"),
        _row(),  # duplicate canonical_id ignored
        _row(canonical_id="aapl", provider_symbol="AAPL", asset_class="equity"),
    ]
    instruments = ev.instruments_from_mappings(rows, "yfinance", "d")
    assert [(i.canonical_id, i.symbol) for i in instruments] == [
        ("aapl", "AAPL"),
        ("spx", "^GSPC"),
    ]


# ── text and timestamp helpers ──────────────────────────────────────────────


def test_clean_text_strips_markup_and_caps() -> None:
    text = ev.clean_text("<p>Hello&amp;  <b>world</b></p>", 8)
    assert text == "Hello& w"


def test_evidence_id_is_stable() -> None:
    first = ev.evidence_id("https://x", "2024-01-01T00:00:00+00:00")
    assert first == ev.evidence_id("https://x", "2024-01-01T00:00:00+00:00")
    assert first.startswith("ev-")
    assert len(first) == 19


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Sun, 31 Dec 2023 15:00:00 GMT", "2023-12-31T15:00:00+00:00"),
        ("2023-12-30T10:00:00Z", "2023-12-30T10:00:00+00:00"),
        ("2023-12-30T10:00:00+09:00", "2023-12-30T01:00:00+00:00"),
        ("2023-12-30T10:00:00", "2023-12-30T10:00:00+00:00"),
        ("not a date", None),
        ("", None),
    ],
)
def test_parse_timestamp(value: str, expected: str | None) -> None:
    assert ev.parse_timestamp(value) == expected


# ── network boundaries ──────────────────────────────────────────────────────


def test_fetch_url_decodes_charset(mocker: MockerFixture) -> None:
    response = mocker.MagicMock()
    response.headers.get_content_charset.return_value = "iso-8859-1"
    response.read.return_value = "caf\xe9".encode("iso-8859-1")
    response.__enter__.return_value = response
    mocker.patch.object(ev.urllib.request, "urlopen", return_value=response)
    assert ev.fetch_url("https://example.org/feed") == "café"


def test_fetch_url_defaults_to_utf8(mocker: MockerFixture) -> None:
    response = mocker.MagicMock()
    response.headers.get_content_charset.return_value = None
    response.read.return_value = b"plain"
    response.__enter__.return_value = response
    mocker.patch.object(ev.urllib.request, "urlopen", return_value=response)
    assert ev.fetch_url("https://example.org/feed") == "plain"


def test_fetch_symbol_news_delegates_to_yfinance(mocker: MockerFixture) -> None:
    ticker = mocker.Mock()
    ticker.get_news.return_value = [{"id": "x"}]
    mocker.patch.object(ev.yf, "Ticker", return_value=ticker)
    assert ev.fetch_symbol_news("AAPL") == [{"id": "x"}]
    ticker.get_news.assert_called_once_with(count=ev._NEWS_FETCH_COUNT)


# ── feed and news parsing ───────────────────────────────────────────────────


def test_parse_feed_rss() -> None:
    entries = ev.parse_feed(RSS_XML)
    assert entries[0]["title"].startswith("Fed holds")
    assert entries[0]["url"] == "https://example.org/fed-holds"
    assert entries[1]["title"] == ""
    assert len(entries) == 3


def test_parse_feed_atom() -> None:
    entries = ev.parse_feed(ATOM_XML)
    assert entries[0]["url"] == "https://example.eu/ecb-statement"
    assert entries[0]["published"] == "2023-12-30T10:00:00Z"
    assert entries[1]["published"] == "2023-12-30T11:00:00Z"
    assert entries[2]["url"] == ""


def test_normalize_news_item_content_shape() -> None:
    entry = ev.normalize_news_item(_news_raw("https://n.example/a"))
    assert entry is not None
    assert entry["url"] == "https://n.example/a"
    assert entry["source"] == "Newswire"


def test_normalize_news_item_flat_shape_with_fallbacks() -> None:
    entry = ev.normalize_news_item({
        "title": "Flat",
        "link": "https://n.example/flat",
        "displayTime": "2023-12-31T08:00:00Z",
        "description": "Old-style summary",
    })
    assert entry is not None
    assert entry["url"] == "https://n.example/flat"
    assert entry["summary"] == "Old-style summary"
    assert entry["source"] == "yahoo-finance"


def test_normalize_news_item_click_through_url() -> None:
    raw = {
        "content": {
            "title": "T",
            "pubDate": "2023-12-31T08:00:00Z",
            "clickThroughUrl": {"url": "https://n.example/ct"},
        }
    }
    entry = ev.normalize_news_item(raw)
    assert entry is not None
    assert entry["url"] == "https://n.example/ct"


def test_normalize_news_item_missing_url_or_title() -> None:
    assert ev.normalize_news_item({"content": {"title": "T"}}) is None
    assert (
        ev.normalize_news_item({"content": {"canonicalUrl": {"url": "https://x"}}})
        is None
    )


# ── bundle assembly ─────────────────────────────────────────────────────────


def _instruments() -> list[ev.EvidenceInstrument]:
    return [
        ev.EvidenceInstrument("aapl", "AAPL", "equity"),
        ev.EvidenceInstrument("msft", "MSFT", "equity"),
        ev.EvidenceInstrument("spx", "^GSPC", "equity_index"),
    ]


def _sources() -> list[ev.EvidenceSource]:
    return [
        ev.EvidenceSource(
            "fed", "Fed", "https://fed.example/feed", "central_bank", ("equity",)
        ),
        ev.EvidenceSource(
            "dead", "Dead feed", "https://dead.example/feed", "energy", ()
        ),
    ]


def _build(fetch_news: Any, fetch_url: Any) -> dict[str, Any]:
    return ev.build_bundle(
        _instruments(),
        _sources(),
        analysis_date="2024-01-01",
        retrieved_at="2024-01-01T05:00:00+00:00",
        fetch_url_fn=fetch_url,
        fetch_news_fn=fetch_news,
    )


def test_build_bundle_end_to_end() -> None:
    shared_url = "https://n.example/shared"

    def fetch_news(symbol: str) -> list[dict[str, Any]]:
        if symbol == "AAPL":
            return [
                _news_raw(shared_url, "Shared story"),
                _news_raw("https://n.example/aapl-only", "AAPL story"),
                _news_raw("https://n.example/old", "Too old", "2023-12-01T00:00:00Z"),
                {"content": {"title": "No URL"}},
            ]
        if symbol == "MSFT":
            return [_news_raw(shared_url, "Shared story")]
        msg = "boom"
        raise ConnectionError(msg)

    def fetch_url(url: str) -> str:
        if url == "https://fed.example/feed":
            return RSS_XML
        msg = "dead feed"
        raise TimeoutError(msg)

    bundle = _build(fetch_news, fetch_url)
    coverage = bundle["metadata"]["coverage"]

    assert coverage["sources"]["yfinance:AAPL"] == {
        "status": "success",
        "item_count": 2,
    }
    assert coverage["sources"]["yfinance:^GSPC"]["status"] == "failed"
    assert coverage["sources"]["feed:fed"] == {
        "status": "success",
        "item_count": 1,
    }
    assert coverage["sources"]["feed:dead"]["status"] == "failed"
    assert coverage["instrument_count"] == 3
    assert coverage["instruments_with_direct_news"] == ["aapl", "msft"]
    assert coverage["asset_classes"] == {
        "equity": {"instruments": 2, "with_direct_news": 2},
        "equity_index": {"instruments": 1, "with_direct_news": 0},
    }

    items = bundle["items"]
    shared = [i for i in items if i["url"] == shared_url]
    assert len(shared) == 1
    assert shared[0]["canonical_ids"] == ["aapl", "msft"]
    macro = [i for i in items if i["category"] == "macro"]
    assert len(macro) == 1
    assert macro[0]["title"] == "Fed holds rates steady & signals patience"
    assert all("<" not in i["title"] for i in items)
    assert bundle["metadata"]["retrieved_at"] == "2024-01-01T05:00:00+00:00"


def test_build_bundle_instrument_with_no_evidence_in_window() -> None:
    def fetch_news(symbol: str) -> list[dict[str, Any]]:
        return [
            _news_raw(f"https://n.example/{symbol}", "Too old", "2023-11-01T00:00:00Z")
        ]

    bundle = _build(fetch_news, lambda _url: "<rss/>")
    coverage = bundle["metadata"]["coverage"]
    assert coverage["instruments_with_direct_news"] == []
    assert coverage["sources"]["yfinance:AAPL"] == {
        "status": "success",
        "item_count": 0,
    }


def test_build_bundle_caps_items_per_instrument() -> None:
    def fetch_news(symbol: str) -> list[dict[str, Any]]:
        return [
            _news_raw(f"https://n.example/{symbol}/{i}", f"Story {i}")
            for i in range(ev.MAX_ITEMS_PER_INSTRUMENT + 3)
        ]

    bundle = _build(fetch_news, lambda _url: "<rss/>")
    for inst in ("AAPL", "MSFT", "^GSPC"):
        assert (
            bundle["metadata"]["coverage"]["sources"][f"yfinance:{inst}"]["item_count"]
            == ev.MAX_ITEMS_PER_INSTRUMENT
        )


def test_build_bundle_default_retrieved_at() -> None:
    bundle = ev.build_bundle(
        [],
        [],
        analysis_date="2024-01-01",
        fetch_url_fn=lambda _url: "<rss/>",
        fetch_news_fn=lambda _symbol: [],
    )
    assert bundle["metadata"]["retrieved_at"]
    assert bundle["items"] == []


def test_bundle_stem_interval_suffix() -> None:
    bundle = {"metadata": {"analysis_date": "2024-01-01", "interval": "d"}}
    assert ev.bundle_stem(bundle) == "2024-01-01"
    bundle["metadata"]["interval"] = "w"
    assert ev.bundle_stem(bundle) == "2024-01-01-w"


def test_save_bundle(tmp_path: Path) -> None:
    bundle = {
        "version": ev.EVIDENCE_VERSION,
        "metadata": {"analysis_date": "2024-01-01", "interval": "d"},
        "items": [],
    }
    path = ev.save_bundle(bundle, tmp_path)
    assert path == tmp_path / "2024-01-01.json"
    assert json.loads(path.read_text())["version"] == ev.EVIDENCE_VERSION


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_missing_mapping(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    rc = ev.main([
        "--mapping",
        str(tmp_path / "missing.csv"),
        "--analysis-date",
        "2024-01-01",
    ])
    assert rc == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_no_instruments(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    mapping = tmp_path / "map.csv"
    mapping.write_text(
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,tradable\n",
        encoding="utf-8",
    )
    rc = ev.main([
        "--mapping",
        str(mapping),
        "--analysis-date",
        "2024-01-01",
    ])
    assert rc == 1
    assert "no instruments" in capsys.readouterr().out


def test_main_success_with_failed_source_warning(
    tmp_path: Path,
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    mapping = tmp_path / "map.csv"
    mapping.write_text(
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,tradable\n"
        "spx,S&P 500,equity_index,,,,yfinance,^GSPC,d,true\n",
        encoding="utf-8",
    )
    bundle = {
        "version": ev.EVIDENCE_VERSION,
        "metadata": {
            "analysis_date": "2024-01-01",
            "interval": "d",
            "coverage": {
                "sources": {
                    "yfinance:^GSPC": {"status": "failed", "error": "boom"},
                }
            },
        },
        "items": [],
    }
    mocker.patch.object(ev, "build_bundle", return_value=bundle)
    rc = ev.main([
        "--mapping",
        str(mapping),
        "--sources",
        "data/mappings/evidence_sources.csv",
        "--analysis-date",
        "2024-01-01",
        "--output",
        str(tmp_path / "out"),
    ])
    out = capsys.readouterr().out
    assert rc == 0
    assert "WARNING: fetch failed for source yfinance:^GSPC" in out
    assert (tmp_path / "out" / "2024-01-01.json").exists()
