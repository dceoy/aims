"""Smoke tests — verify each backward-compatible script entrypoint is runnable."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_SRC_PATH = str(_PROJECT_ROOT / "src")
_ENV = {**os.environ, "PYTHONPATH": _SRC_PATH}

_SCRIPTS = [
    ".agents/skills/market-analysis/scripts/market_analysis.py",
    ".agents/skills/market-analysis/scripts/generate_report.py",
    ".agents/skills/market-analysis/scripts/generate_history.py",
    ".agents/skills/market-analysis/scripts/validate_analysis.py",
    ".agents/skills/market-analysis/scripts/validate_history.py",
    ".agents/skills/market-analysis/scripts/notify_slack.py",
    ".agents/skills/market-analysis/scripts/validate_instrument_mappings.py",
    ".agents/skills/update-cfd-instruments/scripts/update_cfd_instruments.py",
    ".agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py",
]


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
