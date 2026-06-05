# 2026-06-02 20:58 — BaDiVi landing page RFQ copy skill

## Bối cảnh heartbeat
Quét canonical bus `/Users/minhcuong/.openclaw/workspace/memory/agent_task_bus.jsonl` và bus local Bún. Không chạy lại các task freeze (SmallBizOps/Tarot/Ông Đồ.AI). BaDiVi 3 Reel đã có script + render RESULT. Việc còn thiếu trong phễu là landing page/lead form biến traffic Reel thành RFQ thật.

## Chủ đề học: Landing page RFQ cho BaDiVi băng dính/màng co B2B
Mục tiêu landing page không phải “giới thiệu đẹp”, mà là giảm ma sát để buyer gửi nhu cầu đóng gói. Với khách B2B, trang cần trả lời nhanh 5 câu hỏi: sản phẩm có hợp ngành của tôi không, có tư vấn size/quy cách không, tối thiểu đặt hàng/MOQ thế nào, báo giá mất bao lâu, và có mẫu/ảnh/ứng dụng thực tế không.

## Cấu trúc page đề xuất
1. **Hero 1 màn hình**
   - Headline: “Tối ưu vật tư đóng gói cho xưởng/kho/TMĐT — băng dính & màng co theo nhu cầu”
   - Subheadline: “Gửi quy cách thùng/hàng, BaDiVi tư vấn loại vật tư phù hợp và báo giá nhanh.”
   - CTA chính: “Nhận tư vấn & báo giá”
   - CTA phụ: “Xem 3 lỗi đóng gói hay gặp”

2. **Problem block**
   - Hàng bị bung/rách khi vận chuyển.
   - Dùng sai loại băng dính làm tăng hao hụt.
   - Màng co không ôm hàng, tốn thời gian đóng gói.
   - Đặt vật tư không ổn định làm gián đoạn kho.

3. **Solution block**
   - Băng dính đóng thùng, dán tem, cố định kiện.
   - Màng co/màng quấn bảo vệ hàng, gom kiện.
   - Tư vấn theo loại hàng, quy cách đóng gói, sản lượng dự kiến.
   - Không bịa claim “rẻ nhất” hay số liệu chưa kiểm chứng.

4. **RFQ form tối giản**
   Trường bắt buộc:
   - Tên công ty/cửa hàng
   - Ngành hàng: TMĐT, kho vận, thực phẩm, may mặc, linh kiện, khác
   - Sản phẩm cần: băng dính, màng co/màng quấn, cả hai
   - Nhu cầu/tháng hoặc số kiện/ngày
   - SĐT/Zalo
   Trường tùy chọn:
   - Kích thước thùng/kiện
   - Ảnh hiện trạng đóng gói
   - Ghi chú vấn đề đang gặp

5. **Trust/evidence block**
   - Ảnh/cuộn Reel minh họa lỗi đóng gói.
   - Checklist tư vấn quy cách.
   - Cam kết phản hồi theo SLA nội bộ: ghi “phản hồi trong giờ làm việc” nếu chưa có SLA chính thức từ Henry.

## Copy CTA mẫu
- “Gửi nhu cầu — nhận gợi ý vật tư phù hợp”
- “Tư vấn loại băng dính/màng co cho quy cách hàng của bạn”
- “Nhận báo giá theo sản lượng thực tế”

## Tracking cần gắn
- UTM theo từng Reel: `utm_source=facebook&utm_medium=reel&utm_campaign=badivi_rfq&utm_content=reel_01|02|03`
- Hidden field trong form: source, campaign, content, timestamp.
- CRM CSV tối thiểu: lead_id, created_at, source, content, company, industry, product_need, volume_hint, phone_zalo, status, next_followup_at.

## Evidence gate cho lần triển khai tới
Không tính DONE nếu thiếu:
- File landing page thật >1KB.
- Form tạo được CSV/Google Sheet row thật hoặc ít nhất local JSON/CSV test lead.
- 3 link Reel trỏ về landing page có UTM khác nhau.
- Ảnh chụp hoặc HTTP 200 page.

## Blocker cần Henry chốt
- Có cho công bố MOQ, khoảng giá, khu vực giao hàng không?
- SĐT/Zalo nhận lead chính thức là số nào?
- Có ảnh thật sản phẩm/kho/xưởng BaDiVi để tăng trust không?
