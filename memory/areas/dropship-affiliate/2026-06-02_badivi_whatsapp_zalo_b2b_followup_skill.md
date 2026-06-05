# 2026-06-02 — BaDiVi skill: Zalo/WhatsApp follow-up để chốt lead B2B sau Reel/DM

## Bối cảnh
- Canonical bus + local bun bus: không có task `to_agent=bun` NEW/IN_PROGRESS còn hợp lệ chưa có RESULT mới hơn.
- Task 3 Reel BaDiVi đã DONE và Render đã có 3 MP4 verified 1080x1920.
- FB comment scrape thật vẫn blocker cookie/nick phụ; đã có fallback public-web + top outreach 48 lead.
- SmallBizOps/Tarot/Ông Đồ.AI đang freeze.

## Mục tiêu skill
Biến lead từ Reel/DM/public-web thành cuộc hội thoại Zalo/WhatsApp có đủ dữ liệu báo giá, giảm vòng hỏi đáp và tăng tỷ lệ phản hồi trong 24-72h.

## Nguyên tắc follow-up B2B vật tư đóng gói
1. **Không mở đầu chung chung**: nhắc đúng ngành hoặc pain của khách: đóng hàng TMĐT, carton, kho vận, xưởng in, nhà máy.
2. **Một tin = một mục tiêu**: tin 1 xin thông tin định lượng; tin 2 gửi lựa chọn; tin 3 xin lịch gọi/mẫu.
3. **Hỏi 4 thông tin đủ báo giá**:
   - Loại vật tư: băng dính OPP/in logo/dễ vỡ/màng PE/màng bảo vệ/khác.
   - Quy cách: bản rộng, độ dài, độ dày, màu/in logo nếu có.
   - Sản lượng: số cuộn/tháng hoặc số carton/ngày.
   - Địa điểm giao: tỉnh/KCN/kho + thời gian cần hàng.
4. **Không claim quá đà**: chưa có chứng chỉ/giá/lead time được Henry xác nhận thì ghi “BaDiVi sẽ kiểm tra và báo lại”.
5. **Evidence gate CRM**: mọi lead hợp lệ phải có `source`, `contact`, `need`, `quantity`, `location`, `next_action`, `owner`, `status`.

## Cadence 72 giờ
### T0 — phản hồi đầu tiên trong 5 phút
Template:
> Em chào anh/chị, BaDiVi nhận được nhu cầu về [sản phẩm]. Để báo đúng giá, anh/chị cho em xin 4 thông tin nhanh: loại băng/màng cần dùng, quy cách, sản lượng dự kiến/tháng và địa điểm giao hàng ạ?

### T+4h — nếu chưa trả lời
> Em gửi lại để anh/chị tiện phản hồi: nếu chưa rõ quy cách, anh/chị chỉ cần gửi ảnh cuộn đang dùng hoặc ảnh thùng hàng. BaDiVi sẽ gợi ý loại phù hợp rồi báo giá sau.

### T+24h — chuyển sang offer nhẹ
> Bên em có thể báo 2 phương án: tiết kiệm và ổn định cho đóng gói số lượng lớn. Anh/chị muốn em lên thử phương án theo sản lượng hiện tại không ạ?

### T+72h — đóng vòng lịch sự
> Em xin phép lưu nhu cầu của anh/chị. Khi cần băng dính/màng PE/tem dễ vỡ cho đóng gói, anh/chị nhắn em quy cách hoặc ảnh mẫu, BaDiVi sẽ báo lại nhanh.

## Nhánh xử lý phản đối
- “Đang có nhà cung cấp rồi” → hỏi benchmark: “Anh/chị đang ưu tiên giá, độ bám, độ trong hay giao nhanh? Em có thể báo đối chiếu 1 mã để anh/chị so sánh.”
- “Gửi bảng giá đi” → không gửi bảng chung ngay; hỏi quy cách + sản lượng để tránh báo sai.
- “Số lượng ít” → gợi ý SKU tiêu chuẩn/có sẵn; chưa hứa MOQ nếu chưa xác nhận.
- “Cần in logo” → hỏi file logo, số màu, bản rộng, số lượng, deadline; đánh dấu lead `custom_print`.

## KPI cần đo hằng ngày
- Response time median < 15 phút trong giờ làm.
- Lead đủ 4 thông tin / tổng lead inbound.
- Quote issued / lead đủ thông tin.
- Follow-up completed trong 72h.
- Won/lost reason: giá, MOQ, giao hàng, chất lượng, không phản hồi.

## Checklist triển khai với 48 lead top outreach hiện có
1. Gắn tag segment: domestic/ASEAN/carton/logistics/supplier/competitor.
2. Ưu tiên domestic end-user/carton/logistics trước; competitor chỉ dùng để benchmark, không push bán hàng mạnh.
3. Tạo Google Sheet/CSV CRM với cột chuẩn ở trên.
4. Mỗi lead chỉ gửi 1 tin mở đầu cá nhân hóa; không spam hàng loạt.
5. Sau mỗi ngày, xuất CSV có size >1KB để agent đánh giá thật.
