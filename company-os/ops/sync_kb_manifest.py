#!/usr/bin/env python3
"""Sync priority KB files from manifest to Dify dataset. Run by cron every 4h."""
import json, hashlib, urllib.request, urllib.error
from pathlib import Path

ROOT = Path('/Users/minhcuong/.openclaw/workspace')
MANIFEST = ROOT / 'company-os/ops/kb_sync_manifest.json'
STATE = ROOT / 'company-os/ops/sync_kb_manifest_state.json'
CONFIG = ROOT / 'company-os/ops/dify_completion_gate_config.json'

def md5(p): return hashlib.md5(p.read_bytes()).hexdigest()

def upload(base, token, dataset_id, name, text):
    payload = {'name': name, 'text': text, 'indexing_technique': 'high_quality', 'process_rule': {'mode': 'automatic'}}
    req = urllib.request.Request(f'{base}/datasets/{dataset_id}/document/create-by-text',
        data=json.dumps(payload).encode(),
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        method='POST')
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def main():
    cfg = json.loads(CONFIG.read_text())
    manifest = json.loads(MANIFEST.read_text())
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    base = cfg['dify_base_url'].rstrip('/')
    token = cfg['dataset_api_key']
    dataset_id = manifest['dataset_id']

    synced, skipped, errors = 0, 0, 0
    for rel in manifest['include']:
        p = ROOT / rel
        if not p.exists():
            print(f'MISSING {rel}'); errors += 1; continue
        h = md5(p)
        if state.get(rel, {}).get('md5') == h:
            skipped += 1; continue
        try:
            upload(base, token, dataset_id, rel, p.read_text(errors='ignore'))
            state[rel] = {'md5': h}
            print(f'SYNCED {rel}'); synced += 1
        except urllib.error.HTTPError as e:
            print(f'ERR {rel} {e.code} {e.read().decode()[:80]}'); errors += 1

    STATE.write_text(json.dumps(state, indent=2))
    print(f'DONE synced={synced} skipped={skipped} errors={errors}')

if __name__ == '__main__':
    main()
