import pytest
from Lesson_3 import Heap, heapify


@pytest.mark.parametrize("arr, expected",
                         [([2, 3, 4, 6, 7, 12, 34, 11, 35, 66, 89, 5],
                          [2, 3, 4, 6, 7, 5, 34, 11, 35, 66, 89, 12]),
                         ([58, 32, 33, 67, 12, 43, 98, 2, 3, 12, 45],
                          [2, 3, 33, 12, 12, 43, 98, 67, 32, 58, 45])])
def test_heap_heapify(arr, expected):
    heap = Heap(arr)
    assert heap.items == expected

@pytest.mark.parametrize("arr, expected",
                         [([2, 3, 4, 6, 7, 12, 34, 11, 35, 66, 89, 5],
                          [2, 3, 4, 6, 7, 5, 34, 11, 35, 66, 89, 12]),
                         ([58, 32, 33, 67, 12, 43, 98, 2, 3, 12, 45],
                          [2, 3, 33, 12, 12, 43, 98, 67, 32, 58, 45])])
def test_heapify(arr, expected):
    res = heapify(arr)
    assert res == expected
