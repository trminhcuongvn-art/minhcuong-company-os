#!/usr/bin/env python3.12
"""
Upharma TTS Server — edge-tts local HTTP server
Port: 8765
Endpoint: POST /tts
Body: {"text": "...", "voice": "vi-VN-HoaiMyNeural", "rate": "+0%", "volume": "+0%"}
Returns: audio/mpeg (MP3 bytes)
"""
import asyncio, edge_tts, io, logging
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

VOICES = {
    "female": "vi-VN-HoaiMyNeural",
    "male": "vi-VN-NamMinhNeural",
    "default": "vi-VN-HoaiMyNeural"
}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "voices": list(VOICES.keys())})

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json(force=True)
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "text is required"}), 400

    voice_key = data.get("voice", "default")
    voice = VOICES.get(voice_key, VOICES["default"])
    if voice_key.startswith("vi-VN-"):
        voice = voice_key  # allow full voice name

    rate = data.get("rate", "-10%")   # slightly slower for pharmacy
    volume = data.get("volume", "+0%")

    async def generate():
        communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume)
        buf = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buf.write(chunk["data"])
        buf.seek(0)
        return buf

    buf = asyncio.run(generate())
    return send_file(buf, mimetype="audio/mpeg", download_name="tts_output.mp3")

@app.route("/voices", methods=["GET"])
def list_voices():
    return jsonify(VOICES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8765, debug=False)
