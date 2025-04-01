import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

def test_subtract():
    assert calc.subtract(5, 3) == 2

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(1, 0)