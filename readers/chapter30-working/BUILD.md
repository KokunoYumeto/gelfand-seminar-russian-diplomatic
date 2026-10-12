# Build the chapter30 readers

These are the exact standalone LaTeX sources used for the checked PDFs, accompanied by the original diagram excerpt at its relative `figures/` path and the full bilingual reading ledger. The Russian and English documents are separate.

The checked build used LuaLaTeX on Windows, A4 paper and Noto Serif, Noto Sans and Noto Sans Mono fonts. The source selects the Noto Serif TTF files from `C:/Windows/Fonts/`; this font path must be adapted on another system. Additional source-symbol fallbacks are declared in the preamble. No shell escape or network access is required by the document. From this directory, run each source twice, for example:

```
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-russian-reader-volume-30.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-russian-reader-volume-30.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-english-reader-volume-30.tex
lualatex --no-shell-escape --halt-on-error --file-line-error gelfand-english-reader-volume-30.tex
```

Typeset prose, mathematics and diagram labels carry the content. The small manuscript excerpt supplements a partial native recreation. Undetermined connections and readings remain explicit. Both appendices retain109 historical uncertainty records and two additional diagram observations. This working release covers all26 held frames of chapter30; neither full-corpus reader is finished.
