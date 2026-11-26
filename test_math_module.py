import pytest
from math_module import factorial, is_even


def test_factorial_basic():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


@pytest.mark.parametrize("n, expected", [(2, 2), (3, 6), (4, 24), (10, 3628800)])
def test_factorial_parametrized(n, expected):
    assert factorial(n) == expected


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        factorial(2.5)


@pytest.mark.parametrize("n, expected", [(0, True), (1, False), (2, True), (-3, False)])
def test_is_even(n, expected):
    assert is_even(n) == expected