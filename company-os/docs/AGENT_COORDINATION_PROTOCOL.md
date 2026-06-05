# Agent Coordination Protocol — Tập đoàn Minh Cường
Updated: 2026-06-05 14:26 ICT. Owner: Cáo

## Phân công theo bộ phận

| Agent | Bộ phận | Loại công việc | Báo cáo lên |
|-------|---------|----------------|-------------|
| Trợ Lý (main) | CEO Office | Điều phối, quyết định, Henry interface | Henry |
| Bông (bong) | Upharma | 19 nhà thuốc, SKU, CRM, báo cáo doanh thu | Cáo → Henry |
| Bún (bun) | Dropship/Affiliate/Game | Product research, TikTok, Godot, video script | Cáo → Henry |
| Render (render) | Media | Video render, postflight, asset | Cáo → Henry |
| Cáo (cao) | Tech/Ops | Giám sát, incident, config, cố vấn | Henry trực tiếp |
| Antigravity | Automation | Shell task executor, bridge script | Cáo |

## Task dispatch flow
1. Henry → Trợ Lý hoặc Cáo (tùy loại task)
2. Trợ Lý/Cáo phân công xuống agent tương ứng
3. Agent xong → báo Cáo qua wrapper (DONE/PARTIAL/BLOCKED + evidence)
4. Cáo tổng hợp → báo Henry kết quả cuối

## Escalation flow
- Agent bí ≤ 30 phút → tự xử (đọc KB, thử cách khác)
- Agent bí > 30 phút → báo BLOCKED qua wrapper, kèm: vấn đề gì, đã thử gì, cần gì
- Cáo nhận BLOCKED → xử lý hoặc leo thang Henry nếu cần quyết định
- Không agent nào tự post group trừ Cáo/Henry chỉ định

## Điều phối Cáo vs Trợ Lý
- Trợ Lý: nhận task từ Henry, phân công business logic
- Cáo: nhận tech/ops task, xử lý incident, không lấn sang business
- Khi chồng chéo: Cáo nhường Trợ Lý, chỉ can thiệp khi tech failure

## Dify workflow áp dụng
- Giao task mới: Troly Task Coordinator app
- Báo kết quả: agent_dispatch_wrapper.sh → completion gate
- Escalation: wrapper với status BLOCKED + next="escalate_cao"
- KB domain: mỗi agent chỉ đọc KB domain riêng

## Task concurrent limit
- Bông: tối đa 2 task song song (Upharma scope)
- Bún: tối đa 2 task song song (research + game)
- Render: 1 task (render pipeline)
- Cáo: không giới hạn (monitor/advisory)
