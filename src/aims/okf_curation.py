r"""Propose durable OKF theme promotions from accumulated qualitative artifacts.

Deterministic helper behind the ``aims-okf-curator`` skill's periodic
curation pass (#96): it scans committed ``data/qualitative/*.json``
artifacts, clusters recurring market themes by title-token overlap, and
renders a Markdown **proposal** — promotion candidates with dated artifact
and evidence citations plus a ready-to-edit concept skeleton, supporting
per-instrument stance streaks, and retirement candidates among existing
``qualitative-theme`` OKF concepts.

The output is advisory only. Promotion and retirement always go through a
human-reviewed pull request (never auto-merged), a log entry in
``okf/logs/log.md`` (including "no promotions" passes), shadow-content
regeneration via ``tools/okf_hugo_adapter.py``, and a Hugo build. Numeric
market facts stay pointers into ``data/analysis/`` — the skeleton reminds
the curator not to assert them as truth in OKF prose.

Usage:
    uv run .agents/skills/aims-okf-curator/scripts/curate_themes.py \
        --qualitative-dir data/qualitative \
        --concepts-dir okf/concepts
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Final, NamedTuple

import yaml

from aims.okf_hugo import split_front_matter

MIN_DISTINCT_DATES: Final[int] = 3
MIN_SPAN_DAYS: Final[int] = 14
RETIREMENT_DAYS: Final[int] = 60
JACCARD_THRESHOLD: Final[float] = 0.5
THEME_TAG: Final[str] = "qualitative-theme"

_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TOKEN_RE: Final[re.Pattern[str]] = re.compile(r"[^a-z0-9]+")
_STOPWORDS: Final[frozenset[str]] = frozenset({
    "amid",
    "and",
    "are",
    "for",
    "from",
    "his",
    "her",
    "into",
    "its",
    "off",
    "onto",
    "our",
    "over",
    "the",
    "their",
    "under",
    "via",
    "with",
})


class ThemeOccurrence(NamedTuple):
    """One dated appearance of a theme in a qualitative artifact."""

    date: str
    title: str
    citations: tuple[str, ...]
    source: str


@dataclass
class ThemeCluster:
    """Recurring theme candidate anchored on its first occurrence's tokens."""

    tokens: frozenset[str]
    occurrences: list[ThemeOccurrence] = field(default_factory=list)

    @property
    def dates(self) -> list[str]:
        return sorted({occurrence.date for occurrence in self.occurrences})

    @property
    def span_days(self) -> int:
        dates = self.dates
        return (date.fromisoformat(dates[-1]) - date.fromisoformat(dates[0])).days

    @property
    def latest_title(self) -> str:
        return self.occurrences[-1].title


def theme_tokens(title: str) -> frozenset[str]:
    """Significant lowercase tokens of a theme title (stopwords/digits out)."""
    return frozenset(
        word
        for word in _TOKEN_RE.split(title.lower())
        if len(word) >= 3 and word not in _STOPWORDS and not word.isdigit()
    )


def _jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def cluster_themes(
    artifacts: list[tuple[str, dict[str, Any]]],
) -> tuple[list[ThemeCluster], list[str]]:
    """Greedily cluster market themes across artifacts by token overlap.

    Artifacts whose market narrative was withheld by the #93 gates are
    skipped: their themes never rendered and should not seed durable
    knowledge.
    """
    clusters: list[ThemeCluster] = []
    warnings: list[str] = []
    for source, artifact in sorted(artifacts, key=lambda pair: _artifact_date(pair[1])):
        meta = artifact.get("metadata", {})
        when = _artifact_date(artifact)
        if meta.get("gates", {}).get("market_narrative_withheld"):
            warnings.append(f"{source}: market narrative withheld by gates; skipped")
            continue
        for theme in artifact.get("market", {}).get("themes", []):
            title = str(theme.get("title", ""))
            tokens = theme_tokens(title)
            if not tokens:
                warnings.append(f"{source}: theme {title!r} has no significant tokens")
                continue
            occurrence = ThemeOccurrence(
                date=when,
                title=title,
                citations=tuple(str(c) for c in theme.get("citations", [])),
                source=source,
            )
            for cluster in clusters:
                if _jaccard(cluster.tokens, tokens) >= JACCARD_THRESHOLD:
                    cluster.occurrences.append(occurrence)
                    break
            else:
                clusters.append(ThemeCluster(tokens=tokens, occurrences=[occurrence]))
    return clusters, warnings


