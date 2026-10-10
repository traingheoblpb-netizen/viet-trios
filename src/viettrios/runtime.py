from .core import chay_ma


class ChayThoi:
    def __init__(self):
        self.scop = {}

    def chay(self, nguon: str) -> str:
        return chay_ma(nguon, self.scop)
