# BaDiVi skill — B2B export/RFQ document pack để tăng trust và giảm vòng hỏi đáp

## Bối cảnh
Heartbeat 21:46 quét canonical bus và bus local Bún: không có task `to_agent=bun` trạng thái NEW/IN_PROGRESS khả thi chưa xử lý. Các task BaDiVi chính đã có RESULT/DONE: script 3 Reel, campaign/RFQ kit, Social SaaS micro, nhiều playbook leadgen/RFQ. Vì vậy chuyển sang học/nâng skill theo rule heartbeat.

## Mục tiêu skill
Khi lead B2B hỏi về băng dính/bao bì BaDiVi, nếu chỉ trả lời giá sẽ dễ rơi vào vòng hỏi đáp dài. Cần một “document pack” chuẩn để gửi trong 1 lần, giúp buyer đủ dữ liệu mở RFQ, so sánh nhà cung cấp và xin duyệt nội bộ.

## Bộ tài liệu tối thiểu cho RFQ/export
1. **Company one-pager**: năng lực sản xuất, nhóm sản phẩm, thị trường phục vụ, quy trình QA, kênh liên hệ.
2. **Product spec sheet** cho từng SKU/chủng loại: vật liệu, độ dày, chiều rộng/cuộn, chiều dài/cuộn, màu, lõi, đóng gói thùng, ứng dụng, tolerance.
3. **MOQ/lead-time sheet**: MOQ theo SKU, thời gian mẫu, thời gian sản xuất, điều kiện tăng/giảm MOQ, cut-off time xác nhận đơn.
4. **Quote template**: EXW/FOB/CIF nếu có, giá bậc thang theo sản lượng, phí khuôn/thiết lập, phí mẫu, điều kiện thanh toán.
5. **Sample request form**: mục đích dùng, ngành hàng, kích thước cần test, số lượng mẫu, địa chỉ nhận, deadline test.
6. **Compliance/evidence folder**: ảnh nhà máy/dây chuyền, chứng chỉ nếu có, QC checklist, hình đóng gói carton/pallet, batch/lot tracking mẫu.
7. **FAQ buyer objections**: độ bám dính, chịu nhiệt/ẩm, bảo quản, đổi trả lỗi, claim process, thời hạn báo giá.

## Workflow dùng với lead
- Bước 1: lead vào từ Reel/Zalo/email → hỏi 3 câu qualify: sản phẩm cần dán/đóng gói gì, sản lượng/tháng, thị trường giao hàng.
- Bước 2: gửi document pack phù hợp kèm form RFQ ngắn, không gửi toàn bộ catalog nếu lead chưa qualify.
- Bước 3: nếu lead chưa có spec → đề xuất 2–3 cấu hình Good/Better/Best để họ chọn test mẫu.
- Bước 4: sau 24h nhắc bằng checklist “còn thiếu 3 dữ liệu để báo giá chính xác”.
- Bước 5: sau sample test ghi kết quả vào CRM: pass/fail, lý do, reorder potential, next action.

## CRM fields cần thêm
- `doc_pack_sent_at`, `doc_pack_version`, `spec_sheet_sent`, `sample_form_status`, `missing_rfq_fields`, `quote_basis` (EXW/FOB/CIF/manual), `sample_test_deadline`, `buyer_internal_approval_stage`, `next_followup_at`, `evidence_links`.

## KPI đo hiệu quả
- Lead → qualified RFQ: mục tiêu pilot 15–25%.
- Qualified RFQ → sample request: mục tiêu 20–35%.
- Sample request → quote: mục tiêu 50%+ nếu đủ spec.
- Thời gian từ first contact → đủ dữ liệu báo giá: mục tiêu dưới 48h với lead ấm.
- Tỷ lệ vòng hỏi đáp lặp lại do thiếu spec: giảm dần qua mỗi phiên bản document pack.

## Guardrail
Không bịa chứng chỉ, không claim năng lực sản xuất chưa có evidence. Trường nào chưa có dữ liệu thật ghi `TBD/needs factory confirmation`. Không public ảnh/chứng từ nội bộ nếu Henry chưa duyệt. Đây là skill/process; chưa đụng production, chưa gửi khách thật.

## Blocker hiện tại
Thiếu spec/MOQ/FOB/chứng chỉ/ảnh nhà máy thật nên chưa thể biến thành official buyer pack. Tuy nhiên có thể dùng cấu trúc này để chuẩn hóa RFQ thủ công và checklist thu thập dữ liệu từ BaDiVi.
