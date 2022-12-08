sample_input = """\
30373
25512
65332
33549
35390
"""


def parse_trees(s: str) -> list[list[int]]:
    """Parses string into a list of list of ints with the height of each tree."""
    trees = [[int(x) for x in row] for row in s.strip().splitlines()]
    return trees


def tree_is_visible(trees, i, j) -> bool:
    """Check if tree i, j is visible in the trees"""
    m, n = len(trees), len(trees[0])

    if i == 0 or j == 0:
        return True

    if i == m - 1 or j == n - 1:
        return True

    height = trees[i][j]

    # find trees to the left, right, top and bottom of the tree i,j
    left = trees[i][:j]
    right = trees[i][j + 1 :]
    top = [row[j] for row in trees][:i]
    bottom = [row[j] for row in trees][i + 1 :]

    return any(
        [
            max(left) < height,  # visible from the left
            max(right) < height,  # visible from the right
            max(top) < height,  # visible from the top
            max(bottom) < height,  # visible from the right
        ]
    )


def visible_trees(s: str) -> int:
    """Count the total number of visible trees."""
    trees = parse_trees(s)
    total = 0
    m, n = len(trees), len(trees[0])
    for i in range(m):
        for j in range(n):
            total += tree_is_visible(trees, i, j)

    return total


def test_sample_part1():
    assert visible_trees(sample_input) == 21


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", visible_trees(s))
