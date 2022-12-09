from collections import defaultdict

from util import array
from util import is_adjacent
from util import make_adjacent
from util import parse_command


sample_input = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def solve2(s: str) -> int:
    """
    Count the number of unique positions the tail visited at least once while
    following the head, but now the rope has 10 knots
    """
    # knots 1-9 are "tail" knots
    knots = [array([0, 0]) for _ in range(10)]  # H, 1, 2, 3, ... 9

    visited_positions = defaultdict(set)
    for knot, position in enumerate(knots):
        visited_positions[knot].add(position)

    for command in s.strip().splitlines():
        direction, amount = parse_command(command)

        for _ in range(amount):
            # apply movement to HEAD knot
            knots[0] += direction

            # check and adjust each H-1, 1-2, 2-3 knot pair
            for k in range(len(knots) - 1):
                k0 = knots[k]
                k1 = knots[k + 1]

                if not is_adjacent(k0, k1):
                    new_k1 = make_adjacent(k0, k1)
                    knots[k + 1] = new_k1
                    visited_positions[k + 1].add(new_k1)

    return len(visited_positions[9])


def test_sample_part2():
    assert solve2(sample_input) == 36


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 2:", solve2(s))
