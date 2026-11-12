# Raw research outputs: the chapters of the critical companion, year by year

This folder holds raw research outputs, not edited for publication: the chapters of the critical companion to the notes
of the I. M. Gelfand seminar, one per academic year (or two small years together), as returned by GPT-6 Astra
(ChatGPT Pro mode); the prompts that produced them, with the full list of what was attached to each; and the scripts
and kit that built the prompts. [METHODOLOGY.md](METHODOLOGY.md) explains how it was done. The companion built from
these chapters will be published in `companion/`.

- Each chapter in `pro_returns/` is AI-produced by GPT-6 Astra (ChatGPT Pro mode). The date of each return is given
  below.
- The labels the chapters give to statements and questions (their class, fate and status) are the model's own. These
  chapters have not been reviewed yet: every statement in them is unchecked.
- No priority or novelty is claimed.
- The programs in the returns (the `code/` folders and the other program files) are published as returned, with
  their data and outputs; we have not run them.
- In these copies the first name of the user who ran the project is replaced by "user", local paths included, and
  e-mail addresses are replaced by "[e-mail address removed]". Nothing else in the files is changed. LaTeX auxiliary
  files, Python caches, font files and compiled binaries are not included, nor the copies of the attached notes that
  some runs kept beside their work (`inputs/`, `sources/`). Each prompt's attachments are listed file by file in
  `prompts/<year>/ATTACHMENTS.md`, with a link to each of our own files and the source of each scan.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.

## Folders

Dates are those on which the return was received (UTC).

| Folder | Academic years | Items | Date | Reviewed |
|---|---|---|---|---|
| `pro_returns/GY1965/` | 1965–66 | 298 | 9 Nov 2026 | no |
| `pro_returns/GY1966/` | 1966–67 | 277 | 9 Nov 2026 | no |
| `pro_returns/GY1967/` | 1967–68, 1968–69 | 320 | 9 Nov 2026 | no |
| `pro_returns/GY1969/` | 1969–70, 1970–71 | 290 | 9 Nov 2026 | no |
| `pro_returns/GY1971/` | 1971–72 | 262 | 9 Nov 2026 | no |
| `pro_returns/GY1972/` | 1972–73 | 272 | 9 Nov 2026 | no |
| `pro_returns/GY1973/` | 1973–74 | 301 | 9 Nov 2026 | no |
| `pro_returns/GY1974/` | 1974–75 | 265 | 10 Nov 2026 | no |
| `pro_returns/GY1975/` | 1975–76 | 256 | 10 Nov 2026 | no |
| `pro_returns/GY1976/` | 1976–77 | 250 | 10 Nov 2026 | no |
| `pro_returns/GY1977/` | 1977–78 | 305 | 10 Nov 2026 | no |
| `pro_returns/GY1978/` | 1978–79 | 216 | 10 Nov 2026 | no |
| `pro_returns/GY1979/` | 1979–80 | 252 | 10 Nov 2026 | no |
| `pro_returns/GY1980/` | 1980–81 | 246 | 11 Nov 2026 | no |
| `pro_returns/GY1981/` | 1981–82 | 210 | 11 Nov 2026 | no |
| `pro_returns/GY1982/` | 1982–83 | 335 | 11 Nov 2026 | no |
| `pro_returns/GY1983/` | 1983–84, 1984–85 | 413 | 12 Nov 2026 | no |
| `pro_returns/GY1985/` | 1985–86 | 260 | 11 Nov 2026 | no |
| `pro_returns/GY1987/` | 1987–88 | 287 | 11 Nov 2026 | no |
| `pro_returns/GY1988/` | 1988–89 | 160 | 12 Nov 2026 | no |
| `prompts/<year>/` | The prompt of each year (`PROMPT.md`), the list of its attachments (`ATTACHMENTS.md`) and our own attached files not published elsewhere in this repository (`attached/`) | | 9–11 Nov 2026 | — |
| `tools/` | The script that builds each year's package (`make_year_package.py`), the prompt template (`PROMPT_TEMPLATE.md`) and the chapter kit (`kit/`: the chapter format, the LaTeX style, the scripts that build and check a chapter and the global reader, and its earlier versions) | | 9–11 Nov 2026 | — |

"Items" is the number of entries in each chapter's `<year>_items.json`, as returned.
GY1983 came back without a compiled PDF, and GY1988 as a condensed text fallback without a chapter file; the
`RETURN_NOTES.md` in each of the two folders says how it was received and checked.
