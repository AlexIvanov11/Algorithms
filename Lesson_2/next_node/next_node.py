from typing import Union

from .tree import Tree, Node


def next_node(root: Node, node: Node) -> Union[Node, None]:
    # Check if we have something to the right side of the node
    if node.right is not None:
        # This method iterates over the right subtree to find the least value
        return min_value(node.right)

    # Create empty node to store result
    nxt = Node(None)

    # Then we check root and all subtrees from that
    # 1. Check if our node is greater than root. If so, then we need to move to the right.
    #   If root is greater than out node, mode to the left and remember visited node.
    #   This node is now the last parent
    # 2. If we moved to the right, we keep searching until we find the root that is greater than our node
    #   after that we perform identical actions as in step 3
    # 3. If we moved to the left, wwe remember the last node and repeat the same actions. We compare new root
    #   to our node and move to the right or left side. When we find the node itself or reach the end of the tree,
    #   the last remembered node is the target. This will be either the parent of node or the lowest possible value
    while root:
        if root.data < node.data:
            root = root.right
        elif root.data > node.data:
            nxt = root
            root = root.left
        else:
            break
    return nxt


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
    test_node = tree.find_node(9)
    print(f"Next node to {test_node.data} is {next_node(tree.root, test_node).data}")

