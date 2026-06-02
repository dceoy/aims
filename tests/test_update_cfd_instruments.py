from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Self

import pytest

if TYPE_CHECKING:
    from types import ModuleType

    from pytest_mock import MockerFixture

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "update-cfd-instruments"
    / "scripts"
    / "update_cfd_instruments.py"
)


@pytest.fixture(scope="module")
def updater() -> ModuleType:
    spec = importlib.util.spec_from_file_location("update_cfd_instruments", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load update_cfd_instruments.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def table(updater: ModuleType, rows: list[list[str]]) -> tuple[str, list[list[object]]]:
    return "table", [[updater.Cell(text=value) for value in row] for row in rows]


def test_html_parser_collects_headings_tables_spans_and_ignores_scripts(
    updater: ModuleType,
) -> None:
    parser = updater.LineupHTMLParser()

    parser.feed(
        """
        <h2> 株価指数CFD レバレッジ：10倍 </h2>
        <script><h2>ignored</h2><b>also ignored</b></script>
        <style><h3>ignored</h3></style>
        <td>outside a row</td>
        <h3> 詳細 </h3>
        <table>
          <tr><th rowspan="2">銘柄</th><th colspan="2">条件</th></tr>
          <tr><td>通貨</td><td>単位</td></tr>
          <tr><td>日本225</td><td>JPY</td><td>10</td></tr>
        </table>
        """
    )
    parser.close()

    assert parser.events[:2] == [
        ("h2", "株価指数CFD レバレッジ：10倍"),
        ("h3", "詳細"),
    ]
    assert updater.table_matrix(parser.events[2][1]) == [
        ["銘柄", "条件", "条件"],
        ["銘柄", "通貨", "単位"],
        ["日本225", "JPY", "10"],
    ]


def test_html_parser_ignores_nested_events_while_in_ignored_depth(
    updater: ModuleType,
) -> None:
    parser = updater.LineupHTMLParser()
    parser.ignored_depth = 1

    parser.handle_starttag("div", [])
    parser.handle_endtag("div")

    assert parser.events == []
    assert parser.ignored_depth == 1


@pytest.mark.parametrize(
    ("value", "expected"),
    [(None, 1), ("", 1), ("0", 1), ("3", 3), ("bad", 1)],
)
def test_parse_span(updater: ModuleType, value: str | None, expected: int) -> None:
    assert updater.parse_span(value) == expected


def test_clean_empty_and_normalized_text(updater: ModuleType) -> None:
    assert updater.clean(None) == ""
    assert updater.clean(" a\xa0  b\nc ") == "a b c"


def test_table_matrix_handles_empty_input(updater: ModuleType) -> None:
    assert updater.table_matrix([]) == []


def test_parse_click_extracts_instruments_stocks_and_detail_tables(
    updater: ModuleType,
) -> None:
    events = [
        ("h2", "補足"),
        ("h2", "株価指数CFD レバレッジ：10倍"),
        table(
            updater,
            [
                ["CFD銘柄名", "参照原資産/取引所", "呼値", "通貨", "取引単位", "時間"],
                ["日本225", "JPX", "1", "JPY", "10", "8:00-翌6:00"],
                ["", "skip"],
            ],
        ),
        table(
            updater,
            [
                ["価格調整額", "あり"],
                ["金利調整額・権利調整額", "共通"],
                ["銘柄ごとの建玉枚数上限", "上限注記"],
                ["最小取引数量", "1枚"],
                ["源泉徴収税", "対象"],
            ],
        ),
        ("h2", "株式CFD レバレッジ：5倍"),
        ("h3", "米国株"),
        table(
            updater,
            [
                ["業種セクター", "銘柄名", "呼値", "通貨", "取引単位", "時間"],
                ["情報技術", "Apple（NASDAQ）", "0.01", "USD", "1", "24h"],
                ["情報技術", ""],
            ],
        ),
        table(
            updater,
            [
                ["金利調整額", "金利のみ"],
                ["権利調整額", "権利のみ"],
                ["対象外ラベル", "無視"],
            ],
        ),
        ("p", "ignored"),
        table(updater, [["unsupported", "wide", "table"]]),
        table(updater, []),
    ]

    rows = updater.parse_click(events, "2026-01-02T03:04:05+09:00")

    assert rows == [
        {
            **updater.empty_row(),
            "source_accessed_at": "2026-01-02T03:04:05+09:00",
            "broker": "GMOクリック証券",
            "source_url": updater.CLICK_URL,
            "category": "株価指数CFD",
            "section": "株価指数CFD",
            "instrument_name": "日本225",
            "underlying_asset_exchange": "JPX",
            "tick_size": "1",
            "currency": "JPY",
            "trade_unit": "10",
            "trading_hours": "8:00-翌6:00",
            "margin_rate_leverage": "10倍",
            "price_adjustment": "あり",
            "interest_adjustment": "共通",
            "rights_adjustment": "共通",
            "instrument_position_limit_note": "上限注記",
            "minimum_trade_quantity": "1枚",
            "withholding_tax_note": "対象",
        },
        {
            **updater.empty_row(),
            "source_accessed_at": "2026-01-02T03:04:05+09:00",
            "broker": "GMOクリック証券",
            "source_url": updater.CLICK_URL,
            "category": "株式CFD",
            "section": "米国株",
            "sector": "情報技術",
            "instrument_name": "Apple（NASDAQ）",
            "tick_size": "0.01",
            "currency": "USD",
            "trade_unit": "1",
            "trading_hours": "24h",
            "margin_rate_leverage": "5倍",
            "interest_adjustment": "金利のみ",
            "rights_adjustment": "権利のみ",
        },
    ]


def test_parse_rakuten_extracts_valid_tables(updater: ModuleType) -> None:
    events = [
        ("h2", "株価指数"),
        ("p", "ignored"),
        table(updater, [["too short"]]),
        table(
            updater,
            [
                ["header"],
                [
                    "銘柄名",
                    "参照原資産",
                    "通貨",
                    "呼値",
                    "表示例",
                    "最小単位",
                    "1枚価値",
                    "証拠金率",
                    "注文上限",
                    "銘柄建玉上限",
                    "口座建玉上限",
                ],
                [
                    "米国500",
                    "CME",
                    "USD",
                    "0.1",
                    "5000.0",
                    "1",
                    "指数x1",
                    "10倍",
                    "100",
                    "1000",
                    "5000",
                ],
                ["", "skip"],
            ],
        ),
    ]

    rows = updater.parse_rakuten(events, "now")

    assert rows == [
        {
            **updater.empty_row(),
            "source_accessed_at": "now",
            "broker": "楽天証券",
            "source_url": updater.RAKUTEN_URL,
            "category": "株価指数",
            "section": "株価指数",
            "instrument_name": "米国500",
            "underlying_asset_exchange": "CME",
            "currency": "USD",
            "tick_size": "0.1",
            "price_display_example": "5000.0",
            "minimum_trade_unit": "1",
            "contract_value_per_lot": "指数x1",
            "margin_rate_leverage": "10倍",
            "max_order_quantity": "100",
            "instrument_position_limit": "1000",
            "account_position_limit": "5000",
        }
    ]


def test_get_cell_returns_empty_for_missing_values(updater: ModuleType) -> None:
    assert updater.get_cell(["first"], 0) == "first"
    assert updater.get_cell(["first"], 1) == ""


@pytest.mark.parametrize(
    ("row", "expected"),
    [
        ({"underlying_asset_exchange": "NASDAQ / Apple Inc."}, "NASDAQ"),
        (
            {
                "broker": "楽天証券",
                "category": "株価指数",
                "instrument_name": "米国500",
                "underlying_asset_exchange": "",
            },
            "ES",
        ),
        (
            {
                "broker": "GMOクリック証券",
                "category": "商品CFD",
                "instrument_name": "金スポット",
                "underlying_asset_exchange": "",
            },
            "XAU",
        ),
        (
            {
                "broker": "GMOクリック証券",
                "category": "株式CFD",
                "instrument_name": "Apple（NASDAQ）",
                "underlying_asset_exchange": "",
            },
            "AAPL",
        ),
        (
            {
                "broker": "GMOクリック証券",
                "category": "株式CFD",
                "instrument_name": "未知（NASDAQ）",
                "underlying_asset_exchange": "",
            },
            "",
        ),
        (
            {
                "broker": "楽天証券",
                "category": "その他",
                "instrument_name": "未知",
                "underlying_asset_exchange": "",
            },
            "",
        ),
    ],
)
def test_infer_ticker_symbol(
    updater: ModuleType, row: dict[str, str], expected: str
) -> None:
    assert updater.infer_ticker_symbol(row) == expected


def test_add_ticker_symbols_updates_rows_and_reports_missing(
    updater: ModuleType, capsys: pytest.CaptureFixture[str]
) -> None:
    rows = [
        {
            **updater.empty_row(),
            "broker": "楽天証券",
            "category": "株価指数",
            "instrument_name": "米国500",
            "underlying_asset_exchange": "",
        },
        {
            **updater.empty_row(),
            "broker": "楽天証券",
            "category": "その他",
            "instrument_name": "未知",
            "underlying_asset_exchange": "不明",
        },
    ]

    with pytest.raises(SystemExit) as exc_info:
        updater.add_ticker_symbols(rows)

    assert exc_info.value.code == 1
    assert rows[0]["ticker_symbol"] == "ES"
    assert rows[1]["ticker_symbol"] == ""
    assert "Missing ticker_symbol mappings:" in capsys.readouterr().out


def test_add_ticker_symbols_succeeds_without_missing(updater: ModuleType) -> None:
    rows = [
        {
            **updater.empty_row(),
            "broker": "楽天証券",
            "category": "株価指数",
            "instrument_name": "米国500",
            "underlying_asset_exchange": "",
        }
    ]

    updater.add_ticker_symbols(rows)

    assert rows[0]["ticker_symbol"] == "ES"


def test_build_rows_fetches_parses_and_requires_rows(
    updater: ModuleType, mocker: MockerFixture
) -> None:
    mocker.patch.object(
        updater,
        "fetch_events",
        side_effect=[["click events"], ["rakuten events"], ["empty"], ["empty"]],
    )
    mocker.patch.object(
        updater,
        "parse_click",
        side_effect=[
            [{"broker": "GMOクリック証券", "instrument_name": "日本225"}],
            [],
        ],
    )
    mocker.patch.object(
        updater,
        "parse_rakuten",
        side_effect=[
            [{"broker": "楽天証券", "instrument_name": "米国500"}],
            [],
        ],
    )
    add_symbols = mocker.patch.object(updater, "add_ticker_symbols")

    rows = updater.build_rows("now")

    assert rows == [
        {"broker": "GMOクリック証券", "instrument_name": "日本225"},
        {"broker": "楽天証券", "instrument_name": "米国500"},
    ]
    add_symbols.assert_called_once_with(rows)

    with pytest.raises(SystemExit, match="No CFD rows extracted"):
        updater.build_rows("now")


def test_fetch_events_uses_request_and_parses_response(
    updater: ModuleType, mocker: MockerFixture
) -> None:
    class Response:
        def __enter__(self) -> Self:
            return self

        def __exit__(self, *args: object) -> None:
            return None

        @staticmethod
        def read() -> bytes:
            return b"<h2>Heading</h2><table><tr><td>A</td></tr></table>"

    urlopen = mocker.patch.object(
        updater.urllib.request, "urlopen", return_value=Response()
    )

    assert updater.fetch_events("https://example.test") == [
        ("h2", "Heading"),
        ("table", [[updater.Cell("A")]]),
    ]
    request = urlopen.call_args.args[0]
    assert request.full_url == "https://example.test"
    assert request.headers["User-agent"] == "Mozilla/5.0"
    assert urlopen.call_args.kwargs == {"timeout": 30}


def test_write_csv_creates_parent_and_writes_field_order(
    updater: ModuleType, tmp_path: Path
) -> None:
    output = tmp_path / "nested" / "rows.csv"
    row = updater.empty_row()
    row.update({"broker": "楽天証券", "instrument_name": "米国500"})

    updater.write_csv([row], output)

    with output.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        assert reader.fieldnames == updater.FIELDS
        assert list(reader) == [row]


def test_parse_args_uses_defaults_and_custom_output(
    updater: ModuleType, mocker: MockerFixture
) -> None:
    mocker.patch.object(sys, "argv", ["update_cfd_instruments.py"])
    default_args = updater.parse_args()

    assert default_args.output == updater.DEFAULT_OUTPUT
    assert default_args.accessed_at

    mocker.patch.object(
        sys,
        "argv",
        [
            "update_cfd_instruments.py",
            "--output",
            "custom.csv",
            "--accessed-at",
            "now",
        ],
    )
    custom_args = updater.parse_args()

    assert custom_args.output == Path("custom.csv")
    assert custom_args.accessed_at == "now"


def test_main_builds_writes_and_prints(
    updater: ModuleType, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    args = mocker.Mock(accessed_at="now", output=Path("out.csv"))
    rows = [{"instrument_name": "米国500"}, {"instrument_name": "日本225"}]
    mocker.patch.object(updater, "parse_args", return_value=args)
    mocker.patch.object(updater, "build_rows", return_value=rows)
    write_csv = mocker.patch.object(updater, "write_csv")

    updater.main()

    write_csv.assert_called_once_with(rows, Path("out.csv"))
    assert capsys.readouterr().out == "wrote out.csv (2 rows)\n"
