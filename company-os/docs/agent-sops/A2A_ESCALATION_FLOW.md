# A2A Escalation Flow — Upharma (Bông → Cáo)

Ngày tạo: 2026-06-05  
Owner: Bông  
Scope: Task Upharma trong `/Users/minhcuong/.openclaw/workspace/upharma/`

## 0) Mục tiêu

Khi Bông gặp khó khăn/blocker, quy trình này giúp:

1. Bông tự xử đủ sâu nhưng không đốt deadline.
2. Escalate lên Cáo đúng lúc, có evidence, có phương án tiếp theo.
3. Không báo DONE/PARTIAL nếu thiếu evidence path/log/link.
4. Không hỏi Henry/Cáo nếu việc có thể tự làm theo AI-FIRST checklist.

## 1) Checklist bắt buộc trước khi escalate

Trước khi hỏi/escalate, Bông tự kiểm 4 câu:

| Câu hỏi | Nếu CÓ | Nếu KHÔNG |
|---|---|---|
| Có tốn tiền/license/API trả phí không? | Hỏi/escalate trước | Tự làm |
| Có đụng dữ liệu thật/production không? | Hỏi/escalate trước | Tự làm |
| Có khó rollback/khó phục hồi không? | Hỏi/escalate trước | Tự làm |
| Có public dữ liệu nội bộ không? | Hỏi/escalate trước | Tự làm |

Nếu **KHÔNG cả 4** → Bông phải tự làm ngay, không hỏi.  
Nếu **CÓ bất kỳ câu nào** → escalate kèm đề xuất + rollback.

## 2) Bông tự xử tối đa bao lâu?

### 2.1 Theo mức deadline

| Loại task | Thời gian tự xử tối đa trước escalation | Quy tắc |
|---|---:|---|
| Deadline gấp ≤ 30 phút | 5–8 phút | Không quá 25% thời lượng còn lại |
| Deadline 30–90 phút | 10–15 phút | Nếu 2 hướng fail liên tiếp → escalate |
| Deadline trong ngày | 25–35 phút | Nếu vẫn chưa có path rõ ràng → escalate |
| Không deadline rõ | 45 phút | Sau 45 phút phải báo trạng thái hoặc escalate |
| Task có rủi ro production/tốn tiền/public | 0 phút | Escalate trước khi thao tác |

### 2.2 Trigger escalate ngay, không chờ hết thời gian

Escalate ngay khi gặp một trong các tình huống:

- Cần quyền/credential/API key/license chưa có.
- Cần quyết định nghiệp vụ: pharmacist review, sửa phân loại thuốc nhạy cảm, thay đổi tiêu chí KPI.
- Có nguy cơ ghi/xóa/sửa database production, Google Sheet chính, GitHub Pages public có dữ liệu nội bộ.
- Tool/service lỗi hệ thống không thể workaround sau provider cascade.
- Dữ liệu đầu vào mâu thuẫn hoặc thiếu nguồn xác thực, có nguy cơ bịa số liệu.
- Deadline sẽ miss nếu tiếp tục tự debug.
- Đã thử ít nhất 2 approach hợp lý mà chưa đạt acceptance.

## 3) Quy trình tự xử trước escalation

### Step A — Audit task và evidence hiện có

- Đọc task bus canonical trước khi báo tiến độ:
  - `/Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl`
- Kiểm tra file output/log hiện có bằng `ls`, `tail`, `wc`, script verify nếu có.
- Không dựa trí nhớ.

### Step B — Xác định acceptance gate

Ghi rõ trong note nội bộ hoặc audit:

- Task ID.
- Output bắt buộc.
- Evidence bắt buộc.
- Deadline.
- Ràng buộc: `db_writes=0`, không production, không public nội bộ, rollback.

### Step C — Tự thử theo cascade

Ví dụ với enrichment/websearch:

1. Đọc skill bắt buộc: `tools/websearch_skill_upgrade_20260604.md`.
2. Query cascade: exact name → normalized name → hoạt chất → SKU/product code → domain dược uy tín.
3. Provider cascade: web_search/web_fetch → site search DAV/Long Châu/Pharmacity/trungtamthuoc/nhà sản xuất → ddgs/SearXNG nếu sẵn/cài không tốn phí.
4. Ghi `provider_errors`, nguồn đã thử, phân loại `VERIFIED_PUBLIC_SOURCE / NEEDS_LABEL_REVIEW / NOT_FOUND`.

Ví dụ với báo cáo:

1. Chạy trong venv: `cd /Users/minhcuong/.openclaw/workspace/upharma && source .venv/bin/activate && bash chay_bao_cao.sh`.
2. Lưu log nếu lỗi.
3. Kiểm tra output GitHub Pages/report file.
4. Nếu lỗi dữ liệu thật/production hoặc deploy public nội bộ → escalate trước khi publish.

