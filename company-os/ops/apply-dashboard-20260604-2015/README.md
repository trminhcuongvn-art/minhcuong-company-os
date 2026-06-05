# Dify/Company OS Apply Dashboard — 2026-06-04 20:15 ICT

## Kết luận áp dụng vào công ty
- Dify đã cài nhưng phần API/provider credential vẫn chưa usable hoàn toàn; Company OS đang được áp dụng bằng no-API runbook và artifacts nội bộ.
- Đã có cadence, evidence gate, task/artifact registry, và trial outputs cho Upharma/Bún.
- Artifact này là dashboard kiểm tra áp dụng thực tế, chỉ đọc file nội bộ, không ghi production DB, không outreach, không public data.

## Status theo hạng mục
| Hạng mục | Trạng thái | Evidence | Size |
|---|---:|---|---:|
| Company OS foundation | DONE | `company-os/README.md` | 520 |
| No-API runbook | DONE | `company-os/ops/COMPANY_OS_NO_API_RUNBOOK_20260604_1642.md` | 1246 |
| Cadence job spec | DONE | `company-os/ops/COMPANY_OPS_CADENCE_JOB_SPEC_20260604_1913.md` | 1085 |
| Evidence gate docs | DONE | `company-os/docs/EVIDENCE_GATE.md` | 430 |
| Evidence gate JSON latest | DONE | `company-os/ops/evidence_gate_20260604_162235.json` | 532 |
| Upharma read-only review trial | DONE | `company-os/ops/p0_results/p0_upharma_readonly_review_20260604_1624.json` | 623 |
| Company knowledge QA trial | DONE | `company-os/ops/p0_results/p0_company_knowledge_qa_20260604_1624.json` | 544 |
| A2A task lookup trial | DONE | `company-os/ops/p0_results/p0_a2a_task_lookup_20260604_1624.json` | 464 |
| Dify usable decision | DONE | `company-os/ops/COMPANY_OS_USABLE_DECISION_20260604_1828.md` | 1459 |
| Upharma SQLPage POC | DONE | `upharma/sqlpage-poc/evidence_inventory_value.html` | 1523 |
| Upharma CRM import audit | DONE | `upharma/4_Ket_Qua_AI/drug_disease_poc_20260604/drug_db_crm_import_ready_audit_20260604_2000.md` | 2008 |
| Bún Epoch playable report | DONE | `bun/epoch-ascendant-mvp/PLAYABLE_TRIAL_REPORT_20260604.md` | 921 |

## README / runbook <=3 lệnh
```bash
# 1) Xem dashboard JSON/Markdown
cat company-os/ops/apply-dashboard-20260604-2015/README.md

# 2) Verify paths + sizes
python3 company-os/ops/apply-dashboard-20260604-2015/verify_apply_dashboard.py

# 3) Rollback artifact mới
rm -rf company-os/ops/apply-dashboard-20260604-2015
```

## Rollback
Xoá thư mục artifact mới: `rm -rf /Users/minhcuong/.openclaw/workspace/company-os/ops/apply-dashboard-20260604-2015`. Không có production DB write nên không cần restore DB.
