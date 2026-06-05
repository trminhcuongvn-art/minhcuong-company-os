# Đề xuất cho Cáo — xem xét Open Design sau khi hoàn thiện Dify

## Người gửi
Trợ Lý theo chỉ đạo Henry — 2026-06-04 15:46 ICT

## Bối cảnh
Henry yêu cầu tập trung hoàn thiện Dify trước. Open Design chỉ nên xem xét sau khi Dify/Dify Ops đã qua acceptance cơ bản, tránh lan man.

## Kết luận đề xuất
Sau khi Dify hoàn thiện bản đầu, Cáo nên đánh giá pilot Open Design như **lớp UI/prototype/export** cho Dify & Company OS, không dùng thay Dify.

## Vai trò đúng
- Dify: workflow / agent / RAG / assistant runtime.
- Company OS: task registry, evidence, SLA, A2A bus.
- Open Design: dựng giao diện/artifact/deck/dashboard, export HTML/PDF/PPTX/MP4 từ dữ liệu Dify/Company OS.

## Use-case ưu tiên sau Dify
1. **Dify Ops Evidence Board**
   - Input: `company-os/ops/*.jsonl`, `memory/agent_task_bus.jsonl`, Dify health/evidence.
   - Output: HTML/PDF local thể hiện health, tasks, blockers, SLA, evidence paths.
   - Mục tiêu: Henry nhìn tiến độ qua board thay vì đọc log dài.

2. **Dify App Blueprint Generator**
   - Tạo spec/wireframe cho workflow trước khi build Dify: node flow, input/output, acceptance, evidence gate.

3. **Company Knowledge Assistant UI mock**
   - UI demo cho Dify RAG: answer, citation, confidence, evidence path.

4. **Report/export layer**
   - Dify xuất JSON/MD; Open Design biến thành PDF/slide/report cho Upharma/BaDiVi/KPI.

## Điều kiện bắt đầu pilot
Chỉ bắt đầu khi Dify bản đầu đạt tối thiểu:
- Dify service health OK.
- Dify Ops local layer có task registry/evidence gate/ACK scanner chạy được.
- 3 use-case P0 đã có acceptance test hoặc blocker rõ.
- Không còn blocker auth/API làm lệch luồng chính.

## Guardrails
- Không sign-in/model router/cloud với dữ liệu nội bộ nếu chưa xác minh.
- Không cài MCP global vào OpenClaw trước khi backup config và có rollback.
- Chạy standalone/local-only trước, dữ liệu sample/redacted.
- Docker bind localhost, token random, không public.

## Pilot an toàn đề xuất
- Output mục tiêu: `company-os/rollout/dify_ops_evidence_board_open_design_poc.html`.
- Rollback: `docker compose down -v`, xóa repo clone, không chạm agent config nếu chưa cài MCP.

## Evidence research
- `/Users/minhcuong/.openclaw/workspace/memory/areas/tech-ops/research/open_design_eval_20260604.md`
- `/Users/minhcuong/.openclaw/workspace/memory/areas/tech-ops/research/open_design_dify_application_20260604.md`
