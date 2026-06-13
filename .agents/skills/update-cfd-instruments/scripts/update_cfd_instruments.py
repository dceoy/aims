#!/usr/bin/env python3
"""Create or update the CFD instruments CSV for the update-cfd-instruments skill."""

from __future__ import annotations

import argparse
import csv
import re
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

CLICK_URL = "https://www.click-sec.com/corp/guide/cfd/lineup/"
RAKUTEN_URL = "https://www.rakuten-sec.co.jp/web/rcfd/lineup/"
DEFAULT_OUTPUT = Path("data/cfd_instruments.csv")
DEFAULT_MAPPINGS_PATH = Path("data/mappings/cfd_ticker_mappings.csv")

FIELDS = [
    "source_accessed_at",
    "broker",
    "source_url",
    "category",
    "section",
    "sector",
    "instrument_name",
    "ticker_symbol",
    "underlying_asset_exchange",
    "currency",
    "tick_size",
    "price_display_example",
    "minimum_trade_unit",
    "contract_value_per_lot",
    "trade_unit",
    "trading_hours",
    "margin_rate_leverage",
    "max_order_quantity",
    "instrument_position_limit",
    "account_position_limit",
    "price_adjustment",
    "interest_adjustment",
    "rights_adjustment",
    "instrument_position_limit_note",
    "minimum_trade_quantity",
    "withholding_tax_note",
]

MAPPING_COLUMNS = (
    "mapping_type",
    "broker",
    "category",
    "instrument_name",
    "base_name",
    "ticker_symbol",
)
VALID_MAPPING_TYPES = frozenset({"broker_instrument", "instrument", "gmo_stock_base"})

UPPERCASE_UNDERLYING = re.compile(r"^\s*([A-Z][A-Z0-9. ]{0,12})\s*/")
CLICK_STOCK_EXCHANGE_SUFFIX = re.compile(r"\s*（(?:NASDAQ|NYSE)）\s*$")
CLICK_CATEGORY = re.compile(r"(.+?CFD)\s*レバレッジ：(.+)")
CLICK_STOCK_COLUMN_COUNT = 2
CLICK_STOCK_NAME_INDEX = 1
PAIR_TABLE_WIDTH = 2
RAKUTEN_MIN_ROWS = 3
RAKUTEN_DATA_START_ROW = 2
RAKUTEN_COLUMN_COUNT = 11


@dataclass
class Cell:
    text: str
    rowspan: int = 1
    colspan: int = 1


@dataclass
class Mappings:
    broker_symbols: dict[tuple[str, str], str]
    instrument_symbols: dict[str, str]
    click_stock_base_symbols: dict[str, str]


@dataclass
class LineupHTMLParser(HTMLParser):
    events: list[tuple[str, Any]] = field(default_factory=list)
    heading_tag: str | None = None
    heading_text: list[str] = field(default_factory=list)
    table_rows: list[list[Cell]] | None = None
    row: list[Cell] | None = None
    cell_attrs: dict[str, int] | None = None
    cell_text: list[str] = field(default_factory=list)
    ignored_depth: int = 0

    def __post_init__(self) -> None:
        """Initialize the underlying HTML parser with character references enabled."""
        super().__init__(convert_charrefs=True)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.ignored_depth += 1
            return
        if self.ignored_depth:
            return
        if tag in {"h2", "h3"}:
            self.heading_tag = tag
            self.heading_text = []
        elif tag == "table":
            self.table_rows = []
        elif tag == "tr" and self.table_rows is not None:
            self.row = []
        elif tag in {"th", "td"} and self.row is not None:
            attrs_dict = dict(attrs)
            self.cell_attrs = {
                "rowspan": parse_span(attrs_dict.get("rowspan")),
                "colspan": parse_span(attrs_dict.get("colspan")),
            }
            self.cell_text = []

    def handle_data(self, data: str) -> None:
        if self.ignored_depth:
            return
        if self.cell_attrs is not None:
            self.cell_text.append(data)
        elif self.heading_tag is not None:
            self.heading_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.ignored_depth = max(0, self.ignored_depth - 1)
            return
        if self.ignored_depth:
            return
        if tag in {"th", "td"} and self.row is not None and self.cell_attrs is not None:
            self.row.append(
                Cell(
                    text=clean(" ".join(self.cell_text)),
                    rowspan=self.cell_attrs["rowspan"],
                    colspan=self.cell_attrs["colspan"],
                )
            )
            self.cell_attrs = None
            self.cell_text = []
        elif tag == "tr" and self.table_rows is not None and self.row is not None:
            self.table_rows.append(self.row)
            self.row = None
        elif tag == "table" and self.table_rows is not None:
            self.events.append(("table", self.table_rows))
            self.table_rows = None
        elif tag == self.heading_tag:
            self.events.append((tag, clean(" ".join(self.heading_text))))
            self.heading_tag = None
            self.heading_text = []


