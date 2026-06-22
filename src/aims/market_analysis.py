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
    uv run .agents/skills/market-analysis/scripts/market_analysis.py \
        generate --mapping data/mappings/canonical_instrument_mappings.csv \
        --provider stooq --output data/analysis/
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

from aims.policy import (
    DEFAULT_COVERAGE_POLICY,
    CoveragePolicy,
    build_config_dict,
    build_coverage_metadata,
    evaluate_coverage,
    get_data_quality_policy,
)

# ── Constants ────────────────────────────────────────────────────────────────

_DEFAULT_PRICES_DIR: Final[Path] = Path("data/prices")
_DEFAULT_ANALYSIS_DIR: Final[Path] = Path("data/analysis")
_DEFAULT_INTERVAL: Final[str] = "d"
_DEFAULT_PROVIDER: Final[str] = "stooq"
_DAILY_POLICY = get_data_quality_policy(_DEFAULT_INTERVAL)
_STALE_DAYS: Final[int] = _DAILY_POLICY.thresholds.stale_days
_MIN_HISTORY: Final[int] = _DAILY_POLICY.thresholds.min_history
_MAX_GAP_DAYS: Final[int] = _DAILY_POLICY.thresholds.max_gap_days
_HIGH_VOL_THRESHOLD: Final[float] = 1.0

_FETCH_STATUS_VERSION: Final[str] = "1.0.0"
_FETCH_STATUS_SUCCESS: Final[str] = "success"
_FETCH_STATUS_FAILED: Final[str] = "failed"
_FETCH_STATUS_PENDING: Final[str] = "pending"

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

# ── Provider metadata ─────────────────────────────────────────────────────────


@dataclass(frozen=True)
class ProviderMetadata:
    """Descriptive metadata for a market data provider."""

    name: str
    supported_intervals: tuple[str, ...]
    symbol_format_notes: str
    timezone_notes: str
    known_limitations: str


STOOQ_METADATA: Final[ProviderMetadata] = ProviderMetadata(
    name="stooq",
    supported_intervals=("d", "w", "m"),
    symbol_format_notes=(
        "Stooq-specific convention: e.g. 'AAPL.US', '^SPX', '7203.JP'."
        " Index symbols use the '^' prefix."
    ),
    timezone_notes=(
        "Timestamps normalized to UTC midnight."
        " Bar date reflects the exchange close date."
    ),
    known_limitations=(
        "Daily, weekly, and monthly bars only — no intraday data."
        " Data availability and history depth vary by symbol."
        " No authentication required but subject to undocumented rate limits."
        " Requires outbound network access."
    ),
)

CSV_METADATA: Final[ProviderMetadata] = ProviderMetadata(
    name="csv",
    supported_intervals=("d", "w", "m"),
    symbol_format_notes=(
        "Symbol must match the file name written by save_ohlcv."
        " Suitable for offline workflows and deterministic unit tests."
    ),
    timezone_notes="UTC assumed for naive timestamps loaded from CSV.",
    known_limitations=(
        "Offline only; reflects data as saved by another provider."
        " No network fetch — cannot be used in the daily workflow."
    ),
)

_PROVIDER_REGISTRY: Final[dict[str, ProviderMetadata]] = {
    "stooq": STOOQ_METADATA,
    "csv": CSV_METADATA,
}

KNOWN_PROVIDERS: Final[frozenset[str]] = frozenset(_PROVIDER_REGISTRY.keys())


def get_provider_metadata(name: str) -> ProviderMetadata:
    """Return metadata for *name*, raising ValueError for unknown providers."""
    meta = _PROVIDER_REGISTRY.get(name)
    if meta is None:
        known = ", ".join(sorted(KNOWN_PROVIDERS))
        msg = f"unknown provider {name!r}; known providers: {known}"
        raise ValueError(msg)
    return meta


def validate_provider_interval(provider_name: str, interval: str) -> None:
    """Raise ValueError when *provider_name* does not support *interval*."""
    meta = get_provider_metadata(provider_name)
    if interval not in meta.supported_intervals:
        supported = ", ".join(sorted(meta.supported_intervals))
        msg = (
            f"provider {provider_name!r} does not support interval {interval!r};"
            f" supported intervals: {supported}"
        )
        raise ValueError(msg)


# ── Canonical instrument mapping ─────────────────────────────────────────────

