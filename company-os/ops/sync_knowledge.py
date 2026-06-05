#!/usr/bin/env python3
import argparse, hashlib, json, os, sys, urllib.request, urllib.error
from pathlib import Path
ROOT=Path('/Users/minhcuong/.openclaw/workspace')
CONFIG=ROOT/'company-os/ops/dify_completion_gate_config.json'
STATE=ROOT/'company-os/ops/sync_knowledge_state.json'
LOG=ROOT/'company-os/ops/sync_knowledge.log'
DEFAULT_DIRS=[ROOT/'memory/areas', ROOT/'company-os/knowledge']
def md5(p): return hashlib.md5(p.read_bytes()).hexdigest()
def log(x): LOG.parent.mkdir(parents=True,exist_ok=True); LOG.open('a',encoding='utf-8').write(x+'\n'); print(x)
def request(method,url,key,payload=None):
    data=json.dumps(payload).encode() if payload is not None else None
    req=urllib.request.Request(url,data=data,method=method,headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode() or '{}')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--limit',type=int,default=0); ap.add_argument('--file'); ap.add_argument('--dataset-id',default=os.getenv('DIFY_DATASET_ID',''))
    a=ap.parse_args(); cfg=json.loads(CONFIG.read_text()); base=cfg['dify_base_url'].rstrip('/'); key=os.getenv('DIFY_DATASET_API_KEY') or cfg.get('dataset_api_key') or cfg.get('completion_gate_api_key')
    state=json.loads(STATE.read_text()) if STATE.exists() else {}
    files=[(ROOT/Path(a.file)).resolve() if a.file and not Path(a.file).is_absolute() else Path(a.file)] if a.file else [p for d in DEFAULT_DIRS if d.exists() for p in d.rglob('*.md')]
    changed=[]
    for p in files:
        if not p.exists(): continue
        h=md5(p); rel=str(p.relative_to(ROOT))
        if state.get(rel,{}).get('md5')!=h: changed.append((p,rel,h))
    if a.limit: changed=changed[:a.limit]
    log(f'SCAN changed={len(changed)} dry_run={a.dry_run}')
    for p,rel,h in changed:
        if a.dry_run or not a.dataset_id:
            state[rel]={'md5':h,'mode':'dry_run' if a.dry_run else 'no_dataset_id'}; log(f'DRY_UPDATE {rel} {h}'); continue
        payload={'name':rel,'text':p.read_text(encoding='utf-8',errors='ignore'),'indexing_technique':'high_quality','process_rule':{'mode':'automatic'}}
        res=request('POST',f'{base}/datasets/{a.dataset_id}/document/create_by_text',key,payload)
        state[rel]={'md5':h,'document_id':res.get('document',{}).get('id') or res.get('id'),'mode':'uploaded'}; log(f'UPLOADED {rel}')
    STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
