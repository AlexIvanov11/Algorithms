class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    # Can accept an array fo nodes for initialization
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            if not isinstance(nodes, list):
                raise TypeError("List can be only initialized with array!")
            if len(nodes) == 0:
                raise ValueError("Empty array specified!")
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # Magic method to print out the values
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Magic method to iterate through values
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_start(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def add_end(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node