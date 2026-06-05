# Dify Company Usage Guide — Minh Cường Company OS

Date: 2026-06-03
Owner: Cáo
Status: v0 usable guide

## 1. Mục tiêu dùng Dify
Dify là nền tảng nội bộ để biến Company OS thành app/workflow AI dùng được cho toàn công ty:
- Knowledge assistant: hỏi đáp theo tài liệu công ty, có nguồn.
- Task intake router: nhận việc mới, phân loại rủi ro, route owner, yêu cầu evidence.
- Agent tool layer: Trợ Lý/Bông/Bún/Render gọi API Dify để lấy quyết định/tri thức/workflow.

## 2. Vai trò trong công ty
- Henry: Product/Strategy owner, quyết định L4/L5, cấp quyền admin/API.
- Trợ Lý: COO/CEO agent, dùng Dify để điều phối công việc, đọc Company OS KB, tạo task.
- Cáo: Technical advisor/QA, duy trì runtime, API, evidence gate, workflow correctness.
- Bông: Upharma BU, dùng KB/workflow cho báo cáo, KPI, CRM, evidence.
- Bún: Growth/MMO/Badivi/Tarot BU, dùng KB/workflow cho campaign, research, execution notes.
- Render: media/render agent, dùng workflow nhận brief, trả postflight evidence.

## 3. App cần có trong Dify
### A. Company Knowledge Assistant
Loại: Chat/Advanced Chat
Mục đích: hỏi đáp nội bộ dựa trên tài liệu Company OS.
Knowledge nên ingest:
- /Users/minhcuong/.openclaw/workspace/company-os/knowledge/
- /Users/minhcuong/.openclaw/workspace/company-os/docs/
- /Users/minhcuong/.openclaw/workspace/company-os/roles/
- /Users/minhcuong/.openclaw/workspace/company-os/registries/
- /Users/minhcuong/.openclaw/workspace/memory/areas/tech-ops/ các incident quan trọng

System rule đề xuất:
"Bạn là Company Knowledge Assistant. Trả lời ngắn, có path nguồn nếu dùng KB. Nếu không có nguồn, nói chưa có evidence. Không tự bịa quyết định. Phân biệt DONE/PARTIAL/STALLED/BLOCKER theo Evidence Gate."

### B. Company Task Intake Router
Loại: Workflow
Input đề xuất:
- task: string
- requester: string
- business_unit: string
- urgency: low|normal|high
- risk_notes: string

Output JSON đề xuất:
{
  "risk_level": "L1|L2|L3|L4|L5",
  "owner": "troly|cao|bong|bun|render|human",
  "needs_henry_approval": true/false,
  "evidence_required": ["path/url/log/test"],
  "next_action": "...",
  "deadline_hint": "..."
}

Routing rules:
- Chi tiền/public chính thức/dữ liệu nhạy cảm/thay đổi không rollback/chiến lược => needs_henry_approval=true.
- Upharma => Bông, trừ lỗi hệ thống => Cáo.
- Dropship/Affiliate/BaDiVi/Tarot growth => Bún.
- Render/video/media => Render.
- Gateway/model/config/error/debug => Cáo.
- Điều phối đa-agent/company priority => Trợ Lý.

## 4. Quy trình dùng hàng ngày
1. Henry/Trợ Lý đưa yêu cầu vào Task Intake Router.
2. Workflow trả owner + risk + evidence_required.
3. Owner làm việc trong workspace riêng.
4. Owner báo A2A result về Cáo, không tự post group nếu chưa chỉ định.
5. Cáo audit Evidence Gate.
6. DONE chỉ được công nhận khi có path/URL/log/test.

## 5. Cách gọi API
Base URL local:
http://localhost/v1

Chat app:
POST /chat-messages
Header: Authorization: Bearer <APP_KEY>
Body:
{
  "inputs": {},
  "query": "Câu hỏi",
  "response_mode": "blocking",
  "conversation_id": "",
  "user": "troly"
}

Workflow:
POST /workflows/run
Header: Authorization: Bearer <WORKFLOW_KEY>
Body:
{
  "inputs": {
    "task": "Tạo báo cáo KPI Upharma T6",
    "requester": "Henry",
    "business_unit": "upharma",
    "urgency": "normal",
    "risk_notes": "internal only"
  },
  "response_mode": "blocking",
  "user": "troly"
}

## 6. Quy tắc vận hành an toàn
- Không public internet Dify khi chưa có auth/network policy.
- Không ingest dữ liệu khách hàng nhạy cảm nếu chưa chốt storage/permission.
- API key không ghi plaintext vào memory/log.
- Nếu đổi .env/docker compose phải ghi tech-ops log.
- Backup trước khi upgrade.

## 7. Trạng thái hiện tại 2026-06-03
DONE:
- Dify local runtime running via Colima/Docker.
- Chat API smoke HTTP 200.
- Workflow API smoke HTTP 200.

PARTIAL:
- KB ingestion chưa verified.
- Company Knowledge Assistant chưa verified với citations.
- Task Intake Router workflow hiện mới smoke succeeded, chưa có routing logic đầy đủ.

Next:
- Henry/Trợ Lý cấu hình KB trong UI hoặc cung cấp dataset API path.
- Cáo test 5 câu KB + 3 task routing mẫu.
