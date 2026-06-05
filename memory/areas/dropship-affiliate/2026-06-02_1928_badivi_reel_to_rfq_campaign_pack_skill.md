# 2026-06-02 19:28 — BaDiVi Reel → RFQ campaign pack skill

## Context
Heartbeat Bún quét canonical bus + local bus: không có task `to_agent=bun` trạng thái NEW/IN_PROGRESS hợp lệ chưa có RESULT mới hơn. BaDiVi 3 Reel đã có script + render mp4 verify; FB comment scrape vẫn blocker thật do thiếu cookie/nick phụ; SmallBizOps/Tarot/Ông Đồ.AI freeze. Chuyển sang học/nâng skill.

## Mục tiêu skill
Biến 3 Reel BaDiVi đã render thành **campaign pack tạo RFQ B2B** thay vì chỉ đăng video rời rạc.

## Campaign pack tối thiểu
1. **Asset gốc**
   - 3 mp4 Reel 9:16 đã verify.
   - 3 caption theo từng persona: chủ xưởng, mua hàng KCN, seller TMĐT/đại lý bao bì.
   - 3 thumbnail/câu hook text: “Hàng hoàn vì đóng gói?”, “Băng dính rẻ có thật sự rẻ?”, “Checklist đóng gói B2B”.
2. **Offer rõ ràng**
   - Miễn phí tư vấn chọn băng dính/màng PE theo loại hàng.
   - Gửi bảng quy cách + mẫu báo giá trong 24h nếu lead cung cấp 4 thông tin: sản phẩm đóng gói, sản lượng/tháng, kích thước/quy cách, địa điểm giao.
   - Không claim quá mức; mọi giá/MOQ cần Henry/BaDiVi xác nhận trước khi gửi thật.
3. **Tracking**
   - UTM cho từng Reel: `utm_source=facebook_reel`, `utm_campaign=badivi_reel_202606`, `utm_content=reel01|reel02|reel03`.
   - CRM CSV bắt buộc có: timestamp, source, reel_id, name/page, phone/zalo, company, need, volume, location, status, next_followup, owner.
4. **SOP phản hồi comment/DM**
   - Reply công khai ngắn: “Anh/chị inbox BaDiVi gửi mẫu quy cách, hoặc để lại Zalo — bên em tư vấn loại băng dính/màng PE phù hợp hàng của mình.”
   - DM 4 câu hỏi: loại hàng, sản lượng, quy cách, địa điểm giao.
   - SLA: phản hồi lead nóng <2h trong giờ làm việc; follow-up D+1, D+3, D+7.

## Ma trận đo lường
- View 3s, 25%, 50%, 95%.
- Comment/DM per 1.000 view.
- Lead đủ 4 trường / tổng DM.
- RFQ sent / lead đủ dữ liệu.
- Quote-to-order nếu có báo giá thật.

## Evidence gate khi triển khai thật
Không báo DONE chiến dịch nếu thiếu một trong các mục:
- URL/post ID từng Reel đã đăng.
- Screenshot hoặc log số liệu view/engagement.
- CRM CSV có lead rows thật hoặc ghi rõ 0 lead.
- UTM/link/form hoạt động.
- File caption + offer + RFQ template tồn tại >1KB.

## Blocker hiện tại
- Thiếu quyền/cookie để scrape comment FB sâu tự động.
- Thiếu bảng giá/MOQ/spec chính thức để gửi báo giá thật.
- Thiếu xác nhận kênh đăng chính thức và người trực inbox.
