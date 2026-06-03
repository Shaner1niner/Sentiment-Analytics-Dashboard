from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
}

LOCAL_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCED_BLOCK_PATTERN = re.compile(r"```.*?```", re.DOTALL)

SENSITIVE_PATTERNS = [
    (re.compile(r"(?i)\b(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]"), "possible secret assignment"),
    (re.compile(r"(?i)\bpostgres(?:ql)?://"), "possible database URL"),
    (re.compile(r"(?i)\bmysql://"), "possible database URL"),
    (re.compile(r"(?i)\bmongodb(?:\+srv)?://"), "possible database URL"),
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"), "private key material"),
]

EXPECTED_SQL_ROLLUP_FIELDS = [
    "date",
    "asset",
    "avg_sentiment_score",
    "total_mentions",
    "avg_engagement_score",
    "close_price",
    "volume_index",
    "return_1d",
    "volatility_bucket",
    "narrative_state",
]


def iter_files(pattern: str) -> list[Path]:
    results: list[Path] = []
    for path in ROOT.rglob(pattern):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            results.append(path)
    return sorted(results)


def strip_fenced_blocks(text: str) -> str:
    return FENCED_BLOCK_PATTERN.sub("", text)


def normalize_markdown_target(raw_target: str) -> str:
    target = raw_target.strip()

    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]

    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    target = target.split("#", 1)[0]
    return unquote(target.strip())


def check_markdown_local_links() -> list[str]:
    failures: list[str] = []

    for md_path in iter_files("*.md"):
        text = strip_fenced_blocks(md_path.read_text(encoding="utf-8"))
        for match in LOCAL_LINK_PATTERN.finditer(text):
            target = normalize_markdown_target(match.group(1))

            if not target:
                continue
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue

            candidate = (md_path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{md_path.relative_to(ROOT)} links outside repo: {target}")
                continue

            if not candidate.exists():
                failures.append(f"{md_path.relative_to(ROOT)} has missing local link/image: {target}")

    return failures


def extract_dictionary_section(dictionary_text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## `{re.escape(heading)}`\s*$([\s\S]*?)(?=^## |\Z)",
        re.MULTILINE,
    )
    match = pattern.search(dictionary_text)
    return match.group(1) if match else ""


def extract_backtick_fields_from_table(section_text: str) -> set[str]:
    fields: set[str] = set()
    for line in section_text.splitlines():
        match = re.match(r"^\|\s*`([^`]+)`\s*\|", line)
        if match:
            fields.add(match.group(1))
    return fields


def check_sample_data_dictionary() -> list[str]:
    failures: list[str] = []
    dictionary_path = ROOT / "docs" / "data_dictionary_sanitized.md"

    if not dictionary_path.exists():
        return ["Missing docs/data_dictionary_sanitized.md"]

    dictionary_text = dictionary_path.read_text(encoding="utf-8")

    for csv_path in sorted((ROOT / "sample_data").glob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8") as handle:
            headers = next(csv.reader(handle))

        section = extract_dictionary_section(dictionary_text, csv_path.name)
        if not section:
            failures.append(f"Data dictionary missing section for {csv_path.name}")
            continue

        documented_fields = extract_backtick_fields_from_table(section)
        missing_fields = [header for header in headers if header not in documented_fields]
        if missing_fields:
            failures.append(
                f"Data dictionary section for {csv_path.name} missing fields: {', '.join(missing_fields)}"
            )

    sql_section = extract_dictionary_section(
        dictionary_text,
        "sql_examples/sentiment_dashboard_rollup_sample.sql",
    )
    if not sql_section:
        failures.append("Data dictionary missing SQL rollup output section")
    else:
        documented_sql_fields = extract_backtick_fields_from_table(sql_section)
        missing_sql_fields = [
            field for field in EXPECTED_SQL_ROLLUP_FIELDS if field not in documented_sql_fields
        ]
        if missing_sql_fields:
            failures.append(
                "SQL rollup dictionary section missing fields: "
                + ", ".join(missing_sql_fields)
            )

    return failures


def check_methodology_sample_contract() -> list[str]:
    failures: list[str] = []
    methodology_path = ROOT / "docs" / "dashboard_methodology.md"

    if not methodology_path.exists():
        return ["Missing docs/dashboard_methodology.md"]

    text = methodology_path.read_text(encoding="utf-8")

    if "- `source_count`" in text:
        failures.append("dashboard_methodology.md still lists public sample field `source_count`")

    if "- `volume`" in text:
        failures.append("dashboard_methodology.md still lists public sample field `volume` instead of `volume_index`")

    if "- `volume_index`" not in text:
        failures.append("dashboard_methodology.md does not list `volume_index`")

    return failures


def check_sensitive_literals() -> list[str]:
    failures: list[str] = []

    for path in iter_files("*"):
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"}:
            continue
        if path.name == "check_public_repo_contract.py":
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for pattern, label in SENSITIVE_PATTERNS:
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)} contains {label}")

    return failures


def main() -> int:
    checks = {
        "markdown local links/images": check_markdown_local_links(),
        "sample data dictionary": check_sample_data_dictionary(),
        "methodology sample contract": check_methodology_sample_contract(),
        "sensitive literal scan": check_sensitive_literals(),
    }

    failed = False

    for name, failures in checks.items():
        if failures:
            failed = True
            print(f"FAIL: {name}")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print(f"OK: {name}")

    if failed:
        print("\nPublic repo contract check failed.")
        return 1

    print("\nPublic repo contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
