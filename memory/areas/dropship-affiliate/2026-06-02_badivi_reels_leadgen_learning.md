# 2026-06-02 — Bún heartbeat learning: tối ưu Reel BaDiVi để kéo lead B2B

## Bối cảnh
Task BaDiVi 3 Reel script đã có RESULT lúc 02:12 với 3 file >1KB trong `/Users/minhcuong/.openclaw/workspace/bun/badivi-reels/`. Heartbeat này không tạo thêm script trùng; chuyển sang nâng skill phục vụ vòng tiếp theo: biến Reel từ “video giới thiệu” thành “máy lọc lead B2B”.

## Khung đánh giá Reel B2B 30–60s
1. **Hook phải là lỗi vận hành, không phải giới thiệu sản phẩm**: “Đơn hoàn vì bung thùng”, “màng PE rách khi quấn pallet”, “băng dính không bám thùng carton tái chế”.
2. **Proof an toàn**: dùng proof dạng quy trình/kiểm tra tại xưởng thay vì claim số liệu chưa có nguồn. Ví dụ: test kéo, test bám dính, test quấn pallet, so sánh sai/chọn đúng theo bề mặt thùng.
3. **Offer cụ thể**: “gửi mẫu băng dính/màng PE theo quy cách”, “tư vấn quy cách theo loại thùng”, “báo giá theo MOQ”.
4. **CTA lọc lead**: yêu cầu comment/inbox theo mã ngắn để phân loại nhu cầu:
   - `BDV-THUNG`: cần băng dính thùng carton
   - `BDV-PE`: cần màng PE quấn pallet
   - `BDV-LOGO`: cần băng dính in logo/cảnh báo
5. **Đầu vào cho lead scoring**: caption nên hỏi 3 thông tin: ngành hàng, sản lượng thùng/pallet mỗi ngày, khu vực. Đây là dữ liệu đủ để chấm điểm lead nóng/lạnh.

## Checklist trước khi render/post
- On-screen text mỗi cảnh <= 9 từ, font lớn, tương phản mạnh.
- 3 giây đầu có visual “lỗi thật” hoặc mô phỏng rõ: thùng bung, kiện móp, pallet lỏng.
- Không dùng claim “giảm hoàn X%/tiết kiệm X%” khi chưa có case study đo được.
- Caption phải có một câu hỏi khiến khách tự khai nhu cầu: “Bạn đang đóng gói thùng carton, pallet hay hàng dễ vỡ?”
- Mỗi Reel gắn UTM riêng nếu đưa về website/Zalo để đo nguồn lead.

## Ý tưởng vòng tiếp theo
- Tạo landing mini `/bang-dinh-thung-carton-hai-phong`, `/mang-pe-quan-pallet`, `/bang-dinh-in-logo` để Reel trỏ về đúng nhu cầu.
- Lập form báo giá 5 trường: tên công ty, sản phẩm cần, kích thước/quy cách, số lượng/tháng, khu vực.
- Sau khi Render xuất video, Bún nên tạo thêm `posting_pack.csv`: title, caption, hashtag, CTA code, landing URL, UTM.

## Postflight guardrail cho Bún
Không báo DONE cho content/video nếu chỉ có ý tưởng. Tối thiểu phải có file thật >1KB, path tuyệt đối, size byte, và nếu là video phải có ffprobe duration/resolution.
