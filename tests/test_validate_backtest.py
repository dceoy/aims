from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from pathlib import Path
    from types import ModuleType

import aims.validate_backtest as _aims_vb

_FEATURES = (
    "ret_1d",
    "ret_5d",
    "ret_20d",
    "ret_60d",
    "ma20_dist",
    "ma50_dist",
    "vol_20d",
    "mdd_60d",
    "rsi_14",
    "zscore_20d",
)


@pytest.fixture(scope="module")
def vb() -> ModuleType:
    return _aims_vb


def _valid() -> dict[str, Any]:
    return {
        "schema_version": "1.2.0",
        "scoring_version": "1.0.0",
        "config": {
            "symbols": ["A", "B"],
            "interval": "d",
            "forward_horizons": [1],
            "top_k": 1,
            "buckets": 2,
            "min_history": 60,
        },
        "observations": 10,
        "date_range": {"start": "2024-01-01", "end": "2024-01-10"},
        "metrics": {
            "1d": {
                "score_buckets": {
                    "1": {"count": 5, "average_return": 0.01},
                    "2": {"count": 5, "average_return": -0.01},
                },
                "benchmark": {"count": 10, "average_return": 0.0},
                "top_k": {
                    "count": 10,
                    "average_return": 0.01,
                    "net_average_return": 0.008,
                    "hit_rate": 0.9,
                    "excess_return": 0.01,
                    "net_excess_return": 0.008,
                },
            }
        },
        "turnover": 0.0,
        "max_drawdown": 0.0,
        "feature_diagnostics": {
            "features": list(_FEATURES),
            "information_coefficient": {
                "1d": {feat: {"mean": 0.5, "n": 10} for feat in _FEATURES}
            },
            "feature_correlation": {
                feat_a: {
                    feat_b: 1.0 if feat_a == feat_b else 0.2 for feat_b in _FEATURES
                }
                for feat_a in _FEATURES
            },
        },
        "significance": {
            "horizon": 1,
            "mean_net_excess_return": 0.008,
            "confidence": 0.95,
            "confidence_interval": {"low": 0.001, "high": 0.015},
            "block_size": 5,
            "iterations": 1000,
            "seed": 0,
            "n": 10,
        },
        "regime_breakdown": {
            "horizon": 1,
            "regimes": {
                "Bullish": {
                    "count": 6,
                    "top_k_net_average_return": 0.01,
                    "benchmark_average_return": 0.005,
                    "excess_return": 0.005,
                },
                "Bearish": {
                    "count": 4,
                    "top_k_net_average_return": -0.01,
                    "benchmark_average_return": -0.015,
                    "excess_return": 0.005,
                },
            },
        },
    }


def test_validate_valid(vb: ModuleType) -> None:
    assert vb.validate_artifact(_valid()) == []


def test_validate_missing_top_key(vb: ModuleType) -> None:
    artifact = _valid()
    del artifact["turnover"]
    errors = vb.validate_artifact(artifact)
    assert any("turnover" in e for e in errors)


