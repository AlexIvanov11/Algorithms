import pytest
from Lesson_1.find_median.source.find_median import find_median


# Test exception for an empty array
def test_empty():
    test_arr = []
    with pytest.raises(ValueError) as excinfo:
        find_median(test_arr)

    assert "at least one element" in str(excinfo)

# Test with one element
def test_one():
    test_arr = [5]
    res = find_median(test_arr)
    assert res == 5

# Test with odd array to return one element
def test_multiple_odd():
    test_arr = [5, 6, 12, 90, 23, 56, 22, 140, 4]
    res = find_median(test_arr)
    test_arr.sort()

    # Check that we work in same way as python does
    assert res == test_arr[len(test_arr) // 2]


# Test with odd array to return one element
def test_multiple_even():
    test_arr = [5, 6, 12, 90, 23, 56, 22, 140, 4, 77]
    res = find_median(test_arr)
    test_arr.sort()

    # Check that we work in same way as python does
    assert res == test_arr[len(test_arr) // 2 - 1: len(test_arr) // 2 + 1]


# Test with different types
def test_float():
    test_arr = [5, 6.5, 12, 90.35, 23, 56.55, 22, 140, 4]
    res = find_median(test_arr)
    test_arr.sort()

    # Check that we work in same way as python does
    assert res == test_arr[len(test_arr) // 2]