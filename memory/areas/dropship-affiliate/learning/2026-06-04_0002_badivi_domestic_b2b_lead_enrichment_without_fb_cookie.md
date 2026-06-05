# 2026-06-04 00:02 — BaDiVi domestic B2B lead enrichment không cần cookie FB

## Context
Heartbeat quét canonical bus + local bus: không có task `to_agent=bun` NEW/IN_PROGRESS khả thi chưa có RESULT. Các task cũ SmallBizOps/Tarot/Ông Đồ.AI đang freeze; Epoch Ascendant MVP đã có spec + playable HTML; BaDiVi campaign kit/3 Reels/Social SaaS micro đã DONE. Vì vậy chuyển sang học tập/nâng skill cho BaDiVi leadgen.

## Mục tiêu
Tăng chất lượng 48 lead seed/các lead mới mà không phụ thuộc cookie FB. Đầu ra cần dùng được cho CRM/RFQ thủ công: ưu tiên tìm đúng buyer, kênh liên hệ, bằng chứng nhu cầu và next action.

## Playbook 5 bước enrichment
1. **Chuẩn hoá lead hiện có**
   - Company name, domain, ngành, tỉnh/thành, quy mô ước lượng, nguồn lead.
   - Gắn `lead_source_type`: distributor, ecommerce seller, manufacturer, warehouse/3PL, retailer, exporter.
2. **Tìm dấu hiệu nhu cầu packaging**
   - Website có trang giao hàng/fulfillment/kho vận.
   - Có sản phẩm dễ vỡ, cần đóng gói, shipping nationwide, B2B procurement.
   - Có bài tuyển kho/vận hành hoặc thông báo mở chi nhánh/kho mới.
3. **Tìm contact không cần FB cookie**
   - Website contact form, email sales/procurement, số Zalo OA/hotline, LinkedIn public, Google Maps public listing.
   - Ưu tiên kênh có khả năng phản hồi nhanh: Zalo/hotline/contact form trước, email sau.
4. **Chấm điểm RFQ readiness 0–10**
   - +2 có ngành phù hợp; +2 có dấu hiệu vận chuyển thường xuyên; +2 có contact rõ; +2 có quy mô vừa/lớn hoặc nhiều điểm bán; +2 có pain signal (hàng dễ vỡ/hoàn hàng/kho mới).
   - A: 8–10 gửi outreach ngay; B: 5–7 cần enrich thêm; C: 3–4 nurture; D: <3 loại.
5. **Câu hỏi outreach tối thiểu**
   - “Bên mình đang dùng loại thùng/băng dính/màng PE nào?”
   - “Sản lượng đóng gói/tháng khoảng bao nhiêu kiện?”
   - “Pain chính là vỡ hàng, hoàn hàng, chi phí vật tư, hay tốc độ đóng gói?”
   - “Có cần mẫu/báo giá theo MOQ không?”

## CRM fields đề xuất thêm
- `domain`, `province`, `lead_source_type`, `pain_signal`, `contact_channel_primary`, `contact_url`, `rfq_readiness_score`, `next_touch_date`, `outreach_template_id`, `evidence_url_1`, `evidence_note`.

## KPI thực dụng
- Enriched lead đủ contact: >=70% danh sách seed.
- A/B lead ratio: >=40% sau enrichment.
- RFQ-qualified rate từ lead A: mục tiêu khởi điểm 10–15% trong 7 ngày thủ công.
- Không dùng vanity metric; chỉ tính khi có contact/evidence/next action trong CRM.

## Blocker
Cookie FB/nick phụ vẫn cần nếu muốn auto scrape comment/group/insight. Không chặn enrichment qua website, Zalo, Google Maps, LinkedIn public và contact form.

## Rollback
Xoá file note này; không đụng production/API/credential.
