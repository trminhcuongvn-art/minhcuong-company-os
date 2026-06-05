# Dify Application Plan for Minh Cường Company OS

## Role of Dify
Dify không thay OpenClaw. Dify dùng làm lớp Knowledge/RAG + Workflow App cho SOP, decision memory, task registry và company assistant apps.

## Immediate use cases
1. Company OS Knowledge Base
- Ingest: ACTIVE_RULES.md, DASHBOARD.md, memory/areas/*, company-os/docs, role charters.
- Output: hỏi nhanh "quy tắc hiện tại là gì", "task này thuộc ai", "blocker trước đó là gì".

2. Agent SOP Assistant
- App cho Trợ Lý/Cáo/Bông/Bún tra SOP và evidence rules.
- Giảm lỗi rule nằm trong memory nhưng không nằm trong flow.

3. Task Intake Classifier
- Workflow nhận yêu cầu Henry → phân loại domain/risk/owner đề xuất/acceptance criteria.
- Không tự public hoặc ghi dữ liệu; chỉ tạo draft task.

4. Evidence Auditor
- Workflow nhận task_id + artifact path → kiểm có evidence hợp lệ không.
- Output: PASS/FAIL + lý do.

5. Customer/Business Knowledge Apps
- Upharma management Q&A trên báo cáo/data docs.
- BaDiVi content/growth knowledge base.

## Phasing
Phase 0 — Install & local trial
- Start Dify local Docker/Colima.
- Create admin + first app manually/local.
- No public exposure.

Phase 1 — Knowledge Base POC
- Ingest Company OS docs + 5–10 memory files.
- Test 20 questions: rules, owner, evidence, current priorities.
- Acceptance: >=80% answers cite correct source.

Phase 2 — Workflow POC
- Build Task Intake Classifier workflow.
- Input: Henry message.
- Output: JSON task with owner/risk/evidence/deadline.

Phase 3 — Integrate with OpenClaw
- Dify becomes callable knowledge/workflow layer.
- OpenClaw remains executor/orchestrator.
- Registry remains source of truth in files/jsonl.

## Guardrails
- No sensitive customer data public.
- Local only until explicit approval.
- Dify answers are advisory; evidence registry decides DONE.
- Rollback: stop Docker compose / remove local app.

## Success metrics
- Time to classify task < 30s.
- Evidence reporting errors reduced.
- Fewer repeated questions about rules.
- 8h block reports generated with source citations.
