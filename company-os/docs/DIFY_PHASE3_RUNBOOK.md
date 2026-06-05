# Dify Phase 3 Runbook — Production Ops
Updated: 2026-06-05 13:22 ICT
Owner: Cáo

## Scope
Operate Dify apps as company workflow backbone: agent task reporting, KB-backed Q&A, domain workflows, monitoring, rollback.

## Daily Operating Flow
1. Agent receives task.
2. Agent completes work with evidence path + rollback.
3. Agent reports via `company-os/ops/agent_dispatch_wrapper.sh`.
4. Cáo reviews DONE/PARTIAL/BLOCKED from task bus/gate.
5. KB sync runs every 4h via `sync_kb_manifest.py`.

## Agent Reporting Command
```bash
bash company-os/ops/agent_dispatch_wrapper.sh <agent> <task_id> <DONE|PARTIAL|BLOCKED> "<evidence_path>" "<next>"
```

## Monitoring
- Cron job: `dify-kb-sync-4h` every 4h.
- Completion gate output: `/tmp/gate_<agent>_<task>.json`.
- Task bus: `memory/agent_task_bus.jsonl`.
- KB manifest: `company-os/ops/kb_sync_manifest.json`.
- Domain KB routing: `company-os/ops/domain_kb_manifest.json`.

## Rollback
- Disable cron job `dify-kb-sync-4h`.
- Revert `kb_sync_manifest.json` from git/manual backup.
- Stop using wrapper and append manual A2A result to task bus.
- Keep production DB writes disabled unless Henry explicitly approves.

## Escalation Rules
- No evidence path → not DONE.
- Blocker >30m → fallback or escalate.
- Credentials/password changes → Henry confirmation required.
