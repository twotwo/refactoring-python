from starting_point import Province


def test_shortfall(asia):
    assert 5 == asia.shortfall


def test_profit(asia):
    assert 230 == asia.profit
