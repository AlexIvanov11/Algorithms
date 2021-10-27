# Python one-liner. I decided to cast result to int so we keep same type without any surprises
def simple_inverse(number: int) -> int:
    # We accept only integers
    if not isinstance(number, int):
        raise TypeError("Algorithm accepts only integers")

    # We do not accept negative numbers for this case
    if number < 0:
        raise ValueError("Number should be positive")

    if number < 10:
        return number

    return int("".join(list(str(number))[::-1]))


# And here I decided to take a math approach to get all the numbers
def math_inverse(number: int) -> int:
    # We accept only integers
    if not isinstance(number, int):
        raise TypeError("Algorithm accepts only integers")

    # We do not accept negative numbers for this case
    if number < 0:
        raise ValueError("Number should be positive")

    # For values lesser than 10 we do not need to inverse them
    if number < 10:
        return number

    res = 0
    while number // 10 != 0:
        res = res * 10 + number % 10
        number //= 10
    res = res * 10 + number
    return res

if __name__ == "__main__":
    print(simple_inverse(123))
    print(math_inverse(123))