### Step D — Quyết định status

Chỉ dùng 4 status:

- `DONE`: đạt acceptance, có evidence path/log/link.
- `PARTIAL`: có output/evidence thật nhưng chưa đạt toàn bộ acceptance.
- `BLOCKED`: không thể tiếp tục vì cần người/quyền/quyết định/rủi ro.
- `NOT_STARTED`: chưa bắt đầu; chỉ dùng khi thực sự chưa làm.

Không ghi DONE/PARTIAL nếu thiếu evidence.

## 4) Escalate lên Cáo như thế nào?

### 4.1 Kênh A2A chuẩn

Ghi result/escalation vào task bus qua wrapper nếu task yêu cầu hoặc cần báo chính thức:

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong <task_id> <STATUS> "<evidence_path_or_log>" "<next_step_or_request>"
```

Ví dụ:

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong bong_drug_enrich_fullsku_20260605_1223 PARTIAL \
  "upharma/4_Ket_Qua_AI/drug_enrich_fullsku_20260605/audit_batch1_20260605.md" \
  "cần Cáo quyết: tiếp tục rule-based hay chờ pharmacist review cho nhóm KHAC"
```

### 4.2 Khi cần escalated message chi tiết hơn

Nếu wrapper `next` quá ngắn, tạo audit file `.md` trong output folder rồi đưa path vào evidence. Audit file nên có:

- Task ID.
- Tóm tắt blocker.
- Đã thử gì.
- Evidence/log.
- Rủi ro.
- Phương án đề xuất.
- Rollback.
- Câu hỏi cần Cáo quyết.

## 5) Format message escalation

### 5.1 Format ngắn qua wrapper

```text
STATUS: BLOCKED hoặc PARTIAL
Evidence: <path/log/link>
Next: <một câu hỏi hoặc đề xuất rõ ràng cho Cáo>
```

Command:

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong <task_id> BLOCKED "<audit_path_or_log_path>" "<request_for_cao>"
```

### 5.2 Format đầy đủ trong audit file

```md
# Escalation — <task_id>

- Time: <YYYY-MM-DD HH:MM GMT+7>
- From: Bông
- To: Cáo
- Status: BLOCKED | PARTIAL
- Deadline: <deadline nếu có>
- Acceptance: <điều kiện DONE>

## Blocker
<1-3 dòng mô tả vấn đề>

## Đã thử
1. <approach 1> → <kết quả/log>
2. <approach 2> → <kết quả/log>
3. <fallback> → <kết quả/log>

## Evidence
- <path/log/link 1>
- <path/log/link 2>

## Rủi ro nếu tự tiếp tục
- <production/public/cost/rollback/deadline/data quality>

## Đề xuất của Bông
- Option A: <khuyến nghị> — rollback: <cách rollback>
- Option B: <phương án khác> — rollback: <cách rollback>

## Cần Cáo quyết
<single clear question>
```

### 5.3 Message mẫu cho Cáo

```text
[BÔNG] BLOCKED task <task_id>.
Blocker: <mô tả ngắn>.
Đã thử: <2-3 approach>.
Evidence: <audit/log path>.
Rủi ro: <nếu tự tiếp tục>.
Đề xuất: <option khuyến nghị + rollback>.
Cần Cáo quyết: <câu hỏi cụ thể>.
```

## 6) Ví dụ thực tế từ task Upharma

### Ví dụ 1 — Enrich thuốc: web_search bị 429

Không được BLOCKED chỉ vì một provider 429.

**Cách xử đúng:**

1. Đọc `tools/websearch_skill_upgrade_20260604.md`.
2. Thử query cascade: exact product title, normalized product name, hoạt chất, SKU, site search domain dược.
3. Thử provider cascade: `web_search`, `web_fetch`, nguồn DAV/SĐK, Long Châu, Pharmacity, trungtamthuoc, nhà sản xuất, ddgs/SearXNG nếu sẵn.
4. Tạo files:
   - `candidates.csv`
   - `sources.csv`
   - `audit.md`
   - `next_batch.csv`
5. Nếu vẫn chưa xác minh được, phân loại `NEEDS_LABEL_REVIEW` hoặc `NOT_FOUND`, không bịa.

**Escalate chỉ khi:** sau cascade vẫn không đạt deadline hoặc cần quyết định nghiệp vụ.

Command mẫu:

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong bong_drug_enrich_fullsku_20260605_1223 PARTIAL \
  "upharma/4_Ket_Qua_AI/drug_enrich_fullsku_20260605/audit_batch1_20260605.md" \
  "đã cascade search; còn nhóm NEEDS_LABEL_REVIEW, chờ Cáo quyết tiếp tục batch rule-based hay pharmacist queue"
```

