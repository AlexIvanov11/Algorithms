from typing import List, Union
from numpy import random as np_rand
from numpy.typing import NDArray


def count_lsd(arr: Union[List[int], NDArray[int]], divider: int) -> None:
    n = len(arr)
    # Output array
    output = [0] * n

    # Helping array for sorting. This will help with calculating of new position for number
    count = [0] * 10

    # Count occurrences of certain digit in desired position for all numbers
    for i in range(n):
        index = arr[i] // divider
        count[index % 10] += 1

    # Calculate the offset to start pushing numbers with certain digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output
    for i in range(n-1, -1, -1):
        index = (arr[i] // divider) % 10
        out_index = count[index] - 1
        output[out_index] = arr[i]
        count[index] -= 1

    # Mutate specified array
    for i in range(n):
        arr[i] = output[i]


# I decided to make and LSD instead of MSD
def radix_lsd(arr: Union[List[int], NDArray[int]]) -> Union[List[int], NDArray[int]]:
    if len(arr) < 2:
        return arr

    # Find the maximum number to know number of digits
    max_value = max(arr)

    divider = 1
    while max_value // divider > 0:
        count_lsd(arr, divider)
        divider *= 10
    return arr


if __name__ == "__main__":
    # We will work only with positive numbers at the moment
    test_arr = np_rand.randint(0, 1000, 20)
    print(test_arr)
    res = radix_lsd(test_arr)
    print(res)
