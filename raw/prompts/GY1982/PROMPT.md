# Task GY1982: the I. M. Gelfand seminar, the academic year 1982–83 — one chapter of the critical companion

## What this is

The I. M. Gelfand seminar met on Monday evenings at Moscow State University. Notes of its talks from 1964 to 1989
survive as handwritten pages, scanned and published by MCCME (https://old.mccme.ru/gelfand/notes/all-links.html,
774 records, listed by date and speaker). We have transcribed the notes in Russian (diplomatic) and translated them
into English; both were made by AI and checked against the scans.

A first run on the year 1964–65 measured what the notes contain: 247 items over 49 records, most of them expository
or published soon after; a few precise open questions, all on famous threads; no orphan ideas. On that evidence the
companion to the notes is a **critical companion**: for every talk, what was said, stated precisely, and what became
of it; an occurrence index of every item and a problem index that follows each definite question across the years;
corrections to the transcription; and full development only where there is a precise question and a plausible
bounded contribution. Each academic year is one chapter, built from data files in one fixed format, so that all
chapters go into one reader with common indices and bibliography.

This task writes the chapter for the academic year 1982–83. It is a bounded research task with a definite end: complete it in this
one run, without asking questions back.

## Attached

- `GY1982_en.tex`: the English translation of the notes of the academic year 1982–83: source pages GELFAND-P001026 to P001115
  (90 pages). `\SourcePage{GELFAND-Pnnnnnn}{label}` starts a scanned page; editorial notes record
  the transcriber's remarks; `\Unclear` marks a doubtful reading.
- `GY1982_ru.tex`: the Russian diplomatic transcription of the same pages. It is the authority: where the English is
  doubtful or a formula matters, read the Russian.
- `GY1982_scans.zip`: the scans of these pages (`GELFAND-Pnnnnnn.png`). Look at the page itself wherever a reading is
  doubtful, a formula or diagram decides the mathematics, or the transcription and the translation disagree.
- `GY1982_talks.md`: the MCCME list of the 37 records of 1982-83 (record, date, speaker), with the
  source pages on which each record's notes lie. The archive is not always in date order, and a page may hold the
  end of one talk and the start of the next; some records are plans or headings, not talks.
- `GY1982_kit.zip`; unzip it:
  - `kit/CHAPTER_FORMAT.md`, the format of the files you deliver (read it first), with `kit/gelfand_companion.sty`
    and `kit/build_chapter.py`, which build and check your chapter;
  - `previous_index.md`, the items and problems of the earlier years already done (ids, titles, classes), so that
    you can link a question that recurs instead of treating it as new;
  - `references_cumulative.bib`, the references already verified in earlier years: reuse their keys.

## Stage 1 — Every talk and every item

