from pathlib import Path


def tao_thu_muc(duong_dan: str):
    duong_dan_path = Path(duong_dan)
    duong_dan_path.mkdir(parents=True, exist_ok=True)
    return str(duong_dan_path)


def tao_tep(duong_dan: str, noi_dung: str = ""):
    duong_dan_path = Path(duong_dan)
    duong_dan_path.parent.mkdir(parents=True, exist_ok=True)
    duong_dan_path.write_text(noi_dung, encoding='utf-8')
    return str(duong_dan_path)


def doc_tep(duong_dan: str) -> str:
    return Path(duong_dan).read_text(encoding='utf-8')


def xoa_tep(duong_dan: str):
    path = Path(duong_dan)
    if path.exists():
        path.unlink()
        return True
    return False
