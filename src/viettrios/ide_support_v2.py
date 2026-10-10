# IDE support cap cao


class VietTriosIDE:
    def __init__(self):
        self.plugins = ["vscode", "pycharm", "neovim"]

    def get_plugins(self):
        return self.plugins

    def cung_cap_ho_tro(self):
        return {"status": "hoat_dong", "plugins": self.plugins}
