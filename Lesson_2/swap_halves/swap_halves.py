from .classes import LinkedList


def swap_halves(lst):
    # If we have on;y one element, we do not need to swap anything
    if lst.head.next is None:
        raise ValueError("Too short list (must have more than one element)")

    # Set pointers to first and second node
    middle_node = lst.head
    last_node = lst.head.next

    # Every move middle_node onto the next one every two moves of last_node
    # We assume that we will always have even number ove elements, to make things easier
    even = False
    while last_node.next is not None:
        last_node = last_node.next
        if even:
            middle_node = middle_node.next
            even = not even
        else:
            even = not even

    # last node now should point at the head
    last_node.next = lst.head

    # when the new head is the next element after middle
    lst.head = middle_node.next

    # And do not forget to empty last pointer or we will get infinite loop
    middle_node.next = None
    return lst


if __name__ == "__main__":
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
    print(swap_halves(lst))