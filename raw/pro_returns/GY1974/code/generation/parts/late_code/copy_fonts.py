from pathlib import Path
import shutil, hashlib, json, csv, re
from fontTools.ttLib import TTFont
workspace=Path(__file__).resolve().parents[2]
source=workspace.parents[1]/'fonts'
target=workspace/'GY1974/fonts'
target.mkdir(parents=True,exist_ok=True)
names=['DejaVuSerif.ttf','DejaVuSerif-Bold.ttf','DejaVuSerif-Italic.ttf','DejaVuSerif-BoldItalic.ttf']
result=[]
for name in names:
 src=source/name
 assert src.is_file(),src
 shutil.copy2(src,target/name)
 assert hashlib.sha256(src.read_bytes()).digest()==hashlib.sha256((target/name).read_bytes()).digest()
 font=TTFont(target/name)
 chars=set().union(*(set(table.cmap) for table in font['cmap'].tables if table.isUnicode()))
 russian=set(range(0x410,0x450))|{0x401,0x451}
 names_table=font['name']
 def name_text(n):
  matches=[rec for rec in names_table.names if rec.nameID==n]
  return matches[0].toUnicode() if matches else ''
 result.append({'file':str(target/name),'bytes':(target/name).stat().st_size,'family':name_text(1),'subfamily':name_text(2),'version':name_text(5),'russian_alphabet_complete':russian<=chars,'sha256':hashlib.sha256((target/name).read_bytes()).hexdigest()})
 font.close()
shutil.copy2(source/'LICENSE_DEJAVU',target/'LICENSE_DEJAVU')
rows=list(csv.DictReader((workspace/'parts/late_corrections.csv').open()))
issues=[]
for i,row in enumerate(rows,1):
 for field in ('place','transcription_reads','should_read','evidence'):
  text=row[field]
  outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',text,flags=re.S)
  if re.search(r'(?<!\\)[_%&#^$]',outside):
   issues.append({'row':i,'field':field,'text':text})
report={'fonts':result,'correction_rows_checked':len(rows),'raw_latex_prose_issues':issues,'metadata_note':'faithful_error is an intentional schema value; its underscore is not edited.'}
(workspace/'parts/late_code/font_copy_and_csv_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert not issues
