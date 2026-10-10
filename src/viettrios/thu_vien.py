GOI_MAC_DINH = {
    "viettrios": "0.2.0",
    "viettrios.std": "0.1.0",
    "viettrios.core": "0.1.0",
}


def tao_goi(ten: str, phien_ban: str = "0.1.0", mo_ta: str = ""):
    return {
        "ten": ten,
        "phien_ban": phien_ban,
        "mo_ta": mo_ta,
    }


def danh_sach_goi():
    return list(GOI_MAC_DINH.items())


def cai_dat_goi(ten: str):
    if ten in GOI_MAC_DINH:
        return f"Goi '{ten}' da ton tai trong kho goi mac dinh."
    GOI_MAC_DINH[ten] = "0.1.0"
    return f"Da cai dat goi '{ten}'."


def goi_thong_tin(ten: str):
    if ten not in GOI_MAC_DINH:
        return None
    return {
        "ten": ten,
        "phien_ban": GOI_MAC_DINH[ten],
    }
