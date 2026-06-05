# Company OS No-API Runbook — 2026-06-04 16:42 ICT

Canonical mode: Local Company Ops no-API fallback. Dify API auth is optional and not a blocker.

## Run command
```bash
cd /Users/minhcuong/.openclaw/workspace
./company-os/ops/dify_ops_loop.sh
```

## Loop actions
1. Dispatch registry tasks to `memory/agent_task_bus.jsonl`.
2. Scan SLA/ACK and mark stale `IN_PROGRESS` tasks `BLOCKED`.
3. Run evidence gate. DONE/PARTIAL requires existing evidence paths with byte sizes.
4. Write loop log under `company-os/ops/dify_ops_loop_*.log`.

## Task registry
Path: `company-os/ops/task_registry.jsonl`
Required fields: `task_id`, `owner`, `status`, `title`, `created_at`, `updated_at`, `evidence`, `blocker`, `next`, `rollback`.
Allowed status: `NOT_STARTED`, `PARTIAL`, `DONE`, `BLOCKED`, `STALLED`, `KILLED`.

## Evidence rule
No evidence path/size/log => no DONE/PARTIAL.
Production DB write/outreach requires approval.

## Reporting format
`Task / Owner / Status / Evidence / Blocker / Next`
Delta-only; do not repeat stale evidence.

## Rollback
Remove no-API ops artifacts:
```bash
rm -rf company-os/ops/p0_results
rm -f company-os/ops/COMPANY_OS_NO_API_RUNBOOK_20260604_1642.md
```
Do not remove historical logs unless explicitly requested.
