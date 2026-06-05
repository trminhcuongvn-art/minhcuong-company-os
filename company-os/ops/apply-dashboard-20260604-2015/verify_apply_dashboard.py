#!/usr/bin/env python3
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[3]
data=json.loads((pathlib.Path(__file__).parent/'apply_dashboard.json').read_text(encoding='utf-8'))
fail=[]
for r in data['evidence']:
    p=root/r['path']
    size=p.stat().st_size if p.exists() else 0
    print(f"{('OK' if size==r['size_bytes'] and size>0 else 'MISS')}	{size}	{r['path']}")
    if size!=r['size_bytes'] or size<=0: fail.append(r['path'])
print('ROLLBACK:', data['rollback'])
sys.exit(1 if fail else 0)
