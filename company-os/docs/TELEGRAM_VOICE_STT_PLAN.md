# Telegram Voice STT Plan
Updated: 2026-06-05 14:28 ICT. Owner: Cáo

## Goal
Henry gửi voice note trong Telegram group/private → hệ thống tự transcribe → đưa text vào OpenClaw/agent context như tin nhắn thường.

## Proposed flow
1. Telegram bot receives `voice` / `audio` message.
2. Download file via Telegram Bot API `getFile`.
3. Convert OGG/Opus to WAV/MP3 if needed using ffmpeg.
4. Send audio to STT provider: OpenAI Whisper/GPT-4o-transcribe or local Whisper.
5. Return transcript into chat as text or inject as user message to target agent.
6. Store transcript metadata; do not store raw audio unless explicitly enabled.

## Implementation options
- Fast path: OpenAI transcription API + current Telegram bot webhook.
- Privacy path: local whisper.cpp/whisper-large-v3-turbo if host resources allow.
- Hybrid: local for short voice, cloud fallback for failures.

## Needed config
- Telegram bot token/webhook access.
- STT API key or local model path.
- ffmpeg installed.
- Routing rule: group voice → Trợ Lý by default; mentions route to named agent.

## Risks
- API cost if many voice notes.
- Privacy: audio may contain business data; default should delete raw audio after transcript.
- Latency: local model slower, cloud faster.

## Next build step
Create `telegram_voice_stt_bridge.py`, test with one voice sample, then wire to gateway route.
