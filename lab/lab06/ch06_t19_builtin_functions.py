from typing import Any


def distance_from_zero(s: Any) -> Any:
    if type(s) == int or type(s) == float:
        return abs(s)
    return "Nope"
