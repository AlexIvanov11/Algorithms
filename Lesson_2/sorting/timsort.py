from typing import List, Union
from numpy import random as np_rand
from numpy.typing import NDArray
from copy import copy

# Experiments say that with MIN_RUN less than 32 this sorting does not make sense
MIN_RUN = 32


# Gets maximum possible power of 2 that is less than length of array
def get_min_run(n: int) -> int:
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r


# Just insertion sort for array chunks
def insertion_sort(arr: Union[List[int], NDArray[int]],
                   left: int,
                   right: int) -> None:
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Just merge of the arrays
def merge(arr: Union[List[int], NDArray[int]], left: int, mid: int, right: int) -> None:
    # after comparing, we merge those two array
    # in larger sub array
    len_left, len_right = mid - left + 1, right - mid
    left_part, right_part = [], []
    # Instead of slicing parts, here I manually create two copies because somehow slicing does not prevent
    # original array from mutating
    for i in range(len_left):
        left_part.append(arr[left + i])
    for i in range(len_right):
        right_part.append(arr[mid + 1 + i])

    # Moved explicit pointer initialization here because two lops before are mutating i
    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < len_left:
        arr[k] = left_part[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len_right:
        arr[k] = right_part[j]
        k += 1
        j += 1

def timsort(arr):
    # I do not want to mutate arr directly
    temp_arr = copy(arr)
    n = len(temp_arr)
    min_run = get_min_run(n)
    # Consecutively iterate over array by min_run
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(temp_arr, start, end)

    # size of
    size = min_run
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(temp_arr, left, mid, right)

        size = 2 * size
    return temp_arr

if __name__ == "__main__":
    # We will work only with positive numbers at the moment
    test_arr = np_rand.randint(0, 1000, 200)
    print(test_arr)
    res = timsort(test_arr)
    print(res)
