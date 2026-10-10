from viettrios.compiler import Compiler, Bytecode
from viettrios.vm import VirtualMachine
from viettrios.parser import Tokenizer
from viettrios.stdlib_toan_hoc import *
from viettrios.stdlib_chuoi import *
from viettrios.stdlib_tep import *
from viettrios.stdlib_mang import *
from viettrios.stdlib_du_lieu import *


class EngineVietTriosV2:
    """Engine v2 voi parser, compiler va VM"""
    
    def __init__(self):
        self.vm = VirtualMachine()
    
    def chay(self, ma: str):
        # Tokenize
        tokenizer = Tokenizer(ma)
        tokens = tokenizer.tokenize()
        
        # Compile
        compiler = Compiler(tokens)
        bytecode = compiler.compile()
        
        # Run
        ket_qua = self.vm.chay(bytecode)
        return ket_qua
