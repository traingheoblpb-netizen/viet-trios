# Compiler v2

from typing import List
from .parser import Token, TokenType


class Bytecode:
    def __init__(self):
        self.instructions = []

    def emit(self, op, *args):
        self.instructions.append((op, args))


class Compiler:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = 0

    def compile(self) -> Bytecode:
        bc = Bytecode()
        while self.index < len(self.tokens):
            token = self.tokens[self.index]
            if token.kieu == TokenType.EOF:
                break
            if token.kieu == TokenType.IN_RA:
                self.index += 1
                # compile expression after IN_RA
                bc.emit('PRINT')
            elif token.kieu == TokenType.ASSIGN:
                bc.emit('ASSIGN')
                self.index += 1
            else:
                self.index += 1
        return bc
