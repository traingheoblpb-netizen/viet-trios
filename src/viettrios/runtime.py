from .core import chay_ma


class ChayThoi:
    def __init__(self):
        self.scop = {}

    def chay(self, nguon: str) -> str:
        return chay_ma(nguon, self.scop)

    def lay_bien(self, ten: str):
        return self.scop.get(ten, None)

    def dat_bien(self, ten: str, gia_tri):
        self.scop[ten] = gia_tri
