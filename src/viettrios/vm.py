# Virtual Machine v2

from typing import Any, Dict, List
from .compiler import Bytecode


class VirtualMachine:
    def __init__(self):
        self.stack: List[Any] = []
        self.scope: Dict[str, Any] = {}

    def run(self, bytecode: Bytecode):
        for op, args in bytecode.instructions:
            if op == 'PRINT':
                if self.stack:
                    print(self.stack.pop())
            elif op == 'ASSIGN':
                pass
        return None
