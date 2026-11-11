# GY1977 — critical companion chapter

Read `GY1977_test.pdf` for the complete chapter. `GY1977_report.md` explains
scope, counts, provenance, methods, limitations and website presentation.
The packet includes 28 requested catalogue envelopes and adjacent material
from 1978–79; read each affected talk's provenance notice before using dates.

## Rebuild the chapter

From this directory, with Python 3, XeLaTeX and BibTeX installed:

```sh
python build_chapter.py GY1977
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
bibtex GY1977_test
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
python code/validate_chapter.py .
```

The style uses CMU Serif when available, otherwise DejaVu Serif. The original
supplied kit is preserved under `code/source_inputs/kit/`. Any local
typography amendments are documented in `code/output/build_validation.json`.
The canonical data are the top-level JSON/CSV/BibTeX and overview/development
files; do not edit the generated chapter by hand.

The working environment's installed TeX packages had missing lookup databases
and no format file. `code/tex_runtime/run_tex.py` repairs that situation using
workspace-local files only. If needed on a comparable Linux installation,
run `python code/tex_runtime/run_tex.py xelatex ...` and similarly for BibTeX.
No package download or system modification was needed for this chapter.

## Rerun the mathematical checks

Python dependencies: SymPy; Pillow for scan integrity and contact sheets;
pypdf for PDF inspection. The symbolic checks do not require internet access.

```sh
python code/check_jets.py
python code/check_kp.py
python code/check_laplacian.py
python code/coin_check.py
python code/verify_emendations.py
```

Additional Calogero verification scripts are included in `code/` and in the
late-range editorial generators. Their docstrings identify their outputs.
Existing outputs are under `code/output/`; the coin script writes its JSON
beside the script, as in the original working run. Exact arithmetic is used
where claimed. Finite checks are not substitutes for the general proofs.

## Editorial evidence and reassembly

- `code/editorial_inputs/` contains the completed per-range research fragments.
- `code/editorial_generators/` contains the record-writing scripts actually
  used in the working session. They preserve original workspace paths and
  are archival evidence, not the preferred public rebuild interface.
- `code/research_logs/` contains access/search decisions and the independent
  proof review. URLs and theorem locators are in the reference audit.
- `code/source_inputs/` contains the supplied text transcriptions, catalogue,
  task specification, previous index and cumulative bibliography.
- `code/output/` contains scientific results, counts, validation/build logs,
  the scan-recovery audit and the recovered P000722 image.

To reproduce the fragment assembly in a fresh output directory:

```sh
python code/assemble_fragments.py code/editorial_inputs reassembled code/source_inputs
python code/make_report.py reassembled
python code/repair_typesetting.py reassembled
```

Then rebuild from the generated canonical files as above. Final typography
repairs, if any, are also recorded as a deterministic code script.

The original 94-image scan ZIP is not duplicated here. `audit_scans.py` and
`recover_scan_722.py` retain their original workspace-layout assumptions:
place the original images in `scans/` and the scripts in `work/code/` beneath
one workspace root. Recovery additionally needs network access to MCCME.
The recovery script verifies the complete neighboring scans and that the
damaged attachment is a prefix of the recovered page; it does not overwrite
the original upload.

Downloaded research papers are cited, not redistributed. All source and
status assertions distinguish a full-result read from a metadata check.
The final status date is 10 November 2026. The explicit integral cohomology
development makes no claim of research priority.
