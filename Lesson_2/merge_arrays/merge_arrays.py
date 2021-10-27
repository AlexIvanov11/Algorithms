from typing import List, Callable

# This is an object to access validation lambdas (another python toy)
# I could do this to arr2_index_mod and arr2_index_check but decided not to move them outside of the method
# And to do that in a cleaner way (you'll see later)
ordering = {
    "asc": (lambda x, y: x <= y),
    "desc": (lambda x, y: x >= y),
}


# Helper function to define order of array
def define_order(arr: list) -> str:
    return "asc" if (len(arr) == 1 or arr[1] - arr[len(arr) - 1] <= 0) else "desc"


# Function to merge two sorted arrays in specified order
def merge_in_order(arr1: List[int],
                   arr2: List[int],
                   order_function: Callable[[int, int], bool],
                   same_order: bool) -> List[int]:
    res = []

    # If we have arrays sorted in different order, we start from the end with second array
    arr1_index, arr2_index = 0, 0 if same_order else len(arr2) - 1

    # So we have another check clause if we are moving backwards
    def arr2_index_check(index):
        return index < len(arr2) if same_order else index >= 0

    # And we also modify the index in different way
    def arr2_index_mod(index):
        return index + 1 if same_order else index - 1

    # And in this loop we move through both arrays in some direction
    # For the first one we always move from start to the end (could be also changed)
    # Direction for second array depends on the order of both arrays
    while arr1_index < len(arr1) and arr2_index_check(arr2_index):
        if order_function(arr1[arr1_index], arr2[arr2_index]):
            res.append(arr1[arr1_index])
            arr1_index += 1
        else:
            res.append(arr2[arr2_index])
            arr2_index = arr2_index_mod(arr2_index)

    # And we append remaining elements like we do in merge sort
    while arr1_index < len(arr1):
        res.append(arr1[arr1_index])
        arr1_index += 1

    while arr2_index_check(arr2_index):
        res.append(arr2[arr2_index])
        arr2_index = arr2_index_mod(arr2_index)

    return res


def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    # Check that we got correct types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Invalid arguments specified, should be two arrays")
    # We could also check that both arrays are sorted in some order,
    # but I do not think that we need this at the moment

    # Base case, we do not work with empty arrays
    # Array with len == 1 is sorted, of course )
    if len(arr1) == 0:
        raise ValueError("First array is empty!")
    if len(arr2) == 0:
        raise ValueError("Second array is empty!")

    # Define order of both arrays
    arr1_order = define_order(arr1)
    arr2_order = define_order(arr2)

    # We assume that the order of first array is more important
    res = merge_in_order(arr1, arr2, ordering[arr1_order], arr1_order == arr2_order)
    return res


if __name__ == "__main__":
    print(merge_arrays([9], [2]))
