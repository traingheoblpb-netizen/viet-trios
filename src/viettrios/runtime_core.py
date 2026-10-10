# Tich hop runtime tu standards

from viettrios.engine_v2 import EngineVietTriosV2
from viettrios.desktop import VietTriosDesktop
from viettrios.ide_support_v2 import VietTriosIDE


class VietTriosRuntime:
    def __init__(self):
        self.engine = EngineVietTriosV2()
        self.desktop = VietTriosDesktop()
        self.ide = VietTriosIDE()

    def run_script(self, ma: str):
        return self.engine.chay(ma)

    def run_desktop(self):
        return self.desktop.chay()

    def provide_ide_support(self):
        return self.ide.cung_cap_ho_tro()
