from viettrios.bo_dich import chuyen_thanh_khong_dau
from viettrios.quan_ly_goi import danh_sach_goi


def chuyen_doi_nguon(nguon: str) -> str:
    return chuyen_thanh_khong_dau(nguon)


def xem_goi() -> list:
    return danh_sach_goi()
