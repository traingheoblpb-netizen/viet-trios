# Standard Library Math - Thu vien toan hoc chuan

import math as py_math


def cong(a, b):
    return a + b


def tru(a, b):
    return a - b


def nhan(a, b):
    return a * b


def chia(a, b):
    if b == 0:
        raise ValueError("Khong the chia cho 0")
    return a / b


def luy_thua(a, b):
    return a ** b


def can_bac_hai(a):
    if a < 0:
        raise ValueError("Can bac hai cua so am")
    return py_math.sqrt(a)


def sin(x):
    return py_math.sin(x)


def cos(x):
    return py_math.cos(x)


def tan(x):
    return py_math.tan(x)


def log(x, co_so=py_math.e):
    return py_math.log(x, co_so)


def exp(x):
    return py_math.exp(x)
