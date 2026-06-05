# BaDiVi learning — Post-Reel → RFQ SLA playbook (2026-06-03 02:13)

## Mục tiêu
Biến 3 Reel BaDiVi và campaign/RFQ kit thành quy trình phản hồi lead B2B có SLA rõ, tránh mất lead vì trả lời chậm hoặc thiếu thông tin kỹ thuật.

## Nguyên tắc vận hành
1. **Lead nóng phải phản hồi trong 15 phút**: comment/inbox có từ khóa “báo giá”, “mua”, “sỉ”, “cuộn”, “thùng”, “màng PE”, “in logo” được gắn tag HOT.
2. **Không hỏi lan man**: dùng 5 câu đủ để báo giá sơ bộ: sản phẩm, kích thước/quy cách, số lượng, địa điểm giao, thời gian cần hàng.
3. **Tách 3 luồng**:
   - OPP/băng dính carton: ưu tiên size lõi, bản rộng, độ dài, màu, in logo hay không.
   - Màng PE/stretch film: hỏi khổ, trọng lượng/cuộn, lõi, độ dày nếu khách biết.
   - Khách đại lý/xưởng/logistics: hỏi volume/tháng và khu vực phân phối.
4. **Evidence gate**: mọi lead phải có dòng trong CRM CSV, không chỉ lưu trong inbox.

## SLA đề xuất
| Mức | Tín hiệu | SLA | Hành động |
|---|---|---:|---|
| HOT | hỏi giá/MOQ/số lượng rõ | 15 phút | gửi form RFQ + xin SĐT/Zalo + hẹn báo giá |
| WARM | hỏi chung “có bán không”, “ib” | 2 giờ | hỏi 5 field RFQ tối thiểu |
| COLD | like/share/comment cảm thán | 24 giờ | gửi catalog ngắn + CTA xem bảng quy cách |
| PARTNER | đại lý/xưởng/logistics | 4 giờ | hỏi volume/tháng + đề nghị bảng giá sỉ |

## Script trả lời nhanh
**OPP/carton:**
> Dạ BaDiVi có băng dính đóng carton. Anh/chị cho em xin 5 thông tin để báo giá đúng: bản rộng x độ dài/cuộn, số lượng cần, màu/in logo không, địa chỉ giao, thời gian cần hàng. Nếu gấp, để lại Zalo/SĐT em báo ngay.

**Màng PE:**
> Dạ bên em có màng PE quấn pallet/hàng hóa. Anh/chị cần loại khổ bao nhiêu, trọng lượng hoặc độ dày/cuộn, số lượng dự kiến và địa chỉ giao ở đâu ạ? Em gom thông tin để báo giá nhanh.

**Đại lý/B2B:**
> Dạ nếu anh/chị lấy định kỳ, bên em có thể làm bảng giá theo volume. Cho em xin nhóm sản phẩm cần nhập, sản lượng/tháng, khu vực và yêu cầu hóa đơn/giao hàng để em gửi phương án phù hợp.

## KPI cần đo sau mỗi 72h
- Reel views không phải KPI chính; KPI chính là **RFQ đủ 5 field**.
- Comment/inbox → RFQ complete rate mục tiêu: ≥25%.
- HOT lead first-response time median: <30 phút.
- RFQ → báo giá gửi đi trong 24h: ≥80%.
- Báo giá → đơn thử/meeting: đo riêng theo SKU.

## Checklist trước khi publish Reel
- Caption có CTA cụ thể: “comment BÁO GIÁ + loại sản phẩm” hoặc “inbox quy cách”.
- Link/UTM hoặc mã campaign theo reel: R1_HOANVO, R2_SAIQUYCACH, R3_B2B.
- CRM CSV có cột: campaign_code, lead_source, persona, product_interest, rfq_complete, next_action_at.
- Người trực inbox biết 5 câu RFQ tối thiểu và SLA.

## Blocker còn tồn tại
FB comment scrape tự động vẫn cần cookie/nick phụ hợp lệ. Tuy nhiên quy trình publish + ghi CRM thủ công không bị chặn; có thể launch trước, scrape/automation bổ sung sau.
