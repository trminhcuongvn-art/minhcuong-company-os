# Skill: BaDiVi B2B — Chiến lược báo giá theo bậc số lượng (Quote/Pricing Tiers) để tăng tỷ lệ chốt RFQ

Ngày: 2026-06-02 (heartbeat learning — Bún)
Mảng: BaDiVi (băng dính / màng co / vật tư đóng gói B2B)
Mục tiêu skill: Tăng win-rate từ RFQ → đơn hàng bằng cấu trúc báo giá thông minh, giảm vòng "mặc cả" và tăng giá trị đơn (AOV).

## 1. Vấn đề thực tế khi báo giá B2B vật tư đóng gói
- Khách B2B (xưởng, kho, shop bán online số lượng lớn) so giá rất nhanh — báo 1 giá lẻ là dễ bị ép.
- Báo "giá tốt nhất" ngay vòng 1 → mất biên + khách vẫn mặc cả tiếp.
- Không có mốc số lượng → khách không có lý do để mua nhiều hơn.
- Báo giá chậm (quá 1 ngày) → mất đơn vào tay đối thủ (đã ghi ở note SLA follow-up).

## 2. Khung báo giá 3 bậc (Good–Better–Best) cho vật tư đóng gói
Luôn báo 3 mốc thay vì 1 giá. Tâm lý khách neo vào mốc giữa.

| Bậc | Số lượng (ví dụ băng dính) | Vị trí định giá | Mục tiêu tâm lý |
|-----|---------------------------|-----------------|-----------------|
| Lẻ / dùng thử | 1–10 cuộn / 1 thùng | Giá niêm yết (cao nhất/đv) | Neo giá, làm bậc trên rẻ hơn |
| **Phổ biến (khuyên dùng)** | 1 thùng → vài thùng | Giảm 8–15%/đv | Mốc "ngon" — đa số chốt ở đây |
| Sỉ / hợp đồng tháng | ≥ X thùng hoặc cam kết tháng | Giảm 15–25%/đv | Khóa khách dài hạn, tăng LTV |

Nguyên tắc: chênh lệch giữa các bậc phải đủ rõ (≥7–8%/đv) để tạo động lực nâng số lượng, nhưng vẫn bảo vệ biên ở bậc 1.

## 3. Quy tắc định giá (không bịa số sản phẩm thật — đây là khung công thức)
- Giá sàn = giá vốn × (1 + biên tối thiểu). KHÔNG báo dưới sàn dù khách ép.
- Mỗi bậc tăng số lượng → giảm % theo đường cong giảm dần (không tuyến tính): 0% → 10% → 18% → 23% (trần).
- Phí ship: gộp vào giá ở bậc sỉ ("freeship đơn ≥ X") thay vì giảm giá đơn vị — bảo vệ giá niêm yết.
- Cọc/thanh toán: bậc sỉ/hợp đồng có thể yêu cầu cọc 30–50% → lọc khách nghiêm túc.

## 4. Cấu trúc 1 báo giá chuẩn (template để bàn giao)
1. Lời chào + xác nhận đúng nhu cầu (1 dòng): "Anh/chị cần băng dính trong khổ 48mm, dùng đóng thùng — em báo giá theo số lượng dưới đây."
2. Bảng 3 bậc rõ ràng (số lượng – đơn giá – thành tiền – tiết kiệm).
3. Highlight bậc "khuyên dùng" (in đậm / icon ⭐).
4. Điều khoản: thời gian giao, phí ship, chính sách đổi lỗi, MOQ.
5. CTA + deadline mềm: "Báo giá giữ trong 5 ngày. Anh/chị chốt số lượng nào để em lên đơn ngay ạ?"
6. 1 social proof ngắn (đã cung cấp cho xưởng/kho tương tự) — KHÔNG bịa tên khách.

## 5. Xử lý mặc cả (đối ứng — nối với note objection handling)
- "Bên kia rẻ hơn" → hỏi rõ cùng quy cách/định lượng/độ dày không (vật tư đóng gói khác định lượng = khác giá). Đổi trục so sánh sang chất lượng + tỷ lệ lỗi.
- "Giảm thêm đi" → đổi lấy điều kiện: tăng số lượng / thanh toán nhanh / cam kết tháng → "Nếu anh lấy lên mốc X em hỗ trợ được mức Y."
- Không bao giờ giảm giá "miễn phí" — mọi nhượng bộ đổi lấy thứ gì đó (số lượng, cọc, đơn lặp lại).

## 6. Liên kết pipeline BaDiVi (mắt xích còn thiếu đã bù)
Reel hook/retention → leadgen/scoring → DM/follow-up SLA → **[note này] báo giá tiers** → chốt → đơn lặp lại.
Báo giá là điểm rơi đơn nhiều nhất → cần chuẩn hóa template + bảng tính tự động (Google Sheet: nhập số lượng → tự ra 3 bậc).

## 7. Việc nên làm tiếp (đề xuất cho lần sau)
1. Dựng 1 Google Sheet "Quote Builder" 3 bậc: input giá vốn + biên → tự sinh bảng báo giá copy-paste.
2. Mẫu báo giá PDF có brand BaDiVi để gửi Zalo/email (tăng chuyên nghiệp).
3. A/B: báo 1 giá vs báo 3 bậc → đo win-rate & AOV thực tế khi có data đơn.

## Đánh giá self
- Đây là khung công thức/chiến lược, KHÔNG bịa số liệu sản phẩm cụ thể.
- Bù đúng mắt xích còn thiếu trong pipeline (trước đó chưa có note về pricing/quote tiers).
- Sẵn sàng chuyển thành tool Quote Builder khi có giá vốn thật.
