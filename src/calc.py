import math


def add(a: float, b: float) -> float:
    return a + b


def circle_area(r: float) -> float:
    if r < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * r * r
