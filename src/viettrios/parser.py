# Parser v2 - hoan chinh hon

from __future__ import annotations

import re
from enum import Enum
from typing import List, Any


class TokenType(Enum):
    SO = "SO"
    CHUOI = "CHUOI"
    BIEN = "BIEN"
    HAM = "HAM"
    LOP = "LOP"
    NEU = "NEU"
    LAP = "LAP"
    TRONG = "TRONG"
    TRA_VE = "TRA_VE"
    IN_RA = "IN_RA"
    XUAT = "XUAT"
    DUNG = "DUNG"
    SAI = "SAI"
    CONG = "CONG"
    TRU = "TRU"
    NHAN = "NHAN"
    CHIA = "CHIA"
    MOD = "MOD"
    LUY_THUA = "LUY_THUA"
    BANG = "BANG"
    KHAC = "KHAC"
    LON = "LON"
    NHO = "NHO"
    LON_BANG = "LON_BANG"
    NHO_BANG = "NHO_BANG"
    NGOAC_MO = "NGOAC_MO"
    NGOAC_DONG = "NGOAC_DONG"
    NGOAC_VUONG_MO = "NGOAC_VUONG_MO"
    NGOAC_VUONG_DONG = "NGOAC_VUONG_DONG"
    NGOAC_VON_MO = "NGOAC_VON_MO"
    NGOAC_VON_DONG = "NGOAC_VON_DONG"
    DIEM_PHAY = "DIEM_PHAY"
    DUO_CHAM = "DUO_CHAM"
    ASSIGN = "ASSIGN"
    EOF = "EOF"


class Token:
    def __init__(self, kieu: TokenType, gia_tri: Any, hang: int = 1, cot: int = 1):
        self.kieu = kieu
        self.gia_tri = gia_tri
        self.hang = hang
        self.cot = cot

    def __repr__(self):
        return f"Token({self.kieu.name}, {self.gia_tri!r})"