### Ví dụ 2 — Báo cáo Upharma lỗi khi chạy script

**Tình huống:** `bash chay_bao_cao.sh` lỗi do thiếu cột trong CSV.

**Bông tự xử:**

1. Lưu log lỗi: `logs/report_run_<timestamp>.log`.
2. Kiểm tra schema input, script Python liên quan.
3. Nếu chỉ là fix code local, không production, rollback dễ → tự patch và chạy lại.
4. Nếu fix làm thay đổi logic KPI hoặc số liệu public trên GitHub Pages → escalate trước khi publish.

**Escalation mẫu:**

```text
[BÔNG] PARTIAL task upharma_report_run_<date>.
Blocker: script báo cáo lỗi thiếu cột `gross_profit`, có thể map từ `profit` nhưng sẽ đổi logic KPI.
Đã thử: verify schema input + chạy lại script; log ở logs/report_run_20260605_1420.log.
Evidence: upharma/logs/report_run_20260605_1420.log.
Rủi ro: publish KPI sai lên GitHub Pages.
Đề xuất: dùng mapping tạm trong staging report, chưa deploy public; rollback revert patch.
Cần Cáo quyết: có cho map `profit -> gross_profit` cho kỳ này không?
```

### Ví dụ 3 — Pharmacist review/import staging

**Tình huống:** Henry nói không cần pharmacist duyệt cho một bước enrichment, nhưng import staging vẫn có thể ảnh hưởng dữ liệu thật.

**Cách xử đúng:**

- Tạo full enriched CSV + staging import plan.
- `db_writes=0` cho đến khi staging plan hoàn tất/được duyệt.
- Không ghi production DB nếu chưa được duyệt.

**Escalate mẫu:**

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong bong_drug_enrich_fullsku_20260605_1223 PARTIAL \
  "upharma/4_Ket_Qua_AI/drug_enrich_fullsku_20260605/staging_import_plan.md" \
  "cần Cáo xác nhận import staging; rollback: delete staging rows by batch_id"
```

### Ví dụ 4 — Không có evidence thì không DONE/PARTIAL

Sai:

```text
DONE — đã chạy xong theo trí nhớ.
```

Đúng:

```bash
bash /Users/minhcuong/.openclaw/workspace/company-os/ops/agent_dispatch_wrapper.sh \
  bong <task_id> DONE \
  "upharma/4_Ket_Qua_AI/<folder>/<artifact>.csv" \
  "chờ review Cáo"
```

Trước khi báo, kiểm tra:

```bash
ls -lh <artifact>
wc -l <artifact>
tail -n 5 /Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl
```

## 7) Rollback chuẩn

Mỗi escalation phải có rollback hoặc ghi rõ `rollback=none` nếu chỉ đọc/tạo file mới.

Rollback gợi ý:

- File output mới: `rm -f <file1> <file2>` hoặc `rm -rf <output_dir>`.
- Code patch: `git diff` + `git checkout -- <file>` nếu repo sạch; hoặc copy `.prepatch`.
- Staging DB: delete theo `batch_id`/transaction ID, không xóa mơ hồ.
- GitHub Pages public: revert commit hoặc deploy bản trước.

## 8) Cadence báo cáo khi đang kẹt nhưng chưa BLOCKED

Nếu task dài và vẫn đang chạy:

- Mỗi 30–45 phút hoặc trước deadline 10 phút: báo `PARTIAL` nếu có artifact thật.
- Nếu chưa có artifact, tạo audit log và báo `BLOCKED` hoặc tiếp tục tự xử nếu còn trong timebox.
- Không heartbeat vô nghĩa.

## 9) Preflight mini-checklist trước khi gửi Cáo

- [ ] Đã audit task bus/file mới, không dựa trí nhớ.
- [ ] Status chỉ là DONE/PARTIAL/NOT_STARTED/BLOCKED.
- [ ] Có evidence path/log/link thật.
- [ ] Có next step/câu hỏi rõ ràng.
- [ ] Có rollback hoặc lý do `rollback=none`.
- [ ] Không leak token/dữ liệu nội bộ ra public/group chat.
- [ ] Với search/enrichment: có provider_errors + nguồn đã thử trong audit.

## 10) Một dòng nhớ nhanh

**Tự xử theo timebox → tạo evidence → nếu rủi ro/deadline/2 approach fail thì escalate Cáo bằng wrapper, kèm blocker + đã thử + evidence + đề xuất + rollback.**
