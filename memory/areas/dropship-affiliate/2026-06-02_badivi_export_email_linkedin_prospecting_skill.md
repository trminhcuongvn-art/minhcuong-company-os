# BaDiVi — Email Outbound Deliverability + LinkedIn B2B Prospecting (Xuất khẩu)

Ngày: 2026-06-02 (Bún heartbeat learning)
Mục tiêu: biến top50 outreach list (ASEAN 28 + nội địa 20) thành reply rate đo được, không vào spam.
Bổ sung cho: cold_outreach_copywriting, alibaba_xnk_setup. KHÔNG trùng các note Reel/DM.

## 1. Vì sao email outbound B2B xuất khẩu hay thất bại
- Vào spam vì domain mới gửi cold, không warm-up, thiếu SPF/DKIM/DMARC.
- Gửi từ Gmail cá nhân → bị flag, không scale, không tracking.
- Email quá dài, nhiều link/ảnh, file đính kèm nặng → spam filter.
- Không cá nhân hóa → bounce + report spam → giết domain.

## 2. Hạ tầng gửi cần có TRƯỚC khi gửi (evidence gate)
- Domain phụ để gửi cold (vd: badivipack.com thay vì domain chính) → bảo vệ domain chính.
- 3 bản ghi DNS BẮT BUỘC: SPF, DKIM, DMARC. Kiểm tra bằng mail-tester.com (mục tiêu ≥ 8/10).
- Warm-up 2-3 tuần: ngày đầu 5-10 email, tăng dần ~30%/ngày, đến ~40-50/ngày/inbox.
- 1 inbox không gửi quá 40-50 cold/ngày. Cần volume → nhiều inbox + xoay vòng.
- Tool gợi ý: Instantly / Lemlist / Smartlead (warm-up + xoay inbox + tracking) — cần Henry duyệt ngân sách.

## 3. Cấu trúc cold email xuất khẩu (≤120 từ)
1. Subject: ngắn, cụ thể, không "bán". VD: "Packing tape supplier for [Company] shipments".
2. Dòng 1: lý do liên hệ cá nhân hóa (thấy họ là importer/distributor ngành X).
3. Dòng 2-3: 1 value cụ thể (FOB price, MOQ thấp, Trade Assurance, lead time).
4. CTA mềm: "Open to a quick quote sheet?" — không ép call.
5. Chữ ký: tên thật + công ty + website + (nếu có) Alibaba store link.
- KHÔNG đính kèm catalogue ở email 1. Gửi link hoặc đợi reply.

## 4. Sequence 4 chạm (mỗi chạm cách 2-3 ngày)
- Email 1: intro + value.
- Email 2: case/proof ngắn (loại khách đang phục vụ, không bịa số).
- Email 3: gửi quote sheet mẫu / bảng giá FOB.
- Email 4: break-up "should I close your file?" (tỷ lệ reply cao bất ngờ).
- Dừng ngay khi có reply → chuyển sang 1-1.

## 5. LinkedIn prospecting song song email
- Tìm decision maker: Procurement / Purchasing / Import Manager / Operations tại công ty logistics/e-commerce/3PL/đóng gói.
- Connect note ≤ 300 ký tự, không pitch ngay.
- Sau khi connect: 1 message value, rồi mới đề xuất quote.
- LinkedIn Sales Navigator filter: industry (Logistics & Supply Chain, Packaging), region (SEA), title.
- Giới hạn an toàn: ~20-25 connect request/ngày để không bị restrict.

## 6. KPI & evidence gate (đo thật, không định tính)
- CSV tracking: lead_id, channel(email/linkedin), sent_date, opens, replies, status.
- Mục tiêu benchmark cold B2B: open 40-60%, reply 5-10%, positive reply 1-3%.
- Deliverability gate: mail-tester ≥ 8/10 + bounce rate < 3% trước khi scale.
- Báo cáo phải có: số email gửi, % bounce, số reply thật (screenshot/CSV), không báo "đã gửi nhiều".

## 7. Việc cần Henry/Cáo duyệt trước khi chạy
- Mua domain phụ + ngân sách tool warm-up (Instantly/Smartlead ~$30-100/tháng).
- Tên pháp lý tiếng Anh + FOB price + MOQ (đã flag ở note Alibaba).
- LinkedIn account dùng để outreach (nguy cơ restrict nick chính).

## 8. Next actionable (khi được duyệt)
1. Setup domain phụ + SPF/DKIM/DMARC, chạy mail-tester lấy điểm.
2. Import top50_outreach CSV vào tool, viết 4 email sequence EN.
3. Warm-up 2 tuần, sau đó gửi batch nhỏ, log CSV reply.
