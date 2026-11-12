function support() {
 const clone=x=>JSON.parse(JSON.stringify(x));
 function bibEntries(s) {
  const out=[]; let pos=0;
  while(pos<s.length) {
   const m=/@([A-Za-z]+)\s*\{/g; m.lastIndex=pos;const q=m.exec(s);if(!q)break;
   let p=m.lastIndex,depth=1,escaped=false;
   for(;p<s.length;p++){const c=s[p];if(escaped){escaped=false;continue;}if(c==="\\"){escaped=true;continue;}if(c==="{")depth++;if(c==="}"&&--depth===0)break;}
   if(depth)throw Error("Unbalanced BibTeX entry at "+q.index);
   const raw=s.slice(q.index,p+1),key=raw.match(/^@\w+\s*\{\s*([^,\s]+)\s*,/)?.[1];
   if(key)out.push({key,raw});pos=p+1;
  }
  return out;
 }
 const page=s=>String(s||"").replace(/P0*(\d+)/g,"$1").replace(/[–—]/g,"--");
 const normItem=i=>{
  i=clone(i);i.pages=page(i.pages);
  if(i.fate)i.fate=i.fate.replace(/Verified locator:/g,"Locator and verification scope:");
  for(const [k,v]of Object.entries(i))if(typeof v==="string")i[k]=v.replace(/\u200b/g,"").replace(/hardyramanujan1918partitions/g,"hardyramanujan1918asymptotic");
  i.refs=(i.refs||[]).map(k=>k==="hardyramanujan1918partitions"?"hardyramanujan1918asymptotic":k);
  if(i.literal_assessment && /malformed|wrong|inconsistent|must include|requires correction|require correction|BD-zero|N-versus-M/i.test(i.literal_assessment))i.literal_correctness="false as written";
  return i;
 };
 const normTalk=t=>{t=clone(t);if(t.actual_pages){t.catalogue_pages=t.pages;t.pages=t.actual_pages;}t.pages=page(t.pages);return t;};
 const normProblem=p=>{
  p=clone(p);p.status_date=p.status_date||"2026-11";p.status=p.status||p.present_status||p.fate||"";
  p.refs=(p.refs||[]).map(k=>k==="hardyramanujan1918partitions"?"hardyramanujan1918asymptotic":k);
  for(const[k,v]of Object.entries(p))if(typeof v==="string")p[k]=v.replace(/hardyramanujan1918partitions/g,"hardyramanujan1918asymptotic");
  return p;
 };
 function normCorrection(c){
  c=clone(c);c.type_original=c.type;const t=String(c.type||"").toLowerCase();
  c.type=/translat/.test(t)?"translation":/transcript|ocr/.test(t)&&!/not |conditional/.test(t)?"transcription":/provenance|histor|chronolog|date|bibliographic/.test(t)?"provenance":/ambigu|unresolved|underspec|under-spec|clarification|hypothes|scope|convention|normalization/.test(t)?"ambiguity":"faithful_error";
  return c;
 }
 const csv=(rows,fields)=>fields.join(",")+"\n"+rows.map(r=>fields.map(f=>'"'+String(r[f]??"").replace(/"/g,'""')+'"').join(",")).join("\n")+"\n";
 const count=(rows,key)=>rows.reduce((o,r)=>(o[r[key]]=(o[r[key]]||0)+1,o),{});
 return{clone,bibEntries,page,normItem,normTalk,normProblem,normCorrection,csv,count};
}