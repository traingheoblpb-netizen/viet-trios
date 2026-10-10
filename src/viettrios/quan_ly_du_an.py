from viettrios.ho_tro_he_thong import tao_thu_muc, tao_tep, doc_tep, xoa_tep


def tao_du_an_mau(ten_du_an: str):
    root = tao_thu_muc(ten_du_an)
    tao_thu_muc(f"{root}/src")
    tao_thu_muc(f"{root}/tests")
    tao_tep(f"{root}/README.md", f"# {ten_du_an}\n\nDu an Viet Trios mau.\n")
    tao_tep(f"{root}/app.vt", 'in ra "Xin chao Viet Trios"\n')
    return root


def doc_du_lieu(duong_dan: str):
    return doc_tep(duong_dan)


def xoa_du_an(duong_dan: str):
    return xoa_tep(duong_dan)
