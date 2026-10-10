from viettrios.thu_vien import noi_chuoi, dem_so, dao_nguoc, loc_so


def test_noi_chuoi():
    assert noi_chuoi("Xin ", "chao") == "Xin chao"


def test_dem_so():
    assert dem_so([1, 2, 3]) == 3


def test_dao_nguoc():
    assert dao_nguoc([1, 2, 3]) == [3, 2, 1]


def test_loc_so():
    assert loc_so([1, "a", 2, "b"]) == [1, 2]
