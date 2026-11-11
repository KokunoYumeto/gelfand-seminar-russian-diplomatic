from pathlib import Path
p=Path(__file__).with_name('build_middle.py')
t=p.read_text()
t=t.replace("S'\\)",r'S^{\prime}\)').replace("E_i'\\)",r'E_i^{\prime}\)')
t=t.replace("\\pi_\\varphi(\\mathcal A)''",r'\pi_\varphi(\mathcal A)^{\prime\prime}')
t=t.replace("booktitle='Actes du Congr\\`es International des Math\\'ematiciens (Nice, 1970)'",'booktitle="Actes du Congrès International des Mathématiciens (Nice, 1970)"')
p.write_text(t)
