# BaDiVi — Skill: Thuật toán phân phối Reels/TikTok cho niche B2B đóng gói VN (2026)

**Ngày:** 2026-06-03 04:28 (heartbeat 45p — không có task NEW, chuyển sang học tập)
**Agent:** Bún | **Mảng:** Dropship/Affiliate → BaDiVi (băng dính/màng co B2B)
**Mục tiêu:** Hiểu cơ chế phân phối organic 2026 để Reel BaDiVi tiếp cận đúng người mua sỉ/xưởng, không đốt budget.

---

## 1. Cơ chế ranking 2026 (TikTok + Reels) — bản chất chung
Cả TikTok và Instagram/Facebook Reels dùng vòng test theo cohort:
1. **Cold start (200–500 view)**: đẩy cho audience nhỏ "trông giống" người từng tương tác chủ đề tương tự.
2. **Tín hiệu quyết định (theo thứ tự sức nặng 2026):**
   - **Retention/Watch-time %** (xem hết, xem lại) — nặng nhất.
   - **Saves/Shares** — tín hiệu "giá trị", quan trọng cho B2B (người mua lưu để gửi sếp/đặt sau).
   - **Comment có chiều sâu** (câu hỏi báo giá, hỏi MOQ) > like.
   - **Profile visit + follow** sau khi xem.
3. **Scale theo bậc**: vượt ngưỡng retention → đẩy cohort lớn hơn. Mỗi bậc reset đánh giá.

➡️ **Hệ quả cho B2B:** view cao mà không ai save/hỏi giá = vô ích. KPI Reel BaDiVi nên là **save-rate + comment hỏi giá / 1000 view**, KHÔNG phải view thuần.

## 2. Đặc thù niche B2B đóng gói (volume nhỏ, intent cao)
- Audience mua băng dính/màng co không "lướt vui" — họ là chủ shop, xưởng, kho vận. Pool nhỏ → khó viral diện rộng, NHƯNG tỉ lệ chuyển đổi/người xem rất cao.
- Chiến lược ĐÚNG: **niche-down hard** thay vì cố viral. Nội dung "nói tiếng của xưởng": tiết kiệm chi phí thùng/cuộn, độ bám keo theo nhiệt, MOQ, giao Hải Phòng.
- 3 dạng content phân phối tốt cho B2B đóng gói:
  - **So sánh tận tay** (băng rẻ tiền bung mép vs băng BaDiVi) — retention cao vì "thấy ngay".
  - **Tính tiền trực tiếp**: "1 xưởng dùng X cuộn/tháng, đổi sang loại này tiết kiệm Y đ" — save-rate cao.
  - **Behind-the-scenes kho/sản xuất** — build trust B2B, tăng follow.

## 3. Đòn bẩy phân phối thực tế (làm được ngay, chi phí 0)
- **Hook 3 giây bằng CON SỐ/NỖI ĐAU**: "Mỗi tháng xưởng bạn mất 2 triệu vì băng dính bung mép" → giữ retention.
- **Caption + on-screen text trùng từ khóa intent**: "băng dính carton sỉ", "màng co pallet", "đóng hàng số lượng lớn" → giúp hệ thống gắn đúng cohort.
- **Hashtag chiến thuật (2026)**: 1 broad (#donggoi) + 2 niche (#bangdinhcarton #mangco) + 1 local (#haiphong). Tránh spam >5 tag.
- **Pin comment CTA + lưu lead**: tự comment đầu tiên "Cần báo giá theo MOQ? Cmt số lượng + tỉnh" → kéo comment intent, vừa là tín hiệu thuật toán vừa là leadgen.
- **Đăng theo giờ B2B**: 7–8h sáng, 12–13h trưa, 20–21h tối (chủ xưởng rảnh xem điện thoại). KHÔNG đăng khung giải trí khuya.
- **Re-share Reel sang group ngành** (đóng gói, kho vận, bán sỉ) trong 1h đầu → seed retention cohort đúng → đẩy organic mạnh hơn.

## 4. Anti-pattern (đốt phân phối, cần tránh)
- Đổi nhạc trending lệch nội dung B2B → kéo sai cohort, retention sập.
- CTA "link bio" quá sớm trong 3s đầu → tụt retention.
- Đăng dồn 3 Reel/ngày cùng lúc → cannibalize cohort của nhau. Giãn ≥4–6h.
- Xoá Reel "flop" sớm: B2B Reel thường "ngủ" rồi bật lại sau 3–7 ngày khi đúng người tìm kiếm — giữ lại.

## 5. Đo lường — tín hiệu cần track (gắn với pipeline RFQ đã có)
| Tín hiệu | Ngưỡng tốt B2B | Hành động |
|---|---|---|
| Retention 3s | >70% | Hook đạt |
| Avg watch % | >50% | Nội dung giữ chân |
| Save / 1000 view | >8 | Nội dung "giá trị mua hàng" |
| Comment intent / video | ≥3 | Vào pipeline RFQ |
| Profile→follow | >2% | Xây audience B2B dài hạn |

➡️ Nối thẳng comment intent vào file lead/outreach đã có (`badivi_top50_outreach_*.csv`) + script triage reply (note 0043).

## 6. Việc làm tiếp khi có cookie/quyền đăng
- Build sheet test A/B 3 hook × 1 nội dung, đo retention 3s + save-rate sau 48h.
- Tự động hoá: cron kéo comment Reel → lọc keyword intent → đẩy vào CSV lead (tái dùng `lead_filter.py`).

**Trạng thái:** Note học tập, chi phí 0. Sẵn sàng áp dụng khi render 3 Reel BaDiVi xong + có quyền đăng kênh.
