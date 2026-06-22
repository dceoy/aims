"""Smoke tests — verify each backward-compatible script entrypoint is runnable."""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import types

import pytest

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_SRC_PATH = str(_PROJECT_ROOT / "src")
_ENV = {**os.environ, "PYTHONPATH": _SRC_PATH}
_UV = shutil.which("uv")

_SCRIPTS = [
    ".agents/skills/market-analysis/scripts/market_analysis.py",
    ".agents/skills/market-analysis/scripts/generate_report.py",
    ".agents/skills/market-analysis/scripts/generate_history.py",
    ".agents/skills/market-analysis/scripts/backtest.py",
    ".agents/skills/market-analysis/scripts/validate_analysis.py",
    ".agents/skills/market-analysis/scripts/validate_history.py",
    ".agents/skills/market-analysis/scripts/notify_slack.py",
    ".agents/skills/market-analysis/scripts/validate_instrument_mappings.py",
    ".agents/skills/update-cfd-instruments/scripts/update_cfd_instruments.py",
    ".agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py",
]

_SCRIPT_SYMBOLS = [
    (
        ".agents/skills/market-analysis/scripts/market_analysis.py",
        ["OhlcvBar", "StooqProvider", "generate_artifact", "score_instruments"],
    ),
    (
        ".agents/skills/market-analysis/scripts/generate_report.py",
        ["generate_report", "report_filename"],
    ),
    (
        ".agents/skills/market-analysis/scripts/generate_history.py",
        ["build_history"],
    ),
    (
        ".agents/skills/market-analysis/scripts/backtest.py",
        ["run_backtest"],
    ),
    (
        ".agents/skills/market-analysis/scripts/notify_slack.py",
        ["build_success_payload"],
    ),
    (
        ".agents/skills/market-analysis/scripts/validate_analysis.py",
        ["validate_artifact"],
    ),
    (
        ".agents/skills/market-analysis/scripts/validate_history.py",
        ["validate"],
    ),
    (
        ".agents/skills/market-analysis/scripts/validate_instrument_mappings.py",
        ["validate_mappings"],
    ),
    (
        ".agents/skills/update-cfd-instruments/scripts/update_cfd_instruments.py",
        ["build_rows"],
    ),
    (
        ".agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py",
        ["validate_csv"],
    ),
]


def _import_script(rel_path: str) -> types.ModuleType:
    path = _PROJECT_ROOT / rel_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.mark.parametrize("script", _SCRIPTS, ids=lambda s: Path(s).name)
def test_script_help_exits_zero(script: str) -> None:
    result = subprocess.run(
        [sys.executable, str(_PROJECT_ROOT / script), "--help"],
        capture_output=True,
        text=True,
        env=_ENV,
        check=False,
    )
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()


@pytest.mark.parametrize(
    ("script", "symbols"),
    _SCRIPT_SYMBOLS,
    ids=[Path(s).name for s, _ in _SCRIPT_SYMBOLS],
)
def test_script_re_exports_public_api(script: str, symbols: list[str]) -> None:
    mod = _import_script(script)
    for symbol in symbols:
        assert hasattr(mod, symbol), f"missing re-export: {symbol}"
    assert set(symbols) <= set(mod.__all__)


@pytest.mark.skipif(_UV is None, reason="uv not in PATH")
@pytest.mark.parametrize("script", _SCRIPTS, ids=lambda s: Path(s).name)
def test_script_help_via_uv_run_exits_zero(script: str) -> None:
    assert _UV is not None
    result = subprocess.run(
        [_UV, "run", "python", str(_PROJECT_ROOT / script), "--help"],
        capture_output=True,
        text=True,
        cwd=str(_PROJECT_ROOT),
        check=False,
    )
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()