_MAPPING_REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "canonical_id",
    "display_name",
    "asset_class",
    "broker",
    "broker_instrument_name",
    "broker_ticker_symbol",
    "provider",
    "provider_symbol",
    "provider_interval",
    "tradable",
)

_MAPPING_REQUIRED_NON_EMPTY: Final[frozenset[str]] = frozenset({
    "canonical_id",
    "display_name",
    "provider",
    "provider_symbol",
    "provider_interval",
})


@dataclass(frozen=True)
class InstrumentMappingRow:
    """One row from canonical_instrument_mappings.csv."""

    canonical_id: str
    display_name: str
    asset_class: str
    broker: str
    broker_instrument_name: str
    broker_ticker_symbol: str
    provider: str
    provider_symbol: str
    provider_interval: str
    tradable: str
    notes: str = ""


def load_instrument_mappings(mapping_path: Path) -> list[InstrumentMappingRow]:
    """Load and parse canonical_instrument_mappings.csv."""
    with mapping_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return [
            InstrumentMappingRow(
                canonical_id=row.get("canonical_id", ""),
                display_name=row.get("display_name", ""),
                asset_class=row.get("asset_class", ""),
                broker=row.get("broker", ""),
                broker_instrument_name=row.get("broker_instrument_name", ""),
                broker_ticker_symbol=row.get("broker_ticker_symbol", ""),
                provider=row.get("provider", ""),
                provider_symbol=row.get("provider_symbol", ""),
                provider_interval=row.get("provider_interval", ""),
                tradable=row.get("tradable", ""),
                notes=row.get("notes", ""),
            )
            for row in reader
        ]


def symbols_from_mappings(
    rows: list[InstrumentMappingRow],
    provider: str,
    interval: str,
) -> list[str]:
    """Return provider symbols for *provider*/*interval* from mapping rows.

    Results are sorted by canonical_id for determinism.
    """
    matched = [
        r for r in rows if r.provider == provider and r.provider_interval == interval
    ]
    matched.sort(key=lambda r: r.canonical_id)
    seen: set[str] = set()
    result: list[str] = []
    for r in matched:
        if r.provider_symbol not in seen:
            seen.add(r.provider_symbol)
            result.append(r.provider_symbol)
    return result


def instrument_display_map(
    rows: list[InstrumentMappingRow],
    provider: str,
    interval: str,
) -> dict[str, dict[str, str]]:
    """Return {provider_symbol: {canonical_id, display_name}}.

    Filters to rows matching *provider* and *interval*.
    """
    result: dict[str, dict[str, str]] = {}
    for r in rows:
        if (
            r.provider == provider
            and r.provider_interval == interval
            and r.provider_symbol not in result
        ):
            result[r.provider_symbol] = {
                "canonical_id": r.canonical_id,
                "display_name": r.display_name,
            }
    return result


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


def make_provider(
    name: str,
    data_dir: Path = _DEFAULT_PRICES_DIR,
) -> MarketDataProvider:
    """Instantiate a provider by registry name."""
    if name == "stooq":
        return StooqProvider()
    if name == "csv":
        return CsvFileProvider(data_dir)
    known = ", ".join(sorted(KNOWN_PROVIDERS))
    msg = f"unknown provider {name!r}; known providers: {known}"
    raise ValueError(msg)


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


# ── Fetch status (current-run coverage source of truth) ───────────────────────


