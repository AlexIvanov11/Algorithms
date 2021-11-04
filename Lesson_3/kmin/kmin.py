from typing import List


# Copied from heapify lesson. It is already useful) But here I will use max heap
class Heap:
    def __init__(self, max_size: int = 0, items: List[int] = None) -> None:
        self.size = 0
        self.max_size = max_size
        self.items = []
        if items:
            for item in items:
                self._insert(item)

    # get position of parent node
    @staticmethod
    def _parent(index: int) -> int:
        return (index - 1) // 2

    # swap two elements
    def _swap(self, pos1: int, pos2: int) -> None:
        self.items[pos1], self.items[pos2] = self.items[pos2], self.items[pos1]

    # Function to print the contents of the heap
    def print_heap(self) -> None:
        for i in range(1, (self.size // 2)):
            print(" PARENT : " + str(self.items[i]) + " LEFT CHILD : " +
                  str(self.items[2 * i]) + " RIGHT CHILD : " +
                  str(self.items[2 * i + 1]))

    def _insert(self, item: int) -> None:
        self.items.append(item)
        self.size += 1

        # Pointer at the last element that ws pushed into heap
        current = self.size - 1

        # save it into variable for better readability
        parent_index = self._parent(current)

        # if current item is smaller than parent, change places
        while self.items[current] > self.items[parent_index] and parent_index >= 0:
            self._swap(current, parent_index)
            current = parent_index
            parent_index = self._parent(current)

    def rebuild(self) -> None:
        for i in range(self.size):
            current = i
            # save it into variable for better readability
            parent_index = self._parent(current)
            # if current item is smaller than parent, change places
            while self.items[i] > self.items[parent_index] and parent_index >= 0:
                self._swap(current, parent_index)
                current = parent_index
                parent_index = self._parent(current)

    def insert_no_extension(self, item: int) -> None:
        # Remove the first element as the largest one
        self.items.pop(0)
        self.items.append(item)
        self.rebuild()

    @staticmethod
    def swap(arr: List[int], pos1: int, pos2: int) -> None:
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

    @property
    def root(self) -> int:
        return self.items[0]


def kmin(arr: List[int], k: int) -> List[int]:
    # Check that we can even find this
    if k > len(arr):
        raise ValueError("K is greater than length of specified array")

    # If we have exact the same number of elements, we do not need to find stats
    if k == len(arr):
        return arr

    # Get first k elements. Some python magic)
    res = Heap(k, [x for x in arr[:k]])
    # And now just iterate over all items and compare them to the root of our heap
    for item in arr[k:]:
        if item < res.root:
            res.insert_no_extension(item)

    return res.items


if __name__ == "__main__":
    # We have K items to find in an array with length of N
    # So the resulting complexity will be O(N + log(K))
    test_arr = [58, 32, 33, 67, 12, 43, 98, 2, 3, 12, 45]
    res = kmin(test_arr, 3)
    print(res)