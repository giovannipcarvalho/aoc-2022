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


def compare(left, right) -> bool | None:
    match left, right:
        case int(), int():
            if left == right:
                return None
            else:
                return left < right
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case list(), list():
            for lt, rt in zip(left, right):
                if compare(lt, rt) is not None:
                    return compare(lt, rt)
            else:
                # did not find a deciding factor
                # `left` could either be same length, shorter or longer than `right`
                return compare(len(left), len(right))

    return None


def solve1(s: str) -> int:
    """
    Sum the indices (1-based) of the pairs that are in the right order.
    """
    pairs = []
    for pair in s.strip().split("\n\n"):
        pairs.append([eval(p) for p in pair.split("\n")])

    return sum(idx for idx, pair in enumerate(pairs, start=1) if compare(*pair))


def test_sample_part1():
    assert solve1(sample_input) == 13


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
