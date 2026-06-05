#!/usr/bin/env python3
"""
Upharma Banner Generator Server — Chrome headless HTML→PNG
Port: 8766
POST /banner
Body: {
  "discount": "GIẢM 20%",
  "title": "Tất cả Vitamin & Thực phẩm chức năng",
  "detail": "Áp dụng toàn bộ sản phẩm...",
  "validity": "01/06 – 30/06/2026",
  "pharmacy": "Upharma Quận 1",
  "width": 800,
  "height": 400
}
Returns: image/png
"""
import subprocess, tempfile, os, json, base64
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Arial',sans-serif; background:#fff; }}
.banner {{
  width:{width}px; height:{height}px;
  background: linear-gradient(135deg, #0057A8 0%, #003d7a 60%, #00284f 100%);
  position:relative; overflow:hidden;
  display:flex; flex-direction:column; justify-content:center;
  padding:40px 50px;
}}
.banner::before {{ content:''; position:absolute; top:-80px; right:-80px;
  width:300px; height:300px; background:rgba(255,255,255,0.05); border-radius:50%; }}
.banner::after {{ content:''; position:absolute; bottom:-100px; right:100px;
  width:400px; height:400px; background:rgba(255,255,255,0.04); border-radius:50%; }}
.logo {{ font-size:28px; font-weight:900; color:#fff; letter-spacing:2px;
  text-transform:uppercase; margin-bottom:6px; }}
.logo span {{ background:#fff; color:#0057A8; padding:2px 8px; border-radius:4px; }}
.tagline {{ font-size:12px; color:rgba(255,255,255,0.7); letter-spacing:1px;
  text-transform:uppercase; margin-bottom:25px; }}
.promo-badge {{ display:inline-block; background:#FFD700; color:#0057A8;
  font-size:44px; font-weight:900; padding:8px 20px; border-radius:8px;
  margin-bottom:14px; width:fit-content; }}
.promo-title {{ font-size:22px; color:#fff; font-weight:700; margin-bottom:8px; line-height:1.3; }}
.promo-detail {{ font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; }}
.validity {{ position:absolute; bottom:22px; left:50px; font-size:12px; color:rgba(255,255,255,0.6); }}
.pharmacy-name {{ position:absolute; bottom:22px; right:50px; font-size:13px;
  color:rgba(255,255,255,0.8); font-weight:600; }}
.cross::before, .cross::after {{ content:''; position:absolute; background:rgba(255,255,255,0.12); border-radius:4px; }}
.cross::before {{ width:16px; height:50px; top:22px; right:58px; }}
.cross::after {{ width:50px; height:16px; top:38px; right:45px; }}
</style></head>
<body><div class="banner">
  <div class="cross"></div>
  <div class="logo"><span>U</span> pharma</div>
  <div class="tagline">Chuỗi nhà thuốc uy tín — 19 chi nhánh</div>
  <div class="promo-badge">{discount}</div>
  <div class="promo-title">{title}</div>
  <div class="promo-detail">{detail}</div>
  <div class="validity">⏰ Từ {validity}</div>
  <div class="pharmacy-name">📍 {pharmacy}</div>
</div></body></html>"""

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "upharma-banner-generator"})

BANNER_OUT_DIR = "/Users/minhcuong/.openclaw/workspace/upharma/banner_output"
os.makedirs(BANNER_OUT_DIR, exist_ok=True)

@app.route("/banner", methods=["POST"])
def generate_banner():
    data = request.get_json(force=True)
    width = data.get("width", 800)
    height = data.get("height", 400)
    html = HTML_TEMPLATE.format(
        width=width, height=height,
        discount=data.get("discount", "GIẢM 20%"),
        title=data.get("title", "Chương trình khuyến mãi"),
        detail=data.get("detail", "").replace("\n", "<br>"),
        validity=data.get("validity", ""),
        pharmacy=data.get("pharmacy", "Upharma")
    )
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode='w', encoding='utf-8') as f:
        f.write(html)
        html_path = f.name
    import time
    filename = f"banner_{int(time.time())}.png"
    out_path = os.path.join(BANNER_OUT_DIR, filename)
    try:
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--no-sandbox",
            f"--screenshot={out_path}",
            f"--window-size={width},{height}",
            f"file://{html_path}"
        ], capture_output=True, timeout=15)
        os.unlink(html_path)
        size = os.path.getsize(out_path)
        # Return JSON with file path + base64
        with open(out_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        return jsonify({
            "status": "ok",
            "file_path": out_path,
            "filename": filename,
            "size_bytes": size,
            "base64_preview": b64[:100] + "...",
            "download_url": f"http://localhost:8766/download/{filename}"
        })
    except Exception as e:
        if os.path.exists(html_path): os.unlink(html_path)
        return jsonify({"error": str(e)}), 500

FLYER_TEMPLATE = open('/Users/minhcuong/.openclaw/workspace/upharma/banner_templates/upharma_flyer_a4_template.html', 'r', encoding='utf-8').read()

@app.route("/flyer", methods=["POST"])
def generate_flyer():
    """Generate A4 tờ rơi (595x842) — POST JSON same as /banner + optional products list"""
    import time, re
    data = request.get_json(force=True)
    html = FLYER_TEMPLATE
    # Replace dynamic fields
    replacements = {
        'GIẢM 20%': data.get('discount', 'GIẢM 20%'),
        'Tất cả Vitamin &amp;': data.get('title_line1', 'Tất cả Vitamin &amp;'),
        'Thực phẩm chức\n         năng': data.get('title_line2', 'Thực phẩm chức\n         năng'),
        'Áp dụng cho toàn bộ sản phẩm vitamin nhóm B, C, D, E': data.get('detail_line1', 'Áp dụng cho toàn bộ sản phẩm vitamin nhóm B, C, D, E'),
        '01/06 – 30/06/2026': data.get('validity', '01/06 – 30/06/2026'),
        'Upharma Quận 1': data.get('pharmacy', 'Upharma Quận 1'),
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as f:
        f.write(html)
        html_path = f.name
    filename = f'flyer_{int(time.time())}.png'
    out_path = os.path.join(BANNER_OUT_DIR, filename)
    try:
        subprocess.run([
            CHROME, '--headless', '--disable-gpu', '--no-sandbox',
            f'--screenshot={out_path}',
            '--window-size=595,842',
            f'file://{html_path}'
        ], capture_output=True, timeout=15)
        os.unlink(html_path)
        size = os.path.getsize(out_path)
        return jsonify({
            'status': 'ok', 'type': 'flyer_a4',
            'file_path': out_path, 'filename': filename,
            'size_bytes': size,
            'download_url': f'http://localhost:8766/download/{filename}'
        })
    except Exception as e:
        if os.path.exists(html_path): os.unlink(html_path)
        return jsonify({'error': str(e)}), 500

@app.route("/download/<filename>", methods=["GET"])
def download_banner(filename):
    path = os.path.join(BANNER_OUT_DIR, filename)
    if not os.path.exists(path):
        return jsonify({"error": "not found"}), 404
    return send_file(path, mimetype="image/png", download_name=filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8766, debug=False)
