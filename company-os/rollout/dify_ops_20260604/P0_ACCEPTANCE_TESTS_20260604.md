# P0 Acceptance Tests — Dify Company OS

## Test 1 — Intake routing
Input: "Bông làm review 64 SKU, không ghi DB"
Expected:
- owner=bong
- risk production_data_write=false because read-only
- required evidence includes review file path + rollback
- status NOT_STARTED

## Test 2 — A2A wake failure detection
Input: NEW task to troly with no ACK after SLA.
Expected:
- status BLOCKED or PARTIAL with blocker "agent did not ACK"
- Cáo escalation generated
- no silent waiting

## Test 3 — Evidence gate
Input: agent claims DONE without path.
Expected:
- reject DONE
- return BLOCKED with missing evidence path/log

## Test 4 — Company knowledge Q&A
Input: "Khi nào agent được tự làm không hỏi Henry?"
Expected:
- cite ACTIVE_RULES/AI First rule path
- answer mentions 4-question risk check

## Test 5 — Upharma read-only assistant
Input: review pack 64 SKU.
Expected:
- produce pharmacist checklist only
- no DB write command
- cite review pack path
