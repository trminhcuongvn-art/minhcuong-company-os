# BaDiVi — Cold Outreach DM/Email Script cho 48 lead Top50 (ASEAN + nội địa)

Ngày: 2026-06-02 17:13 (+07)
Tác giả: Bún (heartbeat learning)
Bối cảnh: Đã có `badivi_top50_outreach_20260601.csv` (48 unique lead: ASEAN 28, nội địa 20). Mắt xích còn thiếu: kịch bản first-touch + objection handling để biến danh sách thành inquiry/RFQ thật. Note này KHÔNG bịa số liệu sản phẩm — chỗ số/giá để placeholder cần Henry confirm.

## 1. Nguyên tắc cold outreach B2B đóng gói (tape/màng PE)
- **Ngắn, cụ thể, 1 CTA duy nhất.** Email <120 từ, DM <60 từ.
- **Mở bằng relevance, không bằng giới thiệu bản thân.** Nhắc đúng ngành/sản phẩm của họ.
- **Bán "giảm rủi ro hoàn/vỡ hàng", không bán "băng dính".** Buyer mua kết quả.
- **Đính kèm proof nhẹ:** 1 Reel link (đã có 3 mp4) + 1 spec sheet PDF (cần Render/Henry).
- **Follow-up 4 chạm trong 12 ngày** mới là nơi 80% reply đến.

## 2. Phân nhánh theo segment (từ CSV)

### A. ASEAN buyer (28 lead) — kênh: Email + LinkedIn
Subject: `Tape & PE film supplier — cut your return/damage rate`

```
Hi {first_name},
Saw {company} handles {their_category} packaging. We supply BOPP carton tape
& PE stretch film direct from VN factory — consistent adhesion, no edge-lift,
MOQ from {MOQ_placeholder}, FOB {port_placeholder}.
A 30s look: {reel_link}
Open to a quick quote on your current spec? Reply and I'll send FOB pricing same day.
{your_name} — BaDiVi
```

### B. Nội địa (20 lead) — kênh: Zalo/WhatsApp/SĐT
```
Chào anh/chị {ten},
Bên em là BaDiVi, sản xuất băng dính carton & màng PE quấn pallet cho DN đóng gói.
Em thấy {company} đang dùng nhiều vật tư đóng gói — em gửi báo giá so sánh
độ bám + giá theo cuộn để anh/chị tham khảo nhé? MOQ linh hoạt, giao HP/QN/HD.
Em gửi bảng giá ngay nếu anh/chị cho em biết khổ + định lượng đang dùng.
```

## 3. Objection handling (3 phản đối hay gặp)
| Phản đối | Phản hồi |
|---|---|
| "Đang có NCC rồi" | "Hiểu ạ — em không xin thay, chỉ xin làm phương án dự phòng + báo giá đối chiếu. Nhiều DN giữ 2 nguồn để khỏi đứt hàng." |
| "Giá bao nhiêu?" | Trả lời NGAY bằng khoảng giá theo khổ (placeholder), kèm 1 câu hỏi spec để chốt báo giá chính xác. Không né giá. |
| "Gửi mẫu được không?" | "Được — em gửi mẫu {x} cuộn, anh/chị chỉ chịu phí ship. Test thực tế rồi quyết." (cần Henry confirm chính sách mẫu) |

## 4. Cadence 4 chạm / 12 ngày
- D0: First touch (script trên)
- D3: Bump ngắn "có nhận được spec không ạ" + đính proof khác
- D7: Value add — gửi 1 tip đóng gói/giảm vỡ hàng (không bán)
- D12: Break-up "em đóng hồ sơ, cần thì alo" → thường kéo 10-15% reply

## 5. Evidence gate khi triển khai thật
- File log: `badivi-leadgen/outreach_log_YYYYMMDD.csv` cột: lead_id, channel, touch_no, sent_ts, reply(y/n), stage
- KPI tối thiểu vòng 1: ≥48 first-touch gửi, reply rate ghi nhận thật, ≥3 inquiry/RFQ
- KHÔNG báo DONE nếu chưa có file log thật >1KB

## 6. Blocker cần Henry/Cáo
- Giá FOB/khổ/MOQ/định lượng thật (placeholder) — bắt buộc để điền script
- Chính sách gửi mẫu (free/ship-only)
- LinkedIn/email account để gửi ASEAN; Zalo nick để gửi nội địa
- Spec sheet PDF EN (Render hỗ trợ) đính kèm proof
