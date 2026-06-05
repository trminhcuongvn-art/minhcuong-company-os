# BaDiVi — SOP xử lý phản hồi 72h sau đăng Reel/RFQ kit

## Bối cảnh
Heartbeat 00:43 quét canonical bus và local bus Bún. Các task BaDiVi 3 Reel + campaign/RFQ kit đã có RESULT và artifact thật. SmallBizOps/Tarot/Ông Đồ.AI đang freeze. FB comment scrape vẫn có blocker cookie/nick phụ, nhưng không chặn việc launch organic/outreach thủ công.

## Mục tiêu kỹ năng
Biến mọi tương tác sau 3 Reel BaDiVi thành pipeline RFQ có bằng chứng: comment/inbox/Zalo/email → phân loại intent → lấy thông tin tối thiểu → báo giá/đặt lịch → cập nhật CRM CSV.

## Phân loại phản hồi
1. **High intent**: hỏi giá, hỏi sỉ, cần số lượng, hỏi giao hàng, xin báo giá, xin catalogue.
2. **Medium intent**: hỏi loại băng dính/màng PE, hỏi quy cách, hỏi có in logo/dễ vỡ/chống tĩnh điện không.
3. **Low intent**: thả tim, hỏi chung chung, tag bạn bè, xem thêm.
4. **Negative/objection**: chê đắt, so với nhà cung cấp khác, nghi ngờ chất lượng, hỏi MOQ quá thấp.

## Script trả lời nhanh
### High intent
“Dạ BaDiVi có băng dính/màng PE/vật tư đóng gói cho xưởng và shop. Anh/chị cho em xin 3 thông tin để báo đúng giá: loại cần dùng, số lượng/tháng, địa chỉ giao hàng. Nếu cần, em gửi bảng quy cách + mẫu báo giá trong hôm nay.”

### Medium intent
“Dạ bên em có nhiều quy cách theo nhu cầu đóng gói. Anh/chị đang dùng cho thùng carton, hàng dễ vỡ, kho vận hay sản xuất ạ? Em sẽ gợi ý loại phù hợp để tránh mua sai gây bung/thừa chi phí.”

### Objection giá
“Dạ với đơn B2B, giá phụ thuộc độ dày, lõi, chiều dài, số lượng và yêu cầu in logo. Em không chốt một giá chung để tránh sai quy cách. Anh/chị gửi nhu cầu, em báo 2–3 option: tiết kiệm / cân bằng / ổn định chất lượng.”

## Trường CRM bắt buộc
- timestamp
- source_post/reel_id
- channel: FB comment / inbox / Zalo / email / phone
- company/name
- contact
- product_interest
- monthly_volume_estimate
- location
- intent_level
- next_action
- owner
- status: new / contacted / waiting_info / quoted / won / lost
- proof_link_or_screenshot

## SLA xử lý
- High intent: phản hồi trong 15 phút giờ làm việc; ngoài giờ phản hồi trong 12h.
- Medium intent: phản hồi trong 2h.
- Low intent: gom cuối ngày, nuôi bằng catalogue/post follow-up.
- Báo giá: không quá 24h sau khi đủ quy cách/số lượng/giao hàng.

## Evidence gate
Không ghi “lead” nếu không có ít nhất 1 bằng chứng: link comment, ảnh chụp inbox, Zalo message, email, hoặc dòng CRM có contact thật. Không báo campaign hiệu quả chỉ bằng view/like; KPI chính là số RFQ hợp lệ và số báo giá đã gửi.

## KPI 72h
- >= 3 phản hồi high/medium intent được phân loại đúng.
- 100% high intent có next_action rõ.
- 0 lead thiếu proof.
- Tỷ lệ quoted/high-intent là chỉ số ưu tiên hơn view.

## Blocker còn lại
FB automation/scrape comment sâu vẫn cần cookie/nick phụ hợp lệ hoặc live browser ổn định. Khi chưa có, dùng quy trình thủ công + CRM CSV từ campaign kit để không trì hoãn launch.
