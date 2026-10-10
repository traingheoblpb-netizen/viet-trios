# Virtual Machine - Cau nhan cua Viet Trios

from typing import Any, Dict, List
from .compiler import Bytecode


class VirtualMachine:
    def __init__(self):
        self.stack: List[Any] = []
        self.bien: Dict[str, Any] = {}
        self.ham_tuc_thoi: Dict[str, Any] = {}
    
    def chay(self, bytecode: Bytecode) -> Any:
        for lenh, args in bytecode.cac_lenh:
            self._xu_ly_lenh(lenh, args)
        return self.stack[-1] if self.stack else None
    
    def _xu_ly_lenh(self, lenh: str, args: tuple):
        if lenh == "in_ra":
            print(self.stack.pop() if self.stack else "")
        elif lenh == "ham":
            pass
        elif lenh == "lop":
            pass
        else:
            raise ValueError(f"Lenh khong ho tro: {lenh}")
