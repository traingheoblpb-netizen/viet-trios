import unicodedata


def chuyen_thanh_khong_dau(nguon: str) -> str:
    if nguon is None:
        return ""
    bang_nho = unicodedata.normalize("NFD", nguon)
    ket_qua = "".join(ch for ch in bang_nho if not unicodedata.combining(ch))
    return ket_qua


def chuyen_thanh_co_dau(nguon: str) -> str:
    return nguon
