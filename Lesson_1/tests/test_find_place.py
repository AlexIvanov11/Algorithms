import pytest
from Lesson_1 import find_place


def test_empty():
    with pytest.raises(ValueError) as excinfo:
        find_place([])
    assert "short" in str(excinfo)


def test_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        find_place("Accidental string")
    assert "type" in str(excinfo)


def test_non_binary():
    with pytest.raises(ValueError) as excinfo:
        find_place([1, 0, 0, 4])
    assert "4" in str(excinfo)


def test_start():
    res = find_place([0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1])
    assert res == 3


def test_end():
    res = find_place([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0])
    assert res == 3


def test_somewhere_even():
    res = find_place([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1])
    assert res == 2


def test_somewhere_odd():
    res = find_place([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
    assert res == 3
