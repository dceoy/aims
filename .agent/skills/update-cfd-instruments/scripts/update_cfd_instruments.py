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

BROKER_SYMBOLS = {
    ("GMOクリック証券", "日本225"): "NK; NKD; NIY",
    ("GMOクリック証券", "日本TPX"): "TPX",
    ("GMOクリック証券", "米国30"): "YM",
    ("GMOクリック証券", "米国S500"): "ES",
    ("GMOクリック証券", "米国NQ100"): "NQ",
    ("GMOクリック証券", "米国NQ100ミニ"): "MNQ",
    ("GMOクリック証券", "米国RS2000"): "RTY",
    ("GMOクリック証券", "上海A50"): "CN",
    ("GMOクリック証券", "香港H"): "HSI",
    ("GMOクリック証券", "イギリス100"): "Z",
    ("GMOクリック証券", "ユーロ50"): "FESX",
    ("GMOクリック証券", "ドイツ40"): "FDAX",
    ("GMOクリック証券", "フランス40"): "FCE",
    ("楽天証券", "日本225"): "NKD; NIY",
    ("楽天証券", "日本TPX"): "TPX",
    ("楽天証券", "米国30"): "YM",
    ("楽天証券", "米国500"): "ES",
    ("楽天証券", "米国400"): "EMD",
    ("楽天証券", "米国NQ100"): "NQ",
    ("楽天証券", "米国2000"): "RTY",
    ("楽天証券", "米国TEC"): "FANG",
    ("楽天証券", "英国100"): "Z",
    ("楽天証券", "ドイツ40"): "FDAX",
    ("楽天証券", "ユーロ50"): "FESX",
    ("楽天証券", "中国A50"): "CN",
    ("楽天証券", "中国H株"): "HHI",
    ("楽天証券", "香港HS50"): "HSI",
    ("楽天証券", "インド50"): "NIFTY",
    ("楽天証券", "オーストラリア200"): "AP",
    ("楽天証券", "フランス40"): "FCE",
    ("楽天証券", "イタリア40"): "FIB",
    ("楽天証券", "スペイン35"): "IBEX",
    ("楽天証券", "スイス20"): "FSMI",
    ("楽天証券", "オランダ25"): "EOE",
    ("楽天証券", "シンガポール"): "SMSI",
    ("楽天証券", "台湾50"): "TW",
}

INSTRUMENT_SYMBOLS = {
    "米国半導体ETF": "SOXX",
    "インドネシア株価指数ETF": "EIDO",
    "タイ株価指数ETF": "THD",
    "ベトナム株価指数ETF": "VNM",
    "マレーシア株価指数ETF": "EWM",
    "フィリピン株価指数ETF": "EPHE",
    "シンガポール株価指数ETF": "EWS",
    "韓国株価指数ETF": "EWY",
    "台湾株価指数ETF": "EWT",
    "トルコ株価指数ETF": "TUR",
    "ロシア株価指数ETF ※": "RSX",
    "イタリア株価指数ETF": "EWI",
    "スイス株価指数ETF": "EWL",
    "オランダ株価指数ETF": "EWN",
    "ベルギー株価指数ETF": "EWK",
    "スウェーデン株価指数ETF": "EWD",
    "南アフリカ株価指数ETF": "EZA",
    "ブラジル株価指数ETF": "EWZ",
    "チリ株価指数ETF": "ECH",
    "メキシコ株価指数ETF": "EWW",
    "カナダ株価指数ETF": "EWC",
    "オーストラリア株価指数ETF": "EWA",
    "金スポット": "XAU",
    "銀スポット": "XAG",
    "プラチナスポット": "XPT",
    "銅先物": "HG",
    "鉄鉱石": "FEF",
    "WTI原油": "CL",
    "北海原油": "BRN",
    "天然ガス": "NG",
    "ガソリン": "RB",
    "ヒーティングオイル": "HO",
    "コーン": "ZC",
    "大豆": "ZS",
    "小麦": "ZW",
    "砂糖": "SB",
    "粗糖": "SB",
    "ココア": "CC",
    "コーヒー": "KC",
    "コットン": "CT",
    "牛肉": "LE",
    "生牛": "LE",
    "豚肉": "HE",
    "金": "GC",
    "銀": "SI",
    "銅": "HG",
    "プラチナ": "PL",
    "パラジウム": "PA",
    "米国VI": "VX",
    "米国30ブル3倍ETF": "UDOW",
    "米国30ベア3倍ETF": "SDOW",
    "NQ100ブル3倍ETF": "TQQQ",
    "NQ100ベア3倍ETF": "SQQQ",
    "米国小型株ベア3倍ETF": "TZA",
    "米国半導体ブル3倍ETF": "SOXL",
    "米国半導体ベア3倍ETF": "SOXS",
    "米国エネルギーブル2倍ETF": "ERX",
    "米国エネルギーベア2倍ETF": "ERY",
    "新興国ブル3倍ETF": "EDC",
    "新興国ベア3倍ETF": "EDZ",
    "中国ブル3倍ETF": "YINN",
    "中国ベア3倍ETF": "YANG",
    "金ブル2倍ETF": "NUGT",
    "金ベア2倍ETF": "DUST",
    "米国債20年ブル3倍ETF": "TMF",
    "米国債20年ベア3倍ETF": "TMV",
    "グローバル不動産ETF": "RWO",
    "グローバル（米国除く）不動産ETF": "RWX",
    "米国リートETF": "VNQ",
    "米国リート・不動産株ETF": "IYR",
    "モーゲージ不動産ETF": "REM",
}

