import pytest
from viettrios.core import chay_ma


def test_in_ra_co_ban():
    ket_qua = chay_ma('in ra "Xin chao"')
    assert ket_qua == 'Xin chao'


def test_gan_bien():
    ket_qua = chay_ma('x = 5\nin ra x')
    assert ket_qua == '5'


def test_phep_cong():
    ket_qua = chay_ma('x = 5\ny = 3\nz = x + y\nin ra z')
    assert ket_qua == '8'


def test_dieu_kien_dung():
    ket_qua = chay_ma('x = 10\nneu x > 5:\n    in ra "lon"')
    assert ket_qua == 'lon'


def test_dieu_kien_sai():
    ket_qua = chay_ma('x = 3\nneu x > 5:\n    in ra "lon"')
    assert ket_qua == ''


def test_vong_lap():
    ket_qua = chay_ma('lap i trong [1, 2, 3]:\n    in ra i')
    assert '1' in ket_qua and '2' in ket_qua and '3' in ket_qua


def test_bien_chuoi():
    ket_qua = chay_ma('ten = "Tuan"\nin ra ten')
    assert ket_qua == 'Tuan'


def test_phep_nhan():
    ket_qua = chay_ma('x = 4\ny = 5\nz = x * y\nin ra z')
    assert ket_qua == '20'
