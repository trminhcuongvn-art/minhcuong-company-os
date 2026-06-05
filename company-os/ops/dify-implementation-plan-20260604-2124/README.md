# Dify implementation plan — Company OS

Time: 2026-06-04 21:24 ICT
Owner: Cáo supervise; Trợ Lý implement; Antigravity verify UI/queue; Bông provides Upharma pilot data.

## Why progress looked stalled
Dify runtime is UP, but native console API `/console/api/apps` returns `401 UNAUTHORIZED`, so app/workflow/KB cannot be created by unauthenticated API. I kept repeating health checks instead of pushing the next safe offline lane. Corrective action: run two lanes in parallel.

## Lane A — Native Dify unblock
Goal: create real Dify app/workflow/KB when auth/provider is available.
1. Audit auth/session/token path and provider credential requirement.
2. Verify if browser/user session can access console and export/import app config.
3. If token available, create pilot objects:
   - App: Company Ops Evidence Auditor
   - Knowledge base: Company OS runbooks/evidence logs
   - Workflow: A2A task intake -> evidence gate -> status report
4. Export artifacts under this folder; no production DB writes.

Acceptance:
- `/console/api/apps` authenticated 200 or browser-created app visible.
- Export path, app id/name, KB id/name, workflow id/name.
- Rollback documented: delete created Dify app/KB/workflow.

Blocker:
- Need authenticated Dify console/API session and provider credential for model execution.

## Lane B — No-API Company OS pilot now
Goal: deliver usable Company OS workflow without waiting for native Dify.
1. Use existing apply dashboard as control plane.
2. Make runbook for 3 pilots:
   - Upharma CRM import review
   - Agent A2A evidence dashboard
   - Render task intake/evidence postflight
3. Create JSON workflow specs compatible with future Dify import.
4. Wire Antigravity canonical sync bridge as task intake.

Acceptance:
- At least 3 workflow spec JSON files.
- README/runbook <=3 commands.
- Verification log checks referenced evidence paths.

## Timeline
- T+15m: plan + task delegation artifact DONE.
- T+45m: no-API pilot specs + verification DONE.
- T+90m: native auth audit result: DONE or BLOCKER with exact missing credential/session.
- T+180m: if auth solved, native Dify app/KB/workflow created; else no-API pilot remains operational.

## Rollback
Delete `company-os/ops/dify-implementation-plan-20260604-2124/` and any native Dify app/KB/workflow created during Lane A.
