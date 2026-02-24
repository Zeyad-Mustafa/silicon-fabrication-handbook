#!/usr/bin/env python3
"""Validate local Markdown links in this repository.

Checks:
- Relative file and directory links
- Fragment anchors in the same file or another Markdown file

Skips:
- External URLs (http/https/mailto/etc.)
- Links inside fenced code blocks
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


LINK_RE = re.compile(r"(?P<bang>!?)\[(?P<label>[^\]]*)\]\((?P<target>[^)\n]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE_RE = re.compile(r"^\s*```")


@dataclass
class LinkIssue:
    file: Path
    line: int
    target: str
    message: str


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


def collect_anchors(md_file: Path, cache: dict[Path, set[str]]) -> set[str]:
    if md_file in cache:
        return cache[md_file]

    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    try:
        text = md_file.read_text(encoding="utf-8")
    except OSError:
        cache[md_file] = anchors
        return anchors

    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        heading_text = m.group(2).strip()
        anchors.add(slugify(heading_text, counts))

    cache[md_file] = anchors
    return anchors


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            rp = path.resolve()
            if rp not in seen:
                seen.add(rp)
                files.append(path)
            continue
        if path.is_dir():
            for md in sorted(path.rglob("*.md")):
                rp = md.resolve()
                if rp not in seen:
                    seen.add(rp)
                    files.append(md)
    return files


def is_external_target(target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme:
        return True
    return target.startswith("//")


def parse_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()
    if " " in target:
        return target.split(" ", 1)[0].strip()
    return target


def iter_links(path: Path):
    in_fence = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(line):
            yield line_no, parse_target(match.group("target"))


def validate_link(
    source_file: Path,
    line_no: int,
    target: str,
    anchor_cache: dict[Path, set[str]],
) -> list[LinkIssue]:
    issues: list[LinkIssue] = []
    if not target:
        issues.append(LinkIssue(source_file, line_no, target, "empty link target"))
        return issues

    if is_external_target(target):
        return issues

    normalized = unquote(target)
    path_part, frag = normalized.split("#", 1) if "#" in normalized else (normalized, "")

    if path_part == "":
        anchors = collect_anchors(source_file, anchor_cache)
        if frag and frag not in anchors:
            issues.append(LinkIssue(source_file, line_no, target, f"missing anchor '#{frag}' in {source_file.name}"))
        elif not frag:
            issues.append(LinkIssue(source_file, line_no, target, "empty link target"))
        return issues

    resolved = (source_file.parent / path_part).resolve()
    if not resolved.exists():
        issues.append(LinkIssue(source_file, line_no, target, f"missing path '{path_part}'"))
        return issues

    if frag:
        if resolved.is_dir():
            issues.append(LinkIssue(source_file, line_no, target, "cannot validate anchor on directory link"))
            return issues
        if resolved.suffix.lower() != ".md":
            issues.append(LinkIssue(source_file, line_no, target, "anchor target is not a Markdown file"))
            return issues
        anchors = collect_anchors(resolved, anchor_cache)
        if frag not in anchors:
            issues.append(LinkIssue(source_file, line_no, target, f"missing anchor '#{frag}' in {resolved.name}"))

    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check local Markdown links and anchors.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["README.md", "PROJECT_STRUCTURE.md", "docs"],
        help="Markdown files or directories to check",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = iter_markdown_files([Path(p) for p in args.paths])
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 2

    issues: list[LinkIssue] = []
    anchor_cache: dict[Path, set[str]] = {}

    for md_file in files:
        try:
            file_issue_count_before = len(issues)
            for line_no, target in iter_links(md_file):
                issues.extend(validate_link(md_file, line_no, target, anchor_cache))
            status = "ok" if len(issues) == file_issue_count_before else "issues"
            print(f"{status:6} {md_file}")
        except UnicodeDecodeError:
            issues.append(LinkIssue(md_file, 0, "", "unable to decode file as UTF-8"))
            print(f"issues {md_file}")

    if issues:
        print("\nLink check failures:")
        for issue in issues:
            loc = f"{issue.file}:{issue.line}" if issue.line else f"{issue.file}"
            print(f"- {loc}: `{issue.target}` -> {issue.message}")
        print(f"\nFound {len(issues)} issue(s).")
        return 1

    print("\nAll checked links passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
