import pytest
from starting_point import Province


@pytest.fixture
def asia(sample_province_data) -> Province:
    return Province(sample_province_data)


@pytest.fixture
def sample_province_data():
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


@pytest.fixture
def no_producers() -> Province:
    return Province({"name": "No producers", "producers": [], "demand": 30, "price": 20,})
