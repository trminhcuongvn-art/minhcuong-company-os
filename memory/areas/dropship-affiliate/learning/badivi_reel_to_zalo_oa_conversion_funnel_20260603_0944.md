# BaDiVi — Funnel chuyển lead từ Reel/Social → Zalo OA → RFQ/chốt đơn B2B

Ngày: 2026-06-03 09:44 (heartbeat learning — Bún)
Chủ đề: Vì sao Zalo là kênh chốt B2B đóng gói tốt nhất ở VN, và cách thiết kế funnel từ Reel về Zalo OA. Chủ đề MỚI — chưa có note nào trong learning/ cover Zalo conversion.

---

## 1. Vì sao chọn Zalo OA làm "đáy phễu" cho BaDiVi (B2B băng dính/màng co)

- Khách B2B đóng gói VN (xưởng, kho, shop sỉ, công ty logistics) gần như 100% dùng Zalo cho công việc hàng ngày — đặt hàng, gửi báo giá, gửi ảnh sản phẩm, chốt số lượng.
- Email phản hồi chậm/ít check; Facebook Messenger dễ rơi vào spam/secondary inbox với tài khoản doanh nghiệp.
- Zalo cho phép gửi **file PDF báo giá, ảnh quy cách, video demo** ngay trong chat — đúng nhu cầu RFQ packaging.
- Số điện thoại = định danh Zalo => lead có SĐT là gần như chắc chắn liên hệ được.

KẾT LUẬN: Reel/TikTok để KÉO chú ý → nhưng CTA phải đẩy về **Zalo OA**, không phải form web hay inbox FB.

---

## 2. Funnel 3 tầng (Reel → Zalo → RFQ)

**Tầng 1 — Reel/TikTok (Awareness):**
- Hook 3s nói trúng nỗi đau (hàng hoàn/vỡ do đóng gói sai).
- KHÔNG bán hàng trong Reel. Chỉ tạo tò mò + 1 CTA duy nhất.
- CTA cuối Reel/caption: "Nhắn Zalo [số/QR] để nhận bảng quy cách + báo giá sỉ theo loại hàng của bạn."

**Tầng 2 — Zalo OA (Capture + Qualify):**
- Tin nhắn chào tự động (welcome message) khi user nhắn lần đầu:
  - Hỏi 3 câu qualify: (1) Loại hàng đóng gói? (2) Sản lượng/tháng (cuộn/kg)? (3) Khu vực kho?
- Gắn nhãn (label) lead theo persona ngay trong Zalo OA: xưởng / shop sỉ / logistics / cá nhân.
- Gửi ngay 1 file PDF "Bảng chọn băng dính/màng co theo loại hàng" => tạo giá trị trước khi báo giá.

**Tầng 3 — RFQ + chốt:**
- Sau khi user trả lời 3 câu → báo giá thật theo sản lượng.
- Gửi video demo (chính là 3 Reel đã render) qua Zalo để tăng tin tưởng.
- Chốt bằng offer cụ thể: mẫu thử / giá theo thang sản lượng / freeship đơn đầu.

---

## 3. Công cụ Zalo OA tận dụng được (không cần code nhiều)

- **Tin nhắn tự động (auto-reply / welcome):** trả lời tức thì khi lead nhắn — bám SLA <5 phút (khớp note SLA 0213).
- **ZNS (Zalo Notification Service):** gửi template được duyệt cho follow-up có cấu trúc (xác nhận RFQ, nhắc báo giá). Lưu ý: ZNS cần template approve + chi phí/tin, dùng cho re-engage lead đã có SĐT.
- **Broadcast OA:** gửi nội dung mới (sản phẩm, video) cho follower đã quan tâm — chi phí thấp hơn quảng cáo lạnh.
- **Label + ghi chú:** thay CRM nhẹ cho giai đoạn đầu; export khi cần đồng bộ với crm_lead_log_template.csv.

---

## 4. Bổ sung field CRM cho funnel Zalo (đề xuất thêm vào crm_lead_log_template.csv)

| Field mới | Ý nghĩa |
|---|---|
| zalo_phone | SĐT = định danh Zalo, key liên hệ |
| zalo_label | Nhãn persona gán trong OA |
| welcome_answered | Đã trả lời 3 câu qualify? (Y/N) |
| pdf_sent | Đã gửi bảng quy cách? (Y/N) |
| demo_video_sent | Đã gửi Reel demo qua Zalo? (Y/N) |
| zns_followup_count | Số lần ZNS follow-up đã gửi |

---

## 5. KPI funnel (north-star vẫn là RFQ qualified, không vanity)

- Reel view → Zalo click rate (CTA hiệu quả không).
- Zalo nhắn lần đầu → trả lời 3 câu qualify (qualify rate).
- Qualify → RFQ thật (báo giá theo sản lượng).
- RFQ → đơn mẫu/đơn đầu (close rate).
- Đo từng tầng để biết nghẽn ở đâu: thường nghẽn ở tầng 1→2 (CTA Reel yếu) hoặc 2→3 (welcome hỏi quá nhiều, lead bỏ).

---

## 6. Sai lầm cần tránh

- Đặt nhiều CTA trong Reel (web + FB + Zalo) → loãng. Chỉ 1 CTA = Zalo.
- Welcome message hỏi >3 câu → lead nản, rớt.
- Báo giá ngay khi chưa biết sản lượng → giá sai, mất uy tín.
- Spam broadcast/ZNS → bị report, OA giảm tin cậy. Chỉ gửi khi có giá trị thật.

---

## Blocker liên quan
- FB comment/lead scrape tự động vẫn cần cookie/nick phụ hợp lệ — KHÔNG chặn funnel Zalo (Zalo dùng kênh riêng, đã có tool zalouser khả dụng cho test outreach).
- Web search hiện không cấu hình (SearXNG base URL chưa set) → note này viết từ kiến thức nội tại về kênh B2B VN, cần verify số liệu chi phí ZNS thực tế khi có nguồn.

## Next skill gợi ý
- Soạn sẵn welcome script 3 câu + PDF "bảng chọn băng dính/màng co theo loại hàng" để gắn vào OA.
- Map 3 Reel hiện có vào đúng tầng funnel nào để gửi qua Zalo.
