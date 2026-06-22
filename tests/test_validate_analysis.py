from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from types import ModuleType

    from pytest_mock import MockerFixture

import aims.validate_analysis as _aims_va


@pytest.fixture(scope="module")
def va() -> ModuleType:
    return _aims_va


VALID_INSTRUMENT: dict[str, Any] = {
    "symbol": "AAPL.US",
    "rank": 1,
    "score": 75.0,
    "is_reliable": True,
    "risk_gates": [],
    "explanation": "Strong momentum.",
    "features": {"ret_1d": 0.01},
}

VALID_ARTIFACT: dict[str, Any] = {
    "version": "1.0.0",
    "metadata": {
        "generated_at": "2024-01-01T00:00:00+00:00",
        "git_commit": "abc1234",
        "data_source": "stooq",
        "data_freshness": {"AAPL.US": "2024-01-01"},
        "scoring_version": "1.0.0",
        "config": {
            "interval": "d",
            "stale_days": 5,
            "max_gap_days": 7,
            "min_history": 60,
            "coverage_policy": {
                "min_success_ratio": 0.8,
                "max_missing_symbols": 1,
            },
        },
        "coverage": {
            "attempted_count": 1,
            "fetched_count": 1,
            "missing_symbols": [],
            "success_ratio": 1.0,
            "passed": True,
            "violations": [],
        },
    },
    "instruments": [VALID_INSTRUMENT],
}


def write_artifact(tmp_path: Path, artifact: dict[str, Any]) -> Path:
    path = tmp_path / "test.json"
    path.write_text(json.dumps(artifact))
    return path


# ── validate_artifact ──────────────────────────────────────────────────────────


def test_validate_valid(va: ModuleType) -> None:
    errors = va.validate_artifact(dict(VALID_ARTIFACT))
    assert errors == []


def test_validate_missing_version(va: ModuleType) -> None:
    data = {k: v for k, v in VALID_ARTIFACT.items() if k != "version"}
    errors = va.validate_artifact(data)
    assert any("version" in e for e in errors)


def test_validate_missing_metadata(va: ModuleType) -> None:
    data = {k: v for k, v in VALID_ARTIFACT.items() if k != "metadata"}
    errors = va.validate_artifact(data)
    assert any("metadata" in e for e in errors)


def test_validate_missing_instruments(va: ModuleType) -> None:
    data = {k: v for k, v in VALID_ARTIFACT.items() if k != "instruments"}
    errors = va.validate_artifact(data)
    assert any("instruments" in e for e in errors)


def test_validate_multiple_missing_top_keys(va: ModuleType) -> None:
    errors = va.validate_artifact({})
    assert len([e for e in errors if "missing required key" in e]) == 3


def test_validate_wrong_version(va: ModuleType) -> None:
    data = {**VALID_ARTIFACT, "version": "2.0.0"}
    errors = va.validate_artifact(data)
    assert any("unsupported version" in e for e in errors)


def test_validate_metadata_not_dict(va: ModuleType) -> None:
    data = {**VALID_ARTIFACT, "metadata": "bad"}
    errors = va.validate_artifact(data)
    assert any("metadata" in e and "object" in e for e in errors)


def test_validate_metadata_missing_key(va: ModuleType) -> None:
    bad_meta = {
        k: v for k, v in VALID_ARTIFACT["metadata"].items() if k != "git_commit"
    }
    data = {**VALID_ARTIFACT, "metadata": bad_meta}
    errors = va.validate_artifact(data)
    assert any("git_commit" in e for e in errors)


def test_validate_instruments_not_list(va: ModuleType) -> None:
    data = {**VALID_ARTIFACT, "instruments": {"a": 1}}
    errors = va.validate_artifact(data)
    assert any("array" in e for e in errors)


def test_validate_instrument_not_dict(va: ModuleType) -> None:
    data = {**VALID_ARTIFACT, "instruments": ["not_a_dict"]}
    errors = va.validate_artifact(data)
    assert any("object" in e for e in errors)


