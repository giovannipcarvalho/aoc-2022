def most_calories_in_a_single_elf(input: str) -> int:
    """Returns the most total calories held by a single elf."""
    # each elf is separated by blank lines
    elfs = input.split("\n\n")
    elf_calories = [elf.split("\n") for elf in elfs]
    elf_calories_int = [[int(c) for c in calories] for calories in elf_calories]

    return max(sum(calories) for calories in elf_calories_int)


def test_sample_input():
    sample_input = """1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000"""
    assert most_calories_in_a_single_elf(sample_input) == 24000


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().strip()
        print(most_calories_in_a_single_elf(input))
