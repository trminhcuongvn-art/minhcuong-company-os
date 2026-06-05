# BaDiVi — Học/nâng skill: Biến RFQ thành đơn bằng "quote psychology" B2B
Ngày: 2026-06-03 08:58 (+07) · Agent: Bún · Loại: learning note (không có task NEW trong bus)
Phạm vi: băng dính / màng PE / màng co đóng gói B2B (BaDiVi). Xentric ON HOLD — bỏ qua.

## 1. Vấn đề thực tế cần giải
Pipeline hiện tại đã có tới bước RFQ (3 Reel → comment/DM → phiếu báo giá). Nút thắt kế tiếp KHÔNG phải "có thêm lead" mà là **tỉ lệ RFQ → đơn (close rate)**. B2B vật tư đóng gói khách hỏi giá nhiều nơi, dễ rớt ở khâu báo giá nếu chỉ gửi 1 con số trần trụi.

## 2. 5 đòn bẩy báo giá làm tăng close rate (áp dụng được ngay, không cần tool)

### a) Báo giá 3 bậc (Good–Better–Best) thay vì 1 giá
- Bậc 1 (Tiết kiệm): đúng nhu cầu cơ bản, giá thấp → giữ khách nhạy giá.
- Bậc 2 (Khuyến nghị – in đậm): cân bằng giá/chất lượng → "mỏ neo" để khách chọn giữa.
- Bậc 3 (Cao cấp): màng dày hơn / keo chịu lực hơn / in logo → nâng trần giá, làm bậc 2 trông hợp lý.
- Hiệu ứng: decoy + anchoring → đa số chọn bậc giữa, AOV cao hơn báo 1 giá.

### b) Quy giá về **đơn vị sử dụng**, không chỉ đơn giá cuộn
- Thay vì "X đ/cuộn", thêm "≈ Y đ/thùng hàng" hoặc "≈ Z đ/100 kiện".
- B2B mua theo chi phí/đơn vị output → con số nhỏ trên mỗi kiện làm quyết định dễ hơn và lộ rõ khi đối thủ rẻ hơn/cuộn nhưng đắt hơn/kiện (mỏng, dính kém, phải quấn nhiều vòng).

### c) Khung MOQ + bậc số lượng (volume break) hiển thị sẵn
- Bảng: 1–10 thùng / 11–50 / 51+ với giá giảm dần.
- Tác dụng kép: (1) tạo lý do mua nhiều hơn để "lên bậc", (2) chốt MOQ ngay, giảm hỏi tới hỏi lui.

### d) Hidden-cost reframing trong báo giá (không chỉ bán giá)
- Mỗi báo giá kèm 1 dòng "chi phí ẩn nếu chọn loại mỏng/keo kém": hàng bung, hoàn đơn, mất uy tín, nhân công quấn lại.
- Định lượng thô: ví dụ 1% đơn bị bung × giá trị đơn >> phần tiết kiệm vài đồng/cuộn. Đưa khách từ tư duy "giá rẻ" sang "tổng chi phí".

### e) Mỏ neo thời gian + khan hiếm thật
- "Giá giữ trong 7 ngày", "lô tồn theo size X còn N cuộn", "đặt trước ngày … kịp giao trước cao điểm".
- Chỉ dùng khan hiếm THẬT (tồn kho/lịch giao) — không bịa, tránh mất uy tín B2B.

## 3. Cấu trúc 1 tin báo giá chốt nhanh (template chữ)
1. Xác nhận nhu cầu (size, tải trọng, sản lượng/ngày) — chứng tỏ đã nghe.
2. Đề xuất bậc Khuyến nghị trước + lý do hợp với họ.
3. Bảng 3 bậc + giá theo đơn vị sử dụng + volume break.
4. 1 dòng hidden-cost reframing.
5. CTA 1 hành động: "Chốt size + số lượng, em gửi mẫu/giao thử trong … ngày."

## 4. Trường dữ liệu cần thêm vào CRM để đo close
Bổ sung vào crm_lead_log_template.csv (đã có ở campaign kit):
- quote_tier_sent (1/2/3) · quote_unit_price · quote_per_box_price
- moq_offered · volume_break_applied (Y/N)
- objection_main (giá / giao hàng / chất lượng / đang dùng NCC khác)
- outcome (won / lost / negotiating) · lost_reason · order_value

KPI bổ sung north-star: **RFQ→Won %** và **AOV theo quote_tier**. Vanity (view/like) chỉ phụ.

## 5. Blocker giữ nguyên (không chặn việc này)
- FB comment/lead scrape tự động vẫn cần cookie/nick phụ hợp lệ → vẫn nhập RFQ/outcome thủ công vào CRM CSV được, không chặn skill báo giá này.

## 6. Next khi có task thật
- Sinh file `badivi_quote_template_3tier.md` + cập nhật cột mới vào crm_lead_log_template.csv khi Trợ Lý/Henry duyệt launch và có RFQ thật để điền.
