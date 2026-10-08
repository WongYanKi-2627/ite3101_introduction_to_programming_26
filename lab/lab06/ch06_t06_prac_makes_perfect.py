def cube(number: int) -> int:
    return number ** number


def by_three(number: int) :
    if number % 3 == 0:
        return cube(number)

