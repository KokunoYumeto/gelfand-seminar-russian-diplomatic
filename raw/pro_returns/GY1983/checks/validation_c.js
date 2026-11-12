// Standalone wrapper for the original in-memory validation, using this package.
const fs=require("fs"),path=require("path"),base=path.resolve(__dirname,"..");
const all=JSON.parse(fs.readFileSync(path.join(base,"GY1983_items.json"),"utf8"));
const bib=fs.readFileSync(path.join(base,"GY1983_references.bib"),"utf8");
const B={items:all.filter(x=>x.record>=620&&x.record<=630),references:[...bib.matchAll(/@\w+\s*\{\s*([^,\s]+)\s*,/g)].map(m=>({key:m[1]}))};
// Executed against the in-memory core bundle B on 2026-11-12.
const required = ["id","record","pages","kind","title","notes","statement",
 "reconstruction","class","fate","present_status","literal_correctness",
 "publication_match","verification","development","problem","worth","refs","confidence"];
const refset = new Set(B.references.map(r => r.key));
const ids = new Set(), duplicate_item_ids = [], missing_required_fields = [];
const unresolved_bibliography_keys = [], math_delimiter_mismatches = [];
for (const x of B.items) {
 if (ids.has(x.id)) duplicate_item_ids.push(x.id);
 ids.add(x.id);
 for (const k of required) if (!(k in x)) missing_required_fields.push([x.id,k]);
 for (const r of x.refs) if (!refset.has(r)) unresolved_bibliography_keys.push([x.id,r]);
 for (const k of ["notes","statement","reconstruction","fate"]) {
  const v = x[k] || "";
  if ((v.match(/\\\(/g)||[]).length !== (v.match(/\\\)/g)||[]).length)
   math_delimiter_mismatches.push([x.id,k,"inline"]);
  if ((v.match(/\\\[/g)||[]).length !== (v.match(/\\\]/g)||[]).length)
   math_delimiter_mismatches.push([x.id,k,"display"]);
 }
}

console.log(JSON.stringify({items:B.items.length,duplicate_item_ids,missing_required_fields,unresolved_bibliography_keys,math_delimiter_mismatches},null,2));
