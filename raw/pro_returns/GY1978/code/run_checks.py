"""Run the six supplied mathematical checks and retain their exact outputs."""
from pathlib import Path
import subprocess,sys
HERE=Path(__file__).resolve().parent
names=['check_independent','check_spin1','check_contact','check_vertex','check_math','check_p807_independent']
for name in names:
    result=subprocess.run([sys.executable,str(HERE/(name+'.py'))],cwd=HERE,
                          stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (HERE/(name+'_output.txt')).write_text(result.stdout)
    print(name+': exit '+str(result.returncode))
    if result.returncode:
        print(result.stdout)
        raise SystemExit(result.returncode)
print('All exact assertions and explicitly finite numerical checks passed.')
