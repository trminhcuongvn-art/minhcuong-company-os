# BaDiVi Social SaaS — adapter contracts & evidence-first publish design (2026-06-03 15:01)

## Context
Heartbeat Bún quét canonical/local bus: các task BaDiVi script Reel, render, campaign kit và Social SaaS micro-deliverable đã có RESULT/DONE với artifact thật. SmallBizOps/Tarot/Ông Đồ.AI đang freeze theo lệnh vận hành hiện tại; FB leadgen tự động vẫn blocker cookie/nick phụ nhưng không chặn thiết kế SaaS nội bộ.

## Chủ đề học/nâng skill
Thiết kế contract cho platform adapter của Badivi Social SaaS để sau này publish/DM/log không bị lẫn logic nghiệp vụ với token nền tảng.

## Adapter contract tối thiểu
Mỗi platform adapter (Facebook Page, Zalo OA, TikTok, LinkedIn) nên expose 5 hàm, trả về object chuẩn có `status`, `external_id`, `evidence_url`, `raw_response_path`, `rollback_hint`:

1. `validate_credentials()` — chỉ kiểm token/quyền, không publish.
2. `preflight_post(asset, caption, utm)` — kiểm file >1KB, duration/resolution nếu video, caption có CTA/RFQ link.
3. `publish_post(content_id, dry_run=False)` — idempotent theo `content_id`; nếu gọi lại không tạo post trùng.
4. `fetch_engagement(external_id, since)` — lấy metrics và comment/inbox nếu được phép.
5. `private_reply_or_dm(lead_id, template_id)` — chỉ chạy khi policy cho phép, log từng message.

## State machine đề xuất
`DRAFT -> READY_FOR_QA -> QA_PASSED -> SCHEDULED -> PUBLISHED -> MEASURED -> RFQ_CAPTURED -> FOLLOWED_UP -> CLOSED/LOST`

Guardrail bắt buộc:
- Không cho `SCHEDULED` nếu asset path không tồn tại hoặc <=1KB.
- Không cho `PUBLISHED` nếu thiếu `preflight_report_path`.
- Không cho `RFQ_CAPTURED` nếu thiếu ít nhất: contact, company/use_case, SKU_need, quantity/MOQ hint, deadline.
- Mọi transition ghi `audit_log.jsonl` để Evidence Gate kiểm.

## Evidence registry schema
Một dòng JSONL cho mỗi artifact:
```json
{"content_id":"badivi-reel-01","artifact_type":"video","path":".../badivi_reel_01.mp4","size_bytes":1100000,"sha256":"...","status":"qa_passed","created_at":"..."}
```

Một dòng JSONL cho mỗi publish attempt:
```json
{"content_id":"badivi-reel-01","platform":"zalo_oa","dry_run":true,"status":"preflight_pass","external_id":null,"raw_response_path":"logs/preflight_001.json","rollback_hint":"no-op dry run"}
```

## KPI cho SaaS nội bộ
- Operational KPI: % content qua QA lần đầu, số publish duplicate = 0, số artifact thiếu evidence = 0.
- Growth KPI: RFQ qualified / 1.000 views, RFQ -> quote sent, quote -> won.
- Reliability KPI: adapter error rate, retry success rate, time từ lead vào CRM đến follow-up đầu tiên.

## Acceptance gap hiện tại
Đã có state machine skeleton, adapter spec và smoke test local; chưa có token nền tảng nên chỉ dry-run/spec. Khi có token thật phải thêm sandbox smoke test: validate credential + preflight + dry-run log, tuyệt đối chưa auto publish production nếu chưa được duyệt.

## Rollback
Thiết kế này là note học tập, không ghi production. Rollback: xoá file note này; không ảnh hưởng data thật.
