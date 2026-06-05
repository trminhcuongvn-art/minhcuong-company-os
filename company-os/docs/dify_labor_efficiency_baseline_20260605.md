# Dify Labor Efficiency Baseline — 2026-06-05

## Methodology
So sánh output/giờ trước và sau khi triển khai Dify (Phase 1 live: 05/06 11:34 ICT).

## Pre-Dify baseline (ước tính từ task bus trước 05/06)
- Agent output: chủ yếu manual chat, không có completion gate
- Wrapper adoption: 0% (chưa có wrapper)
- Task visibility: thấp — không đếm được run thật
- Escalation: không có cơ chế chuẩn

## Post-Dify metrics (05/06 11:34 → 16:44 ICT, ~5 tiếng)
| Metric | Value |
|--------|-------|
| Total wrapper runs | 469 |
| DONE runs | 301 (64%) |
| PARTIAL runs | 53 (11%) |
| BLOCKED runs | 14 (3%) |
| Agents active | 5 (Bông, Bún, Trợ Lý, Render, Cáo) |
| Commits hôm nay | 4 (962e73f, e5e3c23, 7185751, 110d75c) |
| Files pushed | 146+ files |
| New tools shipped | Voice STT, output_gate.sh, anti-procrastination cron |

## Agent output breakdown hôm nay
| Agent | Runs | Highlight |
|-------|------|-----------|
| Bông | 135 | fullSKU enrich 8/10 batch (4000/5065 SKU) |
| Bún | 91 | github_top100_ai + dropship_opportunities |
| Trợ Lý | 76 | coordination, escalation routing |
| Render | 56 | heartbeat clips, glowpulse learning |
| Cáo | 36 | Dify Phase 2/3, Voice STT, anti-procrastination |

## Gaps / chưa đo được
- Baseline trước Dify không có số liệu chính xác (không có wrapper)
- Chưa đo latency per task (start → DONE)
- Chưa đo error rate per domain
- Chưa đo Henry time saved (review time)

## Kế hoạch đo tiếp
1. Thêm timestamp vào wrapper log (start_ts + end_ts) → tính duration per task
2. Weekly snapshot mỗi thứ Hai → trend chart
3. Baseline retroactive: ước tính từ git history trước 05/06

## Kết luận sơ bộ
Wrapper adoption 64% DONE trong ngày đầu tiên mandatory = tích cực.
Không có baseline định lượng → chưa thể so sánh % improvement chính xác.
Cần ít nhất 1 tuần data để có trend.
