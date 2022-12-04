sample_input = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def contains(a, b):
    """Checks if range `a` entirely contains range `b`"""
    la, ha = [int(x) for x in a.split("-")]
    lb, hb = [int(x) for x in b.split("-")]
    if la <= lb and ha >= hb:
        return True
    return False


def overlap(a, b):
    """
    Checks if range `a` overlaps range `b`

    Considers range `a` to have a lower starting value than `b`.
    """
    la, ha = [int(x) for x in a.split("-")]
    lb, hb = [int(x) for x in b.split("-")]
    return lb <= ha and lb >= la


def solve(s: str) -> int:
    """Count the number of range pairs where one entirely contains the other"""
    num_redundant = 0
    for line in s.splitlines():
        first, second = line.split(",")
        if contains(first, second) or contains(second, first):
            num_redundant += 1
    return num_redundant


def solve2(s: str) -> int:
    """Count the number of overlapping pairs"""
    num_redundant = 0
    for line in s.splitlines():
        first, second = line.split(",")
        if overlap(first, second) or overlap(second, first):
            num_redundant += 1
    return num_redundant


def test_sample_part1():
    assert solve(sample_input) == 2


def test_sample_part2():
    assert solve2(sample_input) == 4


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    print("part 1:", solve(s))
    print("part 2:", solve2(s))
