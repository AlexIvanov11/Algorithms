import pytest
from Lesson_2 import merge_arrays


def test_empty():
    with pytest.raises(ValueError) as excinfo:
        merge_arrays([], [])
    assert "empty" in str(excinfo)


def test_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        merge_arrays("one accidental string", [])
    assert "Invalid" in str(excinfo)


def test_single_element():
    res = merge_arrays([1], [2])
    assert res == [1, 2]


def test_same_elements():
    res = merge_arrays([1, 1, 1, 1], [2, 2, 2, 2, 2])
    assert res == [1, 1, 1, 1, 2, 2, 2, 2, 2]


def test_both_ascending():
    res = merge_arrays([1, 2, 6, 8], [1, 4, 7, 10, 11])
    assert res == [1, 1, 2, 4, 6, 7, 8, 10, 11]


def test_both_descending():
    res = merge_arrays([8, 6, 2, 1], [11, 10, 7, 4, 1])
    assert res == [11, 10, 8, 7, 6, 4, 2, 1, 1]


def test_both_different_asc():
    res = merge_arrays([1, 2, 6, 8],  [11, 10, 7, 4, 1])
    assert res == [1, 1, 2, 4, 6, 7, 8, 10, 11]


def test_both_different_desc():
    res = merge_arrays([8, 6, 2, 1], [1, 4, 7, 10, 11])
    assert res == [11, 10, 8, 7, 6, 4, 2, 1, 1]
