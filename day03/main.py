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


sample_case = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_sample_case():
    assert sum_priorities_for_common_items(sample_case) == 157


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", sum_priorities_for_common_items(s))
