# BaDiVi Reel — Skill: Hook 3 giây & Retention Curve cho B2B

Ngày: 2026-06-02 (Bún, heartbeat learning)
Context: 3 mp4 BaDiVi (reel_01/02/03) đã render xong bằng ffmpeg motion graphics + edge-tts. Điểm yếu thật: dựng tự động → hook 3s đầu yếu, không có pattern-interrupt, retention dễ tụt. Note này là checklist để bản render sau (hoặc bản re-cut) đạt hook mạnh.

## 1. Vì sao hook 3s quyết định
- Trên Facebook/TikTok Reels, >65% lượt xem rớt trong 3 giây đầu nếu không có lý do ở lại.
- B2B (mua băng dính/màng PE/vật tư đóng gói) khán giả ít cảm xúc hơn B2C → hook phải đánh vào **tiền mất / hàng hỏng / bị khách phàn nàn**, không phải "sản phẩm chất lượng".
- Thuật toán đo: 3s view rate, avg watch time, completion rate, re-watch. Hook tốt kéo cả 4.

## 2. 6 dạng hook hiệu quả cho BaDiVi (chọn 1/Reel)
1. **Loss hook**: "Mỗi cuộn băng dính rẻ 2k bạn tiết kiệm có thể làm hoàn cả lô hàng." (số phải có thật, nếu chưa verify thì để dạng câu hỏi).
2. **Visual fail hook**: Cận cảnh thùng carton bung mép / màng co rách / hàng đổ — 0.5s đầu là hình ảnh hỏng, chưa cần lời.
3. **Câu hỏi nhức nhối**: "Hàng đến tay khách bị móp, ai chịu trách nhiệm?"
4. **Phản trực giác**: "Băng dính dày hơn chưa chắc dính chắc hơn — đây là lý do."
5. **So sánh A/B**: split screen cuộn rẻ vs cuộn đạt chuẩn, kéo thử bung mép.
6. **Số/khối lượng**: "1 xưởng đóng 500 đơn/ngày — sai 1 loại keo là mất X giờ."

## 3. Retention curve — giữ người xem từng mốc
- **0–3s**: hook (1 trong 6 trên), KHÔNG để logo/intro slide đầu tiên.
- **3–8s**: nêu vấn đề cụ thể bằng hình thật (B-roll fail), voice nhanh, caption to.
- **8–20s**: proof/giải pháp — sản phẩm BaDiVi giải quyết đúng pain đó, demo kéo/dán/bọc.
- **20–35s**: offer + lý do mua từ nhà sản xuất (giá xưởng, MOQ, in logo theo yêu cầu).
- **2–3s cuối**: CTA cụ thể đo được (Zalo/inbox + mã ưu đãi để track), 1 dòng caption pin.

## 4. Lỗi của bản render auto cần sửa ở vòng sau
- Mở đầu bằng motion graphics chung chung, không có pattern-interrupt → thay bằng B-roll fail thật (cần footage thật: thùng bung, màng rách).
- Caption tĩnh → nên dùng caption động (word-by-word/karaoke) để giữ mắt.
- Thiếu zoom/cut nhịp 1.5–2.5s/scene → bộ não rớt chú ý ở scene tĩnh dài.
- Voice edge-tts đều đều → cần nhấn nhịp ở câu hook và CTA (có thể chèn pause + emphasis trong script).

## 5. Checklist nghiệm thu hook (gate trước khi đăng)
- [ ] 3s đầu có pattern-interrupt (hình/âm/câu hỏi)?
- [ ] Có caption to ngay frame 1?
- [ ] Không có logo/intro chiếm 3s đầu?
- [ ] Mỗi scene ≤ 2.5s, có cut/zoom?
- [ ] CTA cuối có mã/đường dẫn đo được (UTM/Zalo tag)?
- [ ] Claim số liệu sản phẩm: có thật hoặc chuyển thành câu hỏi (không bịa).

## 6. Việc cần input thật (blocker tiềm ẩn)
- Cần **footage thật**: thùng carton bung mép, màng co rách, dây chuyền đóng gói BaDiVi → để thay motion graphics generic. Hiện chưa có asset → render auto bị generic.
- Cần xác nhận **số liệu/claim** (độ dày keo, lực kéo, MOQ, giá xưởng) để hook dạng số không bịa.

## Next action khả thi
- Bổ sung field "hook_variant" vào 3 script reel hiện có, viết 3 phương án hook cho mỗi reel để A/B test khi có footage.
- Khi Henry/Cáo cấp footage thật → re-cut 3 reel theo retention curve ở mục 3.
