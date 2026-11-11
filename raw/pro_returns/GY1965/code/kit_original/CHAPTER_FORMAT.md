# The chapter format (one academic year = one chapter)

Every year's chapter of the companion is built from the same eight files by `build_chapter.py`, with the macros of
`gelfand_companion.sty`, so that all chapters compile together in one reader with a common occurrence index, problem
index and bibliography. `TAG` is the task tag, e.g. `GY1965`; `YEAR` is the first calendar year of the academic year.
All text fields marked LaTeX are inserted as they are: they must be valid LaTeX for XeLaTeX (mathematics in `\( \)`
or `\[ \]`, Russian quotations from the notes in `\ru{...}`, citations as `\citet{key}` or `\citep{key}`). Fields
marked text are plain text (they are escaped). Use only the macros of `gelfand_companion.sty` and standard LaTeX/AMS.

## TAG_talks.json — one object per MCCME record of the year, in source order

```json
{"record": 53, "date": "1965-09-20", "speaker": "J. J. Kohn", "pages": "P000090-P000092",
 "title": "The d-bar Neumann problem", "kind": "talk",
 "summary": "LaTeX: one or two paragraphs on what the talk contained and how it fits the seminar's lines."}
```
`kind`: talk | plan | heading | other. `date`, `speaker`, `pages`, `title`: text. A record with no mathematical
content (a plan, a list of names) still gets an entry, with a summary saying what it contains.

## TAG_items.json — the occurrence index: one object per distinct mathematical item

```json
{"id": "1965-53.2", "record": 53, "pages": "P000091", "kind": "question",
 "title": "Subelliptic estimates for the d-bar Neumann problem",
 "notes": "LaTeX: what the notes say, in their notation, with the Russian where the wording matters",
 "statement": "LaTeX: the precise statement in modern terms, with all hypotheses",
 "reconstruction": "LaTeX or empty: what in the statement is your reconstruction rather than the notes",
 "class": "B",
 "fate": "LaTeX: what became of it, with \\citet{kohn1963harmonic} etc.",
 "present_status": "LaTeX: the status today, dated (as of November 2026)",
 "literal_correctness": "correct", "publication_match": "exact", "verification": "read the result",
 "development": "none", "problem": "GP-1965-01", "worth": "",
 "refs": ["kohn1963harmonic"], "confidence": "high"}
```
- `id`: `YEAR-<record>.<n>`, numbered consecutively within the record.
- `kind` (text): definition | construction | theorem | claim | conjecture | question | problem | method | remark.
- `class`: A published soon after by the speaker or by Gelfand; B developed by others; C partly developed (say
  exactly what remains open); D not developed (say what was searched); E known before the talk (expository);
  F not identifiable from the notes.
- `literal_correctness` (text): correct | correct with missing hypotheses | false as written | not determinable.
- `publication_match` (text): exact | partial | thematic only | none found.
- `verification` (text): read the result | publisher metadata checked | indirect | unresolved lead.
- `development` (text): none | annotated | developed in this chapter.
- `problem` (text, may be empty): the problem-index id when the item belongs to a problem (see below).
- `worth` (LaTeX, required for C and D): one sentence: worth developing now, and why.
- `refs`: the keys in `TAG_references.bib` of every work cited for this item.
- `confidence` (text): high | medium | low (identification and fate).

## TAG_problems.json — the problem index: problems that occur this year

```json
{"id": "GP-1965-01", "title": "...", "statement": "LaTeX", "occurrences": ["1964-17.1", "1965-53.2"],
 "status": "LaTeX: dated status", "status_date": "2026-11", "refs": ["key"]}
```
A problem is a precise question or conjecture that recurs, or that later literature took up, or that is open. When a
problem of an earlier year (see the attached index of earlier years) recurs, reuse its id if it has one, and list
the earlier occurrences too; new problems get `GP-YEAR-nn`. Do not create a problem for every item: only for
questions with a definite statement.

## TAG_overview.tex — LaTeX, no `\chapter` or `\section` command

One to two pages: the year's talks and main lines, what came out of them, the counts of items by class (a small
table), the open problems of the year, and what in this year connects to earlier years.

## TAG_development.tex — LaTeX: the deep work (may be empty if nothing deserves it)

One `\subsection{...}` per developed question, using the environments `theorem, proposition, lemma, corollary,
conjecture, definition, question, example, remark, proof`. Put `\ours` after the title of every result proved,
computed or constructed in this task (`\oursComputed` for computations), and cite the literature for the rest.

## TAG_corrections.csv — corrections to the transcription or translation

Columns: `page,place,transcription_reads,should_read,evidence,applies_to` (`applies_to`: ru | en | both). LaTeX in
the cells is allowed. An empty file with only the header is fine.

## TAG_references.bib — BibTeX, every work cited

Reuse the keys of the attached `references_cumulative.bib` for works already cited in earlier years; new keys as
`authoryearword` (e.g. `kirillov1962unitary`). Every entry has `url` or `doi` and `note = {verified}` if you opened
it, or `note = {unverified}`.

## Building and checking

```
python build_chapter.py TAG          # checks the files, writes TAG_chapter.tex and TAG_test.tex
xelatex TAG_test && bibtex TAG_test && xelatex TAG_test && xelatex TAG_test
```
Fix every ERROR the script prints and every LaTeX error until both steps run cleanly.
