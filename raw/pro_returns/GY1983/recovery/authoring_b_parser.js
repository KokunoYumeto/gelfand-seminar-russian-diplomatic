function parsePythonCalls(source){
 source=source.replace(/V'/g,String.raw`V^{\prime}`);
 const out=[];const rx=/^(I|C|section)\(/gm;let m;
 while((m=rx.exec(source))){
  let p=m.index+m[0].length;const args=[],kw={};const ws=()=>{while(/\s/.test(source[p]||"")&&p<source.length)p++;};
  function value(){ws();let raw=false;if(source[p]==="r"&&["'",'"'].includes(source[p+1])){raw=true;p++;}
   if(["'",'"'].includes(source[p])){const q=source[p];const triple=source.slice(p,p+3)===q.repeat(3);const end=triple?q.repeat(3):q;p+=end.length;let s="";while(p<source.length){if(source.slice(p,p+end.length)===end){p+=end.length;return s;}let c=source[p++];if(c==="\\"&&!raw){const n=source[p++];s+=n==="n"?"\n":n==="r"?"\r":n==="t"?"\t":n;}else{s+=c;}}throw Error("Unclosed string at "+p);}
   const z=source.slice(p).match(/^(?:-?\d+(?:\.\d+)?|None|True|False)/);if(!z)throw Error("Expected literal near "+source.slice(p,p+90));p+=z[0].length;return z[0]==="None"?null:z[0]==="True"?true:z[0]==="False"?false:Number(z[0]);
  }
  while(true){ws();if(source[p]===")"){p++;break;}const k=source.slice(p).match(/^([A-Za-z_]\w*)\s*=/);if(k){p+=k[0].length;kw[k[1]]=value();}else args.push(value());ws();if(source[p]===","){p++;continue;}if(source[p]===")"){p++;break;}throw Error("Expected delimiter near "+source.slice(p-50,p+120));}
  out.push({name:m[1],args,kw});rx.lastIndex=p;
 }return out;
}