def promotion_candidates(clusters: list[ThemeCluster]) -> list[ThemeCluster]:
    """Clusters recurring on ≥3 distinct dates spanning ≥14 days."""
    return [
        cluster
        for cluster in clusters
        if len(cluster.dates) >= MIN_DISTINCT_DATES
        and cluster.span_days >= MIN_SPAN_DAYS
    ]


def stance_streaks(
    artifacts: list[tuple[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    """Instruments holding one stance on ≥3 dates spanning ≥14 days (ungated)."""
    dates_by_key: dict[tuple[str, str, str], set[str]] = {}
    for _source, artifact in artifacts:
        when = _artifact_date(artifact)
        for entry in artifact.get("instruments", []):
            if entry.get("qualitative_gates"):
                continue
            key = (
                str(entry.get("canonical_id", "")),
                str(entry.get("symbol", "")),
                str(entry.get("stance", "")),
            )
            dates_by_key.setdefault(key, set()).add(when)
    streaks: list[dict[str, Any]] = []
    for (canonical_id, symbol, stance), when_set in sorted(dates_by_key.items()):
        dates = sorted(when_set)
        span = (date.fromisoformat(dates[-1]) - date.fromisoformat(dates[0])).days
        if len(dates) >= MIN_DISTINCT_DATES and span >= MIN_SPAN_DAYS:
            streaks.append({
                "canonical_id": canonical_id,
                "symbol": symbol,
                "stance": stance,
                "dates": dates,
            })
    return streaks


class ThemeConcept(NamedTuple):
    """Existing OKF concept tagged as a promoted qualitative theme."""

    path: str
    title: str
    tokens: frozenset[str]


def load_theme_concepts(
    concepts_dir: Path,
) -> tuple[list[ThemeConcept], list[str]]:
    """Parse ``qualitative-theme``-tagged concepts and their theme tokens."""
    concepts: list[ThemeConcept] = []
    warnings: list[str] = []
    if not concepts_dir.is_dir():
        warnings.append(f"{concepts_dir}: concepts directory not found")
        return concepts, warnings
    for path in sorted(concepts_dir.glob("*.md")):
        try:
            metadata, _body, _has = split_front_matter(path)
        except (yaml.YAMLError, TypeError) as exc:
            warnings.append(f"{path}: unreadable front matter: {exc}")
            continue
        tags = metadata.get("tags")
        if not isinstance(tags, list) or THEME_TAG not in [str(t) for t in tags]:
            continue
        raw_tokens = metadata.get("theme_tokens")
        if not isinstance(raw_tokens, list) or not raw_tokens:
            warnings.append(
                f"{path}: tagged {THEME_TAG!r} but has no 'theme_tokens' front"
                " matter; cannot assess recurrence"
            )
            continue
        concepts.append(
            ThemeConcept(
                path=path.as_posix(),
                title=str(metadata.get("title", path.stem)),
                tokens=frozenset(str(token) for token in raw_tokens),
            )
        )
    return concepts, warnings


def retirement_candidates(
    concepts: list[ThemeConcept],
    clusters: list[ThemeCluster],
    as_of: str,
) -> list[dict[str, Any]]:
    """Theme concepts unseen in any artifact for over ``RETIREMENT_DAYS``."""
    candidates: list[dict[str, Any]] = []
    for concept in concepts:
        last_seen: str | None = None
        for cluster in clusters:
            for occurrence in cluster.occurrences:
                if _jaccard(
                    concept.tokens, theme_tokens(occurrence.title)
                ) >= JACCARD_THRESHOLD and (
                    last_seen is None or occurrence.date > last_seen
                ):
                    last_seen = occurrence.date
        if last_seen is None:
            candidates.append({
                "path": concept.path,
                "title": concept.title,
                "last_seen": None,
            })
            continue
        stale_days = (date.fromisoformat(as_of) - date.fromisoformat(last_seen)).days
        if stale_days > RETIREMENT_DAYS:
            candidates.append({
                "path": concept.path,
                "title": concept.title,
                "last_seen": last_seen,
            })
    return candidates


def _slug(title: str) -> str:
    slug = _TOKEN_RE.sub("-", title.lower()).strip("-")
    return slug[:60].rstrip("-") or "theme"


def concept_skeleton(cluster: ThemeCluster, as_of: str) -> str:
    """Ready-to-edit OKF concept draft for a promotion candidate."""
    title = cluster.latest_title
    slug = _slug(title)
    tokens = ", ".join(sorted(cluster.tokens))
    observed = [
        f'- `{occurrence.source}` ({occurrence.date}): "{occurrence.title}"'
        f" — evidence: {', '.join(occurrence.citations) or 'none'}"
        for occurrence in cluster.occurrences
    ]
    sources = sorted({occurrence.source for occurrence in cluster.occurrences})
    citations = [f"- `{source}`" for source in sources]
    return "\n".join([
        "---",
        f"id: okf/concepts/theme-{slug}",
        f"title: {title}",
        (
            "description: TODO — one-sentence qualitative description of the"
            " durable driver."
        ),
        "type: concept",
        f"tags: [{THEME_TAG}]",
        f"timestamp: {as_of}T00:00:00Z",
        "resource:",
        f"  path: okf/concepts/theme-{slug}.md",
        "  source: repository",
        "status: proposed",
        f"theme_tokens: [{tokens}]",
        "---",
        "",
        f"# {title}",
        "",
        ("TODO — describe the recurring driver qualitatively. Never assert"),
        ("scores, ranks, dates, prices, risk gates, or data availability as"),
        ("truth in prose; numeric facts stay pointers into `data/analysis/`."),
        "",
        "## Observed in qualitative artifacts",
        "",
        *observed,
        "",
        "# Citations",
        "",
        *citations,
    ])


def _artifact_date(artifact: dict[str, Any]) -> str:
    when = artifact.get("metadata", {}).get("analysis_date")
    if not isinstance(when, str) or not _DATE_RE.match(when):
        msg = "qualitative artifact has no valid metadata.analysis_date"
        raise ValueError(msg)
    return when


def _candidate_section(candidates: list[ThemeCluster], as_of: str) -> list[str]:
    if not candidates:
        return [
            (
                "_No recurring themes meet the promotion criteria"
                f" (≥{MIN_DISTINCT_DATES} distinct dates spanning"
                f' ≥{MIN_SPAN_DAYS} days). Record a "no promotions" pass in'
                " `okf/logs/log.md`._"
            )
        ]
    lines: list[str] = []
    for cluster in candidates:
        lines.extend((
            f"### {cluster.latest_title}",
            "",
            (
                f"Recurs on {len(cluster.dates)} distinct dates spanning"
                f" {cluster.span_days} days:"
            ),
            "",
        ))
        lines.extend(
            f'- {occurrence.date} — "{occurrence.title}"'
            f" (`{occurrence.source}`; evidence:"
            f" {', '.join(occurrence.citations) or 'none'})"
            for occurrence in cluster.occurrences
        )
        lines.extend(("", "Draft concept skeleton (edit before committing):", ""))
        lines.extend(("```", concept_skeleton(cluster, as_of), "```", ""))
    return lines[:-1] if not lines[-1] else lines


def render_proposal(
    artifacts: list[tuple[str, dict[str, Any]]],
    concepts_dir: Path,
    as_of: str | None,
) -> str:
    """Render the deterministic curation-proposal Markdown."""
    clusters, warnings = cluster_themes(artifacts)
    concepts, concept_warnings = load_theme_concepts(concepts_dir)
    warnings.extend(concept_warnings)
    candidates = promotion_candidates(clusters)
    streaks = stance_streaks(artifacts)

    dates = sorted({_artifact_date(artifact) for _source, artifact in artifacts})
    effective_as_of = as_of or (dates[-1] if dates else None)
    header = f"# OKF qualitative theme curation proposal — {effective_as_of or 'n/a'}"
    if dates:
        scope = (
            f"Deterministic pass over {len(artifacts)} qualitative artifact(s)"
            f" from {dates[0]} to {dates[-1]}."
        )
    else:
        scope = (
            "Deterministic pass over 0 qualitative artifacts — none have"
            " accumulated yet; this is a recorded empty pass."
        )
    lines = [
        header,
        "",
        scope + " Promotion is a human-reviewed pull request only — never auto-merged.",
        "",
        "## Promotion candidates",
        "",
        *_candidate_section(candidates, effective_as_of or "1970-01-01"),
        "",
        "## Per-instrument stance streaks (supporting context)",
        "",
    ]
    if streaks:
        lines.extend(
            f"- **{streak['symbol']}** ({streak['canonical_id']}) held"
            f" `{streak['stance']}` on {len(streak['dates'])} dates"
            f" ({streak['dates'][0]} to {streak['dates'][-1]})"
            for streak in streaks
        )
    else:
        lines.append(
            "_No instrument held a single stance on"
            f" ≥{MIN_DISTINCT_DATES} dates spanning ≥{MIN_SPAN_DAYS} days._"
        )
    lines.extend(("", "## Retirement candidates", ""))
    if effective_as_of is None:
        lines.append(
            "_No qualitative artifacts available — recurrence of existing"
            " theme concepts cannot be assessed; skipping._"
        )
    else:
        retirements = retirement_candidates(concepts, clusters, effective_as_of)
        if retirements:
            lines.extend(
                f"- `{item['path']}` — {item['title']}: last seen"
                f" {item['last_seen'] or 'never in the loaded artifacts'}"
                f" (archive after {RETIREMENT_DAYS} days without recurrence)"
                for item in retirements
            )
        else:
            lines.append("_No theme concepts are due for retirement._")
    if warnings:
        lines.extend(("", "## Warnings", ""))
        lines.extend(f"- {warning}" for warning in sorted(warnings))
    lines.extend((
        "",
        "## Curation checklist",
        "",
        (
            "- [ ] Review candidates; edit a draft into"
            " `okf/concepts/theme-<slug>.md` (cite dated artifacts; numeric"
            " facts stay pointers into `data/analysis/`)"
        ),
        '- [ ] Record this pass — including "no promotions" — in `okf/logs/log.md`',
        (
            "- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst"
            " content/knowledge --clean`"
        ),
        (
            "- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst"
            " content/knowledge --check`"
        ),
        "- [ ] `hugo --gc --minify`",
        "- [ ] Open a human-reviewed PR — never auto-merge OKF changes",
    ))
    return "\n".join(lines) + "\n"


def load_artifacts(
    qualitative_dir: Path,
) -> tuple[list[tuple[str, dict[str, Any]]], list[str]]:
    """Load qualitative artifacts, skipping unreadable files with warnings."""
    artifacts: list[tuple[str, dict[str, Any]]] = []
    warnings: list[str] = []
    if not qualitative_dir.is_dir():
        return artifacts, warnings
    for path in sorted(qualitative_dir.glob("*.json")):
        try:
            with path.open(encoding="utf-8") as stream:
                artifact = json.load(stream)
            _artifact_date(artifact)
        except (json.JSONDecodeError, ValueError) as exc:
            warnings.append(f"{path.as_posix()}: skipped unreadable artifact: {exc}")
            continue
        artifacts.append((path.as_posix(), artifact))
    return artifacts, warnings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--qualitative-dir", type=Path, default=Path("data/qualitative")
    )
    parser.add_argument("--concepts-dir", type=Path, default=Path("okf/concepts"))
    parser.add_argument(
        "--as-of",
        default=None,
        help="Retirement reference date (default: latest artifact date)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write the proposal to a file instead of stdout",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.as_of is not None and not _DATE_RE.match(args.as_of):
        print(f"ERROR: --as-of {args.as_of!r} is not a YYYY-MM-DD date")
        return 1
    artifacts, load_warnings = load_artifacts(args.qualitative_dir)
    for warning in load_warnings:
        print(f"WARNING: {warning}")
    proposal = render_proposal(artifacts, args.concepts_dir, args.as_of)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(proposal, encoding="utf-8")
        print(f"Curation proposal written to {args.output}")
    else:
        print(proposal, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
