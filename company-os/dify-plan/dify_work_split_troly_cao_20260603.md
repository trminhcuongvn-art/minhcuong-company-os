# Phân chia công việc Dify — Trợ Lý x Cáo (draft, 2026-06-03)

Yêu cầu Henry: trao đổi với Cáo và phân chia công việc.

## Trạng thái trao đổi
- Đã gửi yêu cầu cho Cáo qua subagent: agent:cao:subagent:8d0731c4-232c-4786-a5ef-53854ba35d9b
- Lưu ý: lần gửi sessions_send đầu lỗi 429; đã spawn lại bằng gpt-5.5 thành công.
- Đang chờ Cáo phản biện/chốt nhận việc.

## Mục tiêu chung
Đưa Dify từ trạng thái "runtime chạy nhưng app rỗng" sang "Company Knowledge Assistant chạy thật" trong block 16:00–24:00.

## Evidence hiện có
- Dify runtime/API: DONE (containers/API đã verify trước đó).
- Marketplace research: DONE — company-os/dify-plan/dify_marketplace_research_20260603.md
- Usage guide: DONE — company-os/dify-plan/dify_company_usage_guide_20260603.md
- Current gap: model provider + KB + app giá trị thật: NOT_STARTED.

## Phân vai đề xuất
### Cáo — Dify Runtime/Builder Owner
Nhiệm vụ:
1. Cắm Ollama local vào Dify làm Model Provider.
2. Tạo/import Company Knowledge Assistant app.
3. Tạo Knowledge Base tối thiểu hoặc hướng dẫn UI nếu cần thao tác login.
4. Publish app.
5. Test API để chứng minh answer không còn chỉ là "ok" rỗng.

Acceptance/evidence:
- Screenshot hoặc log Dify model provider configured.
- App ID/key hoặc tên app.
- API test HTTP 200, answer có nội dung thật.
- Log path: company-os/dify-plan/cao_dify_runtime_log_20260603.md

Deadline đề xuất: trước 18:30 GMT+7.

### Trợ Lý — Company OS / KB / Governance Owner
Nhiệm vụ:
1. Chọn tài liệu nạp KB tối thiểu:
   - memory/DASHBOARD.md
   - ACTIVE_RULES/AI First nếu có
   - company-os/dify-plan/dify_company_usage_guide_20260603.md
   - company-os/dify-plan/dify_marketplace_research_20260603.md
2. Viết system prompt cho Company Knowledge Assistant.
3. Viết acceptance test 5 câu hỏi.
4. Viết hướng dẫn sử dụng cho Henry.
5. Sau khi Cáo có app/API, test độc lập và chấm Evidence Gate.

Acceptance/evidence:
- KB manifest file.
- Prompt file.
- Test spec + test result.
- User guide.

Deadline đề xuất: trước 19:30 GMT+7.

### Phase 2 — Task Intake Workflow
Cáo:
- Dựng workflow trong Dify theo template Question Classifier / Work Ticket System.
Trợ Lý:
- Viết JSON schema routing:
  {domain, owner, risk_flags, ai_first_allowed, evidence_required, deadline, status}
- Mapping owner: Bông/Upharma, Bún/Dropship, Render/media, Cáo/governance, Trợ Lý/coordination.

Deadline đề xuất: 20:30–22:00 GMT+7 sau khi Company KB chạy.

## Quy tắc chấm
- DONE: có evidence path/link/log.
- PARTIAL: có artifact nhưng chưa pass test.
- BLOCKED: cần Henry/API/login/UI thao tác.
- NOT_STARTED: không có evidence.

## Risk/human override
- Ollama local: free, không public, reversible => AI First tự làm.
- 9router/OpenAI/BrightData/Gmail/Slack OAuth: tốn tiền hoặc đưa data ra ngoài => cần Henry duyệt.
