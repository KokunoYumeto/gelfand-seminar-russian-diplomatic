function runChecks() {
  const out = {description:"Independent finite computations for GY1983 editorial propositions. These are checks, not proofs.", covariance:[], radon:[], matrix:[], laurent:[]};
  function simpson(f,a,b,n) { let s=f(a)+f(b); for(let j=1;j<n;j++)s+=(j%2?4:2)*f(a+(b-a)*j/n); return (b-a)*s/(3*n); }
  function lagSum(L,eta) { let s=0; for(let dx=1-L;dx<L;dx++) for(let dy=1-L;dy<L;dy++)s+=(L-Math.abs(dx))*(L-Math.abs(dy))*Math.pow(1+dx*dx+dy*dy,-eta/2); return s; }
  function directSum(L,eta) {let s=0;for(let x=0;x<L;x++)for(let y=0;y<L;y++)for(let u=0;u<L;u++)for(let v=0;v<L;v++)s+=Math.pow(1+(x-u)**2+(y-v)**2,-eta/2);return s;}
  for (const eta of [.25,1,1.5]) {
    const integrand=t=>8*Math.pow(1+t*t,-eta/2)*(1/(2-eta)-(1+t)/(3-eta)+t/(4-eta));
    const target=simpson(integrand,0,1,16384), target2=simpson(integrand,0,1,8192);
    const rows=[4,8,16,32,64,128,256].map(L=>({L,normalized_variance:lagSum(L,eta)/Math.pow(L,4-eta)}));
    const check=[4,8].map(L=>({L,relative_error:Math.abs(lagSum(L,eta)-directSum(L,eta))/directSum(L,eta)}));
    out.covariance.push({eta,normalizing_exponent:2-eta/2,continuum_target:target,quadrature_resolution_difference:Math.abs(target-target2),rows,independent_pair_sum_checks:check});
  }
  for(const R of [.5,1,2]){
    const derivativeEnergy=simpson(t=>4*Math.PI*Math.PI*t*t,-R,R,4096);
    const volume=4*Math.PI*R**3/3;
    out.radon.push({radius:R,derivative_energy:derivativeEnergy,volume,ratio:derivativeEnergy/volume,expected:2*Math.PI});
  }
  function multiply(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>s+x*B[k][j],0)));}
  for(const k of [[1,0,0],[0,1,0],[0,0,1],[1,2,3],[-2,3,-5],[.25,-.5,2]]){
    const [x,y,z]=k,Q=[[0,-x,-y,-z],[x,0,-z,y],[y,z,0,-x],[z,-y,x,0]],Q2=multiply(Q,Q),norm=x*x+y*y+z*z;
    out.matrix.push({wave_vector:k,max_error_Q2_plus_norm_identity:Math.max(...Q2.flatMap((row,i)=>row.map((v,j)=>Math.abs(v+(i===j?norm:0)))))});
  }
  out.matrix_bad_2_by_2 = {a:2,b:3,upper_off_diagonal_imaginary_part:12,lower_off_diagonal_imaginary_part:-12,diagonal:13,corrected_diagonal:13,reason:"For [[a,ib],[-ib,a]], squaring gives diagonal a^2+b^2 and off-diagonals +2iab,-2iab; changing the lower-right entry to -a gives (a^2+b^2)I."};
  for(const h of [-2,.5,3])for(const tau of [-2,-.5,.25,2]){
    const q=-1/tau,p=h*tau*tau,qd=1/(tau*tau),pd=2*h*tau,Q=q+p,P=q+2*p;
    out.laurent.push({h,tau,H_error:Math.abs(p*q*q-h),q_equation_error:Math.abs(qd-q*q),p_equation_error:Math.abs(pd+2*p*q),transformed_H_error:Math.abs((P-Q)*(2*Q-P)**2-h)});
  }
  out.laurent_symplectic_determinant=1*2-1*1;
  out.coisotropic_counterexample={group:"(R^3,+)",bivector:"z d/dx wedge d/dy",subgroup:"z-axis",dual_bracket:"[dx,dy]=dz",annihilator:"span(dx,dy) is not closed",action:"trivial, hence all smooth functions on any Poisson M are invariant and bracket-closed",checks:"Coefficient z is additive; Jacobi on the sole independent coordinate triple is zero."};
  return out;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = {runChecks};
  if (require.main === module) process.stdout.write(JSON.stringify(runChecks(),null,2)+"\n");
}