# BaDiVi — Buyer persona mapping cho B2B packaging lead-gen

## Mục tiêu
Biến lead rời rạc từ Reel/website/public-web thành đúng nhóm người mua để viết offer và follow-up chính xác hơn, tránh gửi một mẫu cho mọi khách.

## 5 persona ưu tiên
1. **Xưởng/nhà máy sản xuất**: cần băng dính OPP, màng PE, băng dính in logo theo lô đều. Nỗi đau: hàng bung/vỡ, thiếu vật tư đột xuất, cần hóa đơn/ổn định.
2. **Kho vận/fulfillment/e-commerce seller lớn**: cần đóng gói nhanh, giảm hoàn hàng, có quy cách cố định. Nỗi đau: tốc độ đóng hàng, chi phí mỗi đơn, thiếu tồn cuối tuần.
3. **Đại lý vật tư đóng gói**: mua lại để bán. Nỗi đau: giá sỉ, chiết khấu, giao nhanh, danh mục đủ.
4. **Xưởng carton/bao bì adjacent**: không nhất thiết là khách cuối, nhưng là kênh referral/cross-sell. Nỗi đau: cần thêm băng dính/màng PE để trọn gói đơn hàng.
5. **SME mới mở kho/xưởng**: chưa biết quy cách. Nỗi đau: chọn sai băng dính/màng PE, muốn tư vấn nhanh qua Zalo.

## Trường phân loại bắt buộc trong CRM CSV
- lead_name, company_type, location, source_url, source_channel
- persona: manufacturer | logistics_fulfillment | reseller | packaging_partner | sme_new
- need_signal: hỏi giá | tìm NCC | mua số lượng | đóng gói lỗi | referral
- product_interest: OPP | in_logo | fragile | PE_stretch | carton_adjacent | unknown
- urgency: high/medium/low dựa trên từ khóa “cần gấp”, “báo giá”, “mua số lượng”, deadline giao hàng
- next_action: gọi/Zalo/email/LinkedIn/comment reply

## Offer theo persona
- Manufacturer: “Báo giá theo quy cách + MOQ + lịch giao định kỳ”.
- Logistics/fulfillment: “Combo băng dính OPP + màng PE theo sản lượng đơn/ngày”.
- Reseller: “Bảng giá sỉ + chính sách lấy lại + danh mục SKU”.
- Packaging partner: “Hợp tác referral/cross-sell băng dính & màng PE cho khách carton/bao bì”.
- SME new: “Tư vấn miễn phí chọn đúng loại băng dính/màng PE trong 5 phút”.

## Evidence gate
Không coi là lead hợp lệ nếu thiếu ít nhất 2/4: tên đơn vị, khu vực, tín hiệu nhu cầu, kênh liên hệ. Mỗi vòng outreach phải xuất CSV có persona + next_action; không chỉ ghi cảm tính.

## KPI
- ≥70% lead có persona xác định.
- ≥50% lead có product_interest rõ.
- Reply rate đo theo persona, không gộp chung.
- Sau 7 ngày: loại persona có reply thấp nhất phải đổi hook/offer.
