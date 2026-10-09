# Building the chapter reader

Each file in `sources/` is a standalone LuaLaTeX document. The original working master is not needed to build the reader chapters. Compile twice, with shell escape disabled:

```text
lualatex --no-shell-escape --halt-on-error --interaction=nonstopmode gelfand-russian-diplomatic-volume-01.tex
lualatex --no-shell-escape --halt-on-error --interaction=nonstopmode gelfand-russian-diplomatic-volume-01.tex
```

The distributed PDFs were compiled with LuaHBTeX 1.25.7 (MiKTeX 26.5). Packages include fontspec, amsmath, amssymb, amsthm, mathtools, TikZ, tikz-cd, hyperref, ulem, newunicodechar and adjustbox.

The checked rendering uses the installed Noto Serif, Noto Sans, Noto Sans Mono, Segoe UI Symbol and MS Gothic fonts. Several refined chapters explicitly select the Noto Serif TrueType files under `C:/Windows/Fonts/`. These are system font locations, not project file references. No font files are redistributed. Building on another platform requires configuring corresponding installed fonts and repeating glyph/layout checks; identical pagination is not promised after a font change.

The combined reader adds two separately typeset introductory/catalog pages. It copies all 1374 chapter page content streams unchanged, prefixes each chapter's named destinations, preserves 568 figure links, adds 34 chapter bookmarks and catalog links, and retains chapter page numbering through viewer page labels.

Renderer-only edits have an exact inverse to the held diplomatic master frame bodies: diagram width wrappers, breakable prose underlining, seven original syntax spans plus one diagram-label position adjustment, and 27 full annotation calls relocated into notes after their own source frames. The original annotation arguments and source mathematics remain recoverable; literal TeX layout-token identity is not claimed.

All 1527 frame slots are present. 24 lack imported returns; 6738 uncertainty-ledger entries remain unresolved. This is not completed manuscript quality assurance. The source archive is linked in README.md.
