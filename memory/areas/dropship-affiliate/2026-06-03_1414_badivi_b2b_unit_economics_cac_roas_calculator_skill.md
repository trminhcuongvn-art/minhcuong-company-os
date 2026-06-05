# BaDiVi B2B — Unit Economics: CAC / CPL / CPQ / ROAS / Payback (skill + calculator)

Ngày: 2026-06-03 14:14 (heartbeat learning — Bún)
Khoảng trống lấp: các note trước phủ hook/retention/distribution/leadgen/RFQ/objection/AB-test, nhưng CHƯA có khung **đo hiệu quả đồng tiền** khi đổ ads/boost cho 3 reel. Note này định nghĩa unit economics B2B và kèm calculator chạy được.

## 1. Vì sao B2B khác B2C khi đo
- Chu kỳ bán dài (lead → RFQ → báo giá → mẫu → đàm phán → đơn): 2–8 tuần. Không đo ROAS theo ngày như B2C.
- Giá trị đơn lớn, tần suất lặp (reorder) cao → LTV mới là thước đo, không phải đơn đầu.
- Phễu hẹp: ít lead nhưng chất → tối ưu **chất lượng lead (SQL)**, không phải số lead thô.
- Vì vậy KPI chính: **CPQ (cost per qualified RFQ)** và **LTV/CAC**, không phải CPM/CPC.

## 2. Định nghĩa metric (chuẩn để mọi agent dùng chung)
- Spend = tiền ads/boost đã chi trong kỳ.
- Lead = số người để lại liên hệ (form/DM/comment-to-DM).
- SQL (Sales Qualified Lead) = lead đạt tiêu chí: có nhu cầu thật + số lượng/tháng + ngân sách + người quyết định (BANT rút gọn).
- RFQ = yêu cầu báo giá thực (đã gửi spec/số lượng).
- Won = đơn chốt.
- CPL = Spend / Lead
- CPQ = Spend / RFQ  ← KPI gate chính cho BaDiVi
- CAC = Spend / Won (chỉ tính chi phí marketing; nếu có sales cost thì cộng vào CAC mở rộng)
- AOV = doanh thu trung bình/đơn won
- GM% = biên gộp (giá bán − giá vốn − ship) / giá bán
- LTV = AOV × GM% × số đơn lặp dự kiến (reorder)
- ROAS = doanh thu won / Spend
- Contribution ROAS = (doanh thu won × GM%) / Spend  ← thước đo lời thật
- Payback (đơn) = CAC / (AOV × GM%) → bao nhiêu đơn để hoàn vốn 1 khách

## 3. Benchmark khởi điểm BaDiVi (mốc TEST — KHÔNG phải claim thật)
Dùng làm ngưỡng để bật/tắt ngân sách, hiệu chỉnh sau 2 tuần data thật:
- CPL mục tiêu: ≤ 30–60k đ/lead (VN, B2B niche packaging)
- Lead→SQL: ≥ 25%
- SQL→RFQ: ≥ 50%
- RFQ→Won: 15–30% (B2B công nghiệp)
- CPQ trần (kill switch): nếu CPQ > 2× giá trị GM của 1 đơn trung bình → cắt creative/audience đó.
- Contribution ROAS gate ngắn hạn: ≥ 1.0 trong 72h (chấp nhận lỗ creative kém), ≥ 2.5 sau 2 tuần.
- LTV/CAC mục tiêu lành mạnh: ≥ 3.0.

## 4. Quy trình quyết định ngân sách (7 ngày đầu)
1. Chia ngân sách đều 3 reel (creative test) — mỗi reel 1 ad set.
2. Ngày 1–3: chỉ xem CPL + hook retention (3s). Cắt reel CPL cao nhất nếu chênh >50% median.
3. Ngày 4–7: chuyển sang CPQ. Dồn 70% ngân sách vào reel có CPQ thấp nhất.
4. Tuần 2: tính Contribution ROAS + LTV/CAC; chỉ scale khi LTV/CAC ≥ 3 và CPQ ổn định.
5. Mọi quyết định ghi vào crm_lead_log_template.csv (đã có ở campaign kit) để truy vết.

## 5. Calculator
Script: `/Users/minhcuong/.openclaw/workspace/bun/badivi-tools/unit_economics_calc.py`
Chạy: `python3 unit_economics_calc.py` (đọc input JSON hoặc dùng demo). Output: bảng metric + verdict scale/hold/kill.

## 6. Liên kết
- Campaign kit: bun/badivi-campaign-kit-20260603/ (captions_utm.csv, crm_lead_log_template.csv)
- AB-test/cadence: 2026-06-03_1329_badivi_reels_ab_test_cadence_kpi_playbook.md
- Lead scoring: 2026-06-02_badivi_b2b_lead_scoring_rfq_prioritization_skill.md

## 7. BLOCKER chạy thật
Chưa có FB/TikTok ad account + page permission + ngân sách. Khi có: nạp số thật vào calculator, không bịa.
