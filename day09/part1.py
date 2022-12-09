from util import array
from util import is_adjacent
from util import make_adjacent
from util import parse_command

sample_input = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


def solve1(s: str) -> int:
    """
    Count the number of unique positions the tail visited at least once while
    following the head.
    """
    H = array([0, 0])  # head position
    T = array([0, 0])  # tail position

    visited_positions = set()
    visited_positions.add(T)
    for command in s.strip().splitlines():
        direction, amount = parse_command(command)
        for _ in range(amount):
            H += direction
            if not is_adjacent(H, T):
                T = make_adjacent(H, T)
                visited_positions.add(T)

    return len(visited_positions)


def test_sample_part1():
    assert solve1(sample_input) == 13


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
