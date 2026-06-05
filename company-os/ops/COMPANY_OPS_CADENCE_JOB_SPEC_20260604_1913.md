# Company Ops Cadence Job Spec — 2026-06-04 19:13 ICT

Status: READY_TO_ENABLE

## Purpose
Run Company OS no-API operating cadence without relying on Dify API auth.

## Cadence
- Every 15m: Company Ops/Dify health + material delta check.
- Every 30m: Bông/Bún WIP evidence audit.
- Every 45m: cross-track evidence audit.
- Every 8h: block review + next block WIP limit max 3.

## Required behavior
Each checkpoint must output either:
1. new artifact path + size + status, or
2. `NO_NEW_ARTIFACT` with blocker/next.

No health-only report.

## Loop command
```bash
cd /Users/minhcuong/.openclaw/workspace
./company-os/ops/dify_ops_loop.sh
```

## Acceptance statuses
Allowed: DONE, PARTIAL, BLOCKED, STALLED, KILLED.
Forbidden: ACTIVE/ONGOING without evidence.

## Current canonical artifacts
- `company-os/ops/COMPANY_OS_NO_API_RUNBOOK_20260604_1642.md`
- `company-os/ops/COMPANY_OS_USABLE_DECISION_20260604_1828.md`
- `company-os/ops/COMPANY_OS_APPLY_TRIAL_20260604_1731.json`

## Rollback
Do not delete evidence logs. Disable cadence by removing/updating the scheduler job only.
