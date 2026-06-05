# BaDiVi — A/B Test Framework + Thư viện Hook biến thể (đo lường được)

Ngày: 2026-06-03 03:43 (Asia/Saigon)
Agent: Bún | Loại: Heartbeat learning (không có task NEW; campaign kit đã DONE 23:13)
Liên kết: badivi-campaign-kit-20260603/ (3 Reel + captions_utm.csv + CRM template)

## 1. Vì sao cần A/B test có cấu trúc
3 Reel BaDiVi đã render + có UTM riêng (reel01/02/03). Khi publish, vấn đề là **không biết hook nào kéo RFQ**. Nếu test ngẫu nhiên sẽ không phân bổ được nguyên nhân. Cần khung test 1 biến/lần, đo bằng RFQ thật (không vanity).

## 2. Quy tắc test (1 biến đổi/lần)
- Mỗi chu kỳ chỉ đổi MỘT yếu tố: hook 3s đầu | caption dòng 1 | CTA | thumbnail/text overlay.
- Giữ nguyên phần còn lại để cô lập tác động.
- Mẫu tối thiểu trước khi kết luận: ≥1.000 view/biến HOẶC ≥7 ngày (lấy mốc đến trước). B2B traffic mỏng → ưu tiên mốc thời gian + số RFQ.
- North-star metric: **số RFQ hợp lệ** (qualified: có ngành + nhu cầu + volume/tháng). Phụ: hold-rate 3s, CTR link/inbox.

## 3. Thư viện hook 3s đầu (8 biến — gắn mã để track)
Mã hook ghi vào utm_content (vd: reel01_h3) để map ngược.
- H1 (Loss/sợ mất): "Mỗi tháng kho bạn mất bao nhiêu tiền vì băng dính bung keo?"
- H2 (Số cụ thể): "1 cuộn băng dính sai loại = 12% đơn hàng móp khi giao."
- H3 (Câu hỏi chẩn): "Hàng hay bị hoàn vì rách thùng? 90% là do màng co sai định lượng."
- H4 (Phản trực giác): "Mua băng dính rẻ nhất lại là cách đắt nhất."
- H5 (Định danh): "Xưởng/kho đóng >500 đơn/ngày — clip này cho bạn."
- H6 (Demo-first): [cảnh thùng bung keo khi nhấc] "Đây là lý do khách phàn nàn."
- H7 (Authority): "Vật tư đóng gói B2B chọn theo 3 thông số, không theo giá."
- H8 (Time/urgency): "Trước peak mùa cao điểm, kiểm tra 3 thứ này trong kho."

## 4. Biến CTA (test riêng sau khi chốt hook)
- C1: "Inbox 'RFQ' nhận checklist vật tư theo ngành." (lead magnet)
- C2: "Để lại ngành + sản lượng/tháng, BaDiVi báo phương án." (qualify ngay)
- C3: "Comment tên ngành, mình gửi mẫu định lượng phù hợp." (engagement→DM)
Giả thuyết: C1 ra nhiều lead nhưng loãng; C2 ít lead nhưng qualified cao hơn → ưu tiên C2 cho B2B.

## 5. Lịch test gợi ý (xoay vòng, không chờ cookie FB)
- Tuần 1: cố định caption/CTA, xoay hook H1/H3/H4 trên reel01 (3 lần đăng cách nhau).
- Tuần 2: chốt hook thắng → test CTA C1 vs C2.
- Tuần 3: chốt CTA → test caption dòng 1 (lợi ích vs nỗi đau).
- Ghi mọi lần đăng vào bảng test log (cột: ngày, asset, biến đổi, utm_content, view, hold3s, click/inbox, RFQ_qualified).

## 6. Test log schema (thêm vào campaign kit)
post_id,date,asset_id,variable_tested,variant_code,platform,views,hold_3s_pct,clicks_or_inbox,rfq_total,rfq_qualified,notes
→ Mỗi RFQ qualified map về variant_code để tính RFQ/1k view.

## 7. Quy tắc ra quyết định
- Thắng = RFQ_qualified/1k view cao hơn ≥30% ở mẫu đủ; nếu chênh <30% coi như hòa → giữ biến đơn giản/rẻ sản xuất.
- Hold-rate 3s chỉ dùng để loại hook quá yếu (<25% giữ), KHÔNG dùng làm tiêu chí thắng cuối.
- Mọi kết luận phải dựa trên RFQ thật trong CRM (crm_lead_log_template.csv), không suy từ like/share.

## 8. Blocker & ranh giới
- FB comment/lead scrape tự động vẫn cần cookie/nick phụ hợp lệ → KHÔNG chặn việc publish + nhập RFQ thủ công vào CRM.
- View/hold-rate lấy từ insight thủ công của trang khi đăng thật; chưa có nên framework ở trạng thái sẵn sàng, chờ data thật.

## 9. Hành động kế tiếp khi có traffic
1. Tạo file test_log.csv trong badivi-campaign-kit theo schema mục 6.
2. Gắn variant_code vào utm_content khi đăng.
3. Sau 7 ngày: tổng hợp RFQ/1k view theo variant → chốt hook + CTA thắng.
