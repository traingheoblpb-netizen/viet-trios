# Tests cho engine v2

from viettrios.parser import Tokenizer, TokenType
from viettrios.compiler import Compiler
from viettrios.engine_v2 import EngineVietTriosV2


def test_tokenizer():
    ma = 'in_ra "Xin chao"'
    tokenizer = Tokenizer(ma)
    tokens = tokenizer.tokenize()
    assert tokens[0].kieu == TokenType.IN_RA
    assert tokens[1].kieu == TokenType.CHUOI


def test_compiler():
    ma = 'in_ra "Xin chao"'
    tokenizer = Tokenizer(ma)
    tokens = tokenizer.tokenize()
    compiler = Compiler(tokens)
    bytecode = compiler.compile()
    assert bytecode is not None


def test_stdlib_math():
    from viettrios.stdlib_toan_hoc import cong, tru
    assert cong(2, 3) == 5
    assert tru(5, 2) == 3


def test_stdlib_string():
    from viettrios.stdlib_chuoi import noi, do_dai
    assert noi("Xin", "chao") == "Xinchao"
    assert do_dai("Hello") == 5
