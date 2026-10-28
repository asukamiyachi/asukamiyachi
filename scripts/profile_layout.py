#!/usr/bin/env python3
"""Reposition generated GitHub Profile 3D metrics without changing their values.

Runs after upstream github-profile-3d-contrib, because that generator
recreates the footer on every workflow execution.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

TARGET = Path("profile-3d-contrib/profile-night-rainbow.svg")
FOOTER_START = "<g><text style=\"font-size: 32px; font-weight: bold;\" x=\"384\""
FOOTER_AFTER = "<g id=\"profile-top-metrics\"><line x1=\"532\" y1=\"194\" x2=\"748\" y2=\"194\" stroke=\"#eeeeff\" stroke-width=\"1\" stroke-opacity=\"0.24\"></line><text style=\"font-size: 32px; font-weight: bold;\" x=\"384\""
REPLACEMENTS = [
    ("style=\"font-size: 32px; font-weight: bold;\" x=\"384\" y=\"830\" text-anchor=\"end\" class=\"fill-strong\"", "style=\"font-size: 76px; font-weight: bold;\" x=\"640\" y=\"132\" text-anchor=\"middle\" class=\"fill-strong\""),
    ("style=\"font-size: 24px;\" x=\"394\" y=\"830\" text-anchor=\"start\" class=\"fill-fg\"", "style=\"font-size: 27px;\" x=\"640\" y=\"173\" text-anchor=\"middle\" class=\"fill-fg\""),
    ("transform=\"translate(608, 802), scale(2)\"", "transform=\"translate(568, 212), scale(2)\""),
    ("style=\"font-size: 32px; font-weight: bold;\" x=\"650\" y=\"830\" text-anchor=\"start\" class=\"fill-fg\"", "style=\"font-size: 28px; font-weight: bold;\" x=\"614\" y=\"239\" text-anchor=\"start\" class=\"fill-fg\""),
    ("transform=\"translate(736, 802), scale(2)\"", "transform=\"translate(696, 212), scale(2)\""),
    ("style=\"font-size: 32px; font-weight: bold;\" x=\"772\" y=\"830\" text-anchor=\"start\" class=\"fill-fg\"", "style=\"font-size: 28px; font-weight: bold;\" x=\"742\" y=\"239\" text-anchor=\"start\" class=\"fill-fg\""),
]


def apply_layout(source: str) -> str:
    # Accept an already-adjusted SVG for safe local re-runs.
    if 'id="profile-top-metrics"' in source and FOOTER_START not in source:
        for _, replacement in REPLACEMENTS:
            if source.count(replacement) != 1:
                raise ValueError("Partial or inconsistent profile metrics layout")
        ET.fromstring(source)
        return source

    if source.count(FOOTER_START) != 1:
        raise ValueError("Upstream metrics footer changed; refusing unsafe replacement")
    result = source.replace(FOOTER_START, FOOTER_AFTER, 1)
    for old, new in REPLACEMENTS:
        if result.count(old) != 1:
            raise ValueError("Upstream metrics schema changed: " + old)
        result = result.replace(old, new, 1)
    ET.fromstring(result)
    return result


if __name__ == "__main__":
    current = TARGET.read_text(encoding="utf-8")
    updated = apply_layout(current)
    TARGET.write_text(updated, encoding="utf-8")
    print("Placed live contributions and star/fork counts at upper center")
