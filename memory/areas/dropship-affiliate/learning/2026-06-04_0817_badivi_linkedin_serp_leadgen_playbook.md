# 2026-06-04 08:17 — BaDiVi LinkedIn/SERP leadgen playbook (không cần cookie FB)

## Lý do chọn chủ đề
FB comment scrape vẫn bị blocker cookie/nick phụ, nên kênh leadgen rủi ro thấp nhất hiện tại là OSINT công khai: Google/SERP, LinkedIn public profile/company page, website doanh nghiệp, danh bạ xuất nhập khẩu công khai. Mục tiêu là tạo RFQ qualified lead cho BaDiVi mà không cần đăng nhập hoặc đụng dữ liệu riêng tư.

## AI First checklist
- Tốn tiền/license: Không.
- Ghi/xoá production/dữ liệu thật: Không, chỉ tạo note playbook.
- Khó đảo ngược: Không, rollback xoá file này + dòng RESULT bus.
- Public dữ liệu nội bộ: Không.
=> Tự làm ngay.

## Quy trình 5 bước
1. **Define ICP**: doanh nghiệp e-commerce fulfillment, xưởng thực phẩm/đồ uống, kho 3PL, nhà máy linh kiện, nhà phân phối cần đóng thùng/pallet.
2. **SERP query set**: dùng truy vấn `site:.vn "đóng gói" "kho"`, `"màng PE" "pallet"`, `"băng dính" "carton" "nhà máy"`, `"fulfillment" "Việt Nam"`, `"3PL" "kho" "Hải Phòng"`.
3. **Lead fields tối thiểu**: company, website/source URL, ngành, tín hiệu nhu cầu, người liên hệ công khai nếu có, kênh outreach, note cá nhân hoá, UTM/source.
4. **Scoring 100 điểm**: nhu cầu đóng gói rõ 30; quy mô/kho/nhà máy 20; có contact công khai 20; fit sản phẩm BaDiVi 20; tín hiệu gần đây 10.
5. **Outreach 4 chạm**: ngày 0 email/Zalo giới thiệu ngắn; ngày 2 gửi checklist giảm lỗi đóng gói; ngày 5 hỏi mẫu báo giá; ngày 10 case-style follow-up không bịa số liệu.

## Template copy ngắn
Subject: Gợi ý giảm lỗi đóng gói/carton cho {{company}}

Chào anh/chị {{name}}, em thấy {{company}} có hoạt động {{signal}} nên có thể phát sinh nhu cầu băng dính/màng PE cho thùng/pallet. BaDiVi hỗ trợ chuẩn hoá vật tư đóng gói B2B theo nhu cầu kho/xưởng. Nếu anh/chị đang cần so sánh định mức hoặc lấy báo giá, em xin gửi form 4 thông tin: loại hàng, quy cách thùng/pallet, sản lượng/tháng, địa điểm giao.

## Evidence gate cho lần chạy thật
- CSV lead phải có ≥20 dòng, mỗi dòng có source_url công khai.
- Không ghi DONE nếu thiếu nguồn hoặc chỉ là tên công ty không kiểm chứng.
- Không scrape sau login/không dùng cookie cá nhân nếu chưa được cấp.
- Kết quả đo: số outreach đã gửi, số reply, số RFQ đủ 4 field, ngày follow-up tiếp theo.

## Rollback
Xoá file note này và xoá/đánh dấu ignore RESULT tương ứng trong `memory/agent_task_bus.jsonl`.
