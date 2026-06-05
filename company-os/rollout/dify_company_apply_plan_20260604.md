# Dify Company Apply Plan — P0 — 2026-06-04

Owner: Cáo + Trợ Lý coordination
Status: PARTIAL draft, pending Trợ Lý A2A alignment and app/workflow auth test.

## Basis
- Local Dify evidence gate PASSED: `antigravity_tasks/outbox/result_task_a752b51d_20260604_133957.json`.
- canonical/local/artifact/mirror checked; secrets exposed = false.
- Scope is low-risk: read-only Company OS adoption plan; no production DB writes; no public exposure.

## P0 use-cases
1. CEO Company OS Knowledge Q&A
   - Input: `company-os/knowledge/`
   - Output: answers with cited local knowledge file paths.
   - Acceptance: 5/5 rule questions answered from KB; no token shown.

2. A2A / Task Evidence Lookup
   - Input: `memory/agent_task_bus.jsonl`, tech-ops logs, artifact registry if present.
   - Output: status answer in DONE/PARTIAL/BLOCKED/NOT_STARTED with evidence path.
   - Acceptance: given a task id, returns latest status + evidence + blocker + next.

3. Upharma Review Assistant — read-only
   - Input: review pack/QA files under `upharma/4_Ket_Qua_AI/drug_disease_poc_20260604/`.
   - Output: pharmacist review checklist, flags, prioritization.
   - Acceptance: no DB write; no medical claim beyond review assist; flags rows with source/evidence.

## Execution sequence
1. Cáo keeps Antigravity on technical executor/auth action.
2. Trợ Lý aligns business rollout and task ownership.
3. Create Dify app/workflow config mapping P0 use-cases if authenticated access is available.
4. Run read-only acceptance tests.
5. Report only evidence-backed status.

## Rollback
- Remove this rollout folder/files.
- Do not change production DB or public integrations.
