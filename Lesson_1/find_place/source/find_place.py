from typing import Union, List
from math import ceil


# Complexity is O(n)
# Could be shorter when written with python magic one-liners, but this seems to be more understandable
def map_zeros(sequence: Union[list, tuple]) -> List[int]:
    res = []
    current = 0
    for i in range(len(sequence)):
        if sequence[i] != 0 and sequence[i] != 1:
            raise ValueError(f'Sequence should contain only 0 and 1! Got {sequence[i]} at position {i}')
        if sequence[i] == 0:
            current += 1
        elif current != 0:
            res.append(current)
            current = 0
        else:
            current = 0
    if current != 0:
        res.append(current)

    return res


def find_place(sequence: Union[list, tuple]) -> int:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Wrong type of sequence")

    if len(sequence) < 2:
        raise ValueError("Too short sequence")

    zeros = map_zeros(sequence)
    max_space = 0
    # Initial setup, we check if we can take place at the start or end
    if sequence[0] == 0:
        max_space = zeros[0]
    if sequence[-1] == 0:
        max_space = max(max_space, zeros[-1])
    for val in zeros:
        # We round number to the ceil because for odd numbers we get smaller value than it will actually be
        # I.e? fjr 5 we get 2.5, but this means that we will have 1 in at least 3 positions to the side
        max_space = max(max_space, ceil(val / 2))
    return max_space


if __name__ == "__main__":
    print(find_place([0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0]))
