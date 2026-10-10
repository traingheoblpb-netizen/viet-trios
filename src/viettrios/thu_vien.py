def noi_chuoi(*items):
    return "".join(str(item) for item in items)


def doi_chuoi(gia_tri):
    return str(gia_tri)


def dem_so(gia_tri):
    if gia_tri is None:
        return 0
    if hasattr(gia_tri, "__len__"):
        return len(gia_tri)
    return 0


def dao_nguoc(danh_sach):
    return list(reversed(list(danh_sach)))


def loc_so(danh_sach):
    return [item for item in danh_sach if isinstance(item, (int, float))]


def lay_chuoi(gia_tri):
    return str(gia_tri)
