# Trợ Lý COO plan từ 02:05 đến 08:00 — 2026-06-05

## Mục tiêu
Đến 08:00 có Company Ops/Dify adoption usable hơn, không báo cáo lặp; các task Henry giao có owner, deadline, evidence, blocker rõ.

## Timeline
### 02:05–02:30 — Stabilize COO control

### 02:10–02:30 — Multi-agent delegation skill update
- Codify WIP lane policy for Bông/Bún/Render/Antigravity/Cáo/Trợ Lý.
- Add delegation template: owner/deadline/acceptance/evidence/rollback/escalation.
- Output: `company-os/ops/skills/troly_multi_agent_delegation_skill_20260605.md`.

- Scan A2A bus/task registry, lập danh sách active tasks.
- Chuẩn hoá status: DONE/PARTIAL/NOT_STARTED/BLOCKED.
- Output: `troly_active_task_snapshot_20260605_0230.md`.

### 02:30–03:15 — Evidence registry + Henry daily view v0
- Tạo `company-os/ops/evidence_registry.jsonl` nếu chưa có.
- Tạo dashboard đọc nhanh cho Henry: Dify, Upharma, Game, BaDiVi, blockers.
- Output: `HENRY_DAILY_VIEW_20260605_0315.md`.

### 03:15–04:00 — Dify adoption package import-ready
- Rà lại 6 app blueprint/KB manifest/runbook.
- Chốt native Dify unblock list: credential/session/provider/app import steps.
- Output: `native_dify_import_readiness_20260605_0400.md`.

### 04:00–05:00 — Upharma/Bông handoff control
- Audit drug DB staging/review pack status.
- Chốt next owner/action cho 63/64 SKU staging hoặc blocker human/pharmacist.
- Output: `upharma_drug_db_handoff_control_20260605_0500.md`.

### 05:00–06:00 — Game/Bún handoff control
- Audit live GitHub game, mobile fix, remaining Unity/Archero-like roadmap.
- Chốt trial DONE + next milestone không làm lan man.
- Output: `epoch_game_handoff_control_20260605_0600.md`.

### 06:00–07:00 — A2A watcher minimum viable
- Tạo script scan bus quá hạn + NEW chưa ACK + output markdown.
- Dry-run không mutate production.
- Output: `automation/a2a_watcher/a2a_watcher_report_20260605_0700.md`.

### 07:00–08:00 — COO morning report
- Tổng hợp: status, evidence, blocker, next 3 actions.
- Gửi báo cáo 08:00 cho Henry.
- Output: `COO_MORNING_REPORT_20260605_0800.md`.

## Guardrails
- Không mở research/tool mới.
- Không ghi/xoá production DB.
- Không public dữ liệu nội bộ.
- Không báo DONE/PARTIAL nếu thiếu evidence path/link/log + size.
