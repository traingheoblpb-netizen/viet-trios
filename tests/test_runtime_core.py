# Tests cho runtime cap cao

from viettrios.runtime_core import VietTriosRuntime
from viettrios.parser import Tokenizer, TokenType


def test_tokenizer_basic():
    tokens = Tokenizer('in_ra "Xin chao"').tokenize()
    assert tokens[0].kieu == TokenType.IN_RA


def test_runtime_desktop():
    runtime = VietTriosRuntime()
    info = runtime.run_desktop()
    assert info["status"] == "ready"


def test_ide_support():
    runtime = VietTriosRuntime()
    info = runtime.provide_ide_support()
    assert info["status"] == "hoat_dong"


def test_runtime_script_empty():
    runtime = VietTriosRuntime()
    assert runtime.run_script('') is None
