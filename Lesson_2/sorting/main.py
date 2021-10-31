from copy import copy
from numpy import random as np_rand
import time

from quicksort import quicksort
from counting import counting
from radix import radix_lsd
from timsort import timsort

if __name__ == "__main__":
    # Let's compare how quick algorithms are
    test_arr_1 = np_rand.randint(0, 100, 32)
    test_arr_2 = np_rand.randint(0, 1000, 400)
    test_arr_3 = np_rand.randint(0, 10000, 1000)
    test_arr_4 = np_rand.randint(0, 100000, 10000)

    start_time = time.time()

    # counting
    counting(test_arr_1)
    count_1 = time.time()
    counting(test_arr_2)
    count_2 = time.time()
    counting(test_arr_3)
    count_3 = time.time()
    counting(test_arr_4)
    count_4 = time.time()

    print(f'Counting sort: '
          f' 32 elements - {count_1 - start_time},'
          f' 400 elements - {count_2 - count_1}, '
          f' 1000 elements - {count_3 - count_2}'
          f' 10000 elements - {count_4 - count_3}')
    # quicksort
    quicksort(test_arr_1)
    quick_1 = time.time()
    quicksort(test_arr_2)
    quick_2 = time.time()
    quicksort(test_arr_3)
    quick_3 = time.time()
    quicksort(test_arr_4)
    quick_4 = time.time()

    print(f'Quick sort: '
          f' 32 elements - {quick_1 - count_4}, '
          f' 400 elements - {quick_2 - quick_1}, '
          f' 1000 elements - {quick_3 - quick_2}'
          f' 10000 elements - {quick_4 - quick_3}')

    # radix
    radix_lsd(copy(test_arr_1))
    radix_1 = time.time()
    radix_lsd(copy(test_arr_2))
    radix_2 = time.time()
    radix_lsd(copy(test_arr_3))
    radix_3 = time.time()
    radix_lsd(copy(test_arr_4))
    radix_4 = time.time()

    print(f'Radix sort: '
          f' 32 elements - {radix_1 - quick_4}, '
          f' 400 elements - {radix_2 - radix_1}, '
          f' 1000 elements - {radix_3 - radix_2}'
          f' 10000 elements - {radix_4 - radix_3}')

    # timsort
    timsort(test_arr_1)
    timsort_1 = time.time()
    timsort(test_arr_2)
    timsort_2 = time.time()
    timsort(test_arr_3)
    timsort_3 = time.time()
    timsort(test_arr_4)
    timsort_4 = time.time()

    print(f'Timsort: '
          f' 32 elements - {timsort_1 - radix_4}, '
          f' 400 elements - {timsort_2 - timsort_1}, '
          f' 1000 elements - {timsort_3 - timsort_2}'
          f' 10000 elements - {timsort_4 - timsort_3}')