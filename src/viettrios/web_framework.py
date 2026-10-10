# Web Framework cho Viet Trios

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs, urlparse


class VietTriosRequest:
    def __init__(self, phuong_thuc, duong_dan, params=None):
        self.phuong_thuc = phuong_thuc
        self.duong_dan = duong_dan
        self.params = params or {}


class VietTriosResponse:
    def __init__(self):
        self.ma_trang_thai = 200
        self.noi_dung = ""
        self.tieu_de = {}
    
    def json(self, du_lieu):
        self.tieu_de["Content-Type"] = "application/json"
        self.noi_dung = json.dumps(du_lieu, ensure_ascii=False)
        return self
    
    def text(self, van_ban):
        self.tieu_de["Content-Type"] = "text/plain"
        self.noi_dung = van_ban
        return self
    
    def html(self, html):
        self.tieu_de["Content-Type"] = "text/html"
        self.noi_dung = html
        return self


class VietTriosApp:
    def __init__(self):
        self.routes = {}
    
    def duong(self, duong_dan):
        def decorator(func):
            self.routes[duong_dan] = func
            return func
        return decorator
    
    def chay(self, host="127.0.0.1", port=8000):
        app = self
        
        class Handler(BaseHTTPRequestHandler):
            def do_GET(handler_self):
                duong_dan = urlparse(handler_self.path).path
                if duong_dan in app.routes:
                    request = VietTriosRequest("GET", duong_dan)
                    response = app.routes[duong_dan](request)
                    
                    handler_self.send_response(response.ma_trang_thai)
                    for ten, gia_tri in response.tieu_de.items():
                        handler_self.send_header(ten, gia_tri)
                    handler_self.end_headers()
                    handler_self.wfile.write(response.noi_dung.encode('utf-8'))
                else:
                    handler_self.send_response(404)
                    handler_self.end_headers()
            
            def log_message(handler_self, format, *args):
                pass
        
        server = HTTPServer((host, port), Handler)
        print(f"Viet Trios web dang chay tai http://{host}:{port}")
        server.serve_forever()
