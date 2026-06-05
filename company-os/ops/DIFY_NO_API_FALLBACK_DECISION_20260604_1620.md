# Dify No-API Fallback Decision — 2026-06-04 16:20 ICT

Decision by Henry: assume no Dify API auth. Do not use missing auth API as blocker anymore.

Operating mode:
- Use Local Company Ops as primary operating layer.
- Dify is optional UI/KB layer only when browser/session is available.
- Core loop: task registry -> dispatch -> SLA/ACK scanner -> evidence gate -> summary.

Acceptance rule:
- DONE/PARTIAL requires evidence path/size/log.
- Missing Dify API auth is not a blocker.
- Blockers must be about local loop failure, evidence absence, agent SLA miss, or production-write approval.

Immediate deliverables:
1. P0 local tests for Company OS Knowledge Q&A, A2A/task lookup, Upharma read-only review.
2. Update loop/report language to remove Dify API auth blocker.
3. Continue with no-auth fallback as canonical path.

Rollback:
- Remove `company-os/ops/*NO_API_FALLBACK*` and revert reports to previous auth-dependent model.
