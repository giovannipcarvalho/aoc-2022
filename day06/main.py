import pytest


def solve1(s: str) -> int:
    """Find the first index at which the previous 4 characters are unique."""
    for i in range(4, len(s)):
        if len(set(s[i - 4 : i])) == 4:
            return i
    return -1


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
def test_sample(input, expected):
    assert solve1(input) == expected


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
