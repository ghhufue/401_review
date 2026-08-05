#!/usr/bin/env python3
"""Append a midterm-supplement block to docs/supplements/sample_midterm_2021_knowledge.md.

This script is intentionally separate from scripts/add_worked_example.py.
It does not modify cheating_sheet.md. It only maintains the detailed
knowledge-supplement file used for longer, step-by-step exam explanations.

Usage examples:

  python scripts/add_midterm_supplement.py \
    --id SM21-028 \
    --title "New Topic Title" \
    --tags normal-approximation continuity-correction \
    --body-file /tmp/body.md

  python scripts/add_midterm_supplement.py \
    --title "Auto Numbered Extra Exercise" \
    --tags bayes conditional-probability \
    --body-file /tmp/body.md

If --id is omitted, the script creates the next SM21-### ID found in the
supplement file.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SUPPLEMENT = Path("docs/supplements/sample_midterm_2021_knowledge.md")
INSERT_MARKER = "<!-- AUTO-MIDTERM-SUPPLEMENT-INSERT-BEFORE -->"
ZONE_START = "<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-START -->"
ZONE_END = "<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-END -->"

DEFAULT_HEADER = f"""# VE401 Sample Midterm 2021 - 逐题知识补充

> 这个文件是 `cheating_sheet.md` 之外的详细题目讲解区，用来放每一题的解题步骤、题型识别和涉及知识点。  
> 维护方式：可以手动编辑，也可以用 `scripts/add_midterm_supplement.py` 继续逐题追加。

---

<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-START -->

<!-- AUTO-MIDTERM-SUPPLEMENT-INSERT-BEFORE -->

<!-- AUTO-MIDTERM-SUPPLEMENT-ZONE-END -->
"""


def slugify_id(item_id: str) -> str:
    return item_id.strip().lower()


def normalize_tag(tag: str) -> str:
    tag = tag.strip()
    if not tag:
        raise ValueError("empty tag is not allowed")
    return tag if tag.startswith("#") else f"#{tag}"


def inline_code_tag(tag: str) -> str:
    return f"`{normalize_tag(tag)}`"


def ensure_file(path: Path) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(DEFAULT_HEADER, encoding="utf-8")


def ensure_zone(text: str) -> str:
    marker_count = text.count(INSERT_MARKER)
    if marker_count != 1:
        raise RuntimeError(
            f"insert marker must appear exactly once; found {marker_count}. "
            f"Expected marker: {INSERT_MARKER}"
        )
    if ZONE_START not in text or ZONE_END not in text:
        raise RuntimeError("supplement zone markers are missing")
    return text


def next_auto_id(text: str) -> str:
    used = [int(x) for x in re.findall(r"SM21-(\d{3,})", text)]
    nxt = max(used, default=0) + 1
    return f"SM21-{nxt:03d}"


def build_block(item_id: str, title: str, tags: list[str], body: str) -> str:
    anchor = slugify_id(item_id)
    tag_text = " ".join(inline_code_tag(t) for t in tags)
    body = body.strip()
    return f"""---

<a id=\"{anchor}\"></a>

## {item_id} — {title}

**Concept Tags:** {tag_text}  
**Inserted By:** `scripts/add_midterm_supplement.py`

{body}

"""


def insert_block(text: str, item_id: str, block: str) -> str:
    anchor = f'<a id="{slugify_id(item_id)}"></a>'
    if re.search(rf"^##\s+{re.escape(item_id)}\b", text, flags=re.MULTILINE) or anchor in text:
        raise RuntimeError(f"supplement id already exists: {item_id}")
    return text.replace(INSERT_MARKER, block + INSERT_MARKER, 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Append one detailed exercise block to the sample midterm supplement."
    )
    parser.add_argument("--supplement", default=str(SUPPLEMENT), help="path to supplement markdown file")
    parser.add_argument("--id", default=None, help="optional stable ID, e.g. SM21-028")
    parser.add_argument("--title", required=True, help="exercise title")
    parser.add_argument("--tags", nargs="+", required=True, help="tags without or with #")
    parser.add_argument("--body-file", required=True, help="markdown file containing the explanation body")
    parser.add_argument("--dry-run", action="store_true", help="print generated block without writing")
    args = parser.parse_args(argv)

    supplement_path = Path(args.supplement)
    body_path = Path(args.body_file)

    ensure_file(supplement_path)
    if not body_path.exists():
        raise FileNotFoundError(f"body file not found: {body_path}")

    text = supplement_path.read_text(encoding="utf-8")
    text = ensure_zone(text)

    item_id = args.id or next_auto_id(text)
    if not re.fullmatch(r"SM21-\d{3,}", item_id):
        raise ValueError("id must look like SM21-028")

    body = body_path.read_text(encoding="utf-8")
    block = build_block(item_id=item_id, title=args.title, tags=args.tags, body=body)
    new_text = insert_block(text, item_id, block)

    if args.dry_run:
        print(block)
        return 0

    supplement_path.write_text(new_text, encoding="utf-8")

    checked = supplement_path.read_text(encoding="utf-8")
    if checked.count(INSERT_MARKER) != 1:
        raise RuntimeError("post-check failed: marker count is not 1")
    if checked.count(f'<a id="{slugify_id(item_id)}"></a>') != 1:
        raise RuntimeError("post-check failed: item anchor count is not 1")

    print(f"Inserted {item_id} — {args.title} into {supplement_path}")
    print(f"Marker retained: {INSERT_MARKER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
