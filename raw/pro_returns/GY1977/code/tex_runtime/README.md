# Workspace-local XeLaTeX and BibTeX runtime

The image contains XeTeX and the required TeX Live package files, but its generated configuration is incomplete. In particular, `/usr/share/texlive/texmf-dist/ls-R` and `/usr/share/texmf/ls-R` point into the absent `/var/lib/texmf`; the default database-only (`!!`) Kpathsea search therefore fails to find installed packages. The XeLaTeX format, language configuration, and aggregate font maps are also absent.

`run_tex.py` repairs this environment entirely within its own directory. It searches the installed package trees directly, copies the distribution's base language configuration, aggregates the installed Computer Modern/AMS/Latin Modern font maps, and builds a local `xelatex.fmt`. It reads the system installation but changes no system file. No network download was required.

## Build commands

From the directory containing the chapter source and bibliography, run:

```bash
python3 /workspace/scratch/1eb0e8a5924e/work/tex_runtime/run_tex.py xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error chapter.tex
python3 /workspace/scratch/1eb0e8a5924e/work/tex_runtime/run_tex.py bibtex chapter
python3 /workspace/scratch/1eb0e8a5924e/work/tex_runtime/run_tex.py xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error chapter.tex
python3 /workspace/scratch/1eb0e8a5924e/work/tex_runtime/run_tex.py xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error chapter.tex
```

Replace `chapter` with the actual job name. The launcher path may be relocated; its generated tree is always resolved relative to the launcher. The installed package trees are expected at the Debian paths recorded in `runtime_manifest.json`.

To force regeneration after moving to another installation of the same layout:

```bash
python3 run_tex.py --bootstrap
```

## Scope and verification

The format uses the installed XeTeX 0.999996 binary and LaTeX2e 2024-11-01, patch level 2. The smoke document uses an unmodified copy of the delivered `gelfand_companion.sty` as it existed at test time. It exercises Cyrillic Unicode text, DejaVu fonts, AMS symbols and fraktur, theorem/proof environments, occurrence fields, the corrections table, and natbib with BibTeX `plainnat`.

The initial XeLaTeX pass, BibTeX, and two final XeLaTeX passes all completed successfully. The final PDF has a resolved `(Knuth, 1984)` citation and bibliography. The final TeX log has no undefined citation, missing glyph, or font warning. Some sample lines and the corrections table produce ordinary overfull-box notices at the sample book's narrow default text width; these are layout checks for the chapter editor, not runtime failures.

The installation provides Russian Babel locale data but no Russian hyphenation package. The delivered style's locale fallback renders Cyrillic correctly; this bootstrap does not add Russian hyphenation patterns. Only the required Latin/AMS math maps are aggregated. The driver configuration is copied from the installed distribution and omits references to absent generated CJK maps, which this chapter does not use.

## Files for packaging

Keep `run_tex.py`, this README, `runtime_manifest.json`, `bootstrap.log`, and the smoke source, bibliography, check JSON, final `.log`/`.blg`, and PDF as reproducibility evidence. The local `texmf/` tree is generated and can be omitted from a source-only package; `run_tex.py` recreates it automatically if the format is absent. The format is approximately 4 MiB. Installed TeX packages and font binaries are not copied into the deliverable.
