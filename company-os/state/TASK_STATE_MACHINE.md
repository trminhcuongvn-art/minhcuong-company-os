# Task State Machine

Allowed states:
BACKLOG -> THIS_BLOCK -> BUILDING -> VERIFYING -> DONE
BACKLOG -> THIS_BLOCK -> BLOCKED
THIS_BLOCK/BUILDING -> STALLED
ANY -> KILLED
DONE -> LEARNED

State rules:
- THIS_BLOCK requires owner, acceptance criteria, risk class, due checkpoint.
- BUILDING requires started_at and expected artifact.
- VERIFYING requires test/check command or review checklist.
- DONE requires evidence path/URL + size/log/test.
- BLOCKED requires exact blocker + what was tried + unblock owner.
- STALLED if no artifact/evidence after checkpoint or 2 audit cycles.
- KILLED requires reason and replacement/next priority.

Risk classes:
LOW: reversible, no spend, no sensitive data, no public external action.
MEDIUM: internal data write or public draft but reversible.
HIGH: spending, customer-facing publish, sensitive data, irreversible action, strategic pivot.

Autonomy:
- LOW: agent acts without asking.
- MEDIUM: agent may act if delegated in block plan; otherwise ask Trợ Lý/Cáo.
- HIGH: ask Henry.
