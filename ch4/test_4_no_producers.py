from starting_point import Province


def test_shortfall(no_producers):
    assert no_producers.shortfall == 30


def test_profit(no_producers):
    assert no_producers.profit == 0
