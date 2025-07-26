"""
Unit tests for the calculator module using pytest.
"""

import pytest
from app.calculator import add, subtract, multiply, divide

def test_add():
    """Test the add function with positive and negative numbers."""
    assert add(3, 5) == 8
    assert add(-2, 4) == 2

def test_subtract():
    """Test the subtract function with positive and negative results."""
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6

def test_multiply():
    """Test the multiply function with various values."""
    assert multiply(3, 5) == 15
    assert multiply(0, 100) == 0

def test_divide():
    """Test the divide function and division by zero."""
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)