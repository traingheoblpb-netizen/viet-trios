# Core Parser cho Viet Trios

import re
from enum import Enum
from typing import List, Tuple, Any


class TokenType(Enum):
    # Literals
    SO = "SO"
    CHUOI = "CHUOI"
    DUNG = "DUNG"
    SAI = "SAI"
    
    # Keywords
    HAM = "HAM"
    LOP = "LOP"
    NEU = "NEU"
    LAP = "LAP"
    TRONG = "TRONG"
    TRA_VE = "TRA_VE"
    IN_RA = "IN_RA"
    XUAT = "XUAT"
    
    # Operators
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
    VA = "VA"
    HOAC = "HOAC"
    KHONG = "KHONG"
    
    # Delimiters
    NGOAC_MO = "NGOAC_MO"
    NGOAC_DONG = "NGOAC_DONG"
    NGOAC_VON_MO = "NGOAC_VON_MO"
    NGOAC_VON_DONG = "NGOAC_VON_DONG"
    NGOAC_VUONG_MO = "NGOAC_VUONG_MO"
    NGOAC_VUONG_DONG = "NGOAC_VUONG_DONG"
    DIEM_PHAY = "DIEM_PHAY"
    DIEM_THAN = "DIEM_THAN"
    DUO_CHAM = "DUO_CHAM"
    
    # Special
    TRANG_THAB = "TRANG_THAB"
    TIEN_TA = "TIEN_TA"
    EOF = "EOF"


class Token:
    def __init__(self, kieu: TokenType, gia_tri: Any, hang: int, cot: int):
        self.kieu = kieu
        self.gia_tri = gia_tri
        self.hang = hang
        self.cot = cot
    
    def __repr__(self):
        return f"Token({self.kieu}, {self.gia_tri}, {self.hang}, {self.cot})"


