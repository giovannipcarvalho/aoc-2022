import operator


class array(tuple):
    def __add__(self, other):
        return self.__class__(map(operator.add, self, other))

    def __sub__(self, other):
        return self.__class__(map(operator.sub, self, other))

    def __abs__(self):
        return self.__class__(map(abs, self))

    def __eq__(self, other):
        return all(a == b for a, b in zip(self, other))

    def __lt__(self, other):
        return all(a < b for a, b in zip(self, other))

    def __str__(self):
        s = ", ".join(str(x) for x in self)
        return f"({s})"

    def __hash__(self):
        return hash(str(self))


def parse_command(command: str) -> tuple[array, int]:
    DIRECTION = {
        "R": array([0, +1]),
        "L": array([0, -1]),
        "U": array([-1, 0]),
        "D": array([+1, 0]),
    }
    direction, amount = command.split()
    return DIRECTION[direction], int(amount)


def is_adjacent(H: array, T: array) -> bool:
    """Check whether H and T are adjacent."""
    return max(abs(H - T)) <= 1


def clip(a: array, a_min=-1, a_max=1) -> array:
    """Clip values to at most -1, 1"""
    return array([min(a_max, max(v, a_min)) for v in a])


def make_adjacent(H: array, T: array) -> array:
    """Returns new T position to make it adjacent to H."""
    gradient = H - T
    return T + clip(gradient)
