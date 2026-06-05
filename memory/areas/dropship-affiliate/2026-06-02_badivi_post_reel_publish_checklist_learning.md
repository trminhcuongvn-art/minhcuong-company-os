# 2026-06-02 — BaDiVi post-Reel publishing checklist & evidence gate

## Context
Heartbeat 13:27 ICT quét canonical bus + local bun bus: không có task `to_agent=bun` status NEW/IN_PROGRESS hợp lệ chưa có RESULT mới hơn. 3 script Reel BaDiVi đã DONE, Render đã xuất 3 mp4 9:16 đã ffprobe PASS. FB comment scraping vẫn blocker thật khi thiếu cookie/nick phụ; có fallback public-web/Scrapling + top outreach 48 leads.

## Mục tiêu nâng skill
Biến 3 video Reel đã render từ “artifact video” thành chiến dịch đăng thật có đo lead, tránh DONE giả chỉ vì có mp4. Mỗi lần publish phải có 4 lớp bằng chứng: file video, copy/caption, link bài đăng, lead/engagement log.

## Checklist publish 3 Reel BaDiVi
1. **Pre-publish asset QA**
   - Dùng đúng file: `/Users/minhcuong/.openclaw/workspace/render/badivi-reels/reel_01.mp4`, `reel_02.mp4`, `reel_03.mp4`.
   - Không dùng draft `_badivi.mp4` 320x240/deprecated.
   - Verify lại trước upload: 1080x1920, 30-60s, size >0, caption nằm safe-zone.

2. **Caption theo phễu lead B2B**
   - Dòng 1: pain cụ thể, ví dụ “Đóng gói sai có thể làm đơn bị hoàn/vỡ — kiểm tra 3 lỗi này trước khi gửi hàng.”
   - Dòng 2: offer mềm: “BaDiVi hỗ trợ tư vấn băng dính/màng PE theo loại hàng, khối lượng và quy cách đóng gói.”
   - CTA: “Comment ‘BÁO GIÁ’ hoặc inbox: loại hàng + số cuộn/tháng + khu vực để nhận tư vấn.”
   - Không claim số liệu tiết kiệm/giảm hỏng nếu chưa có case study thật.

3. **Tracking bắt buộc**
   - Mỗi Reel có mã chiến dịch: `BDV_REEL01_202606`, `BDV_REEL02_202606`, `BDV_REEL03_202606`.
   - Nếu dùng link: gắn UTM `utm_source=facebook&utm_medium=reel&utm_campaign=badivi_reel_202606&utm_content=reel01`.
   - Comment/inbox phải ghi vào CRM CSV tối thiểu: timestamp, source_reel, name/page, phone/zalo nếu có, nhu_cau, khu_vuc, status, next_action.

4. **Evidence gate sau publish**
   - Link bài đăng hoặc screenshot nếu chưa có link public.
   - Caption đã dùng.
   - 24h metrics: views, comments, shares, inbox, qualified leads.
   - File CRM CSV >1KB hoặc nêu rõ 0 lead trong 24h kèm metrics thật.

## Ma trận thử nghiệm tối thiểu
- Reel 01: pain “hàng hoàn/vỡ” — CTA comment “BÁO GIÁ”.
- Reel 02: pain “chọn sai băng dính/màng PE mất tiền” — CTA gửi ảnh kiện hàng để tư vấn.
- Reel 03: trust/company solution — CTA xin bảng quy cách/MOQ.

## Guardrail
Không báo DONE chiến dịch nếu chỉ upload video mà chưa có link/screenshot + metric/log. Nếu thiếu quyền page Facebook/Zalo/OA thì báo BLOCKER rõ: thiếu quyền đăng, thiếu account, hoặc thiếu cookie/session.
