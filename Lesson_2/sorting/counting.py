from typing import List, Union
from numpy import random as np_rand
from numpy.typing import NDArray


def counting(arr: Union[List[int], NDArray[int]]) -> Union[List[int], NDArray[int]]:
    # Remember maximum and minimum
    max_value = max(arr)
    min_value = min(arr)

    # remember the length of array, because I just want to do so
    length = len(arr)
    # We can create an array for the range between maximum and minimum value
    count = [0] * (max_value - min_value + 1)

    for i in range(length):
        # Explicit calculation of index because we can probably even get negative numbers
        index = arr[i] - min_value
        count[index] += 1

    # Generation of result is also made explicit for better readability
    res = []
    for i in range(len(count)):
        if (count[i]) != 0:
            res += [i+min_value] * count[i]

    return res


if __name__ == "__main__":
    test_arr = np_rand.randint(-10, 10, 30)
    print(test_arr)
    res = counting(test_arr)
    print(res)
