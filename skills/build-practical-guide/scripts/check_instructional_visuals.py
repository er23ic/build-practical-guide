#!/usr/bin/env python3
"""Check structural requirements for native SVG teaching visuals."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.svg)(?:\s+\"[^\"]*\")?\)")
UNICODE_SUPERSCRIPTS = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ")
SVG_NS = {"svg": "http://www.w3.org/2000/svg"}


def files_under(paths: list[Path], suffix: str) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == suffix:
            files.add(path.resolve())
        elif path.is_dir():
            files.update(
                item.resolve()
                for item in path.rglob(f"*{suffix}")
                if item.is_file()
            )
    return sorted(files)


def markdown_svg_references(paths: list[Path]) -> tuple[set[Path], list[str]]:
    referenced: set[Path] = set()
    failures: list[str] = []
    for markdown in files_under(paths, ".md"):
        text = markdown.read_text(encoding="utf-8")
        for alt, target in MARKDOWN_IMAGE.findall(text):
            target_path = (markdown.parent / target.split("#", 1)[0]).resolve()
            if not alt.strip():
                failures.append(f"{markdown}: SVG image has empty alternative text")
            if not target_path.is_file():
                failures.append(f"{markdown}: missing SVG image {target}")
            else:
                referenced.add(target_path)
    return referenced, failures


def check_svg(path: Path) -> list[str]:
    failures: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        return [f"{path}: invalid XML: {error}"]

    if not root.get("viewBox"):
        failures.append(f"{path}: missing viewBox")
    if root.get("role") != "img":
        failures.append(f'{path}: root SVG must use role="img"')

    title = root.find("svg:title", SVG_NS)
    description = root.find("svg:desc", SVG_NS)
    if title is None or not "".join(title.itertext()).strip():
        failures.append(f"{path}: missing non-empty <title>")
    if description is None or not "".join(description.itertext()).strip():
        failures.append(f"{path}: missing non-empty <desc>")

    labelled_by = set((root.get("aria-labelledby") or "").split())
    for element, name in ((title, "title"), (description, "desc")):
        element_id = element.get("id") if element is not None else None
        if not element_id or element_id not in labelled_by:
            failures.append(f"{path}: aria-labelledby does not reference <{name}> id")

    svg_text = path.read_text(encoding="utf-8")
    simulated = sorted(set(svg_text) & UNICODE_SUPERSCRIPTS)
    if simulated:
        failures.append(
            f"{path}: simulated Unicode superscript characters found: {''.join(simulated)}"
        )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Markdown-linked native SVG teaching visuals."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    referenced, failures = markdown_svg_references(args.paths)
    svg_files = set(files_under(args.paths, ".svg")) | referenced
    for svg in sorted(svg_files):
        failures.extend(check_svg(svg))

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(
        f"Instructional SVG structure: passed "
        f"({len(svg_files)} SVG files, {len(referenced)} Markdown references)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
