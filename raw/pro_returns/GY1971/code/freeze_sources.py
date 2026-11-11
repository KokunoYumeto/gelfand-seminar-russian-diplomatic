#!/usr/bin/env python3
"""Freeze supplied inputs and authoring fragments for an auditable final merge.

Initial-authoring command:
  python GY1971/code/freeze_sources.py --workspace /path/to/working-directory
The delivered snapshot can be merged directly; this freezing step is not
required to rebuild the chapter from the delivered seven data files.
"""
import argparse
import hashlib
import json
import pathlib
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace', type=pathlib.Path, required=True)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    root = pathlib.Path(__file__).resolve().parents[1]
    target = root / 'code' / 'source_fragments'
    target.mkdir(parents=True, exist_ok=True)
    copied = []
    for group in 'abc':
        dest = target / group
        dest.mkdir(exist_ok=True)
        for path in sorted((workspace / 'work' / group).iterdir()):
            if path.suffix in {'.json', '.csv', '.bib', '.py', '.md'}:
                shutil.copy2(path, dest / path.name)
                copied.append(str((dest/path.name).relative_to(root)))
        ledger_name = {'a':'research_records_229_243.md',
                       'b':'research_records_244_258.md',
                       'c':'research_records_259_288.md'}[group]
        shutil.copy2(workspace/'work'/group/'research_log.md', root/'audit'/ledger_name)
    for name in ('previous_index.md', 'references_cumulative.bib'):
        shutil.copy2(workspace / name, target / name)
    shutil.copy2(workspace / 'work' / 'records.json', target / 'catalogue_records.json')
    inputs = root / 'source_inputs'
    inputs.mkdir(exist_ok=True)
    for name in ('GY1971_prompt.md', 'GY1971_talks.md', 'GY1971_en.tex', 'GY1971_ru.tex'):
        shutil.copy2(workspace / 'upload' / name, inputs / name)
    manifest = []
    paths = sorted((workspace/'upload').iterdir())
    paths += sorted(workspace.glob('GELFAND-P*.png'))
    paths += [workspace/'kit'/'CHAPTER_FORMAT.md', workspace/'kit'/'build_chapter.py',
              workspace/'kit'/'gelfand_companion.sty', workspace/'previous_index.md',
              workspace/'references_cumulative.bib']
    for path in paths:
        if path.is_file():
            manifest.append({'input':str(path.relative_to(workspace)),
                             'bytes':path.stat().st_size,
                             'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (root/'audit'/'input_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'frozen_fragment_files':copied, 'input_manifest_entries':len(manifest)},indent=2))


if __name__ == '__main__': main()
