#!/usr/bin/env python3
# Viet Trios CLI v2

import argparse
from pathlib import Path

from viettrios.engine_v2 import EngineVietTriosV2
from viettrios.quan_ly_goi_v2 import QuanLyGoiV2
from viettrios.web_framework import VietTriosApp, VietTriosResponse


def chay_script(duong_dan):
    engine = EngineVietTriosV2()
    ma = Path(duong_dan).read_text(encoding='utf-8')
    engine.chay(ma)


def quan_ly_goi_cli():
    quan_ly = QuanLyGoiV2()
    
    parser = argparse.ArgumentParser(description="Quan ly goi Viet Trios")
    subparsers = parser.add_subparsers(dest="lenh")
    
    install_parser = subparsers.add_parser("cai_dat")
    install_parser.add_argument("ten_goi")
    
    list_parser = subparsers.add_parser("danh_sach")
    
    args = parser.parse_args()
    
    if args.lenh == "cai_dat":
        quan_ly.cai_dat_goi(args.ten_goi)
    elif args.lenh == "danh_sach":
        print(quan_ly.goi_da_cai_dat())


def demo_web():
    app = VietTriosApp()
    
    @app.duong("/")
    def trang_chu(request):
        html = """<html><body><h1>Viet Trios v2.0</h1></body></html>"""
        return VietTriosResponse().html(html)
    
    @app.duong("/api/hello")
    def hello(request):
        return VietTriosResponse().json({"message": "Xin chao Viet Trios"})
    
    app.chay()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        demo_web()
    elif len(sys.argv) > 1 and sys.argv[1] == "goi":
        quan_ly_goi_cli()
    else:
        chay_script(sys.argv[1])
