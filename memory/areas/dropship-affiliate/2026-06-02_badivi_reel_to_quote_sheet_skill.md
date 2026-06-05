# 2026-06-02 — BaDiVi skill: biến Reel/DM thành báo giá B2B có thể chốt

## Bối cảnh
Heartbeat 08:57: quét canonical bus và bus local Bún. Không thấy task `to_agent=bun` trạng thái NEW/IN_PROGRESS chưa có RESULT mới hơn. Task 3 Reel BaDiVi đã DONE, Render đã verify 3 MP4 9:16. FB leadgen comment sâu vẫn có blocker cookie/nick phụ; không dừng rảnh, chuyển sang nâng skill phục vụ BaDiVi.

## Chủ đề học
Kỹ năng chuyển tín hiệu từ Reel/Inbox/lead public web thành **phiếu yêu cầu báo giá** đủ dữ liệu để BaDiVi trả giá nhanh, tránh hỏi qua lại nhiều lần.

## Checklist thông tin tối thiểu trước khi báo giá
1. **Loại sản phẩm**: băng dính OPP trong/đục, băng dính in logo, băng dính cảnh báo/dễ vỡ, màng PE, băng dính 2 mặt, băng dính giấy/kraft.
2. **Quy cách**: khổ rộng, độ dài/cuộn, độ dày hoặc yêu cầu bám dính; với màng PE cần khổ/cuộn/kg/lõi.
3. **Số lượng & tần suất**: đơn test, đơn tháng, hay hợp đồng định kỳ; ghi rõ MOQ mong muốn.
4. **Ứng dụng**: đóng carton TMĐT, kho vận, may mặc, điện tử, thực phẩm, pallet, hàng dễ vỡ.
5. **Địa điểm giao**: tỉnh/thành, khu công nghiệp nếu có, yêu cầu hóa đơn/chứng từ.
6. **Yêu cầu đặc biệt**: in logo, màu, chống tĩnh điện, chịu nhiệt, mẫu thử, thời gian cần hàng.

## Form lead chuẩn đưa vào CRM/CSV
Các cột nên dùng:
`lead_id, source, source_url, created_at, company_or_name, phone, zalo, email, province, segment, product_need, spec_width, spec_length, spec_thickness, quantity, frequency, delivery_location, urgency, decision_role, budget_hint, next_action, status, owner, notes`.

## Kịch bản hỏi nhanh trong inbox
- Câu 1: “Anh/chị đang cần loại nào: băng dính đóng carton, băng dính in logo hay màng PE quấn pallet?”
- Câu 2: “Mình dùng khoảng bao nhiêu cuộn/kg mỗi tháng và giao ở tỉnh nào ạ?”
- Câu 3: “Nếu có ảnh cuộn/thùng đang dùng hoặc quy cách cũ, anh/chị gửi giúp để bên em báo đúng loại, tránh chọn sai gây bung thùng/tốn chi phí.”
- Chốt: “Em tổng hợp quy cách rồi gửi báo giá/mẫu đề xuất trong ngày. Nếu cần, BaDiVi có thể tư vấn loại phù hợp theo mục đích đóng gói.”

## Quy tắc scoring lead
- +3: có số điện thoại/Zalo rõ.
- +3: có nhu cầu sản phẩm cụ thể hoặc hỏi giá.
- +2: có địa điểm giao trong miền Bắc/Hải Phòng/Quảng Ninh/Hải Dương.
- +2: có số lượng/tần suất.
- +1: lead là xưởng/kho/TMĐT/logistics, không phải đối thủ thuần túy.
- Trừ 2: chỉ là nhà cung cấp/đối thủ không có dấu hiệu mua.
Lead >=7 điểm: gọi/Zalo trong 2 giờ làm việc. Lead 4-6 điểm: hỏi thêm 3 thông tin. Lead <4: nurture bằng catalogue/giới thiệu.

## Ứng dụng cho 3 Reel đã render
- Caption nên gắn CTA cụ thể: “Comment ‘BÁO GIÁ’ + loại hàng đang đóng, BaDiVi gửi checklist chọn băng dính/màng PE.”
- Pinned comment dùng form 4 dòng: loại sản phẩm / quy cách / số lượng tháng / tỉnh giao.
- Mỗi comment/inbox phải được chuyển thành quote sheet, không để trôi trong chat.

## Evidence gate
Không báo đã có lead chốt nếu chưa có CSV/CRM row thật. Mọi báo cáo lead cần kèm path CSV >1KB, số row, và ít nhất các cột phone/Zalo hoặc source_url + next_action.
