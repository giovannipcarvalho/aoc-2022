import string

priority = dict(zip(string.ascii_letters, range(1, 53)))


def common_item_rucksack(sack: str) -> str:
    half = len(sack) // 2
    compartment1 = sack[:half]
    compartment2 = sack[half:]
    return "".join(set(compartment1) & set(compartment2))


def sum_priorities_for_common_items(s: str) -> int:
    total = 0
    for sack in s.splitlines():
        total += priority[common_item_rucksack(sack)]
    return total


def badge(group):
    x = set(group[0])
    for sack in group:
        x = x & set(sack)
    return "".join(x)


def sum_priorities_for_group_badges(s: str) -> int:
    sacks = s.splitlines()
    n = 3
    groups = [sacks[i : i + n] for i in range(0, len(sacks), n)]
    badges = [badge(group) for group in groups]
    return sum(priority[b] for b in badges)


sample_case = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

sample_case_part2 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_sample_case():
    assert sum_priorities_for_common_items(sample_case) == 157


def test_sammple_case_part2():
    assert sum_priorities_for_group_badges(sample_case_part2) == 70


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", sum_priorities_for_common_items(s))
    print("part 2:", sum_priorities_for_group_badges(s))
