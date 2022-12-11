import math
import operator
from collections import defaultdict
from collections import namedtuple
from typing import Iterable

sample_input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".rstrip()


def parse_items(line: str):
    return [int(x) for x in line.split(": ")[1].split(", ")]


def parse_operation(line: str):
    _OPS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    def fn(old):
        a, op, b = line.split("= ")[1].split()
        a = old if a == "old" else int(a)
        b = old if b == "old" else int(b)
        return _OPS[op](a, b)

    return fn


def parse_behavior(lines: list[str]):
    div = int(lines[0].split()[-1])
    case_true = int(lines[1].split()[-1])
    case_false = int(lines[2].split()[-1])

    def fn(worry: int) -> int:
        if worry % div == 0:
            return case_true
        else:
            return case_false

    return fn, div


Monkey = namedtuple("Monkey", ["items", "operation", "behavior", "div"])


def parse_monkey(s: str):
    """Parse a monkey behavior"""
    lines = s.splitlines()
    items = parse_items(lines[1])
    operation = parse_operation(lines[2])
    behavior, div = parse_behavior(lines[3:])

    return Monkey(items, operation, behavior, div)


def solve1(s: str) -> int:
    monkeys = {idx: parse_monkey(m) for idx, m in enumerate(s.split("\n\n"))}
    inspections: dict[int, int] = defaultdict(int)

    for round in range(20):
        for monkey_id, monkey in monkeys.items():
            while len(monkey.items):
                # worry level is the item value itself
                item = monkey.items.pop(0)

                # calculate new worry level
                item = monkey.operation(item)

                # score number of inspections
                inspections[monkey_id] += 1

                # chill
                item = math.floor(item / 3)

                # test who's getting thrown the item
                new_monkey = monkey.behavior(item)
                monkeys[new_monkey].items.append(item)

    # multiply the number of inspections of the two most active monkeys
    x = sorted(inspections.values(), reverse=True)
    return x[0] * x[1]


def prod(vals: Iterable[int | float]):
    """Product of a sequence"""
    result: int | float = 1
    for v in vals:
        result *= v
    return result


def solve2(s: str, rounds=10000) -> int:
    monkeys = {idx: parse_monkey(m) for idx, m in enumerate(s.split("\n\n"))}
    inspections: dict[int, int] = defaultdict(int)

    # new factor to reduce worry levels
    div = prod(m.div for m in monkeys.values())

    for round in range(rounds):
        for monkey_id, monkey in monkeys.items():
            while len(monkey.items):
                # worry level is the item value itself
                item = monkey.items.pop(0)

                # score number of inspections
                inspections[monkey_id] += 1

                # calculate new worry level
                item = monkey.operation(item)

                # chill
                item = item % div

                # test who's getting thrown the item
                new_monkey = monkey.behavior(item)

                monkeys[new_monkey].items.append(item)

    # multiply the number of inspections of the two most active monkeys
    x = sorted(inspections.values(), reverse=True)
    return x[0] * x[1]


def test_sample_part1():
    assert solve1(sample_input) == 10605


def test_sample_part2():
    assert solve2(sample_input) == 2713310158


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
