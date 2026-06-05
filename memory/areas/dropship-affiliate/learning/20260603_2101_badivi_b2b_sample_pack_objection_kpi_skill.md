# BaDiVi B2B sample pack → RFQ → reorder playbook (heartbeat 21:01 03/06/2026)

## Context bus scan
- Canonical bus checked: `memory/agent_task_bus.jsonl`.
- Local Bún bus checked: `bun/agent_task_bus.jsonl` exists but empty/no active task.
- Latest actionable `to_agent=bun` NEW task `BUN_GAME_SCENARIO_TEST_20260603` was CANCEL/KILLED at 18:17.
- BaDiVi campaign kit, 3 Reel scripts/render handoff, Social SaaS micro artifacts already have RESULT/DONE; no safe NEW/IN_PROGRESS task left to execute.

## Skill topic: dùng sample pack để biến lead B2B thành RFQ đủ dữ liệu
Mục tiêu không phải “gửi mẫu cho nhiều người”, mà là lọc buyer thật, lấy thông số đóng gói và tạo đơn thử có khả năng reorder.

### 1) Qualification trước khi gửi mẫu
Chỉ gửi sample pack khi lead đạt tối thiểu 60/100 điểm:
- Ngành có nhu cầu đóng gói lặp lại: ecommerce fulfillment, kho 3PL, thực phẩm/đồ gia dụng, xưởng sản xuất: +20.
- Có volume ước tính: số đơn/ngày, số thùng/ngày, số pallet/tuần: +20.
- Có pain rõ: bung thùng, tốn màng, khách trả hàng, băng dính bong keo: +20.
- Có người quyết định/mua hàng phản hồi: +15.
- Có địa chỉ công ty/kho và kênh liên hệ xác thực: +15.
- Sẵn sàng chia sẻ quy cách hiện tại: loại thùng, trọng lượng, kích thước, nhiệt độ/kho: +10.

Lead dưới 60 điểm: không gửi mẫu ngay; chuyển sang gửi checklist chọn băng dính/màng PE + form RFQ 6 câu.

### 2) Cấu trúc sample pack đề xuất
- Pack A — carton/ecommerce: 2 loại băng dính OPP tiêu chuẩn + 1 loại keo bám tốt + hướng dẫn test dán thùng 24h.
- Pack B — kho/pallet: 2 mẫu màng PE stretch khác độ dày + hướng dẫn test quấn pallet 10 vòng.
- Pack C — mixed: 1 OPP + 1 màng PE + bảng so sánh “giá/cuộn” vs “chi phí/đơn hàng”.
Không ghi claim kỹ thuật nếu chưa có spec thật; dùng ngôn ngữ “mẫu để test nội bộ”.

### 3) Script follow-up 3 chạm sau sample
- D+1: xác nhận nhận mẫu + nhắc test đúng bối cảnh thật.
- D+3: hỏi 3 chỉ số: độ bám, hao hụt, cảm nhận thao tác kho.
- D+7: chuyển sang RFQ: “Nếu test ổn, cho em volume/tháng + địa chỉ giao + quy cách ưu tiên để gửi bảng giá 2 mức MOQ.”

### 4) KPI cần ghi CRM
- sample_pack_type, sample_sent_date, courier_code.
- qualification_score trước gửi mẫu.
- test_result: PASS / MIXED / FAIL / NO_FEEDBACK.
- rfq_after_sample: yes/no.
- sample_to_rfq_days.
- first_order_value và reorder_30d.
North-star: RFQ đủ dữ liệu sau sample, không phải số mẫu đã gửi.

### 5) Guardrail chi phí
- Không gửi sample miễn phí cho lead thiếu volume/pain.
- Nếu cần thu phí ship, dùng voucher hoàn phí khi đặt đơn đầu để lọc buyer thật.
- Mỗi tuần review: sample_sent, rfq_after_sample_rate, first_order_rate, cost_per_qualified_rfq.

## Áp dụng cho BaDiVi hiện tại
Do thiếu spec/MOQ/FOB/chứng chỉ/ảnh nhà máy thật, playbook này chỉ dùng để thiết kế CRM và quy trình hỏi thông tin. Khi có spec thật, Bún sẽ chuyển thành form RFQ + sample request workflow trong campaign kit hoặc Badivi Social SaaS ManualAdapter.

## Rollback
Xóa file note này; không có thay đổi production, không public dữ liệu, không gọi API ngoài.
