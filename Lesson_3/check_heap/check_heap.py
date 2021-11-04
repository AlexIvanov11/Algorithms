from typing import List


def check_min_heap(arr, index):
    # we can check the index inside of the method because it is easier nad has less code
    # than checking it before caling the method
    if index >= len(arr):
        return True

    return arr[index // 2] <= arr[index] \
           and check_min_heap(arr, (index * 2) + 1) \
           and check_min_heap(arr, (index * 2) + 2)


def check_max_heap(arr, index):
    if index >= len(arr):
        return True

    return arr[(index - 1) // 2] >= arr[index] \
           and check_max_heap(arr, (index * 2) + 1) \
           and check_max_heap(arr, (index * 2) + 2)


CHECKS = {
    "min": check_min_heap,
    "max": check_max_heap
}


# In the end this is really like the example given :)
def check_heap(arr: List[int], method) -> bool:
    if len(arr) == 0:
        raise ValueError("Empty array specified")

    # Array with len
    if len(arr) == 1:
        return True

    # We can safely start now from the second (index 1) element
    res = CHECKS[method](arr, 1)
    return res



if __name__ == "__main__":
    # 2n + 1, 2n + 2
    test_arr = [3, 5, 7, 10, 11, 12, 14, 13, 15, 25, 27, 33, 56, 22, 23, 30, 31]
    print(check_heap(test_arr, "max"))
