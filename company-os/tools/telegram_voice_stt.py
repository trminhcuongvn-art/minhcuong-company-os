#!/usr/bin/env python3
"""
Telegram Voice STT Bridge
Nhận voice message từ Telegram → transcribe bằng OpenAI Whisper → trả text

Usage:
  python3 telegram_voice_stt.py --file <ogg_file>   # test local file
  python3 telegram_voice_stt.py --webhook            # start webhook server (port 8766)

Env: OPENAI_API_KEY, TELEGRAM_BOT_TOKEN
"""
import os, sys, json, subprocess, tempfile, argparse, urllib.request, urllib.parse

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com")


def convert_ogg_to_mp3(input_path: str) -> str:
    """Convert OGG/Opus (Telegram voice) to MP3 for Whisper."""
    out = tempfile.mktemp(suffix=".mp3")
    result = subprocess.run(
        ["ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", "-b:a", "64k", out],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg error: {result.stderr[:200]}")
    return out


def transcribe(audio_path: str, language: str = "vi") -> str:
    """Send audio to OpenAI Whisper API and return transcript."""
    url = f"{OPENAI_BASE_URL}/v1/audio/transcriptions"
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    boundary = "----TelegramVoiceSTT"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="model"\r\n\r\nwhisper-1\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="language"\r\n\r\n{language}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="audio.mp3"\r\n'
        f"Content-Type: audio/mpeg\r\n\r\n"
    ).encode() + audio_bytes + f"\r\n--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        result = json.loads(r.read().decode())
    return result.get("text", "").strip()


def download_telegram_file(file_id: str) -> str:
    """Download a Telegram file by file_id, return local path."""
    # Step 1: get file path
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={file_id}"
    with urllib.request.urlopen(url, timeout=15) as r:
        info = json.loads(r.read().decode())
    file_path = info["result"]["file_path"]

    # Step 2: download
    dl_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"
    tmp = tempfile.mktemp(suffix=".ogg")
    with urllib.request.urlopen(dl_url, timeout=30) as r:
        with open(tmp, "wb") as f:
            f.write(r.read())
    return tmp


def send_telegram_message(chat_id, text: str, reply_to_message_id=None):
    """Send text back to Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if reply_to_message_id:
        payload["reply_to_message_id"] = reply_to_message_id
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


def handle_voice_message(update: dict) -> str | None:
    """Process a Telegram update containing a voice message."""
    msg = update.get("message", {})
    voice = msg.get("voice") or msg.get("audio")
    if not voice:
        return None

    chat_id = msg["chat"]["id"]
    message_id = msg["message_id"]
    file_id = voice["file_id"]

    print(f"[STT] Received voice file_id={file_id[:12]}...")

    # Download + convert + transcribe
    ogg_path = download_telegram_file(file_id)
    mp3_path = convert_ogg_to_mp3(ogg_path)
    text = transcribe(mp3_path)

    # Cleanup audio files (privacy)
    os.unlink(ogg_path)
    os.unlink(mp3_path)

    if text:
        reply = f"🎤 <b>Transcript:</b>\n{text}"
        send_telegram_message(chat_id, reply, reply_to_message_id=message_id)
        print(f"[STT] Transcript: {text[:80]}")
    return text


def start_webhook_server(port: int = 8766):
    """Simple HTTP server to receive Telegram webhook updates."""
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                update = json.loads(body.decode())
                handle_voice_message(update)
            except Exception as e:
                print(f"[STT] Error: {e}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")

        def log_message(self, format, *args):
            pass  # quiet

    print(f"[STT] Webhook server listening on port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Telegram Voice STT")
    parser.add_argument("--file", help="Local OGG/audio file to transcribe")
    parser.add_argument("--webhook", action="store_true", help="Start webhook server")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--lang", default="vi", help="Language code (default: vi)")
    args = parser.parse_args()

    if args.file:
        if not OPENAI_API_KEY:
            print("ERROR: OPENAI_API_KEY not set")
            sys.exit(1)
        path = args.file
        if path.endswith(".ogg") or path.endswith(".opus"):
            path = convert_ogg_to_mp3(path)
            cleanup = True
        else:
            cleanup = False
        text = transcribe(path, language=args.lang)
        if cleanup:
            os.unlink(path)
        print(f"Transcript: {text}")
    elif args.webhook:
        if not TELEGRAM_BOT_TOKEN:
            print("ERROR: TELEGRAM_BOT_TOKEN not set")
            sys.exit(1)
        start_webhook_server(args.port)
    else:
        parser.print_help()
