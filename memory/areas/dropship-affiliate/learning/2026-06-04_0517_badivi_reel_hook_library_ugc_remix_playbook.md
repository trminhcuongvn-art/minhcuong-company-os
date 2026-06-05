# BaDiVi — Reel Hook Library + UGC Remix Playbook (B2B, no FB cookie)

Date: 2026-06-04 05:17 +07
Agent: bun (heartbeat learning)
Context: 3 Reel BaDiVi 9:16 đã render xong (render/badivi_outputs_20260602/). Cần scale content output mà không phụ thuộc cookie FB / scrape tự động. Đây là skill content-engine để tăng reach → comment → RFQ.

---

## 1. Vì sao cần hook library
- B2B đóng gói (băng dính/màng co) là ngách "khô", người mua là chủ xưởng/quản lý kho/mua hàng — họ lướt nhanh.
- 90% retention quyết định ở 0-3 giây đầu. 1 video tốt không đủ; cần **10-15 hook xoay vòng** để A/B và tránh fatigue thuật toán.
- Mục tiêu: từ 1 concept gốc → đẻ 5-8 biến thể chỉ thay hook + caption, dùng lại body/B-roll → giảm chi phí sản xuất 70%.

## 2. Hook Library — 5 nhóm angle (B2B packaging)

### A. Pain / Loss-aversion (mạnh nhất với B2B)
1. "Mỗi cuộn băng dính rẻ 2k đang khiến xưởng bạn mất 5 triệu/tháng — đây là lý do."
2. "Hàng bị bung thùng khi giao = khách bom hàng. Lỗi nằm ở cuộn băng này."
3. "Bạn đang trả tiền cho 'không khí': băng dính mỏng phải quấn 3 vòng thay vì 1."

### B. Curiosity / Pattern-interrupt
4. "Thử kéo đứt cuộn băng dính này bằng tay xem — nếu được thì xưởng bạn đang dùng sai loại."
5. "99% xưởng đóng gói sai bước này (và không ai nói cho họ biết)."
6. "Cầm 2 cuộn băng nhìn giống hệt nhau — 1 cuộn đắt gấp đôi vì lý do này."

### C. Authority / Spec-proof
7. "Màng co bao nhiêu micron là đủ cho thùng 15kg? Con số chính xác đây."
8. "Test độ bám 3 loại băng dính ở nhiệt 35°C kho không điều hòa — kết quả bất ngờ."

### D. Offer / B2B-direct
9. "Đặt sỉ từ 1 thùng, có hóa đơn VAT, giao tận xưởng Hải Phòng/Quảng Ninh trong 24h."
10. "Gửi mẫu test miễn phí trước khi đặt — comment 'MẪU' để nhận."

### E. Comparison / Switch
11. "Đổi từ băng dính chợ sang băng công nghiệp: chi phí/thùng giảm thế nào sau 1 tháng."
12. "Tại sao xưởng X bỏ nhà cung cấp cũ sau 3 năm (và tiết kiệm 20% vật tư đóng gói)."

> Quy tắc: mỗi hook ≤ 12 từ on-screen, đọc ≤ 3.5s. Số liệu phải có cơ sở (không bịa); nếu chưa có số thật → để dạng câu hỏi/định tính, KHÔNG bịa con số cụ thể.

## 3. UGC Remix Playbook — từ 1 video → 8 biến thể
| Lớp | Thay đổi | Reuse |
|-----|----------|-------|
| V1-base | Hook A1 + body gốc | — |
| V2 | Hook B4 (đổi 3s đầu) | body + CTA |
| V3 | Hook D9 (offer-led) | body |
| V4 | Đổi caption/tone (formal → thân mật) | toàn bộ video |
| V5 | Cắt 15s "highlight" cho TikTok/Shorts | clip từ V1 |
| V6 | Thêm sticker/poll "Bạn dùng loại nào?" | V1 |
| V7 | Voiceover giọng khác (nam/nữ) | edge-tts khác voice |
| V8 | "Reply comment" format (trả lời 1 câu hỏi thật) | quay/dựng mới phần đầu, ghép body |

## 4. Caption framework (3 dòng) — tối ưu comment → RFQ
- Dòng 1 (hook lặp lại pain): "Băng dính bung thùng = mất khách."
- Dòng 2 (proof ngắn + spec): "Băng công nghiệp 45mm, keo acrylic, bám chắc kho nóng."
- Dòng 3 (CTA + leadgen trigger): "Comment 'MẪU' hoặc nhắn tin nhận báo giá sỉ + mẫu test."
- Hashtag: #dónggói #băngdính #màngco #xưởngsản xuất #B2B (3-5 cái, đủ ngách).

## 5. Cadence không cần cookie (manual-first)
- Đăng 1 Reel/ngày, xoay vòng 5 hook/tuần (mỗi tuần đổi nhóm angle để đo nhóm nào ra RFQ tốt nhất).
- Theo dõi thủ công: hook nào → nhiều comment "MẪU"/"giá" → đẩy ngân sách boost (khi có).
- Map mọi comment vào crm_lead_log_template.csv (đã có) với field hook_id để biết hook nào sinh lead chất.

## 6. Liên kết tài sản sẵn có
- 3 Reel render: /Users/minhcuong/.openclaw/workspace/render/badivi_outputs_20260602/reel01-03_badivi_9x16.mp4
- CRM template: badivi-leadgen/ (crm_lead_log_template.csv) + rfq_form_spec.md
- Caption/UTM: badivi-campaign-kit-20260603/captions_utm.csv → thêm cột hook_id để attribution.

## 7. Next actionable (rủi ro thấp, có thể tự làm khi có task)
1. Sinh 8 biến thể script .md từ 3 Reel gốc dùng remix table (chỉ cần Render dựng lại phần hook).
2. Thêm cột `hook_id` vào captions_utm.csv để A/B attribution.
3. Khi có cookie FB phụ → tự động đăng + pull comment; chưa có thì manual triage (đã có note 0302).

## Rollback
rm /Users/minhcuong/.openclaw/workspace/memory/areas/dropship-affiliate/learning/2026-06-04_0517_badivi_reel_hook_library_ugc_remix_playbook.md
