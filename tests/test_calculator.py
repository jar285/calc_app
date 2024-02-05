'''Testing the calculator class'''
from calculator import Calculator

def test_add():
    '''Test that calculator addind works'''
    assert Calculator.add(2,2) == 4

def test_subtract():
    '''Test that calculator substraction works'''
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that calculator multiply works'''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that calculator divide works'''
    assert Calculator.divide(2,2) == 1
