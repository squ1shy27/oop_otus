
import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
from src.rectangle import Rectangle
@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (2, 3),
        (1.2, 6.5)
    ])
def test_rectangle_are_positive( first_side, second_side):
    print(first_side, second_side)
    a = first_side * second_side
    react = Rectangle(first_side, second_side)
    print(a)
    print(react.get_area)
    assert react.get_area == a


import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (0, 3),
        (-4, 6.5)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(first_side, second_side):
    with pytest.raises(ValueError):
        print(f"side one: {first_side}")
        print(f"side two: {second_side}")
        Rectangle(first_side, second_side)
