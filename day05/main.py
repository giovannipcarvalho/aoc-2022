import re
from collections import defaultdict


def parse_crates(s: str) -> dict:
    """
    Parses crates and returns a dict where keys are the crate ID, and the values
    are a list of items contained in the crate (top-most to bottom-most).
    """
    crates = defaultdict(list)

    # ignore the last line with crate ids
    for line in s.splitlines()[:-1]:
        # append an empty char to make the line evenly divisible by 4
        # split into chunks of 4
        values = re.findall("....", line + " ")
        for idx, v in enumerate(values, start=1):
            if v[1] != " ":
                crates[idx].append(v[1])
    return crates


def parse_command(line: str) -> tuple[int, int, int]:
    """
    Parses move commands

    e.g.
        >>> 'move 2 from 5 to 9'
        (2, 5, 9)
    """
    _, amount, _, origin, _, dest = line.split(" ")
    return int(amount), int(origin), int(dest)


def parse_input(s: str) -> tuple[dict, list[tuple[int, int, int]]]:
    """Parses input and returns crates and list of rearrengement instructions"""
    _crates, _commands = s.split("\n\n")
    crates = parse_crates(_crates)
    commands = [parse_command(c) for c in _commands.splitlines()]
    return crates, commands


def solve1(s: str) -> str:
    """Follow moving instructions item-by-item"""
    crates, commands = parse_input(s)
    for amount, origin, dest in commands:
        for _ in range(amount):
            item = crates[origin].pop(0)
            # move crates to the top of the stack
            crates[dest].insert(0, item)

    return "".join([v[0] for k, v in crates.items()])


def solve2(s: str) -> str:
    """Follow moving instructions by moving chunks of items (maintaining order)"""
    crates, commands = parse_input(s)
    for amount, origin, dest in commands:
        for i in range(amount):
            item = crates[origin].pop(0)
            # move crates in chunks i.e. insert in the original order
            crates[dest].insert(i, item)

    return "".join([v[0] for k, v in crates.items()])


def test_part1():
    s = open("input.txt").read().strip()
    assert solve1(s) == "FHSWJPSWM"


def test_part2():
    s = open("input.txt").read().strip()
    assert solve2(s) == "PWHWFGPZS"


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
