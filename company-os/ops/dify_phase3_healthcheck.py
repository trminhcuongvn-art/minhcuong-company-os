#!/usr/bin/env python3
from pathlib import Path
import json, sys, time
ROOT=Path('/Users/minhcuong/.openclaw/workspace')
checks=[]
def check(name, cond, detail=''):
    checks.append({'name':name,'ok':bool(cond),'detail':detail})

files=[
 'company-os/ops/dify_app_registry.json',
 'company-os/ops/dify_completion_gate_caller.py',
 'company-os/ops/agent_dispatch_wrapper.sh',
 'company-os/ops/kb_sync_manifest.json',
 'company-os/ops/domain_kb_manifest.json',
 'company-os/docs/DIFY_USER_GUIDE_V1.md',
 'company-os/docs/DIFY_PHASE3_RUNBOOK.md',
 'memory/areas/tech-ops/SKILL_APP_REGISTRY.md'
]
for f in files:
    p=ROOT/f
    check(f, p.exists() and p.stat().st_size>0, str(p.stat().st_size if p.exists() else 0))

try:
    reg=json.loads((ROOT/'company-os/ops/dify_app_registry.json').read_text())
    check('apps>=7', len(reg) >= 7 if isinstance(reg,list) else len(reg.get('apps',[]))>=7, 'registry loaded')
except Exception as e:
    check('apps>=7', False, str(e))

try:
    km=json.loads((ROOT/'company-os/ops/kb_sync_manifest.json').read_text())
    paths=km.get('paths') or km.get('files') or []
    check('kb_manifest_paths>0', len(paths)>0, str(len(paths)))
except Exception as e:
    check('kb_manifest_paths>0', False, str(e))

try:
    bus=(ROOT/'memory/agent_task_bus.jsonl').read_text(errors='ignore').splitlines()
    recent='\n'.join(bus[-50:])
    check('a2a_gate_recent', 'phase2_gate_test_bong' in recent or 'bong_drug_enrich_fullsku' in recent, 'bus recent checked')
except Exception as e:
    check('a2a_gate_recent', False, str(e))

ok=all(c['ok'] for c in checks)
out={'status':'PASS' if ok else 'FAIL','checked_at':'2026-06-05T13:22:00+07:00','checks':checks}
print(json.dumps(out,ensure_ascii=False,indent=2))
sys.exit(0 if ok else 1)
