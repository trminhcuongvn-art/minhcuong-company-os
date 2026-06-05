# BaDiVi Reels — A/B Test + Posting Cadence + KPI Benchmark Playbook
Ngày: 2026-06-03 13:29 (+07) | Agent: Bún | Loại: Heartbeat learning (no NEW task)
Bối cảnh: 3 reel BaDiVi 9:16 đã render (reel_01/02/03 tại render/badivi-reels/) + campaign kit đã có. Các note trước đã phủ hook/retention/distribution/leadgen funnel. Note này lấp khoảng trống: **đo lường & ra quyết định** — biến content thành 1 vòng test có thể chạy ngay khi có FB/TikTok page.

## 1. Vấn đề: thiếu vòng đo lường → đốt content mù
Hiện trạng: có 3 reel + caption/UTM, nhưng CHƯA định nghĩa:
- Biến cần test (hook nào, CTA nào, thời điểm đăng).
- Ngưỡng quyết định (giữ/cắt/scale variant nào).
- KPI gate B2B (lead-quality, không phải vanity views).
Nếu đăng cả 3 cùng lúc không tag UTM/không log → không biết reel nào ra lead.

## 2. Khung biến A/B (mỗi lần test chỉ đổi 1 biến)
| Layer | Variant A | Variant B | Cách đo |
|---|---|---|---|
| Hook 3s đầu | Pain ("3 lỗi đóng gói khiến hàng vỡ") | Loss/tiền ("Chọn sai băng dính = mất tiền") | View 3s retention %, hold tới 50% |
| CTA | "Nhắn 'BAOGIA' để nhận báo giá" (comment-to-DM) | "Link RFQ form ở bio" (click-out) | comment/DM rate vs link CTR |
| Thời điểm đăng | 7:30-8:30 (giờ mở xưởng/văn phòng) | 12:00-13:00 / 20:00-21:00 | reach giờ vàng theo audience B2B |
| On-screen text | Số liệu cụ thể ("tiết kiệm 12%/cuộn") | Câu hỏi ("Xưởng bạn đang mất bao nhiêu?") | save + share rate |

Quy tắc: 1 biến / 1 tuần. Giữ visual/voice/độ dài cố định để cô lập biến.

## 3. Posting cadence đề xuất (B2B niche, dung lượng audience nhỏ → ưu tiên chất lượng lead)
- Tần suất: 3-4 reel/tuần/platform (FB Reels + TikTok). Không spam; B2B mua theo nhu cầu, cần tái tiếp xúc đều.
- Lịch mẫu: T2/T4/T6 đăng 1 reel mới; T7 đăng lại bản remix (đổi hook) reel thắng tuần trước.
- Mỗi reel sống 7 ngày trước khi đánh giá; reel "winner" (qua gate §4) → bơm thành ad/retarget.
- Cross-post: cùng nội dung sang LinkedIn (decision-maker B2B) + Zalo OA story.

## 4. KPI gate B2B — ngưỡng ra quyết định
Thay vì view, đo theo phễu lead. Đặt ngưỡng tương đối (so chính mình tuần trước), điều chỉnh sau 2 chu kỳ data thật:
1. **3s retention ≥ 35%** → hook đạt; <25% → thay hook.
2. **Avg watch ≥ 40% độ dài** → nội dung giữ chân; nếu rớt mạnh ở scene nào → cắt scene đó.
3. **Lead signal = comment chứa keyword + DM "BAOGIA" + click UTM form**. Gate: ≥ 1 lead-signal / 1.000 reach (0.1%) cho B2B packaging là mốc khởi điểm thực tế để test, KHÔNG phải benchmark đã kiểm chứng — cần đo lại bằng data thật rồi cập nhật.
4. **Cost-per-qualified-lead** (khi chạy ad): set trần theo giá trị đơn RFQ trung bình; reel nào vượt trần → tắt.

Decision rule: CẮT nếu thua gate §4.1+§4.3 hai chu kỳ liên tiếp; SCALE (bơm ad) nếu thắng cả 4. KEEP-TEST nếu pha trộn → đổi đúng 1 biến.

## 5. Tracking tối thiểu (không cần tool trả phí)
- Mỗi reel 1 dòng UTM riêng trong `captions_utm.csv` (đã có sẵn cột) → link RFQ form gắn `?utm_source=fb&utm_medium=reel&utm_campaign=badivi_<reel_id>`.
- Log thủ công vào `crm_lead_log_template.csv`: cột `source_reel_id`, `keyword`, `channel(comment/DM/form)`, `date`, `qualified(y/n)`.
- Cuối tuần: pivot theo `source_reel_id` → ra winner/loser. Đây là input để chốt §4.

## 6. Việc làm được NGAY (không cần cookie FB)
- [x] Chuẩn hoá UTM per-reel trong captions_utm.csv (đã tồn tại, kiểm tra cột campaign khác nhau).
- [ ] Thêm cột `source_reel_id` + `qualified` vào crm_lead_log_template nếu thiếu (rủi ro thấp → tự làm chu kỳ sau).
- [ ] Soạn 2 hook variant cho reel_01 (Pain vs Loss) để sẵn khi có page.
BLOCKER thật để CHẠY (không phải để chuẩn bị): chưa có FB/TikTok page + quyền đăng → mọi số §4 là giả định cho tới khi có reach thật.

## 7. Bài học cốt lõi
- B2B packaging: tối ưu **lead-per-reach** chứ không tối ưu view. 1.000 view rác < 5 DM xưởng đóng gói thật.
- Luôn cô lập 1 biến; không đổi 3 thứ rồi đoán cái nào hiệu quả.
- Mọi benchmark ở đây là MỐC KHỞI ĐIỂM để test, phải thay bằng data thật sau 2 chu kỳ — không tự nhận là chuẩn ngành.

Nguồn tham khảo (khung, untrusted, không trích số): chiến lược short-form B2B 2026 (videoeditingcompany, collabonly, sophieflow, unhooked). Số liệu trong note do Bún tự đặt làm giả định test, KHÔNG bịa claim sản phẩm.
