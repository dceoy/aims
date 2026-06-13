from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from types import ModuleType

    from pytest_mock import MockerFixture

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "market-analysis"
    / "scripts"
    / "validate_analysis.py"
)


@pytest.fixture(scope="module")
def va() -> ModuleType:
    spec = importlib.util.spec_from_file_location("validate_analysis", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load validate_analysis.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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
        "scoring_version": "1.0.0",
        "config": {"stale_days": 5},
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
