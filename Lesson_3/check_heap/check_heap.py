from typing import List, Callable


CHECKS = {
    "min": lambda x, y: x <= y,
    "max": lambda x, y: x >= y
}


def is_heap(arr: List[int], index: int, method: Callable) -> bool:
    # we can check the index inside of the method because it is easier nad has less code
    # than checking it before calling the method
    if index >= len(arr):
        return True

    return method(arr[(index - 1) // 2], arr[index]) \
           and is_heap(arr, (index * 2) + 1, method) \
           and is_heap(arr, (index * 2) + 2, method)


# In the end this is really like the example given :)
def check_heap(arr: List[int], method: str) -> bool:
    if len(arr) == 0:
        raise ValueError("Empty array specified")

    # Array with len
    if len(arr) == 1:
        return True

    # We can safely start now from the second (index 1) element
    # I decided to add logic to check min and max heaps
    # So here we get necessary lambda from dictionary
    res = is_heap(arr, 1, CHECKS[method])
    return res



if __name__ == "__main__":
    # 2n + 1, 2n + 2
    test_arr = [3, 5, 7, 10, 11, 12, 14, 13, 15, 25, 27, 33, 56, 22, 23, 30, 31]
    print(check_heap(test_arr, "max"))
