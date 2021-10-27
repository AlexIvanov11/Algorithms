import pytest
from Lesson_1 import array_shift


def test_wrong_value():
    with pytest.raises(TypeError) as excinfo:
        array_shift("Accidental string", 3)
    assert "value" in str(excinfo)


def test_float_positions():
    with pytest.raises(TypeError) as excinfo:
        array_shift([1, 2, 3], 22.5)
    assert "integer" in str(excinfo)


def test_empty():
    with pytest.raises(ValueError) as excinfo:
        array_shift([], 20)
    assert "Empty" in str(excinfo)


def test_single():
    test_arr = [1]
    res = array_shift(test_arr, 1000)
    assert res == test_arr


def test_shift():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = array_shift(test_arr, 5)
    assert res == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


def test_full_circle():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = array_shift(test_arr, 20)
    assert res == test_arr


def test_a_lot():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = array_shift(test_arr, 25)
    assert res == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
