# BaDiVi — B2B Cold Outreach Copywriting (EN + VN) cho buyer ASEAN/quốc tế
Date: 2026-06-03 08:13 (+07) | Author: Bún | Topic: copywriting outreach để biến top50 lead thành reply/RFQ

## 1. Vì sao cần note này
- Top50 outreach list (badivi_top50_outreach_20260601.csv, 27KB) gồm ASEAN 28 + domestic 20.
- Các note trước tập trung Reel/A/B test/SLA. CHƯA có khung copywriting outreach message cụ thể cho cold contact B2B (email/LinkedIn/WhatsApp).
- Mục tiêu: tăng reply rate -> book call/RFQ, KHÔNG spam, KHÔNG bịa claim sản phẩm.

## 2. Nguyên tắc cốt lõi (B2B cold, không phải B2C)
1. **Relevance > Volume**: 1 dòng đầu phải chứng minh "tôi nghiên cứu DN bạn", không template chung chung.
2. **Một CTA duy nhất**, low-friction: "Bạn có muốn nhận bảng giá FOB + mẫu test không?" thay vì "mua ngay".
3. **Ngắn**: cold email B2B hiệu quả thường 50–125 từ. Mobile-readable.
4. **Value-first**: nói lợi ích đo được của họ (giảm hàng hoàn/vỡ, giảm chi phí đóng gói/đơn), không nói về mình.
5. **No fake urgency / no fake claim**: chỉ nêu fact thật (MOQ, FOB, lead time, cert nếu có thật).

## 3. Khung 4 dòng PAS-lite cho cold email EN
- **Line 1 (Hook/Relevance)**: nhắc ngành/sản phẩm của họ cụ thể.
- **Line 2 (Pain)**: vấn đề đóng gói phổ biến của phân khúc đó.
- **Line 3 (Proof/Offer)**: BaDiVi giải quyết thế nào + offer cụ thể (mẫu test / báo giá FOB).
- **Line 4 (CTA câu hỏi)**: 1 câu hỏi yes/no dễ trả lời.

## 4. Template EN (điền {{biến}})
Subject options (A/B):
- A: "Packaging tape that survives long-haul to {{country}}"
- B: "Quick question about {{company}}'s carton sealing"

Body:
> Hi {{first_name}},
> Saw {{company}} ships {{product_category}} — long-haul freight often means tape lifting and cartons opening in transit.
> We're BaDiVi, a Vietnam-based packaging tape/PE film manufacturer. We supply B2B with FOB Hai Phong pricing, MOQ {{moq}}, and can send a free sample roll for your line to test adhesion before any order.
> Would it help if I sent the spec sheet + FOB quote this week?
> Best, {{sender}} | BaDiVi | {{phone/whatsapp}}

## 5. Biến thể kênh
- **LinkedIn DM**: bỏ subject, rút còn 3 dòng, kết bằng "Open to a quick chat?".
- **WhatsApp**: thêm 1 dòng giới thiệu danh tính + đề nghị gửi catalogue PDF; tránh gửi nhiều tin liên tiếp.
- **VN nội địa (Zalo/email)**: dùng tiếng Việt, nhấn "test mẫu miễn phí + báo giá tận xưởng Hải Phòng", CTA "Anh/chị cho em xin SĐT Zalo để gửi bảng giá nhé?".

## 6. Follow-up sequence (cold -> warm), không spam
- T+0: email/DM #1 (template trên).
- T+3 ngày: follow-up #1 — thêm 1 proof point khác (ví dụ: ảnh test peel-off), KHÔNG lặp y nguyên.
- T+7 ngày: follow-up #2 — đổi offer (gửi luôn quote PDF kèm sẵn) + "breakup" nhẹ: "Nếu chưa đúng thời điểm, em gửi lại sau quý nhé?".
- Tối đa 3 chạm cold. Quá 3 mà không reply -> chuyển sang nurture list, không đẩy tiếp.

## 7. Personalization tokens cần điền từ CSV
- {{company}}, {{first_name}}, {{country}}, {{product_category}} — lấy từ cột lead.
- Lead nào thiếu token cá nhân hóa -> hạ priority, không gửi cold message generic (giảm reply + tăng nguy cơ spam-flag).

## 8. KPI đo lường (evidence gate)
- North-star: số RFQ qualified / 100 outreach gửi đi (KHÔNG dùng open rate làm thành tích).
- Track trong CRM CSV: sent_date, channel, opened?, replied?, rfq?, quote_sent?, status.
- Quy tắc quyết định: nếu sau 100 cold message mà reply < ~5% -> sửa subject/dòng 1 (relevance) trước; nếu reply ổn nhưng RFQ thấp -> sửa offer/CTA.

## 9. Compliance / risk
- Không scrape email trái ToS; chỉ dùng email/phone public đã thu hợp lệ (note Scrapling public-web).
- Tôn trọng opt-out; lead nói "no" -> remove khỏi list.
- Không claim chứng nhận/thông số chưa có thật. Mọi spec đợi Henry xác nhận (FOB/MOQ/cert/tên pháp lý EN — vẫn pending từ note Alibaba 01/06).

## 10. Next (khi có dữ liệu thật)
- Henry duyệt spec/FOB/MOQ -> điền vào template thật.
- Gắn template này vào outreach_sequence.md của campaign kit để dùng đồng bộ.
- Sau 1 batch 50 cold message -> log CRM CSV -> review reply/RFQ, vòng tối ưu tiếp.

## Blocker
- Vẫn pending: spec/FOB/MOQ/cert/tên pháp lý EN từ Henry (chặn việc gửi outreach thật, không chặn việc chuẩn bị template).
- FB comment/lead scrape tự động vẫn cần cookie/nick phụ hợp lệ.
