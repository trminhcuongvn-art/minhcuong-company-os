# BaDiVi — Skill: chuyển phản đối B2B thành RFQ đủ dữ liệu (2026-06-03 17:16 ICT)

## Bối cảnh
Heartbeat quét canonical bus và bus local: các task BaDiVi đang mở kiểu NEW/IN_PROGRESS đã có RESULT/DONE sau đó (3 Reel, campaign/RFQ kit, Social SaaS micro). SmallBizOps/Tarot/Ông Đồ.AI đang freeze theo điều phối, nên chuyển sang học/nâng skill phục vụ BaDiVi leadgen.

## Mục tiêu skill
Khi khách B2B phản hồi bằng các câu mơ hồ như “giá sao?”, “có rẻ hơn không?”, “gửi báo giá”, “băng dính loại nào?”, Bún/đội sales không trả lời chung chung mà chuyển thành RFQ đủ thông tin để báo giá nhanh, đo được và lưu CRM.

## 5 nhóm phản đối thường gặp và cách xử lý
1. **Giá cao / hỏi giá ngay**
   - Không tranh luận giá trước.
   - Câu đáp: “Để báo đúng, em xin 4 thông tin: loại băng/màng, khổ x độ dài, số lượng/tháng, địa điểm giao. Nếu anh/chị đang dùng mẫu cũ, gửi ảnh lõi/cuộn là em quy đổi giúp.”
   - Field CRM bắt buộc: product_type, spec, monthly_volume, delivery_location.

2. **Chưa rõ loại sản phẩm**
   - Dùng menu chọn nhanh: OPP trong/đục, băng in logo, băng dễ vỡ, màng PE, băng dính nền, băng 2 mặt, băng giấy/kraft.
   - Câu đáp: “Anh/chị dùng để dán carton, quấn pallet, niêm phong hàng dễ vỡ hay in logo thương hiệu?”

3. **So sánh nhà cung cấp cũ**
   - Tránh claim chưa có proof.
   - Câu đáp: “Bên em có thể benchmark theo mẫu hiện tại: độ bám, độ dày, chiều dài thực, tỷ lệ lỗi khi đóng gói. Anh/chị gửi mẫu/spec đang dùng, em đề xuất phương án tương đương hoặc tối ưu hơn.”
   - Field CRM: current_supplier, current_price_if_shared, pain_point.

4. **Sợ MOQ / đơn thử nhỏ**
   - Câu đáp: “Mình chốt trước nhu cầu dùng/tháng; em tách báo giá 2 mức: đơn test và đơn định kỳ để anh/chị dễ so tổng chi phí.”
   - Field CRM: trial_qty, monthly_qty, reorder_cycle.

5. **Chưa có thời gian trao đổi**
   - Câu đáp: “Em gửi form 1 phút, chỉ cần chọn loại hàng + số lượng + địa chỉ. Có đủ thông tin em trả báo giá trong ngày làm việc.”
   - Field CRM: preferred_contact_time, zalo/phone.

## SLA phản hồi
- Lead nóng có keyword “cần mua/gửi báo giá/đặt hàng”: phản hồi <15 phút trong giờ làm việc.
- Lead hỏi chung “giá sao/loại nào”: phản hồi <2 giờ.
- Lead chưa đủ spec: gửi RFQ mini-form + follow-up sau 24 giờ.

## Evidence gate sau mỗi vòng leadgen
- CSV lead log có ít nhất: timestamp, source, contact, persona, objection_type, RFQ_fields_completed, next_action, owner, status.
- Không ghi DONE nếu chỉ có caption/script mà không có log CRM hoặc artifact >1KB.
- Không tự động nhắn khách nếu chưa có quyền page/token hoặc xác nhận vận hành.

## Câu chốt RFQ mẫu
“Để em báo đúng giá và tránh sai loại băng/màng: anh/chị cho em xin 1) loại dùng, 2) khổ/độ dài hoặc ảnh mẫu, 3) số lượng dự kiến/tháng, 4) địa điểm giao. Có đủ 4 ý em gửi báo giá + phương án test trước.”

## Áp dụng ngay cho BaDiVi
- Gắn vào campaign kit như macro trả lời inbox/comment.
- Gắn vào Social SaaS ManualAdapter: mỗi comment/DM phải qua objection_type -> rfq_required_fields -> next_action.
- North-star KPI: số RFQ đủ 4 field / tổng lead có phản hồi, không dùng view/like làm DONE.
