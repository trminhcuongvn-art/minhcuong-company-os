# 2026-06-04 03:02 — BaDiVi B2B Reel comment/manual triage without FB cookie

## Context
Heartbeat Bún quét canonical bus + local bus: không có task `to_agent=bun` trạng thái `NEW/IN_PROGRESS` khả thi chưa có RESULT mới hơn. Các task game gần nhất: web MVP DONE, polish DONE; Unity foundation PARTIAL do Unity Editor cần Rosetta 2 nên chưa có compile/playtest evidence. SmallBizOps/Tarot/Ông Đồ.AI freeze. Với BaDiVi, blocker tự động Facebook vẫn là thiếu cookie/nick phụ hoặc FB login-wall; vì vậy nhịp này học/nâng skill theo hướng **manual triage sau khi đăng Reel**, không cần cookie.

## Skill: quy trình triage comment/inbox thủ công trong 30 phút đầu
Mục tiêu: biến tín hiệu sau Reel thành RFQ đủ dữ liệu, tránh sa vào vanity metrics.

### 1) Phân loại tín hiệu
- **A — RFQ-ready**: hỏi giá, số lượng, kích thước, giao hàng, in logo, VAT, mẫu thử.
- **B — Buyer intent mềm**: hỏi “có loại này không”, “băng dính này bền không”, tag đồng nghiệp/kho/xưởng.
- **C — Channel/partner**: đại lý vật tư, carton, kho vận, seller phụ kiện đóng gói.
- **D — Noise**: spam, emoji, hỏi lạc đề.

### 2) Response SLA
- A: phản hồi <15 phút, chuyển ngay sang form RFQ/Zalo với 6 trường: loại băng dính, quy cách, số lượng/tháng, tỉnh giao, cần in logo hay không, deadline cần hàng.
- B: phản hồi <30 phút bằng 1 câu chẩn đoán + CTA RFQ rút gọn.
- C: xin danh mục/địa bàn/phân khúc để xét cộng tác; log vào CRM nhưng không ưu tiên báo giá.
- D: không inbox trừ khi có tín hiệu chuyển nhóm.

### 3) Mẫu reply ngắn
- A: “Bên em báo giá được. Anh/chị cho em 6 thông tin: loại băng dính, quy cách, số lượng dự kiến/tháng, tỉnh giao, có in logo không, thời điểm cần hàng. Có thể gửi nhanh qua Zalo/RFQ để em chốt đúng giá.”
- B: “Loại này cần xem thùng/hàng nặng nhẹ và môi trường kho. Anh/chị đóng hàng ngành gì, mỗi tháng dùng khoảng bao nhiêu cuộn?”
- C: “Bên em có thể trao đổi kênh phân phối/vật tư đóng gói. Anh/chị đang bán khu vực nào và nhóm khách chính là xưởng/kho/sàn TMĐT?”

### 4) CRM fields tối thiểu
`source_reel`, `comment_url`, `lead_name`, `company_or_page`, `phone_zalo`, `province`, `product_need`, `monthly_volume`, `urgency`, `lead_grade`, `next_followup_at`, `owner`, `status`.

### 5) KPI 24h sau đăng
- Qualified RFQ count, không chỉ view/comment.
- Median response time với nhóm A/B.
- % lead có đủ 6 trường RFQ.
- Quote sent count.
- Follow-up due count.

## Evidence gate áp dụng
DONE chỉ tính nếu có file log/CSV thật >1KB sau khi đăng: `crm_lead_log_template.csv` có row thật, hoặc screenshot/comment URL + triage sheet. Nếu chưa có cookie FB, vẫn có thể làm manual bằng browser/login của người vận hành; không tự động scrape.

## Rollback
Xoá note này nếu không dùng: `rm /Users/minhcuong/.openclaw/workspace/memory/areas/dropship-affiliate/learning/2026-06-04_0302_badivi_b2b_reel_comment_manual_triage_without_cookie.md`.
