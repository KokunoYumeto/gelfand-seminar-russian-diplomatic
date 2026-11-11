# Final archive extraction disposition

The fresh-extraction rebuild passed after the wrapper was taught to honour an
actual request for another XeLaTeX label pass. All required builder/compiler
commands succeed; a fourth XeLaTeX pass settles the labels on a clean first
build. The additional-pass loop has a finite limit and still exits nonzero if
any retained build or layout warning remains. The initial failure log is kept
as evidence under `audit/archive_extraction_initial_failure.txt`.

The successful extraction contained no saved binary TeX format. It created a
fresh local format, rebuilt the chapter and test driver byte for byte, produced
164 PDF pages with text identical on every page, and passed the structural
validator. Exact results and the checked ZIP hash are in
`audit/archive_extraction_check.json`; compiler and validator output are in
`audit/archive_extraction_build.txt`. The final packaging pass adds these audit
results without changing the chapter, code, or mathematical data.

The prior-index checker was separately rerun after allowing sentence-ending
punctuation following occurrence IDs. All 23 earlier occurrence identifiers
and the reused GP-1982-03 problem identifier exist in the supplied earlier index.
The full list and zero-missing result are in `audit/previous_index_validation.json`.

The final archive is independently checked for duplicate members, required-file
coverage, ZIP CRC integrity, and every SHA-256 entry in its internal manifest.
