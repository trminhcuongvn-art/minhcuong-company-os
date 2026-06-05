# AREA: Dropship & Affiliate (BÚN / Xentric)

## Phạm vi
Nghiên cứu sản phẩm, phân tích NCC (AliExpress/CJDropshipping/Spocket), xu hướng thị trường, affiliate tracking.

## TRẠNG THÁI THỰC TẾ (cập nhật 2026-06-02)
✅ Thông tin cũ “workspace `bun/` chỉ có .gitkeep/chưa có output” đã HỦY. Hiện đã có output thật cho BaDiVi leadgen/reels, Tarot research/plan, và Badivi Social SaaS skeleton. Xem `memory/areas/dropship-affiliate/2026-06-02.md` và các file theo timestamp.

## Template đầu bài research (chuẩn dispatch S1)
- Mục tiêu: (vd: tìm 10 SP trending niche X có margin ≥40%)
- Input: niche/budget/thị trường mục tiêu
- Tiêu chí nghiệm thu: bảng SP + giá NCC + giá bán đề xuất + margin + nguồn
- Định dạng output: bảng markdown/CSV
- Deadline

## Log
- 2026-06-01: Tạo stub. Chờ đầu bài đầu tiên.

## 2026-06-01 23:12 ICT — SmallBizOps Day2 quick win
- Trợ Lý scan task bus ca 23:00, chọn SmallBizOps/Ông Đồ.AI traffic+tracking là TOP1.
- Evidence live: `https://trminhcuongvn-art.github.io/smallbizops/` HTTP 200; `viet-nhanh.html` HTTP 200.
- Đã thêm SEO crawl assets: `sitemap.xml`, `robots.txt`; commit/push `fdc6fdb` vào repo `smallbizops`.
- Dispatch Bún tiếp tục harden tracking/content funnel, deadline 2026-06-02 01:00, checkpoint 00:15, phải báo Cáo qua A2A.

## 2026-06-03 17:30 ICT — Daily checkpoint SmallBiz Ops + Tarot
- SmallBiz Ops / Badivi Social SaaS: PARTIAL. Evidence mới nhất: `bun/badivi-social-saas/docs/queue_state_machine_platform_adapter_spec_20260603_1631.md` (4,057 bytes, 16:32), `poc/src/content_queue_state_machine.py` (3,603 bytes), `logs/state_machine_smoke_20260603.txt` (590 bytes), `schema_20260603.sql` (1,108 bytes). Hôm nay tạo spec queue/state machine + adapter interface + smoke/audit log; chưa có UI/API chạy production.
- Tarot / ArcanaAI: PARTIAL. Evidence mới nhất: `bun/tarot/js/app.js` (12,900 bytes, 08:31), `bun/tarot/logs_arcana_history_test_20260603.log` (538 bytes, 08:32), `dropship/tarot/research_arcana_ai_20260603.md` (4,902 bytes, 00:26). Hôm nay có artifact app/history test + research; thiếu evidence deploy/public URL/commit mới.

## 2026-06-04 13:09 ICT — Epoch Ascendant focus-to-clear delta
- Status: PARTIAL, task `bun_epoch_ascendant_clear_to_done_20260604_1200`.
- Evidence: `/Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/EPOCH_CLEAR_DELTA_1309.md` (2272B), runtime log `Logs/runtime_playtest/epoch_clear_input_cdp_20260604_1309.log` (3872B), frame `epoch_clear_gameplay_7_1780553548373.png` (24918B).
- Metrics: 6 skills, Mammoth boss, Bronze transition, 8 visible enemies, WebGL build succeeded/0 errors; runtime retry 8 frames + 6 input events; `instanceReady=false` so not DONE.
- Rollback: remove/revert files after 12:00 under `bun/epoch-ascendant-unity` listed in delta report.

## 2026-06-04 19:14 ICT — Epoch Ascendant heartbeat delta
- Status: PARTIAL (delta-only after 19:10).
- Evidence: `/Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/epoch_ascendant_clear_1910/index.html` (4001B), `evidence/metrics.json`, 8 PNG frames unique_md5=8.
- Features covered: visible combat loop, camera/hero/enemy labels, 6 skills, Mammoth King boss, Bronze transition MVP, input mapping WASD/Shift/Space/6.
- Blocker: local Chrome screenshot runtime broken due missing Google Chrome Framework; see `epoch_ascendant_clear_1910/evidence/chrome.err`.

## 2026-06-04 21:10 ICT — Epoch Ascendant heartbeat delta after 19:40
- Task: bun_epoch_ascendant_clear_to_done_20260604_1200 / focus-to-clear runtime live capture retry.
- Status: BLOCKED for Unity WebGL live Chrome capture after 19:40; earlier DONE artifacts remain on bus, but this heartbeat reports delta-only.
- Evidence: /Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/EPOCH_CLEAR_DELTA_1940.md (1721 bytes); Logs/runtime_playtest/epoch_clear_1940/chrome.log (11713 bytes); chrome_9223.log (11085 bytes); capture_error.log (264 bytes); instanceReady.txt (81 bytes).
- Metrics: instanceReady=false; frames=0; unique_md5=0; CDP input attempted (WASD, Digit1-6, Space) but Page.enable/Page.captureScreenshot hung; Chrome GPU/WebGL log shows transient GPU command buffer failure and CVDisplayLinkCreateWithCGDisplay failed; browser tool localhost navigation blocked by policy.
- Rollback: rm -rf /Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/Logs/runtime_playtest/epoch_clear_1940 /Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/EPOCH_CLEAR_DELTA_1940.md /Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-unity/capture_epoch_1940*.js; stop server/chrome if still running.

## 2026-06-05 00:15 ICT — Epoch Ascendant heartbeat delta
- Status: BLOCKED. Evidence: `bun/epoch-ascendant-unity/EPOCH_CLEAR_DELTA_0010.md`; server 8124 HTTP 200; Chrome real CDP tab detected; frames after input 0, unique_md5 0; no dropship/learning.

## 2026-06-05 03:10 ICT — Epoch Ascendant heartbeat delta
- Status: PARTIAL. Evidence: `bun/epoch-ascendant-unity/EPOCH_CLEAR_DELTA_0310.md` (876B), Unity log (20411B), md5s (972B).
- Metrics: fresh_frames_after_0310=9, fresh_unique_md5=1, live_webgl_required_unique=5; DB writes 0.
- Rollback: remove the three 0310 files and new combat_sim PNGs after 03:10.

## 2026-06-05 15:16 ICT — Epoch Ascendant delta
- Status: PARTIAL strict gate. Fresh HTML5 runtime capture: `bun/epoch-ascendant-mvp/EPOCH_CLEAR_DELTA_1512.md`; 10 frames, unique_md5=5, 6+ skills, Mammoth runtime, Bronze current, db_writes=0. Unity WebGL strict capture still not proven.
