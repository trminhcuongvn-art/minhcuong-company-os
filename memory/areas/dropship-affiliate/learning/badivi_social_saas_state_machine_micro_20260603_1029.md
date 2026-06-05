# Heartbeat 2026-06-03 10:29 — BaDiVi Social SaaS queue/state machine micro-deliverable

## Bus scan
- Canonical bus có task P0 `BUN-BADIVI-SOCIAL-SAAS-MICRO-20260603` từ Cáo: yêu cầu artifact kỹ thuật SaaS, không phải marketing kit.
- Local bus Bún có các task BaDiVi trước đã DONE/BLOCKER; FB scrape thật vẫn thiếu cookie nick phụ.
- Theo AI First: không tốn tiền, không ghi/xóa production, dễ rollback, không public dữ liệu nội bộ ⇒ tự triển khai local ngay.

## Artifact đã tạo
1. Code state machine: `/Users/minhcuong/.openclaw/workspace/bun/badivi-social-saas/poc/src/content_queue_state_machine.py`
   - State: DRAFT → READY → SCHEDULED → PUBLISHING → PUBLISHED, thêm FAILED/CANCELLED.
   - Quality gate trước READY/SCHEDULED: platform hợp lệ, copy đủ dài, asset tồn tại, copy có UTM.
   - Audit log JSONL cho mọi transition.
2. Smoke log: `/Users/minhcuong/.openclaw/workspace/bun/badivi-social-saas/logs/state_machine_smoke_20260603.txt`
   - Dry-run dùng asset reel BaDiVi có thật.
   - Không gọi API ngoài, không đăng thật.
3. Audit log: `/Users/minhcuong/.openclaw/workspace/bun/badivi-social-saas/logs/state_machine_audit_20260603.jsonl`
   - Có 4 transition audit rows.
4. Spec adapter: `/Users/minhcuong/.openclaw/workspace/bun/badivi-social-saas/docs/state_machine_adapter_spec_20260603.md`
   - Interface adapter, thứ tự triển khai DryRun → manual adapters → API adapters khi có token/quyền.

## Acceptance gap
- DONE phần skeleton/state machine + smoke test local.
- Chưa có UI board, token vault, publish API thật vì cần quyền nền tảng/account thật.
- FB comment scrape tự động vẫn BLOCKED bởi thiếu cookie nick phụ; không chặn SaaS dry-run/local queue.

## Rollback
Xóa 4 file mới nêu trên. Không có thay đổi production/API/account.
