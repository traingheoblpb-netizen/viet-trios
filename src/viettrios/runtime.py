from viettrios.core import chay_ma


class ChayThoi:
    def __init__(self):
        self.scop = {}

    def chay(self, nguon: str) -> str:
        return chay_ma(nguon, self.scop)

    def dat_bien(self, ten: str, gia_tri):
        self.scop[ten] = gia_tri

    def lay_bien(self, ten: str):
        return self.scop.get(ten)

    def xoa_bien(self, ten: str):
        if ten in self.scop:
            del self.scop[ten]
