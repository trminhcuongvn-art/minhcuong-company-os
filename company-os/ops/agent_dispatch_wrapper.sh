#!/bin/bash
# Usage: agent_dispatch_wrapper.sh <agent> <task_id> <status> <evidence> <next> [start_ts]
# Writes to task bus AND calls Dify completion gate
# v2: adds duration_ms tracking and persistent metrics log
AGENT=$1; TASK_ID=$2; STATUS=$3; EVIDENCE=$4; NEXT=$5; START_TS=$6
TS=$(date -u +"%Y-%m-%dT%H:%M:%S+07:00")
TS_EPOCH=$(date +%s%3N 2>/dev/null || date +%s)000
MSG_ID="A2A-$(echo $AGENT | tr a-z A-Z)-$(date +%Y%m%d-%H%M)"
LOG_FILE="/Users/minhcuong/.openclaw/workspace/memory/wrapper_metrics.jsonl"

# Calculate duration if start_ts provided (epoch ms)
DURATION_MS="null"
if [ -n "$START_TS" ]; then
  DURATION_MS=$(( TS_EPOCH - START_TS ))
fi

# Append to task bus
echo "{\"message_id\":\"$MSG_ID\",\"ts\":\"$TS\",\"ts_epoch_ms\":$TS_EPOCH,\"from_agent\":\"$AGENT\",\"to_agent\":\"cao\",\"intent\":\"RESULT\",\"status\":\"$STATUS\",\"task_id\":\"$TASK_ID\",\"evidence\":\"$EVIDENCE\",\"next\":\"$NEXT\",\"duration_ms\":$DURATION_MS}" >> /Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl

# Append to metrics log (lightweight — agent, status, duration only)
echo "{\"ts\":\"$TS\",\"agent\":\"$AGENT\",\"task_id\":\"$TASK_ID\",\"status\":\"$STATUS\",\"duration_ms\":$DURATION_MS}" >> "$LOG_FILE"

# Call Dify completion gate
python3 /Users/minhcuong/.openclaw/workspace/company-os/ops/dify_completion_gate_caller.py \
  --agent "$AGENT" --task-id "$TASK_ID" --status "$STATUS" \
  --evidence "$EVIDENCE" --rollback "none" --next "$NEXT" > /tmp/gate_${AGENT}_${TASK_ID}.json 2>&1

echo "DISPATCHED $AGENT $TASK_ID $STATUS"
