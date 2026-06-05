#!/usr/bin/env bash
set -euo pipefail
ROOT="${ROOT:-/Users/minhcuong/.openclaw/workspace}"
PLUGIN_GLOB="$ROOT/external/dify/docker/volumes/plugin_daemon/cwd/langgenius/openai-*/models/llm/llm.py"
PATCH_MARKER='cx/gpt-5.5'
LOG="$ROOT/company-os/ops/dify_plugin_autopatch.log"
shopt -s nullglob
files=( $PLUGIN_GLOB )
if [[ ${#files[@]} -eq 0 ]]; then echo "$(date +%Y-%m-%dT%H:%M:%S%z) BLOCKED no llm.py found" | tee -a "$LOG"; exit 2; fi
status=0
for f in "${files[@]}"; do
  if ! grep -q 'def _num_tokens_from_messages' "$f"; then echo "$(date +%Y-%m-%dT%H:%M:%S%z) BLOCKED missing signature $f" | tee -a "$LOG"; status=2; continue; fi
  if grep -q "$PATCH_MARKER" "$f"; then echo "$(date +%Y-%m-%dT%H:%M:%S%z) OK already patched $f" | tee -a "$LOG"; continue; fi
  cp "$f" "$f.bak.$(date +%Y%m%d%H%M%S)"
  python3 - "$f" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); s=p.read_text()
old='if model == "chatgpt-4o-latest" or model.startswith(("o1", "o3", "o4", "gpt-4.1", "gpt-4.5", "gpt-5")):'
new='if model == "chatgpt-4o-latest" or model.startswith(("o1", "o3", "o4", "gpt-4.1", "gpt-4.5", "gpt-5")) or model.startswith(("cx/gpt-5.5", "cc/claude-sonnet-4-6")):'
if old not in s:
    raise SystemExit('patch anchor not found')
p.write_text(s.replace(old,new,1))
PY
  echo "$(date +%Y-%m-%dT%H:%M:%S%z) PATCHED $f" | tee -a "$LOG"
done
exit $status
