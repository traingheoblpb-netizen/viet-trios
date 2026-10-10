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


def test_ham_va_tra_ve():
    ket_qua = chay_ma('ham tong(a, b):\n    tra_ve a + b\nin ra tong(2, 3)')
    assert ket_qua == '5'


def test_lop_va_phuong_thuc():
    ket_qua = chay_ma('lop Nguoi:\n    ham xin_chao(self, ten):\n        in ra "Xin chao " + ten\nnguoi = Nguoi()\nnguoi.xin_chao("Tuan")')
    assert 'Xin chao Tuan' in ket_qua


def test_tu_dien():
    ket_qua = chay_ma('data = {"ten": "Tuan", "tuoi": 20}\nin ra data["ten"]')
    assert ket_qua == 'Tuan'


def test_danh_sach():
    ket_qua = chay_ma('list = [1, 2, 3]\nin ra list[1]')
    assert ket_qua == '2'


def test_bien_bool():
    ket_qua = chay_ma('dung_vai = dung\nin ra dung_vai')
    assert ket_qua == 'True'


def test_len_hang():
    ket_qua = chay_ma('list = [1, 2, 3]\nin ra len(list)')
    assert ket_qua == '3'


def test_vong_lap_tren_chuoi():
    ket_qua = chay_ma('lap ky_tu trong ["a", "b", "c"]:\n    in ra ky_tu')
    assert 'a' in ket_qua and 'b' in ket_qua and 'c' in ket_qua


def test_he_thong_chuyen_doi():
    ket_qua = chay_ma('x = 10\nneu x >= 10:\n    in ra "dat"')
    assert ket_qua == 'dat'


def test_doi_tuong_nhan_bien():
    ket_qua = chay_ma('lop Xe:\n    ham in_ra_ten(self):\n        in ra "Xe"\nxe = Xe()\nxe.in_ra_ten()')
    assert ket_qua == 'Xe'
