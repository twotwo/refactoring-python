from starting_point import Province


def get_sample_province_data():
    return {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6},
        ],
        "demand": 30,
        "price": 20,
    }


def test_province():
    asia = Province(get_sample_province_data())
    assert 5 == asia.shortfall
