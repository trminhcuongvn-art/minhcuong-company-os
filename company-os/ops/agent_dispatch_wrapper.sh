#!/bin/bash
# Usage: agent_dispatch_wrapper.sh <agent> <task_id> <status> <evidence> <next>
# Writes to task bus AND calls Dify completion gate
AGENT=$1; TASK_ID=$2; STATUS=$3; EVIDENCE=$4; NEXT=$5
TS=$(date -u +"%Y-%m-%dT%H:%M:%S+07:00")
MSG_ID="A2A-$(echo $AGENT | tr a-z A-Z)-$(date +%Y%m%d-%H%M)"

# Append to task bus
echo "{\"message_id\":\"$MSG_ID\",\"ts\":\"$TS\",\"from_agent\":\"$AGENT\",\"to_agent\":\"cao\",\"intent\":\"RESULT\",\"status\":\"$STATUS\",\"task_id\":\"$TASK_ID\",\"evidence\":\"$EVIDENCE\",\"next\":\"$NEXT\"}" >> /Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl

# Call Dify completion gate
python3 /Users/minhcuong/.openclaw/workspace/company-os/ops/dify_completion_gate_caller.py \
  --agent "$AGENT" --task-id "$TASK_ID" --status "$STATUS" \
  --evidence "$EVIDENCE" --rollback "none" --next "$NEXT" > /tmp/gate_${AGENT}_${TASK_ID}.json 2>&1

echo "DISPATCHED $AGENT $TASK_ID $STATUS"
