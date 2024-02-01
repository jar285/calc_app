"""My Calculator Test"""
from calculator import add, substract

def test_addition():
    """Test that addition function works"""
    assert add (2,2) == 4

def test_subtraction():
    """Test that substraction function works """
    assert substract(2,2) == 0
