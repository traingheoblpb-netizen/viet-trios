# IDE Plugin support cho Viet Trios


class VietTriosLSP:
    """Language Server Protocol cho Viet Trios"""
    
    def __init__(self):
        self.do_cu = {}
    
    def gan_di_definition(self, ten_bien):
        return f"Variable: {ten_bien}"
    
    def hoan_thanh_tu(self, tien_to):
        keywords = [
            'ham', 'lop', 'neu', 'lap', 'tra_ve', 'in_ra',
            'xuat', 'dung', 'sai', 'va', 'hoac', 'khong'
        ]
        return [k for k in keywords if k.startswith(tien_to)]
    
    def kiem_loi(self, ma):
        errors = []
        # Kiem tra loi co ban
        if ma.count('(') != ma.count(')'):
            errors.append("Ngoac khong can bang")
        return errors


class VietTriosDebugger:
    """Debugger cho Viet Trios"""
    
    def __init__(self):
        self.breakpoints = []
        self.bien_theo_doi = {}
    
    def dat_diem_dung(self, so_dong):
        self.breakpoints.append(so_dong)
    
    def theo_doi_bien(self, ten_bien):
        self.bien_theo_doi[ten_bien] = None
