from pathlib import Path
p=Path('work/late_correction_preflight.py')
s=p.read_text().replace("for field,value in row.items():","for field in ['place','transcription_reads','should_read','evidence']:\n        value=row[field]")
p.write_text(s)
