import textwrap

sample_input = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

expected_drawing = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....\
"""


def cpu(s: str) -> list[int]:
    values = [1]  # cycle 1

    for instruction in s.strip().splitlines():
        match instruction.split():
            case ["noop"]:
                values.append(values[-1])
            case ["addx", v]:
                values.append(values[-1])
                values.append(values[-1] + int(v))
            case _:
                raise ValueError(f"unexpected instruction {instruction}")

    return values


def solve1(s: str) -> int:
    """
    Computes signal strength at 20th, 60th, 100th, 140th, 180th and 220th cycles.

    Signal strength is defined as cycle_number * signal_value.
    """
    values = cpu(s)
    return sum(n * values[n - 1] for n in [20, 60, 100, 140, 180, 220])


def solve2(s: str):
    values = cpu(s)[:-1]  # ignore last cycle as values is written for the future
    pixels = []

    for idx, sprite_center in enumerate(values):
        row_pixel = idx % 40
        if abs(row_pixel - sprite_center) < 2:
            pixel = "#"  # lit
        else:
            pixel = "."  # off
        pixels.append(pixel)

    crt = "\n".join(textwrap.wrap("".join(pixels), 40))
    return crt


def test_sample_part1():
    assert solve1(sample_input) == 13140


def test_sample_part2():
    assert solve2(sample_input) == expected_drawing


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
    print("part 2:\n")
    print(solve2(s))
