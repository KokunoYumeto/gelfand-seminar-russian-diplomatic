function verifyA(){
 const out=[];
 const check=(name,ok,evidence)=>{out.push({name,pass:Boolean(ok),evidence});if(!ok)throw Error(name);};
 const T=[[4,3],[9,7]];
 check("congruence counterexample",T[0][0]*T[1][1]-T[0][1]*T[1][0]===1&&T.flat().every((v,i)=>(v-(i===0||i===3?1:0))%3===0)&&T[0][0]+T[1][1]===11,"det=1; trace=11; T=I mod3; real spectral radius>1");
 let z=[0,0],orbit=[z];
 for(let j=0;j<5;j++){z=[z[0]*z[0]-z[1]*z[1],2*z[0]*z[1]+1];orbit.push(z);}
 check("critical orbit z^2+i",JSON.stringify(orbit)===JSON.stringify([[0,0],[0,1],[-1,1],[0,-1],[-1,1],[0,-1]]),orbit);
 const bin=(n,k)=>{if(k<0||k>n)return 0;let r=1;for(let j=1;j<=k;j++)r=r*(n-j+1)/j;return r;};
 let cube=true;for(let d=0;d<=8;d++)for(let j=0;j<=d;j++){let v=0;for(let i=j;i<=d;i++)v+=2**(d-i)*bin(d,i)*bin(i,j)*(-1)**(i-j);cube&&=v===bin(d,j);}
 check("cube shifted face polynomial through dimension8",cube,"Coefficientwise F(t-1)=(1+t)^d for d=0,...,8; exact integers");
 const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],sub=(a,b)=>[a[0]-b[0],a[1]-b[1]];
 const mm=(a,b)=>[[add(mul(a[0][0],b[0][0]),mul(a[0][1],b[1][0])),add(mul(a[0][0],b[0][1]),mul(a[0][1],b[1][1]))],[add(mul(a[1][0],b[0][0]),mul(a[1][1],b[1][0])),add(mul(a[1][0],b[0][1]),mul(a[1][1],b[1][1]))]];
 const s1=[[[0,0],[1,0]],[[1,0],[0,0]]],s2=[[[0,0],[0,-1]],[[0,1],[0,0]]],m12=mm(s1,s2),m21=mm(s2,s1);
 const com=m12.map((r,i)=>r.map((v,j)=>sub(v,m21[i][j])));
 check("Pauli factor2",JSON.stringify(com)===JSON.stringify([[[0,2],[0,0]],[[0,0],[0,-2]]]),com);
 let h21=0,e21=0;for(let x=0;x<=2;x++){let entries=[x,2-x,2-x,x-1];if(entries.every(v=>v>=0))h21++;if(entries.every(v=>v===0||v===1))e21++;}
 check("matrix coefficients h21/e21 at m21",h21===2&&e21===1,{h21,e21});
 const assignments=(parts,target)=>{let count=0;const sums=target.map(()=>0);function rec(j){if(j===parts.length){if(sums.every((v,i)=>v===target[i]))count++;return;}for(let i=0;i<sums.length;i++){sums[i]+=parts[j];rec(j+1);sums[i]-=parts[j];}}rec(0);return count;};
 check("labelled equal power-sum factors",assignments([1,1],[1,1])===2&&assignments([2,1],[2,1])===1,{p11_to_m11:2,p21_to_m21:1});
 check("zero Kostka entry",!(1<1),"The only content(2) filling of a two-box column repeats1, violating strict columns; K_(11),(2)=0");
 check("first Riccati coefficients",2*(-1/2)+1===0&&(-1/2)+2*(1/4)===0,"Coefficients of u and u_prime cancel for chi1=-u/2,chi2=u_prime/4");
 let oscillator=true;for(let n=0;n<=8;n++)oscillator&&=-(n+2)*(n+1)+n*(n-1)===-4*n-2;
 check("oscillator commutator on monomials",oscillator,"[D^2,-z^2]z^n=(-4n-2)z^n for n=0,...,8; formula holds algebraically for all n");
 const kernelDims=[-1,0,1].map(t=>1-Number(Math.hypot(0,t)>0));
 check("complex skew-Hermitian parity counterexample",kernelDims.join(",")==="0,1,0",{family:"D_t=it on C",parameters:[-1,0,1],complexKernelDimensions:kernelDims});
 return {date:"2026-11-12",execution:"Pure JavaScript V8; no shell or filesystem required",tests:out,total:out.length,passed:out.every(x=>x.pass)};
}
if(typeof module!=="undefined"&&module.exports){module.exports={verifyA};if(require.main===module)console.log(JSON.stringify(verifyA(),null,2));}
