import pytest
from Lesson_2 import next_node, Tree, Node


@pytest.mark.parametrize("node, expected", [(4,6),(6,7),(9,20),(20,28),(35,38),(31,35)])
def test_find_next(node, expected):
    test_arr = [20, 7, 4, 6, 9, 35, 31, 28, 40, 38, 52]
    tree = Tree(test_arr)
    test_node = tree.find_node(node)
    res = next_node(test_node)
    assert res.data == expected


def test_no_next():
    test_arr = [20, 7, 4, 6, 9, 35, 31, 28, 40, 38, 52]
    tree = Tree(test_arr)
    test_node = tree.find_node(52)
    res = next_node(test_node)
    assert res is None


def test_find_node():
    test_arr = [20, 7, 4, 6, 9, 35, 31, 28, 40, 38, 52]
    tree = Tree(test_arr)
    test_value = 52
    test_node = tree.find_node(test_value)
    assert all([isinstance(test_node, Node), test_node.data == test_value])


def test_no_such_element():
    test_arr = [20, 7, 4, 6, 9, 35, 31, 28, 40, 38, 52]
    tree = Tree(test_arr)
    test_value = 55
    with pytest.raises(ValueError) as excinfo:
        tree.find_node(test_value)
    assert "No such element" in str(excinfo)


def test_find_in_empty():
    test_arr = []
    tree = Tree(test_arr)
    test_value = 55
    with pytest.raises(ValueError) as excinfo:
        tree.find_node(test_value)
    assert "empty" in str(excinfo)