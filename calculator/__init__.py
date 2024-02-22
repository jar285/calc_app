from .operations import add, subtract, multiply, divide

class Calculator:
    '''Class variable to store history of calculations'''
    history = []

    def __init__(self):
        '''This can be used for instance-specific properties if needed'''
        pass

    @classmethod
    def add(cls, a: float, b: float) -> float:
        result = add(a, b)
        cls.history.append(f"Added {a} to {b} got {result}")
        return result

    @classmethod
    def subtract(cls, a: float, b: float) -> float:
        result = subtract(a, b)
        cls.history.append(f"Subtracted {b} from {a} got {result}")
        return result

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        result = multiply(a, b)
        cls.history.append(f"Multiplied {a} with {b} got {result}")
        return result

    @classmethod
    def divide(cls, a: float, b: float) -> float:
        result = divide(a, b)
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
        cls.history.append(calculation)
