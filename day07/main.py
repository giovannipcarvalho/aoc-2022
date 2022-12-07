import os.path
from collections import defaultdict

sample_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def parents(path: str):
    parts = os.path.normpath(path).split(os.path.sep)
    for n in range(1, len(parts)):
        yield os.path.join(*parts[:n])


def traverse(s: str):
    path = ""
    files = []
    for line in s.strip().splitlines():
        match line.split():
            case ["$", "cd", arg]:
                if arg == "/":
                    path = "/"
                elif arg == "..":
                    path = os.path.dirname(path)
                else:
                    path = os.path.join(path, arg)
            case ["$", "ls"]:
                pass
            case ["dir", *_]:
                pass
            case _:
                size, filename = line.split()
                files.append((os.path.join(path, filename), int(size)))

    return files


def dir_sizes(files: dict) -> dict[str, int]:
    sizes: dict[str, int] = defaultdict(int)
    for file, size in files:
        for parent in parents(file):
            sizes[parent] += size

    return sizes


def sum_directories_of_size_up_to(s, max_size=100000) -> int:
    sizes = dir_sizes(traverse(s))
    return sum(v for v in sizes.values() if v <= max_size)


def test_sample_part1():
    assert sum_directories_of_size_up_to(sample_input) == 95437


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", sum_directories_of_size_up_to(s))