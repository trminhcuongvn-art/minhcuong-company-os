#!/usr/bin/env python3.12
"""
Telegram Voice STT Bridge — Local Whisper
Nhận voice OGG từ Telegram → ffmpeg convert → whisper local → transcript text
"""
import os, sys, json, subprocess, tempfile, argparse

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

def convert_ogg_to_wav(input_path: str) -> str:
    out = tempfile.mktemp(suffix=".wav")
    r = subprocess.run(
        ["ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", out],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg: {r.stderr[:200]}")
    return out

def transcribe_local(audio_path: str, language: str = "vi", model_name: str = "base") -> str:
    import whisper
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, language=language)
    return result["text"].strip()

def generate_test_wav() -> str:
    import struct
    num_samples = 32000  # 2s 16kHz
    wav_path = tempfile.mktemp(suffix=".wav")
    with open(wav_path, "wb") as f:
        data = struct.pack("<" + "h"*num_samples, *[0]*num_samples)
        f.write(b"RIFF")
        f.write(struct.pack("<I", 36+len(data)))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("<IHHIIHH", 16, 1, 1, 16000, 32000, 2, 16))
        f.write(b"data")
        f.write(struct.pack("<I", len(data)))
        f.write(data)
    return wav_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Audio file to transcribe")
    parser.add_argument("--test", action="store_true", help="Run with silent test audio")
    parser.add_argument("--model", default="base", help="Whisper model (tiny/base/small/medium)")
    parser.add_argument("--lang", default="vi")
    args = parser.parse_args()

    if args.test:
        wav = generate_test_wav()
        print(f"[TEST] Generated silent wav: {wav}")
        t = transcribe_local(wav, language=args.lang, model_name=args.model)
        os.unlink(wav)
        print(f"[TEST] Transcript: '{t}' (empty = OK for silent audio)")
    elif args.file:
        path = args.file
        if not path.endswith(".wav"):
            path = convert_ogg_to_wav(path)
            cleanup = True
        else:
            cleanup = False
        t = transcribe_local(path, language=args.lang, model_name=args.model)
        if cleanup: os.unlink(path)
        print(f"Transcript: {t}")
    else:
        parser.print_help()
