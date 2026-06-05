# Antigravity canonical A2A sync bridge — runbook

Mirror `memory/agent_task_bus.jsonl` tasks with `to_agent=antigravity` and `status=NEW` into `antigravity_tasks/inbox/*.json`. Idempotent by canonical `message_id/task_id`; writes state/log only in this ops folder. Secrets are redacted in generated JSON/log text.

## Runbook (<=3 lệnh)
```bash
cd /Users/minhcuong/.openclaw/workspace
python3 company-os/ops/antigravity-sync-bridge-20260604-2031/antigravity_sync_bridge.py --dry-run --fixture
python3 company-os/ops/antigravity-sync-bridge-20260604-2031/antigravity_sync_bridge.py
```

## Rollback
```bash
rm -f antigravity_tasks/inbox/task_a2a_*.json; rm -rf company-os/ops/antigravity-sync-bridge-20260604-2031
```

## Test evidence
Dry-run fixture executed at 2026-06-04 20:32 ICT. It found 3 candidates, would mirror fixture `FIXTURE-A2A-ANTIGRAVITY-DRYRUN-20260604-2031`, and skipped already mirrored `A2A-CAO-ANTIGRAVITY-DIFY-COMPANY-APPLY-20260604-2015` pointing to `antigravity_tasks/inbox/task_ce823e8b_20260604_202912.json`.
