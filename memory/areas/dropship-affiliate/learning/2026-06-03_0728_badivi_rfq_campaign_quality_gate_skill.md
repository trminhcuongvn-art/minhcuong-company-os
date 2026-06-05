# BaDiVi RFQ campaign quality gate — học tập heartbeat 07:28 03/06/2026

## Bối cảnh
Campaign kit BaDiVi đã có đủ 3 Reel render thật và bộ RFQ/outreach. Bài học mới là phải dựng **quality gate trước khi publish** để tránh chạy nội dung có video/lead/form không đồng bộ, hoặc đo vanity metric mà không sinh RFQ.

## Quality gate 5 lớp trước publish
1. **Asset gate**: mỗi Reel phải có file mp4 thật >1KB, đúng 9:16, duration 30-60s, caption đọc được trong safe-zone. File nào là draft 320x240 hoặc placeholder phải loại khỏi publish list.
2. **Message gate**: caption, on-screen text, form RFQ và outreach phải dùng cùng một offer. Ví dụ: “nhận tư vấn chọn băng dính/màng PE theo kiện hàng” thì form phải hỏi loại hàng, khối lượng/tháng, lỗi đang gặp, khu vực giao.
3. **UTM/source gate**: mỗi Reel có source_code riêng: reel01_packaging_errors, reel02_wrong_material_cost, reel03_badivi_solution. CRM bắt buộc ghi source_code để biết video nào sinh lead.
4. **RFQ qualification gate**: lead hợp lệ tối thiểu có công ty/ngành, nhu cầu vật tư, sản lượng/tháng hoặc tần suất mua, tỉnh/thành, số điện thoại/Zalo. Comment chỉ hỏi giá nhưng thiếu 2 trường phải đưa vào trạng thái NEED_QUALIFY, chưa tính RFQ.
5. **Follow-up SLA gate**: phản hồi trong 15 phút giờ làm việc; follow-up D+1/D+3/D+7; mọi lần follow-up ghi next_action và outcome vào CRM CSV.

## Checklist publish 72h
- Ngày 0: đăng 3 Reel, pin comment CTA “Bình luận RFQ hoặc inbox để nhận tư vấn quy cách”. Gắn link/form nếu có.
- Giờ 0-6: trả lời comment thủ công bằng canned responses, không spam, không claim quá mức về tiết kiệm chi phí nếu chưa có case study thật.
- Ngày 1: rà CRM, tách lead nóng cần báo giá trong 24h và lead lạnh cần hỏi thêm quy cách.
- Ngày 2-3: so sánh RFQ qualified / 1.000 view, không chỉ nhìn view. Nếu Reel nào view cao nhưng RFQ thấp, đổi CTA/caption trước khi đổi video.

## Ngưỡng đánh giá thực dụng
- PASS: có ít nhất 1 RFQ qualified hoặc 3 lead NEED_QUALIFY trong 72h.
- PARTIAL: có comment/inbox nhưng thiếu thông tin quy cách; cần follow-up script.
- FAIL: chỉ có view/like, không có comment/inbox/RFQ; cần sửa hook 3s hoặc offer.

## Rủi ro và guardrail
- Không tự động scrape FB sâu khi thiếu cookie/nick phụ hợp lệ; dùng nhập CRM thủ công hoặc public-web lead list đã có.
- Không gọi top50 nếu sau dedupe chỉ có 48 lead; ghi đúng số row.
- Không báo DONE nếu artifact chưa tồn tại hoặc dưới 1KB, trừ RFQ spec ngắn nhưng phải đủ schema. Khi spec dưới 1KB nên bổ sung ví dụ trường và validation để vượt evidence gate.

## Việc nên làm tiếp theo
Tạo một `publish_checklist.csv` gồm reel_id, mp4_path, caption_id, utm_source, form_url/source, owner, publish_time, status. File này giúp Trợ Lý/Cáo audit nhanh trước khi Henry cho đăng thật.
