# BaDiVi RFQ form conversion copy — skill note (2026-06-03 18:46)

## Bối cảnh
Heartbeat Bún quét canonical bus + local bus: task NEW gần nhất `BUN_GAME_SCENARIO_TEST_20260603` đã bị Cáo CANCEL/KILLED lúc 18:17 do Henry tag nhầm, không thực thi. Các task BaDiVi chính đã có RESULT: 3 Reel render, campaign/RFQ kit, Social SaaS micro. Vì không còn task hợp lệ chưa xử lý, chuyển sang học/nâng skill theo rule heartbeat.

## Mục tiêu học
Tăng tỷ lệ chuyển từ người xem Reel / lead outreach sang RFQ đủ dữ liệu, không phụ thuộc cookie Facebook. Trọng tâm là copy + cấu trúc form báo giá cho khách B2B bao bì: băng dính, màng PE, vật tư đóng gói.

## Nguyên tắc form RFQ B2B
1. Hỏi ít nhưng đủ để báo giá được: loại sản phẩm, quy cách, sản lượng/tháng, địa điểm giao, thời gian cần hàng.
2. Không bắt khách biết thuật ngữ kỹ thuật: dùng ví dụ dễ hiểu như “màng PE quấn pallet 50cm”, “băng dính trong/đục/in logo”.
3. Tách trường bắt buộc và tuỳ chọn: bắt buộc chỉ 5–6 field, còn chứng chỉ/ảnh mẫu/MOQ để tuỳ chọn.
4. Copy phải hứa kết quả rõ: “nhận checklist báo giá trong 24h”, không hứa giá rẻ nhất nếu chưa có dữ liệu FOB/MOQ thật.
5. Gắn evidence gate: mỗi RFQ phải có source_url/source_reel/source_utm và trạng thái `rfq_qualified` trước khi tính lead thật.

## Cấu trúc RFQ form đề xuất
- Field 1: Tên công ty / người phụ trách.
- Field 2: Kênh liên hệ ưu tiên: Zalo / email / phone.
- Field 3: Nhóm sản phẩm cần báo giá: băng dính, màng PE, dây đai, combo đóng gói.
- Field 4: Quy cách hiện dùng hoặc ảnh mẫu: placeholder hướng dẫn “VD: băng dính 48mm x 100y, màng PE 50cm x 2.4kg”.
- Field 5: Sản lượng dự kiến mỗi tháng: <100, 100–500, 500–2000, >2000 cuộn/thùng.
- Field 6: Tỉnh/thành giao hàng và deadline cần hàng.
- Field tuỳ chọn: vấn đề hiện tại: hàng bung, móp hộp, chi phí hoàn hàng, thiếu ổn định nhà cung cấp.

## Copy CTA ngắn cho Reel
- “Comment RFQ để nhận checklist báo giá theo đúng quy cách kho của bạn.”
- “Muốn biết đang mất bao nhiêu tiền vì đóng gói sai? Gửi quy cách hiện dùng, BaDiVi tính lại phương án.”
- “Có ảnh mẫu băng dính/màng PE đang dùng? Gửi qua Zalo, nhận đề xuất thay thế trong 24h.”

## Chấm điểm RFQ quality
- 0 điểm: chỉ hỏi “giá bao nhiêu” không có quy cách/số lượng.
- 1 điểm: có sản phẩm + kênh liên hệ.
- 2 điểm: có quy cách hoặc ảnh mẫu.
- 3 điểm: có sản lượng/tháng + địa điểm giao.
- 4 điểm: có deadline + pain point kinh doanh.
- 5 điểm: đủ để báo giá 3-tier Good/Better/Best.

## Handoff áp dụng vào kit hiện có
- Bổ sung các field trên vào `rfq_form_spec.md` khi deploy form thật.
- Bổ sung cột `rfq_quality_score`, `source_reel`, `source_utm`, `pain_point`, `next_followup_at` vào CRM CSV.
- Khi chưa có FB cookie, vẫn chạy được bằng Zalo OA/manual form/email outreach.

## Blocker thật
- Chưa có spec/MOQ/FOB/chứng chỉ/ảnh nhà máy xác nhận nên chỉ dừng ở form/copy/qualification; chưa gửi báo giá thật.
- Chưa có FB cookie/nick phụ nên không scrape/comment-auto; không chặn RFQ thủ công.

## Rollback
Xoá note này nếu không dùng: `rm /Users/minhcuong/.openclaw/workspace/memory/areas/dropship-affiliate/learning/2026-06-03_1846_badivi_rfq_form_conversion_copy_skill.md`.
