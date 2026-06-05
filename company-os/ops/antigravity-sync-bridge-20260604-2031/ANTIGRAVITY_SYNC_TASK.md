# Antigravity canonical A2A sync bridge task — 2026-06-04 20:31 ICT

Owner: Antigravity + Trợ Lý, supervised by Cáo.

## Problem
Cáo dispatched `A2A-CAO-ANTIGRAVITY-DIFY-COMPANY-APPLY-20260604-2015` into canonical `memory/agent_task_bus.jsonl`, but Antigravity executor actually watches `antigravity_tasks/inbox/*.json`. This caused no ACK until Cáo manually resubmitted a queue task.

## Mission
Create/verify a safe bridge so canonical tasks addressed to `antigravity` are mirrored into `antigravity_tasks/inbox/*.json`, and results from `antigravity_tasks/outbox/*.json` are summarized back into canonical task bus/log.

## Requirements
1. No production DB write, no external outreach, no secrets exposure.
2. Read only canonical bus: `memory/agent_task_bus.jsonl`.
3. Write only bridge artifacts under `company-os/ops/antigravity-sync-bridge-20260604-2031/` and Antigravity queue files under `antigravity_tasks/inbox/`.
4. Handle duplicate tasks idempotently; do not create duplicate inbox tasks for same canonical message_id.
5. Output README/runbook <=3 commands, status file, and rollback.

## Acceptance
- Path + file sizes reported.
- Dry-run or test task proves canonical-to-inbox sync.
- Rollback command documented.
- Logs include exact task ids and no raw credentials.

## Rollback
Delete `company-os/ops/antigravity-sync-bridge-20260604-2031/` and any test inbox/outbox task created by this task.
