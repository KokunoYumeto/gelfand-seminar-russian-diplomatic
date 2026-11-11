"""Verify the ZIP from a fresh extraction, including the complete TeX rebuild.

Run: python code/check_archive.py [chapter_directory] [archive_zip]
Uses PyMuPDF to compare rendered PDF text; generated PDF metadata may differ.
The check adds its result to the source directory for the final packaging pass.
"""
import hashlib,json,subprocess,sys,tempfile,zipfile
from pathlib import Path
import fitz
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
Z=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else D.parent/'GY1985.zip'
audit=D/'audit';report={'archive_sha256_at_check':hashlib.sha256(Z.read_bytes()).hexdigest(),'scope':'Fresh extraction of all payload files before adding this audit result; subsequent packaging adds audit files only.'}
with tempfile.TemporaryDirectory(prefix='gy1985_extraction_',dir=D.parent) as tmp:
    E=Path(tmp)
    with zipfile.ZipFile(Z) as z:
        assert z.testzip() is None
        for n in z.namelist():
            assert not Path(n).is_absolute() and '..' not in Path(n).parts,n
        z.extractall(E)
    assert not (E/'code/texruntime').exists()
    original_tex={n:(E/n).read_bytes() for n in ['GY1985_chapter.tex','GY1985_test.tex']}
    original=fitz.open(E/'GY1985_test.pdf')
    before=[p.get_text() for p in original];original.close()
    with (audit/'archive_extraction_build.txt').open('w') as stream:
        run=subprocess.run(['bash','code/rebuild.sh'],cwd=E,stdout=stream,stderr=subprocess.STDOUT)
    report['rebuild_exit_code']=run.returncode
    assert run.returncode==0,'Fresh extraction rebuild failed; see audit/archive_extraction_build.txt'
    report['generated_tex_identical']={n:(E/n).read_bytes()==v for n,v in original_tex.items()}
    rebuilt=fitz.open(E/'GY1985_test.pdf');after=[p.get_text() for p in rebuilt];rebuilt.close()
    report['pages']=len(after);report['pdf_text_identical']=before==after
    report['fresh_local_format_created']=(E/'code/texruntime/xelatex.fmt').exists()
    report['rebuild_status']=json.loads((E/'audit/build_output.json').read_text())['status']
    report['validation_status']=json.loads((E/'audit/validation_output.json').read_text())['status']
    assert all(report['generated_tex_identical'].values()) and report['pdf_text_identical']
    assert report['rebuild_status']==report['validation_status']=='PASS'
report['status']='PASS'
(audit/'archive_extraction_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
