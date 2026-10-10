# Engine v2 chinh thuc

from .parser import Tokenizer
from .compiler import Compiler
from .vm import VirtualMachine


class EngineVietTriosV2:
    def __init__(self):
        self.vm = VirtualMachine()

    def chay(self, ma: str):
        tokenizer = Tokenizer(ma)
        tokens = tokenizer.tokenize()
        compiler = Compiler(tokens)
        bytecode = compiler.compile()
        return self.vm.run(bytecode)
