function checkRecoveryMathematics() {
  const assert = (b, m) => { if (!b) throw Error(m); };
  const pop = x => { let k=0; for (;x;x&=x-1) k++; return k; };
  const bin = (n,k) => {
    if(k<0 || k>n || n<0) return 0n;
    let a=1n;
    for(let i=1;i<=k;i++) a=a*BigInt(n-i+1)/BigInt(i);
    return a;
  };
  const fact = n => {
    let a=1n;
    for(let i=2;i<=n;i++) a*=BigInt(i);
    return a;
  };
  const convolution = (a,b) => {
    const c=Array(a.length+b.length-1).fill(0n);
    a.forEach((u,i)=>b.forEach((v,j)=>c[i+j]+=u*v));
    return c;
  };
  const plusMinus = (m,k) => convolution(
    Array.from({length:m-k+1},(_,i)=>bin(m-k,i)),
    Array.from({length:k+1},(_,i)=>(k-i)%2 ? -bin(k,i):bin(k,i))
  );
  const stats={};

  function graph(n,edges) {
    const m=edges.length, cuts=new Map();
    const spin=Array(m+1).fill(0n), even=Array(m+1).fill(0n);
    for(let s=0;s<(1<<n);s++) {
      let mask=0;
      edges.forEach(([u,v],e)=>{
        if(((s>>u)^(s>>v))&1) mask|=1<<e;
      });
      cuts.set(mask,(cuts.get(mask)||0)+1);
      spin[m-pop(mask)]+=1n<<BigInt(m);
    }
    for(let a=0;a<(1<<m);a++) {
      let parity=0;
      edges.forEach(([u,v],e)=>{
        if(a&(1<<e)) parity^=(1<<u)|(1<<v);
      });
      if(!parity) even[pop(a)]++;
    }
    const rhs=Array(m+1).fill(0n);
    even.forEach((v,k)=>{
      if(v) plusMinus(m,k).forEach((c,i)=>{
        rhs[i]+=c*v*(1n<<BigInt(n));
      });
    });
    assert(spin.every((v,i)=>v===rhs[i]),"Graph polynomial identity");
    const parent=Array.from({length:n},(_,i)=>i);
    const root=u=>{
      while(parent[u]!==u) u=parent[u];
      return u;
    };
    for(const [u,v] of edges) parent[root(u)]=root(v);
    const components=new Set(parent.map((_,u)=>root(u))).size;
    assert([...cuts.values()].every(v=>v===2**components),
           "Cut fibre multiplicity");
    const cutpoly=Array(m+1).fill(0);
    for(const a of cuts.keys()) cutpoly[pop(a)]++;
    return {even:even.map(Number),cuts:cutpoly};
  }

  let count=0;
  const byVertices={};
  for(let n=1;n<=5;n++) {
    const complete=[];
    for(let u=0;u<n;u++)
      for(let v=u+1;v<n;v++) complete.push([u,v]);
    byVertices[n]=1<<complete.length;
    for(let g=0;g<(1<<complete.length);g++) {
      graph(n,complete.filter((_,i)=>g&(1<<i)));
      count++;
    }
  }
  stats.graphs={count,byVertices};
  const cube=[];
  for(let u=0;u<8;u++)
    for(let i=0;i<3;i++) {
      const v=u^(1<<i);
      if(u<v) cube.push([u,v]);
    }
  stats.cube=graph(8,cube);

  function rank(rows) {
    const pivots=new Map();
    let r=0;
    for(let a of rows) {
      while(a) {
        const p=a.toString(2).length-1;
        if(pivots.has(p)) a^=pivots.get(p);
        else { pivots.set(p,a); r++; break; }
      }
    }
    return r;
  }

  stats.tori=[];
  for(const L of [3,4]) {
    const N=L**3;
    const idx=c=>c[0]+L*(c[1]+L*c[2]);
    const coords=Array.from({length:N},(_,v)=>[
      v%L,Math.floor(v/L)%L,Math.floor(v/L/L)
    ]);
    const edges=[], lookup=new Map();
    const step=(c,d)=>c.map((x,i)=>i===d?(x+1)%L:x);
    const key=(u,v)=>u<v?u+","+v:v+","+u;
    coords.forEach(c=>{
      for(let d=0;d<3;d++) {
        const u=idx(c),v=idx(step(c,d));
        lookup.set(key(u,v),edges.length);
        edges.push([u,v,c,d]);
      }
    });
    const bit=(c,d)=>1n<<BigInt(
      lookup.get(key(idx(c),idx(step(c,d))))
    );
    const stars=Array(N).fill(0n), faces=[];
    let seam=0n;
    edges.forEach(([u,v,c,d],e)=>{
      stars[u]^=1n<<BigInt(e);
      stars[v]^=1n<<BigInt(e);
      if(d===0 && c[0]===L-1) seam|=1n<<BigInt(e);
    });
    coords.forEach(c=>{
      for(let a=0;a<3;a++)
        for(let b=a+1;b<3;b++)
          faces.push(bit(c,a)^bit(step(c,a),b)^
                     bit(step(c,b),a)^bit(c,b));
    });
    const parity=x=>{
      let p=0;
      for(;x;x&=x-1n) p^=1;
      return p;
    };
    assert(faces.every(f=>parity(f&seam)===0),"Seam locally closed");
    let winding=0n;
    for(let x=0;x<L;x++) winding^=bit([x,0,0],0);
    assert(parity(winding&seam)===1,"Seam not a cut");
    const cutRank=rank(stars);
    const closedDimension=edges.length-rank(faces);
    assert(cutRank===N-1 && closedDimension-cutRank===3,
           "Torus cohomology");
    stats.tori.push({
      L,cutRank,closedDimension,
      sectors:2**(closedDimension-cutRank)
    });
  }

  function tuples(bounds,fn,a=[],i=0) {
    if(i===bounds.length) { fn(a.slice()); return; }
    for(let k=0;k<=bounds[i];k++) {
      a[i]=k; tuples(bounds,fn,a,i+1);
    }
  }

  let degreeCases=0;
  for(let d=2;d<=4;d++) {
    const Q=[];
    for(let mask=1;mask<(1<<d);mask++) {
      const s=pop(mask);
      if(s>=2) Q.push({
        e:Array.from({length:d},(_,i)=>(mask>>i)&1),
        c:BigInt(s-1)
      });
    }
    let power=new Map([[Array(d).fill(0).join(","),1n]]);
    const coeff=new Map();
    for(let r=0;r<=Math.floor(3*d/2);r++) {
      for(const [key,c] of power)
        coeff.set(key,(coeff.get(key)||0n)+BigInt(r+1)*c);
      const next=new Map();
      for(const [key,c] of power) {
        const a=key.split(",").map(Number);
        for(const q of Q) {
          const b=a.map((x,i)=>x+q.e[i]);
          if(b.every(x=>x<=3)) {
            const k=b.join(",");
            next.set(k,(next.get(k)||0n)+c*q.c);
          }
        }
      }
      power=next;
    }
    tuples(Array(d).fill(3),ell=>{
      const total=ell.reduce((a,b)=>a+b,0);
      if(!total) return;
      let jet=0n, restored=0n;
      tuples(ell,k=>{
        const s=k.reduce((a,b)=>a+b,0),r=total-s;
        let denominator=1n,chern=1n,p1=1n,p2=1n;
        for(let i=0;i<d;i++) {
          denominator*=fact(ell[i]-k[i]);
          chern*=bin(ell[i]+1,k[i]);
          p1*=bin(s,k[i])*bin(s+1+ell[i]-k[i],ell[i]-k[i]);
          p2*=bin(s-1,k[i])*bin(s+ell[i]-k[i],ell[i]-k[i]);
        }
        jet+=(s%2?-1n:1n)*BigInt(r+1)*fact(r)/denominator*chern;
        restored+=(r%2?-1n:1n)*(BigInt(s+1)*p1-BigInt(s)*p2);
      });
      const expected=coeff.get(ell.join(","))||0n;
      assert(jet===expected,"Jet degree "+ell);
      assert(restored===expected,"Restored degree "+ell);
      degreeCases++;
    });
  }
  stats.hyperdeterminants={degreeCases,failures:0};
  stats.note="Executed in the JavaScript tool after the filesystem outage; this is independent recovery code, not byte-identical recovery of the original Python programs.";
  return stats;
}

console.log(JSON.stringify(checkRecoveryMathematics(),null,2));
