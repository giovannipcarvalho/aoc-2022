import os.path
from collections import defaultdict
from typing import Iterable

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


def parents(path: str) -> Iterable[str]:
    """
    Returns a list of all parents for a path:
    e.g. '/a/b/c/d.txt'
        ['', 'a', 'a/b', 'a/b/c']

    The empty string is the root dir `/`.
    """
    parts = os.path.normpath(path).split(os.path.sep)
    for n in range(1, len(parts)):
        yield os.path.join(*parts[:n])


def traverse(s: str) -> list[tuple[str, int]]:
    """
    Traverse a sequence of commands and outputs to generate a list of file
    paths and sizes.
    """
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


def dir_sizes(files: list[tuple[str, int]]) -> dict[str, int]:
    """
    Computes directory sizes for all directories in a tree, given a list
    of all of its files.
    """
    sizes: dict[str, int] = defaultdict(int)
    for file, size in files:
        for parent in parents(file):
            sizes[parent] += size

    return sizes


def sum_directories_of_size_up_to(s, max_size=100000) -> int:
    """
    Sum the size of all directories of total size up to `max_size`.
    """
    sizes = dir_sizes(traverse(s))
    return sum(v for v in sizes.values() if v <= max_size)


def min_delete_size(s, desired_free_space=30000000, total_disk_size=70000000) -> int:
    """
    Find the smallest directory size that when deleted will achieve the desired
    free space.
    """
    sizes = dir_sizes(traverse(s))
    current_total_used = sizes[""]  # root is the empty str
    current_free_space = total_disk_size - current_total_used
    minimum_delete_size = desired_free_space - current_free_space
    for size in sorted(sizes.values()):
        if size >= minimum_delete_size:
            return size
    return 0


def test_sample_part1():
    assert sum_directories_of_size_up_to(sample_input) == 95437


def test_sample_part2():
    assert min_delete_size(sample_input) == 24933642


if __name__ == "__main__":
    s = open("input.txt").read()
    print("part 1:", sum_directories_of_size_up_to(s))
    print("part 2:", min_delete_size(s))
