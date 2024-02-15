# Project Install Instructions


## Install

1. clone
2. pip install -r requirements.txt

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## The objective of this homework assignment is to create your own 

Your goal in this homeowrk is to design your own calculator from scratch using the techniuqes that you can figure out based on my examples.  Your calculator needs to do the following:

1. Add, Subtract, Multiply, and Divide
2. Throw exception for divide by zero and test that the exception is thrown
3. Use at least one class, at least one static method, at least one class method.
4. It needs to  store a history of calculations, so that you can retrieve the last calculation, add a calculation, 
5. It needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code.  
6.  You should use type hints for input parameter types and return types.
7.  Implement a pytest fixture to test the 

## Grading:

1.  20  Points for (add subtract, multiply, divide) 
2.  10 Points for exception throwing and testing on divide by zero
3.  30 points each for using static, class, and instance methods correctly
4.  5 Points for having a calculation class that stores the arthitmentic operation in a instance property.
5.  15 Points for having a calculation history to store calculation instances
6.  10 Points for having the convenience methods on the calculations class to manage the history
7.  10 Points for using parameterized test data
