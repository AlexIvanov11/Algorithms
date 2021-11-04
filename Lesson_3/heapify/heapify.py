from typing import List


# So as we are writing heapify method, why not add it to the class?
class Heap:
    def __init__(self, items: List[int] = None):
        self.size = 0
        self.items = []
        if items:
            for item in items:
                self._insert(item)

    # get position of parent node
    @staticmethod
    def _parent(index):
        return (index - 1) // 2

    # swap two elements
    def _swap(self, pos1, pos2):
        self.items[pos1], self.items[pos2] = self.items[pos2], self.items[pos1]

    # Function to print the contents of the heap
    def print_heap(self):
        for i in range(1, (self.size // 2)):
            print(" PARENT : " + str(self.items[i]) + " LEFT CHILD : " +
                  str(self.items[2 * i]) + " RIGHT CHILD : " +
                  str(self.items[2 * i + 1]))

    def _insert(self, item):
        self.items.append(item)
        self.size += 1

        # Pointer at the last element that ws pushed into heap
        current = self.size - 1

        # save it into variable for better readability
        parent_index = self._parent(current)

        # if current item is smaller than parent, change places
        while self.items[current] < self.items[parent_index] and parent_index >= 0:
            self._swap(current, parent_index)
            current = parent_index
            parent_index = self._parent(current)

    @staticmethod
    def swap(arr, pos1, pos2):
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

    @classmethod
    def insert(cls, arr, item):
        arr.append(item)
        # Pointer at the last element that ws pushed into heap
        current = len(arr) - 1
        # save it into variable for better readability
        parent_index = (current - 1) // 2
        while arr[current] < arr[parent_index] and parent_index >= 0:
            arr[current], arr[parent_index] = arr[parent_index], arr[current]
            current = parent_index
            parent_index = (current - 1) // 2

    @classmethod
    def heapify(cls, arr: List[int]):
        # basically this is almost the same as init of Heap
        res = [arr[0]]
        for item in arr[1:]:
            cls.insert(res, item)
        return res


def heapify(arr: List[int]) -> List[int]:
    res = Heap.heapify(arr)
    return res


if __name__ == "__main__":
    test_arr = [58, 32, 33, 67, 12, 43, 98, 2, 3, 12, 45]
    heap = Heap(test_arr)
    print(heap.items)
    print(heapify(test_arr))
