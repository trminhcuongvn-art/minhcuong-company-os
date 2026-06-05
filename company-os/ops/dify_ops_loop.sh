#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/minhcuong/.openclaw/workspace"
cd "$ROOT"
LOG="company-os/ops/dify_ops_loop_$(date +%Y%m%d_%H%M%S).log"
{
  echo "[$(date -Iseconds)] Dify Ops loop start"
  ./company-os/ops/dify_ops_cli.py dispatch || true
  ./company-os/ops/dify_ops_cli.py scan || true
  ./company-os/ops/dify_ops_cli.py gate --status PARTIAL --evidence company-os/ops/task_registry.jsonl --evidence company-os/ops/dify_ops_cli.py --blocker "NO_API_FALLBACK canonical; Dify API optional" --next "Continue local Company Ops no-API path; API is optional future enhancement" || true
  python3 company-os/ops/dify_auth_probe.py || true
  echo "[$(date -Iseconds)] Dify Ops loop end"
} | tee "$LOG"
echo "$LOG"
