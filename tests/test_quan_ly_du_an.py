from viettrios.quan_ly_du_an import tao_du_an_mau


def test_du_an_mau():
    root = tao_du_an_mau("demo_app")
    assert "demo_app" in root
