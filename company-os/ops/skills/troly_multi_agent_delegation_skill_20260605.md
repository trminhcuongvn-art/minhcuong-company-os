# Trợ Lý skill — Multi-agent delegation & workload distribution

Created: 2026-06-05 02:08 ICT
Owner: Trợ Lý / COO Execution Coordinator
Scope: Bông, Bún, Render, Antigravity, Cáo, Trợ Lý

## Mục tiêu
Tăng năng lực đa nhiệm: không để Trợ Lý làm tuần tự mọi thứ; biết chia việc đúng agent, giữ WIP thấp, kiểm evidence, ép unblock đúng lúc.

## Nguyên tắc điều phối
1. One owner per task
- Mỗi task chỉ có 1 owner chính.
- Contributor được ghi rõ nhưng không được làm mờ trách nhiệm.

2. WIP limit
- Mỗi execution agent tối đa 1 CRITICAL + 1 SUPPORT task.
- Nếu agent còn task Henry giao chưa DONE/BLOCKED thật: không giao task mới ngoài cùng luồng.

3. Dispatch contract
Mọi giao việc phải có:
- task_id
- owner
- objective
- deadline/checkpoint
- acceptance criteria
- evidence_required path/link/log + size
- rollback
- escalation rule

4. Parallel lanes
- Bông lane: Upharma/drug DB/CRM/import-readiness.
- Bún lane: game/SaaS/Tarot/dropship/leadgen.
- Render lane: media/video/image artifacts + QA postflight.
- Antigravity lane: queued executor, bridge inbox/outbox, long-running technical jobs.
- Cáo lane: technical acceptance, Dify/OpenClaw/Gateway, blocker diagnosis.
- Trợ Lý lane: intake, prioritization, owner matrix, evidence gate, final report.

5. Cadence
- 30-min checkpoint: only delta artifact or NO_NEW_ARTIFACT.
- Critical task checkpoint: 15-min if blocked/near deadline.
- Missed SLA: mark STALLED/BLOCKED and reassign/unblock, not silent.

6. Pull vs push
- Agents push artifacts to bus/status.
- Trợ Lý pulls bus/status before every Henry report.
- Delivery not-requested is not excuse; audit runs/bus.

7. Priority scoring
Score = Henry_direct(5) + revenue_or_cost(3) + deadline_risk(2) + blocker_age(2) - dependency_wait(2)
Highest score gets active slot.

8. Anti-patterns banned
- “Đang theo sát” without artifact.
- Reporting old evidence as new.
- Letting Bông/Bún/Render outputs hide Trợ Lý/Cáo unfinished work.
- Researching new tools while direct tasks are PARTIAL and locally actionable.

## Delegation templates
### TASK
```json
{
  "intent":"TASK",
  "task_id":"...",
  "owner":"bong|bun|render|antigravity|cao|troly",
  "priority":"CRITICAL|HIGH|MEDIUM",
  "objective":"...",
  "deadline":"ISO8601",
  "acceptance":["..."],
  "evidence_required":["path/link/log + size"],
  "rollback":"...",
  "escalation":"if no artifact by checkpoint => BLOCKED/STALLED"
}
```

### CHECKPOINT AUDIT
- Read artifacts after last checkpoint.
- Compare mtime/size.
- Update status only with evidence.
- If no new artifact: say NO_NEW_ARTIFACT, not DONE/PARTIAL.

## Immediate implementation to 08:00
- Add active owner matrix to 02:30 snapshot.
- Add evidence registry entries per lane.
- Add A2A watcher MVP with per-agent WIP and overdue NEW/IN_PROGRESS scan.
- 08:00 report must include per-agent: active task, status, evidence, next deadline, blocker.

## Status
PARTIAL: skill codified. Needs automation in watcher and first real 08:00 report validation.
