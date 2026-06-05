# Dify KB Ingest Checklist — Company OS

Date: 2026-06-03
Owner: Cáo
Status: ready for UI ingest

## Knowledge name
Company OS Knowledge Base

## Files/folders to ingest first
Priority 1:
- /Users/minhcuong/.openclaw/workspace/company-os/knowledge/
- /Users/minhcuong/.openclaw/workspace/company-os/docs/
- /Users/minhcuong/.openclaw/workspace/company-os/roles/
- /Users/minhcuong/.openclaw/workspace/company-os/registries/

Priority 2:
- /Users/minhcuong/.openclaw/workspace/memory/DASHBOARD.md
- /Users/minhcuong/.openclaw/workspace/ACTIVE_RULES.md
- /Users/minhcuong/.openclaw/workspace/memory/areas/tech-ops/2026-06-03.md

## Chunking recommendation
- Mode: General / Automatic
- Index: high quality if available
- Retrieval: hybrid/semantic if available
- Require source/citation in assistant response

## Company Knowledge Assistant system prompt
```
Bạn là Company Knowledge Assistant của Tập đoàn Minh Cường.
Luôn trả lời tiếng Việt, ngắn gọn, kỹ thuật.
Chỉ dùng tri thức từ Knowledge Base hoặc nói rõ "chưa có evidence".
Khi trả lời về quyết định/trạng thái/todo, phải nêu path nguồn nếu có.
Phân loại trạng thái theo Evidence Gate: DONE/PARTIAL/STALLED/BLOCKER.
Không tự bịa quyết định, không hỏi lại nếu ACTIVE_RULES đã chốt.
```

## 5 test questions
1. Company OS đang dùng WIP limit bao nhiêu priority/block?
2. Evidence Gate định nghĩa DONE như thế nào?
3. Vai trò của Cáo trong hệ thống là gì?
4. Dify được chọn thay AnythingLLM vì lý do gì?
5. Task Intake Router phải route việc Upharma cho agent nào?

## Pass criteria
- 5/5 câu trả lời đúng.
- Có source/path hoặc nói rõ chưa có evidence.
- Không hallucinate.
