# Compiler va optimizer cho Viet Trios

from typing import List, Any, Dict
from .parser import Token, TokenType


class Bytecode:
    def __init__(self):
        self.cac_lenh = []
        self.so_hieu = {}
    
    def them_lenh(self, lenh: str, *args):
        chi_so = len(self.cac_lenh)
        self.cac_lenh.append((lenh, args))
        return chi_so
    
    def dat_so_hieu(self, ten: str):
        self.so_hieu[ten] = len(self.cac_lenh)
    
    def __repr__(self):
        return f"Bytecode({len(self.cac_lenh)} cac_lenh)"


class Compiler:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.vi_tri = 0
        self.bytecode = Bytecode()
    
    def compile(self) -> Bytecode:
        while not self._la_cuoi():
            self._compile_cau_lenh()
        return self.bytecode
    
    def _la_cuoi(self):
        return self._token_hien_tai().kieu == TokenType.EOF
    
    def _token_hien_tai(self):
        if self.vi_tri < len(self.tokens):
            return self.tokens[self.vi_tri]
        return self.tokens[-1]
    
    def _token_tiep_theo(self):
        self.vi_tri += 1
    
    def _compile_cau_lenh(self):
        token = self._token_hien_tai()
        if token.kieu == TokenType.IN_RA:
            self._compile_in_ra()
        elif token.kieu == TokenType.HAM:
            self._compile_ham()
        elif token.kieu == TokenType.LOP:
            self._compile_lop()
        else:
            self._token_tiep_theo()
    
    def _compile_in_ra(self):
        self._token_tiep_theo()
        self.bytecode.them_lenh("in_ra")
    
    def _compile_ham(self):
        self._token_tiep_theo()
        self.bytecode.them_lenh("ham")
    
    def _compile_lop(self):
        self._token_tiep_theo()
        self.bytecode.them_lenh("lop")
