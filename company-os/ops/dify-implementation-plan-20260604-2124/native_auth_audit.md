# Native Dify auth/provider audit — 2026-06-04 21:43 ICT

## Scope
Find why native Dify app/workflow/KB creation is blocked and what is safe to do next. No DB writes, no secret exposure, no external calls.

## Observed endpoints
- `/` returns HTTP 307: web entrypoint is reachable.
- `/console/api/setup` returns HTTP 200: setup/system API reachable without app auth.
- `/console/api/system-features` returns HTTP 200: feature discovery reachable.
- `/console/api/apps` returns HTTP 401: app list/create requires authenticated console/API session.

## Interpretation
Runtime is healthy enough; blocker is not container availability. Native Dify automation needs one of:
1. Authenticated browser session/cookie for console, or
2. Console API token/session, or
3. Manual login followed by export/import using UI/browser automation.

## Safe next path
- Continue no-API Company OS lane for operations.
- For native lane, use browser/user session only if Henry/user already logged in and present; otherwise mark BLOCKED rather than attempting credential guessing/reset.
- Do not reset Dify credentials or mutate DB without explicit approval; that would touch auth/production-like state and is hard to rollback.

## Native creation target once auth exists
- App: Company Ops Evidence Auditor
- KB: Company OS Runbooks + Evidence Logs
- Workflow: A2A task intake -> Evidence Gate -> Status Report

## Rollback
If native objects are created later: delete the app, KB, workflow from Dify console and remove exported files under this plan folder.
