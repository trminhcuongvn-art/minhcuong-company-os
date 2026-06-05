# Dify Workflow Node Spec — Company Task Intake Router v0

Date: 2026-06-03
Owner: Cáo
Status: ready for UI configuration

## Workflow name
Company Task Intake Router

## Goal
Nhận yêu cầu công việc từ Henry/Trợ Lý/agent, phân loại risk, route owner, yêu cầu evidence, và trả JSON chuẩn để Company OS dùng.

## Inputs
Tạo các input variables trong Start node:
- task: paragraph/string, required
- requester: text, default "Henry"
- business_unit: select/text: company-os|upharma|badivi|tarot|render|voice|godot|saas|tech
- urgency: select: low|normal|high|urgent
- risk_notes: paragraph/string

## Node 1 — Start
Input fields như trên.

## Node 2 — LLM / Classifier
Name: Risk + Owner Classifier
Prompt:
```
Bạn là Company Task Intake Router cho Tập đoàn Minh Cường.

Hãy phân loại task sau theo Company OS:
Task: {{task}}
Requester: {{requester}}
Business unit: {{business_unit}}
Urgency: {{urgency}}
Risk notes: {{risk_notes}}

Quy tắc owner:
- upharma/KPI/nhà thuốc/CRM khách hàng => bong
- badivi/dropship/affiliate/tarot/growth/content/campaign/crawl => bun
- render/video/reel/media/postflight => render
- tech/gateway/model/config/debug/dify/docker/security => cao
- điều phối/công ty/priority/task board => troly
- strategic/chi tiền/public official/dữ liệu nhạy cảm/irreversible => human/henry approval

Risk:
- L1: đọc/nháp/nội bộ, không side effect
- L2: tạo file nội bộ, reversible
- L3: chạy tool nội bộ, chỉnh config reversible, ingest KB nội bộ
- L4: public, gửi khách hàng, chi tiền nhỏ, dữ liệu nhạy cảm
- L5: irreversible, chiến lược, production critical, legal/finance

Evidence Gate:
DONE phải có path/URL/log/test. Không chấp nhận "active/ongoing/studying".

Trả về JSON hợp lệ, không markdown:
{
  "risk_level": "L1|L2|L3|L4|L5",
  "owner": "troly|cao|bong|bun|render|henry",
  "needs_henry_approval": true/false,
  "status_start": "NEW",
  "evidence_required": ["..."],
  "next_action": "...",
  "deadline_hint": "<=45m|today|needs planning",
  "reason": "..."
}
```

## Node 3 — End
Map output variable:
- result_json = output text from classifier

## Expected outputs examples
Input: "Bông sửa báo cáo thăng hạng KHTT chỉ tính Thân thiết trở lên"
Expected:
{
  "risk_level":"L2",
  "owner":"bong",
  "needs_henry_approval":false,
  "status_start":"NEW",
  "evidence_required":["CSV/MD report path", "script/log path", "filter proof excludes Chưa hạng"],
  "next_action":"Regenerate customer upgrade report with tier >= Thân thiết only",
  "deadline_hint":"<=45m",
  "reason":"Internal Upharma report, reversible, no public release"
}

## Publish
Sau khi cấu hình:
1. Save
2. Publish Changes
3. Test API /v1/workflows/run
