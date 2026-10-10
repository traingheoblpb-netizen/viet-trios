# Package Manager v2 - Quan ly goi nang cap

import json
from pathlib import Path


class QuanLyGoiV2:
    def __init__(self, kho_path="~/.viet-trios/packages"):
        self.kho_path = Path(kho_path).expanduser()
        self.kho_path.mkdir(parents=True, exist_ok=True)
    
    def cai_dat_goi(self, ten_goi, phien_ban="latest"):
        print(f"Dang cai dat {ten_goi}@{phien_ban}...")
        goi_path = self.kho_path / ten_goi
        goi_path.mkdir(parents=True, exist_ok=True)
        return True
    
    def goi_da_cai_dat(self):
        goi_list = []
        for item in self.kho_path.iterdir():
            if item.is_dir():
                goi_list.append(item.name)
        return goi_list
    
    def xoa_goi(self, ten_goi):
        goi_path = self.kho_path / ten_goi
        if goi_path.exists():
            import shutil
            shutil.rmtree(goi_path)
            return True
        return False
    
    def tim_goi(self, tu_khoa):
        ket_qua = []
        for goi in self.goi_da_cai_dat():
            if tu_khoa.lower() in goi.lower():
                ket_qua.append(goi)
        return ket_qua
