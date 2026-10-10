import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from .engine import tao_engine


class ApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        duong_dan = urlparse(self.path)
        params = parse_qs(duong_dan.query)

        if duong_dan.path == "/ping":
            self._tra_ve_json({"status": "ok", "ten": "Viet Trios"})
            return

        if duong_dan.path == "/run":
            script = params.get("script", [""])[0]
            engine = tao_engine()
            ket_qua = engine.chay(script)
            self._tra_ve_json({"script": script, "ket_qua": ket_qua})
            return

        self._tra_ve_json({"status": "not_found"}, 404)

    def _tra_ve_json(self, payload, ma_trang_thai=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(ma_trang_thai)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def chay_api(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), ApiHandler)
    print(f"Viet Trios api dang chay tai http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    chay_api()