def parse_span(value: str | None) -> int:
    if not value:
        return 1
    try:
        return max(1, int(value))
    except ValueError:
        return 1


def clean(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(value.replace("\xa0", " ").split())


def empty_row() -> dict[str, str]:
    return dict.fromkeys(FIELDS, "")


def load_mappings(path: Path) -> Mappings:
    if not path.exists():
        message = f"Mappings file not found: {path}"
        raise SystemExit(message)

    broker_symbols: dict[tuple[str, str], str] = {}
    instrument_symbols: dict[str, str] = {}
    click_stock_base_symbols: dict[str, str] = {}
    errors: list[str] = []

    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        actual_cols = list(reader.fieldnames or [])
        missing = [c for c in MAPPING_COLUMNS if c not in actual_cols]
        if missing:
            message = f"Mappings file {path} is missing columns: {missing}"
            raise SystemExit(message)

        for row_num, row in enumerate(reader, start=2):
            mtype = row["mapping_type"]
            ticker = row["ticker_symbol"]

            if mtype == "broker_instrument":
                key: tuple[str, str] = (row["broker"], row["instrument_name"])
                if key in broker_symbols:
                    errors.append(f"row {row_num}: duplicate broker_instrument {key}")
                else:
                    broker_symbols[key] = ticker
            elif mtype == "instrument":
                iname = row["instrument_name"]
                if iname in instrument_symbols:
                    errors.append(f"row {row_num}: duplicate instrument {iname!r}")
                else:
                    instrument_symbols[iname] = ticker
            elif mtype == "gmo_stock_base":
                base = row["base_name"]
                if base in click_stock_base_symbols:
                    errors.append(f"row {row_num}: duplicate gmo_stock_base {base!r}")
                else:
                    click_stock_base_symbols[base] = ticker
            else:
                errors.append(f"row {row_num}: unknown mapping_type {mtype!r}")

    if errors:
        print("Mapping errors:")
        for msg in errors:
            print(f"  {msg}")
        raise SystemExit(1)

    return Mappings(
        broker_symbols=broker_symbols,
        instrument_symbols=instrument_symbols,
        click_stock_base_symbols=click_stock_base_symbols,
    )


def fetch_events(url: str) -> list[tuple[str, Any]]:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
    parser = LineupHTMLParser()
    parser.feed(html)
    parser.close()
    return parser.events


def table_matrix(rows: list[list[Cell]]) -> list[list[str]]:
    matrix: list[list[str]] = []
    spans: dict[tuple[int, int], str] = {}
    for row_index, row_cells in enumerate(rows):
        row: list[str] = []
        col_index = 0

        def fill_pending(current_row_index: int, target_row: list[str]) -> None:
            nonlocal col_index
            while (current_row_index, col_index) in spans:
                target_row.append(spans.pop((current_row_index, col_index)))
                col_index += 1

        fill_pending(row_index, row)
        for cell in row_cells:
            fill_pending(row_index, row)
            for col_offset in range(cell.colspan):
                row.append(cell.text)
                if cell.rowspan > 1:
                    for row_offset in range(1, cell.rowspan):
                        span_key = row_index + row_offset, col_index + col_offset
                        spans[span_key] = cell.text
            col_index += cell.colspan
        fill_pending(row_index, row)
        matrix.append(row)
    width = max((len(row) for row in matrix), default=0)
    return [row + [""] * (width - len(row)) for row in matrix]


def parse_click(
    events: list[tuple[str, Any]], accessed_at: str
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    section_details: dict[tuple[str, str], dict[str, str]] = {}
    current_category = ""
    current_section = ""
    current_leverage = ""

    for event_type, payload in events:
        if event_type == "h2":
            heading = str(payload)
            match = CLICK_CATEGORY.fullmatch(heading)
            if match:
                current_category = clean(match.group(1))
                current_leverage = clean(match.group(2))
                current_section = current_category
            else:
                current_section = heading
            continue
        if event_type == "h3":
            current_section = str(payload)
            continue
        if event_type != "table":
            continue

        matrix = table_matrix(payload)
        if not matrix:
            continue
        header = matrix[0]
        key = (current_category, current_section)

        if header and header[0] == "CFD銘柄名":
            for source_row in matrix[1:]:
                if not source_row or not source_row[0]:
                    continue
                row = empty_row()
                row.update({
                    "source_accessed_at": accessed_at,
                    "broker": "GMOクリック証券",
                    "source_url": CLICK_URL,
                    "category": current_category,
                    "section": current_section,
                    "instrument_name": source_row[0],
                    "underlying_asset_exchange": get_cell(source_row, 1),
                    "tick_size": get_cell(source_row, 2),
                    "currency": get_cell(source_row, 3),
                    "trade_unit": get_cell(source_row, 4),
                    "trading_hours": get_cell(source_row, 5),
                    "margin_rate_leverage": current_leverage,
                })
                rows.append(row)
            continue

        if header and header[0] == "業種セクター":
            for source_row in matrix[1:]:
                if (
                    len(source_row) < CLICK_STOCK_COLUMN_COUNT
                    or not source_row[CLICK_STOCK_NAME_INDEX]
                ):
                    continue
                row = empty_row()
                row.update({
                    "source_accessed_at": accessed_at,
                    "broker": "GMOクリック証券",
                    "source_url": CLICK_URL,
                    "category": current_category,
                    "section": current_section,
                    "sector": source_row[0],
                    "instrument_name": source_row[CLICK_STOCK_NAME_INDEX],
                    "tick_size": get_cell(source_row, 2),
                    "currency": get_cell(source_row, 3),
                    "trade_unit": get_cell(source_row, 4),
                    "trading_hours": get_cell(source_row, 5),
                    "margin_rate_leverage": current_leverage,
                })
                rows.append(row)
            continue

        if len(header) == PAIR_TABLE_WIDTH:
            details: dict[str, str] = {}
            for raw_label, raw_value in matrix:
                label = clean(raw_label)
                value = clean(raw_value)
                if label == "価格調整額":
                    details["price_adjustment"] = value
                elif label == "金利調整額・権利調整額":
                    details["interest_adjustment"] = value
                    details["rights_adjustment"] = value
                elif label == "金利調整額":
                    details["interest_adjustment"] = value
                elif label == "権利調整額":
                    details["rights_adjustment"] = value
                elif label == "銘柄ごとの建玉枚数上限":
                    details["instrument_position_limit_note"] = value
                elif label == "最小取引数量":
                    details["minimum_trade_quantity"] = value
                elif label == "源泉徴収税":
                    details["withholding_tax_note"] = value
            section_details[key] = details

    for row in rows:
        row.update(section_details.get((row["category"], row["section"]), {}))
    return rows


def parse_rakuten(
    events: list[tuple[str, Any]], accessed_at: str
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current_category = ""

    for event_type, payload in events:
        if event_type == "h2":
            current_category = str(payload)
            continue
        if event_type != "table":
            continue

        matrix = table_matrix(payload)
        if (
            len(matrix) < RAKUTEN_MIN_ROWS
            or len(matrix[1]) < RAKUTEN_COLUMN_COUNT
            or matrix[1][0] != "銘柄名"
        ):
            continue
        for source_row in matrix[RAKUTEN_DATA_START_ROW:]:
            if len(source_row) < RAKUTEN_COLUMN_COUNT or not source_row[0]:
                continue
            row = empty_row()
            row.update({
                "source_accessed_at": accessed_at,
                "broker": "楽天証券",
                "source_url": RAKUTEN_URL,
                "category": current_category,
                "section": current_category,
                "instrument_name": source_row[0],
                "underlying_asset_exchange": source_row[1],
                "currency": source_row[2],
                "tick_size": source_row[3],
                "price_display_example": source_row[4],
                "minimum_trade_unit": source_row[5],
                "contract_value_per_lot": source_row[6],
                "margin_rate_leverage": source_row[7],
                "max_order_quantity": source_row[8],
                "instrument_position_limit": source_row[9],
                "account_position_limit": source_row[10],
            })
            rows.append(row)
    return rows


def get_cell(row: list[str], index: int) -> str:
    return row[index] if index < len(row) else ""


def infer_ticker_symbol(row: dict[str, str], mappings: Mappings) -> str:
    match = UPPERCASE_UNDERLYING.match(row.get("underlying_asset_exchange", ""))
    if match:
        return match.group(1).strip()
    broker_symbol = mappings.broker_symbols.get((row["broker"], row["instrument_name"]))
    if broker_symbol:
        return broker_symbol
    instrument_symbol = mappings.instrument_symbols.get(row["instrument_name"])
    if instrument_symbol:
        return instrument_symbol
    if row["broker"] == "GMOクリック証券" and row["category"] == "株式CFD":
        base_name = CLICK_STOCK_EXCHANGE_SUFFIX.sub("", row["instrument_name"])
        return mappings.click_stock_base_symbols.get(base_name, "")
    return ""


def add_ticker_symbols(rows: list[dict[str, str]], mappings: Mappings) -> None:
    missing: list[tuple[int, str, str, str, str]] = []
    for row_number, row in enumerate(rows, start=2):
        symbol = infer_ticker_symbol(row, mappings)
        if not symbol:
            missing.append((
                row_number,
                row["broker"],
                row["category"],
                row["instrument_name"],
                row["underlying_asset_exchange"],
            ))
        row["ticker_symbol"] = symbol
    if missing:
        print("Missing ticker_symbol mappings:")
        for item in missing:
            print("\t".join(map(str, item)))
        raise SystemExit(1)


def build_rows(accessed_at: str, mappings: Mappings) -> list[dict[str, str]]:
    rows = parse_click(fetch_events(CLICK_URL), accessed_at)
    rows.extend(parse_rakuten(fetch_events(RAKUTEN_URL), accessed_at))
    if not rows:
        message = "No CFD rows extracted"
        raise SystemExit(message)
    add_ticker_symbols(rows, mappings)
    return rows


def write_csv(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="CSV output path"
    )
    parser.add_argument(
        "--mappings",
        type=Path,
        default=DEFAULT_MAPPINGS_PATH,
        help="Ticker mappings CSV path",
    )
    parser.add_argument(
        "--accessed-at",
        default=datetime.now().astimezone().isoformat(timespec="seconds"),
        help="Timestamp to write to source_accessed_at",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mappings = load_mappings(args.mappings)
    rows = build_rows(args.accessed_at, mappings)
    write_csv(rows, args.output)
    print(f"wrote {args.output} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
