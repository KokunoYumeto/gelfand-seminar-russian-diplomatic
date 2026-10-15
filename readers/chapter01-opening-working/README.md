# Chapter 1: opening of the Russian and English readers

This working excerpt starts at the first original scan, **GELFAND-P000001**. It contains the complete typed transcription of that scan and its four full historical reading notes. Each language has **four A4 pages**: two pages of transcription and two pages of reading notes. **This is one source frame, not the complete chapter.**

- [Russian PDF](gelfand-russian-chapter01-opening-crops.pdf)
- [English PDF](gelfand-english-chapter01-opening-crops.pdf)
- [Russian LaTeX](gelfand-russian-chapter01-opening-crops.tex)
- [English LaTeX](gelfand-english-chapter01-opening-crops.tex)
- [Full reading notes](reading-notes.json) and [crop locations](source-crops.json)

Every uncertain-reading entry has the relevant original detail beside the typed reading. The original diagram accompanies its typed description. The full reading notes repeat the relevant source details, retain the historical alternatives, and distinguish fresh inspection from earlier assessments. Text, formulas and readable labels remain typed; source crops supplement them.

Both PDFs compiled in two LuaLaTeX passes. All eight physical pages were inspected. The source uncertainties were checked in the original and at 3×, 5× and 10×. No mathematical reconstruction has been substituted for a diplomatic reading. A native recreation of the opening diagram remains to be considered during continued chapter preparation.

Production now proceeds from chapter 1 in source order. Earlier chapter 30–31 working PDFs are partial releases and require the same uncertainty-crop treatment. [Whole-reader coverage](../../READERS-STATUS.md).

![Russian opening with original uncertainty details](russian-opening-page1.png)

To rebuild, use LuaLaTeX with shell escape disabled and run each source twice from this folder. The supplied font declaration expects Noto Serif in the Windows fonts folder; other installations can select the same installed font with fontspec. The `figures` folder is required.
