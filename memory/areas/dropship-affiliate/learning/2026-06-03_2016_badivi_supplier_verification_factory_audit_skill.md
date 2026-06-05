# BaDiVi — Supplier verification & factory-audit-lite skill (2026-06-03 20:16 ICT)

## Mục tiêu
Khi BaDiVi chạy leadgen/RFQ B2B, rủi ro lớn không chỉ là thiếu khách mà là nhận lead mua sỉ nhưng chưa đủ bằng chứng năng lực cung ứng. Playbook này giúp lọc/chuẩn hoá bằng chứng nhà cung cấp trước khi gửi báo giá hoặc listing Alibaba/Global Sources.

## Checklist bằng chứng tối thiểu trước khi báo giá nghiêm túc
1. **Pháp lý & nhận diện**: tên pháp lý EN/VN, mã số thuế, địa chỉ nhà máy/kho, người phụ trách xuất khẩu, domain/email công ty.
2. **Spec sản phẩm**: loại băng dính/màng PE/túi/bao bì, vật liệu, độ dày, kích thước, màu, lõi, trọng lượng cuộn, dung sai, ảnh sản phẩm thật.
3. **MOQ/FOB/lead time**: MOQ theo SKU, bậc giá theo số lượng, Incoterms, cảng xuất, lead time mẫu/đơn hàng, điều kiện thanh toán.
4. **Chứng chỉ & compliance**: ISO/QC nội bộ, chứng nhận liên quan nếu có, MSDS/COA nếu sản phẩm yêu cầu, chính sách đổi trả lỗi.
5. **Năng lực sản xuất**: số dây chuyền/máy, công suất tháng, ca sản xuất, giới hạn mùa cao điểm, ảnh/video xưởng có timestamp.
6. **QC & đóng gói xuất khẩu**: quy trình kiểm đầu-cuối, AQL mẫu, tiêu chuẩn carton/pallet, nhãn, barcode, chống ẩm/móp.
7. **Trade proof**: invoice/packing list mẫu đã che thông tin nhạy cảm, case ngành tương tự, feedback khách hàng nếu được phép chia sẻ.

## Factory-audit-lite qua online call 20 phút
- 0–3 phút: xác nhận người tham gia, địa chỉ, sản phẩm chính.
- 3–8 phút: đi camera từ biển hiệu/kho/nguyên liệu/sản phẩm hoàn thiện, quay liên tục để giảm rủi ro ảnh cũ.
- 8–13 phút: hỏi công suất, lead time, MOQ, bottleneck; yêu cầu chỉ máy/line thực tế.
- 13–17 phút: xem khu QC, đóng gói, mẫu lỗi, tem nhãn/carton.
- 17–20 phút: chốt bằng chứng cần gửi sau call: bảng giá, spec sheet, ảnh/video, chứng chỉ, packing standard.

## Scoring 100 điểm để nhập CRM/RFQ
- Legal identity: 15
- Product spec completeness: 20
- Pricing/MOQ/lead time clarity: 20
- Capacity proof: 15
- QC/compliance proof: 15
- Export readiness/logistics: 10
- Responsiveness within SLA: 5

Ngưỡng hành động:
- **80–100**: đủ đưa vào shortlist và gửi quote có điều kiện.
- **60–79**: cần bổ sung bằng chứng trước khi chốt đơn lớn; chỉ cho sample/đơn nhỏ.
- **<60**: không dùng cho lead quốc tế; chỉ giữ dạng source dự phòng.

## CRM fields cần thêm
`supplier_score`, `legal_name`, `factory_address_verified`, `moq_confirmed`, `fob_confirmed`, `lead_time_days`, `capacity_month`, `qc_docs_received`, `factory_video_received`, `audit_call_date`, `evidence_folder`, `risk_notes`, `next_action_owner`.

## Ứng dụng cho BaDiVi hiện tại
- Các campaign/Reel đã có thể tạo RFQ nhưng chưa nên claim mạnh về giá/xuất khẩu khi thiếu spec/MOQ/FOB/chứng chỉ.
- Nếu chưa có cookie FB, vẫn chạy outreach thủ công; nhưng mọi lead inbound phải qua form RFQ + supplier evidence gate để không tạo lời hứa quá mức.
- Khi Henry cung cấp spec thật, Bún có thể biến checklist này thành form Google Sheet/CRM và template email yêu cầu bằng chứng.

## Rollback
Đây là note học tập nội bộ, không ghi production/không public dữ liệu. Rollback: xoá file note này và xoá dòng RESULT tương ứng trong bus nếu cần.
