#!/usr/bin/env python3
import os,re,json,datetime,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'company-os/ops'
patterns=[re.compile(r'Bearer\s+([A-Za-z0-9_\-\.]{20,})'),re.compile(r'(?:api[_-]?key|token|authorization)["\'\s:=]+([A-Za-z0-9_\-\.]{20,})',re.I)]
scan_dirs=[ROOT/'memory/areas/tech-ops/dify_evidence_20260604',ROOT/'company-os',ROOT/'antigravity_tasks']
found=[]
for d in scan_dirs:
 if d.exists():
  for p in d.rglob('*'):
   if p.is_file() and p.stat().st_size<200000:
    txt=p.read_text(errors='ignore')
    for pat in patterns:
     for m in pat.finditer(txt):
      tok=m.group(1); found.append({'path':str(p),'kind':'candidate','prefix':tok[:4]+'...','len':len(tok)})
# non-secret endpoint probes only, no candidate used unless env DIFY_API_TOKEN set
def curl(url,token=None):
 cmd=['curl','-sS','-o','/tmp/dify_probe_body','-w','%{http_code}','--max-time','5']
 if token: cmd += ['-H',f'Authorization: Bearer {token}']
 cmd.append(url)
 try: return subprocess.check_output(cmd,text=True).strip()
 except Exception as e: return 'ERR:'+str(e)
res={'checked_at':datetime.datetime.now().isoformat(),'base':'http://localhost','unauth':{},'auth':None,'candidates_redacted':found[:20], 'status':'BLOCKED','blocker':None,'next':None}
for ep in ['/console/api/apps','/console/api/datasets','/console/api/system-features']:
 res['unauth'][ep]=curl('http://localhost'+ep)
tok=os.environ.get('DIFY_API_TOKEN') or os.environ.get('DIFY_CONSOLE_TOKEN')
if tok:
 res['auth']={'/console/api/apps':curl('http://localhost/console/api/apps',tok),'token':'[REDACTED]'}
 res['status']='DONE' if res['auth']['/console/api/apps'].startswith('2') else 'BLOCKED'
 res['blocker']=None if res['status']=='DONE' else 'Provided token did not authorize /console/api/apps'
else:
 res['blocker']='No approved DIFY_API_TOKEN/DIFY_CONSOLE_TOKEN env available; only redacted candidates found in local files, not used.'
 res['next']='Set approved env token or use browser-auth session export; do not store raw token in repo.'
out=OUT/f"dify_auth_probe_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
out.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print(out)
print(json.dumps(res,ensure_ascii=False,indent=2))
