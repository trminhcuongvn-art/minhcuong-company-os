# BaDiVi — Skill: B2B Cold Outreach Copywriting (biến top50 lead thành reply)

Ngày: 2026-06-02 (Bún, heartbeat learning)
Bối cảnh: Đã có `badivi-leadgen/badivi_top50_outreach_20260601.csv` (48 lead unique, segment ASEAN 28 + nội địa 20, có phone/email một phần). Bước nghẽn tiếp theo KHÔNG phải tìm thêm lead mà là **tỷ lệ reply**. Note này đúc skill copywriting cold outreach B2B áp dụng ngay.

## 1. Nguyên tắc cốt lõi (B2B khác B2C)
- B2B mua vì **giảm rủi ro/chi phí**, không vì cảm xúc. Mọi câu phải quy về tiền/thời gian/uy tín.
- Người đọc là chủ xưởng/mua hàng (purchaser), bận, đọc 3 giây. → Subject + dòng đầu quyết định 80%.
- Cold outreach không bán ngay — chỉ xin **1 micro-yes** (xem báo giá / nhận mẫu / 1 câu trả lời).
- Cá nhân hóa thật (tên DN + ngành cụ thể) > template chung. Lead CSV đã có `category` để cá nhân hóa.

## 2. Khung email/inbox 5 dòng (ngắn, mobile-first)
1. **Trigger cá nhân hóa**: "Em thấy bên [Tên] đang phân phối/đóng gói [ngành cụ thể]..."
2. **Pain quy ra tiền**: "...nhiều đơn vị cùng ngành đang mất 2-5% hàng do băng dính bong/màng PE rách khi vận chuyển xa."
3. **Proof ngắn**: "BaDiVi (Việt Hàn, Hải Phòng) là **nhà sản xuất** băng dính OPP/in logo + màng PE, không qua trung gian."
4. **Offer rủi ro thấp**: "Gửi anh/chị **bảng giá theo MOQ + mẫu test miễn phí** trong 24h, không cam kết mua."
5. **CTA 1 chạm**: "Anh/chị cho em xin **quy cách + sản lượng/tháng** là em báo giá ngay ạ. Zalo: 0941463869."

## 3. Subject line / dòng mở Zalo (A/B test)
- A (pain): "Giảm 2-5% hàng vỡ khi đóng gói — [Tên DN]"
- B (giá): "Báo giá băng dính OPP tận xưởng cho [Tên DN]"
- C (mẫu): "Mẫu test băng dính/màng PE miễn phí — [Tên DN]"
→ Đo open/reply theo từng biến thể, giữ winner.

## 4. Biến thể theo segment (từ CSV)
- **Nội địa (Hải Phòng/QN/HD)**: nhấn "tận xưởng, giao nhanh nội vùng, hỗ trợ in logo theo yêu cầu". CTA Zalo.
- **ASEAN supplier/distributor** (Malaysia, v.v.): tiếng Anh, nhấn "OEM/private-label OPP tape & PE film from Vietnam factory, FOB Haiphong, competitive vs local". CTA: "Send our catalog + FOB price?" → email.
- **Đối thủ/đại lý**: đổi góc — không bán, mà offer **làm nguồn cung sỉ/OEM** (B2B2B).

## 5. Sai lầm cần tránh
- Tường email dài, kể lể lịch sử công ty → xóa ngay.
- Gửi link website có placeholder `info@example.com` / `+1` (audit đã phát hiện) → mất uy tín. **Phải sửa website trước khi gửi outreach.**
- Spam đồng loạt 1 nội dung → vào spam + cháy domain. Gửi 10-15/ngày, cá nhân hóa.
- Không có cách đo reply → mù. Phải tag nguồn (UTM/Zalo OA) + cột status trong CRM CSV.

## 6. Quy trình đo lường (gắn với lead CSV)
Thêm cột vào CSV outreach: `sent_date, channel(email/zalo/fb), subject_variant, opened, replied, status(new/replied/quote_sent/sample_sent/won/lost), note`.
- KPI vòng 1: gửi 48 lead → mục tiêu reply rate ≥10% (5 reply), quote_sent ≥3.
- Nếu reply <5%: vấn đề ở subject/offer, không phải sản phẩm → đổi offer (mẫu free mạnh hơn).

## 7. 3 việc thực thi tiếp (khi Henry mở)
1. **Sửa trust website** (info@example.com, +1, thêm CTA Zalo/báo giá) — chặn outreach hiệu quả.
2. Tạo `badivi_outreach_tracker.csv` từ top50 + 7 cột đo lường ở trên.
3. Soạn 3 template hoàn chỉnh (VI nội địa / EN ASEAN / OEM-offer) sẵn copy-paste.

## Liên kết
- Lead: `bun/badivi-leadgen/badivi_top50_outreach_20260601.csv` (48 rows)
- Reels funnel: các note `2026-06-02_badivi_reels_*`
- Website audit: `bun/plan/badivi_website_audit_bangdinhviethan_2026.md`
