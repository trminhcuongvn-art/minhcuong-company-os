# Multi-Agent Operating Model v0 — Minh Cường

## Principle
Company can run multiple tasks in parallel, but each agent handles max 1 primary task per 8h block. Trợ Lý coordinates; agents execute.

## Agents
- Trợ Lý: Executive Planner/Router/Auditor.
- Cáo: Tech/QA/Safety/Evidence Monitor; Dify and infra owner.
- Bông: Upharma operations/reporting owner.
- Bún: BaDiVi/dropship/growth owner.
- Render: creative/video asset owner.
- Workers: spawned for bounded subtasks.

## State machine
NEW → TRIAGED → ASSIGNED → IN_PROGRESS → VERIFYING → DONE
Alternative states: BLOCKED, STALLED, PARKED, KILLED.

## 8h block cadence
- 08:00–16:00 Block A
- 16:00–24:00 Block B
- 00:00–08:00 Block C

Each block requires:
- Agent roster
- 1 primary task per agent
- Acceptance criteria
- Evidence path/link/log
- Blocker owner

## Current correction
The company is not limited to 1 task total. The failure was that Trợ Lý/Cáo were acting as only visible workers. New rule: every active track must either have assigned agent/worker or be PARKED/NOT_STARTED.
