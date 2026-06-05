# BaDiVi Reel — Hook 3 giây đầu & framework A/B test (Heartbeat learning 2026-06-02 22:28)

> Bối cảnh: 3 Reel BaDiVi đã script + render xong (verified mp4). Bước nâng cấp tiếp theo để tăng lead B2B: tối ưu **3 giây đầu** (hook) vì đây là yếu tố quyết định retention → reach → lead. Note này là thư viện hook + cách A/B test có đo lường, không bịa số liệu sản phẩm.

## 1. Vì sao 3 giây đầu quyết định
- Thuật toán Reel/TikTok đẩy reach dựa trên **3s retention + average watch time + share/save**. Hook yếu = video chết ở 1s, dù nội dung sau hay.
- B2B đóng gói: người xem lướt rất nhanh, hook phải chạm **nỗi đau tiền bạc / rủi ro vận hành** trong 3s, không "chào hỏi", không intro logo.
- Quy tắc vàng: **hook phải nói được "cái này liên quan tới TÔI và túi tiền của tôi"** ngay câu đầu.

## 2. Thư viện 10 hook mẫu cho BaDiVi (B2B đóng gói)
Phân theo nhóm tâm lý, dùng làm biến thể A/B:

**Nhóm A — Tổn thất tiền (Loss)**
1. "Mỗi tháng bạn mất bao nhiêu tiền vì hàng bị bung thùng khi vận chuyển?"
2. "Một cuộn băng dính rẻ 2.000đ có thể khiến bạn đền cả lô hàng."

**Nhóm B — Sai lầm/Cảnh báo (Mistake)**
3. "3 lỗi đóng gói khiến đơn B2B của bạn bị hoàn — số 2 ai cũng mắc."
4. "Đừng mua màng co theo giá rẻ nhất — đây là lý do."

**Nhóm C — Tò mò/Phản trực giác (Curiosity)**
5. "Băng dính đắt hơn lại giúp bạn tiết kiệm hơn — thật không?"
6. "Tại sao kho lớn không bao giờ mua màng co ngoài chợ?"

**Nhóm D — So sánh trực quan (Visual demo)**
7. [Cảnh kéo bung thùng] "Cái nào giữ được? Xem đến cuối."
8. "Cùng 1 thùng, 2 loại băng — kết quả khác nhau hoàn toàn."

**Nhóm E — Định danh đối tượng (Call-out)**
9. "Nếu bạn ship 100+ đơn/ngày, video này dành cho bạn."
10. "Chủ kho, chủ shop đóng gói số lượng lớn — nghe 15 giây này."

## 3. Khung A/B test có đo lường (không cần budget ads)
**Đơn vị test = HOOK, giữ nguyên phần thân + CTA.**

| Bước | Hành động | Metric ghi nhận |
|------|-----------|-----------------|
| 1 | Cắt 3 biến thể hook (vd A1, C5, D7) ghép vào cùng 1 thân video | 3 file mp4 |
| 2 | Đăng lệch giờ (cùng khung giờ vàng các ngày khác nhau, hoặc 3 nền tảng) | thời điểm đăng |
| 3 | Sau 48h thu số: views, **3s view %**, avg watch time, share, save, comment, click link bio | bảng CSV |
| 4 | Chọn hook có **3s retention cao nhất + share cao nhất** làm winner | hook winner |
| 5 | Nhân winner ra 3 chủ đề tiếp theo | scale |

**Metric ưu tiên cho B2B (không chỉ views):**
- 3s view % (≥ 50% là tốt cho B2B niche)
- Save rate (B2B hay lưu lại để tham khảo mua sau) — chỉ báo intent mạnh
- Click link bio / DM "báo giá" — chỉ báo lead thật
- Comment có keyword intent (giá, sỉ, mua, liên hệ) → đẩy sang SOP lead đã viết trước

## 4. Mẫu bảng theo dõi (CSV gợi ý)
```
reel_id,hook_variant,platform,posted_at,views,view3s_pct,avg_watch_s,shares,saves,bio_clicks,intent_comments,leads
R01,A1_loss,fb_reels,2026-06-03 20:00,,,,,,,,
R01,C5_curiosity,tiktok,2026-06-04 20:00,,,,,,,,
R01,D7_visualdemo,fb_reels,2026-06-05 20:00,,,,,,,,
```
→ Khi có data thật, đổ vào file CSV trong badivi-leadgen để nối tiếp phễu lead đã thiết kế.

## 5. Nguyên tắc viết hook (checklist trước khi render)
- [ ] Câu đầu < 8 từ, đọc được trong ≤ 2.5s
- [ ] Có con số hoặc "mất tiền/rủi ro" hoặc câu hỏi
- [ ] On-screen text trùng khớp voice câu đầu (xem không cần tiếng)
- [ ] Không có intro logo/chào hỏi ở giây 0-3
- [ ] Visual đầu tiên là cảnh "động" (kéo bung thùng, hàng đổ) — không phải cảnh tĩnh

## 6. Việc tiếp theo (khi unblock)
- Blocker giữ nguyên: FB comment/lead scrape cần cookie/nick phụ hợp lệ để lấy data thật → chưa có số liệu retention thực tế.
- Khi Henry duyệt đăng 3 Reel: áp dụng A/B hook ngay vòng đầu, thu 48h, chọn winner, ghi RESULT kèm CSV.
- Có thể chuẩn bị sẵn 3 biến thể hook đã cắt cho Render dựng nếu được giao.

---
Tác giả: Bún | Loại: Heartbeat learning (không có task NEW) | Liên kết: nối tiếp các note distribution / landing / quote sheet / publish checklist / persona / competitor trước đó.
