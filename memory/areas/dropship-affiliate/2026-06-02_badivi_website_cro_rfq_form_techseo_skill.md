# BaDiVi — Website CRO + RFQ Form Spec + Technical SEO (skill note)
Date: 2026-06-02 (heartbeat learning, Bún)
Site thật: bangdinhviethan.com — nhà SX/phân phối băng dính, màng PE, vật tư đóng gói (Hải Phòng).
Bối cảnh: Reel/Alibaba/outbound đổ traffic về web; phải biến click → RFQ/Zalo có thể đo. Audit trước phát hiện placeholder info@example.com + số +1 trên footer/theme → mất trust nặng. File này là checklist kỹ thuật để fix và tăng conversion, KHÔNG bịa số.

## 1. Trust fix BẮT BUỘC (làm trước mọi thứ — nếu không, mọi traffic lãng phí)
- [ ] Xoá toàn bộ placeholder theme: info@example.com, +1 (xxx), "Lorem ipsum", địa chỉ demo.
- [ ] Thay bằng NAP thật nhất quán mọi nơi (header, footer, contact, schema):
  - Tên pháp lý: Công ty TNHH Băng Dính Việt Hàn
  - Phone/Zalo: 0941463869
  - Email: congtytnhhbangdinhviethan@gmail.com (nên nâng cấp email domain @bangdinhviethan.com để pro hơn)
  - Địa chỉ: Kiều Đông, An Dương, Hải Phòng
- [ ] Thêm: MST, năm thành lập, ảnh nhà máy/kho thật, ảnh đội ngũ → giảm rủi ro cảm nhận khi mua B2B.

## 2. Hệ phân cấp CTA (mỗi trang chỉ 1 hành động chính)
Thứ tự ưu tiên kênh liên hệ B2B VN: **Zalo > Gọi > Form RFQ > Email**.
- Sticky bar mobile: nút Zalo + nút Gọi (tel:) luôn hiện đáy màn hình.
- Nút phụ "Nhận báo giá theo quy cách" → mở form RFQ (xem mục 3).
- Tránh CTA chung chung "Liên hệ". Dùng động từ + lợi ích: "Nhận báo giá + mẫu test trong 24h".
- Đặt CTA: above-the-fold, sau bảng quy cách, cuối mỗi landing SKU.

## 3. RFQ form spec (form ngắn = nhiều lead; nhưng B2B cần đủ data để báo giá)
Cân bằng: 6–7 field, chỉ 3 field bắt buộc. Field thừa giết conversion.
- BẮT BUỘC: (1) Số điện thoại/Zalo, (2) Loại sản phẩm (select: băng dính OPP / in logo / màng PE / 2 mặt / khác), (3) Số lượng dự kiến (range: <100 / 100–500 / 500–2000 / >2000 cuộn|kg).
- TUỲ CHỌN: tên DN, ngành (logistics/SX/in/thực phẩm...), quy cách (khổ x dài x dày), thời điểm cần.
- Anti-spam: honeypot field ẩn (không dùng captcha nặng giết mobile conversion).
- Sau submit: redirect /cam-on/ (trang thank-you riêng để track conversion) + auto mở Zalo.
- Lưu lead → CSV/Google Sheet/CRM. Evidence gate: mỗi lead phải có ít nhất phone + product + qty.
- KHÔNG để form gửi về info@example.com. Test gửi thật 1 lần trước khi go-live.

## 4. Trang landing SKU theo nhu cầu (SEO + conversion)
Mỗi nhóm SP 1 landing tối ưu intent mua:
1. Băng dính carton OPP (đóng thùng) — keyword "băng dính carton giá sỉ", "băng dính đóng thùng"
2. Băng dính in logo theo yêu cầu — "in băng dính theo yêu cầu", "băng dính in logo công ty"
3. Màng PE quấn pallet — "màng PE quấn pallet", "màng chít quấn hàng"
4. Băng dính 2 mặt / giấy / vải / chịu nhiệt / chống tĩnh điện — gom cluster.
Cấu trúc mỗi landing: H1 rõ intent → 3 bullet lợi ích → bảng quy cách/MOQ/đơn vị tính → ảnh thật → social proof → form RFQ + Zalo. Có FAQ (MOQ tối thiểu? in logo bao lâu? giao Hải Phòng/toàn quốc?).

## 5. Technical SEO checklist (để Reel/organic kéo traffic bền)
- [ ] Title/meta description từng landing có keyword + địa danh (Hải Phòng/toàn quốc).
- [ ] Schema.org: Organization (NAP đúng) + Product + LocalBusiness + FAQPage.
- [ ] Google Business Profile: tạo/claim, ảnh nhà máy, đúng NAP → bắt local "băng dính Hải Phòng".
- [ ] Sitemap.xml + robots.txt + submit Google Search Console.
- [ ] Tốc độ: nén ảnh WebP, lazy-load, mobile-first (đa số B2B VN tra cứu qua điện thoại).
- [ ] HTTPS + canonical tránh trùng nội dung listing.
- [ ] Alt text ảnh sản phẩm có keyword.

## 6. Đo lường (không có tracking = không học được gì)
- GA4 + GTM: event `rfq_submit`, `zalo_click`, `call_click`, `view_quote_table`.
- UTM cho mọi nguồn: Reel FB (utm_source=fb&utm_medium=reel&utm_campaign=...), Alibaba, email outbound, LinkedIn.
- Trang /cam-on/ = conversion goal đếm RFQ.
- KPI tuần: sessions, RFQ submit, Zalo click, tỉ lệ RFQ/visit, lead hợp lệ (đủ phone+product+qty), chi phí/lead.
- Evidence gate báo cáo: chỉ tính lead có dòng CSV thật (phone+product+qty), không tính "view".

## 7. Thứ tự triển khai (ROI cao → thấp)
1. Fix trust placeholder + NAP thật + sticky Zalo/Gọi (1 ngày, impact cực cao).
2. RFQ form 3 field bắt buộc + thank-you page + lưu lead.
3. GA4/GTM + UTM (đo được mới tối ưu được).
4. 3–4 landing SKU chính + schema + GBP.
5. Mở rộng FAQ, social proof, ảnh nhà máy, blog kéo organic.

## Liên kết artifact đã có
- Audit web: bun/plan/badivi_website_audit_bangdinhviethan_2026.md
- Master plan 3 kênh: bun/plan/badivi_master_plan_2026.md
- Reel landing offer: memory/areas/dropship-affiliate/2026-06-02_badivi_reels_b2b_landing_offer_learning.md
- Lead top50: bun/badivi-leadgen/badivi_top50_outreach_20260601.csv (48 rows, 27369 bytes)
