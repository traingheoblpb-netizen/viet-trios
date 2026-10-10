# Standard Library Strings - Thu vien xu ly chuoi


def noi(chuoi1, chuoi2):
    return str(chuoi1) + str(chuoi2)


def do_dai(chuoi):
    return len(str(chuoi))


def chu_hoa(chuoi):
    return str(chuoi).upper()


def chu_thuong(chuoi):
    return str(chuoi).lower()


def cat_chuoi(chuoi, dau, cuoi):
    return str(chuoi)[dau:cuoi]


def thay_the(chuoi, cu, moi):
    return str(chuoi).replace(str(cu), str(moi))


def tach_chuoi(chuoi, phan_tach=" "):
    return str(chuoi).split(str(phan_tach))


def tim_kiem(chuoi, tu_khoa):
    return str(chuoi).find(str(tu_khoa))
