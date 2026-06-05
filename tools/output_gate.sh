#!/bin/bash
# OUTPUT GATE — chạy trước mỗi hourly brief
# Kiểm tra có output thật trong N phút qua không
# Usage: ./output_gate.sh [minutes=60]

MINUTES=${1:-60}
WORKSPACE="/Users/minhcuong/.openclaw/workspace"

cd "$WORKSPACE"

# Check 1: git commits
COMMITS=$(git log --since="${MINUTES} minutes ago" --oneline 2>/dev/null | wc -l | tr -d ' ')

# Check 2: new/modified files
NEW_FILES=$(find . -newer <(date -v-${MINUTES}M +%Y%m%d%H%M.%S 2>/dev/null || date -d "${MINUTES} minutes ago" +%Y%m%d%H%M.%S 2>/dev/null) \
  -not -path "./.git/*" -not -path "./node_modules/*" -not -name "*.log" \
  -type f 2>/dev/null | wc -l | tr -d ' ')

echo "=== OUTPUT GATE REPORT ==="
echo "Window: last ${MINUTES} minutes"
echo "Commits: $COMMITS"
echo "Modified files: $NEW_FILES"

if [ "$COMMITS" -gt 0 ] || [ "$NEW_FILES" -gt 0 ]; then
  echo "STATUS: PASS — có output thật"
  echo "---"
  git log --since="${MINUTES} minutes ago" --oneline 2>/dev/null | head -5
  exit 0
else
  echo "STATUS: FAIL — không có output thật trong ${MINUTES} phút"
  echo "ACTION REQUIRED: chọn 1 TODO và làm ngay trước khi gửi brief"
  exit 1
fi
