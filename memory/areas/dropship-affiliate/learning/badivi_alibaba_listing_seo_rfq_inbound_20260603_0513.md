# BaDiVi — Alibaba/B2B Listing SEO & RFQ Inbound Optimization (Skill)

Ngày: 2026-06-03 05:13 (+07) — Heartbeat learning Bún
Bối cảnh: đã có file setup Alibaba (badivi_alibaba_xnk_setup_2026.md, 16.6KB) nói về chi phí/gói/quy trình lên sàn. Note này bổ sung phần CÒN THIẾU: tối ưu LISTING để được tìm thấy + biến traffic Alibaba/B2B directory thành RFQ inbound đo được. Không bịa số liệu sàn; mọi giả định đánh dấu [CẦN VERIFY].

## 1. Vì sao listing SEO quan trọng với BaDiVi
- Alibaba/Made-in-China rank sản phẩm theo: keyword match + completeness + response rate + Trade Assurance + lịch sử giao dịch. Listing tốt = inbound RFQ miễn phí, không phụ thuộc FB cookie (đang blocker).
- BaDiVi là supplier B2B (băng dính, màng PE, thùng carton, vật tư đóng gói) → buyer search bằng cụm chuyên ngành tiếng Anh. Match đúng từ khóa là 70% trận đấu.

## 2. Keyword research framework cho B2B đóng gói (làm được ngay, không cần cookie)
Quy tắc: mỗi listing nhắm 1 từ khóa chính (head) + 3-5 long-tail. Lấy ý tưởng từ:
- Alibaba search bar autosuggest (gõ "packing tape" → liệt kê gợi ý)
- "Related searches" cuối trang kết quả
- RFQ market (buyer post nhu cầu, ngôn ngữ thật của buyer)
- Đối thủ top 10: đọc tiêu đề listing của họ, trích cụm lặp lại

### Cụm từ khóa lõi BaDiVi (seed EN — [CẦN VERIFY volume trên sàn]):
| Nhóm | Head keyword | Long-tail mẫu |
|---|---|---|
| Băng dính | BOPP packing tape | clear bopp packing tape 48mm, custom printed packing tape, brown carton sealing tape |
| Màng PE | stretch film / pe stretch wrap | hand stretch film 17mic, machine pallet wrap, jumbo roll stretch film |
| Thùng carton | corrugated carton box | custom mailer box, shipping carton 5 ply, e-commerce packaging box |
| Vật tư | packaging materials supplier | bubble wrap roll, void fill, strapping band pp |

### Quy tắc tiêu đề (title) — công thức [Material/Spec] + [Product] + [Use case] + [Differentiator]
- VD: "Custom Printed BOPP Packing Tape 48mm x 100m Brown Carton Sealing — OEM Logo, MOQ 500"
- Tránh nhồi nhét; Alibaba phạt keyword stuffing. 2-3 keyword/title là đủ.

## 3. Listing completeness checklist (ảnh hưởng rank + conversion)
- [ ] 5+ ảnh thật (không lấy ảnh stock đối thủ), 1 ảnh white-bg chính, 1 ảnh scale/in-use, 1 ảnh chi tiết spec
- [ ] 1 video 9:16/16:9 demo (TÁI DÙNG 3 Reel BaDiVi đã render — reel_01/02/03.mp4)
- [ ] Bảng spec đầy đủ: material, size, thickness, color, adhesive type, MOQ, lead time
- [ ] FOB price range + tier MOQ (dùng quote_pricing_tiers note đã có)
- [ ] Trade Assurance bật, response time < 12h hiển thị
- [ ] Mô tả có alt-text/keyword tự nhiên trong 3 đoạn đầu

## 4. Biến traffic → RFQ inbound đo được (evidence gate)
- Mỗi listing gắn 1 mã nguồn (vd ALB-TAPE-01) → ghi vào CRM khi inquiry đến, để biết listing nào sinh RFQ.
- North-star: số RFQ qualified/tháng/listing, KHÔNG phải view/inquiry rác.
- CRM dùng lại crm_lead_log_template.csv (campaign-kit) + thêm cột `source_listing_id`, `channel=alibaba`.
- Decision rule: listing 0 RFQ qualified sau 30 ngày + có traffic → đổi keyword/ảnh; 0 traffic → keyword sai, research lại.

## 5. RFQ market (chủ động) — chiến thuật quote chances
- Alibaba cho ~giới hạn quote/tháng [CẦN VERIFY theo gói]. Đừng spray.
- Lọc RFQ: chỉ quote khi (a) đúng sản phẩm BaDiVi làm được, (b) MOQ khả thi, (c) buyer có lịch sử/profile thật.
- Quote thắng = phản hồi nhanh + giá tier rõ + đính video Reel + 1 câu Proof (giảm hư hỏng/hoàn hàng).

## 6. Anti-pattern (tránh)
- Copy title đối thủ y hệt → cạnh tranh giá thuần, thua xưởng TQ.
- Nhồi 10 keyword 1 title → tụt rank + buyer nghi spam.
- Quote mọi RFQ → tốn quota, response rate giả tạo.
- Không gắn source_id → không biết kênh nào ra tiền, mù dữ liệu.

## 7. Việc làm được ngay (không cần cookie/ngân sách)
1. Soạn 15 listing draft EN theo công thức title trên (tái dùng catalogue EN trong setup file).
2. Map mỗi listing → 1 Reel mp4 đã render làm video.
3. Thêm cột source_listing_id vào CRM template.
4. Khi Henry duyệt gói Alibaba → upload + theo dõi RFQ qualified/listing.

## Blocker / cần Henry
- [CẦN VERIFY] keyword volume thực tế trên sàn (cần tài khoản seller để xem analytics).
- Cần Henry chốt: spec/FOB/MOQ/tên pháp lý EN (đã nêu trong setup file) để draft listing không bịa.

## Liên kết note đã có (tái dùng, không trùng)
- badivi_alibaba_xnk_setup_2026.md (gói/chi phí/quy trình)
- 2026-06-02_badivi_b2b_quote_pricing_tiers_skill.md (giá tier)
- 2026-06-02_badivi_export_email_linkedin_prospecting_skill.md (outbound song song)
- campaign-kit crm_lead_log_template.csv (CRM)