class Tokenizer:
    def __init__(self, ma: str):
        self.ma = ma
        self.vi_tri = 0
        self.hang = 1
        self.cot = 1

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []
        while self.vi_tri < len(self.ma):
            ky_tu = self.ma[self.vi_tri]

            if ky_tu.isspace():
                self._xu_ly_khoang_trang()
                continue

            if ky_tu == '#':
                self._bo_qua_comment()
                continue

            if ky_tu in ('"', "'"):
                tokens.append(self._doc_chuoi())
                continue

            if ky_tu.isdigit() or (ky_tu == '-' and self.vi_tri + 1 < len(self.ma) and self.ma[self.vi_tri + 1].isdigit()):
                tokens.append(self._doc_so())
                continue

            if ky_tu.isalpha() or ky_tu == '_':
                tokens.append(self._doc_bien())
                continue

            if ky_tu in '()[]{}':
                tokens.append(self._doc_ngoac())
                continue

            if ky_tu in '+-*/%':
                tokens.append(self._doc_toan_tu())
                continue

            if ky_tu in '=<>!':
                tokens.append(self._doc_so_sanh())
                continue

            if ky_tu == ',':
                tokens.append(Token(TokenType.DIEM_PHAY, ',', self.hang, self.cot))
                self.vi_tri += 1
                self.cot += 1
                continue

            if ky_tu == ':':
                tokens.append(Token(TokenType.DUO_CHAM, ':', self.hang, self.cot))
                self.vi_tri += 1
                self.cot += 1
                continue

            raise ValueError(f"Ky tu khong ho tro: {ky_tu} tai hang {self.hang}, cot {self.cot}")

        tokens.append(Token(TokenType.EOF, None, self.hang, self.cot))
        return tokens

    def _xu_ly_khoang_trang(self):
        if self.ma[self.vi_tri] == '\n':
            self.hang += 1
            self.cot = 1
        else:
            self.cot += 1
        self.vi_tri += 1

    def _bo_qua_comment(self):
        while self.vi_tri < len(self.ma) and self.ma[self.vi_tri] != '\n':
            self.vi_tri += 1
            self.cot += 1

    def _doc_chuoi(self):
        dau = self.ma[self.vi_tri]
        hang = self.hang
        cot = self.cot
        self.vi_tri += 1
        self.cot += 1
        noi_dung = ""
        while self.vi_tri < len(self.ma) and self.ma[self.vi_tri] != dau:
            if self.ma[self.vi_tri] == '\\':
                self.vi_tri += 1
                self.cot += 1
                if self.vi_tri < len(self.ma):
                    noi_dung += self.ma[self.vi_tri]
            else:
                noi_dung += self.ma[self.vi_tri]
            self.vi_tri += 1
            self.cot += 1
        if self.vi_tri >= len(self.ma):
            raise ValueError("Chuoi khong dong")
        self.vi_tri += 1
        self.cot += 1
        return Token(TokenType.CHUOI, noi_dung, hang, cot)

    def _doc_so(self):
        hang = self.hang
        cot = self.cot
        bat_dau = self.vi_tri
        if self.ma[self.vi_tri] == '-':
            self.vi_tri += 1
            self.cot += 1
        while self.vi_tri < len(self.ma) and (self.ma[self.vi_tri].isdigit() or self.ma[self.vi_tri] == '.'):
            self.vi_tri += 1
            self.cot += 1
        so = self.ma[bat_dau:self.vi_tri]
        return Token(TokenType.SO, float(so) if '.' in so else int(so), hang, cot)

    def _doc_bien(self):
        hang = self.hang
        cot = self.cot
        bat_dau = self.vi_tri
        while self.vi_tri < len(self.ma) and (self.ma[self.vi_tri].isalnum() or self.ma[self.vi_tri] == '_'):
            self.vi_tri += 1
            self.cot += 1
        ten = self.ma[bat_dau:self.vi_tri]
        mapping = {
            'ham': TokenType.HAM,
            'lop': TokenType.LOP,
            'neu': TokenType.NEU,
            'lap': TokenType.LAP,
            'trong': TokenType.TRONG,
            'tra_ve': TokenType.TRA_VE,
            'in_ra': TokenType.IN_RA,
            'xuat': TokenType.XUAT,
            'dung': TokenType.DUNG,
            'sai': TokenType.SAI,
        }
        return Token(mapping.get(ten, TokenType.BIEN), ten, hang, cot)

    def _doc_ngoac(self):
        ky_tu = self.ma[self.vi_tri]
        hang = self.hang
        cot = self.cot
        mapping = {
            '(': TokenType.NGOAC_MO,
            ')': TokenType.NGOAC_DONG,
            '[': TokenType.NGOAC_VUONG_MO,
            ']': TokenType.NGOAC_VUONG_DONG,
            '{': TokenType.NGOAC_VON_MO,
            '}': TokenType.NGOAC_VON_DONG,
        }
        self.vi_tri += 1
        self.cot += 1
        return Token(mapping[ky_tu], ky_tu, hang, cot)

    def _doc_toan_tu(self):
        ky_tu = self.ma[self.vi_tri]
        hang = self.hang
        cot = self.cot
        mapping = {
            '+': TokenType.CONG,
            '-': TokenType.TRU,
            '*': TokenType.NHAN,
            '/': TokenType.CHIA,
            '%': TokenType.MOD,
        }
        if ky_tu == '*' and self.vi_tri + 1 < len(self.ma) and self.ma[self.vi_tri + 1] == '*':
            self.vi_tri += 2
            self.cot += 2
            return Token(TokenType.LUY_THUA, '**', hang, cot)
        self.vi_tri += 1
        self.cot += 1
        return Token(mapping[ky_tu], ky_tu, hang, cot)

    def _doc_so_sanh(self):
        hang = self.hang
        cot = self.cot
        ky_tu = self.ma[self.vi_tri]
        if self.vi_tri + 1 < len(self.ma) and self.ma[self.vi_tri + 1] == '=':
            token_map = {
                '=': TokenType.BANG,
                '>': TokenType.LON_BANG,
                '<': TokenType.NHO_BANG,
                '!': TokenType.KHAC,
            }
            self.vi_tri += 2
            self.cot += 2
            return Token(token_map[ky_tu], ky_tu + '=', hang, cot)
        
        token_map = {
            '=': TokenType.ASSIGN,
            '>': TokenType.LON,
            '<': TokenType.NHO,
        }
        self.vi_tri += 1
        self.cot += 1
        return Token(token_map[ky_tu], ky_tu, hang, cot)
