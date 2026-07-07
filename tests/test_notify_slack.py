from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import pytest

if TYPE_CHECKING:
    from types import ModuleType

import aims.notifications as _aims_ns

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "analysis_2024-01-01.json"


@pytest.fixture(scope="module")
def ns() -> ModuleType:
    return _aims_ns


@pytest.fixture(scope="module")
def fixture_artifact() -> dict[str, Any]:
    with FIXTURE_PATH.open() as fh:
        return json.load(fh)


# ── market_regime integration ───────────────────────────────────────────────────


def test_notify_uses_shared_market_regime(ns: ModuleType) -> None:
    # Regime comes from aims.reports.market_regime (MA20 breadth), so a
    # broadly declining universe is labelled Bearish in the payload.
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "config": {},
        },
        "instruments": [
            {
                "symbol": sym,
                "rank": rank,
                "score": 50.0,
                "is_reliable": True,
                "risk_gates": [],
                "features": {"ma20_dist": -0.02},
            }
            for rank, sym in enumerate(["^SPX", "^NDX", "^DJI"], start=1)
        ],
    }
    payload = ns.build_success_payload(artifact)
    assert "Bearish" in payload["text"]


# ── build_success_payload tests ─────────────────────────────────────────────────


def test_build_success_payload(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/report/")
    assert "text" in payload
    assert "blocks" in payload
    text = payload["text"]
    assert "2024-01-01" in text
    assert "Bullish" in text


def test_build_success_payload_history(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    history = {
        "previous_analysis_date": "2023-12-30",
        "instruments": [
            {
                "symbol": "^SPX",
                "new_top_k": True,
                "consecutive_top_k_reports": 2,
                "risk_gates_added": ["high_volatility"],
                "risk_gates_removed": [],
            },
            {
                "symbol": "^NDX",
                "new_top_k": False,
                "consecutive_top_k_reports": 1,
                "risk_gates_added": [],
                "risk_gates_removed": [],
            },
        ],
    }
    payload = ns.build_success_payload(fixture_artifact, history=history)
    text = json.dumps(payload, ensure_ascii=False)
    assert "new top: ^SPX" in text
    assert "persistent: ^SPX" in text
    assert "risk changes: ^SPX" in text


def test_build_success_payload_regime_in_blocks(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/")
    blocks = payload["blocks"]
    # Find a field containing regime
    fields_text = json.dumps(blocks, ensure_ascii=False)
    assert "Bullish" in fields_text
    assert "^SPX" in fields_text


def test_build_success_payload_stale_warning(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {"^SPX": "2024-01-01", "^NDX": "n/a"},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "^SPX",
                "rank": 1,
                "score": 70.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Good",
                "features": {},
            }
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "^NDX" in fields_text


def test_build_success_payload_coverage_invalid_types(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "data_source": "stooq",
            "data_freshness": {},
            "coverage": {
                "attempted_count": "5",
                "fetched_count": 4,
                "success_ratio": 0.8,
            },
        },
        "instruments": [],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "Coverage:" not in fields_text


def test_build_success_payload_coverage_summary(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "Coverage:" in fields_text
    assert "3/3" in fields_text


def test_build_success_payload_price_consistency_escalated(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    artifact = {
        **fixture_artifact,
        "metadata": {
            **fixture_artifact["metadata"],
            "price_consistency": {
                "results": [
                    {"canonical_id": "spx", "escalated": True},
                    {"canonical_id": "dji", "escalated": False},
                ]
            },
        },
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "Provider divergence:" in fields_text
    assert "spx" in fields_text
    assert "dji" not in fields_text


def test_build_success_payload_price_consistency_no_escalation(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    artifact = {
        **fixture_artifact,
        "metadata": {
            **fixture_artifact["metadata"],
            "price_consistency": {
                "results": [{"canonical_id": "spx", "escalated": False}]
            },
        },
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "Provider divergence:" not in fields_text


def test_build_success_payload_excludes_non_tradable_from_top_signals(
    ns: ModuleType,
) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "data_source": "stooq",
            "data_freshness": {},
            "config": {},
        },
        "instruments": [
            {
                "symbol": "BEST",
                "rank": 1,
                "score": 99.0,
                "is_reliable": True,
                "risk_gates": [],
                "features": {},
                "tradable": False,
            },
            {
                "symbol": "NEXT",
                "rank": 2,
                "score": 50.0,
                "is_reliable": True,
                "risk_gates": [],
                "features": {},
                "tradable": True,
            },
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload["blocks"], ensure_ascii=False)
    assert "NEXT" in fields_text
    assert "BEST" not in fields_text


def test_build_success_payload_no_reliable(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-15T00:00:00+00:00",
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "BAD",
                "rank": 1,
                "score": 20.0,
                "is_reliable": False,
                "risk_gates": ["stale_data"],
                "explanation": "Suppressed",
                "features": {},
            }
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    assert "text" in payload
    assert isinstance(payload["blocks"], list)


def test_build_success_payload_no_stale(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {"AAPL": "2024-01-01"},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "AAPL",
                "rank": 1,
                "score": 70.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Good",
                "features": {"rsi_14": 60.0},
            }
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "No data" not in fields_text


def test_build_success_payload_non_string_generated_at(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": 12345,
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "git_commit": "abc",
        },
        "instruments": [],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    assert "text" in payload
    assert "n/a" in payload["text"]


def test_build_success_payload_bullish_emoji(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/")
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "📈" in fields_text


def test_build_success_payload_neutral_emoji(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "git_commit": "abc",
        },
        "instruments": [
            {
                "symbol": "AAPL",
                "rank": 1,
                "score": 55.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Neutral",
                "features": {"ma20_dist": 0.01},
            },
            {
                "symbol": "MSFT",
                "rank": 2,
                "score": 45.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Neutral",
                "features": {"ma20_dist": -0.01},
            },
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "➡️" in fields_text


def test_build_success_payload_bearish_emoji(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "git_commit": "abc",
        },
        "instruments": [
            {
                "symbol": "BAD",
                "rank": 1,
                "score": 25.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Bearish",
                "features": {"ma20_dist": -0.05},
            }
        ],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "📉" in fields_text


def test_build_success_payload_unavailable_emoji(ns: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "git_commit": "abc",
        },
        "instruments": [],
    }
    payload = ns.build_success_payload(artifact, "https://example.com/")
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "❓" in fields_text


# ── build_failure_payload tests ─────────────────────────────────────────────────


def test_build_failure_payload(ns: ModuleType) -> None:
    payload = ns.build_failure_payload("https://github.com/actions/runs/12345")
    assert "text" in payload
    assert "❌" in payload["text"]
    assert "https://github.com/actions/runs/12345" in json.dumps(
        payload["blocks"], ensure_ascii=False
    )


def test_build_failure_payload_custom_message(ns: ModuleType) -> None:
    payload = ns.build_failure_payload(
        "https://example.com/run", "Custom failure message"
    )
    assert "Custom failure message" in payload["text"]


def test_build_failure_payload_no_run_url_omits_actions_block(
    ns: ModuleType,
) -> None:
    payload = ns.build_failure_payload("")
    assert all(block["type"] != "actions" for block in payload["blocks"])


# ── send_notification tests ─────────────────────────────────────────────────────


def test_send_notification_success(ns: ModuleType) -> None:
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)
    mock_response.status = 200

    with patch("urllib.request.urlopen", return_value=mock_response):
        ns.send_notification("https://hooks.slack.com/test", {"text": "hello"})


def test_send_notification_url_error(ns: ModuleType) -> None:
    with (
        patch("urllib.request.urlopen", side_effect=URLError("connection refused")),
        pytest.raises(URLError),
    ):
        ns.send_notification("https://hooks.slack.com/test", {"text": "hello"})


# ── main() tests ────────────────────────────────────────────────────────────────


def test_main_no_webhook(ns: ModuleType, capsys: pytest.CaptureFixture[str]) -> None:
    env: dict[str, str] = {}
    with patch.dict("os.environ", env, clear=True):
        result = ns.main(["--report-url", "https://example.com/"])
    captured = capsys.readouterr()
    assert result == 0
    assert "SLACK_WEBHOOK_URL" in captured.out


def test_main_success_mode(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    with FIXTURE_PATH.open() as fh:
        data = json.load(fh)
    artifact_path.write_text(json.dumps(data))

    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)

    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        result = ns.main([
            "--artifact",
            str(artifact_path),
            "--report-url",
            "https://example.com/report/",
        ])
    assert result == 0


def test_main_success_with_history(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    history_path = tmp_path / "history.json"
    history_path.write_text(json.dumps({"previous_analysis_date": None}))
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)
    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        assert (
            ns.main(["--artifact", str(artifact_path), "--history", str(history_path)])
            == 0
        )


@pytest.mark.parametrize("content", [None, "{"])
def test_main_invalid_history(
    ns: ModuleType, tmp_path: Path, content: str | None
) -> None:
    artifact_path = tmp_path / "artifact.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    history_path = tmp_path / "history.json"
    if content is not None:
        history_path.write_text(content)
    with patch.dict(
        "os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}
    ):
        assert (
            ns.main(["--artifact", str(artifact_path), "--history", str(history_path)])
            == 1
        )


def test_main_failure_mode(ns: ModuleType) -> None:
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)

    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        result = ns.main([
            "--failure",
            "--run-url",
            "https://github.com/actions/runs/99",
            "--message",
            "Pipeline failed",
        ])
    assert result == 0


def test_main_url_error(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    with FIXTURE_PATH.open() as fh:
        data = json.load(fh)
    artifact_path.write_text(json.dumps(data))

    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", side_effect=URLError("err")),
    ):
        result = ns.main([
            "--artifact",
            str(artifact_path),
            "--report-url",
            "https://example.com/",
        ])
    assert result == 1


def test_main_success_missing_artifact(ns: ModuleType) -> None:
    with patch.dict(
        "os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}
    ):
        result = ns.main(["--report-url", "https://example.com/"])
    assert result == 1


def test_main_success_artifact_not_found(ns: ModuleType, tmp_path: Path) -> None:
    missing = tmp_path / "nonexistent.json"
    with patch.dict(
        "os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}
    ):
        result = ns.main([
            "--artifact",
            str(missing),
            "--report-url",
            "https://example.com/",
        ])
    assert result == 1


def test_main_success_bad_json(ns: ModuleType, tmp_path: Path) -> None:
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("not json {{")
    with patch.dict(
        "os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}
    ):
        result = ns.main([
            "--artifact",
            str(bad_file),
            "--report-url",
            "https://example.com/",
        ])
    assert result == 1


def test_main_failure_mode_no_run_url(ns: ModuleType) -> None:
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)

    captured_payload: dict[str, Any] = {}

    def _capture_urlopen(req: Any, timeout: float) -> MagicMock:  # noqa: ARG001
        captured_payload.update(json.loads(req.data.decode()))
        return mock_response

    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", side_effect=_capture_urlopen),
    ):
        result = ns.main(["--failure"])
    assert result == 0
    assert all(block["type"] != "actions" for block in captured_payload["blocks"])


def test_build_success_payload_with_pr_url(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(
        fixture_artifact, pr_url="https://github.com/dceoy/aims/pull/99"
    )
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "View PR" in fields_text
    assert "Analysis PR created" in payload["text"]
    assert "https://github.com/dceoy/aims/pull/99" in fields_text


def test_build_success_payload_pr_url_overrides_report_url(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(
        fixture_artifact,
        "https://example.com/report/",
        pr_url="https://github.com/dceoy/aims/pull/99",
    )
    fields_text = json.dumps(payload, ensure_ascii=False)
    assert "View PR" in fields_text
    assert "https://github.com/dceoy/aims/pull/99" in fields_text
    assert "https://example.com/report/" not in fields_text


def test_build_success_payload_no_urls_omits_actions_block(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact)
    # no actions block since no url provided
    block_types = [b["type"] for b in payload["blocks"]]
    assert "actions" not in block_types


def test_main_success_with_pr_url(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    with FIXTURE_PATH.open() as fh:
        data = json.load(fh)
    artifact_path.write_text(json.dumps(data))
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)
    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        result = ns.main([
            "--artifact",
            str(artifact_path),
            "--pr-url",
            "https://github.com/dceoy/aims/pull/99",
        ])
    assert result == 0


# ── SAMPLE_PAYLOAD constants ────────────────────────────────────────────────────


def test_sample_payloads(ns: ModuleType) -> None:
    assert isinstance(ns.SAMPLE_SUCCESS_PAYLOAD, dict)
    assert "text" in ns.SAMPLE_SUCCESS_PAYLOAD
    assert isinstance(ns.SAMPLE_FAILURE_PAYLOAD, dict)
    assert "text" in ns.SAMPLE_FAILURE_PAYLOAD


# ── performance / stance hit-rate line (#97) ────────────────────────────────────


def _perf(horizons: dict[str, Any]) -> dict[str, Any]:
    return {"stance_evaluation": {"horizons": horizons}}


def _bucket(count: int, hit_rate: float | None) -> dict[str, Any]:
    return {"count": count, "hit_rate": hit_rate}


def test_performance_summary_reports_blended_hit_rate(ns: ModuleType) -> None:
    performance = _perf({
        "1d": {
            "stances": {
                "supportive": _bucket(2, 1.0),
                "conflicting": _bucket(2, 0.5),
                "neutral": _bucket(1, None),
            }
        },
        "20d": {
            "stances": {
                "supportive": _bucket(0, None),
                "conflicting": _bucket(0, None),
                "neutral": _bucket(0, None),
            }
        },
    })
    assert ns._performance_summary(performance) == "1d 75% (n=4); 20d n/a"


def test_performance_summary_none_when_no_matured_data(ns: ModuleType) -> None:
    performance = _perf({
        "1d": {
            "stances": {
                "supportive": _bucket(0, None),
                "conflicting": _bucket(0, None),
                "neutral": _bucket(0, None),
            }
        }
    })
    assert ns._performance_summary(performance) is None


def test_build_success_payload_adds_hit_rate_field(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    performance = _perf({"1d": {"stances": {"supportive": _bucket(1, 1.0)}}})
    payload = ns.build_success_payload(fixture_artifact, performance=performance)
    texts = [f["text"] for f in payload["blocks"][1]["fields"]]
    assert any("AI stance hit rate:" in t for t in texts)


def test_build_success_payload_omits_hit_rate_when_empty(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    performance = _perf({"1d": {"stances": {"supportive": _bucket(0, None)}}})
    payload = ns.build_success_payload(fixture_artifact, performance=performance)
    texts = [f["text"] for f in payload["blocks"][1]["fields"]]
    assert not any("AI stance hit rate:" in t for t in texts)


def test_main_success_with_performance(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    with FIXTURE_PATH.open() as fh:
        artifact_path.write_text(json.dumps(json.load(fh)))
    perf_path = tmp_path / "performance.json"
    perf_path.write_text(
        json.dumps(_perf({"1d": {"stances": {"supportive": _bucket(1, 1.0)}}}))
    )
    mock_response = MagicMock()
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=False)
    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        result = ns.main([
            "--artifact",
            str(artifact_path),
            "--performance",
            str(perf_path),
        ])
    assert result == 0


def test_main_reports_invalid_performance(ns: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "artifact.json"
    with FIXTURE_PATH.open() as fh:
        artifact_path.write_text(json.dumps(json.load(fh)))
    perf_path = tmp_path / "performance.json"
    perf_path.write_text("{")
    with patch.dict(
        "os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}
    ):
        result = ns.main([
            "--artifact",
            str(artifact_path),
            "--performance",
            str(perf_path),
        ])
    assert result == 1
