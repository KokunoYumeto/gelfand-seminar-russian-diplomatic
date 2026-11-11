#!/usr/bin/env python3
"""Recorded, idempotent repairs to the segment source after editorial review."""
from pathlib import Path
p = Path(__file__).with_name("build_segment.py")
s = p.read_text()
left = chr(96) * 2
pairs = [
    (left+"50 cases (Gudkov)''", "“50 cases (Gudkov)”"),
    (left+"50''", "“50”"),
    (left+"Positive oval''", "“Positive oval”"),
    (left+"Limit points''", "“Limit points”"),
    (left+"Type I''", "“Type I”"),
    (left+"type II''", "“type II”"),
    (left+"Dear Misha you are wrong.''", "“Dear Misha you are wrong.”"),
    ("'lemma' if False else 'claim'", "'claim'"),
    ("zero modes are omitted.','A'", "zero modes are omitted.','E'"),
    ("Does a bounded linear operator on a separable infinite-dimensional Banach space have an orbit dense in the entire space?", "Does there exist a separable infinite-dimensional Banach space and a bounded linear operator on it with an orbit dense in the entire space?"),
]
for before, after in pairs:
    count = s.count(before)
    s = s.replace(before, after)
    print(f"{count} replacement(s): {before} -> {after}")
p.write_text(s)
