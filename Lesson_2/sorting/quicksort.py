from typing import List, Union
from random import randrange
from numpy import random as np_rand
from numpy.typing import NDArray


def quicksort(arr: Union[NDArray[int], List[int]]) -> Union[List[int], NDArray[int]]:
    # Basic case
    if len(arr) < 2:
        return arr

    # We can take any element as a target for comparison so why not make it random?
    index = randrange(0, len(arr))

    # Instead of constantly retrieving an item from array let's just remember it
    comp_elem = arr[index]

    # Arrays of lesser and greater numbers
    # Could be written with python oneliners, but with them we will iterate twice over the array
    # lesser = [i for i in array if i < comp_elem]
    # greater = [i for i in array if i > comp_elem]
    # Explicit form iterates only once

    lesser = []
    greater = []

    # Let's not forget about duplicates
    equal = []
    for num in arr:
        if num < comp_elem:
            lesser.append(num)
        elif num > comp_elem:
            greater.append(num)
        else:
            equal.append(num)

    # ... repeat :)
    return quicksort(lesser) + equal + quicksort(greater)


if __name__ == "__main__":
    test_arr = np_rand.randint(1, 100, 100)
    print(test_arr)
    res = quicksort(test_arr)
    print(res)
