import pytest
from Lesson_3 import kmin


def test_wrong_size():
    with pytest.raises(ValueError) as excinfo:
        res = kmin([1, 2], 3)
    assert "greater" in str(excinfo)


@pytest.mark.parametrize("arr, k",
                         (([1, 2, 3], 3),
                          ([1, 2, 3, 4], 4),
                          ([1, 5, 3, 7, 5, 4], 6)
                          ))
def test_same(arr, k):
    res = kmin(arr, k)
    assert res == arr


@pytest.mark.parametrize("arr, k, expected",
                         (
                                 ([22, 33, 44, 55, 12, 11, 31], 3, [22, 12, 11]),
                                 ([1, 2, 3, 4, 5, 6, 7], 5, [1, 2, 3, 4, 5]),
                                 ([90, 80, 70, 50, 60, 40, 30, 20, 10], 5, [50, 40, 30, 20, 10])
                         ))
def test_kmin(arr, k, expected):
    res = kmin(arr,k)
    assert all([x in expected for x in res])
