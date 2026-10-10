from viettrios.ecosystem import thong_tin_ecosystem


def test_ecosystem():
    data = thong_tin_ecosystem()
    assert data["ten"] == "Viet Trios"
    assert "cli" in data["tinh_nang"]
