"""Assemble the single requested GY1964.zip, with sources and audit evidence.

Run from the research workspace after final compilation and visual review.
Only the chapter PDF is distributed; third-party research PDFs and raw web
responses used during research are not copied into this archive.
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys
import zipfile
import subprocess

WORK=Path(__file__).resolve().parents[1]
SOURCE=WORK/'output'
DESTINATION=WORK.parent/'GY1964.zip'
STAGE=WORK/'package'


def main():
    required=['GY1964_talks.json','GY1964_items.json','GY1964_problems.json',
              'GY1964_overview.tex','GY1964_development.tex',
              'GY1964_corrections.csv','GY1964_references.bib',
              'GY1964_report.md','GY1964_chapter.tex','GY1964_test.pdf']
    for name in required:
        if not (SOURCE/name).is_file():raise FileNotFoundError(name)
    checks=json.loads((SOURCE/'evidence/build/build_results.json').read_text())['checks']
    for key in ['latex_errors','overfull_boxes','missing_glyphs','undefined_references',
                'font_warnings','bibliography_warnings']:
        if checks[key]:raise ValueError(f'Build requires attention: {key}')
    if not (WORK/'evidence/visual_review.md').is_file():
        raise FileNotFoundError('Complete visual_review.md before packaging.')
    if STAGE.exists():shutil.rmtree(STAGE)
    STAGE.mkdir()
    for name in required+['GY1964_test.tex','build_chapter.py',
                           'gelfand_companion.sty','CHAPTER_FORMAT.md']:
        shutil.copy2(SOURCE/name,STAGE/name)
    shutil.copytree(WORK/'code',STAGE/'code',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
        p=STAGE/'code/kit_original'/name;p.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(WORK/'kit'/name,p)
    def skip_part(directory,names):
        return [n for n in names if n=='__pycache__' or n=='primary' or
                n.startswith('web_') or n.endswith('.pyc') or n.endswith('.pdf')]
    shutil.copytree(WORK/'parts',STAGE/'parts',ignore=skip_part)
    shutil.copytree(WORK/'source_pages',STAGE/'source_pages')
    for name in ['previous_index.md','references_cumulative.bib']:
        shutil.copy2(WORK/name,STAGE/name)
    def skip_evidence(directory,names):
        return [n for n in names if n=='pages' or n=='__pycache__' or
                n.startswith('domar') or n.endswith('.pyc') or
                n.endswith('.pdf') or n.startswith('package_')]
    shutil.copytree(WORK/'evidence',STAGE/'evidence',ignore=skip_evidence)
    shutil.copytree(SOURCE/'evidence/build',STAGE/'evidence/build',dirs_exist_ok=True)
    for part in ['autumn','winter','spring']:
        shutil.copy2(WORK/'parts'/part/'research_log.md',
                     STAGE/'evidence'/f'{part}_research_log.md')
    # Test the documented layout using the actual packaged scripts. This
    # checks that relative paths survive moving code/parts/evidence into the
    # delivered archive root.
    check_dir=WORK/'reproduction_check'
    check_dir.mkdir(exist_ok=True)
    reproduction=[]
    for script,args in [('assemble_data.py',[str(check_dir)]),
                        ('finalize_data.py',[str(check_dir)]),
                        ('make_report.py',[str(check_dir)]),
                        ('audit_data.py',['.'])]:
        command=[sys.executable,str(STAGE/'code'/script),*args]
        result=subprocess.run(command,cwd=STAGE,text=True,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (STAGE/'evidence'/('packaged_'+script.replace('.py','')+'_output.txt')).write_text(result.stdout)
        reproduction.append({'script':script,'returncode':result.returncode})
        if result.returncode:raise RuntimeError(script+' failed:\n'+result.stdout)
    matches={}
    for suffix in ['talks.json','items.json','problems.json','corrections.csv',
                   'references.bib','overview.tex','report.md']:
        name='GY1964_'+suffix
        matches[name]=(check_dir/name).read_bytes()==(STAGE/name).read_bytes()
    if not all(matches.values()):raise ValueError('A packaged reconstruction differs from the delivered files.')
    (STAGE/'evidence/reproducibility_check.json').write_text(json.dumps({
        'commands':reproduction,'byte_identical_reconstructed_files':matches,
        'development':'Authoritative hand-written proof source, independently reviewed; not regenerated from JSON.'},indent=2)+'\n')
    counts=json.loads((WORK/'evidence/counts.json').read_text())
    page_count=json.loads((WORK/'evidence/visual/page_inventory.json').read_text())['pages']
    (STAGE/'README.md').write_text(f'''# GY1964 — critical companion to the 1964–65 Gelfand seminar

Status checked through **12 November 2026**. This archive contains the complete
chapter and the reproducible research record requested in GY1964_prompt.md.

## Reading the result

Start with `GY1964_test.pdf` (**{page_count} pages**) for the typeset chapter, or
`GY1964_report.md` for the editorial findings, counts, search decisions,
limitations, and website recommendations. The chapter covers **{counts['records']}
records, {counts['items']} mathematical occurrences, {counts['problems']} indexed
problems, {counts['references']} references, and {counts['corrections']} corrections**.
All 247 supplied occurrence IDs are retained. The added support assertion is
1964-6.9. P000090 belongs to the next academic year and is retained only in
the source extracts and provenance discussion.

The seven authoritative sources are `GY1964_talks.json`, `GY1964_items.json`,
`GY1964_problems.json`, `GY1964_overview.tex`, `GY1964_development.tex`,
`GY1964_corrections.csv`, and `GY1964_references.bib`. The supplied format is
reproduced in `CHAPTER_FORMAT.md`. `GY1964_chapter.tex` and `GY1964_test.tex`
are generated from these sources.

The bibliography has {counts['bibliography_notes'].get('verified',0)} entries marked
`verified` and {counts['bibliography_notes'].get('unverified',0)} marked `unverified`.
These markers record whether the link or DOI opened. The occurrence fields
and bibliography annotations separately state whether the theorem, abstract,
metadata, or only an indirect source was inspected.

## Build the chapter

Requirements: Python 3, XeLaTeX, BibTeX, and the packages used by the supplied
style (fontspec, babel, AMS packages, mathtools, natbib, xurl, hyperref,
booktabs, longtable, enumitem, needspace, and etoolbox). The PDF was built
with TeX Live 2025/dev and embedded DejaVu Serif, Latin Modern, and Computer
Modern mathematical fonts. The style also supports CMU Serif if installed.

From the extracted archive directory:

```sh
python build_chapter.py GY1964
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
bibtex GY1964_test
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
```

Or run the wrapper, which preserves command output and checks the final log:

```sh
python code/build_and_check.py .
```

The execution environment contained TeX packages but dangling filename and
format databases. `code/tex_environment.py` handles that specific condition
by using the installed trees and creating a local XeLaTeX format in
`.tex-cache`. It does not alter the system installation or the supplied
builder/style. A normally configured TeX installation needs no fallback.

## Reproduce the exact mathematics

Python 3.12.14 and SymPy 1.14.0 were used. The independent checker uses only
the Python standard library. Run in this order:

```sh
python code/bishop_certificates.py evidence/bishop_certificates.json > evidence/bishop_certificates_output.txt
python code/independent_bishop_check.py > evidence/independent_bishop_check_output.txt
python code/finite_action_check.py evidence/finite_action_check.json > evidence/finite_action_check_output.txt
```

The two Bishop implementations use different elimination and integration
routes. They agree on the endpoint signs, all 31 small coprime pairs, and
all five exact approximation certificates. The all-denominator statements
are proved in the development, rather than inferred from these checks.
`evidence/development_proof_review.md` records the independent proof review.
The finite group script checks the 168-element counterexample in 1964-34.13.

## Reconstruct the data from reviewed blocks

The frozen research blocks are in `parts/autumn`, `parts/winter`, and
`parts/spring`, with `parts/root_references.bib` supplying shared primary
references. Their own generation scripts and outputs are retained. The
following sequence reconstructs the delivered root files from the reviewed
block data, applies the logged editorial changes, and regenerates the report:

```sh
python code/normalize_corrections.py --check-only
python code/assemble_data.py .
python code/finalize_data.py .
python code/audit_data.py .
python code/make_report.py .
python code/build_and_check.py .
```

Run finalization only after fresh assembly: it assigns canonical problem
IDs and intentionally rejects an already-finalized input. The problem map,
before/after decisions, bibliography merge review, and correction formatting
ledger are in `evidence/`. Thirteen question-kind occurrences intentionally
lack a separate problem entry; `evidence/problem_index_review.md` gives the
reason for each exclusion and records the added Brown subnormal problem.

## Source and visual audits

`source_pages/` contains all 90 Russian and English page extracts from the
supplied transcriptions. The reduced reading extracts in `parts/` are
convenience outputs; the diplomatic Russian and scans govern doubtful
readings. To repeat extraction and input hashing, supply the directory
containing the original six attachments:

```sh
python code/audit_inputs.py /path/to/original-attachments
python code/extract_sources.py /path/to/original-attachments
```

The source hashes are in `evidence/input_audit.json`. Use the originally
supplied scan archive for scan review. Research logs retain source URLs,
locators, access limits, and chronology decisions. The three block reviews,
proof review, final build logs, and visual review are separate records of
different kinds of verification.

For page rendering, install PyMuPDF, Pillow, and Poppler's `pdftoppm`, then run:

```sh
python code/render_review.py GY1964_test.pdf evidence/visual
```

Every page was rendered at 90 dpi; labelled contact sheets and a page
inventory are included. The visual review also examined selected full pages,
including the overview, mathematical development, problem index,
corrections, and bibliography. The final build has no errors, overflowing
boxes, missing glyphs, undefined references, font warnings, or bibliography
warnings. Earlier build-attempt logs are retained as superseded diagnostics.

`MANIFEST.sha256` records every delivered file except itself. No network
access is required to rebuild the chapter or rerun the exact computations.
''')
    # Confirm that the supplied kit was kept unchanged.
    kit_same={n:(STAGE/n).read_bytes()==(WORK/'kit'/n).read_bytes()
              for n in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']}
    if not all(kit_same.values()):raise ValueError('Supplied kit changed unexpectedly.')
    audit={'required_files':required,'all_required_present':True,
           'supplied_kit_unchanged':kit_same,
           'final_build_checks':checks,'counts':counts,
           'archive_integrity_check':'zipfile.testzip is executed after archive creation'}
    (STAGE/'evidence/package_check.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    (STAGE/'evidence/package_output.txt').write_text(
        'All required files present. Supplied kit hashes match. Final build checks clean.\n'
        'Archive is checked with zipfile.testzip before delivery.\n')
    files=sorted(p for p in STAGE.rglob('*') if p.is_file())
    lines=[hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(STAGE).as_posix()
           for p in files]
    (STAGE/'MANIFEST.sha256').write_text('\n'.join(lines)+'\n')
    with zipfile.ZipFile(DESTINATION,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(p for p in STAGE.rglob('*') if p.is_file()):
            z.write(p,p.relative_to(STAGE).as_posix())
    with zipfile.ZipFile(DESTINATION) as z:
        bad=z.testzip()
        if bad:raise ValueError('Corrupt archive member: '+bad)
        names=z.namelist()
        if not set(required).issubset(names):raise ValueError('Missing required archive member.')
    result={'archive':DESTINATION.name,'files':len(names),'bytes':DESTINATION.stat().st_size,
            'sha256':hashlib.sha256(DESTINATION.read_bytes()).hexdigest(),
            'zip_integrity':'PASS','required_files':'PASS','supplied_kit':'UNCHANGED'}
    (WORK/'evidence/package_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
