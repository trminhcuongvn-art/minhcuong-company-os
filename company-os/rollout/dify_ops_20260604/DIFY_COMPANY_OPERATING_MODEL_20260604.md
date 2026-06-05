# Dify Company Operating Model — 2026-06-04

Status: PARTIAL — implementation blueprint created by Cáo after Henry directive. Local Dify evidence gate already PASSED.

## Problem to fix
Current company AI work is fragmented:
- Telegram chat asks are not reliably converted into executable tasks.
- A2A file bus exists but does not wake/drive agents automatically.
- Agents report progress inconsistently unless Cáo audits evidence.
- Dify is running but not yet the operational front door for Company OS workflows.

## Target model
Dify becomes the operating layer for company work intake, routing, evidence, and review.

Telegram/Henry request → Dify Intake App → Company OS Workflow → Task Registry → Agent Executor/Wake → Evidence Gate → Cáo summary → Henry/group.

## P0 workflows
1. Task Intake + Router
- Input: Henry/group request text.
- Output: structured task JSON with owner, priority, risk, due time, required evidence, rollback.
- Routes to: Trợ Lý/Bông/Bún/Cáo/Render.
- Acceptance: every task has id, owner, DONE/PARTIAL/BLOCKED/NOT_STARTED criteria.

2. A2A Wake + Follow-up
- Input: task registry NEW/IN_PROGRESS rows.
- Output: session wake/direct dispatch/cron heartbeat.
- Acceptance: if agent does not ACK within SLA, Dify marks BLOCKED and escalates to Cáo.

3. Evidence Gate
- Input: claimed DONE/PARTIAL and artifact paths.
- Output: pass/fail evidence check; no DONE/PARTIAL without path/log.
- Acceptance: status cannot be DONE without file path + size/log verification.

4. Company Knowledge Q&A
- Input: Company OS docs and rules.
- Output: answer with cited local file paths.
- Acceptance: no unsourced operational answer.

5. Review Assistants
- Upharma read-only review queue assistant.
- Dify app suggests flags/checklist only; no production DB write.

## Immediate implementation sequence
1. Freeze manual A2A as source of truth but stop relying on passive polling.
2. Create a Dify-facing task registry schema and local JSONL bridge.
3. Add a dispatcher script that reads registry and wakes/dispatches agents.
4. Create acceptance test pack for 3 P0 workflows.
5. Only after local pass, wire authenticated Dify app/workflow API.

## Guardrails
- No prod DB writes without approval.
- No external outreach without approval.
- No raw token/secret in artifacts.
- Rollback must be listed per workflow.

## Rollback
Remove this rollout folder and disable dispatcher/cron job if created.
