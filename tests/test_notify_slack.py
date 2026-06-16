from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import pytest

if TYPE_CHECKING:
    from types import ModuleType


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "market-analysis"
    / "scripts"
    / "notify_slack.py"
)

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "analysis_2024-01-01.json"


@pytest.fixture(scope="module")
def ns() -> ModuleType:
    spec = importlib.util.spec_from_file_location("notify_slack", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load notify_slack.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def fixture_artifact() -> dict[str, Any]:
    with FIXTURE_PATH.open() as fh:
        return json.load(fh)


# ── _market_regime tests ────────────────────────────────────────────────────────


def test_notify_market_regime_bullish(ns: ModuleType) -> None:
    assert ns._market_regime([65.0, 75.0]) == "Bullish"


def test_notify_market_regime_neutral(ns: ModuleType) -> None:
    assert ns._market_regime([50.0]) == "Neutral"


def test_notify_market_regime_bearish(ns: ModuleType) -> None:
    assert ns._market_regime([30.0]) == "Bearish"


def test_notify_market_regime_empty(ns: ModuleType) -> None:
    assert ns._market_regime([]) == "Unavailable"


# Even-length median
def test_notify_market_regime_even_neutral(ns: ModuleType) -> None:
    assert ns._market_regime([30.0, 70.0]) == "Neutral"


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


def test_build_success_payload_regime_in_blocks(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/")
    blocks = payload["blocks"]
    # Find a field containing regime
    fields_text = json.dumps(blocks, ensure_ascii=False)
    assert "Bullish" in fields_text
    assert "^SPX" in fields_text


def test_build_success_payload_stale_warning(
    ns: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    payload = ns.build_success_payload(fixture_artifact, "https://example.com/")
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
    assert "2/3" in fields_text


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
                "features": {},
            }
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
                "features": {},
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

    with (
        patch.dict("os.environ", {"SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"}),
        patch("urllib.request.urlopen", return_value=mock_response),
    ):
        result = ns.main(["--failure"])
    assert result == 0


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
