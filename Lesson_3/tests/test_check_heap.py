import pytest
from Lesson_3 import check_heap


def test_empty():
    test_arr = []
    with pytest.raises(ValueError) as excinfo:
        res = check_heap(test_arr, "min")
    assert "Empty" in str(excinfo)


@pytest.mark.parametrize("method", ("min", "max"))
def test_one_element(method):
    test_arr = [1]
    assert check_heap(test_arr, method)


@pytest.mark.parametrize("method", ("min", "max"))
def test_not_heap(method):
    test_arr = [20, 7, 4, 6, 6, 9, 35, 31, 40, 28, 38, 52]
    assert not check_heap(test_arr, method)


def test_min_heap():
    test_arr = [3, 5, 7, 10, 11, 12, 14, 13, 15, 25, 27, 33, 56, 22, 23, 30, 31]
    assert check_heap(test_arr, "min") and not check_heap(test_arr, "max")


def test_max_heap():
    test_arr = [31, 20, 22, 19, 18, 21, 18, 17, 8, 15, 12, 12, 11, 6, 8, 3, 5, 1]
    assert check_heap(test_arr, "max") and not check_heap(test_arr, "min")
