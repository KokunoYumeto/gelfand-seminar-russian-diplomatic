# Final packaging and reproducibility review

Reviewed on 11 November 2026. Scope: the current authoring fragments and deliverable, the supplied task and chapter format, and the four principal build/check entry points. This review made no changes to those scripts or mathematical content. The final ZIP had not yet been assembled when this review was written.

## Result

All ten files expressly required by `GY1985_prompt.md` are present and nonempty in `work/deliverable`: the seven chapter inputs, the report, the generated chapter TeX, and the compiled PDF. The additional test driver, supplied builder and style, chapter-format specification, adjacent-page JSON, and four licensed DejaVu Serif font files are also present. The latest recorded build and structural validation both report `PASS`; the final TeX log has no retained layout/reference messages.

An independent isolated reassembly copied only the required authoring dependencies to a temporary directory and ran `assemble.py`, `write_report.py`, and `build_chapter.py GY1985`. All three commands exited successfully. All eleven compared outputs were **byte-identical** to the current deliverable: the seven core inputs, adjacent-page JSON, report, generated chapter TeX, and test driver. Hashes and command output are recorded in `reassembly_probe_output.json`. The temporary directory was removed; the original sources were not changed.

This comparison precedes the final announced CSV prose copyedit. The integrating editor should rerun assembly after that edit; the evidence file records the exact earlier snapshot through its hashes.

## Concrete build findings and disposition

| Finding | Disposition |
|---|---|
| The validator originally defaulted to `deliverable/` even when installed in the archive's root `code/` directory. | Fixed and reread: it now selects the directory containing the root data when present and otherwise the authoring `deliverable/` directory. The wrapper also passes an explicit directory. |
| A saved `xelatex.fmt` could be incompatible with the recipient's TeX engine; the fallback reused an existing local format. | The integrating editor has agreed to exclude `texruntime/` and all format binaries. The wrapper then uses the installed format or creates a fresh local fallback. |
| The inspected `build_all.py` wrote `REVIEW` for surviving log messages but returned success. | Reported; the integrating editor has agreed to make this case exit nonzero. Current recorded output is already `PASS`. Verify this small final gate change before packaging. |
| `rebuild.sh` was mode `0644` at inspection. | Document `bash code/rebuild.sh`; the integrating editor has also agreed to preserve an executable mode. |
| `rebuild.sh` rebuilds the chapter and runs structural validation; it does not rerun symbolic mathematics. | Give the mathematical-check command separately in the README. This is a documentation requirement, not a failure of the PDF build. |

No additional extraction-path blocker was found in the normal root-data build. The scripts derive their working directory from their own location or an explicit argument. Recorded historical logs naturally contain the original execution paths; those paths are evidence, not runtime dependencies.

## Supplied-kit provenance

The three supplied kit members are **byte-for-byte equal** to both `work/kit` and `work/deliverable`. Their SHA-256 values are:

| File | SHA-256 |
|---|---|
| `CHAPTER_FORMAT.md` | `9a36cc64df393abe06ff833b815ada34b76967d731d21855e3c4b027eb5fe0ca` |
| `build_chapter.py` | `e68acb2619dbb3f4ea14af9e147f43c97fc776b285ae261d23bd50465b1877f8` |
| `gelfand_companion.sty` | `cf2df459ec0b4206dc995b5494b5737afe232f0c6587096616387e4ac1fd2145` |

The historical “Compatibility amendments” comment is already present in the ZIP attached to this task. It must not be attributed to a new edit in this run. A diff against the supplied archive is empty. Preserve the attached kit as the provenance baseline and record this equality; an `audit/kit_changes.diff` may be empty with an explanatory provenance note. There is no evidence here for a different pristine predecessor. The current formatting adjustments reside in the authoring formatter/layout modules, and the runtime fallback resides in the build wrapper.

## Minimal reproducible arrangement

At archive root, retain all ten required deliverables plus `GY1985_test.tex`, `GY1985_adjacent_items.json`, `build_chapter.py`, `gelfand_companion.sty`, `CHAPTER_FORMAT.md`, `README.md`, and `fonts/` including its license. Put the normal build/check entry points under root `code/`, and preserve their recorded outputs and the validation/build logs under `code/` or `audit/` with paths stated in the README.

The proposed authoring checkpoint `code/authoring/work/{code,kit,early,strings,virasoro,late}` is sufficient when it contains:

- `code/assemble.py`, `format_corrections.py`, `format_layout.py`, `cumulative_keys.json`, and `write_report.py`;
- each research fragment's `talks.json`, `items.json`, `problems.json`, `corrections.csv`, and `references.bib`;
- `strings/adjacent_corrections.csv`, `adjacent.tex`, and `adjacent_items.json`;
- `virasoro/stacking_development.tex`, `late/checks.tex`, and `late/overview.tex`;
- all three supplied kit files.

Running the nested assembler writes to `code/authoring/work/deliverable/`; running the nested report generator completes the report there. The independent probe verified this layout. The original research generators may be retained as provenance with their historical path assumptions disclosed; regenerating the reviewed final fragments is a different operation from assembling the chapter.

The assembler does not copy fonts. To compile the newly assembled nested copy itself, also provide its `fonts/` directory, or use the normal archive-root build after deliberately transferring the regenerated inputs. This does not affect the byte-identical root-data reconstruction already checked. The formatter's standalone QA mode likewise needs its authoring `--work-root` when invoked from root `code/`; its imported use by the nested assembler works directly.

## Commands and dependencies to document

From the extracted archive root:

```bash
bash code/rebuild.sh
python3 code/check_mathematics.py
```

For the preserved authoring checkpoint:

```bash
python3 code/authoring/work/code/assemble.py
python3 code/authoring/work/code/write_report.py
```

The ordinary build requires Python, Bash, `kpsewhich`, XeLaTeX, BibTeX, and the packages imported by the supplied style (including fontspec, Babel, AMS packages, natbib, and xurl). The mathematical verification additionally requires SymPy. The recorded successful mathematical run used Python **3.12.14** and SymPy **1.14.0**. Assembly uses `str.removeprefix`, so Python 3.9 or later is necessary; documenting the tested version avoids an unsupported cross-version claim. The local TeX fallback has Debian-style search locations; a normal configured TeX installation uses its own installed format.

Preserve all substantive computational scripts and their outputs, including the independent checks and corrections-format QA, as requested. Exclude machine-specific format binaries, `texruntime/`, and Python caches. Close the audit by checking the actual ZIP member list and rerunning the root entry points from a clean extraction; that final archive-level check remains the integrating editor's packaging step.
