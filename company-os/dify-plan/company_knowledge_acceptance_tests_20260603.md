# Company Knowledge Assistant — Acceptance Tests v1 (2026-06-03)

Pass condition: 5/5 câu trả lời đúng ý chính, tiếng Việt, có source/path khi nói trạng thái/evidence.

## Test 1 — Vai trò Dify
Question: Dify dùng để làm gì trong công ty mình? Có thay OpenClaw không?
Expected:
- Dify là lớp Knowledge/RAG + app/workflow AI nội bộ.
- Không thay OpenClaw.
- OpenClaw/Trợ Lý vẫn điều phối/thực thi.
- Source: dify_company_usage_guide_20260603.md.

## Test 2 — Trạng thái Dify hiện tại
Question: Dify hiện đang DONE phần nào và còn thiếu gì?
Expected:
- Runtime/API publish: DONE.
- App/workflow khung: DONE.
- Model provider + Knowledge Base/app giá trị thật: NOT_STARTED hoặc theo evidence mới nhất nếu Cáo đã cập nhật.
- Không được nói DONE nếu không có smoke output trả lời thật.
- Source: dify_company_usage_guide_20260603.md và/or dify_work_split_final_20260603.md.

## Test 3 — Phân vai Trợ Lý/Cáo
Question: Cáo làm gì, Trợ Lý làm gì trong triển khai Dify?
Expected:
- Cáo: runtime/UI/config/API, cắm Ollama, tạo/import app, gắn KB, publish, smoke API.
- Trợ Lý: KB manifest, prompt/policy, acceptance test, guide Henry.
- Deadline: Cáo 18:00 ICT, Trợ Lý 17:30 ICT theo bản chốt.
- Source: dify_work_split_final_20260603.md.

## Test 4 — Marketplace nên dùng template nào trước
Question: Nên bắt đầu với template Marketplace nào?
Expected:
- Knowledge Retrieval + Chatbot / Smart Chatbot cho Company Knowledge Assistant.
- Question Classifier / Work Ticket System cho Task Intake sau.
- Market Research Agent/Open-Box Deals Aggregator cho BÚN sau, cẩn trọng API phí.
- Source: dify_marketplace_research_20260603.md.

## Test 5 — KB v1 gồm tài liệu nào và không nạp gì?
Question: KB v1 nên nạp tài liệu nào, và không nên nạp gì?
Expected:
- Nạp: DASHBOARD.md, HENRY_CRITICAL_TASK_BOARD.md, dify_company_usage_guide, dify_marketplace_research, dify_work_split_final, Upharma MEMORY.
- Không nạp: API key/token/password, dữ liệu khách hàng/đơn thuốc/production nhạy cảm, transcript dài chưa lọc, data.db thô.
- Source: company_knowledge_kb_manifest_20260603.md.

## Kết quả test
- Chưa chạy: NOT_STARTED — chờ Cáo publish app gắn model + KB.
