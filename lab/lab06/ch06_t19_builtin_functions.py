import tr from typing


def distance_from_zero(s: any) -> Any:
    if type(s) == int or type(s) == float:
        return abs(s)
    return "Nope"
