# BaDiVi skill — RFQ spec sheet template tối thiểu để chốt báo giá B2B/export

## Mục tiêu
Biến lead từ Reel/outreach thành RFQ đủ dữ liệu để sales/nhà máy báo giá trong 1 vòng, không phải hỏi lại nhiều lần. Áp dụng cho băng dính OPP/in logo/dễ vỡ và màng PE.

## 1) Spec sheet cần bắt khách điền
- Loại sản phẩm: OPP trong/đục, in logo, băng dính dễ vỡ, băng dính giấy/vải/điện, màng PE quấn pallet.
- Quy cách: chiều rộng mm, chiều dài m/cuộn, độ dày micron hoặc trọng lượng lõi/cuộn, màu, loại keo nếu biết.
- Nhu cầu sử dụng: đóng thùng carton, e-commerce, kho vận, linh kiện, thực phẩm, xuất khẩu, chống tĩnh điện/chịu nhiệt.
- Sản lượng dự kiến: số cuộn/tháng hoặc thùng/tháng; đơn thử đầu; kế hoạch mua lặp.
- Yêu cầu in: số màu, logo file, vị trí in, yêu cầu proof mẫu.
- Điều kiện giao: địa chỉ nhận, thời gian cần hàng, nội địa hay FOB/CIF, yêu cầu hóa đơn/chứng từ.
- Tiêu chí quyết định: giá, độ dính, độ bền, thời gian giao, công nợ, mẫu thử, chứng chỉ.

## 2) Scoring RFQ để ưu tiên phản hồi
- A — Báo giá ngay: có loại sản phẩm + quy cách + sản lượng + địa chỉ + deadline; phản hồi SLA <2 giờ.
- B — Cần hỏi thêm 1 lần: thiếu 1-2 trường chính; gửi form ngắn + đề xuất 2 quy cách phổ biến.
- C — Lead thăm dò: chỉ hỏi giá chung/không có sản lượng; gửi catalog + MOQ dự kiến + xin use case.
- D — Không phù hợp: yêu cầu quá nhỏ hoặc ngoài danh mục; lưu CRM, không tốn thời gian báo chi tiết.

## 3) Template phản hồi nhanh
### Nội địa
Chào anh/chị, để BaDiVi báo giá đúng loại băng dính/màng PE và tránh sai quy cách, anh/chị gửi giúp 5 thông tin: loại sản phẩm, quy cách, số lượng/tháng, địa chỉ giao, thời gian cần hàng. Nếu chưa rõ quy cách, BaDiVi có thể gợi ý 2-3 cấu hình phổ biến theo mục đích đóng gói của anh/chị.

### Export/ASEAN
Hi, to quote accurately, please share product type, roll width/length/thickness, monthly quantity, delivery term/address, and target delivery date. If specifications are not fixed, BaDiVi can suggest common packaging tape/stretch film configurations for your use case.

## 4) Evidence gate khi chạy thật
- Mỗi RFQ phải có CRM row: source, UTM/reel, contact, product_type, spec_status, volume_status, score A/B/C/D, next_action, owner, timestamp.
- Không báo DONE campaign nếu không có file CRM cập nhật hoặc screenshot/message/log minh chứng.
- Nếu thiếu spec/MOQ/FOB/chứng chỉ/ảnh nhà máy: ghi BLOCKED_FIELD, không bịa claim.

## 5) Rollback/guardrail
Đây là checklist nội bộ, không đụng production, không gửi khách tự động, không public dữ liệu. Rollback: xóa file note này.
