# Hướng dẫn sử dụng Dify — Tập đoàn Minh Cường

Cập nhật: 2026-06-05 13:56 ICT (Phase 2+3). Author: Cáo Technical Advisor.

## 1. Truy cập
- URL: http://localhost
- Email: trminhcuongvn@gmail.com
- Password: MinhCuong2026!

## 2. Danh sách apps và dùng khi nào

| App | Dùng khi | Mode |
|-----|----------|------|
| Agent-to-Cao Completion Gate | Agent báo Cáo kết quả task | Workflow |
| Company Knowledge Assistant | Hỏi về quy trình/rule/SOP công ty | Chat |
| Troly Task Coordinator | Giao task mới cho agent | Workflow |
| Upharma CRM Import Review | Duyệt thuốc/SKU vào hệ thống | Workflow |
| Render Brief to Postflight | Lên kế hoạch render video | Workflow |
| Bun Product Research Desk | Nghiên cứu sản phẩm dropshipping | Workflow |
| Bun Godot Blocker to Task | Chuyển blocker game thành task | Workflow |

## 3. Dùng qua API (tự động hoá)

```python
import urllib.request, json

def call_dify_workflow(token, inputs, user="henry"):
    url = "http://localhost/v1/workflows/run"
    payload = {"inputs": inputs, "response_mode": "blocking", "user": user}
    req = urllib.request.Request(url,
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

# Ví dụ: Giao task cho Troly
result = call_dify_workflow(
    token="app-25b8d54dfc6beaf981db5abbdde38fd3",
    inputs={
        "task_name": "Kiểm tra báo cáo doanh thu tuần",
        "owner_agent": "bong",
        "priority": "P1",
        "deadline": "17:00",
        "acceptance_criteria": "Báo cáo có evidence, DONE/PARTIAL/BLOCKED"
    }
)
print(result["data"]["status"])  # succeeded
```

## 4. Dùng qua Dify UI
1. Vào http://localhost → Studio
2. Chọn app muốn dùng
3. Click "Run" (workflow) hoặc chat (chat app)
4. Điền inputs → Submit

## 5. Xem lịch sử chạy
- Vào app → "Logs" (góc trái)
- Mỗi run có: inputs, outputs, status, thời gian

## 6. API Tokens
Xem đầy đủ tại: `company-os/ops/dify_app_registry.json`

## 7. KB — Company Knowledge Base
- Dataset: "Company OS Knowledge Base"
- Files: ACTIVE_RULES, ACTIVE_GOALS, DECISIONS, DASHBOARD + 10 docs cũ
- Sync tự động mỗi 4 giờ qua cron job

## 8. Agent Reporting — Quy trình bắt buộc
Sau khi xong task, **tất cả agent** chạy:
```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  <agent> <task_id> <DONE|PARTIAL|BLOCKED> "<evidence_path>" "<next_step>"
```
Ví dụ:
```bash
bash company-os/ops/agent_dispatch_wrapper.sh bong bong_sku_enrich_20260605 DONE \
  "upharma/4_Ket_Qua_AI/full_enrich_100sku_20260605.csv" "chờ staging review"
```
Quy trình cũ (chỉ chat, không có evidence) bị Cáo mark INVALID.

## 9. Domain KB Routing
Mỗi agent chỉ đọc KB domain riêng:
- Cáo / Trợ Lý → Company OS KB (ACTIVE_RULES, DECISIONS, ORG_MODEL)
- Bông → Upharma KB (MEMORY, full_enrich_100sku, staging plan)
- Bún → Dropship/Affiliate KB (playbook, product research)
- Render → Render KB (render notes, postflight)

Config: `company-os/ops/domain_kb_manifest.json`

## 10. Monitoring / Healthcheck
```bash
python3 company-os/ops/dify_phase3_healthcheck.py
# Expected: status PASS, checks 11, failed 0
```
Runbook đầy đủ: `company-os/docs/DIFY_PHASE3_RUNBOOK.md`

## 11. Rollback
- Xoá app: Dify UI → Settings → Delete
- Xoá KB doc: Dify UI → Knowledge → Dataset → Documents
- Revoke token: Dify UI → App → API Access → Revoke