def test_validate_instrument_missing_key(va: ModuleType) -> None:
    bad_inst = {k: v for k, v in VALID_INSTRUMENT.items() if k != "symbol"}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("symbol" in e for e in errors)


def test_validate_score_not_numeric(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "score": "high"}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("score" in e and "number" in e for e in errors)


def test_validate_score_out_of_range(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "score": 150.0}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("score" in e and "outside" in e for e in errors)


def test_validate_score_zero_valid(va: ModuleType) -> None:
    inst = {**VALID_INSTRUMENT, "score": 0.0}
    data = {**VALID_ARTIFACT, "instruments": [inst]}
    errors = va.validate_artifact(data)
    score_errors = [e for e in errors if "score" in e]
    assert score_errors == []


def test_validate_rank_not_integer(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "rank": "first"}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("rank" in e and "integer" in e for e in errors)


def test_validate_rank_boolean_rejected(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "rank": True}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("rank" in e and "integer" in e for e in errors)


def test_validate_rank_zero(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "rank": 0}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("rank" in e and ">= 1" in e for e in errors)


def test_validate_rank_negative(va: ModuleType) -> None:
    bad_inst = {**VALID_INSTRUMENT, "rank": -1}
    data = {**VALID_ARTIFACT, "instruments": [bad_inst]}
    errors = va.validate_artifact(data)
    assert any("rank" in e and ">= 1" in e for e in errors)


def test_validate_multiple_instruments(va: ModuleType) -> None:
    inst2 = {**VALID_INSTRUMENT, "symbol": "MSFT.US", "rank": 2}
    data = {**VALID_ARTIFACT, "instruments": [VALID_INSTRUMENT, inst2]}
    errors = va.validate_artifact(data)
    assert errors == []


def test_validate_empty_instruments_list(va: ModuleType) -> None:
    data = {**VALID_ARTIFACT, "instruments": []}
    errors = va.validate_artifact(data)
    assert errors == []


# ── data_freshness validation ──────────────────────────────────────────────────


def test_validate_coverage_passed_false_allowed(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {
            **VALID_ARTIFACT["metadata"],
            "coverage": {
                **VALID_ARTIFACT["metadata"]["coverage"],
                "passed": False,
                "violations": ["success ratio (50.00% < 80%)"],
            },
        },
    }
    errors = va.validate_artifact(data)
    assert not any("coverage.passed is false" in e for e in errors)


def test_validate_config_missing_key(va: ModuleType) -> None:
    bad_config = {
        k: v
        for k, v in VALID_ARTIFACT["metadata"]["config"].items()
        if k != "max_gap_days"
    }
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "config": bad_config},
    }
    errors = va.validate_artifact(data)
    assert any("max_gap_days" in e for e in errors)


def test_validate_config_not_dict(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "config": "bad"},
    }
    errors = va.validate_artifact(data)
    assert any("metadata.config must be a JSON object" in e for e in errors)


def test_validate_coverage_policy_not_dict(va: ModuleType) -> None:
    bad_config = {
        **VALID_ARTIFACT["metadata"]["config"],
        "coverage_policy": "bad",
    }
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "config": bad_config},
    }
    errors = va.validate_artifact(data)
    assert any("coverage_policy must be a JSON object" in e for e in errors)


def test_validate_coverage_not_dict(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "coverage": "bad"},
    }
    errors = va.validate_artifact(data)
    assert any("metadata.coverage must be a JSON object" in e for e in errors)


def test_validate_coverage_missing_key(va: ModuleType) -> None:
    bad_coverage = {
        k: v
        for k, v in VALID_ARTIFACT["metadata"]["coverage"].items()
        if k != "violations"
    }
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "coverage": bad_coverage},
    }
    errors = va.validate_artifact(data)
    assert any("violations" in e for e in errors)


