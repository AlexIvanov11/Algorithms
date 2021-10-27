import pytest
from Lesson_1 import find_average


def test_empty():
    with pytest.raises(ValueError) as excinfo:
        find_average([])
    assert "empty" in str(excinfo)

def test_string():
    with pytest.raises(TypeError) as excinfo:
        find_average("accidental string")
    assert "type" in str(excinfo)

def test_one():
    res = find_average((1))
    assert res == 1


def test_two():
    res = find_average((1, 4))
    assert res == 1


def test_find_average():
    res = find_average((1, 2, 5, 9, 50))
    assert res == 9
