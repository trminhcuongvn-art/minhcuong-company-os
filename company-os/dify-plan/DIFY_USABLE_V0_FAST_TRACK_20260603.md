# Dify Usable v0 Fast Track — 2026-06-03

## Deadline
- 16:15 usable v0
- 16:30 hard checkpoint

## Minimal scope
1. Runtime/API already DONE.
2. Use currently working Dify app/workflow keys.
3. Company Knowledge Assistant v0: ingest only core docs first:
   - ACTIVE_RULES.md
   - memory/DASHBOARD.md
   - company-os/dify-plan/DIFY_COMPANY_USAGE_GUIDE.md
   - company-os/dify-plan/DIFY_KB_INGEST_CHECKLIST_20260603.md
   - company-os/dify-plan/DIFY_WORKFLOW_NODE_SPEC_20260603.md
   - company-os/docs/multi_agent_operating_model_v0.md
   - company-os/roles/troly_job_description.md
4. Task Router v0: return JSON owner/risk/evidence/next.
5. Acceptance: 5 KB questions + 3 routing tasks.

## Manual UI checklist if automation blocked
- Knowledge → Create: Company OS Knowledge Base
- Upload/import core docs above
- App → Company Knowledge Assistant → Context/Knowledge → attach KB
- Publish changes
- Workflow → Company Task Intake Router → configure classifier prompt from node spec → map output to End → Publish changes

## Pass criteria
- Chat API answer is not just "ok".
- Workflow output is not empty `{}`.
- At least 3/5 KB questions pass with source/path or explicit evidence note.
- 3/3 routing tasks return owner + risk + evidence_required.
