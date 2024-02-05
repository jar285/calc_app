'''Testing the calculator class'''
from calculator import calculator

def test_calculator():
    '''Test that calculator addind works'''
    assert calculator.add(2,2) == 4
