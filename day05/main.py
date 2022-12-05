from copy import deepcopy

# remove the crates from input.txt XD
CRATES = {
    1: list("CFBLDPZS"),
    2: list("BWHPGVN"),
    3: list("GJBWF"),
    4: list("SCWLFNJG"),
    5: list("HSMPTLJW"),
    6: list("SFGWCB"),
    7: list("WBQMPTH"),
    8: list("TWSF"),
    9: list("RCN"),
}


def solve1(s: str) -> str:
    crates = deepcopy(CRATES)
    for line in s.splitlines():
        _, amount, _, origin, _, dest = line.split(" ")
        for _ in range(int(amount)):
            x = crates[int(origin)].pop(0)
            # move crates to the top of the stack
            crates[int(dest)].insert(0, x)
    return "".join([v[0] for k, v in crates.items()])


def solve2(s: str) -> str:
    crates = deepcopy(CRATES)
    for line in s.splitlines():
        _, amount, _, origin, _, dest = line.split(" ")
        for i in range(int(amount)):
            x = crates[int(origin)].pop(0)
            # move crates in chunks i.e. insert into the original order
            crates[int(dest)].insert(i, x)
    return "".join([v[0] for k, v in crates.items()])


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    print("part 1:", solve1(s))
    print("part 2:", solve2(s))
