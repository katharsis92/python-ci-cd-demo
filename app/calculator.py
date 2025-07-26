"""
A simple calculator module that provides basic arithmetic operations.

Functions:
    add(a, b): Return the sum of a and b.
    subtract(a, b): Return the difference of a and b.
    multiply(a, b): Return the product of a and b.
    divide(a, b): Return the quotient of a and b. Raises an error if dividing by zero.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract one number from another.

    Args:
        a (float): Number to subtract from.
        b (float): Number to subtract.

    Returns:
        float: The result of a - b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide one number by another.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: The result of a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b