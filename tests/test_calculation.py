"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("operand1, operand2, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Addition with decimals
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Division with decimals
])
def test_calculation_operations(operand1, operand2, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    Ensures the Calculation class correctly performs the arithmetic operation
    (specified by 'operation') on two Decimal operands ('operand1' and 'operand2'),
    and that the result matches the expected outcome.
    """
    calc = Calculation(operand1, operand2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    Verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    Checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()