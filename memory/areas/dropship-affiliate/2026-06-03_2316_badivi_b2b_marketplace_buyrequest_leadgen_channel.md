# BaDiVi — Kênh leadgen B2B Marketplace "Buy Request" (không cần cookie FB)

**Ngày:** 2026-06-03 23:16 | **Agent:** Bún | **Loại:** Heartbeat learning — leadgen channel
**Bối cảnh:** Leadgen BaDiVi đang bị chặn ở cookie Facebook. Cần kênh nguồn lead B2B thay thế, ghi vào RFQ pipeline đã có (crm_lead_log_template.csv). Đây là note research → áp dụng vào outreach_sequence.

---

## 1. Vấn đề & insight
- BaDiVi (băng dính/màng co đóng gói B2B) bán cho nhà máy, kho vận, FMCG packer, e-commerce fulfillment.
- FB Reels/Ads chỉ tốt cho inbound brand awareness; **outbound RFQ phải tới đúng người mua công nghiệp**.
- Insight mới từ research: tồn tại lớp nền tảng **"Buy Request / RFQ marketplace"** — buyer chủ động đăng nhu cầu mua, supplier reply. Đây là **inbound-có-ý-định-cao mà không cần FB**.

## 2. Bản đồ kênh (4 lớp) — ưu tiên cho BaDiVi

| Lớp | Nền tảng | Cơ chế lead | Chi phí | Phù hợp BaDiVi |
|---|---|---|---|---|
| A. Buy-request board | Tradewheel.com `/buyers/stretch-film`, TradeFord `/packaging-tape` | Buyer đăng "buy request" công khai → mình reply RFQ | Free tier + paid membership | ⭐⭐⭐⭐ Cao — intent rõ |
| B. Marketplace lớn | Alibaba.com, GlobalSources, Made-in-China | Đăng product + nhận inquiry; có RFQ market | Membership phí cao | ⭐⭐⭐ Cần đầu tư |
| C. Trade data intel | Volza (62k buyers / 51k suppliers packing tape+stretch film), ImportGenius | Mua dữ liệu shipment → list buyer thật đang nhập | Trả phí data | ⭐⭐⭐⭐ Targeting cực chuẩn |
| D. Domestic VN | Các sàn B2B nội (vật tư công nghiệp), group ngành logistics/đóng gói | Outbound trực tiếp | Free | ⭐⭐⭐⭐ Ít rào cản nhất, làm trước |

## 3. Playbook áp dụng (không cần cookie FB)
**Bước 1 — Harvest buy-request (free):**
- Quét trang buyer của stretch film / packaging tape: lấy `tên cty, quốc gia, sản phẩm cần, số lượng, ngày đăng`.
- Lọc theo thị trường mục tiêu: VN nội địa + ASEAN (Indo, Phil, Thái) trước EU (rào cản logistics/chứng nhận cao hơn).

**Bước 2 — Enrich:**
- Map vào `crm_lead_log_template.csv` đã build (cột: company, country, product_need, qty, source, intent_score, stage, next_action).
- intent_score: buy-request gần đây <30 ngày = HOT.

**Bước 3 — Reply RFQ chuẩn:**
- Dùng `rfq_form_spec.md` + spec sheet template đã có (note 2232).
- Phản hồi trong <24h, đính kèm: spec kỹ thuật (độ dày micron, độ dính, MOQ), bảng giá theo bậc, ảnh sản phẩm thật, video Reel BaDiVi (3 mp4 Render đã có).

**Bước 4 — Sequence:** dùng `outreach_sequence.md` 5 chạm (intro → spec → mẫu → giá → chốt MOQ).

## 4. Đề xuất next-action cho pipeline
1. **Tự build scraper buy-request** (giống trend scraper đã có) → output CSV daily, không cần login với nguồn public listing. Rủi ro thấp, làm được ngay.
2. **Domestic-first**: 70% effort vào buyer VN + ASEAN (logistics gần, MOQ vừa, thanh toán dễ); 30% EU exploratory.
3. **Trade-data như món de' đầu tư**: chỉ mua data Volza/tương tự khi đã validate được conversion từ kênh free — tránh đốt tiền sớm (AI First checklist: có tốn tiền → phải hỏi Henry trước).

## 5. Đo lường
- KPI kênh này: # buy-request harvested/ngày, # RFQ reply gửi, reply-rate, # quote → # mẫu gửi → # đơn MOQ.
- Mục tiêu validate tuần đầu: 30 buy-request thật, 10 RFQ reply, đo reply-rate baseline.

## 6. Tái sử dụng tài sản đã có
- Reels mp4 (Render) → đính kèm RFQ làm social proof.
- campaign_pack.md + captions_utm.csv → repurpose landing/RFQ form.
- crm_lead_log_template.csv → đổ lead mới vào.

---
**Trạng thái:** Note learning DONE — chưa scrape thật (cần xác nhận nguồn public hợp lệ trước khi build scraper). Đề xuất #1 (scraper buy-request public) đủ rủi ro thấp để tự làm ở heartbeat sau.
