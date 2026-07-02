r"""Send Slack notifications for AIMS pipeline results via incoming webhook.

Usage:
    # Success
    uv run .agents/skills/market-analysis/scripts/notify_slack.py \
        --artifact data/analysis/2024-01-01.json \
        --report-url https://dceoy.github.io/aims/results/2024-01-01-market-analysis/

    # Failure
    uv run .agents/skills/market-analysis/scripts/notify_slack.py \
        --failure \
        --run-url https://github.com/dceoy/aims/actions/runs/12345 \
        --message "Daily analysis failed"

Reads SLACK_WEBHOOK_URL from the environment.
If SLACK_WEBHOOK_URL is not set, prints a warning and exits 0 (no-op).
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from typing import Any, Final

from aims.reports import market_regime

_TIMEOUT: Final[int] = 15


def build_success_payload(
    artifact: dict[str, Any],
    report_url: str = "",
    *,
    pr_url: str | None = None,
    history: dict[str, Any] | None = None,
) -> dict[str, Any]:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "")
    date_str = generated_at[:10] if isinstance(generated_at, str) else "n/a"
    data_source = str(meta.get("data_source", ""))

    instruments = artifact.get("instruments", [])
    reliable = [i for i in instruments if i.get("is_reliable")]
    regime = market_regime(reliable)

    top3 = sorted(reliable, key=lambda i: float(i.get("score", 0)), reverse=True)[:3]
    signals = ", ".join(
        f"{i.get('symbol', '')} ({float(i.get('score', 0)):.1f})" for i in top3
    )

    freshness_raw = meta.get("data_freshness", {})
    freshness: dict[str, str] = (
        {str(k): str(v) for k, v in freshness_raw.items()}
        if isinstance(freshness_raw, dict)
        else {}
    )
    stale = sorted(sym for sym, val in freshness.items() if val == "n/a")

    regime_emoji = {"Bullish": "📈", "Bearish": "📉", "Neutral": "➡️"}.get(regime, "❓")

    fields: list[dict[str, str]] = [
        {"type": "mrkdwn", "text": f"*Date:* {date_str}"},
        {"type": "mrkdwn", "text": f"*Source:* {data_source}"},
        {"type": "mrkdwn", "text": f"*Regime:* {regime_emoji} {regime}"},
    ]
    if signals:
        fields.append({"type": "mrkdwn", "text": f"*Top signals:* {signals}"})
    if stale:
        fields.append({
            "type": "mrkdwn",
            "text": f"*⚠️ No data:* {', '.join(stale)}",
        })
    if history is not None and history.get("previous_analysis_date") is not None:
        rows = history.get("instruments", [])
        new_top = sorted(str(row["symbol"]) for row in rows if row.get("new_top_k"))
        persistent = sorted(
            str(row["symbol"])
            for row in rows
            if int(row.get("consecutive_top_k_reports", 0)) >= 2
        )
        risk_changes = sorted(
            str(row["symbol"])
            for row in rows
            if row.get("risk_gates_added") or row.get("risk_gates_removed")
        )
        summary = (
            f"*History:* new top: {', '.join(new_top) or 'none'}; "
            f"persistent: {', '.join(persistent) or 'none'}; "
            f"risk changes: {', '.join(risk_changes) or 'none'}"
        )
        fields.append({"type": "mrkdwn", "text": summary})

    coverage_raw = meta.get("coverage")
    if isinstance(coverage_raw, dict):
        fetched = coverage_raw.get("fetched_count")
        attempted = coverage_raw.get("attempted_count")
        ratio = coverage_raw.get("success_ratio")
        if (
            isinstance(fetched, int)
            and isinstance(attempted, int)
            and isinstance(ratio, (int, float))
        ):
            fields.append({
                "type": "mrkdwn",
                "text": (
                    f"*Coverage:* {fetched}/{attempted} ({float(ratio):.0%} success)"
                ),
            })

    if pr_url is not None:
        text = f"AIMS Market Analysis {date_str}: {regime} market. Analysis PR created."
        button_text = "View PR"
        button_url = pr_url
    elif report_url:
        text = f"AIMS Market Analysis {date_str}: {regime} market."
        button_text = "View Report"
        button_url = report_url
    else:
        text = f"AIMS Market Analysis {date_str}: {regime} market."
        button_text = None
        button_url = None

    blocks: list[dict[str, Any]] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "📊 AIMS Market Analysis"},
        },
        {"type": "section", "fields": fields},
    ]
    if button_url is not None:
        blocks.append({
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": button_text},
                    "url": button_url,
                    "style": "primary",
                }
            ],
        })

    return {"text": text, "blocks": blocks}


def build_failure_payload(
    run_url: str,
    message: str = "Daily market analysis failed",
) -> dict[str, Any]:
    text = f"❌ {message}"
    blocks: list[dict[str, Any]] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "❌ AIMS Pipeline Failure"},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*{message}*"},
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "View Run"},
                    "url": run_url,
                    "style": "danger",
                }
            ],
        },
    ]
    return {"text": text, "blocks": blocks}


def send_notification(webhook_url: str, payload: dict[str, Any]) -> None:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as _resp:
        pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--failure",
        action="store_true",
        help="Send a failure notification instead of a success notification",
    )
    parser.add_argument("--history", type=str, help="Path to score-history JSON")
    parser.add_argument(
        "--artifact",
        type=str,
        default=None,
        help="Path to analysis artifact JSON (required in success mode)",
    )
    parser.add_argument(
        "--report-url",
        type=str,
        default=None,
        help="URL to the generated Hugo report page",
    )
    parser.add_argument(
        "--run-url",
        type=str,
        default=None,
        help="URL to the GitHub Actions run (used in failure mode)",
    )
    parser.add_argument(
        "--message",
        type=str,
        default="Daily market analysis failed",
        help="Failure message (used in failure mode)",
    )
    parser.add_argument(
        "--pr-url",
        type=str,
        default=None,
        help="URL to the analysis pull request (used in success mode)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "")
    if not webhook_url:
        print("WARNING: SLACK_WEBHOOK_URL not set; skipping notification.")
        return 0

    if args.failure:
        run_url = args.run_url or ""
        payload = build_failure_payload(run_url, args.message)
    else:
        if not args.artifact:
            print("ERROR: --artifact is required in success mode.")
            return 1
        try:
            with open(args.artifact, encoding="utf-8") as fh:  # noqa: PTH123
                artifact: dict[str, Any] = json.load(fh)
        except FileNotFoundError:
            print(f"ERROR: artifact file not found: {args.artifact}")
            return 1
        except json.JSONDecodeError as exc:
            print(f"ERROR: invalid JSON in {args.artifact}: {exc}")
            return 1
        report_url = args.report_url or ""
        history = None
        if args.history:
            try:
                with open(args.history, encoding="utf-8") as fh:  # noqa: PTH123
                    history = json.load(fh)
            except (FileNotFoundError, json.JSONDecodeError) as exc:
                print(f"ERROR: invalid history artifact: {exc}")
                return 1
        payload = build_success_payload(
            artifact, report_url, pr_url=args.pr_url or None, history=history
        )

    try:
        send_notification(webhook_url, payload)
    except urllib.error.URLError as exc:
        print(f"ERROR: failed to send Slack notification: {exc}")
        return 1
    print("Slack notification sent.")
    return 0


SAMPLE_SUCCESS_PAYLOAD: dict[str, Any] = {
    "text": "AIMS Market Analysis 2024-01-01: Bullish market.",
    "blocks": [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "📊 AIMS Market Analysis"},
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": "*Date:* 2024-01-01"},
                {"type": "mrkdwn", "text": "*Source:* stooq"},
                {"type": "mrkdwn", "text": "*Regime:* 📈 Bullish"},
                {"type": "mrkdwn", "text": "*Top signals:* ^SPX (72.5)"},
            ],
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "View Report"},
                    "url": "https://dceoy.github.io/aims/results/2024-01-01-market-analysis/",
                    "style": "primary",
                }
            ],
        },
    ],
}

SAMPLE_FAILURE_PAYLOAD: dict[str, Any] = {
    "text": "❌ Daily market analysis failed",
    "blocks": [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "❌ AIMS Pipeline Failure"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Daily market analysis failed*",
            },
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "View Run"},
                    "url": "https://github.com/dceoy/aims/actions/runs/12345",
                    "style": "danger",
                }
            ],
        },
    ],
}

if __name__ == "__main__":
    raise SystemExit(main())
