# GUI do hoa / UI va runtime


class VietTriosDesktop:
    def __init__(self):
        self.app_name = "Viet Trios Desktop"

    def tao_thu_muc(self):
        return {"name": self.app_name, "type": "desktop"}

    def chay(self):
        return {"status": "ready", "app": self.app_name}
