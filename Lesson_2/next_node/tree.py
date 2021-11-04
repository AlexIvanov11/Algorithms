from queue import Queue
from copy import deepcopy
from typing import TypeVar, Generic, Optional, List, Union

T = TypeVar("T")


# A binary tree node
class Node(Generic[T]):

    # Constructor to create a new node
    def __init__(self, data: Union[int, str]) -> None:
        self.data = data
        self.left = None
        self.right = None


# A binary tree itself
class Tree(Generic[T]):

    def __init__(self, nodes: List[int] = None) -> None:
        self.root = None
        if nodes:
            for n in nodes:
                self.insert(n)

    def insert(self, data: int) -> None:
        if self.root:
            self.insert_node(self.root, data)
        else:
            self.root = Node(data)

    def insert_node(self, node: Node[T], data: int) -> None:
        if node.data <= data:
            if node.right is not None:
                self.insert_node(node.right, data)
            else:
                node.right = Node(data)
        else:
            if node.left is not None:
                self.insert_node(node.left, data)
            else:
                node.left = Node(data)

    def print_depth(self) -> None:
        self._print_node_recursive(self.root)

    def _print_node_recursive(self, node: Node[T]) -> None:
        if node is not None:
            print(node.data)
            self._print_node_recursive(node.left)
            self._print_node_recursive(node.right)

    def find_node(self, value: int) -> Node[T]:
        if self.root:
            res = self._find_node(self.root, value)
        else:
            raise ValueError("Tree is empty")

        if res is not None:
            return res
        else:
            raise ValueError("No such element")

    @staticmethod
    def _find_node(node: Node[T], value: int) -> Optional['Node[T]']:
        if node is not None:
            if node.data == value:
                return node
            elif node.data > value:
                return Tree._find_node(node.left, value)
            else:
                return Tree._find_node(node.right, value)
        else:
            return None

    # Helper for printing out the data
    def _fill_tree(self, height: int) -> None:
        fill_nodes(self.root, height)

    def pretty_print(self) -> None:
        """
        """
        # get height of tree
        total_layers = get_height(self.root)

        tree = deepcopy(self)
        tree._fill_tree(total_layers)
        # start a queue for BFS
        queue = Queue()
        # add root to queue
        queue.put(tree.root)  # self = root
        # index for 'generation' or 'layer' of tree
        gen = 0
        # BFS main
        while not queue.empty():
            # copy queue
            #
            copy = Queue()
            while not queue.empty():
                copy.put(queue.get())

            first_item_in_layer = True
            extra_spaces_next_node = False

            # modified BFS, layer by layer (gen by gen)
            while not copy.empty():
                node = copy.get()

                # -----------------------------
                # spacing
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid = pow(2, total_layers - gen + 2) - 2
                init_padding = 2
                spaces_front += init_padding

                # -----------------------------
                # handle condition for extra spaces when node lengths don't match or are even:
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0
                # account for longer data
                data_length = len(str(node.data))
                if data_length > 1:
                    if data_length % 2 == 1:  # odd
                        spaces_mid -= (data_length - 1) // 2
                        spaces_front -= (data_length - 1) // 2
                        if data_length != 1:
                            extra_spaces_next_node = True
                    else:  # even
                        spaces_mid -= (data_length - 1)
                        spaces_front -= (data_length - 1)
                if first_item_in_layer:
                    print((" " * spaces_front) + str(node.data), end="")
                    first_item_in_layer = False
                else:
                    print((" " * (spaces_mid - extra_spaces)) + str(node.data), end="")

                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)

            # Finally a new line
            if not queue.empty():
                print("\n", end="")

            # increase layer index
            gen += 1
        print("\n")


# Additional functions to print tree in a pretty way
def get_height(node: Node[T]) -> int:
    if node is None:
        return 0
    else:
        return max(get_height(node.right), get_height(node.left)) + 1


# Fill empty leaves with spaces for pretty output
def fill_nodes(node: Node[T], height: int) -> None:
    if height <= 1:
        return
    if node:
        if not node.left:
            node.left = Node(' ')
        if not node.right:
            node.right = Node(' ')
        fill_nodes(node.left, height - 1)
        fill_nodes(node.right, height - 1)
