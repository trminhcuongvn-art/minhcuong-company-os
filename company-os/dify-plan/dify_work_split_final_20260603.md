# Phân công cuối Dify — Trợ Lý x Cáo (2026-06-03)

## Chốt sau khi Cáo phản biện
Cáo đồng ý phân vai: Cáo giữ runtime/UI/config/API; Trợ Lý giữ KB/spec/prompt/acceptance/guide.

## Phase 1 — Company Knowledge Assistant
### Cáo — Runtime/UI/API Owner
Status hiện tại: NOT_STARTED trong phần app trả lời thật (chưa có smoke output có nội dung/source).
Deadline checkpoint: 2026-06-03 18:00 ICT.

Scope:
1. Cắm Ollama local provider vào Dify.
2. Tạo/import app `Company Knowledge Assistant`.
3. Gắn Knowledge Base theo manifest của Trợ Lý.
4. Publish app.
5. Test API trả lời thật, không còn `ok`/rỗng.

Evidence DONE cần có:
- Log/config Dify/Ollama provider.
- App ID/API endpoint/key smoke masked.
- API smoke output trả lời thật, có source/path nếu KB retrieval chạy.
- Test tối thiểu 5 câu theo acceptance checklist.

### Trợ Lý — Company OS / KB / Governance Owner
Status hiện tại: PARTIAL (đang tạo artifact spec/prompt/test).
Deadline checkpoint: 2026-06-03 17:30 ICT.

Scope:
1. Chọn tài liệu nạp KB tối thiểu.
2. Viết prompt/policy cho app.
3. Viết 5 câu acceptance test + expected answers.
4. Viết hướng dẫn sử dụng cho Henry sau khi app pass.

Evidence DONE cần có:
- KB manifest file.
- Prompt final.
- Acceptance test file.
- Test result sau khi Cáo publish.

## Phase 2 — Task Intake Workflow
Kích hoạt sau khi Company Knowledge Assistant pass 5/5.

Cáo:
- Dựng runtime workflow dựa trên Question Classifier / Work Ticket System.

Trợ Lý:
- Viết JSON schema + routing owner Bông/Bún/Render/Cáo/Trợ Lý.

## Chuẩn trạng thái
Chỉ dùng: DONE / PARTIAL / NOT_STARTED / BLOCKED.