For each record of the year, in source order: the identification (record, date, speaker, source pages, a short title)
and a summary of what the talk contained. Then split the talk into its distinct mathematical items (definitions,
constructions, theorems or claims, conjectures, questions, problems posed, methods proposed, remarks by Gelfand),
numbered `YEAR-<record>.<n>` (YEAR is the first calendar year of the talk's academic year), and give for each, as
`CHAPTER_FORMAT.md` specifies: what the notes say, in their
notation; the precise statement in modern terms, with all hypotheses; what of it is your reconstruction; the class
A–F; the fate with references; the present status, dated; and the assessment fields (literal correctness, publication
match, verification level, development, confidence).

The classes: **A** published soon after by the speaker or by Gelfand; **B** developed by others into established
results; **C** partly developed (say exactly what remains open); **D** not developed (say what you searched before
saying so); **E** already known before the talk; **F** not identifiable from the notes. For C and D, say in one
sentence whether it is worth developing now and why.

How to find the fate. Search with your web tools: Math-Net.ru (Doklady Akad. Nauk SSSR, Uspekhi Mat. Nauk,
Funktsional. Anal. i Prilozhen., Trudy MMO, Mat. Sbornik: many seminar talks became a Doklady note within a year),
zbMATH Open (author and year), Google Scholar, arXiv, MathOverflow, the speakers' collected works, bibliographies and
obituaries, and recollections of the seminar. What worked in the first run: Math-Net for short Soviet announcements;
author bibliographies for chronology; following references backwards from a later paper when a title search fails.
What it taught: the absence of a first search hit is weak evidence of D; a later paper on the same broad subject is
weak evidence that the exact question was solved; and a question must be matched with its exact quantifiers and
hypotheses (the 1964–65 run nearly classified a question about Weyl algebras with different numbers of canonical
pairs as the fixed-rank Dixmier conjecture). Keep apart a correct old theorem stated in shorthand, a false literal
statement, and a later implementation of an old proof idea.

## Stage 2 — Development, where it is warranted

From the C and D items, take those with a precise question and a plausible bounded contribution, and develop them.
There is no quota: if none qualifies, say so in the overview; a well-supported A, B or E is an informative result,
and an open problem must not be manufactured out of an exposition. For each developed question:

1. the strongest formulation the notes support, and separately the strongest formulation that is plausibly true
   today, with all hypotheses;
2. the state of the art, with exact references and the exact results they prove;
3. why it remained open or was dropped, as far as can be told;
4. the development: complete proofs of whatever you can prove, partial results with their exact scope,
   counterexamples with every hypothesis checked, computations (code and output included), and the next precise
   questions; mark everything you prove or compute yourself (`\ours`, `\oursComputed`) and never present a conjecture
   or a sketch as a theorem;
5. the exact obstruction still present, and how far one further research run could take it.

Check every proof and computation a second time before you finish, independently (re-derive, re-run with other
parameters), and say in the text what the check found. In the first run such a check caught a small-n failure of an
exponential bound and stopped finite evidence from being stated as a theorem for all denominators.

## Stage 3 — Problems, corrections, overview, report

- The problem index: the year's definite questions and conjectures, linked to earlier occurrences (`previous_index.md`)
  and to later literature.
- Corrections: every place where the transcription or the translation looks wrong to you (page and place, what it
  reads, what the notes show, the evidence).
- The overview of the year (one to two pages).
- `GY1982_report.md`: the counts (items by class, by speaker, by area), what was hard, which searches found the
  publications, what the classes miss this year, and any change you propose to the method or the format. The
  companion will also be a small website generated from the data files (pick a year, then a talk, then an item, and
  open its fate, present status and modern results; a problem index across the years; search). Add a short section
  on how this year's material should be presented there: what a reader arriving at one talk needs to reach first,
  which links between items, problems and years matter, and any field the data would need for it.

## Format, building and checking

Write the files exactly as `kit/CHAPTER_FORMAT.md` specifies. Then run `python build_chapter.py GY1982` and compile
`GY1982_test.tex` with XeLaTeX and BibTeX (the commands are in `CHAPTER_FORMAT.md`); fix every error the script or
LaTeX reports until the chapter builds cleanly. The chapter is in English; quote the Russian of the notes (`\ru{...}`)
where the exact wording matters.

## Rules

- Keep three things apart everywhere: what the notes show, what sources say, and what you infer.
- Every reference must be real and checked: give a link or DOI that you opened (`note = {verified}`); otherwise mark
  it `note = {unverified}`. Do not cite from memory without checking.
- Quote sources briefly and cite them exactly.
- Do not fill gaps in the notes from what a speaker "must have" said; mark reconstructions as yours.
- Cover every record of the year; an entry may be short when the talk is short or unidentifiable, but none may be
  missing.
- Do not stop early and do not ask questions back: make the decisions a careful researcher would make, state them, and
  carry on to the end.
- Save your work to files as you go (the items record by record, then each development), so that nothing is lost if
  the final step is interrupted.

## What to return

One zip file, `GY1982.zip`, containing the seven files of `CHAPTER_FORMAT.md` (`GY1982_talks.json`, `GY1982_items.json`,
`GY1982_problems.json`, `GY1982_overview.tex`, `GY1982_development.tex`, `GY1982_corrections.csv`,
`GY1982_references.bib`), `GY1982_report.md`, the built `GY1982_chapter.tex` and `GY1982_test.pdf`, and any code you ran
with its output. Offer only that one download.
