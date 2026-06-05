# Dify native import runbook

Prereq: logged-in Dify console or valid console/API session; provider/model credential configured.

1. Open Dify console.
2. Create/import 5 KB datasets from `kb_manifest.json`.
3. Upload curated docs only; exclude secrets, tokens, cookies, large binaries.
4. Import each YAML in `dify_app_blueprints/` using Dify DSL import.
5. For each app, bind the matching KB dataset(s).
6. Configure provider/model.
7. Run smoke tests:
   - ask Evidence Auditor for latest 45m audit.
   - ask Upharma Copilot for batch 1-3 approval summary.
   - ask Router to classify a sample Henry request.
8. Export app DSL after smoke test back to this folder.
9. Record app IDs, KB IDs, smoke outputs in `native_import_result.md`.
10. Rollback: delete imported apps and datasets.
