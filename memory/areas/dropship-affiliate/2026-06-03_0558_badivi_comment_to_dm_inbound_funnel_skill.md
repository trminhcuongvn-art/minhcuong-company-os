# BaDiVi — Inbound Comment-to-DM Funnel (lách blocker FB scrape, chi phí 0)

Ngày: 2026-06-03 05:58 (heartbeat Bún)
Tác giả: Bún | Area: dropship-affiliate / BaDiVi B2B packaging
Trạng thái nền: FB public scrape (outbound) đang bị login wall — các CSV layer B đều rỗng (46B header-only). POC README đã ghi blocker thật. → Pivot sang INBOUND.

## 1. Vì sao đổi hướng outbound → inbound
- Outbound scrape comment public bằng facebook-scraper/Playwright bị Facebook chặn (login wall, 0 comment). Cần cookie nick phụ → rủi ro checkpoint, không bền.
- Inbound funnel: để khách TỰ comment dưới Reel/Post của BaDiVi → mình chỉ cần thu lead từ comment trên CHÍNH page mình (hợp pháp, không cần scrape bên thứ 3, không cần cookie người khác).
- Đã có 3 Reel 9:16 đang render (A2A render IN_PROGRESS) → đây là nguồn traffic để kích comment.

## 2. Cơ chế funnel (5 bước)
1. Reel/Post có CTA cụ thể: "Comment 'BÁO GIÁ' + loại hàng để nhận bảng giá sỉ + mẫu test."
2. Khách comment keyword → trigger.
3. Auto-reply công khai (giữ reach) + chuyển sang DM xin SĐT/Zalo + nhu cầu (số lượng, quy cách, tần suất).
4. Lọc intent → đẩy vào RFQ pipeline (đã có lead_scoring_rfq skill + quote_pricing_tiers skill).
5. Follow-up theo SLA (đã có quote_followup_sla learning).

## 3. Keyword trigger gợi ý (B2B băng dính/màng co)
- "BÁO GIÁ", "GIÁ SỈ", "MẪU", "SỐ LƯỢNG LỚN", "CARTON", "MÀNG CO", "ĐÓNG GÓI"
- Mỗi keyword map 1 canned response (xem mục 5).

## 4. Công cụ chi phí 0 (không cần cookie người khác)
- **Meta Graph API + Page Access Token (chính chủ page BaDiVi)**: webhook `feed`/`comments` → đọc comment trên page mình hợp lệ. Đây là cách CHÍNH THỐNG, không bị chặn như scrape.
  - Cần: 1 FB Page BaDiVi + 1 App dev (free) + Page token. Đây là tài sản của chính Henry → KHÔNG phải blocker cookie nick lạ.
- **Private Reply API**: `POST /{comment-id}/private_replies` → gửi DM cho người comment (trong 7 ngày). Đúng cơ chế comment→DM hợp pháp.
- Fallback thủ công nếu chưa dựng App: lọc comment bằng tay 2 lần/ngày, copy-paste canned response. Vẫn 0đ.

## 5. Canned responses (copy-paste sẵn)
**Reply công khai (giữ reach):**
> "Dạ BaDiVi đã gửi bảng giá sỉ + quy cách vào tin nhắn cho mình nhé. Anh/chị check Messenger giúp em ạ 📦"

**DM mở đầu (xin thông tin RFQ):**
> "Chào anh/chị, em là tư vấn sỉ của BaDiVi (băng dính/màng co/vật tư đóng gói). Để báo giá chuẩn, anh/chị cho em xin:
> 1) Loại hàng + quy cách (vd băng keo trong 48mm, màng co 500mm)
> 2) Số lượng/tháng dự kiến
> 3) Khu vực giao (Hải Phòng/khác)
> Em gửi báo giá + mẫu test trong 1h ạ."

## 6. Đo lường (KPI inbound)
- Comment chứa keyword / Reel (trigger rate)
- DM mở / comment trigger (conversion comment→DM)
- SĐT-Zalo thu được / DM (lead capture rate)
- RFQ tạo / lead → nối vào quote pipeline
Mục tiêu khởi điểm 72h sau publish 3 Reel: ≥15 comment trigger, ≥8 DM, ≥4 lead có SĐT.

## 7. Vì sao đây là cách bền hơn scrape
- Hợp pháp (dữ liệu trên page mình), không vi phạm ToS, không checkpoint.
- Không phụ thuộc cookie nick phụ → gỡ được blocker chính hiện tại.
- Tận dụng được tài sản đang có (3 Reel render) + các skill RFQ đã viết.

## 8. Next action khả thi (không cần Henry ngay)
- [ ] Chốt CTA keyword đưa vào caption 3 Reel TRƯỚC khi publish (sync với render/cao).
- [ ] Soạn sẵn 5-7 canned response theo keyword → lưu badivi-leadgen/canned_responses.md.
- [ ] (Khi Henry sẵn sàng) dựng FB Page + App dev để bật Graph webhook comment→private_reply.

## Blocker còn lại (thật)
- Chưa có FB Page BaDiVi chính chủ + App token để tự động hoá. Bước thủ công vẫn chạy được 0đ ngay.
- Cần Henry xác nhận caption CTA cho 3 Reel đang render để funnel khớp.
