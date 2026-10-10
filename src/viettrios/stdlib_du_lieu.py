# Standard Library Data - Thu vien du lieu

import json


def tao_tu_dien(**kwargs):
    return dict(kwargs)


def tao_danh_sach(*items):
    return list(items)


def lap_qua_danh_sach(danh_sach):
    for item in danh_sach:
        yield item


def loc_du_lieu(danh_sach, dieu_kien):
    return [item for item in danh_sach if dieu_kien(item)]


def map_du_lieu(danh_sach, ham):
    return [ham(item) for item in danh_sach]
