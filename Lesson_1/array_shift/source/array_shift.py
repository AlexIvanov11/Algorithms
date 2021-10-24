def array_shift(arr: list, positions: int) -> list:
    if not isinstance(arr, list):
        raise TypeError("Non-list value specified")

    if not isinstance(positions, int):
        raise TypeError("Only integer is accepted for number of positions to shift")

    if len(arr) == 0:
        raise ValueError("Empty array specified")

    if len(arr) == 1:
        return arr

    shift = positions % len(arr)
    if shift == 0:
        return arr

    return arr[shift:] + arr[:shift]


if __name__ == "__main__":
    print(array_shift([1, 2, 3, 4, 5], 3))
