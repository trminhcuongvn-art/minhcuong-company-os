# Trợ Lý COO Execution Plan — Company-wide Dify Adoption

## AI First checklist
Không tốn tiền/license; không ghi/xóa production; rollback bằng xóa artifact; không public dữ liệu nội bộ. Vì vậy đã tự tạo execution package local, không hỏi Henry.

## TOP 3 việc đêm 23:00
1. **Dify Company OS adoption package** — owner Trợ Lý, checkpoint 23:30, deadline 00:30. Evidence: folder này + native unblock request.
2. **Upharma drug DB import-ready handoff** — owner Bông, checkpoint 23:45, deadline 00:45. Evidence: `drug_db_crm_import_ready_*`, `handoff_signoff_*`, Dify app spec nếu có.
3. **Epoch playable trial / product Dify specs** — owner Bún, checkpoint 23:45, deadline 01:00. Evidence: playable trial README/report + `bun/dify/20260604_2152/`.

## Execution lane
- Collect domain specs into one import package; Cáo does final acceptance.
- Native Dify console/API step remains gated if it needs auth/token/provider changes.
- No production DB writes; all Upharma data stays read-only/staging.

## Evidence gate
- DONE requires path + size/log + rollback.
- PARTIAL allowed only with artifact and exact missing piece.
- BLOCKED only after local no-risk alternatives tried and logged.
