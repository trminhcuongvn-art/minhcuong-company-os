# 2026-06-02 — BaDiVi skill: Lead scoring + ưu tiên RFQ B2B sau Reel/DM

## Mục tiêu
Sau khi 3 Reel BaDiVi đã có script/render, bước tiếp theo không phải “đăng cho vui” mà là biến mọi tín hiệu từ Reel/DM/Zalo/website thành danh sách lead có điểm ưu tiên để sales gọi đúng người trước. Chủ đề học heartbeat này: thiết kế hệ lead scoring/RFQ prioritization đơn giản, đo được, dùng ngay cho BaDiVi.

## Nguyên tắc evidence gate
- Không tính là lead hợp lệ nếu thiếu tối thiểu: tên công ty/cá nhân kinh doanh, ngành hàng, nhu cầu đóng gói, kênh liên hệ.
- Không báo “đã có khách” chỉ vì có like/comment chung chung; phải có dòng CRM CSV hoặc form RFQ thật.
- Mỗi lead phải có source: reel_01/reel_02/reel_03, Zalo, website, LinkedIn, email, hoặc public-web.
- Mọi follow-up phải lưu timestamp, trạng thái, next action.

## Lead score 100 điểm
1. Nhu cầu rõ ràng — 30đ
   - Có loại sản phẩm cần đóng gói: +10
   - Có vật tư quan tâm: băng dính/màng PE/thùng/carton/phụ kiện: +10
   - Có vấn đề đau cụ thể: hoàn vỡ, chi phí đóng gói cao, giao hàng lỗi, thiếu nhà cung cấp ổn định: +10

2. Quy mô & tần suất — 25đ
   - Có sản lượng/tháng hoặc số đơn/ngày: +10
   - B2B/xưởng/kho/shop online có đơn đều: +10
   - Có nhu cầu lặp lại, không phải mua lẻ một lần: +5

3. Khả năng chốt — 20đ
   - Có deadline cần báo giá/giao hàng: +8
   - Có ngân sách hoặc đang dùng nhà cung cấp hiện tại: +6
   - Người liên hệ có quyền mua hoặc ảnh hưởng mua: +6

4. Dữ liệu liên hệ — 15đ
   - Có số điện thoại/Zalo: +7
   - Có email/công ty/website/fanpage: +4
   - Có địa chỉ giao/ tỉnh thành: +4

5. Tín hiệu từ nội dung — 10đ
   - Comment/inbox bằng từ khóa “báo giá”, “tư vấn”, “màng PE”, “băng dính”, “đóng gói”: +6
   - Xem/ tương tác nhiều hơn 1 Reel hoặc phản hồi follow-up: +4

## Phân tầng xử lý
- A: 75–100 điểm — gọi/Zalo trong 2 giờ làm việc, tạo phiếu RFQ ngay.
- B: 50–74 điểm — nhắn qualification 4 câu, follow-up trong 24h.
- C: 25–49 điểm — nuôi bằng catalogue/bảng câu hỏi, follow-up 72h.
- D: <25 điểm — chỉ lưu remark, không tốn thời gian sales trừ khi tự phản hồi thêm.

## RFQ tối thiểu cần lấy
1. Anh/chị đang đóng gói mặt hàng gì?
2. Mỗi ngày/tháng khoảng bao nhiêu đơn hoặc dùng bao nhiêu cuộn/thùng?
3. Cần loại vật tư nào: băng dính, màng PE, thùng carton, túi, phụ kiện?
4. Giao ở tỉnh/thành nào và cần hàng khi nào?
5. Có mẫu/nhà cung cấp hiện tại để BaDiVi so sánh không?

## Cột CRM CSV đề xuất
lead_id, created_at, source, reel_id, name, company, segment, province, phone_zalo, email, need_product, volume_estimate, pain_point, urgency, current_supplier, score, tier, status, next_action_at, owner, last_touch_at, evidence_url, notes

## KPI cần xem mỗi tuần
- Số lead hợp lệ / 1.000 views theo từng Reel.
- Tỷ lệ lead A+B trên tổng lead.
- Thời gian phản hồi trung vị với lead A.
- Tỷ lệ RFQ hoàn chỉnh / lead hợp lệ.
- Tỷ lệ báo giá gửi đi / RFQ hoàn chỉnh.
- Tỷ lệ phản hồi sau báo giá.

## Ứng dụng với 3 Reel hiện có
- Reel 01 “3 lỗi đóng gói khiến hàng hoàn/vỡ”: ưu tiên lead có pain hoàn vỡ, hàng dễ bể, shop online, fulfillment.
- Reel 02 “chọn sai băng dính/màng co mất tiền”: ưu tiên lead hỏi vật tư cụ thể, đang so sánh chi phí.
- Reel 03 “BaDiVi giải pháp đóng gói doanh nghiệp”: ưu tiên lead doanh nghiệp cần combo nhiều vật tư hoặc supplier ổn định.

## Blocker/guardrail
FB leadgen/comment scrape vẫn cần cookie/nick phụ nếu muốn tự động lấy comment/inbox từ Facebook. Không được tuyên bố đã scrape FB nếu chưa có cookie và file output thật. Fallback hiện tại: nhập tay từ DM/Zalo/form hoặc public-web CSV.
