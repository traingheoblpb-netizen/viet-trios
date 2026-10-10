import pytest

from viettrios.core import run_code


def test_basic_print():
    result = run_code('in ra "Xin chao"')
    assert result == 'Xin chao'


def test_assignment_and_condition():
    result = run_code('x = 7\nneu x > 5:\n    in ra "x lon hon 5"')
    assert result == 'x lon hon 5'