def test_validate_wrong_schema_version(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["schema_version"] = "9.9.9"
    errors = vb.validate_artifact(artifact)
    assert any("unsupported schema_version" in e for e in errors)


def test_validate_config_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["config"] = []
    errors = vb.validate_artifact(artifact)
    assert any("config must be an object" in e for e in errors)


def test_validate_config_missing_key(vb: ModuleType) -> None:
    artifact = _valid()
    del artifact["config"]["top_k"]
    errors = vb.validate_artifact(artifact)
    assert any("config missing required key: 'top_k'" in e for e in errors)


def test_validate_date_range_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["date_range"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("date_range must be an object" in e for e in errors)

    artifact = _valid()
    artifact["date_range"]["start"] = 5
    errors = vb.validate_artifact(artifact)
    assert any("date_range.start must be a string or null" in e for e in errors)

    artifact = _valid()
    artifact["date_range"]["start"] = None
    artifact["date_range"]["end"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_observations_must_be_int(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["observations"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("observations must be an integer" in e for e in errors)


def test_validate_turnover_and_drawdown_type(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["turnover"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("turnover must be a number or null" in e for e in errors)

    artifact = _valid()
    artifact["max_drawdown"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_metrics_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["metrics"] = []
    errors = vb.validate_artifact(artifact)
    assert any("metrics must be an object" in e for e in errors)


def test_validate_metrics_horizon_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["metrics"]["1d"] = []
    errors = vb.validate_artifact(artifact)
    assert any("metrics['1d'] must be an object" in e for e in errors)


def test_validate_score_buckets_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["metrics"]["1d"]["score_buckets"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("score_buckets must be an object" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["score_buckets"]["1"] = []
    errors = vb.validate_artifact(artifact)
    assert any("score_buckets['1'] must be an object" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["score_buckets"]["1"]["count"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("score_buckets['1'].count must be an integer" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["score_buckets"]["1"]["average_return"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any(
        "score_buckets['1'].average_return must be a number or null" in e
        for e in errors
    )


def test_validate_top_k_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["metrics"]["1d"]["top_k"] = []
    errors = vb.validate_artifact(artifact)
    assert any("top_k must be an object" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["top_k"]["count"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("top_k.count must be an integer" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["top_k"]["hit_rate"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("top_k.hit_rate must be a number or null" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["top_k"]["hit_rate"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_feature_diagnostics_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["feature_diagnostics"] = []
    errors = vb.validate_artifact(artifact)
    assert any("feature_diagnostics must be an object" in e for e in errors)


def test_validate_feature_diagnostics_features_must_be_string_list(
    vb: ModuleType,
) -> None:
    artifact = _valid()
    artifact["feature_diagnostics"]["features"] = [1, 2]
    errors = vb.validate_artifact(artifact)
    assert any("features must be an array of strings" in e for e in errors)


def test_validate_information_coefficient_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("information_coefficient must be an object" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"]["1d"] = []
    errors = vb.validate_artifact(artifact)
    assert any("information_coefficient['1d'] must be an object" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"] = []
    errors = vb.validate_artifact(artifact)
    assert any("['ret_1d'] must be an object" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"][
        "mean"
    ] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("mean must be a number or null" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"][
        "mean"
    ] = None
    assert vb.validate_artifact(artifact) == []

    artifact = _valid()
    artifact["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"]["n"] = (
        1.5
    )
    errors = vb.validate_artifact(artifact)
    assert any("n must be an integer" in e for e in errors)


def test_validate_feature_correlation_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["feature_diagnostics"]["feature_correlation"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("feature_correlation must be an object" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["feature_correlation"]["ret_1d"] = []
    errors = vb.validate_artifact(artifact)
    assert any("feature_correlation['ret_1d'] must be an object" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["feature_correlation"]["ret_1d"]["ret_5d"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("must be a number or null" in e for e in errors)

    artifact = _valid()
    artifact["feature_diagnostics"]["feature_correlation"]["ret_1d"]["ret_5d"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_metrics_benchmark_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["metrics"]["1d"]["benchmark"] = []
    errors = vb.validate_artifact(artifact)
    assert any("benchmark must be an object" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["benchmark"]["count"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("benchmark.count must be an integer" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["benchmark"]["average_return"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("benchmark.average_return must be a number or null" in e for e in errors)

    artifact = _valid()
    artifact["metrics"]["1d"]["benchmark"]["average_return"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_top_k_net_and_excess_fields(vb: ModuleType) -> None:
    for field in ("net_average_return", "excess_return", "net_excess_return"):
        artifact = _valid()
        artifact["metrics"]["1d"]["top_k"][field] = "bad"
        errors = vb.validate_artifact(artifact)
        assert any(f"top_k.{field} must be a number or null" in e for e in errors)

        artifact = _valid()
        artifact["metrics"]["1d"]["top_k"][field] = None
        assert vb.validate_artifact(artifact) == []


def test_validate_significance_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["significance"] = []
    errors = vb.validate_artifact(artifact)
    assert any("significance must be an object" in e for e in errors)


def test_validate_significance_integer_fields(vb: ModuleType) -> None:
    for field in ("horizon", "iterations", "block_size", "seed", "n"):
        artifact = _valid()
        artifact["significance"][field] = 1.5
        errors = vb.validate_artifact(artifact)
        assert any(f"significance.{field} must be an integer" in e for e in errors)


def test_validate_significance_mean_and_confidence(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["significance"]["mean_net_excess_return"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any(
        "significance.mean_net_excess_return must be a number or null" in e
        for e in errors
    )

    artifact = _valid()
    artifact["significance"]["mean_net_excess_return"] = None
    assert vb.validate_artifact(artifact) == []

    artifact = _valid()
    artifact["significance"]["confidence"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any("significance.confidence must be a number" in e for e in errors)


def test_validate_significance_confidence_interval_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["significance"]["confidence_interval"] = "bad"
    errors = vb.validate_artifact(artifact)
    assert any(
        "significance.confidence_interval must be an object" in e for e in errors
    )

    artifact = _valid()
    artifact["significance"]["confidence_interval"] = {"low": "bad", "high": 0.01}
    errors = vb.validate_artifact(artifact)
    assert any(
        "significance.confidence_interval.low must be a number" in e for e in errors
    )

    artifact = _valid()
    artifact["significance"]["confidence_interval"] = None
    assert vb.validate_artifact(artifact) == []


def test_validate_regime_breakdown_must_be_object(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["regime_breakdown"] = []
    errors = vb.validate_artifact(artifact)
    assert any("regime_breakdown must be an object" in e for e in errors)


def test_validate_regime_breakdown_horizon(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["regime_breakdown"]["horizon"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("regime_breakdown.horizon must be an integer" in e for e in errors)


def test_validate_regime_breakdown_regimes_shape(vb: ModuleType) -> None:
    artifact = _valid()
    artifact["regime_breakdown"]["regimes"] = []
    errors = vb.validate_artifact(artifact)
    assert any("regime_breakdown.regimes must be an object" in e for e in errors)

    artifact = _valid()
    artifact["regime_breakdown"]["regimes"]["Bullish"] = []
    errors = vb.validate_artifact(artifact)
    assert any("regimes['Bullish'] must be an object" in e for e in errors)

    artifact = _valid()
    artifact["regime_breakdown"]["regimes"]["Bullish"]["count"] = 1.5
    errors = vb.validate_artifact(artifact)
    assert any("regimes['Bullish'].count must be an integer" in e for e in errors)

    for field in (
        "top_k_net_average_return",
        "benchmark_average_return",
        "excess_return",
    ):
        artifact = _valid()
        artifact["regime_breakdown"]["regimes"]["Bullish"][field] = "bad"
        errors = vb.validate_artifact(artifact)
        assert any(
            f"regimes['Bullish'].{field} must be a number or null" in e for e in errors
        )

        artifact = _valid()
        artifact["regime_breakdown"]["regimes"]["Bullish"][field] = None
        assert vb.validate_artifact(artifact) == []


def test_main_valid_file(
    vb: ModuleType, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "backtest.json"
    path.write_text(json.dumps(_valid()), encoding="utf-8")
    assert vb.main(["--input", str(path)]) == 0
    assert "OK" in capsys.readouterr().out


def test_main_invalid_file_exits_nonzero(
    vb: ModuleType, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    artifact = _valid()
    del artifact["turnover"]
    path = tmp_path / "backtest.json"
    path.write_text(json.dumps(artifact), encoding="utf-8")
    assert vb.main(["--input", str(path)]) == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_missing_file(
    vb: ModuleType, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert vb.main(["--input", str(tmp_path / "missing.json")]) == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_invalid_json(
    vb: ModuleType, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    assert vb.main(["--input", str(path)]) == 1
    assert "ERROR" in capsys.readouterr().out