class Tokenizer:
    def __init__(self, ma: str):
        self.ma = ma
        self.vi_tri = 0
        self.hang = 1
        self.cot = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        while self.vi_tri < len(self.ma):
            self._bo_qua_khoang_trang()
            if self.vi_tri >= len(self.ma):
                break
            
            ky_tu = self.ma[self.vi_tri]
            
            if ky_tu == '#':
                self._bo_qua_comment()
                continue
            
            if ky_tu == '"' or ky_tu == "'":
                self._doc_chuoi(ky_tu)
            elif ky_tu.isdigit():
                self._doc_so()
            elif ky_tu.isalpha() or ky_tu == '_':
                self._doc_tien_ta()
            elif ky_tu in '(){}[]':
                self._doc_ngoac(ky_tu)
            elif ky_tu in '+-*/%':
                self._doc_toan_tu(ky_tu)
            elif ky_tu == '=':
                self._doc_gan()
            elif ky_tu == '.':
                self.tokens.append(Token(TokenType.DIEM_THAN, '.', self.hang, self.cot))
                self.vi_tri += 1
                self.cot += 1
            elif ky_tu == ',':
                self.tokens.append(Token(TokenType.DIEM_PHAY, ',', self.hang, self.cot))
                self.vi_tri += 1
                self.cot += 1
            elif ky_tu == ':':
                self.tokens.append(Token(TokenType.DUO_CHAM, ':', self.hang, self.cot))
                self.vi_tri += 1
                self.cot += 1
            else:
                self.vi_tri += 1
                self.cot += 1
        
        self.tokens.append(Token(TokenType.EOF, None, self.hang, self.cot))
        return self.tokens
    
    def _bo_qua_khoang_trang(self):
        while self.vi_tri < len(self.ma) and self.ma[self.vi_tri].isspace():
            if self.ma[self.vi_tri] == '\n':
                self.hang += 1
                self.cot = 1
            else:
                self.cot += 1
            self.vi_tri += 1
    
    def _bo_qua_comment(self):
        while self.vi_tri < len(self.ma) and self.ma[self.vi_tri] != '\n':
            self.vi_tri += 1
    
    def _doc_chuoi(self, quote):
        hang_bat_dau = self.hang
        cot_bat_dau = self.cot
        self.vi_tri += 1
        self.cot += 1
        noi_dung = ''
        while self.vi_tri < len(self.ma) and self.ma[self.vi_tri] != quote:
            if self.ma[self.vi_tri] == '\\':
                self.vi_tri += 1
                if self.vi_tri < len(self.ma):
                    noi_dung += self.ma[self.vi_tri]
                    self.vi_tri += 1
            else:
                noi_dung += self.ma[self.vi_tri]
                self.vi_tri += 1
            self.cot += 1
        self.vi_tri += 1
        self.cot += 1
        self.tokens.append(Token(TokenType.CHUOI, noi_dung, hang_bat_dau, cot_bat_dau))
    
    def _doc_so(self):
        hang_bat_dau = self.hang
        cot_bat_dau = self.cot
        so = ''
        while self.vi_tri < len(self.ma) and (self.ma[self.vi_tri].isdigit() or self.ma[self.vi_tri] == '.'):
            so += self.ma[self.vi_tri]
            self.vi_tri += 1
            self.cot += 1
        if '.' in so:
            gia_tri = float(so)
        else:
            gia_tri = int(so)
        self.tokens.append(Token(TokenType.SO, gia_tri, hang_bat_dau, cot_bat_dau))
    
    def _doc_tien_ta(self):
        hang_bat_dau = self.hang
        cot_bat_dau = self.cot
        ten = ''
        while self.vi_tri < len(self.ma) and (self.ma[self.vi_tri].isalnum() or self.ma[self.vi_tri] == '_'):
            ten += self.ma[self.vi_tri]
            self.vi_tri += 1
            self.cot += 1
        
        keywords = {
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
            'va': TokenType.VA,
            'hoac': TokenType.HOAC,
            'khong': TokenType.KHONG,
        }
        
        if ten in keywords:
            self.tokens.append(Token(keywords[ten], ten, hang_bat_dau, cot_bat_dau))
        else:
            self.tokens.append(Token(TokenType.TIEN_TA, ten, hang_bat_dau, cot_bat_dau))
    
    def _doc_ngoac(self, ky_tu):
        hang = self.hang
        cot = self.cot
        token_map = {
            '(': TokenType.NGOAC_MO,
            ')': TokenType.NGOAC_DONG,
            '{': TokenType.NGOAC_VON_MO,
            '}': TokenType.NGOAC_VON_DONG,
            '[': TokenType.NGOAC_VUONG_MO,
            ']': TokenType.NGOAC_VUONG_DONG,
        }
        self.tokens.append(Token(token_map[ky_tu], ky_tu, hang, cot))
        self.vi_tri += 1
        self.cot += 1
    
    def _doc_toan_tu(self, ky_tu):
        hang = self.hang
        cot = self.cot
        if self.vi_tri + 1 < len(self.ma):
            ky_tu_tiep = self.ma[self.vi_tri + 1]
            if ky_tu == '*' and ky_tu_tiep == '*':
                self.tokens.append(Token(TokenType.LUY_THUA, '**', hang, cot))
                self.vi_tri += 2
                self.cot += 2
                return
        
        token_map = {
            '+': TokenType.CONG,
            '-': TokenType.TRU,
            '*': TokenType.NHAN,
            '/': TokenType.CHIA,
            '%': TokenType.MOD,
        }
        self.tokens.append(Token(token_map[ky_tu], ky_tu, hang, cot))
        self.vi_tri += 1
        self.cot += 1
    
    def _doc_gan(self):
        hang = self.hang
        cot = self.cot
        if self.vi_tri + 1 < len(self.ma) and self.ma[self.vi_tri + 1] == '=':
            self.tokens.append(Token(TokenType.BANG, '==', hang, cot))
            self.vi_tri += 2
            self.cot += 2
        else:
            self.tokens.append(Token(TokenType.TRANG_THAB, '=', hang, cot))
            self.vi_tri += 1
            self.cot += 1
