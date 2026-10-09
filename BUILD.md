# Building the Russian chapter reader

The 34 files in `sources/` are standalone LuaLaTeX documents. Keep the accompanying `sources/figures/` folder beside them. Compile from `sources/`, twice, with shell escape disabled:

```text
lualatex --no-shell-escape --halt-on-error --interaction=nonstopmode gelfand-russian-diplomatic-volume-01.tex
lualatex --no-shell-escape --halt-on-error --interaction=nonstopmode gelfand-russian-diplomatic-volume-01.tex
```

The rendering uses Noto Serif, Noto Sans, Noto Sans Mono, Segoe UI Symbol and MS Gothic. Refined chapter preambles can select installed files under `C:/Windows/Fonts/`. No font files are redistributed. Other platforms require corresponding installed fonts and renewed glyph/layout checks; pagination can change.

The combined reader contains 1398 unchanged chapter page content streams and two introductory/catalog pages. Assembly prefixes 4953 named destinations, preserves 571 source-figure links, and provides 34 chapter bookmarks and catalogue links with chapter page labels.

The reader is derived from the frozen effective accepted returns for all 165 packets and 1527 source-frame records. Reversible rendering edits preserve the original frame content and the full annotation arguments with their source associations. Some long annotations appear immediately after their own source frame. Six spaces repair TikZ ellipse-axis syntax without changing its radii or coordinates; one case-number position is separated from an adjacent index, retaining both labels and the graph strokes. These layout changes make no new manuscript-reading or mathematical-reconstruction claims.

The 25 PNG crops are additions to retained typed diagram content. Their manifest entries bind original source-scan hashes, crop coordinates, modes, dimensions and pixel hashes. PDF image checks use an explicit crop allowlist and compare decoded pixels. There are no full-page scan substitutions for written material.

Every chapter received current-source two-pass build checks, frame-identifier/text extraction checks, missing-glyph checks and all-page physical character-boundary checks. Bounded pages were actually rendered and viewed; this is not an all-page visual-overlap audit or completed manuscript comparison. The uncertainty ledger still contains 6820 unresolved entries.
