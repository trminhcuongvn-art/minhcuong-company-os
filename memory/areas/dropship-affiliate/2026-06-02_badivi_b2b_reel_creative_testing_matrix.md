# 2026-06-02 — BaDiVi skill: ma trận A/B test creative Reel B2B → lead thật

## Bối cảnh
Heartbeat 09:42 quét bus: các task BaDiVi 3 Reel script/render đã có RESULT/DONE và file mp4 thật; Facebook comment scrape vẫn blocker nếu thiếu cookie/nick phụ; SmallBizOps/Tarot/Ông Đồ.AI đang freeze theo rule hiện tại. Vì không có task BaDiVi NEW/IN_PROGRESS cần xử lý ngay, Bún chuyển sang học/nâng skill.

## Mục tiêu skill
Biến 3 Reel BaDiVi hiện có thành vòng test có số đo, thay vì chỉ đăng video. Với B2B băng dính/màng PE, creative tốt phải kéo được 1 trong 3 tín hiệu: comment hỏi giá, inbox gửi quy cách, hoặc click form báo giá.

## Ma trận test 7 ngày
### Trục A — Hook 3 giây đầu
1. **Lỗi/thiệt hại:** “Đóng gói sai, hàng trả về còn tốn hơn cuộn băng dính.”
2. **Checklist:** “3 điểm kiểm tra trước khi gửi hàng số lượng lớn.”
3. **So sánh:** “Băng dính rẻ vs băng dính đúng quy cách khác nhau ở đâu?”
4. **Tình huống xưởng/kho:** “Nếu mỗi ngày đóng 500–2.000 kiện, đừng chọn theo cảm tính.”

### Trục B — CTA
1. Comment keyword: `BAOGIA` để nhận checklist quy cách.
2. Inbox: gửi ảnh kiện hàng + số lượng kiện/ngày để tư vấn.
3. Link form: điền chiều rộng, độ dày, số lượng, ngành hàng.

### Trục C — Offer mềm
1. Checklist chọn băng dính/màng PE cho kho.
2. Mẫu phiếu yêu cầu báo giá 5 dòng.
3. Tư vấn quy cách theo ngành: TMĐT, carton, linh kiện, kho vận.

## Setup đo lường tối thiểu
- Mỗi Reel dùng UTM riêng: `utm_source=fb_reel&utm_medium=organic&utm_campaign=badivi_reel_test_202606&utm_content=reel01_hook_loss`.
- CRM CSV cần cột: `date, source, reel_id, hook_variant, cta_variant, name, phone, company, province, product_need, qty_estimate, status, next_action`.
- Không tính “view” là lead. Lead hợp lệ tối thiểu phải có 1 trong: số điện thoại, inbox có nhu cầu/quy cách, hoặc form có company/province/product.

## KPI nghiệm thu
- 7 ngày đầu: mỗi Reel tối thiểu 2 biến thể caption/hook.
- Tỷ lệ comment/inbox/click mục tiêu ban đầu: 1–3% trên người xem engaged, chưa dùng làm cam kết doanh số.
- Lead hợp lệ: >=10 lead/tuần từ organic + DM là đạt tín hiệu ban đầu; <5 lead thì đổi hook/CTA trước khi tăng ngân sách.
- Tỷ lệ phản hồi báo giá: đo `quote_sent / qualified_lead`, không đo bằng cảm tính.

## Checklist đăng Reel
1. Caption 2 dòng đầu phải có vấn đề cụ thể + ngành hàng.
2. Pin comment CTA: “Comment BAOGIA + ngành hàng, BaDiVi gửi checklist quy cách.”
3. Reply comment trong 15 phút đầu bằng câu hỏi qualify: “Anh/chị đóng khoảng bao nhiêu kiện/ngày và dùng băng dính/màng PE loại nào?”
4. Mọi inbox phải chuyển vào CSV trong ngày; không để lead nằm trong Messenger/Zalo.
5. Sau 24h, ghi lại hook nào tạo nhiều comment/inbox nhất để render phiên bản mới.

## Rủi ro & guardrail
- Không claim giảm hoàn/vỡ bằng % nếu chưa có case thật.
- Không dùng hình ảnh nhà xưởng/khách hàng nếu chưa có quyền.
- Nếu chạy ads, chỉ boost biến thể đã có tín hiệu organic; không boost video chỉ đẹp nhưng không có lead.

## Hành động đề xuất tiếp theo
1. Gắn mã `reel_id` cho 3 mp4 hiện có: R01-loss, R02-wrong-spec, R03-solution.
2. Tạo 6 caption A/B và 3 pinned comment mẫu.
3. Chuẩn bị Google Sheet/CSV lead intake theo schema trên.
4. Sau 7 ngày, merge dữ liệu với `badivi_top50_outreach_20260601.csv` để phân biệt lead nội địa, ASEAN, đối thủ/đại lý.
