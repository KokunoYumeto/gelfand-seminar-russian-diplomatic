# Workspace-local XeLaTeX setup

This setup uses the installed TeX Live packages and fonts. It downloads nothing and changes no system directories. All generated formats, maps, caches, logs and smoke-test outputs stay under this directory.

## Why the default command failed

The executable `/usr/bin/xelatex` was present. The installed LaTeX source and packages were also present, but the packaged `ls-R` database files referred into an absent `/var/lib/texmf` tree. The default `TEXMF` value used `!!` markers, which restrict lookup to those databases. Consequently `kpsewhich latex.ltx` and `kpsewhich xelatex.ini` failed, and automatic format generation could not find `fmtutil.cnf`.

`env.sh` points writable TeX and cache locations here and sets `TEXMF` to include the installed trees without the database-only markers. It sets the format path to the local `formats` directory. `setup_tex.sh` then generates `xelatex.fmt` directly from the installed `xelatex.ini`, bypassing the absent format-manager configuration. It combines the installed AMS/Computer Modern font maps into local `pdftex.map` and `psfonts.map`, and installs a minimal local `dvipdfmx.cfg` loading the former.

## Exact setup and smoke commands

From the task workspace root:

```bash
bash work/texenv/setup_tex.sh > work/texenv/setup_output.log 2>&1
bash work/texenv/run_smoke.sh > work/texenv/smoke_output.log 2>&1
```

Each script resolves its own location, so it can also be called by absolute path from another working directory. The smoke script uses the supplied kit style at `work/kit/gelfand_companion.sty` and the small stored `smoke.tex`/`smoke.bib` inputs. It performs **XeLaTeX, BibTeX, XeLaTeX, XeLaTeX**, checks extracted Russian text and the resolved citation, checks for missing-character/undefined-reference warnings, lists embedded fonts, and renders the first page for visual inspection.

## Commands for the final chapter

The environment must be sourced in the **same shell** that runs the final build. For this conversation:

```bash
source /workspace/scratch/accef2b6e545/work/texenv/env.sh
cd /absolute/path/to/the/final/build/directory
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
bibtex GY1981_test
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
```

The final directory must contain `gelfand_companion.sty`, the generated chapter, and the bibliography, as required by the driver. The kit style supports ordinary installed fonts. For a fully controlled font choice, copy the four `smoke/fonts/DejaVuSerif*.ttf` files into `fonts/` under the final build directory; that is the configuration verified by the smoke test. No change to the kit style is necessary.

The environment variables set by `env.sh` are:

| Variable | Purpose |
|---|---|
| `TEXMFHOME` | Local supplementary maps and dvipdfmx configuration |
| `TEXMFVAR` | Local writable TeX variable data |
| `TEXMFCONFIG` | Local writable configuration area |
| `TEXMFCACHE`, `XDG_CACHE_HOME` | Local engine/font caches |
| `VARTEXFONTS` | Local generated-font area |
| `TEXMF` | Installed trees plus local trees, permitting ordinary filesystem lookup |
| `TEXFORMATS` | Local generated format path plus ordinary fallback |
| `TEXFONTMAPS` | Local map path plus ordinary fallback |
| `DVIPDFMXINPUTS`, `XDVIPDFMXINPUTS` | Local driver configuration path plus ordinary fallback |

No user-home variable is repurposed.

## Evidence and packaging

- `setup_report.json`, `setup_output.log`, `format_build.log`: package lookup and format generation.
- `smoke_report.json`, `smoke_output.log`, `smoke_bibtex.log`, `smoke_final.log`: successful complete smoke sequence.
- `smoke_text.txt`: extracted English, Russian and resolved citation.
- `smoke_fonts.txt`: every used font is embedded, including DejaVu, Computer Modern, AMS and Latin Modern.
- `smoke_first_page.png`: visual rendering checked for the Russian line, mathematics, theorem, class marker and table.
- `smoke/smoke.pdf`: two-page smoke output, including the bibliography.

The binary format and caches can be omitted from a portable deliverable because `setup_tex.sh` regenerates them from the installed matching TeX Live version. The setup scripts, environment file, README, small inputs and success logs preserve the reproducible workflow. The final user-facing deliverable remains the parent agent’s single chapter ZIP.
