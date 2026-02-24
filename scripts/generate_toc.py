#!/usr/bin/env python3
"""Generate or refresh Markdown table-of-contents blocks.

Updates content under a ``## Table of Contents`` heading for Markdown files.
If a file does not contain that heading, the TOC is inserted after the first H1.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TOC_HEADING_RE = re.compile(r"^(#{2,6})\s+Table of Contents\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE_RE = re.compile(r"^\s*```")


@dataclass
class Heading:
    level: int
    text: str
    anchor: str


def iter_markdown_files(paths: list[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            yield path
            continue
        if path.is_dir():
            for file_path in sorted(path.rglob("*.md")):
                yield file_path


def strip_inline_code(text: str) -> str:
    return re.sub(r"`([^`]*)`", r"\1", text)


def strip_links(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def clean_heading_text(text: str) -> str:
    text = strip_links(strip_inline_code(text))
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\\", "")
    return " ".join(text.split()).strip()


def slugify(text: str, counts: dict[str, int]) -> str:
    slug = clean_heading_text(text).lower()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    if not slug:
        slug = "section"
    n = counts.get(slug, 0)
    counts[slug] = n + 1
    return slug if n == 0 else f"{slug}-{n}"


def collect_headings(content: str, min_level: int, max_level: int) -> list[Heading]:
    headings: list[Heading] = []
    in_fence = False
    slug_counts: dict[str, int] = {}

    for line in content.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        text = match.group(2).strip()
        if TOC_HEADING_RE.match(line):
            continue
        if not (min_level <= level <= max_level):
            continue
        if not text:
            continue

        headings.append(Heading(level=level, text=clean_heading_text(text), anchor=slugify(text, slug_counts)))
    return headings


def build_toc(headings: list[Heading], min_level: int) -> str:
    if not headings:
        return "<!-- No headings found for TOC -->"

    lines: list[str] = []
    for heading in headings:
        indent = "  " * max(0, heading.level - min_level)
        lines.append(f"{indent}- [{heading.text}](#{heading.anchor})")
    return "\n".join(lines)


def replace_or_insert_toc(content: str, toc_body: str) -> tuple[str, bool]:
    lines = content.splitlines()
    for i, line in enumerate(lines):
        match = TOC_HEADING_RE.match(line)
        if not match:
            continue

        toc_level = len(match.group(1))
        end = i + 1
        while end < len(lines):
            candidate = lines[end]
            heading_match = HEADING_RE.match(candidate)
            if heading_match and len(heading_match.group(1)) <= toc_level:
                break
            end += 1

        replacement = [lines[i], toc_body, ""]
        new_lines = lines[:i] + replacement + lines[end:]
        return "\n".join(new_lines).rstrip() + "\n", True

    for i, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 1:
            insert_at = i + 1
            block = ["", "## Table of Contents", toc_body, ""]
            new_lines = lines[:insert_at] + block + lines[insert_at:]
            return "\n".join(new_lines).rstrip() + "\n", True

    return content, False


def process_file(path: Path, min_level: int, max_level: int, check_only: bool) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    headings = collect_headings(original, min_level=min_level, max_level=max_level)
    toc_body = build_toc(headings, min_level=min_level)
    updated, changed_possible = replace_or_insert_toc(original, toc_body)

    if not changed_possible:
        return False, "no-h1"

    changed = updated != original
    if changed and not check_only:
        path.write_text(updated, encoding="utf-8")
    return changed, "updated" if changed else "unchanged"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate/update Markdown TOC blocks under '## Table of Contents'."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["docs"],
        help="Markdown files or directories to process (default: docs)",
    )
    parser.add_argument(
        "--min-level",
        type=int,
        default=2,
        help="Smallest heading level to include (default: 2)",
    )
    parser.add_argument(
        "--max-level",
        type=int,
        default=3,
        help="Largest heading level to include (default: 3)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for changes without writing files (exit 1 if any file would change)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not (1 <= args.min_level <= 6 and 1 <= args.max_level <= 6 and args.min_level <= args.max_level):
        print("Invalid heading range: min/max must be between 1 and 6 and min <= max", file=sys.stderr)
        return 2

    paths = [Path(p) for p in args.paths]
    files = list(dict.fromkeys(iter_markdown_files(paths)))
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 2

    changed_any = False
    for path in files:
        changed, status = process_file(path, args.min_level, args.max_level, args.check)
        changed_any = changed_any or changed
        print(f"{status:9} {path}")

    if args.check and changed_any:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
