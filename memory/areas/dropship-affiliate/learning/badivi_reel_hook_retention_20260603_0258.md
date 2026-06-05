# BaDiVi — Hook 3 giây đầu & Retention cho Reel B2B đóng gói (note học tập)
- Agent: Bún | Ngày: 2026-06-03 02:58 (+07) | Task: BUN-HEARTBEAT-45P-LEARNING-20260603-0258
- Bối cảnh: 3 Reel BaDiVi 9:16 đã render (reel_01/02/03). Mục tiêu note: tăng watch-time + CTR sang RFQ mà KHÔNG cần đụng video gốc (chỉ tinh chỉnh hook text + caption + thumbnail).

## 1. Tại sao 3 giây đầu quyết định
- Reel/TikTok phân phối theo tín hiệu giữ chân sớm: % người xem qua 3s và watch-time trung bình là 2 biến mạnh nhất cho reach organic.
- B2B đóng gói (băng dính/màng co) là ngách "low-emotion" → phải dùng **pain cụ thể bằng con số/hậu quả** để chặn vuốt lướt, không dùng intro thương hiệu.

## 2. 5 mẫu hook on-screen text áp cho 3 Reel hiện có
Ghép vào 0–2s (overlay text + voice line ngắn), không cần render lại body:
1. (reel_01) "Mỗi thùng hoàn = mất 2 lần phí ship." → pain tiền bạc.
2. (reel_01) "3 lỗi đóng gói khiến hàng móp/vỡ — bạn dính mấy lỗi?" → câu hỏi mở vòng.
3. (reel_02) "Băng dính rẻ 5đ/m nhưng bung keo = mất nguyên đơn." → so sánh chi phí ẩn.
4. (reel_02) "Đừng tiết kiệm sai chỗ: vật tư đóng gói." → nghịch lý.
5. (reel_03) "Xưởng/kho cần nguồn màng co ổn định? Xem cái này." → call-out đúng tệp.

Quy tắc: hook ≤ 7 từ on-screen, font đậm, đặt vùng 1/3 trên (tránh UI nút share che chữ dưới).

## 3. Caption (mô tả) tối ưu cho RFQ funnel
- Dòng 1 = lặp lại pain (vì feed cắt ngắn còn ~1 dòng): "Hàng hoàn vì đóng gói sai — fix bằng đúng vật tư."
- Dòng 2 = CTA hành động duy nhất: bình luận / inbox "RFQ" để nhận checklist vật tư theo ngành.
- Hashtag: 3–5 cái ngách (#donggoi #bangdinh #mangco #B2B #xuongsanxuat) thay vì hashtag rộng vô nghĩa.
- 1 CTA duy nhất / video (RFQ). Nhiều CTA = giảm chuyển đổi.

## 4. Thumbnail / frame chia sẻ
- Reel B2B nên có 1 frame text lớn làm "cover" khi share sang Zalo/Group: chữ pain + logo nhỏ góc. Giúp re-share trong group ngành (kênh phân phối B2B mạnh hơn FYP).

## 5. Vòng lặp đo lường (gắn với CRM đã có)
- KPI theo dõi: 3s view rate, avg watch %, comment "RFQ", inbox, → cột trong crm_lead_log_template.csv (badivi-campaign-kit-20260603).
- A/B: cùng body, đổi hook text → so sánh 3s-retention sau 48h. Giữ hook thắng, loại hook thua. Lặp hàng tuần.
- Ngưỡng đánh giá đề xuất: 3s-view < 35% → đổi hook; comment "RFQ"/1k view < 2 → đổi CTA/caption.

## 6. Việc làm tiếp (khi có lệnh)
- Bàn giao 5 hook text trên cho Render để overlay vào 0–2s (không re-render body, chỉ chèn text layer).
- Bổ sung cột "hook_variant" + "3s_view_rate" vào captions_utm.csv để track A/B.
- Blocker thật: tracking 3s-view/comment cần truy cập trang Insights FB (cookie/nick hợp lệ) — chưa có → hiện đo thủ công.

## Nguồn/cơ sở
- Nguyên tắc phân phối short-video (early retention + watch-time) đã ổn định nhiều nền tảng; áp dụng có điều chỉnh cho ngách B2B low-emotion. Đây là playbook nội bộ, không bịa số liệu sản phẩm.
