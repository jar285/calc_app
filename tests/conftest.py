# conftest.py
'''Configuration for the tests'''
import pytest
from faker import Faker

@pytest.fixture(scope='session')
def fake_data():
    """Provide a Faker instance for generating fake data."""
    return Faker()

def pytest_addoption(parser):
    '''adjust the test data volume'''
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate")

@pytest.fixture
def num_records(request):
    '''Return the number of records to generate.'''
    return request.config.getoption("--num_records")
