class Calculator:
    '''Class variable to store history of calculations'''
    history = []

    def __init__(self):
        '''This can be used for instance-specific properties if needed'''
        pass

    @staticmethod
    def add(a: float, b: float) -> float:
        '''Adds two numbers and appends the result to the calculation history.'''
        result = a + b
        Calculator.history.append(f"Added {a} to {b} got {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        '''Subtracts the second number from the first and appends the result to the calculation history.'''
        result = a - b
        Calculator.history.append(f"Subtracted {b} from {a} got {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        '''Multiplies two numbers and appends the result to the calculation history.'''
        result = a * b
        Calculator.history.append(f"Multiplied {a} with {b} got {result}")
        return result

    @classmethod
    def divide(cls, a: float, b: float) -> float:
        '''Divides the first number by the second and appends the result to the calculation history.
    Raises a ValueError if the second number is zero.'''
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        cls.history.append(f"Divided {a} by {b} got {result}")
        return result

    @classmethod
    def get_last_calculation(cls) -> str:
        if cls.history:
            return cls.history[-1]
        else:
            return "No calculation history."


    @classmethod
    def add_calculation(cls, calculation: str) -> None:
        '''Retrieves the last entry from the calculation history.'''
        cls.history.append(calculation)
