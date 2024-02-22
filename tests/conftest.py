'''imported pytest and faker to conftest.py'''
import pytest
from faker import Faker
from calculator import Calculator

@pytest.fixture(scope='session')
def fake_data():
    """Provide a Faker instance for generating fake data."""
    return Faker()


def test_addition(fake_data):
    """Addition function"""
    a = fake_data.random_number(digits=2)
    b = fake_data.random_number(digits=2)
    expected_result = a + b
    assert Calculator.add(a, b) == expected_result
    assert Calculator.get_last_calculation() == f"Added {a} to {b} got {expected_result}"
