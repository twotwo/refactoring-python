import pytest


def test_shortfall(no_producers):
    assert no_producers.shortfall == 30


def test_profit(no_producers):
    assert no_producers.profit == 0


def test_zero_demand(asia):
    asia.set_demand(0)
    assert asia.shortfall == -25
    assert asia.profit == 0


def test_negative_demand(asia):
    asia.set_demand(-1)
    assert asia.shortfall == -26
    assert asia.profit == -10


def test_empty_string_demand(asia):
    asia.set_demand("")
    with pytest.raises(TypeError):
        asia.shortfall
    with pytest.raises(TypeError):
        asia.profit
