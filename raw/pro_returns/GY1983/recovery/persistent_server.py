import sys,os,json,pathlib,subprocess,base64,traceback
root=pathlib.Path("/workspace/scratch/242c4b12362c")
root.mkdir(parents=True,exist_ok=True)
(root/"work").mkdir(exist_ok=True)
print(json.dumps({"ready":True,"root":str(root)}),flush=True)
for line in sys.stdin:
 try:
  q=json.loads(line)
  op=q.get("op")
  if op=="write":
   p=root/q["path"];p.parent.mkdir(parents=True,exist_ok=True)
   with p.open(q.get("mode","w"),encoding="utf-8") as f:f.write(q["text"])
   out={"written":q["path"],"bytes":p.stat().st_size}
  elif op=="run":
   r=subprocess.run(q["cmd"],cwd=root/q.get("cwd",""),input=q.get("input"),text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=q.get("timeout",240))
   out={"returncode":r.returncode,"output":r.stdout}
  elif op=="read":
   p=root/q["path"];data=p.read_bytes();start=q.get("offset",0);data=data[start:start+q.get("length",len(data))]
   out={"path":q["path"],"offset":start,"file_size":p.stat().st_size,"data":base64.b64encode(data).decode() if q.get("base64") else data.decode()}
  elif op=="stat":
   out={"files":[{"path":str(p.relative_to(root)),"bytes":p.stat().st_size} for p in root.rglob("*") if p.is_file()]}
  elif op=="exit":break
  else:out={"error":"unknown operation"}
 except Exception as e:out={"error":str(e),"type":type(e).__name__}
 print(json.dumps(out,ensure_ascii=False),flush=True)