def test_validate_coverage_passed_not_boolean(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {
            **VALID_ARTIFACT["metadata"],
            "coverage": {
                **VALID_ARTIFACT["metadata"]["coverage"],
                "passed": "yes",
            },
        },
    }
    errors = va.validate_artifact(data)
    assert any("coverage.passed must be a boolean" in e for e in errors)


def test_validate_config_null_rejected(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "config": None},
    }
    errors = va.validate_artifact(data)
    assert any("metadata.config must not be null" in e for e in errors)


def test_validate_coverage_null_rejected(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "coverage": None},
    }
    errors = va.validate_artifact(data)
    assert any("metadata.coverage must not be null" in e for e in errors)


def test_validate_data_freshness_valid(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {
            **VALID_ARTIFACT["metadata"],
            "data_freshness": {"X": "2024-01-01"},
        },
    }
    errors = va.validate_artifact(data)
    assert not any("freshness" in e for e in errors)


def test_validate_data_freshness_sentinel_valid(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "data_freshness": {"X": "n/a"}},
    }
    errors = va.validate_artifact(data)
    assert not any("freshness" in e for e in errors)


def test_validate_data_freshness_missing(va: ModuleType) -> None:
    bad_meta = {
        k: v for k, v in VALID_ARTIFACT["metadata"].items() if k != "data_freshness"
    }
    data = {**VALID_ARTIFACT, "metadata": bad_meta}
    errors = va.validate_artifact(data)
    assert any("data_freshness" in e for e in errors)


def test_validate_data_freshness_not_dict(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "data_freshness": "2024-01-01"},
    }
    errors = va.validate_artifact(data)
    assert any("data_freshness" in e and "object" in e for e in errors)


def test_validate_data_freshness_invalid_value(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {
            **VALID_ARTIFACT["metadata"],
            "data_freshness": {"X": "not-a-date"},
        },
    }
    errors = va.validate_artifact(data)
    assert any("data_freshness" in e for e in errors)


def test_validate_data_freshness_non_string_value(va: ModuleType) -> None:
    data = {
        **VALID_ARTIFACT,
        "metadata": {**VALID_ARTIFACT["metadata"], "data_freshness": {"X": 20240101}},
    }
    errors = va.validate_artifact(data)
    assert any("data_freshness" in e for e in errors)


# ── parse_args ─────────────────────────────────────────────────────────────────


def test_parse_args_custom(va: ModuleType, mocker: MockerFixture) -> None:
    mocker.patch.object(
        sys,
        "argv",
        ["validate_analysis.py", "--input", "data/analysis/2024-01-01.json"],
    )
    args = va.parse_args()
    assert args.input == Path("data/analysis/2024-01-01.json")


# ── main ───────────────────────────────────────────────────────────────────────


def test_main_valid(
    va: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = write_artifact(tmp_path, VALID_ARTIFACT)
    mocker.patch.object(sys, "argv", ["validate_analysis.py", "--input", str(path)])
    va.main()
    assert "OK" in capsys.readouterr().out


def test_main_invalid_artifact(
    va: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    bad = {**VALID_ARTIFACT, "version": "9.9.9"}
    path = write_artifact(tmp_path, bad)
    mocker.patch.object(sys, "argv", ["validate_analysis.py", "--input", str(path)])
    with pytest.raises(SystemExit) as exc:
        va.main()
    assert exc.value.code == 1
    assert capsys.readouterr().out.strip()


def test_main_file_not_found(
    va: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    missing = tmp_path / "no_such_file.json"
    mocker.patch.object(sys, "argv", ["validate_analysis.py", "--input", str(missing)])
    with pytest.raises(SystemExit) as exc:
        va.main()
    assert exc.value.code == 1
    assert "not found" in capsys.readouterr().out


def test_main_bad_json(
    va: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("not valid json {{{")
    mocker.patch.object(sys, "argv", ["validate_analysis.py", "--input", str(path)])
    with pytest.raises(SystemExit) as exc:
        va.main()
    assert exc.value.code == 1
    assert "JSON" in capsys.readouterr().out
