# GY1985: Critical companion to the Gelfand seminar, 1985–86

Evidence and status date: **11 November 2026**.

## Read the result

`GY1985_test.pdf` is the complete compiled chapter. `GY1985_report.md` explains
the findings, counts, source criticism, selection of the development, verification
limits, earlier-year links, and website recommendations.

The core covers **26 records, 260 mathematical occurrences, 11 problem records,
81 bibliography entries, and 172 correction/provenance rows**. Class counts are
A 4, B 14, C 2, D 0, E 217, F 23. The 12 supplementary items on the two adjacent
leaves have `ADJ-` identifiers and are excluded from the core counts. Record 665
is a catalogue heading, with no invented mathematical item.

## Files and evidence

| File or directory | Purpose |
|---|---|
| `GY1985_talks.json` | All 26 records, in manuscript order |
| `GY1985_items.json` | Core occurrence index and separate assessment fields |
| `GY1985_problems.json` | Definite problems, recurrences, and dated status |
| `GY1985_overview.tex` | Overview fitting within two PDF pages |
| `GY1985_development.tex` | Stacking proofs, independent mathematical checks, and adjacent-page supplement |
| `GY1985_corrections.csv` | Corrections, faithful mathematical errors, ambiguities, and provenance |
| `GY1985_references.bib` | Checked references, locators, and verification annotations |
| `GY1985_adjacent_items.json` | Machine-readable supplementary items outside the core |
| `GY1985_chapter.tex`, `GY1985_test.tex` | Generated chapter and standalone driver |
| `audit/sources/` | Opened-source ledgers and access/verification qualifications |
| `audit/reviews/` | Independent proof, report, rendering, and reproducibility reviews |
| `audit/checks/`, `code/check_mathematics_output.json` | Actual computational outputs |
| `audit/buildlogs/` | Python, XeLaTeX, and BibTeX build outputs |
| `audit/pdf_qa/` | Page-boundary check, contact sheets, and representative readable renders |
| `audit/input_manifest.json` | SHA-256 hashes of the supplied attachments and 61 scans |
| `MANIFEST.sha256` | SHA-256 hashes of every other archived file |

The bibliography's `verified` flag means that the linked source was opened.
Item-level fields and the source ledgers distinguish reading a result from
checking publisher metadata. Inaccessible originals and unresolved identifications
remain explicitly qualified. Search-session reference strings in the audit are
provenance tokens; the actual URLs and theorem/section locators are also retained.

The stacking development concerns a prescribed finite stacking history on a fixed
labelled simplex. It supplies a continuous section and a contraction in that
specified space. It does not claim to settle simplicial four-polytope universality
or identify that history space with every realization of the final type.

## Rebuild the PDF

Install Python 3.10 or later, XeLaTeX, BibTeX, and the TeX packages used by
`gelfand_companion.sty`. The bundled DejaVu fonts and their licence support
consistent Latin/Cyrillic text rendering. From the extracted archive root:

```bash
bash code/rebuild.sh
```

This runs the required builder, XeLaTeX, BibTeX, XeLaTeX, XeLaTeX sequence and
then the structural validator. If a clean first build requests another label
pass, the wrapper runs at most two additional XeLaTeX passes. It exits
unsuccessfully on a command error,
unresolved citation/reference, missing glyph, or overfull box. The elementary
commands are also available directly:

```bash
python build_chapter.py GY1985
xelatex GY1985_test
bibtex GY1985_test
xelatex GY1985_test
xelatex GY1985_test
python code/validate_chapter.py
```

The isolated execution environment lacked a prebuilt XeLaTeX format and TeX
filename databases. `code/build_all.py` records a bounded local fallback for
that case. It creates its format under `code/texruntime/`, with no system-file
changes. No binary TeX format is archived, because it can be incompatible with
another TeX engine. Ordinary TeX installations use their installed format.

The three kit files are byte-for-byte copies of the kit attached to this task;
the hash comparison is in `audit/kit_provenance.json`. Copies are also retained
in `code/kit_original/`. The historical compatibility-amendment comment already
present in the attached builder is not a claim that an earlier kit revision was
available in this run. The seven-file schema and common macros are preserved.

## Rerun the mathematical checks

The checks were run using Python 3.12.14 and SymPy 1.14.0. Install the bounded
dependency in `requirements-checks.txt`, then run:

```bash
python code/run_checks.py
```

This checks the Novikov–Veselov and KdV operator identities by two methods,
the explicit positive two-soliton solution and its unequal velocity ratios,
Baker–Akhiezer leading coefficients, determinant duality, the Beltrami sign,
anomaly coefficients, the hyperelliptic defect, exact rational stacking examples,
and the independent early and oscillator/Schubert calculations. The scripts
state their finite scope; complete general proofs are in the chapter.

For PDF geometry and render regeneration only, install `requirements-render.txt`
and run `python code/pdf_qa.py`. This is a layout check, not mathematical proof
verification. The saved independent visual reviews document the inspected pages.

## Authoring provenance and reconstruction

`code/authoring/work/` preserves the four reviewed research fragments, their
authoring scripts, proof sources, source ledgers, and outputs. The layout keeps
the original relative path structure. The final assembly is reproducible from
those checkpoints:

```bash
cd code/authoring
python work/code/assemble.py
python work/code/write_report.py
python work/code/validate_chapter.py work/deliverable
python work/kit/build_chapter.py GY1985 work/deliverable
```

These commands generate a separate `work/deliverable/` below the authoring
directory. They do not overwrite the published files at the archive root.
Individual authoring scripts record research-stage drafts and may precede
documented editorial adjustments; the reviewed fragment data and final assembly
are the authoritative reconstruction inputs. `audit/reviews/` records an
independent byte-identical reassembly check. The normal PDF rebuild above is
the recommended entry point.

The original scans and complete third-party papers are not duplicated. Their
hashes and verified links preserve the source audit. The supplied transcriptions,
record list, task/format instructions, earlier index, and cumulative bibliography
are retained as reconstruction inputs under `code/authoring/`.
