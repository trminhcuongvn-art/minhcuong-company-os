# Company Knowledge Assistant — KB Manifest v1 (2026-06-03)

Mục tiêu: nạp tối thiểu tài liệu nội bộ để Dify trả lời đúng về cấu trúc công ty, quy tắc AI First/Evidence Gate, trạng thái Dify và marketplace.

## Ingest set v1
1. `/Users/minhcuong/.openclaw/workspace/memory/DASHBOARD.md`
   - Vai trò: tổng quan công ty/current context.
   - Câu hỏi hỗ trợ: công ty đang có track nào, ưu tiên nào.

2. `/Users/minhcuong/.openclaw/workspace/critical-tasks/HENRY_CRITICAL_TASK_BOARD.md`
   - Vai trò: board việc Henry giao trực tiếp.
   - Câu hỏi hỗ trợ: task critical nào, trạng thái nào.

3. `/Users/minhcuong/.openclaw/workspace/company-os/dify-plan/dify_company_usage_guide_20260603.md`
   - Vai trò: hướng dẫn Dify, trạng thái runtime, cách áp dụng.
   - Câu hỏi hỗ trợ: Dify dùng làm gì, còn thiếu gì.

4. `/Users/minhcuong/.openclaw/workspace/company-os/dify-plan/dify_marketplace_research_20260603.md`
   - Vai trò: danh mục marketplace/templates/plugins và shortlist cho công ty.
   - Câu hỏi hỗ trợ: nên dùng template nào.

5. `/Users/minhcuong/.openclaw/workspace/company-os/dify-plan/dify_work_split_final_20260603.md`
   - Vai trò: phân công Trợ Lý/Cáo triển khai Dify.
   - Câu hỏi hỗ trợ: ai làm gì, deadline nào.

6. `/Users/minhcuong/.openclaw/workspace/memory/areas/upharma-ops/MEMORY.md`
   - Vai trò: context Upharma/Bông.
   - Câu hỏi hỗ trợ: Bông phụ trách gì, dữ liệu Upharma ở đâu.

## Không nạp ở v1
- File chứa API key/token/password.
- Data khách hàng/đơn thuốc/dữ liệu nhạy cảm production.
- Toàn bộ transcript chat dài chưa lọc.
- File binary lớn hoặc database thô (`data.db`) — dùng tool riêng, không đưa thẳng vào KB v1.

## Cấu hình gợi ý
- Chunk size: 800–1200 tokens.
- Overlap: 100–200 tokens.
- Retrieval: top_k 4–6.
- Model: Ollama local trước; không public dữ liệu ra ngoài.

## Acceptance
KB v1 pass nếu app trả lời đúng 5/5 câu trong `company_knowledge_acceptance_tests_20260603.md`, có dẫn nguồn/path.
