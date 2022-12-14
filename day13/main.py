from bisect import bisect
from functools import cmp_to_key

sample_input = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def compare(left, right) -> int:
    match left, right:
        case int(), int():
            if left == right:
                return 0
            else:
                return left - right
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case list(), list():
            for lt, rt in zip(left, right):
                if compare(lt, rt) != 0:
                    return compare(lt, rt)
            else:
                # did not find a deciding factor
                # `left` could either be same length, shorter or longer than `right`
                return compare(len(left), len(right))

    return 0


def solve1(s: str) -> int:
    """
    Sum the indices (1-based) of the pairs that are in the right order.
    """
    pairs = []
    for pair in s.strip().split("\n\n"):
        pairs.append([eval(p) for p in pair.split("\n")])

    return sum(idx for idx, pair in enumerate(pairs, start=1) if compare(*pair) < 0)


def solve2(s: str) -> int:
    """
    Sort packets.
    """
    packets = [eval(p) for p in s.strip().split("\n") if p != ""]
    cmp = cmp_to_key(compare)
    packets.sort(key=cmp)

    # 1-based indices
    idx1 = bisect(packets, cmp([[2]]), key=cmp) + 1
    # 1-based + account for adding the first packet
    idx2 = bisect(packets, cmp([[6]]), key=cmp) + 2

    return idx1 * idx2


def test_sample_part1():
    assert solve1(sample_input) == 13


def test_sample_part2():
    assert solve2(sample_input) == 140


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
