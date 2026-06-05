# BaDiVi — Outbound đa kênh KHÔNG phụ thuộc FB cookie (Zalo OA + Cold Email + sàn B2B)

Ngày: 2026-06-04 06:48 (+07) · Agent: Bún · Loại: Learning/Skill
Bối cảnh: FB cookie/nick phụ là blocker dai dẳng cho auto-scrape & auto-post. Reel/leadgen đã có pipeline thủ công, nhưng phụ thuộc 1 kênh (FB) là rủi ro. Note này thiết kế funnel RFQ B2B đa kênh để giảm phụ thuộc FB, dùng đúng evidence gate.

## 1. Vấn đề & mục tiêu
- BaDiVi = băng dính/màng co đóng gói B2B. Khách mục tiêu: xưởng/SME đóng gói, kho vận, thực phẩm/may mặc, sàn TMĐT seller volume.
- FB Reel chỉ là 1 đỉnh phễu. Nếu FB chặn/khóa → mất lead. Cần ≥3 kênh outbound độc lập, tất cả đổ về 1 RFQ form + 1 CRM CSV (đã có template ở badivi-campaign-kit).
- KPI giả định: mỗi kênh ≥ X lead RFQ/tuần; không bịa số — để dạng placeholder cần đo thật.

## 2. Ba kênh outbound độc lập FB

### A. Zalo OA / Zalo cá nhân (mạnh nhất ở VN B2B)
- Zalo có tool `zalouser` (send/image/link/friends/groups). Có thể nhắn tin trực tiếp tới friend/group đã kết nối → kênh outreach hợp pháp với tệp đã quen.
- Playbook: (1) tìm nhóm ngành đóng gói/kho vận trên Zalo, (2) kết bạn người mua hàng/purchasing, (3) gửi mini-demo (ảnh sản phẩm + link RFQ), (4) follow-up 2 chạm.
- Ưu: tỷ lệ mở cao, người VN quen mua qua Zalo. Nhược: rate-limit, cần tệp friend thật — không spam lạnh hàng loạt (vi phạm + risk khóa).

### B. Cold Email B2B (kênh sạch nhất, ít phụ thuộc nền tảng)
- Nguồn email: web công ty (mục Liên hệ), sàn B2B, Google Maps doanh nghiệp ngành đóng gói. Thu thủ công/scrape web public (không cần FB).
- Sequence 3 chạm: Day0 (pain + 1 proof + CTA xem demo), Day3 (case/ảnh sản phẩm), Day7 (offer mẫu thử/giá theo volume).
- Subject line theo angle pain: "Hàng bị bóp méo khi vận chuyển? Lỗi màng co thường gặp", "Đang trả thừa tiền băng dính kém dính?".
- Tool: SMTP/Gmail API hoặc dịch vụ gửi (cần Henry chốt domain + tránh spam). Soạn nội dung sẵn là việc rủi ro thấp → làm ngay; gửi thật cần quyết định.

### C. Sàn B2B & directory (inbound-passive + outbound RFQ)
- Đăng gian hàng / tìm buyer trên: vatgia, các nhóm chợ đầu mối, sàn nội địa; quốc tế: Alibaba RFQ, Made-in-China (nếu hướng export — đã có market research export 2026-05-31).
- Trả lời RFQ có sẵn (buyer đang chủ động tìm) → conversion cao hơn cold.
- Directory Google Maps: list xưởng đóng gói theo tỉnh → enrich SĐT/Zalo → đẩy vào kênh A.

## 3. Kiến trúc phễu hợp nhất (1 đích đến)
```
[FB Reel] ─┐
[Zalo OA] ─┼─► RFQ form (Google Form/landing) ─► crm_lead_log_template.csv ─► scoring ─► follow-up
[Cold Email]┤        + UTM source=kênh                  (hook_id, channel, score)
[Sàn B2B]  ─┘
```
- Mỗi kênh gắn UTM/`channel` riêng để A/B attribution (đã có captions_utm.csv + hook_id từ note 0517).
- CRM field tối thiểu: ngày, kênh, công ty, người LH, SĐT/Zalo/email, nhu cầu (loại băng dính/màng co + volume), score, trạng thái, next action.

## 4. Lead scoring (tái dùng từ note 0002/0302, chuẩn hoá)
- +3 nêu rõ volume/tháng · +2 ngành phù hợp (kho/đóng gói/thực phẩm/may) · +2 hỏi giá/mẫu · +1 có SĐT/Zalo · -2 chỉ hỏi lẻ 1 cuộn.
- Score ≥5 = ưu tiên gọi/Zalo trong 24h. 3-4 = nurture email. <3 = drip nội dung.

## 5. Việc rủi ro thấp làm được NGAY (không cần Henry)
1. Soạn sẵn 3 email template sequence (.md) + 5 subject line theo angle pain.
2. Soạn 5 mẫu tin nhắn Zalo outreach + 2 follow-up.
3. Chuẩn RFQ form spec (đã có rfq_form_spec.md) — map field sang CRM CSV.
4. Script enrich Google Maps → CSV (web public, không FB cookie).

## 6. Cần Henry quyết (rủi ro cao)
- Gửi email thật (domain, volume, tránh blacklist) → đụng reputation domain.
- Gửi Zalo hàng loạt → risk khóa nick; chỉ làm với tệp đã quen.
- Đăng gian hàng sàn có phí.

## 7. Next action gợi ý cho heartbeat sau
- Tạo `badivi-outbound/` chứa: email_sequence.md, zalo_scripts.md, gmaps_enrich.py (web public), unified_crm_map.md.
- Liên kết với campaign-kit đã có để thành 1 launch kit đa kênh hoàn chỉnh.

## Rollback
rm /Users/minhcuong/.openclaw/workspace/memory/areas/dropship-affiliate/learning/2026-06-04_0648_badivi_outbound_multichannel_no_fb_funnel.md
