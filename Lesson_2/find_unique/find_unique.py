from typing import List
import time

def find_unique(arr: List[int]) -> int:
    """
    I will use python dictionary to register all found numbers because it is actually a hashmap
    and has constant access time
    In this method I will also check the existence of necessary key in dictionary
    """

    # Create a dictionary (associative array) for already found numbers
    numbers = dict()  # numbers = {} is basically the same
    for i in range(len(arr)):
        if arr[i] in numbers:
            del numbers[arr[i]]
        else:
            numbers[arr[i]] = 1  # can be any value, it does not matter

    return list(numbers.keys())[0]  # We have only one key here for sure, this is a conversion of the key to int


def find_unique_arrays(arr: List[int]) -> int:
    # And here I use additional array - not really good with time complexity, I just want to compare different
    # approaches
    res = 0
    helper = []
    for i in range(len(arr)):
        if not arr[i] in helper:
            helper.append(arr[i])
            res += arr[i]
        else:
            res -= arr[i]
    return res


if __name__ == "__main__":
    """
    This is a demo that shows previously mentioned idea
    Accessing a key in dictionary is waaaaaaaaaaay faster than checking of existence of element in array
    1000 elements: 0.0s vs 0.02199s
    10000 elements: 0.009998s vs 1.598525s
    100000 elements: 0.03499s vs 172.1367s !!!
    1000000 elements (I regret even trying to check this): 0.373s vs more than hour, didn't wait for so long
    """
    test_list = [i for i in range(1000000)] * 2
    test_list.append(22222)

    start_time = time.time()

    res_dict = find_unique(test_list)
    time_dict = time.time()
    print (f'Dictionary: {time_dict - start_time}')

    res_dict = find_unique_arrays(test_list)
    time_arr = time.time()
    print(f'Arrays: {time_arr - time_dict}')