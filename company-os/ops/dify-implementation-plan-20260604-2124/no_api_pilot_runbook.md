# No-API Company OS pilot runbook — Dify-compatible

## Goal
Run Company OS pilots now while native Dify app/workflow/KB remains blocked by `/console/api/apps` 401.

## Runbook <=3 commands
```bash
cd /Users/minhcuong/.openclaw/workspace
python3 company-os/ops/apply-dashboard-20260604-2015/verify_apply_dashboard.py
python3 company-os/ops/antigravity-sync-bridge-20260604-2031/antigravity_sync_bridge.py --dry-run
```

## Pilot routing
1. Upharma CRM Import Review: read import-ready CSV + blocker/human-review files, generate approval-only report; no DB write.
2. A2A Evidence Dashboard: read canonical bus, enforce DONE/PARTIAL/STALLED/BLOCKED with evidence path/size.
3. Render Intake/Postflight: collect render output path, ffprobe duration/resolution/size, postflight report.

## Native Dify migration map
- Each pilot in `workflows.json` becomes one Dify workflow.
- Evidence files become KB documents.
- Antigravity bridge becomes intake node equivalent.
- Apply dashboard becomes human monitoring UI/reference.

## Rollback
Delete this folder only; no production DB touched.
