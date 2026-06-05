# 2026-06-02 23:00 — Night dispatch

Đã scan ACTIVE_RULES/DASHBOARD/agent_task_bus.

## TOP 3 chọn làm đêm
1. BaDiVi 3 Reels -> campaign/RFQ launch kit
   - Owner: Bún
   - Deadline: 2026-06-03 01:00 ICT
   - Checkpoint: 00:15
   - Evidence gate: campaign_pack.md, captions_utm.csv, rfq_form_spec.md, crm_lead_log_template.csv, outreach_sequence.md.
   - Lý do: có 3 mp4 đã render + 48 lead top outreach; có thể biến artifact thành phễu lead đo được ngay.

2. Upharma dashboard action pack + T6 readiness gate
   - Owner: Bông
   - Deadline: 2026-06-03 01:30 ICT
   - Checkpoint: 00:30
   - Evidence gate: action_pack HTML/MD, alert list có số thật, T6 readiness checklist.
   - Lý do: nhiều phân tích T5 đã DONE; cần đóng gói thành hành động quản lý + chặn rõ T6 target/data.

3. Voice STT/router postflight cleanup
   - Owner: Cáo
   - Deadline: 2026-06-03 00:30 ICT
   - Checkpoint: 23:45
   - Evidence gate: config/code/backup, restart/log, live-test checklist; nếu chưa test live thì giữ PARTIAL.
   - Lý do: task PARTIAL quá hạn, cần cleanup an toàn/rollback, không báo DONE giả.

## Blocker hiện tại
- FB leadgen BaDiVi vẫn cần cookie/nick phụ để scrape comment thật; fallback hiện có: Scrapling/public web + 48 lead dedupe.
- Upharma T6 target/data chưa sẵn sàng; fallback dùng baseline T5.
- Voice STT cần live voice test của Henry sau restart.

Log dispatch đã ghi vào `/Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl` với các message_id:
- A2A-TROLY-NIGHT-DISPATCH-20260602-2300
- A2A-TROLY-BUN-DISPATCH-NIGHT-20260602
- A2A-TROLY-BONG-DISPATCH-NIGHT-20260602
- A2A-TROLY-CAO-TECHOPS-DISPATCH-NIGHT-20260602
