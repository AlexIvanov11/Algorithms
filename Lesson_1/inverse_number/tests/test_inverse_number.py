import pytest
from Lesson_1.inverse_number.source.inverse_number import simple_inverse, math_inverse


def test_simple_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        simple_inverse("string")
    assert "integer" in str(excinfo)


def test_math_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        math_inverse("string")
    assert "integer" in str(excinfo)


def test_simple_negative():
    with pytest.raises(ValueError) as excinfo:
        simple_inverse(-100)
    assert "positive" in str(excinfo)


def test_math_negative():
    with pytest.raises(ValueError) as excinfo:
        math_inverse(-100)
    assert "positive" in str(excinfo)


def test_simple_one_digit():
    res = simple_inverse(5)
    assert res == 5


def test_math_one_digit():
    res = math_inverse(6)
    assert res == 6


def test_simple_round():
    res = simple_inverse(100)
    assert res == 1


def test_math_round():
    res = math_inverse(150)
    assert res == 51


def test_simple():
    res = simple_inverse(1234)
    assert res == 4321


def test_math():
    res = math_inverse(123456)
    assert res == 654321
