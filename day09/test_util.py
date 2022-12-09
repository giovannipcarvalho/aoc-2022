import pytest
from part1 import array
from part1 import is_adjacent


def test_array_equality():
    assert array([0, 0]) == array([0, 0])
    assert array([1, 0]) == array([1, 0])
    assert array([1, 0]) != array([0, 1])


def test_array_comparison():
    assert array([0, 0]) < array([1, 1])
    assert array([1, 1]) > array([0, 0])
    assert array([1, 1]) <= array([2, 2])
    assert array([1, 2]) <= array([2, 2])
    assert array([2, 2]) >= array([1, 1])
    assert array([2, 2]) >= array([2, 1])


@pytest.mark.parametrize(
    "H, T, expected",
    [
        [array([0, 0]), array([0, 0]), True],
        [array([0, 0]), array([1, 0]), True],
        [array([0, 0]), array([1, 1]), True],
        [array([0, 0]), array([2, 1]), False],
        [array([-2, -2]), array([-1, -1]), True],
        [array([-2, -2]), array([-1, 0]), False],
        [array([0, 2]), array([0, 0]), False],
    ],
)
def test_is_adjacent(H, T, expected):
    assert is_adjacent(H, T) is expected
