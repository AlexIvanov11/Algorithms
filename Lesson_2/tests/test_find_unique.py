import pytest
from Lesson_2 import find_unique

@pytest.mark.parametrize("unique", [22,25,444,123,0,33333,1256])
def test_find_unique(unique):
    test_list = [i for i in range(1000000)] * 2
    test_list.append(unique)
    res = find_unique(test_list)
    assert res == unique