# How the chapters of the critical companion were made

This is the account of the year chapters in `pro_returns/`: what each prompt asked and what it attached, which model
answered, what has been checked, and how each year's results were carried into the next prompt. Every file named here
is published in this folder; paths are relative to `raw/`.

## What was asked

The notes of the seminar's talks from 1964 to 1989 survive as handwritten pages, scanned and published by MCCME. This
repository holds our AI-made Russian diplomatic transcription of them and its English translation. A first run on the
year 1964–65 measured what the notes contain: mostly expository material or results published soon after, a few
precise open questions, all on well-known threads. On that evidence the companion to the notes is a critical
companion: for every talk, what was said, stated precisely, and what became of it; an index of every item and a
problem index that follows each definite question across the years; corrections to the transcription; and full
development only where there is a precise question and a plausible bounded contribution. Each academic year (or two
small years together) is one chapter, built from data files in one fixed format, so that all chapters go into one
reader with common indices and bibliography.

The prompt of every year is the template [tools/PROMPT_TEMPLATE.md](tools/PROMPT_TEMPLATE.md) filled in for that year
by [tools/make_year_package.py](tools/make_year_package.py); the filled prompts are `prompts/<year>/PROMPT.md`. It
asks for three stages: (1) every talk and every item in it (definition, construction, theorem or claim, conjecture,
question, problem, method, remark), each stated precisely with what became of it and its status as of November 2026,
with verified references; (2) development, where it is warranted; (3) the problems followed across the years,
corrections to the transcription checked against the scans, an overview and a report. It fixes the format of the files to deliver (`kit/CHAPTER_FORMAT.md`)
and asks the model to build and check its own chapter with the kit's scripts.

## What was attached

Each prompt went with six files, listed for every year in `prompts/<year>/ATTACHMENTS.md`:

- the English translation and the Russian diplomatic transcription of the year's pages, cut page by page from the
  cumulative working readers (the Russian is the authority);
- the scans of those pages, from the MCCME archive (<https://old.mccme.ru/gelfand/notes/all-links.html>);
- the MCCME list of the year's records (date, speaker) with the pages on which each record's notes lie;
- the chapter kit ([tools/kit/](tools/kit/): the chapter format, the LaTeX style and the scripts that build and check a
  chapter), with the index of the items and problems of the years already done (`previous_index.md`) and the
  bibliography already verified (`references_cumulative.bib`).

## The model and the runs

The user sent each package to ChatGPT; the model was GPT-6 Astra in ChatGPT Pro mode. The returns are in
`pro_returns/<year>/` as returned: the chapter (`<year>_chapter.tex` and its parts), the data files (`_talks.json`,
`_items.json`, `_problems.json`, `_corrections.csv`, `_references.bib`), the report (`_report.md`), a test build of the
chapter, and the model's working programs and logs. The returns do not record a run time; the dates in
[README.md](README.md) are those on which each return was received.

## What has been checked

Each return was processed by Claude Opus 5.5: its files were checked against the format, built with the kit, and
merged into the global reader of the companion (built by `kit/build_global_reader.py`). These checks concern the form
and the build. No review of the mathematical content has been made yet: every statement, attribution, status and
reference in the chapters is the model's own and unchecked.

## The path forward

The years were run in order, and each return fed the next prompt. When a chapter came back, its items, problems and
verified references were added to the kit of the following year: `previous_index.md` lists the items and problems of
all earlier years, so that a question that recurs is linked rather than treated as new, and
`references_cumulative.bib` carries every reference verified so far, so that keys are reused. The kit listed in each
`prompts/<year>/ATTACHMENTS.md` therefore shows exactly what the model knew of the earlier years. The kit was revised
during the series; its earlier versions are in `tools/kit/v1_20261109/`, `v2_20261109/` and `v3_20261109/`. The
remaining packages (GY1983, GY1986 and GY1988) have not been returned yet.
