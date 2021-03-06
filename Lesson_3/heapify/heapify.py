from typing import List


# So as we are writing heapify method, why not add it to the class?
class Heap:
    def __init__(self, items: List[int] = None) -> None:
        self.size = 0
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
        while self.items[current] < self.items[parent_index] and parent_index >= 0:
            self._swap(current, parent_index)
            current = parent_index
            parent_index = self._parent(current)

    @staticmethod
    def swap(arr: List[int], pos1:int, pos2: int) -> None:
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

    @classmethod
    def heapify(cls, arr: List[int]) -> None:
        for i in range(len(arr)):
            current = i
            # save it into variable for better readability
            parent_index = cls._parent(current)
            # if current item is smaller than parent, change places
            while arr[current] < arr[parent_index] and parent_index >= 0:
                arr[current], arr[parent_index] = arr[parent_index], arr[current]
                current = parent_index
                parent_index = cls._parent(current)


if __name__ == "__main__":
    test_arr = [58, 32, 33, 67, 12, 43, 98, 2, 3, 12, 45]
    heap = Heap(test_arr)
    print(heap.items)
    Heap.heapify(test_arr)
    print(test_arr)
