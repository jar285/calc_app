'''Imported pytest and calculator folder to test_calculator'''
import pytest
from calculator import Calculator

def test_addition():
    """Test that addition function works."""
    assert Calculator.add(2, 2) == 4
    assert Calculator.get_last_calculation() == "Added 2 to 2 got 4"

def test_subtraction():
    """Test that subtraction function works."""
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.get_last_calculation() == "Subtracted 2 from 2 got 0"

def test_multiplication():
    """Test that multiply function works."""
    assert Calculator.multiply(2, 2) == 4
    assert Calculator.get_last_calculation() == "Multiplied 2 with 2 got 4"

def test_division():
    """Test that divide function works."""
    assert Calculator.divide(2, 2) == 1.0
    assert Calculator.get_last_calculation() == "Divided 2 by 2 got 1.0"


def test_divide_by_zero():
    """Test dividing by zero throws an exception."""
    with pytest.raises(ValueError) as e:
        Calculator.divide(2, 0)
    assert str(e.value) == "Cannot divide by zero."

def test_calculation_history():
    """Test the calculation history tracking."""
    Calculator.add(1, 1)  # Resetting history for this test
    Calculator.subtract(2, 1)
    assert Calculator.history[-2] == "Added 1 to 1 got 2"
    assert Calculator.history[-1] == "Subtracted 1 from 2 got 1"
