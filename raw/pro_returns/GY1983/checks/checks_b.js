function rationalAudit(){
  const add=(p,q)=>{const r={...p};for(const [k,v] of Object.entries(q)){r[k]=(r[k]||0)+v;if(!r[k])delete r[k];}return r;};
  const mul=(p,q)=>{let r={};for(const [a,x] of Object.entries(p))for(const[b,y]of Object.entries(q)){const c=a.split(",").map((n,i)=>+n+(+b.split(",")[i])).join(",");r[c]=(r[c]||0)+x*y;}return r;};
  const neg=p=>Object.fromEntries(Object.entries(p).map(([k,v])=>[k,-v]));
  const compose=(p,q)=>q.split("").map(n=>p[+n]).join("");
  const gm=(a,b)=>{const r={};for(const[p,x]of Object.entries(a))for(const[q,y]of Object.entries(b)){const k=compose(p,q);r[k]=add(r[k]||{},mul(x,y));}return r;};
  const U={"1,0,0":1},V={"0,1,0":1},Z={"0,0,1":1};
  const R=(p,swap)=>({"012":p,[swap]:Z});
  const lhs=gm(gm(R(U,"102"),R(add(U,V),"210")),R(V,"021"));
  const rhs=gm(gm(R(V,"021"),R(add(U,V),"210")),R(U,"102"));
  const difference={};for(const p of new Set([...Object.keys(lhs),...Object.keys(rhs)])){const x=add(lhs[p]||{},neg(rhs[p]||{}));if(Object.keys(x).length)difference[p]=x;}
  const hookDimension=rows=>{let fact=1n;const n=rows.reduce((a,b)=>a+b,0);for(let k=2n;k<=BigInt(n);k++)fact*=k;let den=1n;for(let i=0;i<rows.length;i++)for(let j=0;j<rows[i];j++){let below=0;for(let r=i+1;r<rows.length;r++)if(rows[r]>j)below++;den*=BigInt(rows[i]-j+below);}return String(fact/den);};
  return {method:"Exact integer polynomial arithmetic in C[u,v,z][S3]; z denotes i*c",identity:"R12(u) R13(u+v) R23(v) = R23(v) R13(u+v) R12(u), R(w)=w I+z P",nonzeroDifferenceTerms:difference,passed:Object.keys(difference).length===0,hookDimensions:{"(3,2,1)":hookDimension([3,2,1]),"(5,4,3,2,1)":hookDimension([5,4,3,2,1])},interpretation:"Normalizing each factor by w+z preserves the identity wherever denominators are nonzero; meromorphic continuation supplies the remaining interpretation. This checks a known identity, not a new theorem."};
}
console.log(JSON.stringify(rationalAudit(), null, 2));
