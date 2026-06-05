# Dify agent self-setup research — 2026-06-03

Finding: AI agent can self-setup Dify only if it has Console/Admin auth, not App API key.

Evidence from local source:
- Web console API prefix: /console/api (web/docker/entrypoint.sh, web/config/index.ts)
- Console dataset endpoints exist:
  - POST /console/api/datasets (create empty dataset)
  - POST /console/api/datasets/init (create dataset + first document)
  - POST /console/api/datasets/{id}/documents (add document)
  - PATCH /console/api/datasets/{id} (settings)
- App API /v1 with app-* key only runs published app/workflow; cannot configure datasets/apps/workflows.
- MCP endpoint reachable at /mcp/server/.../mcp but requires MCP client/protocol; GET returns 405 expected.

Self-setup options:
1. Best: provide Dify console session cookie / access token to agent. Then agent can call /console/api directly.
2. Alternative: browser automation with logged-in user session. Blocked by localhost browser policy in current environment.
3. Alternative: Dify MCP if it exposes dataset/app/workflow tools. Need MCP tool list/client config.
4. Fallback: human clicks UI; agent verifies via App API.

Next technical action:
- Obtain console auth from logged-in Dify browser session or Dify API login credentials.
- Then run script to create KB and upload docs via /console/api/datasets/init and /datasets/{id}/documents.
