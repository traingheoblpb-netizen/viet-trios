import re
from typing import Any, Dict, List, Tuple


def _danh_gia_an_toan(bieu_thuc: str, scop: Dict[str, Any]) -> Any:
    bieu_thuc = bieu_thuc.strip()

    if bieu_thuc.startswith('"') and bieu_thuc.endswith('"'):
        return bieu_thuc[1:-1]
    if bieu_thuc.startswith("'") and bieu_thuc.endswith("'"):
        return bieu_thuc[1:-1]
    if bieu_thuc in scop:
        return scop[bieu_thuc]
    if re.fullmatch(r"-?\d+", bieu_thuc):
        return int(bieu_thuc)
    if re.fullmatch(r"-?\d+\.\d+", bieu_thuc):
        return float(bieu_thuc)
    if bieu_thuc.lower() in {"dung", "true"}:
        return True
    if bieu_thuc.lower() in {"sai", "false"}:
        return False

    try:
        return eval(bieu_thuc, {"__builtins__": {}}, scop)
    except Exception:
        raise ValueError(f"Bieu thuc khong hop le: {bieu_thuc}")


def _xu_ly_lap(dong: str, scop: Dict[str, Any]) -> Tuple[str, int]:
    if dong.startswith("lap "):
        phan_lap = dong[4:]
        if " trong " not in phan_lap:
            raise ValueError(f"Lap khong hop le: {dong}")
        bien, phan_trong = phan_lap.split(" trong ", 1)
        bien = bien.strip()
        danh_sach = _danh_gia_an_toan(phan_trong.strip(), scop)
        return bien, danh_sach
    return None, None


def chay_ma(nguon: str, scop: Dict[str, Any] | None = None) -> str:
    scop = {} if scop is None else scop
    ket_qua = []
    dong = [d.strip() for d in nguon.splitlines() if d.strip()]

    i = 0
    while i < len(dong):
        dong_hien_tai = dong[i]

        if dong_hien_tai.startswith("in ra "):
            bieu_thuc = dong_hien_tai[5:].strip()
            ket_qua.append(str(_danh_gia_an_toan(bieu_thuc, scop)))
            i += 1
            continue

        if dong_hien_tai.startswith("xuat "):
            bieu_thuc = dong_hien_tai[5:].strip()
            ket_qua.append(str(_danh_gia_an_toan(bieu_thuc, scop)))
            i += 1
            continue

        if "=" in dong_hien_tai and not dong_hien_tai.startswith("neu ") and not dong_hien_tai.startswith("ham ") and not dong_hien_tai.startswith("lap "):
            ten, bieu_thuc = [phan.strip() for phan in dong_hien_tai.split("=", 1)]
            scop[ten] = _danh_gia_an_toan(bieu_thuc, scop)
            i += 1
            continue

        if dong_hien_tai.startswith("neu "):
            phan_cond = dong_hien_tai[4:]
            if ":" not in phan_cond:
                raise ValueError(f"Lenh dieu kien khong hop le: {dong_hien_tai}")
            dieu_kien, than = [phan.strip() for phan in phan_cond.split(":", 1)]
            if _danh_gia_an_toan(dieu_kien, scop):
                ket_qua_phu = chay_ma(than, scop)
                if ket_qua_phu:
                    ket_qua.append(ket_qua_phu)
            i += 1
            continue

        if dong_hien_tai.startswith("lap "):
            phan_lap = dong_hien_tai[4:]
            if " trong " not in phan_lap or ":" not in phan_lap:
                raise ValueError(f"Lap khong hop le: {dong_hien_tai}")
            phan_bien, phan_sau = phan_lap.split(" trong ", 1)
            bien = phan_bien.strip()
            phan_danh_sach = phan_sau.split(":", 1)[0].strip()
            danh_sach = _danh_gia_an_toan(phan_danh_sach, scop)

            i += 1
            than_lap = []
            while i < len(dong) and dong[i].startswith("    "):
                than_lap.append(dong[i].strip())
                i += 1

            try:
                for phan_tu in danh_sach:
                    scop[bien] = phan_tu
                    ket_qua_phu = chay_ma("\n".join(than_lap), scop)
                    if ket_qua_phu:
                        ket_qua.append(ket_qua_phu)
            except TypeError:
                raise ValueError(f"Danh sach khong hop le cho lap: {phan_danh_sach}")
            continue

        if dong_hien_tai.startswith("ham "):
            phan_ham = dong_hien_tai[4:]
            if "(" not in phan_ham or ")" not in phan_ham:
                raise ValueError(f"Ham khong hop le: {dong_hien_tai}")
            ten_ham = phan_ham.split("(", 1)[0].strip()
            tham_so = phan_ham.split("(", 1)[1].split(")", 1)[0].strip()
            danh_sach_tham_so = [t.strip() for t in tham_so.split(",") if t.strip()]
            i += 1
            than_ham = []
            while i < len(dong) and dong[i].startswith("    "):
                than_ham.append(dong[i].strip())
                i += 1
            scop[ten_ham] = {
                "tham_so": danh_sach_tham_so,
                "than_ham": than_ham,
                "scop_ham": dict(scop),
            }
            continue

        raise ValueError(f"Lenh khong duoc ho tro: {dong_hien_tai}")

    return "\n".join(ket_qua)
