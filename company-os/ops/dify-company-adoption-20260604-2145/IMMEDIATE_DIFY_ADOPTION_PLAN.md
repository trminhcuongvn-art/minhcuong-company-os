# Kế hoạch áp dụng Dify ngay lập tức cho Minh Cường Group

Time: 2026-06-04 21:55 ICT
Owner: Cáo supervise; Trợ Lý implement; Bông/Bún/Render provide domain workflows.

## 0. Nhận định sau khi nghiên cứu lại
Dify không chỉ là chatbot. Dify là nền tảng dựng AI app gồm: Chatbot/Chatflow, Workflow, Agent, Knowledge Base/RAG, API app, observability/logs, import/export DSL YAML. Bản self-host hiện đã chạy Docker OK nhưng console API `/console/api/apps` trả 401 vì thiếu authenticated console/API session/provider credential. Vì vậy kế hoạch đúng là: thiết kế app/KB/workflow theo Dify DSL ngay, dùng no-API runner tạm thời, và import vào Dify ngay khi có session.

## 1. Nguồn tham khảo Dify/app store/community đã kiểm
- Dify docs: app types, workflows/chatflows, datasets/KB, app API, annotations, document/chunk APIs.
- Dify community/app templates: awesome-dify-agents có DSL `.yml` theo nhóm agents/chatbots/rag/integrations/utilities, import qua Dify dashboard "Import DSL file".
- Pattern áp dụng phù hợp công ty: RAG support bot, evidence auditor workflow, task-router agent, document extraction/review, customer/support assistant.

## 2. Inventory công ty hiện có
### Agents
- Trợ Lý/main: CEO coordination, task dispatch, Company OS.
- Cáo/cao: technical advisor, evidence gate, Dify/openclaw/gateway monitor.
- Bông/bong: Upharma 19 nhà thuốc, CRM/import/drug-disease POC.
- Bún/bun: Dropship/affiliate, Tarot, SaaS, Godot/Epoch Ascendant.
- Render: video automation/render postflight.
- Antigravity: queue worker via `antigravity_tasks/inbox` and outbox.

### Data/docs/projects ready for Dify KB
- `memory/agent_task_bus.jsonl`: canonical A2A task/result bus.
- `memory/areas/tech-ops/*.md`: incident/config/evidence logs.
- `upharma/4_Ket_Qua_AI/drug_disease_poc_20260604/*.csv|*.md`: SKU review/import artifacts.
- `upharma/A2A_STATUS.md`, `upharma/HEARTBEAT.md`: Bông ops state.
- `bun/epoch-ascendant-unity/*`: game artifacts and runtime logs.
- `memory/areas/dropship-affiliate/MEMORY.md`: Bún/dropship/game status.
- `memory/areas/render-automation/*`: render learning/postflight assets.
- `company-os/ops/*`: dashboards, bridge, Dify implementation artifacts.

## 3. Áp dụng ngay: 6 Dify apps cần dựng
### App 1 — Company OS Evidence Auditor
- Type: Workflow + KB/RAG.
- Input: task_id, owner, time window, paths.
- KB: tech-ops logs, A2A bus, agent status docs.
- Output: DONE/PARTIAL/STALLED/BLOCKED with evidence path/size/log.
- Business value: chống báo cáo chung chung; dùng ngay cho các checkpoint cron.

### App 2 — Upharma CRM Import Review Copilot
- Type: Chatflow + Workflow + KB.
- Input: CSV SKU review, blocker, revenue/orders metrics.
- KB: Upharma POC docs, batch review files, approval rules.
- Output: approval packet, source-check list, import readiness summary.
- Guardrail: no production DB write before human/pharmacist approval.

### App 3 — Agent Task Router / A2A Dispatcher
- Type: Workflow/Agent.
- Input: Henry request or cron event.
- Logic: classify owner: Bông/Bún/Render/Antigravity/Trợ Lý/Cáo; create canonical A2A entry; mirror Antigravity inbox if needed.
- Output: dispatch artifact + expected SLA/checkpoint.

### App 4 — Render Brief to Postflight Assistant
- Type: Chatflow + Workflow.
- Input: video brief/media requirements.
- KB: render learning notes/postflight reports.
- Output: render task spec, QA checklist, ffprobe postflight summary.

### App 5 — Bún Product/SaaS/Game Research Desk
- Type: Agent + RAG.
- Input: niche/task/feature request.
- KB: dropship-affiliate memory, Tarot/SaaS/Godot docs.
- Output: product research plan, prototype slice, blocker summary.

### App 6 — Executive Knowledge Search for Henry
- Type: Chatbot/RAG.
- Input: natural language question: “đang kẹt gì?”, “Upharma tới đâu?”, “Dify áp dụng sao?”
- KB: curated memory/DASHBOARD, tech-ops, upharma-ops, dropship-affiliate, company-os runbooks.
- Output: short executive answer with evidence links.

## 4. Triển khai 24 giờ
### 0-2 giờ: Chuẩn bị import-ready package
- Tạo DSL skeleton YAML cho 6 apps.
- Tạo KB manifest: file nào đưa vào KB, loại nào exclude vì log quá dài/secrets.
- Tạo seed prompts/system instructions cho từng app.
- Verify bằng local no-API runner.

### 2-4 giờ: Native Dify enable
- Dùng browser session đã login hoặc Henry cung cấp session/API credential.
- Import DSL vào Dify dashboard.
- Tạo KB datasets và upload tài liệu curated.
- Gắn model/provider credential.

### 4-8 giờ: Pilot vận hành nội bộ
- Chạy App 1 cho checkpoint 45m.
- Chạy App 2 cho Upharma batches 1-3.
- Chạy App 3 cho Antigravity/Bông/Bún dispatch.
- Chạy App 6 để Henry hỏi trạng thái công ty.

### 8-24 giờ: Chuẩn hoá Company OS
- Mỗi agent có một Dify app hoặc workflow node tương ứng.
- Mỗi track có KB riêng + shared executive KB.
- A2A bus remains source of truth; Dify is UI/workflow/RAG layer.

## 5. Việc làm ngay sau plan này
- Build `kb_manifest.json` from workspace inventory.
- Build `dify_app_blueprints/*.yml` for 6 apps.
- Build `IMPORT_RUNBOOK.md` <= 10 bước.
- Log evidence and handoff to Trợ Lý/Antigravity for import verification.

## 6. Blocker cần Henry biết, không phải để dừng
- Native import/create vẫn cần logged-in Dify console/API session và provider key.
- Không reset auth DB/credential nếu chưa được duyệt vì rủi ro cao.
- Trong khi chờ, dùng blueprint + no-API runner như operational Company OS.

## 7. Rollback
- Xoá folder `company-os/ops/dify-company-adoption-20260604-2145/`.
- Nếu đã import native Dify: xoá 6 apps + KB datasets tương ứng trong console.
