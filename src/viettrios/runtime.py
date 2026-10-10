import re
from typing import Any, Dict, List, Tuple


class DoiTuong:
    def __init__(self, lop, thuoc_tinh=None):
        self._lop = lop
        self._thuoc_tinh = {} if thuoc_tinh is None else thuoc_tinh

    def __getattr__(self, ten):
        if ten in self._lop["phuong_thuc"]:
            def phuong_thuc_goi(*args, **kwargs):
                return self._lop["phuong_thuc"][ten](self, *args, **kwargs)

            return phuong_thuc_goi
        if ten in self._thuoc_tinh:
            return self._thuoc_tinh[ten]
        raise AttributeError(f"Thuoc tinh khong ton tai: {ten}")

    def __setattr__(self, ten, gia_tri):
        if ten.startswith("_"):
            object.__setattr__(self, ten, gia_tri)
        else:
            self._thuoc_tinh[ten] = gia_tri

    def __repr__(self):
        return f"<DoiTuong {self._lop['ten']}>"


class Lop:
    def __init__(self, ten: str, phuong_thuc: Dict[str, Any]):
        self.ten = ten
        self.phuong_thuc = phuong_thuc

    def __call__(self, *args, **kwargs):
        return DoiTuong({"ten": self.ten, "phuong_thuc": self.phuong_thuc}, {})


def _tach_danh_sach(phan: str, scop: Dict[str, Any]) -> List[Any]:
    if not phan.strip():
        return []
    noi_dung = phan.strip()[1:-1]
    if not noi_dung.strip():
        return []
    phan_tach = []
    tam = ""
    muc = 0
    trong_chuoi = None
    for ky_tu in noi_dung:
        if ky_tu in ('"', "'"):
            if trong_chuoi is None:
                trong_chuoi = ky_tu
            elif trong_chuoi == ky_tu:
                trong_chuoi = None
            tam += ky_tu
            continue
        if ky_tu == "[":
            muc += 1
        elif ky_tu == "]":
            muc -= 1
        elif ky_tu == "," and muc == 0 and trong_chuoi is None:
            phan_tach.append(tam.strip())
            tam = ""
            continue
        tam += ky_tu
    if tam.strip():
        phan_tach.append(tam.strip())
    return [_danh_gia_an_toan(item, scop) for item in phan_tach if item.strip()]


def _tach_tu_dien(phan: str, scop: Dict[str, Any]) -> Dict[str, Any]:
    if not phan.strip():
        return {}
    noi_dung = phan.strip()[1:-1]
    if not noi_dung.strip():
        return {}
    phan_tach = []
    tam = ""
    muc = 0
    trong_chuoi = None
    for ky_tu in noi_dung:
        if ky_tu in ('"', "'"):
            if trong_chuoi is None:
                trong_chuoi = ky_tu
            elif trong_chuoi == ky_tu:
                trong_chuoi = None
            tam += ky_tu
            continue
        if ky_tu == "{":
            muc += 1
        elif ky_tu == "}":
            muc -= 1
        elif ky_tu == "," and muc == 0 and trong_chuoi is None:
            phan_tach.append(tam.strip())
            tam = ""
            continue
        tam += ky_tu
    if tam.strip():
        phan_tach.append(tam.strip())

    ket_qua = {}
    for item in phan_tach:
        if ":" not in item:
            continue
        khoa, gia_tri = [phan.strip() for phan in item.split(":", 1)]
        ket_qua[khoa.strip()] = _danh_gia_an_toan(gia_tri, scop)
    return ket_qua


