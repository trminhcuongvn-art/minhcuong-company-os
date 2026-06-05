# DASHBOARD — Tổng quan (PARA index)

## Trạng thái hệ thống (cập nhật 2026-06-04 23:30 ICT)
- Vận hành 24/7: dùng “việc sắp tới/mốc tiếp theo”, không dùng “việc ngày mai”.
- **Operating qua Cáo** (04/06, Henry chốt): Henry làm việc qua Cáo trừ khi cần liên hệ trực tiếp; các cron heartbeat cũ đã gỡ 22:18 và không còn là default. Cáo self-coordinate 2 focus: Dify application + chuẩn hóa process/knowledge data.
- **Evidence/report chuẩn hiện hành**: chỉ dùng DONE / PARTIAL / NOT_STARTED / BLOCKED. Không báo DONE/PARTIAL nếu thiếu artifact path/link/log. Quy ước cũ có STALLED/KILLED chỉ là lịch sử, không dùng cho báo cáo mới.
- **Company OS + second brain**: `workspace/company-os/`; Cáo anchors: `areas/tech-ops/ACTIVE_GOALS.md`, `DECISIONS.md`, `SKILL_APP_REGISTRY.md`, `CAO_SECOND_BRAIN_OPERATING_SYSTEM_20260604_2210.md`.
- **Mô hình Online Product Studio** (plan `areas/tech-ops/new_company_org_staffing_plan_20260603.md`): Real BU (Upharma, BaDiVi) + Digital BU (Tarot, game/MMO, affiliate, dropship). Phase 1 mới: Automation Agent (`workspace/automation/`) + Growth Agent (`workspace/growth/`). Phase 2: Offer/CRM/Data Agent.
- Telegram group: Phương án B đang hiệu lực — Trợ Lý chỉ route/trả lời khi tag `@TroLyCuaCuong_bot` hoặc reply trực tiếp.
- A2A: per-agent `A2A_STATUS.md` bắt buộc cho task >10ph; canonical bus `memory/agent_task_bus.jsonl` là source of truth; trước khi báo DONE phải check canonical→local→artifact→mirror. Trợ Lý coordinator/tie-breaker, không chờ ACK vô hạn.

## Areas (PARA)
- **upharma-ops** → `memory/areas/upharma-ops/MEMORY.md` + `areas/upharma-ops/2026-06-03.md`
  - Data/report workspace có thật: `upharma/data.db`, report scripts, Excel tháng/target.
  - Quy chuẩn tồn kho 02/06: `giá trị tồn kho = QUANTITY * UNIT_PRICE`, không nhân `COEFFICIENT`; nếu có hệ số phải gọi riêng `tồn quy đổi hệ số`.
  - 03/06 DONE: reorder point, repeat/high-value customer, basket/AOV, KM lift, disease-mix CRM, contact hygiene, replenishment gap, expiry/cash-risk, private-label proxy, drug-disease POC v2. Output `upharma/4_Ket_Qua_AI/` & `upharma/output/`.
  - POC dashboard static: `upharma/evidence-poc-night/index.html` regenerate read-only từ `data.db` — 19 shop, DT T5 4.32 tỷ, 25,923 đơn.
  - 04/06 DONE: SQLPage POC read-only; drug DB/import-ready CRM drug CSV 64 SKU (63 staging-ready, 1 manual blocker), DB writes 0.
  - Mốc tiếp theo: human/pharmacist review 64 SKU; chỉ staging/production import khi được duyệt.

- **dropship-affiliate** → `memory/areas/dropship-affiliate/`
  - BaDiVi: campaign kit 03/06 tại `bun/badivi-campaign-kit-20260603/`; 3 reels script + render output; catalog/export checklist còn thiếu spec thật/MOQ/FOB/chứng chỉ/ảnh nhà máy.
  - Facebook leadgen blocker: thiếu cookie FB nick phụ tại `bun/badivi-leadgen/cookies_fb_secondary.txt`; LinkedIn ưu tiên OSINT/SERP công khai.
  - Tarot Phase 3: content QA VI/EN + UI mystical/effects vẫn cần integrate app chính; input flow không cần DOB cho tarot thuần.
  - Badivi Social SaaS: spec/state-machine PoC có trong `bun/badivi-social-saas/poc/`, chưa có runtime/API/publish.
  - Game/Digital: Epoch Ascendant 04/06 có HTML5 QA pass, Unity compile/scene wiring/WebGL build succeeded tại `bun/epoch-ascendant-unity/Build/WebGL/`; runtime browser capture còn BLOCKED bởi Chrome/WebGL/instanceReady.

- **render-automation** → `memory/areas/render-automation/`
  - BaDiVi reels: 3 mp4 9:16 re-render `render/badivi-reels/`, đã verify ffprobe, chờ quyết định publish/handoff.
  - Tarot Phase 3 intro asset DONE: `render/tarot_phase3_micro_20260603_1117/assets/tarot_intro_nebula_9x16.mp4` (1080x1920, 5s); chưa verify integrate app chính.
  - Google Flow/Omni: chuyển khỏi OCR-heavy; bridge local app tại `/Users/minhcuong/.gemini/antigravity/scratch/google-flow-bridge`; server/extension OK nhưng fail selector prompt input Flow hiện tại.
  - Caption labs 03/06: glassmorphism, kinetic mask, luma wipe, masked reveal, progress timer, chromatic pulse.

