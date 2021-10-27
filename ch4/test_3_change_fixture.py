def test_change_production(asia):
    asia.producers[0].set_production(20)
    assert -6 == asia.shortfall
    assert 292 == asia.profit
