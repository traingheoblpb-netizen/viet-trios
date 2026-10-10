from viettrios.engine import tao_engine


def test_engine():
    engine = tao_engine()
    ket_qua = engine.chay('in ra "xin chao"')
    assert ket_qua == 'xin chao'


def test_engine_bien():
    engine = tao_engine()
    engine.chay('x = 5\nin ra x')
    assert engine.lay_bien('x') == 5
