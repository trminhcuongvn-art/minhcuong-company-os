# 2026-06-02 — BaDiVi: SLA báo giá & follow-up để tăng tỉ lệ chốt B2B

## Bối cảnh
Heartbeat 14:58 quét canonical bus và local bus: các task BaDiVi 3 Reel/script/render đã có RESULT/DONE thật; các task SmallBizOps/Tarot/Ông Đồ.AI đang freeze; FB comment/leadgen thật vẫn phụ thuộc cookie/nick phụ nếu muốn scrape sâu comment. Vì không có task bun NEW/IN_PROGRESS hợp lệ cần chạy lại, chuyển sang học/nâng skill cho BaDiVi.

## Chủ đề học
Thiết kế quy trình SLA báo giá và follow-up sau khi lead đến từ Reel, DM, Zalo, website RFQ hoặc public-web lead. Mục tiêu là tránh mất lead B2B vì phản hồi chậm hoặc thiếu dữ liệu kỹ thuật.

## Playbook SLA đề xuất
1. **0-15 phút sau lead vào**: phản hồi xác nhận đã nhận yêu cầu, xin 4 thông tin tối thiểu: loại sản phẩm, quy cách/kích thước, số lượng dự kiến, địa chỉ/khu vực giao.
2. **15-60 phút**: phân loại lead theo điểm nóng: có đơn gấp, có ảnh mẫu, có định lượng/tháng, là nhà máy/xưởng/kho vận thì ưu tiên cao.
3. **Trong 4 giờ làm việc**: gửi báo giá sơ bộ hoặc hẹn rõ thời điểm trả giá nếu cần kiểm tra tồn/sản xuất/MOQ.
4. **24 giờ**: follow-up lần 1 bằng câu hỏi ngắn: “Em đã gửi báo giá, bên mình muốn chốt loại nào trước để em giữ giá/giao mẫu?”
5. **72 giờ**: follow-up lần 2 kèm offer nhẹ: mẫu thử, tư vấn chọn băng dính/màng PE theo loại thùng, hoặc bảng so sánh tiết kiệm hao hụt.
6. **7 ngày**: đóng trạng thái “cold”, nhưng giữ remark ngành hàng/quy cách để remarketing Reel hoặc broadcast Zalo sau.

## Trường dữ liệu CRM tối thiểu
- lead_id, ngày giờ nhận, nguồn (reel/dm/zalo/web/public-web), UTM/caption nếu có.
- tên công ty/cá nhân, số điện thoại/Zalo, ngành, khu vực.
- sản phẩm quan tâm: OPP tape, băng dính in logo, băng dính dễ vỡ, màng PE, băng dính nền, v.v.
- quy cách, số lượng, tần suất mua, mức gấp.
- trạng thái: new / qualified / quoted / sample_sent / won / lost / cold.
- next_action_at và owner.

## KPI cần đo hằng tuần
- median first-response time.
- % lead đủ 4 thông tin tối thiểu.
- % lead được báo giá trong 4 giờ làm việc.
- quote-to-order conversion.
- lý do lost: giá, MOQ, không đúng quy cách, phản hồi chậm, chỉ hỏi tham khảo.

## Guardrail
Không báo “DONE leadgen” nếu không có file CRM/CSV thật và số dòng thật. Không bịa số conversion khi chưa có tracking. Nếu thiếu cookie FB thì ghi BLOCKER rõ; vẫn có thể làm public-web lead và quy trình xử lý lead nội bộ.

## Next concrete action
Khi có lead mới từ 3 Reel hoặc website, tạo `badivi_quote_pipeline_YYYYMMDD.csv` với các trường trên; sau 7 ngày tổng kết số lead, số quote, số won/lost, và thời gian phản hồi trung vị.
