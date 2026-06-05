# RFC-001 — Ông Đồ.AI Roadmap

Ngày: 2026-05-31
Owner: Trợ Lý
Reviewer: Cáo
Producer dự kiến: Bún
Status: PASS
Critique by: Cáo
Critique at: 2026-05-31 19:17 ICT
PASS at: 2026-05-31 19:18 ICT

## Critique notes (resolved)
1. 5 tool list đã chốt: Caption FB/Zalo, Mô tả sản phẩm, Email/tin nhắn KD, Tóm tắt văn bản, Bài đăng tuyển dụng
2. MVP zero-cost: template tĩnh + prompt guide, không gọi AI API thật

## 1. Context
Henry đã chốt tên tạm thời cho dự án Viết nhanh/Văn AI là **Ông Đồ.AI**. Trọng điểm hiện tại chuyển sang công cụ viết nhanh tiếng Việt cho người dùng phổ thông/kinh doanh. SmallBizOps hiện đã có trang `viet-nhanh.html`, cần đổi branding an toàn và xây roadmap sản phẩm rõ.

## 2. Objective đo được
Trong POC đầu tiên, cần đạt:
- 1 landing/tool page live với branding Ông Đồ.AI.
- Tối thiểu 5 công cụ viết tiếng Việt dùng được ngay, gồm:
  1. Caption mạng xã hội (Facebook/Zalo)
  2. Mô tả sản phẩm shop online
  3. Email/tin nhắn kinh doanh
  4. Tóm tắt văn bản dài
  5. Bài đăng tuyển dụng
- MVP dùng **template tĩnh + prompt guide** để zero-cost, người dùng copy sang ChatGPT/AI khác; chưa gọi AI API thật.
- UI/copy rõ: “Ông Đồ.AI — trợ lý viết tiếng Việt”.
- Có tracking hoặc ít nhất cấu trúc UTM sẵn để đo traffic sau.
- Evidence: URL live HTTP 200 + screenshot + test 5 template/prompt hiển thị đúng.

## 3. Scope in
- Rename UI/copy từ VietNhanh/Văn AI sang Ông Đồ.AI.
- Giữ URL hiện tại nếu cần tránh phá SEO (`viet-nhanh.html` có thể giữ, title đổi).
- Roadmap 3 giai đoạn:
  1. MVP: 5 tool viết nhanh tiếng Việt.
  2. Growth: template theo ngành/ngữ cảnh.
  3. Monetization: lead magnet, affiliate, gói trả phí sau.
- Xây workflow Producer-Reviewer: Bún execute, Cáo review evidence, Trợ Lý nghiệm thu.

## 4. Scope out
- Chưa mua domain mới.
- Chưa chạy ads.
- Chưa tích hợp thanh toán.
- Chưa gửi outreach công khai trước khi có review.

## 5. Options
### Option A — Rename nhẹ trên SmallBizOps hiện tại
Ưu: nhanh, ít rủi ro, tận dụng site có sẵn.
Nhược: URL `viet-nhanh.html` chưa khớp brand.

### Option B — Tạo route/site riêng `ongdo-ai`
Ưu: brand sạch hơn.
Nhược: thêm deploy/SEO tracking, mất thời gian hơn.

Đề xuất: **Option A trước**, sau khi có traction thì tách route riêng.

## 6. Risks/assumptions
- Brand “Ông Đồ.AI” có dấu/chấm dễ đẹp nhưng URL nên không dấu (`ongdo-ai`).
- Cần tránh claim quá mức kiểu “viết thay hoàn toàn”, nên dùng “trợ lý soạn thảo”.
- MVP không dùng AI API thật để tránh quota/cost; chỉ dùng template tĩnh + prompt guide. Nếu sau có traction mới cân nhắc API thật với prompt ngắn và quota limit.
- Cần font hỗ trợ tiếng Việt đầy đủ.

## 7. Evidence gate
- URL live HTTP 200.
- Screenshot trang Ông Đồ.AI.
- Test 5 tool/template: caption mạng xã hội, mô tả sản phẩm, email/tin nhắn kinh doanh, tóm tắt văn bản dài, bài đăng tuyển dụng.
- File diff/commit rõ.
- Cáo REVIEW_RESULT PASS trước khi báo Henry DONE.

## 8. Decision cần
Cáo critique proposal này trong 1 giờ. Nếu PASS/đồng ý có điều kiện, Trợ Lý sẽ giao Bún execute Phase 1.

## 9. Deadline
- Critique: trong 1 giờ.
- Phase 1 execute: trong 24 giờ sau khi critique PASS.
