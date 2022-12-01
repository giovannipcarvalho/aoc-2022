def load_input(input_path: str) -> str:
    with open(input_path) as f:
        text = f.read().strip()
    return text


def parse_input(text: str) -> list[list[int]]:
    elfs = text.split("\n\n")
    elf_calories = [list(map(int, elf.split("\n"))) for elf in elfs]
    return elf_calories


def most_calories_in_a_single_elf(input: str) -> int:
    """Returns the most total calories held by a single elf."""
    # each elf is separated by blank lines
    elf_calories = parse_input(input)

    return max(sum(calories) for calories in elf_calories)


def total_calories_in_top_n_elves(input: str, n: int) -> int:
    """Sums total calories held by the top `n` elves holding the most calories"""
    elf_calories = parse_input(input)
    elf_calories_total = [sum(c) for c in elf_calories]
    elf_calories_total.sort(reverse=True)
    return sum(elf_calories_total[:n])


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
    input = load_input("input.txt")
    print("part 1:", most_calories_in_a_single_elf(input))
    print("part 2:", total_calories_in_top_n_elves(input, 3))