CLICK_STOCK_BASE_SYMBOLS = {
    "Amazon": "AMZN",
    "NIKE": "NKE",
    "GAP": "GPS",
    "ウォルマート": "WMT",
    "P&G": "PG",
    "ペプシ": "PEP",
    "コストコ・ホールセール": "COST",
    "イーベイ": "EBAY",
    "ホーム・デポ": "HD",
    "GE エアロスペース（旧ゼネラル・エレクトリック）": "GE",
    "3M": "MMM",
    "キャタピラー": "CAT",
    "Apple": "AAPL",
    "IBM": "IBM",
    "インテル": "INTC",
    "HP": "HPQ",
    "シスコシステムズ": "CSCO",
    "NVIDIA": "NVDA",
    "AMD": "AMD",
    "クアルコム": "QCOM",
    "アプライド・マテリアルズ": "AMAT",
    "テキサス・インスツルメンツ": "TXN",
    "ラムリサーチ": "LRCX",
    "テラダイン": "TER",
    "スカイワークスソリューションズ": "SWKS",
    "バンク・オブ・アメリカ": "BAC",
    "シティグループ": "C",
    "バークシャー・ハサウェイ": "BRK B",
    "アメリカン・エキスプレス": "AXP",
    "ゴールドマン・サックス・グループ": "GS",
    "モルガン・スタンレー": "MS",
    "Visa": "V",
    "アフラック": "AFL",
    "JPモルガン・チェース": "JPM",
    "ユナイテッドヘルス・グループ": "UNH",
    "コインベース": "COIN",
    "Travelers": "TRV",
    "マクドナルド": "MCD",
    "スターバックス": "SBUX",
    "コカ・コーラ": "KO",
    "アリババ": "BABA",
    "ウォルト・ディズニー": "DIS",
    "ジョンソン・エンド・ジョンソン": "JNJ",
    "Alphabet（旧Google）": "GOOGL",
    "マイクロソフト": "MSFT",
    "オラクル": "ORCL",
    "Meta Platforms(旧Facebook)": "META",
    "アドビ・システムズ": "ADBE",
    "ネットフリックス": "NFLX",
    "アカマイ・テクノロジーズ": "AKAM",
    "Tモバイル": "TMUS",
    "AT&T": "T",
    "ベライゾン・コミュニケーションズ": "VZ",
    "Groupon": "GRPN",
    "ブロック(旧スクエア)": "SQ",
    "ペイパル": "PYPL",
    "ストラテジー（旧マイクロストラテジー）": "MSTR",
    "ストラテジー（旧ﾏｲｸﾛｽﾄﾗﾃｼﾞｰ）": "MSTR",
    "セールスフォース": "CRM",
    "エクソン・モービル": "XOM",
    "ハリバートン": "HAL",
    "シェブロン": "CVX",
    "ファイザー": "PFE",
    "メルク": "MRK",
    "デュポン": "DD",
    "アムジェン": "AMGN",
    "ダウケミカル": "DOW",
    "デルタ航空": "DAL",
    "フォード・モーター": "F",
    "GM": "GM",
    "テスラ": "TSLA",
    "ボーイング": "BA",
    "RTX(旧レイセオン・テクノロジーズ)": "RTX",
    "ハウメット・エアロスペース": "HWM",
    "ハネウェル・インターナショナル": "HON",
}

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


def add_ticker_symbols(rows: list[dict[str, str]]) -> None:
    missing: list[tuple[int, str, str, str, str]] = []
    for row_number, row in enumerate(rows, start=2):
        symbol = infer_ticker_symbol(row)
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


def infer_ticker_symbol(row: dict[str, str]) -> str:
    match = UPPERCASE_UNDERLYING.match(row.get("underlying_asset_exchange", ""))
    if match:
        return match.group(1).strip()
    broker_symbol = BROKER_SYMBOLS.get((row["broker"], row["instrument_name"]))
    if broker_symbol:
        return broker_symbol
    instrument_symbol = INSTRUMENT_SYMBOLS.get(row["instrument_name"])
    if instrument_symbol:
        return instrument_symbol
    if row["broker"] == "GMOクリック証券" and row["category"] == "株式CFD":
        base_name = CLICK_STOCK_EXCHANGE_SUFFIX.sub("", row["instrument_name"])
        return CLICK_STOCK_BASE_SYMBOLS.get(base_name, "")
    return ""


def build_rows(accessed_at: str) -> list[dict[str, str]]:
    rows = parse_click(fetch_events(CLICK_URL), accessed_at)
    rows.extend(parse_rakuten(fetch_events(RAKUTEN_URL), accessed_at))
    if not rows:
        message = "No CFD rows extracted"
        raise SystemExit(message)
    add_ticker_symbols(rows)
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
        "--accessed-at",
        default=datetime.now().astimezone().isoformat(timespec="seconds"),
        help="Timestamp to write to source_accessed_at",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = build_rows(args.accessed_at)
    write_csv(rows, args.output)
    print(f"wrote {args.output} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
