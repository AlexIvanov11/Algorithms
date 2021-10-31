from typing import Union

from .tree import Tree, Node


def next_node(node: Node) -> Union[Node, None]:
    # Parse through all elements to the right
    # If we have something to the right, we are sure that all elements will be either lower thant parent or greater.
    # Both cases mean that we do not have to even check parent
    # If the node is lower than parent, then all nodes opn the right side will be also lower
    # If the node is greater, then the desired value is still greater than parent and we also do not need to check it
    if node.right is not None:
        return min_value(node.right)

    # Then we walk through the parents if we have nowhere to go to the right
    # Basically we need to find the leftmost element of the closes right branch
    parent = node.parent
    while parent is not None:
        # if we got to this point and node value is lower than parents, then the parent is the target node
        if node != parent.right:
            break
        # If we start from the left side of parent, then we need to go higher until we reach the lowest possible value
        # that is still greater than given node
        node = parent
        parent = parent.parent
    return parent


def min_value(node: Node) -> Node:
    current = node

    # loop down to find the leftmost leaf
    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current


if __name__ == "__main__":
    test_arr = [20, 7, 4, 6, 9, 35, 31, 28, 40, 38, 52]
    tree = Tree(test_arr)
    tree.pretty_print()
    test_node = tree.find_node(20)
    print(f"Next node to {test_node.data} is {next_node(test_node).data}")

