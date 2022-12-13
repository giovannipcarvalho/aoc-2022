import heapq

sample_input = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def parse_board(s: str) -> list[list[str]]:
    """
    Parse board string into list of character lists.
    """
    board = [list(line) for line in s.strip().splitlines()]
    return board


def neighbors(board: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns top, left, bottom and right neighbors of `pos` in the board.
    """
    i, j = pos
    rows, cols = len(board), len(board[0])
    n = []
    for i_, j_ in [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]:
        if i_ >= 0 and j_ >= 0 and i_ < rows and j_ < cols:
            n.append((i_, j_))
    return n


def can_move(board: list[list[str]], src: tuple[int, int], dst: tuple[int, int]):
    """
    Check if it is possible to go from `src` to `dst`.
    `dst` must be at most 1 higher than `src`.
    """
    h1 = board[src[0]][src[1]]
    h2 = board[dst[0]][dst[1]]

    if h1 == "S":
        h1 = "a"
    if h2 == "E":
        h2 = "z"

    return ord(h2) - ord(h1) <= 1


def seek(
    board: list[list[str]],
    start_pos: tuple[int, int],
    target_pos: tuple[int, int],
) -> int:
    """
    Find shortest path from `start_pos` to `target_pos` in `board` and return
    its distance.
    """
    seen = set()
    q = [(0, start_pos)]
    seen.add(start_pos)

    while len(q):
        distance, pos = heapq.heappop(q)

        if pos == target_pos:
            return distance

        for neigh in neighbors(board, pos):
            if can_move(board, pos, neigh) and neigh not in seen:
                heapq.heappush(q, (distance + 1, neigh))
                seen.add(neigh)

    return 999999


def solve1(s: str) -> int:
    """
    Find the shortest path from S to E and output its distance.
    """
    S = (0, 0)
    E = (0, 0)

    # find start and end coordinates
    for i, line in enumerate(s.strip().splitlines()):
        for j, letter in enumerate(line):
            if letter == "S":
                S = (i, j)
                continue
            if letter == "E":
                E = (i, j)
                continue

    board = parse_board(s)
    return seek(board=board, start_pos=S, target_pos=E)


def solve2(s: str) -> int:
    """
    Find the shortest path to E from any of the lowest-height starting points
    (height 'a').
    """
    E = (0, 0)
    S = []

    # find start and end coordinates
    for i, line in enumerate(s.strip().splitlines()):
        for j, letter in enumerate(line):
            if letter == "E":
                E = (i, j)
            if letter == "a":
                S.append((i, j))

    board = parse_board(s)
    return min(seek(board, s, E) for s in S)


def test_sample_part1():
    assert solve1(sample_input) == 31


def test_sample_part2():
    assert solve2(sample_input) == 29


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
