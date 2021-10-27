import pytest
from Lesson_2 import swap_halves, LinkedList


def test_empty_list():
    with pytest.raises(ValueError) as excinfo:
        LinkedList([])
    assert "Empty" in str(excinfo)


def test_wrong_list_type():
    with pytest.raises(TypeError) as excinfo:
        LinkedList("string")
    assert "array" in str(excinfo)


def test_single():
    with pytest.raises(ValueError) as excinfo:
        test_list = LinkedList([1])
        swap_halves(test_list)
    assert "short" in str(excinfo)


def test_two_elements():
    test_arr = [1, 2]
    test_list = LinkedList(test_arr.copy())
    res = swap_halves(test_list)
    test_res = test_arr[1:] + test_arr[:1]
    assert all([node.data == test_res[index] for index, node in enumerate(res) if node.data != None])


def test_long_list():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_list = LinkedList(test_arr.copy())
    res = swap_halves(test_list)
    test_res = test_arr[5:] + test_arr[:5]
    assert all([node.data == test_res[index] for index, node in enumerate(res) if node != None])
