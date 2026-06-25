from flask import Flask, request, jsonify, render_template
from scanner import scan_range, resolve_host

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    host = data.get("host", "127.0.0.1").strip()
    start = int(data.get("start", 1))
    end = int(data.get("end", 1024))

    if end - start > 9999:
        return jsonify({"error": "Range too large. Max 10,000 ports."}), 400

    # Resolve domain to IP
    ip = resolve_host(host)
    if not ip:
        return jsonify({"error": f"Could not resolve host: {host}"}), 400

    results = scan_range(ip, start, end)

    ports_data = []
    for port in sorted(results.keys()):
        ports_data.append({
            "port": port,
            "banner": results[port].get("banner")
        })

    return jsonify({
        "host": host,
        "ip": ip,
        "open_ports": ports_data,
        "total_scanned": end - start + 1
    })
    
import urllib.request
import json as json_lib

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    prompt = data.get("prompt", "")

    payload = json_lib.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1000,
        "system": "You are a senior penetration tester. Analyze open ports and give clear, practical security advice. Be concise. Use plain text with clear sections, no markdown symbols.",
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json_lib.loads(response.read())
            text = "".join(b.get("text", "") for b in result.get("content", []))
            return jsonify({"result": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500   

if __name__ == "__main__":
    app.run(debug=True)