- **tech-ops** → `memory/areas/tech-ops/`
  - Cáo là supervisor/company brain; Trợ Lý làm COO execution package khi được Cáo giao, không overlap owner/gate của Cáo.
  - Evidence gate: không DONE/PARTIAL nếu thiếu artifact path/link/log/result; báo cáo delta-only khi Henry yêu cầu.
  - Dify 04/06: runtime healthy và có app/query artifacts trong `areas/tech-ops/dify_evidence_20260604/`, nhưng còn PARTIAL vì native auth/provider/A2A gate/token-redaction chưa khép kín. Henry yêu cầu Dify usage guide chi tiết sau khi hoàn tất.
  - Antigravity bridge/sync ở mức lab; memory indexing BLOCKED do OpenAI embeddings 401.
  - Voice/STT tiếng Việt: không có artifact mới 04/06; giữ NOT_STARTED/BLOCKED cho đến khi có dispatch rõ.

## Skill Library nội bộ
- Đường dẫn: `/Users/minhcuong/.openclaw/workspace/memory/skills/`
- Nguyên tắc: lưu insight/checklist/template tự viết lại, không copy nguyên văn hàng loạt nội dung có bản quyền.
- Skill hiện có: `skills/content/noti_content_framework.md`, `skills/documents/template_net_document_framework.md`.
- Khi dispatch task content/document/video, agent phải đọc skill liên quan trước.

## Cần Henry quyết định / mốc tiếp theo
1. **Dify**: init credential 9router/OpenAI cho `cc/claude-sonnet-4-6` qua console, HOẶC rollback Company Knowledge Assistant về Ollama gemma2:9b để API dùng được ngay (đang `provider_not_initialize`).
2. **Company OS Phase 1**: nghiệm thu artifact đầu của Automation (task board/registry/CRM-RFQ skeleton) + Growth (BaDiVi+Tarot 7-day calendar + funnel checklist).
3. **Epoch Ascendant MVP**: verify build HTML5 playable (deadline 04/06 00:30) — Trợ Lý self-manage.
4. Upharma: duyệt expiry/cash-risk action plan; verify report "Thân thiết+ only" đúng filter; verify GitHub Pages KPI T5; chốt pilot Datasette/Streamlit/Prophet.
5. BaDiVi: quyết định publish 3 reels (`render/badivi-reels/`); cung cấp spec/MOQ/FOB/chứng chỉ/ảnh nhà máy nếu đăng marketplace; cookie FB nick phụ nếu cần real leadgen.
6. Tarot: verify integrate asset render vào app chính + acceptance UI/content Phase 3.
7. Voice/STT tiếng Việt: vẫn STALLED — cần test live route Telegram + benchmark sau khi force `language=vi`/nâng model.
8. Godot game: cài Godot CLI để export/runtime verify scaffold Upharma training game.

## File quan trọng
- Daily memory: `memory/YYYY-MM-DD.md`
- Cải tiến: `memory/improvements-queue.md`
- A2A policy: `memory/skills/agentops/a2a_bus_policy.md`
- Governance: `memory/company-governance/2026-06-02-agent-continuity-evidence-policy.md`

_Cập nhật: 2026-06-04 23:30 ICT — chốt sổ bộ nhớ thứ 2. Roll-up ngày: `memory/2026-06-04.md`._

## 2026-06-03 — A2A DONE Gate correction
- Henry yêu cầu Trợ Lý tự cải thiện vì quên A2A dù policy đã tồn tại.
- New mandatory checklist: `memory/skills/agentops/a2a_done_gate_checklist.md`
- Gate checker: `memory/skills/agentops/a2a_gate_check.py`
- Rule: before reporting DONE/PARTIAL for Bông/Bún/Render, Trợ Lý must check canonical bus → local bus → artifact evidence → mirror to canonical if missing.

## 2026-06-03 — Checkpoint commitment rule
- Henry phản hồi mất niềm tin vì Trợ Lý hứa checkpoint 22:35 rồi tự xoá im lặng.
- Rule file: `memory/skills/agentops/checkpoint_commitment_rule.md`
- Rule: đã hứa checkpoint thì không xoá im lặng; DONE sớm vẫn giữ checkpoint hoặc phải báo công khai nếu huỷ.

## 2026-06-04 00:24 ICT — Henry role reset for Bông/Bún
- Bông: tập trung xây dựng cơ sở dữ liệu thuốc.
- Bún: tập trung xây dựng game Epoch Ascendant.
- Trợ Lý: điều phối Bông/Bún và kiểm soát tiến độ bằng A2A/checkpoint/evidence gate.
- Guardrail: không giao Dify cho Bông/Bún nếu Henry không chỉ định rõ.

## 2026-06-04 00:49 ICT — Efficiency recovery block
- Henry yêu cầu làm việc thật hiệu quả: tự kiểm Unity mỗi 20 phút, xong thì triển khai tiếp không chờ nhắc.
- Cron job: `ef616843-b284-4caf-b463-370cc7d3941f`.
- Bông: CSDL thuốc.
- Bún: game Epoch Ascendant.
- Trợ Lý: điều phối/checkpoint/evidence, không lan man sang Dify.

## 2026-06-05 08:20 ICT — Upharma routing decision
- Henry chốt: mọi vấn đề liên quan Upharma chuyển cho **BÔNG** trả lời/xử lý.
- Rule: `memory/skills/agentops/upharma_route_to_bong.md`.
