# BaDiVi skill — Distributor onboarding scorecard cho B2B/ASEAN

## Mục tiêu
Chuyển lead từ Reel/Zalo/LinkedIn thành đối tác phân phối có thể lặp đơn, không chỉ lấy RFQ lẻ. Scorecard này dùng trước khi gửi bảng giá sâu hoặc mẫu miễn phí.

## 1) Điều kiện tối thiểu trước khi gọi là “distributor lead”
- Có pháp nhân/cửa hàng/website hoặc bằng chứng đang bán vật tư đóng gói.
- Có thị trường rõ: tỉnh/thành, ngành phục vụ, số khách doanh nghiệp đang chăm.
- Có năng lực mua lặp: tần suất nhập, MOQ kỳ vọng, dòng sản phẩm ưu tiên.
- Có kênh bán/fulfillment: kho, đội sales, Shopee/Lazada/B2B catalogue, hoặc route giao định kỳ.
- Có người quyết định giá/nhập hàng tham gia trao đổi.

Nếu thiếu 2/5 điều kiện: giữ ở trạng thái `LEAD_NURTURE`, chưa gửi discount distributor.

## 2) Scorecard 100 điểm
| Nhóm | Điểm | Cách chấm nhanh |
|---|---:|---|
| Product-fit | 20 | Đang bán/tư vấn thùng carton, màng PE, băng dính, túi, pallet wrap; có khách logistics/SME/e-commerce |
| Buying capacity | 20 | Có MOQ/tháng hoặc ngân sách nhập; biết size/quy cách; có lịch bổ sung hàng |
| Market access | 15 | Có tệp khách B2B, shop online, sales địa phương, hoặc hợp đồng cung ứng |
| Decision speed | 15 | Có owner quyết định, phản hồi <24h, sẵn sàng call/báo giá |
| Compliance/export readiness | 10 | Có thông tin công ty, địa chỉ nhận hàng, điều kiện thanh toán/chứng từ |
| Margin discipline | 10 | Không chỉ hỏi “giá thấp nhất”; chấp nhận tier theo volume và dịch vụ |
| Evidence quality | 10 | Có website/catalogue/ảnh kho/đơn mẫu/đầu mối rõ |

Ngưỡng hành động:
- `80-100`: ưu tiên call + quote 3 tier + đề xuất sample/order thử.
- `60-79`: gửi catalogue + 5 câu hỏi qualification + follow-up 48h.
- `40-59`: nurture bằng case/video/FAQ, chưa gửi giá sâu.
- `<40`: chỉ lưu CRM, không tốn thời gian sales.

## 3) Quy trình onboarding 5 bước
1. **Qualify**: hỏi 5 câu: bán nhóm nào, khách hàng chính, volume/tháng, khu vực, điều kiện giao/hoá đơn.
2. **Map SKU**: chọn 3 SKU starter: băng dính carton, màng PE quấn pallet, thùng/túi theo quy cách phổ biến.
3. **Quote tier**: Good/Better/Best theo MOQ; ghi rõ lead time, phí giao, điều kiện đổi trả/chứng từ.
4. **Trial order**: đơn thử nhỏ nhưng có thanh toán; tránh sample miễn phí nếu score <80.
5. **30-day review**: đo sell-through, reorder intent, phản hồi giá/chất lượng; nếu đạt thì gắn `DISTRIBUTOR_ACTIVE`.

## 4) Field CRM cần thêm
- `partner_type`: reseller / factory buyer / exporter / packaging service / ecommerce seller
- `territory`: tỉnh/quốc gia/khu công nghiệp
- `current_products`: sản phẩm đang bán
- `monthly_volume_estimate`: MOQ hoặc doanh số dự kiến
- `score_total`, `score_breakdown`
- `next_action`: call / quote / sample / nurture / close_lost
- `discount_tier_allowed`: none / bronze / silver / gold
- `evidence_url`: website, catalogue, ảnh kho, social page

## 5) Copy hỏi nhanh qua Zalo/WhatsApp
> Để em gửi đúng bảng giá đại lý, anh/chị cho em 5 thông tin nhanh: khu vực bán chính, nhóm sản phẩm đang bán, volume nhập dự kiến/tháng, khách chính là nhà máy/shop online/logistics, và điều kiện nhận hàng/hoá đơn cần gì ạ?

## 6) Guardrail chống mất biên lợi nhuận
- Không mở “giá đại lý” chỉ vì lead tự xưng đại lý.
- Mỗi quote phải kèm MOQ + lead time + điều kiện thanh toán.
- Discount chỉ mở theo reorder hoặc bằng chứng market access.
- Nếu lead chỉ ép giá nhưng không có volume/evidence: chuyển `NURTURE_PRICE_SHOPPER`.

## 7) KPI 14 ngày
- Distributor-qualified rate = qualified distributor leads / all RFQ leads.
- Quote-to-trial order rate.
- Trial-to-reorder rate.
- Gross margin by tier.
- Response SLA: qualified lead phải có phản hồi trong 4h làm việc.

## Rollback / áp dụng
Đây là note chiến lược local-only, không ghi production, không public dữ liệu. Rollback: xoá file note này và không thêm field CRM tương ứng.
