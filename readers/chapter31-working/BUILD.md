# Build the chapter 31 readers

The two standalone LaTeX files are the exact sources used for the checked PDFs. Keep all accompanying `.tex` modules and the `figures/` directory beside them. The full bilingual historical reading ledger is included separately.

Use LuaLaTeX, A4 paper and the Noto Serif, Noto Sans and Noto Sans Mono fonts. The preambles select Noto Serif TTF files from `C:/Windows/Fonts/`; adapt this font location on other systems. Source-symbol fallbacks are declared in the preamble. The documents require no shell escape or network access. Run each source twice from this directory:

```
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-russian-reader-volume-31.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-russian-reader-volume-31.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-english-reader-volume-31.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-english-reader-volume-31.tex
```

Both appendices preserve all 158 historical uncertainty records. Thirteen small original diagram details supplement native recreations with typed labels. Undetermined geometry and source inconsistencies remain explicit. These are chapter readers; neither full-corpus reader is finished.
