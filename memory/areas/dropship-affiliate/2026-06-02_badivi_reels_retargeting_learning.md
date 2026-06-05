# 2026-06-02 — BaDiVi Reel retargeting & comment-to-lead playbook

## Bối cảnh
Heartbeat 04:26 quét canonical bus và local bus: không thấy task `to_agent=bun` NEW/IN_PROGRESS chưa có RESULT mới hơn. BaDiVi 3 Reel script đã DONE, Render đã xuất 3 mp4 9:16. Vì vậy Bún chuyển sang học/nâng skill theo rule.

## Chủ đề học: biến 3 Reel BaDiVi thành chiến dịch retargeting tạo lead B2B

### 1) Mục tiêu phễu
- Reel 1 (3 lỗi đóng gói): dùng để kéo awareness từ nhóm chủ shop/kho vận/e-commerce.
- Reel 2 (chọn sai băng dính/màng PE): dùng để educate và lọc lead có pain rõ.
- Reel 3 (BaDiVi giải pháp): dùng làm warm retargeting + CTA xin báo giá.

### 2) Cấu trúc đo lường bắt buộc
Mỗi video cần một mã UTM riêng:
- `utm_source=facebook_reel`
- `utm_medium=organic_or_boost`
- `utm_campaign=badivi_reels_202606`
- `utm_content=reel01_pain`, `reel02_cost`, `reel03_solution`

Nếu chưa có landing form: dùng Zalo/phone CTA nhưng vẫn ghi `content_code` trong caption để nhân sự nhập tay vào CRM/Sheet.
Ví dụ: “Nhắn Zalo mã BDV01 để nhận checklist đóng gói”.

### 3) Comment-to-lead checklist
Khi đăng Reel, người vận hành cần xuất/ghi các tín hiệu sau:
- Comment có từ khóa: “giá”, “báo giá”, “màng PE”, “băng dính”, “carton”, “số lượng”, “xưởng”, “kho”, “Hải Phòng”.
- Profile là shop/xưởng/kho/logistics/đại lý bao bì: ưu tiên cao.
- Comment hỏi kỹ thuật/quy cách/MOQ: ưu tiên rất cao.
- Comment chỉ khen/chấm/dạo: không push bán ngay, đưa vào warm audience.

### 4) Reply template ngắn
- Comment hỏi giá: “Dạ bên em có băng dính/màng PE theo quy cách doanh nghiệp. Anh/chị cho em xin loại hàng + số lượng/tháng, BaDiVi gửi báo giá nhanh ạ.”
- Comment hỏi quy cách: “Dạ mình đang dùng carton/kho hàng loại nào ạ? BaDiVi tư vấn độ dày/khổ cuộn để tránh bung kiện và tối ưu chi phí.”
- Comment chung: “Em gửi checklist 3 lỗi đóng gói thường gặp cho mình tham khảo nhé. Nếu cần báo giá băng dính/màng PE, nhắn mã BDV01 ạ.”

### 5) Guardrail tránh spam
- Không inbox hàng loạt nếu chưa có tín hiệu mua.
- Không claim số liệu tiết kiệm/vỡ hàng nếu chưa có case study thật.
- Không scrape trái phép group kín; dùng public web/FB session hợp lệ, thao tác chậm, ưu tiên lead tự để lại tín hiệu.

### 6) Output nên làm tiếp
- Tạo Google Sheet/CSV `badivi_reel_leads_YYYYMMDD.csv` với columns: date, reel_code, platform, name, url, comment_text, keyword_hit, segment, priority_score, next_action, owner, status.
- Sau 7 ngày, đo: views, comments, keyword leads, qualified leads, quote requests, orders.

## Kết luận
BaDiVi không nên chỉ “đăng video”; phải gắn từng Reel với mã đo lường + reply script + sheet lead. Ưu tiên tuần đầu: đăng 3 Reel, pin comment CTA, ghi lead thủ công/CSV, sau đó mới tự động hóa sâu hơn.
