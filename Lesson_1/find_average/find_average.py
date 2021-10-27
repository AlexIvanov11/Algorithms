from typing import Union

# I have decided not to sort the array, because if we have a huge number of items
# to process, we will eventually get to O(n*log(n)) complexity, whereas in this case
# we get only O(n)
# Yes, technically thi is not average value

# Also, tuple is preferable as immutable type, but we can use list as well
# int is added because tuple with one element is converted to single number by python
def find_average(arr: Union[int, list, tuple]) -> int:
    # Check type of accepted argument
    if not isinstance(arr, (int, list, tuple)):
        raise TypeError("Value of wrong type specified!")

    # Check if we got int instead fo array
    if isinstance(arr, int):
        return arr

    # Check for empty array
    if len(arr) == 0:
        raise ValueError("Got empty sequence!")

    # With one element it will be the result
    # With two elements we can assume that the average is exactly between
    # both values so we can return any of them
    if (len(arr)) < 3:
       return arr[0]

    # Basic setup for case when we get only positive or only negative
    if arr[0] <= arr[1]:
        min, max = arr[0], arr[1]
    else:
        min, max = arr[1], arr[0]

    # We could do this with python min and max methods, but this is too easy, right?
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]

    # Average between minimum and maximum
    avg = (min + max) / 2

    # Initial value for result
    res = arr[0]
    for i in range(len(arr)):
        # Let's write this explicitly
        if (abs(arr[i] - avg)) < abs(res - avg):
            res = arr[i]

    return res


if __name__ == "__main__":
    print(find_average((1, 2, 5, 9, 50)))
