# GY1969 — Critical companion to the Gelfand seminar

Open **GY1969_test.pdf** for the complete 152-page chapter.
The editorial report, **GY1969_report.md**, explains the findings, source
limitations, counts, development decisions, and website recommendations.

## Coverage

- 55 catalogue records: 174–228, academic years 1969–70 and 1970–71.
- 290 mathematical occurrences and 17 problem entries.
- 99 correction records and 91 bibliography entries.
- Historical classes: A 19, B 8, C 4, D 0, E 231, F 28.

The indexed content lies on P000283–P000359. The supplied adjacent leaves
P000282 and P000360 are documented as previous/next-year boundary evidence.
The opening carryover is not counted again, and no new 229 record is invented
inside this chapter. Dates, source order and ambiguous attribution are explicit.

## Authoritative files

The seven `GY1969_` data files are `talks.json`, `items.json`, `problems.json`,
`overview.tex`, `development.tex`, `corrections.csv`, and `references.bib`.
The generated `GY1969_chapter.tex` and `GY1969_test.tex` build the PDF with the
provided companion style. Edit the data and regenerate; do not edit the
generated chapter by hand.

## Rebuild

From this directory, run:

```bash
bash code/build.sh
```

This runs the supplied builder, the additional data audit, XeLaTeX, BibTeX,
two resolving XeLaTeX passes, and the exact mathematical checks. It includes
a local-format fallback for an uninitialized TeX Live installation. The four
bundled DejaVu Serif fonts and their licence provide reproducible text shapes.
The final build had zero errors, undefined references/citations, missing
characters, overfull boxes, or BibTeX warnings. See `output/build_summary.json`.

The computations can be run separately with standard-library Python:

```bash
python code/verify_annotations.py
python code/verify_four_subspaces.py
```

Code and exact JSON outputs are included. The full proofs, their scope and
independent checks are in the chapter's Developments section and in
`research/proof_audit.md`. No mathematical novelty is claimed.

## Evidence and audit files

`research/source_checks.json` records opened sources and verification scope.
`research/item_areas.csv` makes the report's speaker/area counts reproducible.
The segment snapshots and their validators, logs and peer reviews are retained
in `research/segments/`; drafting scripts are in `code/authoring/`. Those
drafting scripts preserve the original task-workspace paths and may depend on
the supplied source attachments. The final seven-file build and mathematical
checks do not require those drafting paths. Input file hashes are recorded
without duplicating the large scan archive.

The fixed-format chapter is the reviewed final synthesis; raw segment snapshots
precede a few explicitly logged typesetting and precision normalizations.
`code/kit_original/` preserves the supplied kit unchanged. Rendered contact
sheets and the visual inspection record are in `output/`.

The bibliography deliberately distinguishes an opened link (`verified`) from
result-level verification. One 2026 lead is explicitly unverified. Its
inaccessibility is not used to claim that the arbitrary coherent-sequence
problem remains globally open. The report and item assessments state all
material limitations.
