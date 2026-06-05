# 2026-06-04 00:47 — Epoch Ascendant retention & monetization loop skill

## Context
Heartbeat Bún quét canonical bus và local bus: task game `bun_epoch_ascendant_playable_polish_20260604` đã có RESULT DONE lúc 00:27 với `index.html` và `QA_POLISH_20260604.md`. Không có task `to_agent=bun` NEW/IN_PROGRESS khả thi mới sau mốc đó. SmallBizOps/Tarot/Ông Đồ.AI freeze. Theo role reset Henry: Bún tập trung xây dựng game Epoch Ascendant, nên learning này ưu tiên game thay vì BaDiVi.

## Mục tiêu nâng skill
Biến playable MVP từ “chạy được” thành sản phẩm có vòng giữ chân người chơi và có thể test doanh thu nhẹ, không cần backend, không cần mua asset/license, không đụng production.

## Retention loop 7 ngày đề xuất
1. **Run 3 phút**: mỗi lượt chơi kết thúc bằng một kết quả rõ: chết ở wave X, thắng boss, hoặc mở era mới.
2. **Reward sau run**: thưởng `Chrono Shards` theo wave cao nhất + boss kill + thời gian sống sót.
3. **Meta upgrade 1 click**: 3 nhánh ban đầu: Damage, Magnet, Max HP. Mỗi nhánh tăng nhỏ 5-10%, giá tăng tuyến tính để tránh phá game.
4. **Daily objective local-only**: mỗi ngày 3 nhiệm vụ lưu `localStorage`: kill 100 enemies, reach wave 4, collect 30 XP orbs. Reset theo ngày local.
5. **Unlock cảm giác tiến bộ**: mốc level account 3/5/8 mở skin shape/particle màu mới, không ảnh hưởng cân bằng.
6. **Era mastery**: mỗi era có 3 badge: survive, boss, no-death. Badge là mục tiêu sưu tầm để replay.
7. **Next-run promise**: màn kết thúc luôn hiển thị “lượt sau mạnh hơn vì…” + nút restart lớn.

## Monetization test không gây rủi ro
- Giai đoạn prototype chỉ dùng **mock offer** trong UI, không thu tiền thật.
- Offer phù hợp: cosmetic-only “Founder Skin Pack”, hoặc “Support development” placeholder.
- Không bán power ở MVP để tránh pay-to-win và làm bẩn dữ liệu cân bằng.
- Chỉ đo click intent: `mock_offer_view`, `mock_offer_click`, `restart_after_offer` lưu vào localStorage/export JSON.

## Metrics cần thêm vào build tiếp theo
- `runs_total`, `best_wave`, `wins_total`, `avg_run_seconds`.
- `restart_rate_after_death`: người chơi có bấm restart sau thua không.
- `upgrade_purchase_rate`: có tiêu shards hay không.
- `daily_objective_completion`: mục tiêu nào dễ/khó.
- `skill_pick_rate`: skill nào được chọn nhiều, phục vụ cân bằng.

## Implementation checklist cho iteration kế tiếp
1. Thêm object `profile` trong localStorage: shards, upgrades, daily, stats.
2. Thêm end-screen breakdown: XP, shards, best wave, gợi ý nâng cấp.
3. Thêm upgrade panel trước khi start/restart.
4. Thêm daily objective mini-panel trong HUD hoặc pause/end screen.
5. Thêm export debug JSON để Trợ Lý/Henry xem evidence mà không cần backend.
6. Thêm balance guardrail: nếu win rate >70% ở 10 run đầu thì tăng enemy HP wave 4+; nếu <20% thì giảm projectile cooldown hoặc tăng HP pickup.

## Acceptance gate
- File playable vẫn single HTML, không CDN/npm.
- JS syntax pass.
- Có thể reset localStorage để rollback state.
- Có ít nhất 5 metric hiển thị/export được.
- Không claim doanh thu thật, không gọi API thanh toán.

## Rollback
Nếu patch game theo skill này gây lỗi: khôi phục `index.html` từ bản trước hoặc xóa keys localStorage `epochAscendantProfile`, `epochAscendantMetrics`, `epochAscendantDaily`.
