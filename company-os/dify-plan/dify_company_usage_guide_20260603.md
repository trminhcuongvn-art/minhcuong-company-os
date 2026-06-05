# Hướng dẫn dùng Dify cho cả công ty Minh Cường — 2026-06-03

Nghiên cứu trực tiếp trên Dify local Cáo vừa cài. Có verify bằng API thật.

## 1. Hiện trạng (verified)
- Dify chạy local bằng Docker (12 container UP: nginx, api healthy, worker, web, postgres, redis, weaviate, sandbox, plugin_daemon, ssrf_proxy...). Commit ca31762.
- URL: http://localhost/apps (200), http://localhost/install (200).
- Chat API: POST http://localhost/v1/chat-messages → HTTP 200, mode advanced-chat.
- Workflow API: POST http://localhost/v1/workflows/run → HTTP 200, status succeeded.
- NHƯNG: app hiện trả "answer: ok", outputs rỗng, total_tokens 0.
  => App/workflow mới chỉ là khung publish, CHƯA nối LLM model + CHƯA gắn Knowledge Base. Đây là việc cần làm tiếp.

## 2. Dify là gì và dùng để làm gì
Dify = nền tảng xây app AI (chatbot, agent, workflow) + Knowledge/RAG, có UI kéo thả, expose API.
Vai trò trong công ty: lớp Knowledge + App AI nội bộ. KHÔNG thay OpenClaw. OpenClaw vẫn là bộ điều phối/agent thực thi; Dify là nơi hỏi tri thức và chạy workflow chuẩn hóa.

## 3. Việc bắt buộc làm để Dify "thật sự dùng được"
B1. Cấu hình Model Provider
- Settings → Model Provider → thêm OpenAI/Anthropic/Google (hoặc model nội bộ) + API key.
- Không có model thì app chỉ trả rỗng như hiện tại.

B2. Tạo Knowledge Base (RAG)
- Knowledge → Create → upload tài liệu công ty: ACTIVE_RULES.md, DASHBOARD.md, charter phòng ban, SOP, memory/areas chọn lọc.
- Chọn embedding + retrieval. Đây là phần tạo giá trị lớn nhất.

B3. Tạo App gắn KB
- Tạo Chat Assistant → bật Context → trỏ vào Knowledge Base.
- Publish → lấy App API Key (app-xxxx).

## 4. Bộ app đề xuất cho công ty (ưu tiên)
1. Company Knowledge Assistant
   - Hỏi: quy tắc hiện tại, ai sở hữu task, blocker trước đó, KPI block.
2. Task Intake Classifier (Workflow)
   - Input: tin nhắn Henry → Output JSON: domain, risk, owner đề xuất, acceptance, deadline.
3. Evidence Auditor (Workflow)
   - Input: task_id + artifact path → Output PASS/FAIL + lý do.
4. Upharma Q&A
   - KB từ báo cáo/SOP nhà thuốc cho quản lý hỏi nhanh.
5. BaDiVi/Dropship Content KB
   - KB sản phẩm, offer, copy mẫu cho BÚN.

## 5. Cách từng vai trò dùng
- Henry: hỏi Company Knowledge Assistant để nắm trạng thái, không phải hỏi từng agent.
- Trợ Lý: dùng Task Intake Classifier để chuẩn hóa việc trước khi giao.
- Cáo: dùng Evidence Auditor để chấm DONE/FAIL theo evidence.
- Bông: Upharma Q&A cho quản lý nhà thuốc.
- Bún: Content/Product KB cho dropship/affiliate.

## 6. Cách gọi API (mẫu đã test)
Chat:
  POST http://localhost/v1/chat-messages
  Header: Authorization: Bearer app-xxxx
  Body: {"inputs":{},"query":"...","response_mode":"blocking","user":"id"}
Workflow:
  POST http://localhost/v1/workflows/run
  Header: Authorization: Bearer app-xxxx
  Body: {"inputs":{...},"response_mode":"blocking","user":"id"}

## 7. Guardrails
- Local only, KHÔNG expose Docker/API ra internet (bản Dify này từng có lỗ hổng Docker API, đã ở commit mới nhưng vẫn không public).
- KB chỉ nạp tài liệu nội bộ; không nạp dữ liệu khách hàng nhạy cảm khi chưa duyệt.
- Model API key tốn tiền → cần Henry duyệt provider/ngân sách trước khi bật.
- Câu trả lời Dify là tham khảo; registry file/jsonl vẫn là nguồn sự thật để chấm DONE.

## 8. Trạng thái (Evidence Gate)
- Dify runtime: DONE (verified container + API 200).
- App/workflow khung: DONE (publish, API 200).
- Model provider + Knowledge Base: NOT_STARTED (app đang trả rỗng).
- App giá trị thật (KB Q&A, classifier, auditor): NOT_STARTED.

## 9. Việc tiếp theo cần Henry quyết
- Chọn model provider + cấp API key (tốn tiền → cần duyệt).
- Duyệt danh sách tài liệu nạp vào Knowledge Base.
