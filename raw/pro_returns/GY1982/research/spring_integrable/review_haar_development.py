"""Independent character-based check plus read-only rerun of root checker."""
import contextlib,hashlib,io,json,pathlib,sympy as s
D=pathlib.Path(__file__).parent
root=D.parents[2]
code=root/'deliverable/code/haar_check.py'
development=root/'deliverable/GY1982_development.tex'
N=s.symbols('N',integer=True,positive=True)
# For any irreducible character, Schur orthogonality gives
# E chi(U V U^-1 V^-1)=1/dim(chi).
symdim=N*(N+1)/2
altdim=N*(N-1)/2
adjdim=N**2-1
EC=1/N
EC2=s.factor(1/symdim+1/altdim)
EabsC2=s.factor(1+1/adjdim)
varX=s.factor(2*EC2+2*EabsC2-(2*EC)**2)
covX=4/N**2
rows=[]
for d in [2,3,4,5,6,9]:
 edge_count=s.binomial(d,2)
 adjacent_pairs=d*s.binomial(d-1,2)
 varS=s.factor(edge_count*varX+2*adjacent_pairs*covX)
 claimed=d*(d-1)*((N**2+4)/(N**2-1)+(4*d-10)/N**2)
 assert s.cancel(varS-claimed)==0
 rows.append({'d':d,'Fprime':str(-d-d*(d-1)/N**2),'Fsecond':str(varS)})
assert s.cancel(EC2-4/(N**2-1))==0
assert s.cancel(EabsC2-N**2/(N**2-1))==0
# Run the original exact code without editing any parent output.
source=code.read_text()
namespace={'__name__':'review_import','__file__':str(D/'review_haar_development.py')}
exec(compile(source,str(code),'exec'),namespace)
captured=io.StringIO()
with contextlib.redirect_stdout(captured):
 namespace['main']()
(D/'root_haar_rerun.txt').write_text(captured.getvalue())
out={
 'review_result':'PASS',
 'proof_hash_sha256':hashlib.sha256(development.read_bytes()).hexdigest(),
 'code_hash_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
 'independent_method':'Character decomposition and Schur orthogonality, then edge-pair counting.',
 'character_moments':{'EC':str(EC),'EC2':str(EC2),'EabsC2':str(EabsC2)},
 'rows':rows,
 'root_checker_rerun':'all original symbolic and rational assertions passed; outputs saved in this shard',
 'N1':'Separate scalar case F=-d^2 beta, Fsecond=0',
 'local_theorem':'Read arXiv math/0608193v3, pp.1-3, Theorem0.1. Real small-coupling convergence, analytic limit and matching derivatives; no complex-integral convergence or global claim.'
}
(D/'development_review_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
