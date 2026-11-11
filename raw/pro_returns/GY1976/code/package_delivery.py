"""Gate the completed deliverable, write hashes, and create the one requested ZIP."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

REQUIRED=['talks.json','items.json','problems.json','overview.tex','development.tex',
          'corrections.csv','references.bib','report.md','chapter.tex','test.pdf']

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory');ap.add_argument('archive')
    a=ap.parse_args();d=Path(a.directory).resolve();dest=Path(a.archive).resolve()
    for suffix in REQUIRED:
        p=d/('GY1976_'+suffix)
        if not p.exists() or not p.stat().st_size:raise ValueError('Missing/empty '+str(p))
    v=json.loads((d/'code/output/validation.json').read_text())
    b=json.loads((d/'code/output/build/build_summary.json').read_text())
    q=json.loads((d/'code/output/pdf_audit.json').read_text())
    if v['status']!='PASS' or not b['all_returncodes_zero']:raise ValueError('Build/validation did not pass')
    if any(q[k] for k in ['latex_error_count','undefined_citation_or_reference_count','missing_character_count','overfull_box_count']):
        raise ValueError('Unresolved PDF/log issue')
    if q['visual_review']!='completed':raise ValueError('Visual review not completed')
    if 'must be replaced before packaging' in (d/'GY1976_report.md').read_text():raise ValueError('Provisional report')
    # Exclude disposable TeX intermediates: retained logs, .bbl and final PDF
    # suffice to audit the built output, and the driver can recreate the rest.
    for ext in ['aux','out','toc','fls','fdb_latexmk','synctex.gz']:
        p=d/('GY1976_test.'+ext)
        if p.exists():p.unlink()
    paths=sorted(p for p in d.rglob('*') if p.is_file() and p.name!='MANIFEST.sha256')
    manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(d).as_posix()+'\n' for p in paths)
    (d/'MANIFEST.sha256').write_text(manifest)
    paths.append(d/'MANIFEST.sha256')
    dest.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for p in sorted(paths):z.write(p,Path(d.name)/p.relative_to(d))
    with zipfile.ZipFile(dest) as z:
        failure=z.testzip()
        if failure:raise ValueError('Corrupt member '+failure)
        names=z.namelist()
        if len(names)!=len(set(names)):raise ValueError('Duplicate ZIP member')
        for suffix in REQUIRED:
            if d.name+'/GY1976_'+suffix not in names:raise ValueError('Missing ZIP member '+suffix)
    result={'archive':str(dest),'bytes':dest.stat().st_size,'members':len(paths),
        'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'zip_crc_check':'PASS',
        'required_files':'PASS','pdf_pages':q['pages'],'items':v['counts']['items']}
    dest.with_suffix('.verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
