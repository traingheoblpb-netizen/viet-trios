# Standard Library Files - Thu vien ho tro file

from pathlib import Path


def doc_tep(duong_dan):
    return Path(duong_dan).read_text(encoding='utf-8')


def ghi_tep(duong_dan, noi_dung):
    Path(duong_dan).write_text(str(noi_dung), encoding='utf-8')
    return True


def tep_co_ton_tai(duong_dan):
    return Path(duong_dan).exists()


def xoa_tep(duong_dan):
    path = Path(duong_dan)
    if path.exists():
        path.unlink()
        return True
    return False


def tao_thu_muc(duong_dan):
    Path(duong_dan).mkdir(parents=True, exist_ok=True)
    return True
