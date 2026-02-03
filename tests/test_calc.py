import math
import pytest

from src.calc import add, circle_area


def test_add():
    assert add(1, 2) == 3


def test_circle_area():
    assert circle_area(2) == math.pi * 4


def test_circle_area_negative():
    with pytest.raises(ValueError):
        circle_area(-1)
