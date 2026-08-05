#!/usr/bin/env python3
"""Insert a worked example into cheating_sheet.md at a stable marker.

This script is intentionally marker-based and does not update Quick Index,
Concept-to-Example Map, Tag Index, or Related Examples. It is designed for fast
exam-review maintenance: one example goes into one auto-insert zone.

Usage examples:

  python scripts/add_worked_example.py \
    --title "Poisson Area Scaling" \
    --tags poisson area-scaling at-least-one \
    --body-file docs/examples/EX-DIST-005-poisson-area-scaling.md

  python scripts/add_worked_example.py \
    --id EX-DIST-005 \
    --title "Poisson Area Scaling" \
    --tags poisson area-scaling at-least-one \
    --body-file docs/examples/EX-DIST-005-poisson-area-scaling.md

By default, if --id is omitted, the script creates the next EX-AUTO-### ID.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHEAT_SHEET = Path("cheating_sheet.md")
INSERT_MARKER = "<!-- AUTO-WORKED-EXAMPLE-INSERT-BEFORE -->"
ZONE_START = "<!-- AUTO-WORKED-EXAMPLE-ZONE-START -->"
ZONE_END = "<!-- AUTO-WORKED-EXAMPLE-ZONE-END -->"
FALLBACK_SECTION = "## 13. Common Traps"


def slugify_id(example_id: str) -> str:
    return example_id.strip().lower()


def normalize_tag(tag: str) -> str:
    tag = tag.strip()
    if not tag:
        raise ValueError("empty tag is not allowed")
    return tag if tag.startswith("#") else f"#{tag}"


def inline_code_tag(tag: str) -> str:
    return f"`{normalize_tag(tag)}`"


def next_auto_id(text: str) -> str:
    used = [int(x) for x in re.findall(r"EX-AUTO-(\d{3,})", text)]
    nxt = max(used, default=0) + 1
    return f"EX-AUTO-{nxt:03d}"


def ensure_zone(text: str) -> str:
    marker_count = text.count(INSERT_MARKER)
    if marker_count > 1:
        raise RuntimeError(f"marker appears {marker_count} times; expected at most 1")
    if marker_count == 1:
        return text

    if FALLBACK_SECTION not in text:
        raise RuntimeError(
            f"missing insert marker and fallback section {FALLBACK_SECTION!r}; "
            "add the marker manually or restore the standard structure"
        )

    zone = f"""\n\n{ZONE_START}\n\n> Auto-inserted worked examples go above the marker below.\n> This zone is maintained by `scripts/add_worked_example.py`.\n\n{INSERT_MARKER}\n\n{ZONE_END}\n\n---\n\n"""
    return text.replace(FALLBACK_SECTION, zone + FALLBACK_SECTION, 1)


def build_block(example_id: str, title: str, tags: list[str], body: str) -> str:
    anchor = slugify_id(example_id)
    tag_text = " ".join(inline_code_tag(t) for t in tags)
    body = body.strip()
    return f"""---\n\n<a id=\"{anchor}\"></a>\n\n### {example_id} — {title}\n\n**Concept Tags:** {tag_text}  \n**Related Concepts:** Not maintained automatically  \n**Inserted By:** `scripts/add_worked_example.py`\n\n{body}\n\n"""


def insert_example(text: str, example_id: str, block: str) -> str:
    anchor = f'<a id="{slugify_id(example_id)}"></a>'
    if example_id in text or anchor in text:
        raise RuntimeError(f"example id already exists: {example_id}")
    if text.count(INSERT_MARKER) != 1:
        raise RuntimeError("insert marker must appear exactly once before insertion")
    return text.replace(INSERT_MARKER, block + INSERT_MARKER, 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Insert a worked example into cheating_sheet.md.")
    parser.add_argument("--cheat-sheet", default=str(CHEAT_SHEET), help="path to cheating_sheet.md")
    parser.add_argument("--id", default=None, help="optional stable Example ID, e.g. EX-DIST-005")
    parser.add_argument("--title", required=True, help="example title")
    parser.add_argument("--tags", nargs="+", required=True, help="tags without or with #")
    parser.add_argument("--body-file", required=True, help="markdown file containing the example body")
    parser.add_argument("--dry-run", action="store_true", help="print the generated block without writing")
    args = parser.parse_args(argv)

    cheat_path = Path(args.cheat_sheet)
    body_path = Path(args.body_file)

    if not cheat_path.exists():
        raise FileNotFoundError(f"cheat sheet not found: {cheat_path}")
    if not body_path.exists():
        raise FileNotFoundError(f"body file not found: {body_path}")

    text = cheat_path.read_text(encoding="utf-8")
    text = ensure_zone(text)

    example_id = args.id or next_auto_id(text)
    if not re.fullmatch(r"EX-[A-Z]+-\d{3,}", example_id):
        raise ValueError("example id must look like EX-DIST-005 or EX-AUTO-001")

    body = body_path.read_text(encoding="utf-8")
    block = build_block(example_id=example_id, title=args.title, tags=args.tags, body=body)
    new_text = insert_example(text, example_id, block)

    if args.dry_run:
        print(block)
        return 0

    cheat_path.write_text(new_text, encoding="utf-8")

    # Post-write sanity checks.
    checked = cheat_path.read_text(encoding="utf-8")
    if checked.count(INSERT_MARKER) != 1:
        raise RuntimeError("post-check failed: marker count is not 1")
    if checked.count(f'<a id="{slugify_id(example_id)}"></a>') != 1:
        raise RuntimeError("post-check failed: example anchor count is not 1")

    print(f"Inserted {example_id} — {args.title} into {cheat_path}")
    print(f"Marker retained: {INSERT_MARKER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
