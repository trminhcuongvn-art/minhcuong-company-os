# Dify Machine Readiness — 2026-06-03

## Checked current machine
- Host: Mac mini, arm64
- OS: macOS 26.2
- CPU: 10 cores / 10 logical CPUs
- RAM: 16 GiB
- Disk root: 460 GiB total, ~207 GiB available
- Docker: not installed / docker command missing

## Dify documented requirements
- CPU >= 2 cores
- RAM >= 4 GiB
- macOS requires Docker Desktop + Docker Compose 2.24.0+
- Docker VM should be configured with at least 2 vCPU and 8 GiB RAM

## Assessment
Hardware is sufficient for Dify self-host trial.
- CPU: PASS
- RAM: PASS, but allocate Docker 8 GiB and avoid running too many other heavy containers.
- Disk: PASS
- Architecture: arm64 Mac should be acceptable via Docker images, but must verify Dify image compatibility during install.
- Blocking issue: Docker Desktop is missing.

## Recommendation
Focus on Dify as primary. No fallback by default.
Next action:
1. Install Docker Desktop for Mac / verify Docker Compose >= 2.24.
2. Configure Docker resources: 4 vCPU, 8-10 GiB RAM, sufficient disk.
3. Clone Dify into workspace/external/dify or /Users/minhcuong/.openclaw/workspace/dify.
4. Start Dify Docker Compose.
5. If failure, debug logs and fix; do not switch fallback unless strategic decision.

## Risk controls
- Do not public expose Dify initially; local only.
- Do not ingest sensitive customer data until auth/storage policy confirmed.
- Document all config changes and rollback.
