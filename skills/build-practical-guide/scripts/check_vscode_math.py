#!/usr/bin/env python3
"""Reject math delimiters unsupported by VS Code's built-in Markdown preview."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


UNSUPPORTED_DELIMITER = re.compile(r"\\(?:\(|\)|\[|\])")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix.lower() == ".md":
            files.append(path)
    return files


def unsupported_delimiters(path: Path) -> list[tuple[int, str]]:
    findings: list[tuple[int, str]] = []
    fence_marker: str | None = None

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_marker is None:
                fence_marker = marker[0]
            elif marker[0] == fence_marker:
                fence_marker = None
            continue

        if fence_marker is None and UNSUPPORTED_DELIMITER.search(line):
            findings.append((line_number, line.strip()))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check Markdown for \\\\(...\\\\) and \\\\[...\\\\] math delimiters. "
            "VS Code preview requires $...$ and $$...$$."
        )
    )
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    findings = [
        (path, line_number, line)
        for path in markdown_files(args.paths)
        for line_number, line in unsupported_delimiters(path)
    ]

    if findings:
        for path, line_number, line in findings:
            print(f"{path}:{line_number}: unsupported VS Code math delimiter: {line}")
        return 1

    print("VS Code Markdown math delimiters: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
