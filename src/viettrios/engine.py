from __future__ import annotations

from typing import Any, Dict

from .core import chay_ma


class EngineVietTrios:
    def __init__(self):
        self.scop: Dict[str, Any] = {}

    def chay(self, nguon: str) -> str:
        return chay_ma(nguon, self.scop)

    def dat_bien(self, ten: str, gia_tri: Any) -> None:
        self.scop[ten] = gia_tri

    def lay_bien(self, ten: str) -> Any:
        return self.scop.get(ten)

    def xoa_bien(self, ten: str) -> None:
        if ten in self.scop:
            del self.scop[ten]

    def mo_rong(self, ten: str, gia_tri: Any) -> None:
        self.scop[ten] = gia_tri


def tao_engine() -> EngineVietTrios:
    return EngineVietTrios()
