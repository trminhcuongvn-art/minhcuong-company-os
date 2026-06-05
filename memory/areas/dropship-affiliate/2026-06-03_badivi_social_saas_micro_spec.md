# BaDiVi Social SaaS — Queue/State Machine + Platform Adapter Spec

Timestamp: 2026-06-03 16:31 ICT
Owner: Bún
Scope: micro-deliverable cho Badivi Social SaaS, không phải marketing kit.

## Mục tiêu
Tạo lõi vận hành SaaS đăng bài/thu lead an toàn cho BaDiVi: nhận campaign asset (3 Reel + caption + UTM), xếp lịch publish thủ công/bán tự động, ghi trạng thái, thu lead/RFQ vào CRM CSV. Thiết kế ưu tiên adapter tách nền tảng để sau này gắn Facebook/Zalo/LinkedIn mà không viết lại core.

## AI First risk check
1. Tốn tiền/license: Không.
2. Ghi/xoá production/dữ liệu thật: Không, chỉ tạo spec local.
3. Khó rollback: Không, xoá file spec là rollback.
4. Public dữ liệu nội bộ: Không.
=> Tự làm ngay.

## Core entities
- Campaign: id, name, objective, offer, start_at, end_at, status.
- Asset: campaign_id, asset_path, type=video/image/text, checksum, duration, resolution.
- PostJob: campaign_id, platform, scheduled_at, caption, utm_url, status, retry_count.
- LeadEvent: source_platform, post_id, raw_text, intent_score, rfq_fields, owner, status.
- AdapterCredential: platform, auth_mode, secret_ref, status. Không lưu token plaintext trong DB.

## State machine: PostJob
DRAFT -> READY -> SCHEDULED -> PUBLISHING -> PUBLISHED -> MONITORING -> CLOSED

Exception states:
- BLOCKED_ASSET: thiếu file hoặc file <=1KB.
- BLOCKED_CREDENTIAL: thiếu cookie/token/quyền page.
- FAILED_PUBLISH: adapter trả lỗi; retry tối đa 2 lần rồi cần human review.
- ROLLBACK_REQUESTED: gỡ khỏi queue, không xoá log.

Acceptance gate trước READY:
- Video path tồn tại, size >1KB, nếu là Reel: 1080x1920 và 30-60s.
- Caption có CTA và UTM campaign/source/medium/content.
- CRM sink tồn tại: CSV/Sheet/API endpoint.
- Owner nhận lead được gán.

## State machine: LeadEvent
CAPTURED -> QUALIFIED_LIGHT -> RFQ_PENDING -> RFQ_COMPLETE -> QUOTED -> WON/LOST

RFQ required fields tối thiểu:
- company/name, phone/zalo/email
- product_need: băng dính/màng PE/carton/khác
- quantity/month hoặc one-off quantity
- ship_to province
- deadline
- current_supplier/problem nếu có

## Adapter interface
```ts
interface SocialAdapter {
  platform: 'facebook' | 'zalo' | 'linkedin' | 'manual';
  validateCredential(): Promise<AdapterHealth>;
  publish(job: PostJob): Promise<PublishResult>;
  fetchEngagement(postId: string, since?: string): Promise<EngagementEvent[]>;
  reply?(eventId: string, message: string): Promise<ReplyResult>;
}
```

## Adapter priority
1. ManualAdapter: export job JSON/CSV + checklist để người vận hành đăng thủ công; chạy ngay không cần credential.
2. FacebookPageAdapter: cần Page token/cookie hợp lệ; hiện BLOCKED nếu thiếu.
3. ZaloOA/UserAdapter: dùng khi có OA/user API hợp lệ; không tự xin key.
4. LinkedInCompanyAdapter: dùng cho outbound B2B/ASEAN sau khi có account/permission.

## Minimal queue loop
- load READY/SCHEDULED jobs
- preflight asset/caption/UTM/credential
- nếu manual: xuất publish_packet.md + crm_lead_log_template.csv
- nếu platform credential OK: publish, lưu publish_result
- sau publish: poll engagement theo interval, normalize LeadEvent, append CRM

## Evidence logging
Mỗi transition ghi JSONL:
```json
{"ts":"...","job_id":"...","from":"READY","to":"SCHEDULED","evidence":{"asset_size":735381,"utm":"..."}}
```
Không được báo DONE nếu thiếu file/log thật.

## Rollback
- Hủy job chưa publish: set status=ROLLBACK_REQUESTED.
- Job đã publish thủ công: tạo takedown_instruction.md, không tự xoá nếu chưa có quyền.
- Token/cookie: revoke ở platform, xoá secret_ref, giữ audit log không chứa secret.

## Acceptance gap hiện tại
- Có 3 Reel và campaign kit thật.
- Chưa có credential FB/Page/Zalo chính chủ để auto publish/comment-to-DM.
- Vì vậy phiên bản đầu nên ship ManualAdapter + queue audit trước, auto adapter để BLOCKED_CREDENTIAL rõ ràng.
