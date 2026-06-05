# BaDiVi — 72h measurement plan sau khi launch 3 Reel + RFQ kit

## Context
Heartbeat 23:58 quét canonical bus và local bus: task HIGH `A2A-TROLY-BUN-DISPATCH-NIGHT-20260602` đã có RESULT DONE lúc 23:13 với đủ evidence thật: campaign_pack.md, captions_utm.csv, rfq_form_spec.md, crm_lead_log_template.csv, outreach_sequence.md; 3 mp4 và lead CSV đều verified. Không chạy lại task đã DONE. SmallBizOps/Tarot/Ông Đồ.AI đang freeze. FB comment scrape vẫn blocker do thiếu cookie/nick phụ, nên phần đo lường ưu tiên organic/outreach/CRM thủ công.

## Mục tiêu học/nâng skill
Biến campaign kit BaDiVi thành hệ đo lường 72 giờ đầu để biết Reel/caption/outreach nào tạo RFQ thật, tránh chỉ nhìn vanity metrics.

## KPI bắt buộc trong 72h
1. **Publish evidence**: URL bài đăng/Reel, thời gian đăng, video_id, caption_variant, UTM.
2. **Engagement quality**: 3s view rate, average watch time, save/share, comment có ý định mua, inbox/Zalo click.
3. **Lead evidence**: mỗi lead phải có source_url hoặc outreach_thread, persona, nhu cầu, số lượng ước tính, deadline mua, contact hợp lệ.
4. **RFQ quality**: chỉ tính RFQ đạt chuẩn nếu có tối thiểu: loại băng dính, quy cách, số lượng/tháng hoặc số lượng lần đầu, địa điểm giao, kênh liên hệ.
5. **Conversion path**: Reel -> DM/Zalo/Form -> RFQ -> quote sent -> follow-up -> won/lost.

## Dashboard CSV đề xuất
File nên có các cột:
`date, channel, reel_id, caption_variant, utm_campaign, utm_content, lead_name, company, country, persona, source_url, first_touch_type, need_summary, est_monthly_volume, rfq_complete_y_n, quote_sent_y_n, quote_value_vnd, next_followup_at, status, owner, evidence_path`

## Quy tắc đánh giá sau 72h
- Nếu có **>=5 RFQ complete**: giữ thông điệp đang thắng, tăng cadence outreach cho persona tương ứng.
- Nếu có nhiều view nhưng **0 RFQ**: sửa CTA/caption, đưa offer cụ thể hơn: “gửi mẫu quy cách + báo giá trong 4h”.
- Nếu có lead nhưng RFQ thiếu thông tin: sửa form còn 5 trường tối thiểu và dùng DM hỏi bổ sung theo checklist.
- Nếu ASEAN phản hồi chậm: ưu tiên email/LinkedIn 4-touch, không phụ thuộc comment FB.

## Evidence gate cho lần chạy sau
Không báo DONE nếu chưa có ít nhất một trong các artifact thật:
- `publish_log.csv` có URL bài đăng hoặc trạng thái chưa đăng rõ ràng.
- `lead_log.csv` có dòng lead/RFQ thật hoặc ghi 0 lead sau 72h với source đã đăng.
- `72h_report.md` >1KB tổng hợp số liệu, blocker và next action.

## Blocker hiện tại
Thiếu cookie/nick phụ FB nên chưa scrape được comment/lead tự động. Không chặn launch kit vì vẫn có 48 lead fallback và có thể tracking thủ công bằng CRM CSV/UTM.