def _danh_gia_an_toan(bieu_thuc: str, scop: Dict[str, Any]) -> Any:
    bieu_thuc = bieu_thuc.strip()

    if bieu_thuc.startswith("[") and bieu_thuc.endswith("]"):
        return _tach_danh_sach(bieu_thuc, scop)
    if bieu_thuc.startswith("{") and bieu_thuc.endswith("}"):
        return _tach_tu_dien(bieu_thuc, scop)
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
    if bieu_thuc.startswith("len(") and bieu_thuc.endswith(")"):
        noi_dung = bieu_thuc[4:-1].strip()
        return len(_danh_gia_an_toan(noi_dung, scop))
    try:
        return eval(bieu_thuc, {"__builtins__": {"len": len, "sum": sum, "min": min, "max": max}}, scop)
    except Exception:
        raise ValueError(f"Bieu thuc khong hop le: {bieu_thuc}")


def _lay_block(lines: List[str], vi_tri: int) -> Tuple[List[str], int]:
    block = []
    j = vi_tri + 1
    while j < len(lines) and lines[j].startswith("    "):
        block.append(lines[j][4:])
        j += 1
    return block, j


def chay_ma(nguon: str, scop: Dict[str, Any] | None = None) -> str:
    scop = {} if scop is None else scop
    ket_qua = []
    dong = [d.rstrip() for d in nguon.splitlines() if d.strip()]

    i = 0
    while i < len(dong):
        dong_hien_tai = dong[i].strip()

        if dong_hien_tai.startswith("#"):
            i += 1
            continue

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

        if dong_hien_tai.startswith("tra_ve "):
            bieu_thuc = dong_hien_tai[7:].strip()
            return str(_danh_gia_an_toan(bieu_thuc, scop))

        if "=" in dong_hien_tai and not dong_hien_tai.startswith("neu ") and not dong_hien_tai.startswith("ham ") and not dong_hien_tai.startswith("lop ") and not dong_hien_tai.startswith("lap "):
            ten, bieu_thuc = [phan.strip() for phan in dong_hien_tai.split("=", 1)]
            scop[ten] = _danh_gia_an_toan(bieu_thuc, scop)
            i += 1
            continue

        if dong_hien_tai.startswith("neu "):
            phan_cond = dong_hien_tai[4:]
            if ":" not in phan_cond:
                raise ValueError(f"Lenh dieu kien khong hop le: {dong_hien_tai}")
            dieu_kien, than = [phan.strip() for phan in phan_cond.split(":", 1)]
            block = []
            if than.strip():
                block = [than.strip()]
            else:
                block, i = _lay_block(dong, i)
                if not block:
                    raise ValueError(f"Lenh dieu kien khong co than: {dong_hien_tai}")
            if _danh_gia_an_toan(dieu_kien, scop):
                ket_qua_phu = chay_ma("\n".join(block), scop)
                if ket_qua_phu:
                    ket_qua.append(ket_qua_phu)
            if than.strip():
                i += 1
            continue

        if dong_hien_tai.startswith("lap "):
            phan_lap = dong_hien_tai[4:]
            if ":" not in phan_lap:
                raise ValueError(f"Lap khong hop le: {dong_hien_tai}")
            phan_lap = phan_lap[:-1].strip()
            if " trong " not in phan_lap:
                raise ValueError(f"Lap khong hop le: {dong_hien_tai}")
            bien, danh_sach_str = [phan.strip() for phan in phan_lap.split(" trong ", 1)]
            block, i = _lay_block(dong, i)
            if not block:
                raise ValueError(f"Lap khong co than: {dong_hien_tai}")
            danh_sach = _danh_gia_an_toan(danh_sach_str, scop)
            for phan_tu in danh_sach:
                scop[bien] = phan_tu
                ket_qua_phu = chay_ma("\n".join(block), scop)
                if ket_qua_phu:
                    ket_qua.append(ket_qua_phu)
            continue

        if dong_hien_tai.startswith("ham "):
            phan_ham = dong_hien_tai[4:]
            if "(" not in phan_ham or ")" not in phan_ham:
                raise ValueError(f"Ham khong hop le: {dong_hien_tai}")
            ten_ham = phan_ham.split("(", 1)[0].strip()
            tham_so = phan_ham.split("(", 1)[1].split(")", 1)[0].strip()
            danh_sach_tham_so = [t.strip() for t in tham_so.split(",") if t.strip()]
            block, i = _lay_block(dong, i)
            if not block:
                raise ValueError(f"Ham khong co than: {dong_hien_tai}")

            def tao_ham(ten_ham_local, tham_so_local, block_local, scop_local):
                def ham_goi(*args):
                    dia_chi = dict(scop_local)
                    for ten_tham_so, gia_tri in zip(tham_so_local, args):
                        dia_chi[ten_tham_so] = gia_tri
                    ket_qua_ham = chay_ma("\n".join(block_local), dia_chi)
                    return ket_qua_ham

                return ham_goi

            scop[ten_ham] = tao_ham(ten_ham, danh_sach_tham_so, block, scop)
            continue

        if dong_hien_tai.startswith("lop "):
            phan_lop = dong_hien_tai[4:]
            if ":" not in phan_lop:
                raise ValueError(f"Lop khong hop le: {dong_hien_tai}")
            ten_lop = phan_lop[:-1].strip()
            block, i = _lay_block(dong, i)
            if not block:
                raise ValueError(f"Lop khong co than: {dong_hien_tai}")
            phuong_thuc = {}
            for dong_phuong_thuc in block:
                if dong_phuong_thuc.strip().startswith("ham "):
                    ham_text = dong_phuong_thuc.strip()[4:]
                    if "(" not in ham_text or ")" not in ham_text:
                        raise ValueError(f"Ham trong lop khong hop le: {dong_phuong_thuc}")
                    ten_phuong_thuc = ham_text.split("(", 1)[0].strip()
                    tham_so = ham_text.split("(", 1)[1].split(")", 1)[0].strip()
                    danh_sach_tham_so = [t.strip() for t in tham_so.split(",") if t.strip()]
                    phuong_thuc_block = []
                    for d in block[block.index(dong_phuong_thuc) + 1:]:
                        if not d.startswith("    "):
                            break
                        phuong_thuc_block.append(d[4:])
                    def tao_phuong_thuc(ten_phuong_thuc_local, tham_so_local, block_local, scop_local):
                        def phuong_thuc_goi(self, *args):
                            dia_chi = dict(scop_local)
                            dia_chi["self"] = self
                            for ten_tham_so, gia_tri in zip(tham_so_local, args):
                                dia_chi[ten_tham_so] = gia_tri
                            ket_qua_ham = chay_ma("\n".join(block_local), dia_chi)
                            return ket_qua_ham

                        return phuong_thuc_goi

                    phuong_thuc[ten_phuong_thuc] = tao_phuong_thuc(ten_phuong_thuc, danh_sach_tham_so, phuong_thuc_block, scop)
            scop[ten_lop] = {"ten": ten_lop, "phuong_thuc": phuong_thuc}
            continue

        if dong_hien_tai.startswith("doi_tuong "):
            than = dong_hien_tai[len("doi_tuong "):].strip()
            if than in scop and isinstance(scop[than], dict) and "ten" in scop[than]:
                inst = DoiTuong(scop[than], {})
                scop[than] = inst
                i += 1
                continue

        if dong_hien_tai.startswith("goi "):
            bieu_thuc = dong_hien_tai[4:].strip()
            if "(" in bieu_thuc and bieu_thuc.endswith(")"):
                ten_ham, tham_so = bieu_thuc.split("(", 1)
                ten_ham = ten_ham.strip()
                tham_so = tham_so[:-1].strip()
                if not tham_so:
                    args = []
                else:
                    args = [_danh_gia_an_toan(item.strip(), scop) for item in tham_so.split(",")]
                ham = scop.get(ten_ham)
                if ham is None:
                    raise ValueError(f"Ham khong ton tai: {ten_ham}")
                ket_qua.append(str(ham(*args)))
                i += 1
                continue

        raise ValueError(f"Lenh khong duoc ho tro: {dong_hien_tai}")

    return "\n".join(ket_qua)
