# 2026-06-04 03:47 — Epoch Ascendant: bridge Web MVP → Unity khi Unity bị chặn Rosetta

## Context
Heartbeat Bún quét canonical bus + bus local. Các task BaDiVi đã có RESULT/DONE; SmallBizOps/Tarot/Ông Đồ.AI đang freeze. Task game mới nhất `bun_epoch_ascendant_unity_project_foundation_20260604` đã tạo foundation Unity nhưng chỉ PARTIAL vì Unity Editor 6000.4.10f1 yêu cầu Rosetta 2, batchmode compile/import chưa chạy được.

## AI First audit
1. Tốn tiền/license? Không — chỉ viết note nội bộ và audit hướng làm.
2. Đụng dữ liệu thật/production? Không.
3. Khó đảo ngược? Không — xoá file note.
4. Public dữ liệu nội bộ ra ngoài? Không.
=> Tự làm, không hỏi.

## Hướng giữ tiến độ game khi Unity compile bị block
1. **Không nâng Unity foundation lên DONE** nếu chưa có Unity compile/playtest log. Giữ trạng thái PARTIAL/BLOCKED đúng evidence gate.
2. **Dùng Web MVP làm oracle gameplay**: mọi logic mới nên test trước trong `/Users/minhcuong/.openclaw/workspace/bun/epoch-ascendant-mvp/index.html` vì chạy được ngay, không cần Unity.
3. **Tách gameplay spec thành bảng porting**:
   - Hero movement → `HeroController.cs`
   - Camera follow → `CameraFollow.cs`
   - Auto attack/projectile → `AutoAttack.cs` + `Projectile.cs`
   - Enemy chase/spawn → `EnemyController.cs` + `EnemySpawner.cs`
   - XP/level/evolution → `XPOrb.cs` + `EvolutionManager.cs`
   - HUD/game state → `HUDController.cs` + `GameManager.cs`
4. **Static audit trước compile**: check file tồn tại, class name trùng file, không thiếu brace, không dùng API ngoài package mặc định, scene stub có path đúng.
5. **Acceptance gate sau Rosetta**:
   - Unity batchmode mở project không lỗi import.
   - Console không có compile error.
   - Scene `Day1Foundation.unity` có GameManager/Hero/Camera/Spawner/HUD prefab hoặc object stub.
   - Playmode 30s: hero di chuyển, auto-fire, enemy chase, orb XP, HUD update.

## Next action đề xuất không cần hỏi Henry
- Nếu chưa có Rosetta: tiếp tục polish Web MVP hoặc tạo Unity test plan/static audit, không báo DONE.
- Khi Rosetta có: chạy Unity batch validation ngay, capture log, nếu pass mới chuyển DONE.

## Rollback
`rm /Users/minhcuong/.openclaw/workspace/memory/areas/dropship-affiliate/learning/2026-06-04_0347_epoch_unity_rosetta_blocker_web_to_unity_bridge_skill.md`
