import pytest


def find_marker(s: str, n: int) -> int:
    """Find the first index at which the previous `n` characters are unique."""
    for i in range(n, len(s)):
        if len(set(s[i - n : i])) == n:
            return i
    return -1


def solve1(s: str):
    return find_marker(s, 4)


def solve2(s: str):
    return find_marker(s, 14)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_sample_part1(input, expected):
    assert solve1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_sample_part2(input, expected):
    assert solve2(input) == expected


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
