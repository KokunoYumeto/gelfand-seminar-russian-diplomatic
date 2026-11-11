from pathlib import Path
import csv,re,json,shutil
p=Path('work/late_author.py')
s=p.read_text().replace('A fundamental-domain interpretation is possible but absent from the notes.','One can instead integrate over a specified fundamental domain, but the notes do not say so.')
p.write_text(s)
# Independent syntax scan: strip explicit math and inspect every CSV cell.
rows=list(csv.DictReader(Path('work/late_corrections.csv').open()))
errors=[]
for row in rows:
    for field in ['place','transcription_reads','should_read','evidence']:
        value=row[field]
        outside=re.sub(r'\\\[(.*?)\\\]|\\\((.*?)\\\)', '', value, flags=re.S)
        if re.search(r'(?<!\\)[_^]|\\(?:varphi|Phi|sigma|Gamma|rho|frac|sum|int|alpha|beta|partial|mathcal|mathbf|operatorname)\b',outside):
            errors.append({'page':row['page'],'place':row['place'],'field':field,'outside_math':outside})
outdir=Path('work/late_correction_preflight');outdir.mkdir(exist_ok=True)
shutil.copy('project/kit/gelfand_companion.sty',outdir/'gelfand_companion.sty')
tex=[r'\documentclass[11pt,oneside]{book}',r'\usepackage[a4paper,margin=22mm,headheight=15pt]{geometry}',r'\usepackage{gelfand_companion}',r'\setlength{\emergencystretch}{2em}',r'\begin{document}']
for row in rows:
    tex.append(r'\subsection*{'+row['page']+': '+row['place']+'}')
    for label,field in [('Transcription reads','transcription_reads'),('Critical reading','should_read'),('Evidence','evidence')]:
        tex.append(r'\noindent\textit{'+label+r'.} '+row[field]+r'\par')
tex.append(r'\end{document}')
(outdir/'late_correction_test.tex').write_text('\n'.join(tex)+'\n')
Path('work/late_correction_math_audit.json').write_text(json.dumps({'rows_checked':len(rows),'errors':errors},indent=2)+'\n')
print(json.dumps({'rows_checked':len(rows),'errors':errors,'test_document':str(outdir/'late_correction_test.tex')},indent=2))
raise SystemExit(bool(errors))
