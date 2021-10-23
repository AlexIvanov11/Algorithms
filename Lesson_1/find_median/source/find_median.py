from typing import TypeVar, List, Union

# Types definition for acceptable values
T = TypeVar('T', int, float)


# Chosen this one because of the stable time complexity O(n*log(n))
# Thought about timsort, but we do not need to sort huge arrays
def merge_sort(arr: List[T]) -> List[T]:

    # Basic case, we do not need to calculate anything for arrays with length 0 or 1
    # Actually, in this task we cannot get empty array, but this is a generic method anyway
    # and can be used in other use cases
    if len(arr) == 0 or len(arr) == 1:
        return arr

    # Slice array in two parts
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]

    # Call the same function for both parts
    left = merge_sort(left)
    right = merge_sort(right)
    i = j = k = 0

    # Empty array to fill
    res = [0] * (len(left) + len(right))

    # Merge arrays
    while i < len(left) and j < len (right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    # Continue with the rest of elements
    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1

    return res


# We either return one single element for odd length or two middle elements for even length
def find_median(arr: List[T]) -> Union[T, List[T]]:
    # In case someone wants to try this with empty array
    if len(arr) == 0:
        raise ValueError("Array should contain at least one element")

    # Basic case for one element
    if len(arr) == 1:
        return arr[0]

    arr = merge_sort(arr)
    index = len(arr) // 2
    return arr[index] if len(arr) % 2 else arr[index - 1: index + 1]


def main(arr):
    print(find_median(arr))

if __name__ == '__main__':
    test_arr = [1, 3, 8, 5, 6, 2]
    main(test_arr)