# Standard Library Network - Thu vien mang

import json
from urllib.request import urlopen
from urllib.error import URLError


def lay_http(url):
    try:
        voi = urlopen(url, timeout=5)
        noi_dung = voi.read().decode('utf-8')
        return noi_dung
    except URLError:
        return None


def phan_tich_json(chuoi_json):
    return json.loads(str(chuoi_json))


def tao_json(du_lieu):
    return json.dumps(du_lieu, ensure_ascii=False)