def init_fetch_status(
    path: Path,
    symbols: list[str],
    *,
    interval: str,
    analysis_date: str | None = None,
    provider: str | None = None,
) -> None:
    """Initialize a fetch-status file with all symbols marked pending."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {
        "version": _FETCH_STATUS_VERSION,
        "interval": interval,
        "analysis_date": analysis_date,
        "symbols": {symbol: {"status": _FETCH_STATUS_PENDING} for symbol in symbols},
    }
    if provider is not None:
        payload["provider"] = provider
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)


def load_fetch_status(path: Path) -> dict[str, Any]:
    """Load a fetch-status JSON file."""
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        msg = f"fetch status at {path} must be a JSON object"
        raise TypeError(msg)
    return data


def record_fetch_status(
    path: Path,
    symbol: str,
    *,
    success: bool,
    error: str | None = None,
) -> None:
    """Record the outcome of a single-symbol fetch in *path*."""
    data = load_fetch_status(path)
    symbols = data.get("symbols")
    if not isinstance(symbols, dict):
        msg = f"fetch status at {path} is missing a valid 'symbols' object"
        raise TypeError(msg)
    entry: dict[str, str] = {
        "status": _FETCH_STATUS_SUCCESS if success else _FETCH_STATUS_FAILED
    }
    if error:
        entry["error"] = error
    symbols[symbol] = entry
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def validate_fetch_status(
    fetch_status: dict[str, Any],
    *,
    interval: str,
    analysis_date: str | None = None,
    provider: str | None = None,
) -> None:
    """Reject fetch-status metadata that does not match the current run."""
    status_interval = fetch_status.get("interval")
    if status_interval != interval:
        msg = (
            f"fetch status interval {status_interval!r} does not match"
            f" requested interval {interval!r}"
        )
        raise ValueError(msg)
    status_date = fetch_status.get("analysis_date")
    if (
        analysis_date is not None
        and status_date is not None
        and status_date != analysis_date
    ):
        msg = (
            f"fetch status analysis_date {status_date!r} does not match"
            f" requested analysis_date {analysis_date!r}"
        )
        raise ValueError(msg)
    if provider is not None:
        status_provider = fetch_status.get("provider")
        if status_provider is not None and status_provider != provider:
            msg = (
                f"fetch status provider {status_provider!r} does not match"
                f" requested provider {provider!r}"
            )
            raise ValueError(msg)


def resolve_symbols_from_fetch_status(
    symbols: list[str],
    fetch_status: dict[str, Any],
) -> tuple[list[str], list[str]]:
    """Return (fetched, missing) symbol lists from a fetch-status payload."""
    raw_symbols = fetch_status.get("symbols")
    if not isinstance(raw_symbols, dict):
        msg = "fetch status is missing a valid 'symbols' object"
        raise TypeError(msg)
    fetched: list[str] = []
    missing: list[str] = []
    for symbol in symbols:
        entry = raw_symbols.get(symbol)
        if isinstance(entry, dict) and entry.get("status") == _FETCH_STATUS_SUCCESS:
            fetched.append(symbol)
        else:
            missing.append(symbol)
    return fetched, missing


# ── Data quality ──────────────────────────────────────────────────────────────


def check_data_quality(
    bars: list[OhlcvBar],
    *,
    stale_days: int = _STALE_DAYS,
    min_history: int = _MIN_HISTORY,
    max_gap_days: int = _MAX_GAP_DAYS,
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
            if gap > max_gap_days:
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
    max_gap_days: int = _MAX_GAP_DAYS,
) -> list[InstrumentScore]:
    if not data:
        return []

    symbols = list(data)
    reports = {
        s: check_data_quality(
            data[s],
            stale_days=stale_days,
            min_history=min_history,
            max_gap_days=max_gap_days,
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
    coverage: dict[str, Any] | None = None,
    instrument_metadata: dict[str, dict[str, str]] | None = None,
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

    def _build_inst(s: InstrumentScore) -> dict[str, Any]:
        entry: dict[str, Any] = {
            "symbol": s.symbol,
            "rank": s.rank,
            "score": s.score,
            "is_reliable": s.is_reliable,
            "risk_gates": s.risk_gates,
            "explanation": s.explanation,
            "features": _features_to_dict(s.features),
        }
        if instrument_metadata and s.symbol in instrument_metadata:
            meta = instrument_metadata[s.symbol]
            if "canonical_id" in meta:
                entry["canonical_id"] = meta["canonical_id"]
            if "display_name" in meta:
                entry["display_name"] = meta["display_name"]
        return entry

    instruments: list[dict[str, Any]] = [_build_inst(s) for s in scores]
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
        entry: dict[str, Any] = {
            "symbol": sym,
            "rank": next_rank,
            "score": 0.0,
            "is_reliable": False,
            "risk_gates": [RISK_GATE_MISSING_DATA],
            "explanation": f"Suppressed: {RISK_GATE_MISSING_DATA}",
            "features": _features_to_dict(empty_feats),
        }
        if instrument_metadata and sym in instrument_metadata:
            meta = instrument_metadata[sym]
            if "canonical_id" in meta:
                entry["canonical_id"] = meta["canonical_id"]
            if "display_name" in meta:
                entry["display_name"] = meta["display_name"]
        instruments.append(entry)
        next_rank += 1
    artifact_metadata: dict[str, Any] = {
        "generated_at": generated_at,
        "git_commit": _get_git_commit(),
        "data_source": data_source,
        "data_freshness": freshness,
        "scoring_version": SCORING_VERSION,
        "config": config,
    }
    if coverage is not None:
        artifact_metadata["coverage"] = coverage
    return {
        "version": ARTIFACT_VERSION,
        "metadata": artifact_metadata,
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
    provider_name: str = (
        getattr(args, "provider", _DEFAULT_PROVIDER) or _DEFAULT_PROVIDER
    )
    if provider_name == "csv":
        print(
            "ERROR: provider 'csv' is a read-only cached-data provider"
            " and cannot be used with 'fetch'."
            " Use '--provider stooq' to download data."
        )
        return 1
    try:
        validate_provider_interval(provider_name, args.interval)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    start = datetime.strptime(args.start, "%Y-%m-%d").replace(tzinfo=UTC)
    end = datetime.strptime(args.end, "%Y-%m-%d").replace(tzinfo=UTC)
    provider = make_provider(provider_name, Path(args.output))
    fetch_status_path: Path | None = (
        Path(args.fetch_status) if getattr(args, "fetch_status", None) else None
    )
    try:
        bars = provider.fetch_ohlcv(args.symbol, start, end, args.interval)
    except (URLError, ValueError) as exc:
        print(f"ERROR: fetch failed for {args.symbol}: {exc}")
        if fetch_status_path is not None:
            record_fetch_status(
                fetch_status_path, args.symbol, success=False, error=str(exc)
            )
        return 1
    if not bars:
        print(f"ERROR: no data returned for {args.symbol}")
        if fetch_status_path is not None:
            record_fetch_status(
                fetch_status_path,
                args.symbol,
                success=False,
                error="no data returned",
            )
        return 1
    path = save_ohlcv(bars, Path(args.output))
    print(f"saved {len(bars)} bars to {path}")
    if fetch_status_path is not None:
        record_fetch_status(fetch_status_path, args.symbol, success=True)
    if not args.no_validate:
        policy = get_data_quality_policy(args.interval)
        thresholds = policy.thresholds
        report = check_data_quality(
            bars,
            stale_days=thresholds.stale_days,
            min_history=thresholds.min_history,
            max_gap_days=thresholds.max_gap_days,
        )
        for issue in report.issues:
            print(f"WARNING: {issue}")
    return 0


def _cmd_check(args: argparse.Namespace) -> int:
    try:
        bars = load_ohlcv(args.symbol, args.interval, Path(args.data_dir))
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return 1
    policy = get_data_quality_policy(args.interval)
    report = check_data_quality(
        bars,
        stale_days=policy.thresholds.stale_days,
        min_history=policy.thresholds.min_history,
        max_gap_days=policy.thresholds.max_gap_days,
    )
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
    policy = get_data_quality_policy(args.interval)
    thresholds = policy.thresholds
    results = score_instruments(
        data,
        stale_days=thresholds.stale_days,
        min_history=thresholds.min_history,
        max_gap_days=thresholds.max_gap_days,
    )
    print(f"{'rank':>4}  {'symbol':<20}  {'score':>6}  {'reliable':>8}  gates")
    for s in results:
        reliable = "yes" if s.is_reliable else "no"
        gates = ",".join(s.risk_gates) if s.risk_gates else "-"
        print(f"{s.rank:>4}  {s.symbol:<20}  {s.score:>6.1f}  {reliable:>8}  {gates}")
    return 0


def _cmd_init_fetch_status(args: argparse.Namespace) -> int:
    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    if not symbols:
        print("ERROR: no symbols provided")
        return 1
    provider_name: str | None = getattr(args, "provider", None) or None
    init_fetch_status(
        Path(args.output),
        symbols,
        interval=args.interval,
        analysis_date=getattr(args, "analysis_date", None) or None,
        provider=provider_name,
    )
    print(f"fetch status initialized for {len(symbols)} symbol(s) at {args.output}")
    return 0


def _resolve_symbols_for_generate(args: argparse.Namespace) -> list[str] | None:
    """Return the symbol list for generate, or None on error (prints message)."""
    symbols_arg: str | None = getattr(args, "symbols", None)
    mapping_arg: str | None = getattr(args, "mapping", None)

    if symbols_arg and mapping_arg:
        print("ERROR: --symbols and --mapping are mutually exclusive")
        return None

    if mapping_arg:
        provider_name: str = (
            getattr(args, "provider", _DEFAULT_PROVIDER) or _DEFAULT_PROVIDER
        )
        mapping_path = Path(mapping_arg)
        if not mapping_path.exists():
            print(f"ERROR: mapping file not found: {mapping_path}")
            return None
        try:
            rows = load_instrument_mappings(mapping_path)
        except (OSError, csv.Error) as exc:
            print(f"ERROR: failed to load mapping file: {exc}")
            return None
        syms = symbols_from_mappings(rows, provider_name, args.interval)
        if not syms:
            print(
                f"ERROR: no symbols found in mapping for"
                f" provider={provider_name!r} interval={args.interval!r}"
            )
            return None
        return syms

    if symbols_arg:
        return [s.strip() for s in symbols_arg.split(",") if s.strip()]

    print("ERROR: one of --symbols or --mapping is required")
    return None


def _cmd_generate(args: argparse.Namespace) -> int:
    provider_name: str = (
        getattr(args, "provider", _DEFAULT_PROVIDER) or _DEFAULT_PROVIDER
    )
    try:
        validate_provider_interval(provider_name, args.interval)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    symbols = _resolve_symbols_for_generate(args)
    if symbols is None:
        return 1
    if not symbols:
        print("ERROR: no symbols provided")
        return 1

    # Load mapping metadata for display names when mapping is provided
    display_meta: dict[str, dict[str, str]] | None = None
    mapping_arg: str | None = getattr(args, "mapping", None)
    if mapping_arg:
        mapping_path = Path(mapping_arg)
        try:
            rows = load_instrument_mappings(mapping_path)
            display_meta = instrument_display_map(rows, provider_name, args.interval)
        except (OSError, csv.Error):
            display_meta = None

    coverage_policy = CoveragePolicy(
        min_success_ratio=args.min_success_ratio,
        max_missing_symbols=args.max_missing_symbols,
    )
    policy = get_data_quality_policy(args.interval, coverage=coverage_policy)
    thresholds = policy.thresholds

    fetch_status_path: Path | None = (
        Path(args.fetch_status) if getattr(args, "fetch_status", None) else None
    )
    if fetch_status_path is not None:
        try:
            fetch_status = load_fetch_status(fetch_status_path)
            validate_fetch_status(
                fetch_status,
                interval=args.interval,
                analysis_date=getattr(args, "analysis_date", None) or None,
                provider=provider_name if fetch_status.get("provider") else None,
            )
        except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError) as exc:
            print(f"ERROR: invalid fetch status file: {exc}")
            return 1
        fetched_symbols, missing = resolve_symbols_from_fetch_status(
            symbols, fetch_status
        )
    else:
        fetched_symbols = []
        missing = []
        for sym in symbols:
            try:
                load_ohlcv(sym, args.interval, Path(args.data_dir))
            except FileNotFoundError:
                missing.append(sym)
            else:
                fetched_symbols.append(sym)

    coverage_result = evaluate_coverage(
        symbols, fetched_symbols, missing, coverage_policy
    )
    coverage_metadata = build_coverage_metadata(coverage_result)

    data: dict[str, list[OhlcvBar]] = {}
    load_failures: list[str] = []
    for sym in fetched_symbols:
        try:
            data[sym] = load_ohlcv(sym, args.interval, Path(args.data_dir))
        except FileNotFoundError:
            print(f"WARNING: fetch status success but no data file for {sym}")
            load_failures.append(sym)
    if load_failures:
        fetched_symbols = [s for s in fetched_symbols if s not in load_failures]
        missing = sorted(set(missing) | set(load_failures))
        coverage_result = evaluate_coverage(
            symbols, fetched_symbols, missing, coverage_policy
        )
        coverage_metadata = build_coverage_metadata(coverage_result)

    if not data:
        print("ERROR: no symbols could be loaded")
        for violation in coverage_result.violations:
            print(f"ERROR: coverage gate failed: {violation}")
        return 1

    config = build_config_dict(policy)
    analysis_date: str | None = getattr(args, "analysis_date", None) or None
    reference_time: datetime | None = None
    if analysis_date:
        reference_time = datetime.strptime(analysis_date, "%Y-%m-%d").replace(
            tzinfo=UTC
        )
    results = score_instruments(
        data,
        reference_time=reference_time,
        stale_days=thresholds.stale_days,
        min_history=thresholds.min_history,
        max_gap_days=thresholds.max_gap_days,
    )
    artifact = generate_artifact(
        results,
        data,
        config,
        analysis_date=analysis_date,
        missing_symbols=missing or None,
        coverage=coverage_metadata,
        instrument_metadata=display_meta,
    )
    path = save_artifact(artifact, Path(args.output))
    print(f"artifact saved to {path}")
    if missing:
        syms = ", ".join(sorted(missing))
        print(f"WARNING: {len(missing)} symbol(s) had no data: {syms}")
    if not coverage_result.passed:
        for violation in coverage_result.violations:
            print(f"ERROR: coverage gate failed: {violation}")
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_fetch = sub.add_parser(
        "fetch", help="Fetch OHLCV data from a market data provider"
    )
    p_fetch.add_argument(
        "--symbol", required=True, help="Provider symbol, e.g. AAPL.US"
    )
    p_fetch.add_argument("--start", required=True, help="Start date YYYY-MM-DD")
    p_fetch.add_argument("--end", required=True, help="End date YYYY-MM-DD")
    p_fetch.add_argument("--interval", default=_DEFAULT_INTERVAL, help="d/w/m")
    p_fetch.add_argument("--output", default=str(_DEFAULT_PRICES_DIR))
    p_fetch.add_argument("--no-validate", action="store_true", dest="no_validate")
    p_fetch.add_argument(
        "--provider",
        default=_DEFAULT_PROVIDER,
        choices=sorted(KNOWN_PROVIDERS),
        help=f"Market data provider (default: {_DEFAULT_PROVIDER})",
    )
    p_fetch.add_argument(
        "--fetch-status",
        default=None,
        dest="fetch_status",
        help="Path to fetch-status JSON updated with this fetch result",
    )

    p_init_status = sub.add_parser(
        "init-fetch-status",
        help="Initialize fetch-status JSON for a symbol list",
    )
    p_init_status.add_argument("--symbols", required=True, help="Comma-separated list")
    p_init_status.add_argument("--interval", default=_DEFAULT_INTERVAL)
    p_init_status.add_argument(
        "--output",
        required=True,
        help="Path to fetch-status JSON file to create",
    )
    p_init_status.add_argument(
        "--analysis-date",
        default=None,
        dest="analysis_date",
        help="Analysis date (YYYY-MM-DD) recorded in fetch status",
    )
    p_init_status.add_argument(
        "--provider",
        default=_DEFAULT_PROVIDER,
        choices=sorted(KNOWN_PROVIDERS),
        help=f"Market data provider (default: {_DEFAULT_PROVIDER})",
    )

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
    p_gen_src = p_gen.add_mutually_exclusive_group(required=True)
    p_gen_src.add_argument(
        "--symbols",
        default=None,
        help="Comma-separated provider symbol list (explicit mode)",
    )
    p_gen_src.add_argument(
        "--mapping",
        default=None,
        metavar="PATH",
        help="Path to canonical_instrument_mappings.csv (mapping-derived mode)",
    )
    p_gen.add_argument("--interval", default=_DEFAULT_INTERVAL)
    p_gen.add_argument("--data-dir", default=str(_DEFAULT_PRICES_DIR), dest="data_dir")
    p_gen.add_argument("--output", default=str(_DEFAULT_ANALYSIS_DIR))
    p_gen.add_argument(
        "--provider",
        default=_DEFAULT_PROVIDER,
        choices=sorted(KNOWN_PROVIDERS),
        help=f"Market data provider (default: {_DEFAULT_PROVIDER})",
    )
    p_gen.add_argument(
        "--analysis-date",
        default=None,
        dest="analysis_date",
        help="Override analysis date (YYYY-MM-DD; default: today UTC)",
    )
    p_gen.add_argument(
        "--min-success-ratio",
        type=float,
        default=DEFAULT_COVERAGE_POLICY.min_success_ratio,
        dest="min_success_ratio",
        help="Minimum fetched/total symbol ratio (default: 0.8)",
    )
    p_gen.add_argument(
        "--max-missing-symbols",
        type=int,
        default=DEFAULT_COVERAGE_POLICY.max_missing_symbols,
        dest="max_missing_symbols",
        help="Maximum allowed missing symbols (default: 1)",
    )
    p_gen.add_argument(
        "--fetch-status",
        default=None,
        dest="fetch_status",
        help="Path to fetch-status JSON from the current fetch run",
    )

    args = parser.parse_args(argv)

    if args.command == "fetch":
        return _cmd_fetch(args)
    if args.command == "check":
        return _cmd_check(args)
    if args.command == "score":
        return _cmd_score(args)
    if args.command == "init-fetch-status":
        return _cmd_init_fetch_status(args)
    return _cmd_generate(args)


if __name__ == "__main__":
    sys.exit(main())
