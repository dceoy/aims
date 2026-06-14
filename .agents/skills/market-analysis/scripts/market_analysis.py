#!/usr/bin/env python3
r"""Market data fetch, scoring, and analysis artifact generation for AIMS.

This tool is informational only and does not constitute investment advice.

Usage:
    uv run .agents/skills/market-analysis/scripts/market_analysis.py \
        fetch --symbol AAPL.US --start 2024-01-01 --end 2024-12-31
    uv run .agents/skills/market-analysis/scripts/market_analysis.py \
        check --symbol AAPL.US
    uv run .agents/skills/market-analysis/scripts/market_analysis.py \
        score --symbols AAPL.US,MSFT.US
    uv run .agents/skills/market-analysis/scripts/market_analysis.py \
        generate --symbols AAPL.US,MSFT.US --output data/analysis/
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import subprocess
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Final
from urllib.error import URLError
from urllib.request import urlopen

# ── Constants ────────────────────────────────────────────────────────────────

_DEFAULT_PRICES_DIR: Final[Path] = Path("data/prices")
_DEFAULT_ANALYSIS_DIR: Final[Path] = Path("data/analysis")
_DEFAULT_INTERVAL: Final[str] = "d"
_STALE_DAYS: Final[int] = 5
_MIN_HISTORY: Final[int] = 60
_HIGH_VOL_THRESHOLD: Final[float] = 1.0
_MAX_GAP_DAYS: Final[int] = 7

SCORING_VERSION: Final[str] = "1.0.0"
ARTIFACT_VERSION: Final[str] = "1.0.0"

RISK_GATE_STALE: Final[str] = "stale_data"
RISK_GATE_HIGH_VOL: Final[str] = "high_volatility"
RISK_GATE_INSUFFICIENT: Final[str] = "insufficient_history"
RISK_GATE_MISSING_BARS: Final[str] = "missing_bars"
RISK_GATE_MALFORMED: Final[str] = "malformed_input"
RISK_GATE_MISSING_DATA: Final[str] = "missing_data"

_OHLCV_FIELDS: Final[tuple[str, ...]] = (
    "symbol",
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "source",
    "interval",
)

# ── Data model ───────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class OhlcvBar:
    """Single OHLCV candlestick bar with a UTC-aware timestamp."""

    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    source: str
    interval: str


@dataclass
class DataQualityReport:
    """Result of a data-quality assessment for one symbol."""

    symbol: str
    interval: str
    bar_count: int
    issues: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not self.issues


# ── Providers ─────────────────────────────────────────────────────────────────


class MarketDataProvider(ABC):
    """Abstract base class for OHLCV market data providers."""

    @abstractmethod
    def fetch_ohlcv(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = _DEFAULT_INTERVAL,
    ) -> list[OhlcvBar]:
        """Fetch OHLCV bars for *symbol* in [*start*, *end*]."""


class StooqProvider(MarketDataProvider):
    """Provider backed by the Stooq free CSV download API.

    Limitations:
        - Daily / weekly / monthly bars only (no intraday).
        - Symbol format is Stooq-specific: e.g. 'AAPL.US', '^SPX', '7203.JP'.
        - Data coverage varies; some symbols return empty results.
        - No authentication required; subject to Stooq rate limits.
        - Requires outbound network access — not suitable for unit tests.
          Use CsvFileProvider for deterministic testing.
    """

    _BASE_URL: Final[str] = "https://stooq.com/q/d/l/"
    _SOURCE: Final[str] = "stooq"

    def fetch_ohlcv(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = _DEFAULT_INTERVAL,
    ) -> list[OhlcvBar]:
        url = (
            f"{self._BASE_URL}?s={symbol}"
            f"&d1={start.strftime('%Y%m%d')}"
            f"&d2={end.strftime('%Y%m%d')}"
            f"&i={interval}"
        )
        with urlopen(url, timeout=30) as resp:
            content = resp.read().decode("utf-8")
        return self._parse_csv(content, symbol, interval)

    def _parse_csv(self, content: str, symbol: str, interval: str) -> list[OhlcvBar]:
        bars: list[OhlcvBar] = []
        for row in csv.DictReader(io.StringIO(content)):
            date_str = row.get("Date", "")
            if not date_str:
                continue
            try:
                ts = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=UTC)
                bars.append(
                    OhlcvBar(
                        symbol=symbol,
                        timestamp=ts,
                        open=float(row.get("Open") or 0),
                        high=float(row.get("High") or 0),
                        low=float(row.get("Low") or 0),
                        close=float(row.get("Close") or 0),
                        volume=float(row.get("Volume") or 0),
                        source=self._SOURCE,
                        interval=interval,
                    )
                )
            except ValueError:
                pass
        return sorted(bars, key=lambda b: b.timestamp)


class CsvFileProvider(MarketDataProvider):
    """Provider that loads bars from CSV files written by save_ohlcv.

    Suitable for offline workflows and deterministic unit tests.
    """

    def __init__(self, data_dir: Path = _DEFAULT_PRICES_DIR) -> None:
        self._data_dir = data_dir

    def fetch_ohlcv(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = _DEFAULT_INTERVAL,
    ) -> list[OhlcvBar]:
        all_bars = load_ohlcv(symbol, interval, self._data_dir)
        return [b for b in all_bars if start <= b.timestamp <= end]


# ── Save / Load ───────────────────────────────────────────────────────────────


def ohlcv_csv_path(
    symbol: str,
    interval: str,
    data_dir: Path = _DEFAULT_PRICES_DIR,
) -> Path:
    safe = symbol.replace("/", "-").replace("^", "_")
    return data_dir / f"{safe}_{interval}.csv"


def save_ohlcv(
    bars: list[OhlcvBar],
    data_dir: Path = _DEFAULT_PRICES_DIR,
) -> Path:
    if not bars:
        msg = "cannot save an empty bars list"
        raise ValueError(msg)
    path = ohlcv_csv_path(bars[0].symbol, bars[0].interval, data_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(_OHLCV_FIELDS))
        writer.writeheader()
        for b in bars:
            writer.writerow({
                "symbol": b.symbol,
                "timestamp": b.timestamp.isoformat(),
                "open": b.open,
                "high": b.high,
                "low": b.low,
                "close": b.close,
                "volume": b.volume,
                "source": b.source,
                "interval": b.interval,
            })
    return path


def load_ohlcv(
    symbol: str,
    interval: str,
    data_dir: Path = _DEFAULT_PRICES_DIR,
) -> list[OhlcvBar]:
    path = ohlcv_csv_path(symbol, interval, data_dir)
    if not path.exists():
        msg = f"no OHLCV data at {path}"
        raise FileNotFoundError(msg)
    bars: list[OhlcvBar] = []
    with path.open(newline="") as fh:
        for row in csv.DictReader(fh):
            ts = datetime.fromisoformat(row["timestamp"])
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=UTC)
            bars.append(
                OhlcvBar(
                    symbol=row["symbol"],
                    timestamp=ts,
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row["volume"]),
                    source=row["source"],
                    interval=row["interval"],
                )
            )
    return sorted(bars, key=lambda b: b.timestamp)


# ── Data quality ──────────────────────────────────────────────────────────────


def check_data_quality(
    bars: list[OhlcvBar],
    *,
    stale_days: int = _STALE_DAYS,
    min_history: int = _MIN_HISTORY,
    reference_time: datetime | None = None,
) -> DataQualityReport:
    if not bars:
        return DataQualityReport(
            symbol="", interval="", bar_count=0, issues=["empty data"]
        )

    symbol = bars[0].symbol
    interval = bars[0].interval
    report = DataQualityReport(symbol=symbol, interval=interval, bar_count=len(bars))

    now = reference_time if reference_time is not None else datetime.now(tz=UTC)
    age = (now - bars[-1].timestamp).days
    if age > stale_days:
        report.issues.append(
            f"stale data: latest bar is {age} days old (threshold: {stale_days})"
        )

    if len(bars) < min_history:
        report.issues.append(
            f"insufficient history: {len(bars)} bars (minimum: {min_history})"
        )

    for i, bar in enumerate(bars):
        if bar.open <= 0 or bar.high <= 0 or bar.low <= 0 or bar.close <= 0:
            report.issues.append(f"malformed OHLC at index {i}: non-positive price")
            break
        if bar.high < bar.low:
            report.issues.append(f"malformed OHLC at index {i}: high < low")
            break
        if not (bar.low <= bar.open <= bar.high):
            report.issues.append(
                f"malformed OHLC at index {i}: open outside [low, high]"
            )
            break
        if not (bar.low <= bar.close <= bar.high):
            report.issues.append(
                f"malformed OHLC at index {i}: close outside [low, high]"
            )
            break

    timestamps = [b.timestamp for b in bars]
    if len(timestamps) != len(set(timestamps)):
        report.issues.append("duplicate timestamps detected")

    if len(bars) >= 2:
        for i in range(1, len(bars)):
            gap = (bars[i].timestamp - bars[i - 1].timestamp).days
            if gap > _MAX_GAP_DAYS:
                report.issues.append(
                    f"possible missing bars: {gap}-day gap between"
                    f" {bars[i - 1].timestamp.date()} and"
                    f" {bars[i].timestamp.date()}"
                )
                break

    return report


# ── Feature computation ────────────────────────────────────────────────────────


@dataclass
class InstrumentFeatures:
    """Raw features computed from OHLCV bars."""

    ret_1d: float | None
    ret_5d: float | None
    ret_20d: float | None
    ret_60d: float | None
    ma20_dist: float | None
    ma50_dist: float | None
    vol_20d: float | None
    mdd_60d: float | None
    rsi_14: float | None
    zscore_20d: float | None


def _compute_return(closes: list[float], n: int) -> float | None:
    if len(closes) < n + 1:
        return None
    return closes[-1] / closes[-(n + 1)] - 1.0


def _compute_ma_distance(closes: list[float], n: int) -> float | None:
    if len(closes) < n:
        return None
    ma = sum(closes[-n:]) / n
    return (closes[-1] - ma) / ma


def _compute_realized_vol(closes: list[float], n: int) -> float | None:
    if len(closes) < n + 1:
        return None
    rets = [
        closes[i] / closes[i - 1] - 1.0 for i in range(len(closes) - n, len(closes))
    ]
    mean_r = sum(rets) / len(rets)
    var = sum((r - mean_r) ** 2 for r in rets) / len(rets)
    return var**0.5 * 252**0.5


def _compute_max_drawdown(closes: list[float], n: int) -> float | None:
    if not closes:
        return None
    window = closes[-min(n, len(closes)) :]
    peak = window[0]
    mdd = 0.0
    for c in window:
        peak = max(peak, c)
        dd = (peak - c) / peak
        mdd = max(mdd, dd)
    return mdd


def _compute_rsi(closes: list[float], n: int) -> float | None:
    if len(closes) < n + 1:
        return None
    gains = losses = 0.0
    for i in range(len(closes) - n, len(closes)):
        diff = closes[i] - closes[i - 1]
        if diff > 0:
            gains += diff
        else:
            losses -= diff
    avg_loss = losses / n
    if not avg_loss:
        return 100.0
    return 100.0 - 100.0 / (1.0 + gains / n / avg_loss)


def _compute_zscore(closes: list[float], n: int) -> float | None:
    if len(closes) < n:
        return None
    window = closes[-n:]
    mean = sum(window) / n
    std = (sum((c - mean) ** 2 for c in window) / n) ** 0.5
    if not std:
        return 0.0
    return (closes[-1] - mean) / std


def compute_features(bars: list[OhlcvBar]) -> InstrumentFeatures:
    closes = [b.close for b in bars]
    return InstrumentFeatures(
        ret_1d=_compute_return(closes, 1),
        ret_5d=_compute_return(closes, 5),
        ret_20d=_compute_return(closes, 20),
        ret_60d=_compute_return(closes, 60),
        ma20_dist=_compute_ma_distance(closes, 20),
        ma50_dist=_compute_ma_distance(closes, 50),
        vol_20d=_compute_realized_vol(closes, 20),
        mdd_60d=_compute_max_drawdown(closes, 60),
        rsi_14=_compute_rsi(closes, 14),
        zscore_20d=_compute_zscore(closes, 20),
    )


# ── Scoring ────────────────────────────────────────────────────────────────────


@dataclass
class InstrumentScore:
    """Scoring result for one instrument."""

    symbol: str
    rank: int
    score: float
    features: InstrumentFeatures
    risk_gates: list[str]
    is_reliable: bool
    explanation: str


def _percentile_rank(values: list[float | None], idx: int) -> float:
    valid = [v for v in values if v is not None]
    if not valid:
        return 50.0
    v = values[idx]
    if v is None:
        return 50.0
    below = sum(1 for x in valid if x < v)
    return 100.0 * below / len(valid)


def _collect_risk_gates(
    report: DataQualityReport, features: InstrumentFeatures
) -> list[str]:
    gates: list[str] = []
    for issue in report.issues:
        if "stale" in issue:
            gates.append(RISK_GATE_STALE)
        elif "insufficient" in issue:
            gates.append(RISK_GATE_INSUFFICIENT)
        elif "missing" in issue or "gap" in issue:
            gates.append(RISK_GATE_MISSING_BARS)
        else:
            gates.append(RISK_GATE_MALFORMED)
    if features.vol_20d is not None and features.vol_20d > _HIGH_VOL_THRESHOLD:
        gates.append(RISK_GATE_HIGH_VOL)
    return gates


def _build_explanation(
    symbol: str,
    features: InstrumentFeatures,
    risk_gates: list[str],
) -> str:
    if risk_gates:
        return f"Suppressed: {', '.join(risk_gates)}"
    parts: list[str] = []
    if features.ret_20d is not None:
        direction = "up" if features.ret_20d >= 0 else "down"
        parts.append(f"20d {direction} {features.ret_20d:+.1%}")
    if features.ma20_dist is not None:
        side = "above" if features.ma20_dist >= 0 else "below"
        parts.append(f"{side} MA20 by {abs(features.ma20_dist):.1%}")
    if features.rsi_14 is not None:
        parts.append(f"RSI14={features.rsi_14:.0f}")
    if not parts:
        return f"{symbol}: insufficient data for explanation"
    return "; ".join(parts)


def score_instruments(
    data: dict[str, list[OhlcvBar]],
    *,
    reference_time: datetime | None = None,
    stale_days: int = _STALE_DAYS,
    min_history: int = _MIN_HISTORY,
) -> list[InstrumentScore]:
    if not data:
        return []

    symbols = list(data)
    reports = {
        s: check_data_quality(
            data[s],
            stale_days=stale_days,
            min_history=min_history,
            reference_time=reference_time,
        )
        for s in symbols
    }
    features_map = {s: compute_features(data[s]) for s in symbols}
    feature_cols = _build_feature_columns(symbols, features_map)

    scores: list[InstrumentScore] = []
    for idx, symbol in enumerate(symbols):
        feats = features_map[symbol]
        gates = _collect_risk_gates(reports[symbol], feats)
        rank_values = _compute_rank_values(feature_cols, idx)
        combined = sum(rank_values) / len(rank_values)
        scores.append(
            InstrumentScore(
                symbol=symbol,
                rank=0,
                score=round(combined, 2),
                features=feats,
                risk_gates=gates,
                is_reliable=not bool(gates),
                explanation=_build_explanation(symbol, feats, gates),
            )
        )

    scores.sort(key=lambda s: (not s.is_reliable, -s.score))
    for rank, s in enumerate(scores, start=1):
        s.rank = rank

    return scores


def _build_feature_columns(
    symbols: list[str],
    features_map: dict[str, InstrumentFeatures],
) -> list[tuple[list[float | None], bool]]:
    """Return per-feature cross-sectional value lists with direction flags.

    Each tuple is (values, higher_is_better).
    """
    fm = features_map
    return [
        ([fm[s].ret_1d for s in symbols], True),
        ([fm[s].ret_5d for s in symbols], True),
        ([fm[s].ret_20d for s in symbols], True),
        ([fm[s].ret_60d for s in symbols], True),
        ([fm[s].ma20_dist for s in symbols], True),
        ([fm[s].ma50_dist for s in symbols], True),
        ([fm[s].vol_20d for s in symbols], False),
        ([fm[s].mdd_60d for s in symbols], False),
        ([fm[s].rsi_14 for s in symbols], True),
        ([fm[s].zscore_20d for s in symbols], True),
    ]


def _compute_rank_values(
    feature_cols: list[tuple[list[float | None], bool]],
    idx: int,
) -> list[float]:
    result: list[float] = []
    for values, higher_is_better in feature_cols:
        pct = _percentile_rank(values, idx)
        result.append(pct if higher_is_better else 100.0 - pct)
    return result


# ── Artifact generation ────────────────────────────────────────────────────────


def _get_git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except OSError:
        return "unknown"


def _features_to_dict(feats: InstrumentFeatures) -> dict[str, float | None]:
    return {
        "ret_1d": feats.ret_1d,
        "ret_5d": feats.ret_5d,
        "ret_20d": feats.ret_20d,
        "ret_60d": feats.ret_60d,
        "ma20_dist": feats.ma20_dist,
        "ma50_dist": feats.ma50_dist,
        "vol_20d": feats.vol_20d,
        "mdd_60d": feats.mdd_60d,
        "rsi_14": feats.rsi_14,
        "zscore_20d": feats.zscore_20d,
    }


def generate_artifact(
    scores: list[InstrumentScore],
    data: dict[str, list[OhlcvBar]],
    config: dict[str, Any],
    *,
    analysis_date: str | None = None,
    missing_symbols: list[str] | None = None,
) -> dict[str, Any]:
    now = datetime.now(tz=UTC)
    generated_at = (
        f"{analysis_date}T00:00:00+00:00" if analysis_date else now.isoformat()
    )
    sources = sorted({b.source for bars in data.values() for b in bars})
    data_source = ",".join(sources) if sources else "unknown"
    freshness: dict[str, str] = {
        symbol: bars[-1].timestamp.date().isoformat() if bars else "n/a"
        for symbol, bars in data.items()
    }
    for sym in sorted(missing_symbols or []):
        freshness[sym] = "n/a"
    instruments: list[dict[str, Any]] = [
        {
            "symbol": s.symbol,
            "rank": s.rank,
            "score": s.score,
            "is_reliable": s.is_reliable,
            "risk_gates": s.risk_gates,
            "explanation": s.explanation,
            "features": _features_to_dict(s.features),
        }
        for s in scores
    ]
    empty_feats = InstrumentFeatures(
        ret_1d=None,
        ret_5d=None,
        ret_20d=None,
        ret_60d=None,
        ma20_dist=None,
        ma50_dist=None,
        vol_20d=None,
        mdd_60d=None,
        rsi_14=None,
        zscore_20d=None,
    )
    next_rank = max((s.rank for s in scores), default=0) + 1
    for sym in sorted(missing_symbols or []):
        instruments.append({
            "symbol": sym,
            "rank": next_rank,
            "score": 0.0,
            "is_reliable": False,
            "risk_gates": [RISK_GATE_MISSING_DATA],
            "explanation": f"Suppressed: {RISK_GATE_MISSING_DATA}",
            "features": _features_to_dict(empty_feats),
        })
        next_rank += 1
    return {
        "version": ARTIFACT_VERSION,
        "metadata": {
            "generated_at": generated_at,
            "git_commit": _get_git_commit(),
            "data_source": data_source,
            "data_freshness": freshness,
            "scoring_version": SCORING_VERSION,
            "config": config,
        },
        "instruments": instruments,
    }


def save_artifact(
    artifact: dict[str, Any],
    output_dir: Path = _DEFAULT_ANALYSIS_DIR,
) -> Path:
    meta = artifact.get("metadata")
    gen_at = str(meta.get("generated_at", "")) if isinstance(meta, dict) else ""
    date_str = gen_at[:10] if gen_at else datetime.now(tz=UTC).date().isoformat()
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{date_str}.json"
    with path.open("w", encoding="utf-8") as fh:
        json.dump(artifact, fh, indent=2)
    return path


# ── CLI helpers ────────────────────────────────────────────────────────────────


def _cmd_fetch(args: argparse.Namespace) -> int:
    start = datetime.strptime(args.start, "%Y-%m-%d").replace(tzinfo=UTC)
    end = datetime.strptime(args.end, "%Y-%m-%d").replace(tzinfo=UTC)
    provider = StooqProvider()
    try:
        bars = provider.fetch_ohlcv(args.symbol, start, end, args.interval)
    except (URLError, ValueError) as exc:
        print(f"ERROR: fetch failed for {args.symbol}: {exc}")
        return 1
    if not bars:
        print(f"ERROR: no data returned for {args.symbol}")
        return 1
    path = save_ohlcv(bars, Path(args.output))
    print(f"saved {len(bars)} bars to {path}")
    if not args.no_validate:
        report = check_data_quality(bars)
        for issue in report.issues:
            print(f"WARNING: {issue}")
    return 0


def _cmd_check(args: argparse.Namespace) -> int:
    try:
        bars = load_ohlcv(args.symbol, args.interval, Path(args.data_dir))
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return 1
    report = check_data_quality(bars)
    if report.is_valid:
        sym_interval = f"{args.symbol}/{args.interval}"
        print(f"data quality OK: {report.bar_count} bars for {sym_interval}")
        return 0
    for issue in report.issues:
        print(f"ISSUE: {issue}")
    return 1


def _cmd_score(args: argparse.Namespace) -> int:
    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    data: dict[str, list[OhlcvBar]] = {}
    for sym in symbols:
        try:
            data[sym] = load_ohlcv(sym, args.interval, Path(args.data_dir))
        except FileNotFoundError:
            print(f"WARNING: no data for {sym}, skipping")
    if not data:
        print("ERROR: no symbols could be loaded")
        return 1
    results = score_instruments(data)
    print(f"{'rank':>4}  {'symbol':<20}  {'score':>6}  {'reliable':>8}  gates")
    for s in results:
        reliable = "yes" if s.is_reliable else "no"
        gates = ",".join(s.risk_gates) if s.risk_gates else "-"
        print(f"{s.rank:>4}  {s.symbol:<20}  {s.score:>6.1f}  {reliable:>8}  {gates}")
    return 0


def _cmd_generate(args: argparse.Namespace) -> int:
    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    data: dict[str, list[OhlcvBar]] = {}
    missing: list[str] = []
    for sym in symbols:
        try:
            data[sym] = load_ohlcv(sym, args.interval, Path(args.data_dir))
        except FileNotFoundError:
            print(f"WARNING: no data for {sym}, marking as missing")
            missing.append(sym)
    if not data:
        print("ERROR: no symbols could be loaded")
        return 1
    config: dict[str, Any] = {
        "stale_days": _STALE_DAYS,
        "min_history": _MIN_HISTORY,
        "interval": args.interval,
    }
    results = score_instruments(data)
    analysis_date: str | None = getattr(args, "analysis_date", None) or None
    artifact = generate_artifact(
        results,
        data,
        config,
        analysis_date=analysis_date,
        missing_symbols=missing or None,
    )
    path = save_artifact(artifact, Path(args.output))
    print(f"artifact saved to {path}")
    if missing:
        syms = ", ".join(sorted(missing))
        print(f"WARNING: {len(missing)} symbol(s) had no data: {syms}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_fetch = sub.add_parser("fetch", help="Fetch OHLCV data from Stooq")
    p_fetch.add_argument("--symbol", required=True, help="Stooq symbol, e.g. AAPL.US")
    p_fetch.add_argument("--start", required=True, help="Start date YYYY-MM-DD")
    p_fetch.add_argument("--end", required=True, help="End date YYYY-MM-DD")
    p_fetch.add_argument("--interval", default=_DEFAULT_INTERVAL, help="d/w/m")
    p_fetch.add_argument("--output", default=str(_DEFAULT_PRICES_DIR))
    p_fetch.add_argument("--no-validate", action="store_true", dest="no_validate")

    p_check = sub.add_parser("check", help="Check data quality of saved OHLCV")
    p_check.add_argument("--symbol", required=True)
    p_check.add_argument("--interval", default=_DEFAULT_INTERVAL)
    p_check.add_argument(
        "--data-dir", default=str(_DEFAULT_PRICES_DIR), dest="data_dir"
    )

    p_score = sub.add_parser("score", help="Score and rank instruments")
    p_score.add_argument("--symbols", required=True, help="Comma-separated list")
    p_score.add_argument("--interval", default=_DEFAULT_INTERVAL)
    p_score.add_argument(
        "--data-dir", default=str(_DEFAULT_PRICES_DIR), dest="data_dir"
    )

    p_gen = sub.add_parser("generate", help="Generate JSON analysis artifact")
    p_gen.add_argument("--symbols", required=True, help="Comma-separated list")
    p_gen.add_argument("--interval", default=_DEFAULT_INTERVAL)
    p_gen.add_argument("--data-dir", default=str(_DEFAULT_PRICES_DIR), dest="data_dir")
    p_gen.add_argument("--output", default=str(_DEFAULT_ANALYSIS_DIR))
    p_gen.add_argument(
        "--analysis-date",
        default=None,
        dest="analysis_date",
        help="Override analysis date (YYYY-MM-DD; default: today UTC)",
    )

    args = parser.parse_args(argv)

    if args.command == "fetch":
        return _cmd_fetch(args)
    if args.command == "check":
        return _cmd_check(args)
    if args.command == "score":
        return _cmd_score(args)
    return _cmd_generate(args)


if __name__ == "__main__":
    sys.exit(main())
